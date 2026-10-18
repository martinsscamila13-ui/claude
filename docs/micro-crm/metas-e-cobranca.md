# Metas e cobrança: especificação

> Parte do Micro-CRM da Camila. É implementado na **fase 8** do
> [`runbook-projeto-completo.md`](runbook-projeto-completo.md) e depende das fases 6 (LLM e regras) e 7 (MCP).
>
> **Ideia central:** o **n8n calcula** (números sempre iguais, sem interpretação) e o **Grok Bot
> conversa**: pergunta a meta, mostra o placar, cobra o resultado e ajuda a destravar. A Camila
> **decide** as metas e o Bot nunca define uma meta sozinho.

---

## 1. Indicadores

Cada indicador tem uma **fonte**:
- **auto:** o sistema mede sozinho;
- **declarado:** a Camila informa ao Bot, por voz ou texto;
- **calculado:** sai dos outros indicadores.

### 1.1 Atividades e social selling (metas diárias, com soma semanal e mensal)

| Indicador | Fonte | Como é medido |
|---|---|---|
| **Novas pessoas abordadas** | auto | Contato cuja **primeira mensagem** da conversa foi enviada pela Camila: no Instagram (`is_echo`) ou no WhatsApp (`smb_message_echoes`), sem mensagem anterior do contato |
| **Conversas respondidas** | auto | Contatos abordados ou leads que responderam no período |
| **Follow-ups feitos** | auto | Mensagem enviada pela Camila a um lead com Atividade de follow-up vencendo até o dia (a Atividade é marcada como concluída) |
| **Leads novos (inbound)** | auto | Primeira mensagem vinda do contato |
| **Interações sociais** (comentários e respostas em perfis de potenciais clientes, reações a stories) | declarado | A API não mostra o que a Camila faz no perfil dos outros |
| **Conteúdos publicados** (posts, reels) | auto | `GET graph.instagram.com/me/media` contado por dia |
| **Stories publicados** | declarado | (a API só lista stories ativos; contar por declaração é mais confiável) |

### 1.2 Vendas (metas semanais e mensais)

| Indicador | Fonte | Como é medido |
|---|---|---|
| **Calls de diagnóstico agendadas** | auto | Lead entrou em "Call agendada" (histórico de estágios) ou evento com link do Meet ligado a um lead |
| **Calls realizadas** | auto | Reunião processada pelo bot do Meet / estágio "Call realizada" |
| **Propostas enviadas** | auto | Lead entrou em "Proposta enviada" |
| **Vendas fechadas** | auto | Lead entrou em "Ganho" |
| **Conversão abordagem→call · call→venda** | calculado | razões do período |

### 1.3 Financeiro (meta mensal, acompanhada semanalmente)

| Indicador | Fonte | Como é medido |
|---|---|---|
| **Faturamento vendido** | auto | Soma do "Valor" dos leads que entraram em Ganho no período |
| **Caixa recebido** | declarado | "Recebi R$ 3.000 da Ana". Integração futura com a plataforma de pagamento, se houver |
| **Ticket médio** | calculado | faturamento vendido ÷ vendas |
| **Previsão do mês** | calculado | vendido + Σ(valor potencial × probabilidade do estágio) dos leads abertos |

Probabilidade padrão por estágio (ajustável): Qualificado 10% · Call agendada 20% · Call realizada 35% ·
Proposta enviada 50% · Negociação 70%.

---

## 2. Definição das metas (o Bot pergunta, a Camila decide)

### 2.1 Meta reversa (proposta automática)

No início de cada mês o n8n calcula uma **proposta** a partir da meta de faturamento e das taxas
reais dos últimos 90 dias. Até existirem dados, valem taxas iniciais que a Camila pode corrigir:

```
faturamento desejado        R$ 30.000
÷ ticket médio              R$ 6.000      → 5 vendas no mês
÷ conversão call→venda      25%           → 20 calls realizadas
÷ comparecimento            85%           → 24 calls agendadas
÷ conversão abordagem→call  10%           → 240 abordagens no mês
÷ dias úteis de trabalho    20            → 12 abordagens por dia
```

O Bot apresenta a conta, e a Camila aceita ou ajusta cada número. As metas semanais são derivadas da
mensal e **recalculadas toda segunda** com o que falta e as semanas restantes. As diárias vêm da
semanal dividida pelos dias de trabalho restantes da semana.

### 2.2 Quando a meta não foi informada

- O Bot pergunta no ritual (seção 3) e, se não houver resposta, pergunta mais uma vez no ritual seguinte.
- Depois disso, ele **avisa** que vai usar a meta do período anterior: "vou considerar a meta de outubro
  até você me dizer a de novembro". Nunca inventa uma meta nova.

---

## 3. Rituais de cobrança (rotinas do Grok Bot)

