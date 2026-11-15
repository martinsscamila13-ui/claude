#!/usr/bin/env python3
"""
Organiza e converte as aulas do curso Alicerce (.mov -> .mp4) usando o mapa-aulas.csv.

Uso:
  python3 organizar-e-converter-videos.py --origem "/caminho/videos-baixados-do-drive" --destino "/caminho/Alicerce-videos-final"
  python3 organizar-e-converter-videos.py --origem ... --destino ... --simular     # só mostra o que faria

Requisitos: ffmpeg instalado (macOS: `brew install ffmpeg`; Windows: `winget install ffmpeg`).

O que faz:
  1. Lê ferramentas/mapa-aulas.csv.
  2. Procura cada arquivo original (ex.: "Aula 12 ✅.mov") dentro da pasta --origem (inclusive subpastas).
  3. Converte para MP4 H.264 + AAC, até 1080p, com "faststart" (começa a tocar antes de baixar tudo).
  4. Salva em --destino/<módulo>/<arquivo_final>.mp4.
  5. Gera um relatório (relatorio-videos.csv) com: encontrado?, duração, tamanho antes/depois, status.
Nunca apaga nem altera os arquivos originais.
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MAPA = AQUI / "mapa-aulas.csv"
EXTS = {".mov", ".mp4", ".m4v", ".qt", ""}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("✅", "").strip().lower()
    return " ".join(s.split())


def indexar(origem: Path):
    idx = {}
    for p in origem.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            idx.setdefault(norm(p.stem), []).append(p)
            idx.setdefault(norm(p.name), []).append(p)
    return idx


def duracao(p: Path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(p)],
            capture_output=True, text=True, check=True,
        ).stdout
        return round(float(json.loads(out)["format"]["duration"]), 1)
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--origem", required=True)
    ap.add_argument("--destino", required=True)
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--crf", default="23", help="qualidade (18=alta, 23=padrão, 28=menor)")
    a = ap.parse_args()

    if not a.simular and not shutil.which("ffmpeg"):
        sys.exit("ffmpeg não encontrado. Instale (macOS: brew install ffmpeg) e rode de novo.")

    origem, destino = Path(a.origem).expanduser(), Path(a.destino).expanduser()
    idx = indexar(origem)
    linhas = list(csv.DictReader(open(MAPA, encoding="utf-8")))
    relatorio = []

    for l in linhas:
        alvo = destino / l["modulo"] / l["arquivo_final"]
        achados = idx.get(norm(l["arquivo_original_drive"]), [])
        reg = {"modulo": l["modulo"], "ordem": l["ordem"], "titulo": l["titulo_final"],
               "original": l["arquivo_original_drive"], "final": str(alvo), "status_mapa": l["status"]}
        if not achados:
            reg.update(encontrado="NÃO", acao="FALTA — localizar/gravar ou confirmar")
            relatorio.append(reg)
            print(f"[FALTA]   {l['ordem']} {l['titulo_final']}  ({l['arquivo_original_drive']})")
            continue
        src = achados[0]
        reg.update(encontrado="SIM", origem_path=str(src),
                   mb_antes=round(src.stat().st_size / 1e6, 1), duracao_s=duracao(src))
        if a.simular:
            reg["acao"] = "simulado"
            print(f"[SIMULAR] {src.name} -> {alvo}")
        else:
            alvo.parent.mkdir(parents=True, exist_ok=True)
            cmd = ["ffmpeg", "-y", "-i", str(src),
                   "-vf", "scale='min(1920,iw)':-2",
                   "-c:v", "libx264", "-preset", "medium", "-crf", a.crf,
                   "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(alvo)]
            print(f"[CONVERTENDO] {src.name} -> {alvo.name}")
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode == 0:
                reg.update(acao="convertido", mb_depois=round(alvo.stat().st_size / 1e6, 1))
            else:
                reg.update(acao="ERRO ffmpeg", erro=r.stderr[-400:])
                print(f"   ERRO: {r.stderr[-300:]}")
        relatorio.append(reg)

    destino.mkdir(parents=True, exist_ok=True)
    rel = destino / "relatorio-videos.csv"
    campos = sorted({k for r in relatorio for k in r})
    with open(rel, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(relatorio)
    faltas = [r for r in relatorio if r.get("encontrado") == "NÃO"]
    curtos = [r for r in relatorio if r.get("duracao_s") and r["duracao_s"] < 60]
    print(f"\nRelatório: {rel}")
    print(f"Aulas no mapa: {len(relatorio)} | faltando: {len(faltas)} | com menos de 1 min (conferir): {len(curtos)}")


if __name__ == "__main__":
    main()
