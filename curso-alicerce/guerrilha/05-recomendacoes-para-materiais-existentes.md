# Recomendações para os materiais existentes (guerrilha → conversão)

> **Para o orquestrador aplicar.** As trocas estão em ordem de prioridade: **P0** é obrigatório antes de publicar, **P1** tem alto impacto e **P2** é refinamento.
> Os textos "TROCAR" foram copiados dos arquivos **como estavam no momento desta análise**. Se outro agente já editou o arquivo, aplique o "POR" no trecho equivalente.
> Base: `contexto-marca.md` (prova oficial **+400 mentoradas · +2 mil mulheres impactadas**, aulas curtas de propósito, tom de voz, Grande Florianópolis).

---

## P0: Correções obrigatórias (credibilidade)

### P0.1 Prova social desatualizada ("+200") em todos os arquivos
| Arquivo | TROCAR | POR |
|---|---|---|
| `landing-page.html` (hero) | `<p class="prova">Criado por <strong>Camila Martins Finger</strong> · +200 mentoradas</p>` | `<p class="prova">Criado por <strong>Camila Martins Finger</strong> · <strong>+400 mentoradas</strong> · <strong>+2 mil mulheres</strong> impactadas com palestras e treinamentos</p>` |
| `landing-page.html` (sobre) | `<p>Hoje, com <strong>mais de 200 mentoradas</strong>, eu ajudo empresárias a construir negócios lucrativos, organizados e menos dependentes delas.</p>` | `<p>Hoje são <strong>mais de 400 mentoradas</strong> e <strong>mais de 2 mil mulheres impactadas</strong> com palestras e treinamentos, como o <strong>Drink to Talk</strong> (12 edições) e o <strong>Workshop Realize</strong>, na Grande Florianópolis e online. Eu ajudo empresárias a construir negócios lucrativos, organizados e menos dependentes delas.</p>` |
| `copy-divulgacao.md` (descrição completa) | `as 4 fases que já transformaram a rotina de mais de 200 mentoradas:` | `as 4 fases que eu aplico com mais de 400 mentoradas:` *(sem prometer "transformou": é mais seguro)* |
| `copy-divulgacao.md` (bio) | `> Criadora do Método Lucro Anti-Exaustão® · +200 mentoradas` | `> Criadora do Método Lucro Anti-Exaustão® · +400 mentoradas · +2 mil mulheres em palestras` |
| `copy-divulgacao.md` (anúncio B) | `Hoje, mais de 200 mentoradas depois, ele está disponível em formato gravado.` | `Hoje, com mais de 400 mentoradas e mais de 2 mil mulheres impactadas em palestras, ele está disponível em formato gravado, com aulas curtas para empresária sem tempo.` |
| Guia (`Guia_Classroom_Kiwify...md`), seções 6.2, 8.1, 9.1 e 9.2 | todas as ocorrências de `+200 mentoradas` / `mais de 200 mentoradas` | `+400 mentoradas` / `mais de 400 mentoradas` (+ "e mais de 2 mil mulheres impactadas com palestras e treinamentos" na bio longa) |

### P0.2 Porta de entrada para tráfego frio (CTA secundário para o quiz)
**`landing-page.html` (hero), TROCAR:**
```html
      <span class="btn-sub">Acesso imediato · Garantia de 7 dias · Até 12x no cartão</span>
```
**POR:**
```html
      <span class="btn-sub">Acesso imediato · Garantia de 7 dias · Até 12x no cartão</span>
      <a href="LINK_QUIZ?utm_source=lp&utm_medium=hero" style="display:inline-block;margin-top:14px;color:var(--cor-primaria);font-weight:600">Ainda em dúvida? Descubra o seu Índice de Exaustão em 2 min →</a>
```
*(Coloque o mesmo link também no FAQ e no rodapé.)*

