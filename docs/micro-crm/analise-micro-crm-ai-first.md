# Micro-CRM AI-first: análise e arquitetura recomendada

> Para: Camila Martins Finger (mentorias Método Lucro Anti-Exaustão®, Programa de Aceleração, O MAPA)
> Data da pesquisa: 18/10/2026. Preços e recursos de terceiros mudam rápido: confirme nos links antes de contratar.

---

## 1. Resumo executivo

1. **O Grok Bot não consegue ser o CRM inteiro sozinho.** Ele roda num computador na nuvem e
   cumpre rotinas agendadas, mas a documentação oficial não traz nenhuma integração com WhatsApp,
   Instagram, Telegram ou webhooks de entrada, e ele não entra em chamadas de vídeo. Ele pode ser o
   **analista** do CRM (rotinas diárias, revisão de pipeline, rascunhos de follow-up), não o
   **coletor** de mensagens.
2. **A coleta tem que ser feita por vias oficiais.** WhatsApp via *Coexistence* (você continua usando
   o app WhatsApp Business no celular/tablet, e cada mensagem recebida ou enviada chega por webhook);
   Instagram via *Instagram API with Instagram Login* (webhook de DMs).
3. **O "CRM sem interface" fica no Notion, que você já usa.** Um banco de dados de Leads com
   visualização em quadro é o kanban. A conversa com o CRM acontece por um **bot no Telegram**
   (briefing diário, alertas de follow-up e comandos).
4. **Para o Google Meet, use um bot que entra na reunião como participante** (Recall.ai ou Meeting
   BaaS, por volta de US$ 0,50–0,70 por reunião). Como o bot roda no servidor, funciona mesmo você
   estando no app do Meet no tablet. Se o seu Google Workspace tiver o Gemini "Anotações por mim",
   essa é a alternativa sem custo extra.
5. **Arquitetura:** `WhatsApp/Instagram/Meet → n8n (orquestrador) → LLM (Grok API ou Claude) →
   Notion (CRM) → Telegram (você)`. O Grok Bot fica opcional, como camada de rotinas e análise.

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

## 3. Grok Bot: o que ele faz e o que não faz

