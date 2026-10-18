# WhatsApp direto na Meta (sem BSP): runbook para o Claude Code local

> Faz parte do [`runbook-projeto-completo.md`](runbook-projeto-completo.md) (fase 5). Valem as regras
> gerais de lá: pontos de parada 🛑, segredos fora do repositório e registro em `STATUS.md`.
> Aqui, **[CLAUDE]** significa terminal ou Chrome, conforme o passo.

> **Para quem:** o Claude Code rodando no computador da Camila, com acesso ao n8n dela
> (`https://crm.seudominio.com.br`). As etapas marcadas **[CAMILA]** são cliques nos painéis da Meta
> que só a dona da conta pode fazer: o Claude deve parar, explicar o clique e esperar a confirmação.
> As etapas **[CLAUDE]** são construção (páginas, fluxos n8n, SQL, chamadas de API).
>
> **Objetivo:** ligar o número do **WhatsApp Business app** da Camila à **Cloud API** em modo
> **Coexistence**, com um **app próprio no Business Manager (portfólio empresarial)**, sem provedor
> (BSP). O CRM **só lê**: recebe as mensagens dos clientes (`messages`) e as que a Camila envia pelo
> celular (`smb_message_echoes`), mais o histórico de 6 meses (`history`). **Nada é enviado pela API.**
>
> Pesquisa feita em 18/10/2026. A documentação da Meta muda com frequência: **antes de cada etapa,
> confira a página oficial citada** e, se divergir deste arquivo, siga a Meta.

---

## 0. Como a Meta exige que isso seja feito

1. A Coexistence só é ativada pelo **Embedded Signup** (o pop-up de cadastro da Meta) com o fluxo
   de *onboarding de usuários do WhatsApp Business app*. Não há botão no WhatsApp Manager para isso.
   - Doc: <https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/>
2. A página de Coexistence lista como requisito: **"You must already be a Solution Partner or Tech
   Provider"** e **"You must use Embedded Signup with session logging"**. Também exige o WhatsApp Business
   app na versão **2.24.17 ou superior**.
3. A página de App Review diz que quem usa a API **para o próprio negócio** ("Direct Developer") recebe o
   *Standard Access* automaticamente e **não precisa de App Review**. Essa regra vale para a API em
   geral. Para a Coexistence, a página específica pede Tech Provider.

**Estratégia:**
- **Caminho A (tentar primeiro, mais rápido):** criar o app, configurar o Embedded Signup e rodar o
  fluxo com o próprio número da Camila usando só o Standard Access (app e WABA no mesmo portfólio).
  Se a Meta aceitar, pula-se a parte de Tech Provider.
- **Caminho B (o oficial, se o A for bloqueado):** registrar o portfólio da Camila como **Tech Provider**
  (gratuito): verificação da empresa + App Review com 2 vídeos, com resposta média de ~24h.
  Depois rodar o mesmo Embedded Signup.

O Claude deve **registrar no fim deste arquivo** (seção 9) qual caminho funcionou e as respostas reais
da API, porque isso vai servir para as próximas vezes.

---

## 1. Pré-requisitos (checar antes de começar)

- [ ] **[CAMILA]** Número ativo no **WhatsApp Business app** do celular principal, versão ≥ 2.24.17,
      usado há pelo menos alguns dias. O número **não pode** ter sido criado antes por um app de desenvolvedor.
- [ ] **[CAMILA]** **Portfólio empresarial** (business.facebook.com) com **autenticação em dois fatores**
      ativada para todos os administradores.
- [ ] **[CAMILA]** Conta em **developers.facebook.com** com o mesmo login de administradora do portfólio.
- [ ] **[CAMILA]** **Política de privacidade** pública (URL HTTPS) e um **ícone** 1024×1024 para o app.
      O ícone não pode usar a marca do WhatsApp nem da Meta.