### P0.3 Depoimentos vazios: não publicar com espaço reservado
**`landing-page.html`:** enquanto não houver depoimentos autorizados, **TROCAR** o bloco `<div class="depos">…</div>` (3 "DEPOIMENTO REAL") **POR** uma faixa de credenciais verificáveis:
```html
    <div class="depos">
      <div class="depo" style="text-align:center"><p style="font-style:normal;font-family:'Playfair Display',serif;font-size:2.2rem;color:var(--cor-primaria);margin:0">+400</p><span>mentoradas</span></div>
      <div class="depo" style="text-align:center"><p style="font-style:normal;font-family:'Playfair Display',serif;font-size:2.2rem;color:var(--cor-primaria);margin:0">+2 mil</p><span>mulheres impactadas em palestras e treinamentos</span></div>
      <div class="depo" style="text-align:center"><p style="font-style:normal;font-family:'Playfair Display',serif;font-size:2.2rem;color:var(--cor-primaria);margin:0">12</p><span>edições do Drink to Talk</span></div>
    </div>
```
E mude o título `O que dizem as mentoradas` para **`Quem já caminhou comigo`**. Volte para depoimentos assim que a tática 24 (coleta ética) render os primeiros relatos autorizados. **Nenhum nome de cliente sem autorização.**

---

## P1: Alto impacto na conversão

### P1.1 Aulas curtas como DIFERENCIAL (decisão da Camila)
**`landing-page.html` (entregas), TROCAR:**
`<div class="entrega"><div class="ico">🎬</div><h3>+30 aulas gravadas</h3><p>5 módulos práticos, diretos ao ponto, para assistir no seu ritmo.</p></div>`
**POR:**
`<div class="entrega"><div class="ico">🎬</div><h3>+30 aulas de 5 a 8 minutos</h3><p>Curtas de propósito: cada aula termina numa ação para aplicar no mesmo dia. Feito para empresária sem tempo.</p></div>`

**`landing-page.html` (oferta), TROCAR:** `<li>+30 aulas em 5 módulos</li>` **POR:** `<li>+30 aulas curtas (5 a 8 min), cada uma com uma ação prática</li>`

**FAQ: ACRESCENTAR** (antes de "Tem certificado?"):
```html
      <details><summary>Por que as aulas são tão curtas?</summary><p>De propósito. Empresária sem tempo não precisa de mais 40 horas de conteúdo, e sim de clareza e de uma ação por dia. Cada aula tem de 5 a 8 minutos e termina numa ferramenta para usar hoje.</p></details>
```

### P1.2 Âncora de valor real e ética (sem "preço de")
**`landing-page.html` (oferta), TROCAR:**
`<span class="tag">Método Lucro Anti-Exaustão® – Alicerce</span>`
**POR:**
```html
      <span class="tag">Método Lucro Anti-Exaustão® – Alicerce</span>
      <p style="color:var(--cor-texto-suave);font-size:.95rem;margin-top:6px">O mesmo método que eu aplico na mentoria individual (12 encontros em 3 meses), em aulas curtas para você aplicar no seu ritmo.</p>
```
> Se quiser citar o valor da mentoria (ex.: R$ 3.500), use **só o preço vigente real**, como comparação de formato ("mentoria individual: [PREÇO VIGENTE]"), nunca como "de/por".

### P1.3 Público específico (quem se vê no texto, compra)
**`landing-page.html` (hero), TROCAR:**
`<p class="sub">O método em 4 fases para empresárias saírem do caos operacional e construírem uma empresa organizada, lucrativa e menos dependente delas — com tempo para a família e para si mesmas.</p>`
**POR:**
`<p class="sub">Para donas de clínicas, salões, lojas, estúdios e empresas de serviço que faturam, mas vivem apagando incêndio. O método em 4 fases para sair do caos operacional e ter uma empresa organizada, lucrativa e menos dependente de você, com tempo para a família e para si mesma.</p>`

### P1.4 Inimigo cultural + balde furado (a voz da Camila)
**`landing-page.html` (mecanismo), TROCAR:**
`<span class="tag">A verdade que ninguém te contou</span>`
**POR:**
`<span class="tag">"Empresária de verdade dá conta de tudo sozinha." Mentira.</span>`

