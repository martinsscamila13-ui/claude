# Referência — IDs, links e estrutura

## Notion

**Modelo mestre (duplicar este):**
- Página: `3c6faf7b-8170-8194-9cd6-edbe177f9a3d` — https://app.notion.com/p/3c6faf7b817081949cd6edbe177f9a3d
- 🗺️ Jornada — db `01575f2a66d04b8c97ec21c7b5de4c2a` · ds `f926a7af-f8a7-4452-8b63-e11997d2c8b2`
- 🥁 Processo — db `8d94a73defa54ce69751c106019f3a64` · ds `a5c62434-49cf-43ae-9284-10d5ad497452`
- 🎥 Sessões & Gravações — db `96c604248af24b9b94f600a55bf97adb` · ds `484bbbaf-9adb-4e26-bb29-5088e5e4a27f`
- 💎 Patrimônio Valioso — db `cc46d015de9c49a1acdcab8c7100e579` · ds `534ff255-a63e-4327-9196-1e4a062c6a52`

**Exemplo pronto (Vanessa da Silva):** `3c6faf7b-8170-81c0-a259-c36c2e8269e5`
Use como referência de tom e de ficha preenchida.

## Estrutura da página

1. Hero (imagem) · 2. Colunas: foto + ferramentas + links | nome + ficha + dor/desejo
3. Callout de boas-vindas · 4. Índice · 5. **A nossa jornada** (galeria) + tabela do formato
6. **Plano de implementação** (Processo) · 7. **Sessões & gravações** · 8. **Patrimônio construído**
9. **Termômetro do ciclo** (tabela início/fim) · 10. **Glossário** (toggles) · 11. Assinatura

## Schemas

**🗺️ Jornada** — `Nome` TITLE, `Etapa` NUMBER, `Período` RICH_TEXT, `Status` SELECT(Não iniciada,
Em andamento, Concluída), `Foco da etapa` RICH_TEXT, `Capa` FILES. View Galeria ordenada por Etapa.
6 cards: Boas-vindas & Combinados (0) · Fase 1 Raio-X Operacional (1) · Fase 2 Extração
Comportamental Lucrativa (2) · Fase 3 Rotina Anti-Exaustão (3) · Fase 4 Patrimônio Valioso (4) ·
Sessões & Gravações (5).

**🥁 Processo** — `Nome` TITLE, `Fase` SELECT(Bem-vinda, Fase 1 — Raio-X Operacional, Fase 2 —
Extração Comportamental, Fase 3 — Rotina Anti-Exaustão, Fase 4 — Ativação de Patrimônio),
`Status` SELECT(Não iniciada, Em andamento, Dificuldade, Concluído), `Semana` SELECT(Antes de
começar, Semanas 1-3, Semanas 4-6, Semanas 7-9, Semanas 10-12), `Data` DATE, `Ferramenta`
RICH_TEXT, `Responsável` SELECT(<cliente>, Camila, Nós duas), `Evidência anexada` CHECKBOX.
Views: tabela + board "Por fase". 44 linhas.

**🎥 Sessões & Gravações** — `Nome` TITLE, `Encontro` NUMBER, `Data` DATE, `Fase` SELECT,
`Gravação` URL, `Principais decisões` RICH_TEXT, `Tarefas combinadas` RICH_TEXT, `Realizado`
CHECKBOX. 12 linhas (Encontro 1 a 12).

**💎 Patrimônio Valioso** — `Nome` TITLE, `Tipo` MULTI_SELECT(Processo documentado, Delegação,
Oferta / Produto, Autoridade & Conteúdo, Cultura e Equipe, Legado), `Status` SELECT(Ideia, Em
construção, Ativo), `Impacto no lucro` SELECT(Alto, Médio, Baixo), `Data` DATE, `Criado em`
CREATED_TIME. Começa vazio.

## As 4 fases (fonte: doc "Arquivo de Mentoria - Lucro Anti-Exaustao" + board do Trello)