- [ ] **[CLAUDE]** n8n no ar em HTTPS (`https://crm.seudominio.com.br`), com Postgres e o banco `crm` criados.
- [ ] **[CLAUDE]** Confirmar com a Camila: **não haverá envio pela API**. Mesmo assim, a Meta pode pedir
      uma forma de pagamento na conta do WhatsApp (WABA). Sem envio pela API, não há cobrança: mensagens
      enviadas pelo app continuam gratuitas.

> Nada de chaves no repositório. Tokens, App Secret e verify token vão para as **credenciais do n8n**
> e para o cofre de senhas da Camila. O Claude nunca imprime segredos no terminal nem os comita.

---

## 2. Criar o app na Meta

1. **[CAMILA]** developers.facebook.com → **Meus apps → Criar app**
   - Caso de uso: **"Conectar-se com clientes pelo WhatsApp"** (WhatsApp)
   - Portfólio empresarial: o da Camila
   - Nome: algo como "CRM Camila Finger" (sem "WhatsApp" no nome)
2. **[CAMILA]** **Configurações do app → Básico:** ícone, URL da política de privacidade, categoria
   "Empresas e páginas", e-mail de contato. Anotar o **App ID** e o **App Secret** no cofre.
3. **[CAMILA]** Adicionar o produto **Login do Facebook para Empresas** (Facebook Login for Business).
4. **[CAMILA]** Login do Facebook para Empresas → **Configurações** (Client OAuth settings). Ativar:
   *Client OAuth login*, *Web OAuth login*, *Enforce HTTPS*, *Embedded Browser OAuth Login*,
   *Use Strict Mode for redirect URIs* e *Login with the JavaScript SDK*.
   Em **Allowed domains for the JavaScript SDK** e **Valid OAuth redirect URIs**, colocar
   `https://crm.seudominio.com.br/`.
5. **[CAMILA]** Login do Facebook para Empresas → **Configurações (Configurations) → Criar**:
   - a partir do modelo **"WhatsApp Embedded Signup Configuration With 60 Expiration Token"**,
     ou uma configuração personalizada com a variação de login **"WhatsApp Embedded Signup"**;
   - permissões: `whatsapp_business_management` e `whatsapp_business_messaging`;
   - anotar o **Configuration ID** (`config_id`).

Doc: <https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/implementation>
(use a **versão 4** do Embedded Signup: a v2 foi descontinuada em 15/10/2026).

---

## 3. Webhook no n8n (antes do cadastro)

O histórico tem que ser sincronizado em até **24h** depois do cadastro, e os webhooks já precisam
estar recebendo. Por isso o receptor é construído **antes**.

### 3.1 Tabelas no Postgres (`crm`) — [CLAUDE]

```sql
create table if not exists wa_mensagens (
  id            text primary key,            -- message id da Meta (wamid...) → idempotência
  wa_id         text not null,              -- telefone do cliente (formato E.164 sem +)
  direcao       text not null check (direcao in ('entrada','saida')),
  origem        text not null,               -- messages | smb_message_echoes | history
  tipo          text not null,               -- text | audio | image | document | ...
  texto         text,
  midia_id      text,
  enviada_em    timestamptz not null,
  bruto         jsonb not null,
  recebida_em   timestamptz not null default now(),
  analisada     boolean not null default false
);
create index if not exists wa_mensagens_wa_id_idx on wa_mensagens (wa_id, enviada_em);

create table if not exists wa_contatos (
  wa_id       text primary key,
  nome        text,
  atualizado  timestamptz not null default now()
);

create table if not exists wa_exclusao (      -- família, amigas, fornecedores: ignorados
  wa_id text primary key, motivo text
);

create table if not exists wa_eventos_conta (  -- account_update, erros de sync etc.
  id bigserial primary key, tipo text, bruto jsonb, recebido_em timestamptz default now()
);
```

### 3.2 Fluxo n8n "WA · webhook" — [CLAUDE]

- Nó **Webhook** no caminho `whatsapp`, métodos **GET e POST**, *Raw body* ligado (necessário para
  validar a assinatura).
- **GET (verificação da Meta):** se `hub.mode == 'subscribe'` e `hub.verify_token` for igual ao
  token guardado em credencial/variável, responder **200** com o valor de `hub.challenge` em texto puro.
  Senão, **403**.