**E TROCAR:**
`<p class="lead">Isso gera centralização, excesso de decisões, equipe dependente e sobrecarga mental.`
**POR:**
`<p class="lead">É como um balde furado: o lucro entra e vaza por retrabalho, por tarefas que só você faz, por falta de processo, preço mal calculado e urgências. Isso gera centralização, excesso de decisões, equipe dependente e sobrecarga mental.`

**Lista de dores, ACRESCENTAR como último item:**
`<li>Você já pensou: "se mais horas dessem mais lucro, eu já estaria rica".</li>`

### P1.5 Sobre: ativos de autoridade e vulnerabilidade
**`landing-page.html` (sobre), ACRESCENTAR depois do parágrafo "Foi dessa sobrecarga…":**
```html
      <p>Por anos eu trabalhei das 7h às 17h na enfermagem e aprendi que tempo é o recurso mais caro que existe. E aprendi outra coisa: sou casada, sou empresária e até hoje a minha mãe faz comida para mim. Aceitar ajuda não é fraqueza, é estrutura.</p>
      <p>Criei o <strong>Drink to Talk</strong> (12 edições de networking entre empresárias), o <strong>Workshop Realize</strong> (presencial e In Company) e levo palestras como "O Poder da Gestão do Tempo" e "Da procrastinação à AÇÃO!" para empresas e instituições.</p>
```

### P1.6 Escada visível (ascensão)
**`landing-page.html`: ACRESCENTAR** uma seção entre GARANTIA e FAQ:
```html
<section>
  <div class="wrap" style="max-width:760px;text-align:center">
    <span class="tag">E depois do Alicerce?</span>
    <h2>Você não precisa caminhar sozinha</h2>
    <p class="lead">Alunas do Alicerce têm prioridade na <strong>Comunidade Impulso</strong> (encontros em grupo, hot seats e almoço mensal), no próximo <strong>Workshop Realize</strong> e nas vagas de <strong>Mentoria</strong>. Fale comigo no WhatsApp quando quiser dar o próximo passo.</p>
  </div>
</section>
```

### P1.7 Página de obrigado: indicação + VIP + evento
**`obrigado.html`, TROCAR o item 4:**
`<li><strong>Entre no grupo de avisos</strong> para receber lembretes e novidades.</li>`
**POR:**
`<li><strong>Entre na Lista VIP</strong> para saber primeiro do Drink to Talk, do Workshop Realize e das lives "mentorada por um dia".</li>`

**ACRESCENTAR** antes da `<p class="frase">`:
```html
    <p style="margin-top:18px;font-size:.95rem">🎁 <strong>Conhece outra empresária que vive dizendo "se eu não fizer, ninguém faz"?</strong> Depois da Fase 1 você recebe o seu cupom de indicação: ela ganha desconto e você ganha experiências comigo.</p>
```

### P1.8 E-mails: P.S. estratégicos
**`emails/02-boas-vindas-compradora.html`:** antes do bloco "Com carinho," acrescente (no mesmo estilo de `<p>`):
> **P.S.:** As aulas são curtas de propósito (5 a 8 min). Se hoje tu só tiver 10 minutos, assiste a Aula 1 e faz a ação dela. Isso já conta.
> **P.S. 2:** Entra na Lista VIP para saber primeiro do próximo Drink to Talk e das lives "mentorada por um dia": [LINK_GRUPO_VIP]

**`emails/06-conclusao-certificado.html`:** acrescente depois do parágrafo da Comunidade e Mentoria:
> **Indique uma empresária:** com o teu cupom **INDICA-[NOME]**, ela ganha [10%] de desconto e tu ganhas experiências comigo a cada indicação (hot seat, sessão estratégica…). E se quiser viver o método ao vivo, o próximo **Workshop Realize** é em [DATA].
*(E na planilha de automação, troque o botão para levar ao WhatsApp com o texto "Quero meu cupom de indicação".)*

**`emails/07-carrinho-abandonado.html`:** TROCAR
`E lembre: você tem <strong>7 dias de garantia</strong>. Se não for para você, devolvemos 100% do valor.`
POR
`E lembre: as aulas têm de 5 a 8 minutos (cabem no seu dia, de verdade) e você tem <strong>7 dias de garantia</strong>. Se não for para você, devolvemos 100% do valor.`

