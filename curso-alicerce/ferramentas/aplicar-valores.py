#!/usr/bin/env python3
"""
Preenche os campos (placeholders) de todos os arquivos do kit e gera uma cópia pronta em ../publicar/.
Os arquivos originais NÃO são alterados.

Uso:
  1. Copie valores.exemplo.json para valores.json e preencha.
  2. python3 aplicar-valores.py
  3. Confira o relatório: ele lista qualquer campo que ainda ficou sem valor.
"""
import json
import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent                      # pasta curso-alicerce
SAIDA = RAIZ / "publicar"
VALORES = AQUI / "valores.json"
TEXTO = {".html", ".md", ".txt", ".csv", ".json"}
IGNORAR = {"publicar", "ferramentas", ".git"}
# padrões de campo usados no kit
PADRAO = re.compile(r"\b(LINK_[A-Z_]+|FOTO_[A-Z_]+|IMAGEM_[A-Z_]+|MOCKUP_[A-Z_]+|PRAZO_ACESSO|CUPOM_[A-Z_]+|QUIZ_URL|FORM_ACTION_URL|INSTAGRAM_[A-Z_]+|EMAIL_[A-Z_]+|WHATSAPP_[A-Z_]+)\b")


def main():
    if not VALORES.exists():
        sys.exit(f"Crie {VALORES.name} a partir de valores.exemplo.json antes de rodar.")
    valores = {k: v for k, v in json.load(open(VALORES, encoding="utf-8")).items()
               if not k.startswith("_") and v not in ("", None)}
    # apelidos usados pelos arquivos de guerrilha para o mesmo link do quiz
    if "QUIZ_URL" in valores:
        valores.setdefault("LINK_QUIZ", valores["QUIZ_URL"])
        valores.setdefault("LINK_QUIZ_PUBLICO", valores["QUIZ_URL"])
    if SAIDA.exists():
        shutil.rmtree(SAIDA)
    pendentes = {}
    for src in RAIZ.rglob("*"):
        rel = src.relative_to(RAIZ)
        if any(p in IGNORAR for p in rel.parts) or src.is_dir():
            continue
        dst = SAIDA / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() in TEXTO:
            txt = src.read_text(encoding="utf-8")
            # chaves mais longas primeiro, para LINK_CHECKOUT_COM_CUPOM não ser cortado por LINK_CHECKOUT
            for k in sorted(valores, key=len, reverse=True):
                txt = re.sub(rf"\b{re.escape(k)}\b", valores[k], txt)
            for m in set(PADRAO.findall(txt)):
                pendentes.setdefault(m, set()).add(str(rel))
            dst.write_text(txt, encoding="utf-8")
        else:
            shutil.copy2(src, dst)
    print(f"Cópia preenchida gerada em: {SAIDA}")
    if pendentes:
        print("\nCAMPOS AINDA SEM VALOR (preencha em valores.json e rode de novo):")
        for k, arqs in sorted(pendentes.items()):
            print(f"  {k}: {len(arqs)} arquivo(s) — ex.: {sorted(arqs)[0]}")
    else:
        print("Nenhum campo pendente.")


if __name__ == "__main__":
    main()