- **POST:**
  1. Validar `X-Hub-Signature-256` = `sha256=` + HMAC-SHA256(corpo bruto, **App Secret**). Se não
     bater, responder 401 e não processar.
  2. **Responder 200 imediatamente** (a Meta reenvia se demorar) e processar depois.
  3. Para cada `entry[].changes[]`, conforme `field`:
     - `messages` → mensagens **recebidas** (`value.messages[]`, com nome em `value.contacts[]`) → `direcao='entrada'`.
       Os `value.statuses[]` podem ser ignorados.
     - `smb_message_echoes` → mensagens que a **Camila enviou pelo app** → `direcao='saida'`, cliente = destinatário.
     - `history` → blocos do histórico (podem chegar **repetidos e sobrepostos**). Gravar com
       `insert ... on conflict (id) do nothing` e **sem disparar alertas**. Erro `2593109` = a Camila
       recusou compartilhar o histórico.
     - `smb_app_state_sync` → contatos da agenda do app → `wa_contatos`.
     - `account_update` → gravar em `wa_eventos_conta`. Se vier `PRIMARY_INACTIVITY` (celular sem
       abrir há ~14 dias), **alertar a Camila** (e-mail/push).
  4. Ignorar quem está em `wa_exclusao`.
  5. Áudio: guardar `midia_id`. Outro fluxo baixa a mídia (`GET /<MEDIA_ID>` → URL → download com o
     token) e transcreve. **IDs de mídia do histórico só valem para mensagens dos últimos 14 dias.**
  6. Criar/atualizar o lead no Notion (Origem = WhatsApp) e marcar a conversa como pendente de análise.
     Esse passo é o mesmo fluxo do Instagram, então vale reaproveitar o subfluxo.
- Registrar no log só contagens e erros (telemetria sem conteúdo).

> **Atenção ao formato:** os exemplos de payload de `smb_message_echoes` e `history` estão na
> página de Coexistence. O Claude deve **capturar os primeiros payloads reais** (guardar em `bruto`)
> e ajustar o mapeamento a partir deles, sem confiar só em exemplos.

### 3.3 Registrar o webhook no app — [CAMILA] com o Claude guiando

App Dashboard → **WhatsApp → Configuração**:
- URL de callback: `https://crm.seudominio.com.br/webhook/whatsapp`
- Token de verificação: o mesmo do passo 3.2 → **Verificar e salvar**
- Assinar os campos: `messages`, `smb_message_echoes`, `history`, `smb_app_state_sync`, `account_update`.

---

## 4. Página do Embedded Signup — [CLAUDE]

Servir uma página HTML **pelo próprio n8n**: fluxo "WA · cadastro", com um Webhook GET em
`/webhook/wa-cadastro` e um *Respond to Webhook* com `Content-Type: text/html`. O domínio já está
liberado no Login do Facebook. Como a página é usada **uma vez só**, proteja com um parâmetro secreto
na URL e desative o fluxo depois do cadastro.

Esqueleto (conferir os nomes exatos na doc v4 e no *Embedded Signup Builder* do App Dashboard):