**`emails/08-lancamento-abertura.html`:** assunto mais polêmico. TROCAR o `<title>` e o comentário ASSUNTO `As inscrições abriram: Método Lucro Anti-Exaustão®` POR `"Empresária de verdade dá conta de tudo sozinha" (não dá)`. Mantenha o pré-cabeçalho "Uma empresa lucrativa não precisa custar a sua paz."

### P1.9 NOVA sequência: 3 e-mails de nutrição para leads do quiz
*(Criar como `emails/10`, `11` e `12` usando o mesmo gerador ou template. Gatilho: lead do quiz que não comprou.)*

**E-mail 10 (imediato)**
- **Assunto:** `Teu Índice de Exaustão: {{INDICE}}/100`
- **Pré-cabeçalho:** "E o que fazer com ele a partir de hoje."
- **Título:** "{{NOME}}, aqui está o teu resultado"
- **Corpo:**
  > O teu Índice de Exaustão deu **{{INDICE}}/100** e o teu perfil é **{{PERFIL}}**.
  > Antes de qualquer coisa: isso não é falta de capacidade. É uma empresa que cresceu sem estrutura compatível com a nova fase. Um balde furado.
  > **Uma ação para hoje (5 minutos):** pega um papel e responde: *"O que eu faço toda semana que não gera resultado e só faço por obrigação?"* Escolhe UMA coisa dessa lista para não fazer esta semana.
  > Amanhã eu te conto qual é o erro mais comum de quem tem o teu perfil.
- **Botão:** "Entrar na Lista VIP" → `LINK_GRUPO_VIP`

**E-mail 11 (D+2)**
- **Assunto:** `O erro de quem tenta "se organizar" sozinha`
- **Pré-cabeçalho:** "Produtividade não é exaustão."
- **Título:** "Por que o planner não resolveu"
- **Corpo:**
  > Quase toda empresária que chega até mim já tentou: planner, app, acordar às 5h. Funciona por duas semanas e depois desanda.
  > Não é falta de disciplina. É que **produtividade sem estrutura é fazer mais rápido o que nem deveria ser teu.**
  > No Método Lucro Anti-Exaustão® a ordem é outra: primeiro **clareza** (Raio-X), depois **como tu funcionas** (comportamento), depois **rotina**, e por fim **a empresa depender menos de ti**.
  > Com mais de 400 mentoradas, eu vi que pular a primeira etapa é o que faz tudo desandar. Clareza antes de tudo.
- **Botão:** "Ver como o método funciona" → `LINK_LP?utm_source=email&utm_campaign=nutricao-quiz`

**E-mail 12 (D+5)**
- **Assunto:** `Aulas de 5 minutos (de propósito)`
- **Pré-cabeçalho:** "O método inteiro, do jeito que cabe na tua semana."
- **Título:** "O Alicerce cabe na tua rotina"
- **Corpo:**
  > Eu gravei o Método Lucro Anti-Exaustão® com uma regra: **aula curta, ação no mesmo dia.** São mais de 30 aulas de 5 a 8 minutos, em 4 fases, com as planilhas de cada ferramenta.
  > É o mesmo método da minha mentoria individual, para tu aplicares no teu ritmo.
  > O teu resultado no teste indicou começar por: **{{FASE_RECOMENDADA}}**.
  > R$ 497 ou em até 12x, com 7 dias de garantia.
  > Se preferir conversar antes, me responde este e-mail ou chama no WhatsApp.
- **Botão:** "Quero começar pelo Alicerce" → `LINK_LP?utm_source=email&utm_campaign=nutricao-quiz`

---

## P2: Refinamentos

### P2.1 `copy-divulgacao.md`
- **Seção 2 (Bio), TROCAR o bloco inteiro POR:**
  > Camila Martins Finger | Mentora Anti-Exaustão
  > Empresária de verdade NÃO dá conta de tudo sozinha 💛
  > Método Lucro Anti-Exaustão® · +400 mentoradas · +2 mil mulheres em palestras
  > Drink to Talk · Workshop Realize · Grande Floripa
  > ⬇️ Faça o teste: qual é o teu Índice de Exaustão?
  *(O link da bio aponta para o quiz, não direto para a página de vendas.)*
