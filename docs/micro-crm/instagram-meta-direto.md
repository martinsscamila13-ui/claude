# Instagram direto na Meta: runbook para o Claude Code local

> **Para quem:** o Claude Code no computador da Camila, operando o Chrome (extensão Claude in Chrome)
> e o n8n dela. Siga as regras gerais de [`runbook-projeto-completo.md`](runbook-projeto-completo.md)
> (pontos de parada, segredos, registro em `STATUS.md`).
> **[CAMILA]** = só ela faz (senha, código, aceite, celular). **[CLAUDE·CHROME]** = o Claude faz no
> navegador. **[CLAUDE·TERMINAL]** = o Claude faz por API, SQL e arquivos.
>
> **Objetivo:** receber no n8n **todas as DMs** do Instagram profissional da Camila: as que ela
> recebe e as que ela envia pelo app (`is_echo`). Comentários são opcionais. Cada conversa vira lead no
> Notion. **Somente leitura:** o CRM nunca responde pelo Instagram.
>
> API usada: **Instagram API with Instagram Login** (host `graph.instagram.com`), que não exige página do
> Facebook. Doc: <https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/messaging-api>
> Pesquisa de 18/10/2026: confirme cada tela na doc oficial antes de seguir.

---

## 1. Pré-requisitos

- [ ] **[CAMILA]** A conta do Instagram é **profissional** (Criadora de conteúdo ou Empresa).
- [ ] **[CAMILA]** No **app do Instagram no celular**: *Configurações → Mensagens e respostas ao story →
      Controles de mensagem → Ferramentas conectadas → **Permitir acesso às mensagens*** = ligado.
      Sem isso, a API não entrega as DMs.
- [ ] Portfólio empresarial Meta com verificação em dois fatores, conta em developers.facebook.com e política de
      privacidade pública (fase 0 do runbook geral).
- [ ] n8n no ar em HTTPS e banco `crm` no Postgres (fase 1 do runbook geral).

---

## 2. Criar o app

Recomendação: **um app só para o Instagram** ("CRM Camila – Instagram"), separado do app do WhatsApp.
Assim uma análise de app de um lado não trava o outro.

1. **[CLAUDE·CHROME]** developers.facebook.com → **Meus apps → Criar app**.
   - Caso de uso: **"Gerenciar mensagens e conteúdo no Instagram"** (Instagram API)
   - Vincular ao portfólio empresarial da Camila
   - 🛑 Se a Meta pedir senha ou reautenticação: parar e chamar a Camila.
2. **[CLAUDE·CHROME]** *Configurações do app → Básico*: ícone, URL da política de privacidade,
   categoria, e-mail de contato. Salvar.
3. **[CLAUDE·CHROME]** Abrir *Casos de uso → Instagram → **Configuração da API com login do Instagram***.
   Nessa tela aparecem o **ID do app do Instagram** e a **Chave secreta do app do Instagram**, que são
   **diferentes** do App ID/App Secret do Facebook. 🛑 Pedir à Camila que copie a chave secreta direto
   para o cofre e para a credencial do n8n. O Claude não lê nem anota segredos.

---

## 3. Receptor no n8n (antes de ligar o webhook)

### 3.1 Tabelas — [CLAUDE·TERMINAL]

```sql
create table if not exists ig_mensagens (
  id           text primary key,          -- message.mid → idempotência
  igsid        text not null,             -- ID do cliente no Instagram (escopo do app)
  direcao      text not null check (direcao in ('entrada','saida')),  -- is_echo = saida
  tipo         text not null,             -- text | image | audio | video | share | story_mention | story_reply | reel | ...
  texto        text,
  anexo_url    text,
  enviada_em   timestamptz not null,
  bruto        jsonb not null,
  recebida_em  timestamptz not null default now(),
  analisada    boolean not null default false
);
create index if not exists ig_mensagens_igsid_idx on ig_mensagens (igsid, enviada_em);

create table if not exists ig_perfis (
  igsid        text primary key,
  username     text,
  nome         text,
  seguidores   integer,
  segue_voce   boolean,
  atualizado   timestamptz not null default now()
);

create table if not exists ig_comentarios (     -- opcional
  id text primary key, igsid text, username text, texto text, media_id text,
  criado_em timestamptz, bruto jsonb not null
);
```