```html
<!doctype html>
<meta charset="utf-8">
<title>Conectar WhatsApp ao CRM</title>
<button id="conectar">Conectar meu WhatsApp Business</button>
<pre id="log"></pre>
<script>
  const APP_ID = '<APP_ID>';
  const CONFIG_ID = '<CONFIGURATION_ID>';
  const GRAPH_VERSION = 'v25.0'; // usar a versão atual da Graph API
  const BACKEND = 'https://crm.seudominio.com.br/webhook/wa-cadastro-codigo';
  let sessao = {};

  window.fbAsyncInit = () => FB.init({ appId: APP_ID, autoLogAppEvents: true, xfbml: true, version: GRAPH_VERSION });

  // Eventos da sessão (session logging): traz waba_id, phone_number_id e o tipo de conclusão
  window.addEventListener('message', (event) => {
    if (!event.origin.endsWith('facebook.com')) return;
    try {
      const data = JSON.parse(event.data);
      if (data.type === 'WA_EMBEDDED_SIGNUP') {
        sessao = data;
        document.getElementById('log').textContent = JSON.stringify(data, null, 2);
        // Coexistence concluída: data.event === 'FINISH_WHATSAPP_BUSINESS_APP_ONBOARDING'
      }
    } catch (_) {}
  });

  function aoLogar(response) {
    const code = response.authResponse && response.authResponse.code;
    if (!code) return;
    // O code vale ~30 segundos: enviar já para o backend trocar pelo token
    fetch(BACKEND, { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, sessao }) });
  }

  document.getElementById('conectar').onclick = () => FB.login(aoLogar, {
    config_id: CONFIG_ID,
    response_type: 'code',
    override_default_response_type: true,
    extras: {
      setup: {},
      featureType: 'whatsapp_business_app_onboarding', // ativa a Coexistence (confirmar na doc)
      sessionInfoVersion: '3'
    }
  });
</script>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js"></script>
```

> Os valores `featureType` e `sessionInfoVersion` aparecem na documentação de Coexistence, mas a
> página de implementação v4 mostra só `extras: { setup: {} }`. Se o pop-up não oferecer "conectar
> o app WhatsApp Business existente", gere o código no **Embedded Signup Builder** (App Dashboard →
> WhatsApp) com a opção de usuários do Business app e use o que ele produzir.

---

## 5. Backend do cadastro (troca do código) — [CLAUDE]

Fluxo "WA · cadastro-código" (Webhook POST `/webhook/wa-cadastro-codigo`). Tem que rodar em
menos de 30 s:

1. `GET https://graph.facebook.com/<VERSAO>/oauth/access_token?client_id=<APP_ID>&client_secret=<APP_SECRET>&code=<CODE>`
   → **business token**. Guardar em credencial do n8n e não registrar em log.
2. Gravar `waba_id`, `phone_number_id` e `business_id` (da `sessao`) em `wa_eventos_conta`.
3. **Inscrever o app na WABA:**
   `POST https://graph.facebook.com/<VERSAO>/<WABA_ID>/subscribed_apps` (Bearer business token) → `{"success": true}`.
4. **Não registrar o número** (`/register`): na Coexistence ele já está registrado.
5. **Sincronizar contatos (uma vez só):**
   `POST /<PHONE_NUMBER_ID>/smb_app_data` com `{"messaging_product":"whatsapp","sync_type":"smb_app_state_sync"}`.
6. **Sincronizar histórico (uma vez só, em até 24h):**
   `POST /<PHONE_NUMBER_ID>/smb_app_data` com `{"messaging_product":"whatsapp","sync_type":"history"}`.
   O histórico cobre os **180 dias** anteriores ao cadastro, em fases (dia 0–1, 1–90 e 90–180).
   Grupos não entram.
7. Conferir: `GET /<PHONE_NUMBER_ID>?fields=is_on_biz_app,platform_type` → espere
   `is_on_biz_app: true` e `platform_type: "CLOUD_API"`.

**Token para uso contínuo:** como o app e a WABA são do mesmo portfólio, prefira um **token de
usuário do sistema** (Configurações do negócio → Usuários do sistema → usuário "crm-n8n" com função
Admin → atribuir o app e a conta do WhatsApp → gerar token **sem expiração** com
`whatsapp_business_management` e `whatsapp_business_messaging`). Use-o para baixar mídias e para
consultas. O business token do cadastro fica de reserva.

---

## 6. Rodar o cadastro

1. **[CAMILA]** No **computador**, abrir `https://crm.seudominio.com.br/webhook/wa-cadastro?k=<segredo>` e
   clicar em **Conectar**. Fazer login no Facebook, escolher o portfólio, escolher **conectar o
   WhatsApp Business app existente** e informar o número.
2. **[CAMILA]** No **celular**, o WhatsApp Business mostra o pedido: confirmar (QR code ou aviso
   em *Configurações → Conta → Plataforma comercial*) e **aceitar compartilhar o histórico**.
