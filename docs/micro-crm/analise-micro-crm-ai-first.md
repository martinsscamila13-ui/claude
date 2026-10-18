# Micro-CRM AI-first: análise e arquitetura recomendada

> Para: Camila Martins Finger (mentorias Método Lucro Anti-Exaustão®, Programa de Aceleração, O MAPA)
> Decisões (18/10): WhatsApp Business · Instagram profissional · painel no Grok Bot · Galaxy Tab S7 (Android) · WhatsApp direto na Meta, sem BSP.
> Guia de implantação passo a passo: artefato "Micro-CRM da Camila". Runbook do WhatsApp: [`whatsapp-meta-direto.md`](whatsapp-meta-direto.md).
> Data da pesquisa: 18/10/2026. Preços e recursos de terceiros mudam rápido: confirme nos links antes de contratar.

---

## 1. Resumo executivo

1. **O Grok Bot não recebe mensagens, mas é forte como "gerente comercial".** Ele roda num computador
   persistente na nuvem e cumpre rotinas agendadas. Tem conectores para Gmail, Google Calendar,
   Drive/Docs/Sheets e Notion, aceita **servidores MCP próprios** e gera documentos e planilhas.
   O app dele roda no Android (Galaxy Tab S7), com voz. Por outro lado, a documentação não traz nenhuma integração com
   WhatsApp, Instagram ou Telegram, não há webhook de entrada nem processo servidor, e ele não entra
   em chamada de vídeo. Por isso ele fica com a **análise e a rotina**, e a **coleta** fica com outro
   componente.
2. **A coleta tem que ser feita por vias oficiais.** WhatsApp via *Coexistence* (você continua usando
   o app WhatsApp Business no celular/tablet, e cada mensagem recebida ou enviada chega por webhook);
   Instagram via *Instagram API with Instagram Login* (webhook de DMs). Quem recebe é o **n8n**.
3. **O "CRM sem interface" fica no Notion, que você já usa.** Um banco de dados de Leads com
   visualização em quadro é o kanban. O Grok Bot lê e escreve nele pelo conector.
4. **Para o Google Meet, use um bot que entra na reunião como participante** (Recall.ai ou Meeting
   BaaS, por volta de US$ 0,50–0,70 por reunião). Ele funciona com você no app do Meet no tablet. O
   copiloto ao vivo da tecpet (extensão do Chrome) **não roda no tablet**, mas quase todo o desenho
   dele pode ser reaproveitado: playbook tirado de dados reais, três camadas de decisão, gravação
   conservadora no CRM e cliente achado pelo link do Meet (seção 4).
5. **Arquitetura:** `WhatsApp/Instagram/Meet → n8n (coleta + regras fixas) → Notion (CRM) ⇄ Grok Bot
   (análise, briefings, follow-ups, preparação e pós-reunião)`. Nessa versão, você conversa com o CRM
   **pelo app do Grok Bot no Galaxy Tab S7**. O Telegram fica como alternativa sem assinatura.

---

## 2. O que é um CRM AI-first (e o que o diferencia)

Um CRM tradicional depende de alguém digitar dados. Um CRM AI-first parte do princípio inverso:
**a conversa é a fonte da verdade, e o CRM é uma leitura estruturada dela.**

| Princípio | O que significa no seu caso |
|---|---|
| **Captura passiva** ("zero data entry") | Nenhum lead é cadastrado à mão: a primeira mensagem no WhatsApp ou na DM cria o registro. |
| **Extração estruturada** | A LLM lê a conversa e preenche campos fixos (nicho, faturamento, dor, objeção, interesse em qual programa), sempre num esquema JSON validado e nunca em texto livre. |
| **Resolução de identidade** | A mesma pessoa no Instagram (@) e no WhatsApp (telefone) vira **um** lead. A LLM sugere a junção, você confirma. |
| **Memória por contato** | Cada lead tem um resumo vivo ("onde paramos") que é reescrito a cada interação. |
| **Próxima melhor ação** | O sistema não só registra, mas diz o que fazer: "a Ana pediu o valor há 3 dias e você não respondeu". |
| **Regras de cadência** | Follow-ups gerados por regra (D+1, D+3, D+7…) e pausados automaticamente quando a lead responde. |
| **Humano no circuito** | A IA **nunca envia** mensagem para cliente. Ela rascunha e você envia. Mudanças sensíveis (Ganho/Perdido) pedem a sua confirmação. |
| **Rastreabilidade** | Todo campo preenchido pela IA guarda a mensagem de origem (data + trecho), para você auditar. |
| **Consulta em linguagem natural** | "Quem está em proposta há mais de 7 dias?" pelo Telegram. |

### Panorama do mercado (2026)

| Categoria | Exemplos | Pontos fortes | Por que não resolvem bem o seu caso |
|---|---|---|---|
| CRMs AI-native B2B | Attio, Day.ai, Lightfield, Clarify | Captura automática de e-mail, agenda e reuniões; modelo de dados flexível | Pensados para e-mail e vendas B2B em inglês; o WhatsApp entra só por conectores (Zapier etc.) e o Instagram quase não aparece |
| CRMs de mensageria | Kommo; no Brasil, ferramentas como RD Station CRM, Chatwoot (open source) e similares | WhatsApp e Instagram nativos, kanban pronto, IA para resumo e sugestão de resposta | A IA ajuda a responder, mas não *preenche* o CRM de forma inteligente. Em geral exigem trocar o seu WhatsApp para dentro da plataforma, e as mensalidades são por usuário |
| CRMs de contatos leves | folk | Importa conversas do WhatsApp para o pipeline (segundo o próprio fornecedor) | É log de mensagens, não extração de campos |
| **DIY com agente (recomendado)** | n8n + LLM + Notion + Telegram | Exatamente as suas regras e os seus estágios, sem interface nova, custo baixo | Exige montar uma vez (o roteiro está abaixo) |