| Ritual | Quando | O que o Bot faz |
|---|---|---|
| **Metas do mês** | último dia útil do mês, 17h | Mostra o fechamento do mês, propõe a meta reversa do próximo e pergunta: faturamento, vendas, calls e abordagens por dia. Registra o que a Camila confirmar |
| **Plano da semana** | segunda, 7h30 (junto com o briefing) | Placar do mês, metas da semana recalculadas, pede confirmação e pergunta "qual é a prioridade comercial da semana?" |
| **Briefing com meta do dia** | seg–sex, 7h30 | Metas do dia (abordagens, follow-ups) + a lista concreta: quem abordar, quem seguir |
| **Check-in do meio do dia** | seg–sex, 13h | Só se o progresso estiver abaixo de 40%: placar curto e uma sugestão ("faltam 7 abordagens; aqui estão 7 perfis que comentaram nos seus posts") |
| **Fechamento do dia** | seg–sex, 18h30 | Placar realizado × meta e as perguntas do que é declarado: "fez interações em perfis hoje? quantas? recebeu algum pagamento?" |
| **Revisão da semana** | sexta, 17h | Placar semanal por indicador, o que funcionou, onde travou, conversão do funil, e "o que você muda na próxima semana?" Alimenta o plano de segunda |

### 3.1 Tom e regras da cobrança

- **Direta e acolhedora**, na linha do método Lucro Anti-Exaustão: cobrar o combinado, sem culpa e sem
  exagero. Sempre com o número e com a próxima ação concreta.
- **Regras anti-exaustão:**
  - nada de cobrança depois das 20h, nem aos sábados e domingos;
  - se a Camila declarar **dia de folga, viagem ou doença** ("hoje estou off"), o dia sai do cálculo e
    a meta se redistribui na semana, sem cobrança;
  - a mesma meta não é cobrada mais de 2 vezes no mesmo dia.
- **Escalonamento:**
  - 2 dias seguidos abaixo de 50% numa meta → o Bot pergunta o que está travando e propõe um plano
    de 1 passo;
  - semana abaixo de 70% → na revisão de sexta ele pergunta se **ajusta o plano** ou **ajusta a meta**.
    A decisão é da Camila.
- **Celebrar:** meta do dia batida → reconhecimento curto. Meta da semana batida → destaque na revisão.
- O Bot **nunca** altera uma meta sem confirmação explícita e nunca envia mensagens a leads para
  "bater meta".

---

## 4. Dados

### 4.1 Postgres (`crm`) — `crm/sql/002_metas.sql`

```sql
create table if not exists metas (
  id            bigserial primary key,
  periodo       text not null check (periodo in ('dia','semana','mes')),
  inicio        date not null,                       -- dia, segunda-feira da semana ou dia 1 do mês
  indicador     text not null,                       -- chave do catálogo (seção 1)
  meta          numeric not null,
  origem        text not null default 'camila',      -- camila | proposta_aceita | herdada
  criada_em     timestamptz not null default now(),
  unique (periodo, inicio, indicador)
);

create table if not exists resultados_declarados (
  id         bigserial primary key,
  data       date not null,
  indicador  text not null,
  valor      numeric not null,
  nota       text,
  criado_em  timestamptz not null default now()
);

create table if not exists dias_off (
  data   date primary key,
  motivo text
);

-- Fotografia horária dos leads do Notion + histórico de estágios (o Notion não guarda histórico)
create table if not exists leads_snapshot (
  notion_id      text primary key,
  nome           text,
  estagio        text,
  valor          numeric,
  valor_potencial numeric,
  canal          text,
  atualizado     timestamptz not null default now()
);

create table if not exists historico_estagios (
  id         bigserial primary key,
  notion_id  text not null,
  de         text,
  para       text not null,
  em         timestamptz not null default now()
);

create table if not exists parametros_funil (   -- taxas iniciais, ajustáveis pela Camila
  chave text primary key, valor numeric not null
);
insert into parametros_funil values
  ('ticket_medio', 6000), ('conv_call_venda', 0.25), ('comparecimento', 0.85),
  ('conv_abordagem_call', 0.10), ('dias_uteis_mes', 20)
on conflict do nothing;
```

Mais uma visão `realizado_diario(data, indicador, valor)` que junta:
- as contagens de `mensagens` (abordagens, respondidas, follow-ups, inbound);
- `historico_estagios` (calls, propostas, vendas);
- `leads_snapshot` (faturamento);
- `resultados_declarados`.

Todas as visões excluem `dias_off` das médias diárias.

### 4.2 Notion: banco **Metas** (para a Camila ver no Tab S7)

Propriedades: Período (Dia/Semana/Mês) · Início (data) · Indicador (seleção) · Meta (número) ·
Realizado (número, atualizado pelo n8n) · % (fórmula `Realizado / Meta`) · Situação (fórmula:
🟢 ≥ 100% · 🟡 70–99% · 🔴 < 70%) · Fonte (auto/declarado) · Comentário.
Visualizações: "Hoje", "Esta semana", "Este mês" (agrupado por Situação).