3. **[CLAUDE]** Conferir a resposta da troca de código, o `subscribed_apps` e os dois `smb_app_data`.
   Acompanhar as execuções no n8n até começarem a chegar os eventos `history`.
4. **[CAMILA]** Os aparelhos conectados (WhatsApp Web, tablet) são **desconectados** no cadastro.
   Reconectar o Tab S7 e o computador. **Não use o WhatsApp para Windows**: mensagens recebidas ali
   não disparam webhook. Use o WhatsApp Web no navegador.
5. **[CLAUDE]** Desativar o fluxo "WA · cadastro" (a página).

### Se o Caminho A falhar (erro de permissão / exige Tech Provider)

1. **[CAMILA]** App Dashboard → Casos de uso → WhatsApp → Personalizar → **"Tech Provider onboarding"**
   → **verificar a empresa**: razão social, CNPJ, endereço, telefone, site, documentos.
2. **[CLAUDE + CAMILA]** **App Review** pedindo *Advanced Access* para `whatsapp_business_messaging`
   e `whatsapp_business_management`, com **2 vídeos**:
   (a) uma mensagem criada e enviada pelo app e recebida num WhatsApp; para isso, use o **número
   de teste** que a Meta fornece no app, enviando por um fluxo n8n de teste;
   (b) criação de um template de mensagem (pode ser pelo WhatsApp Manager ou por cURL).
   Mais um texto curto explicando o uso: CRM interno que registra as conversas comerciais da própria empresa.
3. Aprovado (~24h em média), repetir a seção 6.

Docs: Tech Provider <https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers>
· App Review <https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/app-review>

---

## 7. Testes de aceite — [CLAUDE] com a Camila

| Teste | Resultado esperado |
|---|---|
| Uma amiga manda "oi, quanto custa a mentoria?" | Linha `entrada` em `wa_mensagens` em menos de 5 s; lead criado no Notion |
| A Camila responde pelo celular | Linha `saida` com origem `smb_message_echoes` |
| Áudio recebido | `midia_id` gravado; transcrição aparece na Interação |
| Número da lista de exclusão manda mensagem | Nada é gravado |
| Reenviar o mesmo webhook (replay manual) | Nenhuma duplicata |
| Corpo com assinatura errada | 401, nada gravado |
| Histórico | `select count(*) from wa_mensagens where origem='history'` cresce nas primeiras horas |

---

## 8. Operação e limites

- **Abrir o WhatsApp Business no celular principal pelo menos a cada 14 dias.** Se o n8n receber
  `account_update` com `PRIMARY_INACTIVITY`, a Camila é alertada.
- **Não suportado na Coexistence:** grupos; mensagens temporárias, de visualização única e
  localização em tempo real (ficam **desligadas** nas conversas 1:1); listas de transmissão (ficam
  somente leitura); chamadas de voz/vídeo; catálogo, status, mensagens de saudação, respostas rápidas
  e etiquetas. Avise a Camila antes do cadastro: **etiquetas, respostas rápidas e mensagem de saudação do app podem deixar de funcionar** (confirmar na tabela de recursos da página de Coexistence).
- Até 4 aparelhos conectados (sem Windows e WearOS). Vazão fixa de 20 msg/s (irrelevante para leitura).
- **Para desfazer:** só pelo celular (WhatsApp Business → Configurações → Conta → Plataforma comercial →
  Desconectar). A API de *deregister* não funciona para números em Coexistence.
- Mensagens enviadas pelo app continuam **gratuitas**. Cobrança só existiria se algo fosse enviado
  pela Cloud API, e este projeto não envia.

---

## 9. Registro do que aconteceu (o Claude local preenche)

- Data do cadastro:
- Caminho usado (A sem Tech Provider / B com Tech Provider):
- Versão da Graph API usada:
- `waba_id` / `phone_number_id`: (não comitar se a Camila preferir; anotar no cofre)
- Desvios em relação a este runbook (nomes de campos, telas, erros e como foram resolvidos):