- **Seção 3 (Carrossel), legenda:** TROCAR `👉 Link na bio para conhecer.` POR `👉 Comenta LUCRO que eu te mando o teste do Índice de Exaustão.`
- **Seção 5 (Reels), CTA:** TROCAR `Comenta MÉTODO que eu te mando o link.` POR `Comenta LUCRO que eu te mando o link.` *(padronizar o CTA da marca)*
- **Seção 8 (Calendário de 7 dias):** acrescentar no topo: "Para o calendário completo de 30 dias e o plano de 90 dias, veja `guerrilha/04-conteudo-guerrilha-30-dias.md` e `guerrilha/00-plano-guerrilha-90-dias.md`."
- **Seção 6 (WhatsApp), acrescentar o script "Ex-participante do Realize/Drink to Talk"** (copiar do arquivo 03, item 1.1b).

### P2.2 Guia (`Guia_Classroom_Kiwify_Lucro_Anti-Exaustao.md`)
- **Seção 7.3 (Cupons):** acrescentar a linha `INDICA-[NOME]` | 10% | alunas e mentoradas que indicam | sem limite, validade de 6 meses (ver `guerrilha/02-programa-indicacao.md`).
- **Seção 7, novo item 7.4 "Licenças B2B e In Company":** "Empresa ou rede compra N acessos → liberação manual na Kiwify (gratuita) → controle na planilha 'Controle de Acessos' com Origem = B2B/[empresa]."
- **Seção 6.5 (Pixels):** acrescentar "Use UTMs em todos os links (padrão em `guerrilha/00`, seção 6) e confira se o relatório de vendas da Kiwify registra as UTMs."
- **Seção 8.1 (Estrutura da LP):** incluir o "Ainda em dúvida? Faça o teste" (P0.2), a faixa de credenciais (P0.3) e a seção de escada (P1.6).
- **Seção 0 (Visão geral):** acrescentar a linha "Publicar o quiz Índice de Exaustão e o grupo VIP **antes** de divulgar a página de vendas."

### P2.3 `landing-page.html`: SEO e compartilhamento
- `<title>`: TROCAR `Método Lucro Anti-Exaustão® – Alicerce` POR `Método Lucro Anti-Exaustão® – Alicerce | Camila Martins Finger`
- `og:description`: TROCAR `Curso gravado em 4 fases + planilhas de ferramentas. Por Camila Martins Finger.` POR `Aulas curtas, 4 fases e planilhas de cada ferramenta. Por Camila Martins Finger: +400 mentoradas e +2 mil mulheres impactadas.`

### P2.4 Bônus que alavancam guerrilha (se o outro agente já criou os complementares)
- Use o **e-book "Raio-X da Empresária Exausta"** (`complementares/ebook-raio-x-empresaria-exausta.pdf`) como **segunda isca**: entregue no fim do quiz e no pós-palestra ("baixe o e-book da palestra").
- O **assistente de IA** (`complementares/ia/`) entra como bônus na oferta da página de vendas ("Assistente Anti-Exaustão: tire dúvidas sobre as ferramentas a qualquer hora") **e** como argumento no B2B (escala para redes).
- O **workbook** pode ir impresso como brinde de luxo no Workshop Realize (alunas do Alicerce).

---

## Resumo: as 5 mudanças mais importantes
1. **Trocar "+200" por "+400 mentoradas · +2 mil mulheres impactadas" em todos os arquivos** (P0.1).
2. **Colocar um CTA secundário para o quiz no hero** e apontar a bio para o quiz, não para o checkout (P0.2, P2.1).
3. **Trocar os depoimentos vazios por uma faixa de credenciais verificáveis** até haver relatos autorizados (P0.3).
4. **Transformar "aulas curtas" em diferencial** na página de vendas, no FAQ e nos e-mails (P1.1).
5. **Criar a nutrição de 3 e-mails para os leads do quiz** e os P.S. de indicação e Lista VIP (P1.8, P1.9).
