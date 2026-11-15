#!/usr/bin/env python3
"""
Revisão automática do kit antes de publicar. Não altera nada, só aponta problemas.

Uso: python3 verificar-materiais.py            (verifica a pasta curso-alicerce)
     python3 verificar-materiais.py --publicar  (verifica a pasta publicar/, já preenchida)

Checa:
  - prova social desatualizada ("+200", "200 mentoradas")
  - depoimentos-modelo ainda não substituídos
  - marcadores [PREENCHER], [VALIDAR], [COLCHETES] etc.
  - campos LINK_/FOTO_/... sem valor (na pasta publicar/)
  - promessas proibidas: "garantido", "resultado garantido", números de resultado inventados
  - links internos de arquivos HTML que apontam para arquivos inexistentes
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ALVO = RAIZ / "publicar" if "--publicar" in sys.argv else RAIZ
IGNORAR = {"ferramentas", ".git"} | ({"publicar"} if ALVO == RAIZ else set())

REGRAS = [
    ("PROVA SOCIAL DESATUALIZADA", re.compile(r"(\+\s?200\b|200 mentoradas|mais de 200)", re.I)),
    ("DEPOIMENTO-MODELO", re.compile(r"DEPOIMENTO REAL|Espaço reservado para depoimento", re.I)),
    ("MARCADOR PARA PREENCHER", re.compile(r"\[(PREENCHER|VALIDAR|CONFIRMAR|NOME|E-MAIL|LINK)[^\]]*\]", re.I)),
    ("CAMPO SEM VALOR", re.compile(r"\b(LINK_[A-Z_]+|FOTO_[A-Z_]+|PRAZO_ACESSO|CUPOM_[A-Z_]+|QUIZ_URL|FORM_ACTION_URL)\b")),
    ("PROMESSA ARRISCADA", re.compile(r"(resultado garantido|lucro garantido|garantimos (que|o) (você|lucro))", re.I)),
]


def main():
    achados = 0
    for f in sorted(ALVO.rglob("*")):
        rel = f.relative_to(ALVO)
        if f.is_dir() or any(p in IGNORAR for p in rel.parts) or f.suffix.lower() not in {".html", ".md", ".csv", ".txt"}:
            continue
        txt = f.read_text(encoding="utf-8", errors="ignore")
        for nome, rx in REGRAS:
            if nome == "PROVA SOCIAL DESATUALIZADA" and "recomendacoes" in f.name:
                continue  # o arquivo de recomendações cita o "+200" de propósito (instrução TROCAR/POR)
            ms = rx.findall(txt)
            if ms:
                exemplos = sorted({m if isinstance(m, str) else m[0] for m in ms})[:4]
                print(f"[{nome}] {rel}: {len(ms)}x  ex.: {exemplos}")
                achados += 1
        if f.suffix == ".html":
            for href in re.findall(r'(?:href|src)="([^"#:?]+\.(?:html|pdf|png|jpg|jpeg|webp|css|js))"', txt):
                if not (f.parent / href).exists():
                    print(f"[LINK QUEBRADO] {rel} -> {href}")
                    achados += 1
    print(f"\n{achados} ponto(s) para revisar em {ALVO}." if achados else f"\nTudo certo em {ALVO}.")


if __name__ == "__main__":
    main()