Visão unificada com o WhatsApp, que a análise por LLM e o MCP vão ler:

```sql
create or replace view mensagens as
  select 'whatsapp' canal, id, wa_id contato, direcao, tipo, texto, enviada_em, analisada from wa_mensagens
  union all
  select 'instagram', id, igsid, direcao, tipo, texto, enviada_em, analisada from ig_mensagens;
```

(Se o WhatsApp ainda não estiver feito, crie a visão só com o Instagram e recrie depois.)

### 3.2 Fluxo "IG · webhook" — [CLAUDE·TERMINAL]

- Webhook no caminho `instagram`, métodos **GET e POST**, *raw body* ligado.
- **GET:** se `hub.mode == 'subscribe'` e `hub.verify_token` == token guardado → responder `hub.challenge`
  em texto puro (200). Senão, 403.
- **POST:**
  1. Validar `X-Hub-Signature-256` com HMAC-SHA256 do corpo bruto usando a **chave secreta do app do
     Instagram**. Se não bater → 401.
  2. Responder 200 já. Processar em seguida.
  3. `entry[].messaging[]`: `sender.id`, `recipient.id`, `timestamp`, `message.mid`, `message.text`,
     `message.attachments[]`, `message.is_echo`. Se `is_echo = true`, `direcao='saida'` e o cliente é o
     `recipient.id`. Senão, `direcao='entrada'` e o cliente é o `sender.id`. Também chegam `message_reactions`,
     `messaging_seen` e mensagens apagadas (`is_deleted`): registre só o que interessa ao CRM.
  4. `entry[].changes[]` com `field = comments` (opcional): gravar em `ig_comentarios`. Comentários com
     sinais de compra ("quero", "valor", "como entro") geram lead com Origem = Instagram (comentário).
  5. `insert ... on conflict (id) do nothing`.
  6. Se o `igsid` ainda não estiver em `ig_perfis`, buscar o perfil:
     `GET https://graph.instagram.com/<VERSAO>/<IGSID>?fields=name,username,follower_count,is_user_follow_business,is_business_follow_user`
     com o token (só funciona para quem já mandou mensagem).
  7. Chamar o subfluxo comum **"Lead · upsert"** (canal = instagram, contato = igsid, @username, nome).
  8. Marcar a conversa como pendente de análise.
- **Capture os primeiros payloads reais** em `bruto` e ajuste o mapeamento a partir deles.

---

## 4. Token e webhook — [CLAUDE·CHROME] com a Camila

1. Na tela *Configuração da API com login do Instagram* → **1. Gerar tokens de acesso → Adicionar conta**.
   🛑 **[CAMILA]** faz o login do Instagram no pop-up e aceita as permissões
   (`instagram_business_basic`, `instagram_business_manage_messages`; `instagram_business_manage_comments`
   se for usar comentários). Se pedir convite de testadora, aceitar em
   instagram.com → Configurações → Apps e sites (ou pela notificação).
2. **Gerar token**. 🛑 A Camila copia para a credencial do n8n "IG token" e para o cofre. O token é de
   longa duração (~60 dias).
3. **2. Configurar webhooks:**
   - URL de callback: `https://<DOMINIO_N8N>/webhook/instagram`
   - Token de verificação: o mesmo do fluxo (gerado pelo Claude e guardado em variável do n8n)
   - **Verificar e salvar.** Se falhar: o fluxo "IG · webhook" precisa estar **ativo** e a URL de produção
     (não a de teste) precisa estar no campo.
   - Assinar os campos: **`messages`** (obrigatório); `message_reactions`, `messaging_seen` e `comments` (opcional).