Fonte: documentação oficial ([overview](https://docs.x.ai/grok-bot/overview),
[FAQ](https://docs.x.ai/grok-bot/faq), [rotinas](https://docs.x.ai/grok-bot/skills-routines-and-automations),
[computador e apps](https://docs.x.ai/grok-bot/computer-and-apps),
[aprovações e privacidade](https://docs.x.ai/grok-bot/approvals-security-and-privacy)).

**O que é:** agente da xAI, em beta desde 11/08/2026. Cada "Bot" é um colega de IA com nome, função
e memória, e trabalha num **computador persistente na nuvem** (navegador, arquivos e terminal). Ele
continua trabalhando com o app fechado. Funciona no Mac, Windows, Linux, iPhone/iPad e Android.
Vem incluído nos planos pagos do Cursor ou pode ser ligado a uma assinatura SuperGrok / Plus / Heavy.
A cobrança é por uso semanal, com uso extra opcional.

| Capacidade | Situação | Relevância para o CRM |
|---|---|---|
| Rotinas agendadas ("todo dia útil às 8h") | ✅ até 50 por Bot, intervalo mínimo de 5 min | Briefing diário, revisão de follow-ups, relatório semanal |
| Gatilhos por evento | ⚠️ só Slack e GitHub documentados | Não recebe WhatsApp, Instagram nem webhook |
| Conectores | ⚠️ lista não publicada; exemplos: Slack, GitHub, X, Trello, "um CRM" | Não há Google Calendar, Notion, WhatsApp, Instagram ou Telegram documentados. Ele usaria o **navegador** para acessá-los |
| Uso de navegador ("computer use") | ✅ | Poderia abrir o Notion ou o WhatsApp Web, mas veja os riscos abaixo |
| Memória | ✅ preferências, papel e resumos de trabalhos anteriores | Lembra as suas regras de CRM |
| Enviar e-mail/Slack | ✅ com a sua revisão antes | Não envia WhatsApp |
| Conversar via Telegram/WhatsApp | ❌ não documentado | Você fala com ele pelo app próprio (no tablet, inclusive) ou marcando @bot no X |
| Entrar em reunião de vídeo | ❌ só existe chat de voz com você | Não serve para o Meet |
| Aprovações | ✅ regras "Pergunte antes" e "Permita automaticamente", botão "Stop now" | Bom para garantir que ele não mande nada sozinho |
| Privacidade | ⚠️ exige armazenamento em nuvem (Cursor). Todos os Bots compartilham o mesmo computador | Conversas de clientes ficariam na nuvem do Cursor/xAI: atenção à LGPD |

**Sobre deixar o Grok Bot ler o WhatsApp Web:** é tecnicamente possível (ele mantém sessões
de navegador), mas **não recomendo**. A sessão cai, a leitura por tela é frágil e lenta,
automatizar o WhatsApp Web viola os termos do WhatsApp (risco de bloqueio do número) e todo o
histórico das clientes passa por um computador de terceiros. Use isso no máximo como teste.

**Comunidade:** existe um projeto não oficial
([grok-telegram-bot](https://github.com/artickc/grok-telegram-bot)) que controla o *Grok Build CLI*
pelo Telegram. Ele não é o Grok Bot, é voltado para programação e não serve de base para um CRM.

**Veredito:** use o Grok Bot (se quiser) como **"gerente de pipeline"**, com rotinas que leem o
Notion e te entregam análises. A coleta e o preenchimento ficam no n8n + LLM via API (a própria
API do Grok serve, com function calling).

---

## 4. Arquitetura recomendada

```
 WhatsApp Business (seu celular/tablet)        Instagram (conta profissional)
        │  Coexistence (BSP oficial)                   │  Instagram API (DM webhooks)
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
                       │
          ┌────────────┴─────────────┐
          ▼                          ▼
   Bot do Telegram (você)     Grok Bot (opcional): rotinas de análise
   briefing, alertas, comandos
```

### 4.1 WhatsApp: coleta somente leitura

| Opção | Como funciona | Risco | Custo | Recomendação |
|---|---|---|---|---|
| **Coexistence (oficial)** | Você conecta o número do **WhatsApp Business** a um BSP (provedor oficial Meta) e segue usando o app normalmente. Mensagens recebidas chegam pelo webhook `messages`; as **que você envia pelo celular** chegam como `smb_message_echoes`. Há sincronização inicial do histórico | Baixo: é o caminho oficial | BSP de ~US$ 0 a 50/mês. Só receber não gera cobrança por mensagem da Meta | ✅ **Usar** |
| Evolution API / Baileys | Simula o WhatsApp Web como "aparelho conectado" | Médio a alto: viola os termos, pode banir o número sem recurso | Servidor ~US$ 5–10/mês | ⚠️ Só se o seu número for WhatsApp **pessoal** e você aceitar o risco. Use somente leitura e nunca envio em massa |
| Exportar conversa manualmente | "Exportar conversa" → arquivo .txt → pasta no Drive → n8n processa | Zero | Zero | Plano B para importar o histórico antigo |

Requisitos da Coexistence: número em uso no **app WhatsApp Business** há pelo menos 7 dias, abrir
o app com regularidade (há relatos de desconexão após cerca de 14 dias sem uso) e saber que
mensagens de clientes em WhatsApp Desktop para Windows e WearOS podem não disparar webhook.
Grave tudo de forma idempotente pelo ID da mensagem, porque o histórico chega com duplicatas.

> **Decisão sua:** o número que você usa com clientes é WhatsApp **pessoal** ou **Business**? Se for
> pessoal, migrar para o app Business (mantém número e conversas) é o que destrava o caminho oficial.

### 4.2 Instagram

- Conta **profissional** (Criadora ou Empresa) + app no Meta for Developers com *Instagram API with
  Instagram Login* e a permissão `instagram_business_manage_messages`. Para a sua própria conta basta
  o acesso Standard, sem App Review avançado.
- Webhooks de mensagens trazem o remetente (IGSID) e o texto. Comentários e menções também podem
  virar sinal de lead (ex.: alguém comenta "quero" num post).
- Limites: só recebe quando a pessoa escreve primeiro; DMs na pasta "Solicitações" inativas há 30 dias
  não voltam pela API; post compartilhado chega só como link.
- O `@` da pessoa já indica o nicho, e a LLM pode usar a bio para enriquecer o lead (como na sua
  skill do Notion).

### 4.3 Google Meet com usuário-bot

| Opção | Funciona no tablet? | Custo | Observações |
|---|---|---|---|
| **Recall.ai** (ou **Meeting BaaS**) | ✅ o bot entra pelo link, independe do seu aparelho | ~US$ 0,50 + 0,15 de transcrição por reunião (Recall) / ~US$ 0,63–0,68 (Meeting BaaS) | Agendado automaticamente pelo n8n a partir do Google Calendar. Você precisa **admitir** o bot na sala. Transcrição com quem falou o quê |
| Gemini "Anotações por mim" (Workspace) | ✅ | Incluso em alguns planos Workspace | Gera um Google Doc no Drive e o n8n lê esse doc. Mais discreto, sem participante extra |
| Extensão do Chrome | ❌ não roda no app do tablet | — | Descartada, como você mesma previu |
| Vexa (open source, auto-hospedado) | ✅ | Só servidor | Mais trabalho técnico |

Após a reunião, a LLM gera: resumo, dores citadas, objeções, compromissos ("vou conversar com
meu marido"), próximo passo e **data de follow-up**, e anexa tudo ao lead no Notion.
**Ética/LGPD:** avise no convite que a sessão é gravada para anotações ("Notas por IA").

### 4.4 O cérebro (LLM)

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

## 5. Modelo do CRM no Notion

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

## 6. O que fazer no Telegram e o que fazer no Grok Bot

### Telegram (o seu "painel" diário). Recomendo como interface principal

Bot próprio criado no @BotFather e ligado ao n8n. Funciona no celular e no tablet.

| Comando/automação | O que faz |
|---|---|
| ☀️ Briefing 8h (automático) | Follow-ups do dia com rascunhos, calls de hoje com resumo do lead, leads quentes parados |
| 🔔 Alertas (automático) | "Lead pediu valor e está sem resposta há 4h", "call em 30 min: resumo da Ana" |
| ✅ Confirmações | "IA quer mover Ana → Proposta enviada [Confirmar] [Corrigir]" |
| `/hoje` | Agenda + follow-ups |
| `/lead ana` | Ficha resumida + último contato + próximo passo |
| `/pipeline` | Contagem por estágio e valor previsto |
| `/nota ana ...` (ou **áudio**) | Registra uma informação. O áudio é transcrito pela LLM |
| `/ganho ana` · `/perdido ana preço` | Fecha o lead (ganho dispara o onboarding no Notion) |
| Pergunta livre | "quem está em proposta há mais de uma semana?" |
| 📊 Relatório de domingo | Métricas da semana |

### Grok Bot (opcional, como "gerente de pipeline")

Se você já tem ou quer assinar o SuperGrok, crie **um Bot "Gerente Comercial"** e configure por
mensagem (o Grok Bot é configurado conversando):

1. **Rotina diária 7h30:** "Abra o banco Leads no Notion, liste follow-ups vencidos e leads
   quentes sem contato há mais de 3 dias, e me mande o resumo." (Ele acessa o Notion pelo navegador
   logado. Faça o login uma vez com o "Take over".)
2. **Rotina semanal:** análise do funil, motivos de perda e sugestões de conteúdo para o Instagram
   a partir das objeções mais frequentes.
3. **Pesquisa de lead sob demanda:** "pesquise o @ dela e o site e me diga o tamanho do negócio".
4. **Regras de aprovação:** "Pergunte antes" para qualquer envio de mensagem e edição em massa.

**Não use o Grok Bot para:** receber mensagens do WhatsApp/Instagram, entrar no Meet ou ser o
único lugar onde ficam os dados. Ele não tem gatilhos para isso, e os dados dos clientes ficariam
num computador de nuvem compartilhado.

> Se o objetivo for **um único assinante e um único lugar**, dá para pular o Grok Bot: o próprio
> n8n faz as rotinas e manda tudo no Telegram, e a LLM via API (Grok ou Claude) faz a análise.

---

## 7. Roteiro de implantação

| Fase | Entrega | Esforço | Custo mensal estimado |
|---|---|---|---|
| **0. Decisões** | WhatsApp pessoal ou Business; plano do Workspace; Notion como CRM | 1 conversa | — |
| **1. CRM no Notion** | Bancos Leads, Atividades, Interações e Reuniões + quadro kanban | 1 dia | já incluso no Notion |
| **2. Telegram + n8n** | Bot, briefing, comandos `/lead` e `/nota` (com áudio) | 1–2 dias | n8n cloud ~€20–24 ou VPS ~US$ 6 |
| **3. Instagram** | App Meta + webhook de DM → leads automáticos | 1 dia | grátis |
| **4. WhatsApp (Coexistence)** | BSP + webhooks + importação do histórico | 1–2 dias | BSP US$ 0–50 |
| **5. Cérebro LLM** | Extração, estágios, cadências e rascunhos no seu tom | 2–3 dias + ajuste fino por 2 semanas | LLM US$ 5–20 |
| **6. Google Meet** | Bot de reunião via Calendar + resumo no lead | 1 dia | ~US$ 0,65 por reunião |
| **7. (Opcional) Grok Bot** | Rotinas de análise | 1h | assinatura SuperGrok/Cursor |

Total recorrente aproximado: **US$ 30–100/mês**, contra US$ 50–150/usuário/mês de CRMs prontos com IA.

---

## 8. LGPD e cuidados

- **Base legal:** legítimo interesse/procedimentos preliminares de contrato para leads e execução de
  contrato para clientes. Inclua uma linha na política de privacidade e na bio/link do Instagram.
- **Minimização:** a LLM recebe só as conversas comerciais. Crie uma lista de exclusão (família,
  amigas) que o n8n ignora.
- **Provedores:** use API com opção de não treinar com os seus dados. O Grok Bot exige armazenamento em
  nuvem do Cursor, por isso só leva dados já resumidos.
- **Reuniões:** avise sobre a gravação e permita que a pessoa recuse.
- **Retenção:** apagar mensagens brutas após 12 meses e manter só resumos.

---

## 9. Próximos passos práticos para você

1. Responder: o WhatsApp de atendimento é **pessoal** ou **Business**? O Instagram é conta **profissional**?
   O seu Google Workspace tem Gemini (Anotações no Meet)?
2. Validar os **estágios** e as **cadências** das seções 5 e 6 (ajustar nomes ao seu jeito de vender).
3. Decidir se o Grok Bot entra (opcional) ou se fica tudo em n8n + Telegram.
4. Começar pela **Fase 1 + 2** (Notion + Telegram): em poucos dias você já tem kanban e briefing,
   mesmo antes de ligar WhatsApp/Instagram.

---

## Fontes

- Grok Bot: [overview](https://docs.x.ai/grok-bot/overview) · [FAQ](https://docs.x.ai/grok-bot/faq) ·
  [rotinas](https://docs.x.ai/grok-bot/skills-routines-and-automations) ·
  [computador e apps](https://docs.x.ai/grok-bot/computer-and-apps) ·
  [aprovações e privacidade](https://docs.x.ai/grok-bot/approvals-security-and-privacy) ·
  [@bot no X](https://docs.x.ai/grok-bot/tag-on-x) · [Vellum: breakdown](https://www.vellum.ai/blog/official-grok-bot-breakdown) ·
  [AlphaSignal: conectores](https://alphasignal.ai/news/xai-s-grok-bot-runs-tasks-3x-faster-and-trades-stocks-on-your-behalf)
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