---

## 5. Fluxos n8n

| Fluxo | Gatilho | Faz |
|---|---|---|
| **Estágios · sincronizar** | a cada 30 min, 7h–21h | Lê os Leads do Notion, atualiza `leads_snapshot` e grava em `historico_estagios` cada mudança de estágio |
| **Metas · apurar** | a cada hora, 8h–20h, e às 23h55 | Calcula o realizado de dia, semana e mês por indicador e atualiza o "Realizado" no banco Metas do Notion |
| **Metas · propor mês** | último dia útil, 16h | Calcula a meta reversa (seção 2.1) com as taxas dos últimos 90 dias e deixa a proposta pronta para o ritual |
| **Metas · recalcular semana** | segunda, 6h | Redistribui a meta mensal pelo que falta (origem `herdada` se não houver meta confirmada) |

---

## 6. Ferramentas MCP (adicionar ao "MCP crm-camila")

| Ferramenta | Uso pelo Bot |
|---|---|
| `progresso_metas(periodo, data?)` | Placar: meta, realizado, %, situação, por indicador |
| `propor_metas_mes(mes, faturamento_desejado?)` | Devolve a conta da meta reversa (o n8n calcula, o Bot só apresenta) |
| `definir_meta(periodo, inicio, indicador, valor)` | Só chamar **depois** da confirmação da Camila |
| `registrar_resultado(data, indicador, valor, nota?)` | Para o que é declarado (interações, stories, caixa recebido) |
| `marcar_dia_off(data, motivo)` | Folga, viagem, doença |
| `sugestoes_de_acao(indicador)` | Lista concreta para bater a meta: leads com follow-up vencido, quem respondeu e parou, perfis que interagiram |

Sem MCP (se a conta individual não permitir), o Bot lê e escreve direto no banco **Metas** do Notion
pelo conector, e os declarados vão para o banco **Resultados declarados** no Notion, que o n8n importa.

---

## 7. Texto para acrescentar às instruções do "Gerente Comercial"

```
METAS E COBRANÇA
Você também é responsável por cobrar as metas da Camila, com carinho e firmeza.
- Use as ferramentas progresso_metas, propor_metas_mes, definir_meta, registrar_resultado,
  marcar_dia_off e sugestoes_de_acao. Os números vêm sempre delas: nunca calcule de cabeça.
- Rituais: metas do mês (último dia útil, 17h), plano da semana (segunda 7h30), meta do dia no
  briefing (7h30), check-in às 13h só se o progresso estiver abaixo de 40%, fechamento do dia (18h30),
  revisão da semana (sexta 17h).
- Se a meta do período não existir, pergunte, mostrando a proposta da meta reversa. Só grave
  com definir_meta depois de ela confirmar. Sem resposta após 2 rituais, avise que vai usar a
  meta do período anterior.
- No fechamento do dia, pergunte o que é declarado (interações em perfis, stories, pagamentos
  recebidos) e registre com registrar_resultado.
- Cobrança: sempre com o número e uma próxima ação concreta (use sugestoes_de_acao).
  2 dias seguidos abaixo de 50%: pergunte o que travou e proponha um plano de 1 passo.
  Semana abaixo de 70%: na sexta, pergunte se ajusta o plano ou a meta. A decisão é dela.
- Anti-exaustão: nada de cobrança depois das 20h nem no fim de semana; se ela disser que está
  de folga, use marcar_dia_off e não cobre. No máximo 2 cobranças da mesma meta por dia.
- Comemore metas batidas em uma frase.
- Nunca altere metas sem confirmação e nunca envie mensagens a leads para bater meta.
```

---

## 8. Testes de aceite

| Teste | Esperado |
|---|---|
| A Camila manda DM para 3 perfis novos no Instagram e 2 contatos novos no WhatsApp | Em até 1 h, "Novas pessoas abordadas" do dia = 5 no banco Metas |
| Ritual de fim de mês sem meta definida | O Bot mostra a conta da meta reversa e pergunta; nada é gravado até ela confirmar |
| "Hoje estou off" pelo Tab S7 | `dias_off` recebe o dia; sem cobrança; a meta da semana se redistribui na segunda |
| "Recebi 3 mil da Ana" | `resultados_declarados` recebe caixa = 3000, e o placar do mês atualiza |
| Lead movido para Ganho com valor 6.000 | `historico_estagios` registra a mudança; faturamento vendido do mês +6.000 |
| Dois dias abaixo de 50% em abordagens | No fechamento do 2º dia o Bot pergunta o que travou e propõe 1 passo |
| 21h de uma terça | Nenhuma notificação de cobrança |