| Fase | Semanas | Princípio | Ferramentas |
|---|---|---|---|
| 1 Raio-X Operacional | 1-3 | clareza antes da expansão | Diagnóstico Operacional · Mapa da Sobrecarga · Auditoria da Rotina · Registro da Rotina · Mapeamento de Gargalos · Roda da Empresária |
| 2 Extração Comportamental Lucrativa | 4-6 | liderança alinhada à performance | Teste MBTI · Mapeamento Comportamental Integrado · Perfil de Liderança · Análise da Energia Produtiva · Mapa da Alta Performance Sustentável |
| 3 Rotina Anti-Exaustão | 7-9 | estrutura leve para crescimento sustentável | Plano Anti-Exaustão · Prioridades Inteligentes · Gestão de Energia · Estrutura de Rotina Lucrativa · Protocolo de Disciplina Sustentável |
| 4 Patrimônio Valioso | 10-12 | empresa forte, vida leve, legado | Estrutura de Delegação · Plano de Expansão Saudável · Cultura de Equipe · Ativação de Liderança · Visão de Legado |

Dor central: reduzir o caos operacional. Desejo central: lucro na empresa sem exaustão da rotina.

> A Fase 4 ainda não existe no board do Trello — os cards do Notion foram derivados do método.
> Se a mentora validar as perguntas dessa fase, atualizar o modelo.

## Links das ferramentas (públicos para leitura, formato /copy)

- FASE 1 — https://docs.google.com/spreadsheets/d/1cR9ArFCeu3V8DchoLKkq90P5DDhNSyMETsob1k5jLVc/copy
- FASE 2 — https://docs.google.com/spreadsheets/d/19Fsgr6FaR6g1ABcjlBq_VAdB5AHU-Sd_h9v5eULpNpU/copy
- FASE 3 — https://docs.google.com/spreadsheets/d/1dwOuaXppdj3NLBbSBUsvzhyHrCr4sBa06Fq1cOjqFlQ/copy
- FASE 4 — https://docs.google.com/spreadsheets/d/1qx73yAeYnIjD-EoWhaome3frGnjp9Qz3ecWsnNLd_PU/copy
- Teste MBTI — https://www.16personalities.com/br/teste-de-personalidade
- Pasta do método no Drive — `1H46rJMQXbkfVdwgk3g-CMfCBvm51NWCT`

Antes de mandar um link novo para a cliente, confira a permissão com `get_file_permissions`
(precisa de `anyone: reader`).

## Canva — artes

Molde branco (base de todas): `DAHTQPxqm-4`
Prontas: Fase 1 `DAHTQHCvF1M` · Fase 2 `DAHTQKZGHSQ` · Fase 3 `DAHTQA9R9H4` ·
Fase 4 `DAHTQOmkfAw` · Sessões `DAHTQENLp9A` · Hero `DAHTQMFKFk8`

Estilo: fundo branco, título centralizado em itálico #1F1F1F, filete #C9C9C9 (140x1 em top 205),
assinatura "Lucro Anti-Exaustão®" itálica #8C8C8C. Formato 851x315.

**Para uma arte nova:**
1. `copy-design` do molde `DAHTQPxqm-4`
2. `read-design` com `open_transaction: true` e `filter.fields: ["design_metadata"]` → transaction_id
3. `edit-design` — locators (iguais em toda cópia):
   - página `PBXjYHw0WjpVkXsM`
   - título `PBXjYHw0WjpVkXsM-LBPpzCBNcSDYVnzv`
   - assinatura `PBXjYHw0WjpVkXsM-LB5mkqlmFs4ykrfj`
   - operações: `replace_text` + `format_text` (italic, center, #1F1F1F) + `position_element` (top 60) + `update_title`
   - corpo por tamanho do título: até 18 caracteres → 46 · 19 a 21 → 38 · 22+ → 34
4. `edit-design` com `finalize: "commit"` (sem operations)
5. `get-export-formats` → `export-design` PNG (só `type` e `export_quality`; width/lossless dão erro)
6. `notion-create-attachment` com a URL do export → devolve `file-upload://<id>`
7. `notion-update-page` `insert_content` no início do card:
   `<image src="file-upload://<id>">Legenda</image>`

Cada `file-upload` serve para uma inserção só — para usar a mesma arte em duas páginas, faça dois
attachments a partir da mesma URL de export.