4. **[CLAUDE·TERMINAL]** Ativar a assinatura da conta:
   ```
   POST https://graph.instagram.com/<VERSAO>/me/subscribed_apps?subscribed_fields=messages,comments&access_token=<TOKEN>
   ```
   Conferir com `GET .../me/subscribed_apps`.
5. **[CLAUDE·CHROME]** Colocar o app **Ao vivo** (*Publicar* no painel). 🛑 Confirmar com a Camila antes,
   porque é uma ação visível para a Meta.

### Acesso padrão × avançado

- Contas que a própria empresa possui e que têm papel no app funcionam com **Acesso padrão**.
- Teste com uma conta **sem papel no app** (uma amiga). Se as DMs dela **não chegarem**, é preciso
  **Acesso avançado** para `instagram_business_manage_messages`: *Análise do app → Permissões e
  recursos → Solicitar*. Pode exigir **verificação da empresa** e um vídeo mostrando o uso (o n8n
  recebendo a DM e o lead aparecendo no CRM). 🛑 Preparar o texto e o vídeo com a Camila. Quem envia é ela.

---

## 5. Fluxos complementares — [CLAUDE·TERMINAL]

- **"IG · renovar token"** (agendado a cada 30 dias):
  `GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=<TOKEN>`
  → atualizar a credencial pela API do n8n. Se falhar, alertar a Camila: sem token, a busca de perfis e o
  histórico param (os webhooks continuam chegando).
- **"IG · importar histórico"** (rodar uma vez): listar conversas
  `GET https://graph.instagram.com/<VERSAO>/me/conversations?platform=instagram&fields=participants,updated_time`
  e, para cada uma, `GET /<CONVERSATION_ID>?fields=messages{id,created_time,from,to,message}`.
  A API só devolve as **mensagens mais recentes** de cada conversa (cerca de 20) e não traz DMs paradas há mais de 30
  dias na pasta *Solicitações*. Gravar como `origem` histórico, sem disparar alertas.
- **"Saúde"** (diário): se não chegar nenhuma DM em 48h, avisar a Camila (o token ou a assinatura pode ter caído).

---

## 6. Identidade entre canais

A mesma pessoa pode aparecer no Instagram (IGSID/@) e no WhatsApp (telefone). Regra:
- Quando uma DM contiver um telefone, ou uma mensagem de WhatsApp citar um @, o fluxo de análise
  **sugere** juntar os leads (campo "Possível duplicado" no Notion).
- A junção só acontece **depois da confirmação da Camila** (pelo Grok Bot ou no Notion).

---

## 7. Testes de aceite

| Teste | Esperado |
|---|---|
| Amiga **sem papel no app** manda DM "quanto custa a mentoria?" | Linha `entrada` em `ig_mensagens` em menos de 5 s; perfil em `ig_perfis`; lead "Novo contato" no Notion com o @ |
| A Camila responde pelo app | Linha `saida` (`is_echo`) |
| Resposta a story / menção | `tipo` story_reply / story_mention gravado |
| Foto ou áudio | `anexo_url` gravado (a URL expira: baixar logo, se for usar) |
| Replay do mesmo webhook | Nenhuma duplicata |
| Assinatura errada | 401 |
| Comentário "quero" num post (se ativado) | Lead com origem comentário |

---

## 8. Limites conhecidos

- A conversa só existe se a pessoa **escrever primeiro**. Não há prospecção ativa pela API.
- DMs na pasta **Solicitações** paradas há mais de 30 dias não voltam pela API.
- Post compartilhado chega **só como link**.
- Mensagens de grupo não são suportadas.
- O token expira em ~60 dias se não for renovado (seção 5).
- A janela de 24h para responder não importa aqui: o CRM não envia nada.

---

## 9. Registro (o Claude preenche ao terminar)

- Data:
- Versão da Graph API:
- Acesso padrão bastou? (sim/não; se não, data do pedido e da aprovação do avançado):
- Campos assinados:
- Desvios em relação a este runbook:
