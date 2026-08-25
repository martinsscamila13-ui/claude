---
name: notion-cliente
description: Cria no Notion o espaço de acompanhamento de uma cliente nova da mentoria (Método Lucro Anti-Exaustão® / Programa de Aceleração / Mentoria O MAPA), a partir do modelo mestre — pronto para compartilhar com ela. Use quando pedirem "criar o Notion da [nome]", "nova cliente/mentorada", "onboarding da cliente no Notion", "duplicar o modelo para a fulana". A skill coleta os dados que faltam (perguntando ou lendo contrato/formulário no Google Drive), duplica o modelo, preenche a ficha, ajusta a jornada e entrega o link para compartilhar.
---

# Notion de cliente nova

Monta o espaço da cliente em ~5 minutos, com a mesma estrutura do modelo: ficha, galeria da
jornada em 4 fases, plano de implementação com 44 etapas, sessões e patrimônio.

## 1. Descobrir o que já se sabe (antes de perguntar)

Nunca pergunte o que dá para achar sozinho. Nesta ordem:

1. **Google Drive** — procure o contrato e materiais da cliente:
   - `search_files` com `title contains '<primeiro nome>'` e depois `fullText contains '<nome>'`
   - o contrato costuma se chamar `CONTRATO MENTORIA ... - <NOME>.pdf` e traz: nome completo,
     cidade, produto contratado, nº de encontros, duração e valor/forma de pagamento
   - leia com `read_file_content`
2. **Notion** — `notion-search` pelo nome, para não criar página duplicada
3. **Trello** — `trelloSearch` (`search_boards`/`search_cards`) pelo nome; se houver quadro dela,
   guarde a URL. Quadro em workspace não conectado retorna erro de permissão: peça o PDF do
   quadro (Menu → Mais → Imprimir e exportar) ou o link, e siga sem ele.

Se o usuário anexar um arquivo (PDF/JSON/print), leia antes de perguntar qualquer coisa.

## 2. Perguntar só o que faltou

Use `AskUserQuestion`, agrupando em no máximo 4 perguntas por rodada. Campos da ficha:

| Campo | Como preencher |
|---|---|
| Nome completo | contrato |
| Programa | Programa de Aceleração · Mentoria O MAPA · Comunidade Impulso · Consultoria |
| Formato | nº de encontros + duração (contrato) |
| Negócio / Nicho | perguntar |
| Faturamento atual | perguntar |
| Tamanho da equipe | perguntar |
| Meta de faturamento do ciclo | perguntar |
| Instagram | perguntar (o @ costuma indicar o nicho) |
| Cidade | contrato |
| Contrato assinado / Início / Fim | contrato + agenda |
| Investimento | contrato (valor + forma de pagamento) |

Dor central, desejo central e transformação são fixos do método — já vêm preenchidos no modelo,
só confirme se cabem para essa cliente.

**Nunca copie CPF, endereço, RG ou dados bancários para o Notion.** A página vai ser
compartilhada com a cliente; a ficha é comercial, não cadastral.

## 3. Duplicar o modelo

Use `notion-duplicate-page` com a página mestre (ID em `reference.md`). A duplicação traz junto os
4 bancos, os 6 cards da galeria com as artes, as 44 etapas do Processo e os 12 encontros.

Depois:
1. `notion-update-page` (`update_properties`) → título = nome da cliente
2. `notion-update-page` (`update_content`) → substitua o callout da ficha pelos dados reais e
   apague o callout "Como usar este modelo" (ele é instrução para a mentora, não para a cliente)
3. Troque "NOME DA CLIENTE" pelo nome no heading da coluna direita
4. Ajuste a linguagem: o modelo já fala "você" com a cliente — mantenha assim
5. Se houver quadro no Trello, cole o link no callout de links

Se a duplicação falhar, recrie do zero seguindo `reference.md` (schemas + conteúdo das 4 fases).

## 4. Ajustar a jornada às datas dela

- Card **Boas-vindas & Combinados** → Status `Em andamento`
- Se as datas dos encontros já estiverem fechadas, preencha `Data` nas linhas de **Sessões &
  Gravações** e marque `Calendário da jornada` como `Concluído` no Processo
- Se a cliente já tiver preenchido alguma ferramenta, marque o Status correspondente

## 5. Capas dos cards

As capas vêm prontas na duplicação: a propriedade **Capa** de cada card aponta para um PNG
hospedado no repositório público `martinsscamila13-ui/claude` (pasta `artes/lucro-anti-exaustao/`),
e a view Galeria já usa `COVER "Capa"`. Não precisa refazer nada.

Se a duplicação não trouxer as capas, refaça em duas chamadas:
1. `notion-update-page` (`update_properties`) com
   `{"Capa": ["https://raw.githubusercontent.com/martinsscamila13-ui/claude/claude/notion-camila-structure-dtwrok/artes/lucro-anti-exaustao/<arte>.png"]}`
   (arquivos: `boas-vindas`, `fase1`, `fase2`, `fase3`, `fase4`, `sessoes`)
2. `notion-update-view` com `COVER "Capa" SIZE medium ASPECT cover`

Para uma arte nova (hero personalizado, por exemplo), clone o molde no Canva, troque o texto e
publique o PNG no repositório — passo a passo em `reference.md`.

## 6. Entregar

Informe ao usuário, nesta ordem:

1. O link da página da cliente
2. **O passo manual que a API não faz** — **compartilhar**: abrir a página → Compartilhar →
   convidar o e-mail da cliente (ou "Publicar na web" e mandar o link)
3. O que ficou em branco na ficha e por quê

## Erros conhecidos

- **Capa de card por API**: só funciona com URL externa **permanente** na propriedade Files —
  daí as artes ficarem no repositório público. Não aceita `file-upload://` nem link do Canva
  (que expira em horas). O `cover` da página tem a mesma restrição.
- **Domínios do Canva bloqueados** neste ambiente: não é possível baixar/ver o PNG exportado,
  mas o Notion baixa server-side via `notion-create-attachment` com `source_url`. Os thumbnails
  retornados pelo `edit-design` são visíveis — use-os para conferir a arte.
- **Fonte no Canva**: a API não troca família tipográfica, só itálico/corpo/cor/posição.