Conclusão: para uma operação de uma pessoa, com venda consultiva de mentoria e canais WhatsApp + Instagram,
**o diferencial AI-first está na camada de extração e follow-up**, e nenhum produto pronto
faz isso bem em português sobre WhatsApp pessoal. Montar o seu sai mais barato e encaixa melhor.

---

## 3. Grok Bot: pesquisa aprofundada

Fontes: a documentação oficial (overview, FAQ, rotinas, computador e apps, bots, arquivos, notificações,
mobile, team bots, aprovações, @bot no X, planos no Cursor), o anúncio da xAI e análises independentes
(Flavio Copes, Vellum, Composio, RohitAI, AlphaSignal, Jay Mount, Agent Finder). Links no fim.

> **Nível de evidência:** o produto está em **beta desde 11/08/2026**. Não encontrei nenhum teste
> independente, feito na prática, de Grok Bot com CRM. As análises são leitura de documentação ou
> relatos isolados, e as fontes discordam sobre preços. Trate o que segue como "documentado", não
> como "comprovado".

### 3.1 O que é

Agente da xAI, operado junto com o Cursor. Cada **Bot** é um "colega de IA" com nome, função e memória
própria. Todos os Bots da sua conta compartilham **um computador na nuvem** (navegador, terminal e
arquivos em `/workspace`) que continua trabalhando com o app fechado. Você configura **conversando**
("Setup is a message, not a workflow builder"), por texto, ditado ou chat de voz. Quando um processo
dá certo, você pede para salvá-lo como **skill** e agendá-lo como **rotina**. Uma skill também pode ser
ensinada **gravando você fazendo a tarefa no navegador** (até 10 min).

### 3.2 Capacidades relevantes para o seu CRM

| Capacidade | O que a documentação diz | Uso no seu caso |
|---|---|---|
| **Rotinas agendadas** | Até 50 por Bot, intervalo mínimo de 5 min, fuso configurável. Cada execução consome uso, e uma rotina a cada 15 min roda 96×/dia | Briefing 7h30, varredura de follow-ups a cada 1–2h, relatório de domingo |
| **Gatilhos por evento** | Documentados: mensagem no Slack e eventos do GitHub. Segundo a AlphaSignal (não confirmado na doc), também **e-mail que chega a um alias** (`voce+crm@…`) | **Gancho importante:** o n8n pode mandar um e-mail para o alias quando uma conversa nova fechar, e esse e-mail dispara a rotina do Bot. Validar no beta |
| **Conectores** | Citados em fontes diferentes: Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Notion, Outlook/Teams, Salesforce, Slack, Trello, X, Stripe, Plaid… Há um marketplace aberto a terceiros | Notion (CRM), Calendar (reuniões), Gmail (propostas e contratos), Drive (contratos e transcrições), Sheets (relatórios) |
| **MCP próprio** | "Custom MCP server, Remote HTTPS" (precisa estar acessível publicamente). Composio é um plugin com mais de 1.000 apps | O **n8n expõe o seu CRM como ferramentas MCP**: `conversas_novas`, `buscar_lead`, `atualizar_lead`, `criar_atividade`. Mais confiável que clicar em telas |
| **Uso de navegador** | Para sites sem conector. Mais frágil: CAPTCHAs, sessões que expiram, sites que bloqueiam IP de nuvem, ação que "parece feita" sem ter sido | Pesquisa de leads (Instagram público, site). **Evitar** WhatsApp Web |
| **Terminal** | Existe no computador da nuvem | Scripts de análise pontuais. A doc **não** prevê servidor ou ouvinte rodando |
| **Arquivos de saída** | Documento com fontes, planilha com fórmulas, apresentação com notas, pasta com prints. Anexos de até 25 MB (áudio incluído) | Relatório semanal, análise de objeções, proposta personalizada em rascunho |
| **Memória** | Preferências, papel e resumo de trabalhos anteriores, por Bot | Ele aprende os seus estágios, o seu tom e as suas regras |
| **Vários Bots** | Até 6 Bots num grupo, um passando trabalho ao outro | Ex.: "Pesquisadora" + "Gerente comercial" (ver 3.4) |
| **App Android (Tab S7)** | Android 9+, ditado, chat de voz, memo de voz do Bot, foto e arquivos, aprovações, notificação push quando termina ou precisa de você. Editar rotinas só pelo desktop | É a sua "interface" do CRM |
| **Envio** | E-mail e Slack com cartão "Enviar / Descartar". **Nada de WhatsApp** | Follow-ups ficam como rascunho para você copiar |
| **Aprovações** | Regras "Pergunte antes" (sempre vencem) e "Permita automaticamente" (com revisão por modelo), "Take over" para senhas e 2FA, "Stop now" | "Pergunte antes" para enviar, apagar, mudar estágio para Ganho/Perdido |
| **Reuniões de vídeo** | ❌ Não entra. Só faz chat de voz com você | O bot do Meet tem que ser outro (Recall) |
| **Telegram / WhatsApp / Instagram / webhook** | ❌ Não documentados. A Vellum afirma: "no reach through email, Slack, Telegram, or phone" | Coleta via n8n |

### 3.3 Limites e riscos

- **Não determinístico:** o Bot planeja cada execução do zero. "Na segunda ele pula o contato que já
  está na cadência; na terça, com uma visão um pouco diferente do CRM, talvez não" (Jay Mount).
  ➜ **Regras com data e estágio ficam no n8n (código fixo). O Bot fica com o julgamento.**
- **Um computador para todos os Bots:** os logins e arquivos são compartilhados. Um Bot não é
  fronteira de segurança, e uma página com *prompt injection* lida por um Bot pode afetar outro
  (RohitAI: "one blast radius"). ➜ Não dê ao Bot acesso a banco/financeiro na mesma conta do CRM.
- **Privacidade:** exige armazenamento na nuvem do Cursor, as gravações de ações ficam 90 dias e a
  xAI não publica o prazo de retenção da memória. ➜ Leve **resumos** ao Bot, não o histórico
  bruto das clientes (LGPD).
- **Uso semanal:** quem roda muitas tarefas relata travar no meio quando o limite semanal acaba
  (Composio). ➜ Rotinas espaçadas e enxutas.
- **Beta:** recursos e nomes mudam toda semana.

### 3.4 Preço (as fontes divergem)

O acesso vem incluso no Cursor Pro (~US$ 20/mês), Pro+ (~US$ 60), Ultra (~US$ 200) e Teams (US$ 40 ou 120 por
pessoa), e dá para ligar uma assinatura SuperGrok (~US$ 30) / Plus / Heavy ou X Premium+. O uso do Bot é
**semanal e separado** do uso do chat, com consumo extra sob demanda opcional. Há um teste grátis com
crédito de 7 dias. Os valores vêm de blogs de consultoria (set/2026), e a xAI não publica preço
unitário. ➜ Para começar, o **plano mais barato com teste** basta: o volume de uma mentora é pequeno.

### 3.5 Desenho com Grok Bot: os "Bots" da Camila

| Bot | Função | Rotinas e gatilhos | Ferramentas |
|---|---|---|---|
| **Gerente Comercial** (principal) | Mantém o pipeline vivo | 7h30 briefing do dia · a cada 2h (8h–20h) processa conversas novas · domingo 18h relatório | MCP do CRM (n8n), Notion, Calendar, Gmail |
| **Preparadora de Reuniões** | Antes de cada call: ficha da lead, dores, histórico, roteiro de diagnóstico personalizado. Depois: resumo, próximos passos, rascunho de proposta | 1h antes de cada evento com link do Meet · gatilho por e-mail quando a transcrição chega | Calendar, Drive (transcrições), Notion |
| **Pesquisadora** (opcional) | Enriquece leads novos: nicho, porte, presença digital | Sob demanda ("pesquisa a @fulana") | Navegador (Instagram e site públicos) |

Instrução inicial para o Bot principal (cole no chat dele):

> Você é a gerente comercial da Camila Martins Finger (mentorias Método Lucro Anti-Exaustão®,
> Programa de Aceleração, O MAPA, Comunidade Impulso). O CRM fica no Notion, banco "Leads",
> com os estágios [lista da seção 6]. Use as ferramentas do MCP "crm-camila" para ler as conversas novas.
> Para cada lead: atualize o resumo vivo, sugira o estágio com o motivo e a evidência (trecho e data),
> crie uma Atividade de follow-up com um rascunho de mensagem no tom da Camila. **Nunca envie
> mensagem para ninguém.** Mudanças para Ganho/Perdido ou para trás: pergunte antes. Às 7h30
> me mande: follow-ups de hoje, calls de hoje com resumo e leads quentes sem resposta há mais de 24h.

### 3.6 O que **não** fazer com o Grok Bot

- Ler o WhatsApp Web pelo navegador do Bot: viola os termos do WhatsApp, a sessão cai e o
  histórico das clientes vai para a nuvem de terceiros.
- Deixar o Bot **calcular datas de follow-up ou mover estágios sozinho** sem regra fixa por trás,
  por causa da variação de uma execução para outra.
- Usar o Bot como **coach ao vivo** durante a call: ele é um agente que leva de segundos a minutos,
  e o coaching ao vivo pede respostas em menos de 10 s (seção 4).
- Usar o mesmo computador do Bot para logins financeiros.

### 3.7 Alternativas não oficiais

O projeto da comunidade [grok-telegram-bot](https://github.com/artickc/grok-telegram-bot) controla o
*Grok Build CLI* (programação) pelo Telegram, **não** o Grok Bot. A API do Grok (modelos 4.x, com
function calling e MCP remoto) pode ser o "cérebro" do n8n sem o Grok Bot.

---

## 4. O copiloto da tecpet: o que dá para trazer para a Camila

### 4.1 O que ele é (resumo)

Extensão do Chrome que **ouve a demo no Google Meet** (captura de áudio WebRTC + reconhecimento de
voz do Chrome), **coacha ao vivo** (perguntas SPIN, objeções, concorrentes, aviso de monólogo,
roteiro 45+15), **preenche a apresentação comercial** e no fim **grava a demo no Bitrix24**. A
infraestrutura é n8n (4 fluxos) + LLM (GLM) + base de conhecimento. O playbook foi tirado de **277 call
reviews reais**.

### 4.2 Por que não dá para copiar como está

| Ponto do copiloto | Situação da Camila |
|---|---|
| Extensão do Chrome no computador do closer | Você usa o **app do Meet no tablet**: extensões não rodam lá |
| Captura de áudio por ganchos no Meet (quebrou 4 vezes em 7 dias; os testes simulados passavam e a call real falhava) | Um **bot participante** (Recall) recebe o áudio por API oficial: não depende do DOM do Meet |
| Bitrix24 | Notion |
| Vários closers, telemetria por vendedor | Uma pessoa só |
| Captura por aba não dispara o aviso de gravação do Meet (risco LGPD) | O bot aparece na sala, o que é mais transparente |

### 4.3 O que vale reaproveitar (e como)

| Ideia do copiloto | Versão para a Camila |
|---|---|
| **Playbook tirado de dados reais** (277 calls → "a trava é a implantação", "falta perguntar o custo da dor em R$") | O Grok Bot analisa o seu histórico: conversas exportadas do WhatsApp + transcrições das últimas calls de diagnóstico (ganhas e perdidas) → `playbook_mentoria.md` com objeções reais, sinais de compra, perguntas que mais convertem e motivos de perda. É uma tarefa ideal para ele (arquivos em `/workspace`, saída em documento) |
| **Três camadas de decisão** (regra local imediata → IA 4–9 s → base de conhecimento 20–60 s) | **Regras fixas no n8n** (datas, cadências, alertas) → **LLM via API** (extração por conversa) → **Grok Bot** (análise, preparação, relatórios) |
| **Cliente achado pelo link do Meet**, não digitado | O evento do Calendar com o link do Meet é ligado ao lead. A transcrição cai no lead certo automaticamente |
| **Preenchimento conservador**: só campo vazio, modo `simular` antes de gravar | A IA só preenche campo vazio. Mudança de estágio vira **sugestão** que você confirma |
| **Prompt e playbook como arquivo versionado** | Ficam neste repositório (`docs/micro-crm/`), e o fluxo do n8n e o Bot leem dali |
| **Roteiro de call que se marca sozinho** + **pergunta do "custo da dor em reais"** | Roteiro da call de diagnóstico (SPIN adaptado ao método): Situação (faturamento, equipe) → Problema (exaustão, lucro) → **Implicação (quanto custa em R$ e em horas por mês)** → Necessidade → apresentação do programa → oferta. O pós-call mede o % do roteiro coberto |
| **Gravação no CRM ao fim da call**: resumo, dores, objeções, desfecho, % de fala | Pós-reunião no Notion: resumo, dores, objeções, compromissos, próximo passo, data de follow-up, **% de fala sua × dela** |
| **Telemetria sem conteúdo** | Log simples no n8n: mensagens recebidas, conversas processadas, erros. Serve para saber se a coleta parou |
| **Lições de integração** (limite de requisições do Bitrix, retentativas, idempotência) | A API do Notion tem limite (~3 req/s): espaçar as chamadas e tentar de novo. Gravar por ID da mensagem para não duplicar |

### 4.4 Coaching **ao vivo** no tablet: é possível?

Sim, com outro caminho técnico e com ressalvas:

```
Meet (você no tablet) ← bot Recall na sala
        │ áudio em tempo real (websocket ~200 ms)
        ▼
Transcrição streaming pt-BR (Deepgram/AssemblyAI/Gladia via Recall)
        ▼
n8n: regras locais (palavras de objeção/compra) + LLM rápido (Grok API ou Claude)
        ▼
"Sussurro" no **celular** ao lado (Telegram/push) ou numa página aberta em outra janela
```

- O modo de baixa latência nativo do Recall é **só em inglês**. Para português é preciso um provedor de
  streaming (verificar o suporte a pt-BR e o custo, de US$ 0,12 a 0,15/h segundo o próprio documento da tecpet).
- A latência total fica em ~3–10 s, suficiente para cartões ("ela citou preço: pergunte o custo da
  dor"), lenta para frases prontas.
- **Recomendação:** começar **sem** o ao vivo (só pré e pós-call, que dão 80% do valor) e acrescentar o
  sussurro na fase final, se você sentir falta. Se em algum momento você fizer as calls de venda no
  **notebook com Chrome**, a própria extensão da tecpet pode ser adaptada (trocar Bitrix por Notion
  e o playbook), mas a lição registrada lá é que a captura de áudio do Meet é a parte que mais quebra.

---

## 5. Arquitetura recomendada

```
 WhatsApp Business (seu celular/tablet)        Instagram (conta profissional)
        │  Coexistence (app Meta próprio)              │  Instagram API (DM webhooks)
        └──────────────┬───────────────────────────────┘
                       ▼
               n8n (orquestrador)  ◄──── Google Calendar (reuniões com link do Meet)
                       │                         │
                       │                         ▼
                       │              Recall.ai / Meeting BaaS (bot entra no Meet)
                       │                         │ transcrição (webhook)
                       ▼                         ▼
          Banco de mensagens (Supabase/Postgres ou tabela no Notion)
                       │  a cada 30 min por conversa ativa (debounce)
                       ▼
          LLM (Grok API ou Claude) → JSON validado: lead, estágio, campos, follow-up
                       │
                       ▼
                 NOTION (CRM): Leads · Atividades · Interações · Reuniões
                       ▲
                       │ conector Notion + MCP "crm-camila" (exposto pelo n8n)
                       │ gatilho: rotina agendada ou e-mail no alias (n8n avisa)
                       ▼
        GROK BOT "Gerente Comercial" (computador na nuvem)
        briefings · follow-ups em rascunho · preparo e pós-call · relatórios
                       │
                       ▼
              Você, no app do Grok Bot no Tab S7 (voz, push, aprovações)
              (alternativa sem assinatura: bot do Telegram ligado ao n8n)
```

**Quem faz o quê:**

| Componente | Responsabilidade | Por quê |
|---|---|---|
| n8n | Receber webhooks (WhatsApp, Instagram, Recall), gravar mensagens, **regras fixas** (datas de cadência, alertas de "sem resposta há 4h"), expor o MCP | O Grok Bot não recebe webhooks, e regras precisam ser determinísticas |
| LLM via API | Extração estruturada por conversa (campos, estágio sugerido, evidência) | Barato, rápido, previsível, com JSON validado |
| Notion | Fonte da verdade e kanban | Você já usa, e funciona no tablet |
| Grok Bot | Julgamento e preparo: briefing, priorização, rascunhos no seu tom, pré e pós-call, análise semanal, pesquisa de leads | É onde um agente com memória e conectores rende mais |

### 5.1 WhatsApp: coleta somente leitura

| Opção | Como funciona | Risco | Custo | Recomendação |
|---|---|---|---|---|
| **Coexistence (oficial)** | Você conecta o número do **WhatsApp Business** à Cloud API, com um **app próprio no portfólio da Meta** (decisão: sem BSP; runbook em `whatsapp-meta-direto.md`) ou por um BSP, e segue usando o app normalmente. Mensagens recebidas chegam pelo webhook `messages`; as **que você envia pelo celular** chegam como `smb_message_echoes`. Há sincronização inicial do histórico | Baixo: é o caminho oficial | App próprio: US$ 0 (pode exigir virar Tech Provider: verificação + App Review). BSP: ~US$ 12–50/mês. Só receber não gera cobrança por mensagem da Meta | ✅ **Usar** |
| Evolution API / Baileys | Simula o WhatsApp Web como "aparelho conectado" | Médio a alto: viola os termos, pode banir o número sem recurso | Servidor ~US$ 5–10/mês | ⚠️ Só se o seu número for WhatsApp **pessoal** e você aceitar o risco. Use somente leitura e nunca envio em massa |
| Exportar conversa manualmente | "Exportar conversa" → arquivo .txt → pasta no Drive → n8n processa | Zero | Zero | Plano B para importar o histórico antigo |

Requisitos da Coexistence: número em uso no **app WhatsApp Business** há pelo menos 7 dias, abrir
o app com regularidade (há relatos de desconexão após cerca de 14 dias sem uso) e saber que
mensagens de clientes em WhatsApp Desktop para Windows e WearOS podem não disparar webhook.
Grave tudo de forma idempotente pelo ID da mensagem, porque o histórico chega com duplicatas.

> **Decisão sua:** o número que você usa com clientes é WhatsApp **pessoal** ou **Business**? Se for
> pessoal, migrar para o app Business (mantém número e conversas) é o que destrava o caminho oficial.

### 5.2 Instagram

- Conta **profissional** (Criadora ou Empresa) + app no Meta for Developers com *Instagram API with
  Instagram Login* e a permissão `instagram_business_manage_messages`. Para a sua própria conta basta
  o acesso Standard, sem App Review avançado.
- Webhooks de mensagens trazem o remetente (IGSID) e o texto. Comentários e menções também podem
  virar sinal de lead (ex.: alguém comenta "quero" num post).
- Limites: só recebe quando a pessoa escreve primeiro; DMs na pasta "Solicitações" inativas há 30 dias
  não voltam pela API; post compartilhado chega só como link.
- O `@` da pessoa já indica o nicho, e a LLM pode usar a bio para enriquecer o lead (como na sua
  skill do Notion).

### 5.3 Google Meet com usuário-bot

| Opção | Funciona no tablet? | Custo | Observações |
|---|---|---|---|
| **Recall.ai** (ou **Meeting BaaS**) | ✅ o bot entra pelo link, independe do seu aparelho | ~US$ 0,50 + 0,15 de transcrição por reunião (Recall) / ~US$ 0,63–0,68 (Meeting BaaS) | Agendado automaticamente pelo n8n a partir do Google Calendar. Você precisa **admitir** o bot na sala. Transcrição com quem falou o quê |
| Gemini "Anotações por mim" (Workspace) | ✅ | Incluso em alguns planos Workspace | Gera um Google Doc no Drive e o n8n lê esse doc. Mais discreto, sem participante extra |
| Extensão do Chrome | ❌ não roda no app do tablet | — | Descartada, como você mesma previu |
| Vexa (open source, auto-hospedado) | ✅ | Só servidor | Mais trabalho técnico |

Após a reunião, a LLM gera: resumo, dores citadas, objeções, compromissos ("vou conversar com
meu marido"), próximo passo e **data de follow-up**, e anexa tudo ao lead no Notion.
**Ética/LGPD:** avise no convite que a sessão é gravada para anotações ("Notas por IA").

### 5.4 O cérebro (LLM)

- **Quando roda:** não a cada mensagem. Após 30 min sem novas mensagens numa conversa (debounce)
  e após cada reunião. Assim fica barato e com contexto completo.
- **Entrada:** resumo atual do lead + mensagens novas + as suas regras (estágios, programas, cadências).
- **Saída (JSON validado):** `{lead_id, nome, canal, programa_de_interesse, nicho, faturamento,
  dor_principal, objecoes[], temperatura, estagio_sugerido, motivo, proximo_passo, data_follow_up,
  resumo_atualizado, evidencias[]}`.
- **Modelo:** Grok API (function calling disponível; preço por token baixo nos modelos 4.x) ou Claude.
  Para o volume de uma mentora (dezenas de conversas por dia), o custo fica na casa de poucos
  dólares por mês.
- **Regra de ouro:** a IA *sugere* mudança de estágio. As mudanças "para trás" e as de Ganho/Perdido
  ficam pendentes até você confirmar no Telegram (um toque).

---

## 6. Modelo do CRM no Notion

### Bancos de dados

1. **Leads:** Nome, WhatsApp, Instagram, Origem (Instagram orgânico / WhatsApp / Indicação /
   Evento / Anúncio), Programa de interesse (Aceleração · O MAPA · Comunidade Impulso · Consultoria),
   Nicho, Faturamento atual, Dor principal, Objeções, Temperatura (🔥 quente / morno / frio),
   Score, **Estágio**, Próximo passo, Data do follow-up, Resumo vivo, Último contato,
   Valor potencial, Motivo de perda.
2. **Atividades:** Tipo (Follow-up · Ligação · Reunião · Enviar proposta · Enviar material),
   Lead, Vencimento, Status, Criada por (IA/Camila), Rascunho de mensagem.
3. **Interações:** log resumido de cada conversa/reunião, com link para a evidência.
4. **Reuniões:** data, lead, transcrição, resumo, próximos passos.

Visualização **Quadro por Estágio = kanban**. Ao fechar, o lead em "Ganho" dispara a sua skill
`notion-cliente` já existente, que cria o espaço da nova mentorada.

### Estágios sugeridos (venda consultiva de mentoria)

| # | Estágio | Entra quando… | Sai quando… |
|---|---|---|---|
| 1 | Novo contato | 1ª mensagem/DM | ela responde a primeira pergunta |
| 2 | Em conversa | há troca de mensagens | a IA identifica perfil e dor, ou você qualifica |
| 3 | Qualificado | perfil, dor e momento batem com algum programa | call agendada |
| 4 | Call de diagnóstico agendada | evento no Calendar com o lead | a reunião acontece |
| 5 | Call realizada | transcrição processada | proposta enviada |
| 6 | Proposta enviada | link/valor/contrato enviado | ela responde com objeção ou decisão |
| 7 | Negociação | objeção ativa (preço, timing, cônjuge…) | decisão |
| ✅ | Ganho | pagamento/contrato | → onboarding (skill notion-cliente) |
| ❌ | Perdido | recusa explícita | motivo registrado → nutrição em 90 dias |
| 💤 | Nutrição | sem resposta após a cadência | reengajamento |

### Qualificação (adaptação do BANT para mentoria)

- **Momento:** está faturando? qual etapa do negócio?
- **Dor:** exaustão, lucro baixo, falta de processo/equipe (a linguagem do seu método)
- **Investimento:** sinalizou capacidade/abertura ao valor?
- **Decisão:** decide sozinha ou depende de sócio/cônjuge?

Score de 0 a 100 = 25 por critério atendido. A temperatura sobe com sinais de compra ("quanto
custa", "como funciona o pagamento", "quando começa a próxima turma").

### Regras de follow-up (cadências)

| Situação | Cadência | Pausa quando |
|---|---|---|
| Lead novo sem resposta | D+1, D+3, D+7 → Nutrição | ela responde |
| Pediu valor/informação e **você** não respondeu | alerta imediato a partir de 4h úteis | você responde |
| Pós-call sem proposta | proposta em até 24h | proposta enviada |
| Proposta enviada | D+1 (dúvidas), D+3 (prova social/case), D+7 (escassez real: turma/vagas), D+14 (encerramento cordial) | resposta |
| Objeção "vou pensar/ver com marido" | follow-up na data que ela mesma disse; senão D+5 | decisão |
| Perdido | reengajar em 90 dias com conteúdo | — |
| Nutrição | 1 toque de valor a cada 30 dias | resposta |

Cada follow-up vira uma **Atividade** com **rascunho da mensagem no seu tom** (a LLM aprende com as
suas mensagens enviadas). Você copia e envia, porque o CRM é somente leitura no WhatsApp.

### Métricas (relatório semanal)

Leads novos por origem · conversão por estágio · tempo médio em cada estágio · follow-ups
atrasados · taxa call→proposta→ganho · motivos de perda · faturamento previsto (pipeline × probabilidade).

---

## 7. O que fazer pelo Grok Bot e o que fazer pelo Telegram

Você **escolhe um dos dois** como "painel". Fazer os dois duplica o trabalho.

| Critério | **Grok Bot** (app no Tab S7) | **Telegram** (bot próprio ligado ao n8n) |
|---|---|---|
| Custo | assinatura Cursor/SuperGrok (~US$ 20–30+/mês, uso semanal) | grátis (só a LLM via API) |
| Conversa livre e com memória | ✅ excelente, inclusive por voz | ⚠️ limitada ao que você programar |
| Pré e pós-reunião, relatórios em documento/planilha | ✅ nativo | ⚠️ texto simples |
| Pesquisa de leads na web | ✅ navegador próprio | ❌ |
| Previsibilidade | ⚠️ varia de uma execução para outra | ✅ sempre igual |
| Alertas em tempo real ("sem resposta há 4h") | ⚠️ só com rotina ou gatilho por e-mail | ✅ imediato |
| Maturidade | beta | estável |

**Recomendação:** o **Grok Bot como painel** (é o que você quer usar e é onde está o valor de IA), com
os **alertas urgentes por push do n8n** (Telegram ou e-mail) como rede de segurança.

### No Grok Bot (configurar conversando, no desktop na 1ª vez)

1. Criar o Bot **"Gerente Comercial"** com a instrução da seção 3.5.
2. **Conectar apps:** Notion, Google Calendar, Gmail, Google Drive. Adicionar o MCP remoto
   `crm-camila` (URL do n8n + chave).
3. **Regras de aprovação:** "Pergunte antes" para enviar e-mail, apagar, mover para Ganho/Perdido
   e editar mais de 5 leads de uma vez.
4. **Rotinas:**
   - 7h30 (seg–sáb): briefing do dia
   - a cada 2h, das 8h às 20h: processar conversas novas → atualizar leads e criar atividades
   - 1h antes de cada call com link do Meet: ficha + roteiro de diagnóstico
   - quando chegar a transcrição (gatilho por e-mail, se disponível; senão, rotina de hora em hora): pós-call
   - domingo 18h: relatório da semana + objeções mais frequentes → ideias de conteúdo para o Instagram
5. **Tarefas pontuais:** "Analise as conversas exportadas e as transcrições em /workspace e escreva o
   playbook de vendas da mentoria" (seção 4.3). "Pesquisa a @fulana."
6. **No dia a dia, pelo Tab S7:** "como está meu pipeline?", "prepara a call das 15h", "registra:
   a Ana vai falar com o sócio e me dá retorno sexta" (por voz).

### No Telegram (se escolher o caminho sem assinatura, ou só para alertas)

Bot próprio criado no @BotFather e ligado ao n8n:

| Comando/automação | O que faz |
|---|---|
| ☀️ Briefing 8h | Follow-ups do dia com rascunhos, calls de hoje, leads quentes parados |
| 🔔 Alertas | "Lead pediu valor e está sem resposta há 4h", "call em 30 min" |
| ✅ Confirmações | "Mover Ana → Proposta enviada? [Confirmar] [Corrigir]" |
| `/hoje` · `/lead ana` · `/pipeline` | Consultas rápidas |
| `/nota ana ...` (ou **áudio**) | Registra uma informação. O áudio é transcrito pela LLM |
| `/ganho ana` · `/perdido ana preço` | Fecha o lead (ganho dispara o onboarding no Notion) |

---

## 8. Roteiro de implantação

| Fase | Entrega | Esforço | Custo mensal estimado |
|---|---|---|---|
| **0. Decisões** | WhatsApp pessoal ou Business; plano do Workspace; Notion como CRM | 1 conversa | — |
| **1. CRM no Notion** | Bancos Leads, Atividades, Interações e Reuniões + quadro kanban | 1 dia | já incluso no Notion |
| **2. n8n + painel** | n8n + MCP `crm-camila`; Grok Bot "Gerente Comercial" (ou Telegram) com briefing | 1–2 dias | n8n cloud ~€20–24 ou VPS ~US$ 6 · Grok Bot ~US$ 20–30+ |
| **3. Instagram** | App Meta + webhook de DM → leads automáticos | 1 dia | grátis |
| **4. WhatsApp (Coexistence)** | App Meta próprio + Embedded Signup + webhooks + histórico (`whatsapp-meta-direto.md`) | 1–2 dias (+ App Review ~24h se exigido) | US$ 0 |
| **5. Cérebro LLM** | Extração, estágios, cadências e rascunhos no seu tom | 2–3 dias + ajuste fino por 2 semanas | LLM US$ 5–20 |
| **6. Google Meet** | Bot de reunião via Calendar + resumo no lead | 1 dia | ~US$ 0,65 por reunião |
| **7. Playbook** | Grok Bot analisa o histórico de conversas e calls → `playbook_mentoria.md` | 1 tarefa | incluso |
| **8. (Opcional) Sussurro ao vivo** | Transcrição streaming pt-BR + cartões no celular durante a call | 2–3 dias | ~US$ 0,15/h + LLM |

Total recorrente aproximado: **US$ 30–100/mês**, contra US$ 50–150/usuário/mês de CRMs prontos com IA.

---

## 9. LGPD e cuidados

- **Base legal:** legítimo interesse/procedimentos preliminares de contrato para leads e execução de
  contrato para clientes. Inclua uma linha na política de privacidade e na bio/link do Instagram.
- **Minimização:** a LLM recebe só as conversas comerciais. Crie uma lista de exclusão (família,
  amigas) que o n8n ignora.
- **Provedores:** use API com opção de não treinar com os seus dados. O Grok Bot exige armazenamento em
  nuvem do Cursor, por isso só leva dados já resumidos.
- **Reuniões:** avise sobre a gravação e permita que a pessoa recuse.
- **Retenção:** apagar mensagens brutas após 12 meses e manter só resumos.

---

## 10. Próximos passos práticos para você

1. Responder: o WhatsApp de atendimento é **pessoal** ou **Business**? O Instagram é conta **profissional**?
   O seu Google Workspace tem Gemini (Anotações no Meet)?
2. Validar os **estágios** e as **cadências** das seções 6 e 7 (ajustar nomes ao seu jeito de vender).
3. Decidir o painel: **Grok Bot** (recomendado; começar pelo teste grátis de 7 dias) ou Telegram.
   Dá para testar o Grok Bot já: crie o Bot, conecte o Notion e o Calendar e peça o briefing do dia.
4. Começar pela **Fase 1 + 2** (Notion + painel): em poucos dias você já tem kanban e briefing,
   mesmo antes de ligar WhatsApp/Instagram.

---

## Fontes

- Grok Bot: [overview](https://docs.x.ai/grok-bot/overview) · [FAQ](https://docs.x.ai/grok-bot/faq) ·
  [rotinas](https://docs.x.ai/grok-bot/skills-routines-and-automations) ·
  [computador e apps](https://docs.x.ai/grok-bot/computer-and-apps) ·
  [aprovações e privacidade](https://docs.x.ai/grok-bot/approvals-security-and-privacy) ·
  [@bot no X](https://docs.x.ai/grok-bot/tag-on-x) · [Vellum: breakdown](https://www.vellum.ai/blog/official-grok-bot-breakdown) ·
  [AlphaSignal: conectores](https://alphasignal.ai/news/xai-s-grok-bot-runs-tasks-3x-faster-and-trades-stocks-on-your-behalf) ·
  [bots](https://docs.x.ai/grok-bot/bots) · [arquivos](https://docs.x.ai/grok-bot/files-and-results) ·
  [notificações](https://docs.x.ai/grok-bot/settings-and-notifications) · [mobile](https://docs.x.ai/grok-bot/mobile) ·
  [team bots / MCP](https://docs.x.ai/grok-bot/team-bots) · [casos de uso](https://docs.x.ai/grok-bot/use-cases) ·
  [planos (Cursor)](https://cursor.com/help/grok-bot/plans) · [anúncio xAI](https://x.ai/news/introducing-grok-bot)
- Análises do Grok Bot: [Flavio Copes](https://flaviocopes.com/grok-bot/) · [Composio](https://composio.dev/content/guide-to-frok-bot) ·
  [RohitAI: "one blast radius"](https://rohitai.com/blog/xai-grok-bot-always-on-ai-teammates) ·
  [Jay Mount: GTM e preços](https://jaymountconsulting.com/blog/grok-bot-for-gtm) · [Agent Finder](https://agent-finder.co/reviews/grok-bot) ·
  [Latent Digital: casos](https://latentdigitalsolutions.com/grok-bot-use-cases/) ·
  [Whisker Beacon: WhatsApp](https://whiskerbeacon.com/guides/grok-bot-whatsapp-customer-support-workflow/)
- Recall tempo real: [docs](https://docs.recall.ai/v1.10/docs/real-time-transcription) · [baixa latência](https://www.recall.ai/blog/low-latency-transcription-api)
- Copiloto tecpet: documento interno `copiloto_estrutura_18out2026.md` (v0.7.3, 18/10/2026)
- Grok + mensageria: [Blueticks: Grok no WhatsApp](https://blueticks.co/blog/grok-whatsapp) ·
  [Whautomate: termos Meta/IA](https://whautomate.com/integrations/xai-grok) ·
  [Layer3: Grok Telegram bot](https://www.layer3labs.io/guides/grok-telegram-bot) ·
  [grok-telegram-bot (comunidade)](https://github.com/artickc/grok-telegram-bot)
- Grok API (preços): [Morphllm](https://www.morphllm.com/grok-api-pricing) · [mem0](https://mem0.ai/blog/xai-grok-api-pricing)
- WhatsApp Coexistence: [DEV: guia para devs](https://dev.to/wapgrowai_org/whatsapp-coexistence-for-developers-when-the-business-app-and-the-cloud-api-share-a-number-1c4a) ·
  [YCloud](https://www.ycloud.com/blog/whatsapp-business-app-coexistence-meta-update) ·
  [InstantReply: limites](https://www.instantreply.co/blog/whatsapp-coexistence-what-actually-syncs-2026) ·
  [Telnyx](https://telnyx.com/release-notes/whatsapp-coexistence)
- Evolution API/Baileys: [docs Evolution](https://mintlify.com/EvolutionAPI/evolution-api/whatsapp/baileys) ·
  [Pillitteri: Evolution vs Cloud API](https://pasqualepillitteri.it/en/news/12969/integrate-whatsapp-evolution-api-vs-cloud-api)
- Instagram: [Messaging API (Meta)](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/messaging-api)
- Google Meet bots: [Recall.ai Google Meet](https://www.recall.ai/product/meeting-bot-api/google-meet) ·
  [Nylas: comparativo 2026](https://www.nylas.com/blog/best-meeting-bot-apis/)
- CRMs: [Kommo](https://www.kommo.com/) · [folk vs Attio (WhatsApp)](https://www.folk.app/articles/folk-crm-vs-attio-whatsapp) ·
  [AI-native CRMs 2026](https://blog.laratranslate.com/best-ai-native-crm-platforms/)
