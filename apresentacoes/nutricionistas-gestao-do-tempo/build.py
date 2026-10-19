import math, pathlib

OUT = pathlib.Path(__file__).parent
QR_TEST = (OUT / "qr.svg").read_text()
QR_INSTA = (OUT / "qr_insta.svg").read_text()

def waves(w=900, h=520, n=14, color="#FBF6F1", op=0.55, amp=70, freq=1.25, tilt=0.35, sw=1.4):
    paths = []
    for i in range(n):
        pts = []
        off = i * (h / (n * 1.6)); ph = i * 0.18
        for x in range(0, w + 1, 12):
            y = h * 0.55 + off - x * tilt + amp * math.sin(x / w * freq * 2 * math.pi + ph)
            pts.append(f"{x},{y:.1f}")
        paths.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-opacity="{op}"/>')
    return f'<svg class="waves" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(paths)}</svg>'

SLIDES = []
def add(html, cls="cream", deco=""):
    SLIDES.append((cls, html, deco))

def quote(text, sub=None):
    add(f"""
<div class="topbar"></div>
<div class="quote-wrap">
  <div class="qmark">&ldquo;</div>
  <p class="quote">{text}</p>
  {f'<p class="qsub">{sub}</p>' if sub else ''}
  <p class="handle">@martinsscamila</p>
</div>
<div class="bottombars"><div></div><div></div></div>
""", "paper nofoot")

def section(num, title, sub):
    add(f"""
<div class="sec"><div class="sec-n">{num}</div><h2 class="sec-t">{title}</h2><p class="sec-s">{sub}</p></div>
""", "dark nofoot", waves(1100, 520, 18, "#B65F3A", 0.55))

def qr_slide(tag, title, steps, foot, qr):
    lis = "".join(f"<li>{s}</li>" for s in steps)
    add(f"""
<div class="qr-wrap">
  <div>
    <div class="tag light">{tag}</div>
    <h2 class="title light huge">{title}</h2>
    <ol class="steps-v">{lis}</ol>
    <p class="url">{foot}</p>
  </div>
  <div class="qr">{qr}</div>
</div>
""", "dark nofoot", "")

# 1 CAPA
add("""
<div class="min-cover">
  <div class="mc-top">Gestão do tempo para nutricionistas</div>
  <h1 class="mega">Agenda cheia,<br>vida em equilíbrio</h1>
  <div class="mc-line"></div>
  <div class="mc-name">Camila Martins Finger</div>
</div>
""", "terra nofoot", waves(900, 360, 12, "#FBF6F1", 0.22))

# 2
quote("Você cuida da alimentação<br>de todo mundo.<br>Quem está cuidando da sua agenda?")

# 3
add("""
<div class="tag light">Dinâmica · 5 min</div>
<h2 class="title light">Quero conhecer vocês</h2>
<div class="prompts">
  <div class="prompt"><span class="pn">01</span><p>Qual <b>palavra</b> define a sua rotina hoje?</p></div>
  <div class="prompt"><span class="pn">02</span><p>De 0 a 10: quanto da sua agenda <b>é realmente sua</b>?</p></div>
</div>
""", "dark", waves(900, 460, 16, "#FBF6F1", 0.28))

# 4
add("""
<h2 class="title">Prazer, Camila.</h2>
<p class="sub">Venho da saúde, como vocês. E sei o que é não ter tempo.</p>
<div class="timeline">
  <div class="tl"><div class="dot"></div><div class="tl-k">Origem</div><h4>Técnica de enfermagem</h4><p>Rotina das 7h às 17h, ônibus, plantão. Cuidando de todo mundo.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Virada</div><h4>Maternidade e empresa na pandemia</h4><p>Aprendi a empreender com pouco tempo e muita coisa ao mesmo tempo.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Método</div><h4>Lucro Anti-Exaustão®</h4><p>Para mulheres que querem crescer sem pagar o crescimento com a própria saúde.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Hoje</div><h4>Mentora de empresárias</h4><p>Profissionais liberais que saíram do modo “faço tudo sozinha”.</p></div>
</div>
<p class="statement">Uma empresa lucrativa <em>não precisa custar a paz da mulher que a construiu.</em></p>
""")

# 5 INSTAGRAM
qr_slide("Vamos manter contato", "@martinsscamila",
         ["Aponte a câmera para o QR code", "Me siga: conteúdo de gestão e rotina toda semana", "Ficou alguma dúvida? <b>Me chama no direct</b>"],
         "instagram.com/martinsscamila", QR_INSTA)

# 6 AGENDA
add("""
<h2 class="title">O que vamos ver hoje</h2>
<div class="agenda">
  <div class="ag"><span class="n">01</span><span class="d">A rotina da nutri real</span></div>
  <div class="ag"><span class="n">02</span><span class="d">Os ladrões do seu tempo</span></div>
  <div class="ag"><span class="n">03</span><span class="d">MBTI · teste de personalidade ao vivo</span></div>
  <div class="ag"><span class="n">04</span><span class="d">A semana modelo da nutri</span></div>
  <div class="ag"><span class="n">05</span><span class="d">Ferramentas: Google Agenda, Trello, Notion, agenda física e planner</span></div>
  <div class="ag"><span class="n">06</span><span class="d">Seu plano de 7 dias</span></div>
</div>
""", "cream ag-notime", waves(700, 380, 12, "#B65F3A", 0.35))

# 7
section("01", "A rotina da nutri real", "Sozinha, centralizadora e com demanda que não para.")

# 8 VOCÊ SE RECONHECE
add("""
<h2 class="title">Você se reconhece?</h2>
<div class="grid3">
  <div class="tile"><span class="ti">01</span><h4>Faz tudo sozinha</h4><p>Atende, monta plano, responde WhatsApp, posta, cobra e ainda estuda.</p></div>
  <div class="tile"><span class="ti">02</span><h4>No máximo, uma secretária</h4><p>E mesmo assim tudo passa por você antes de sair.</p></div>
  <div class="tile"><span class="ti">03</span><h4>“Ninguém faz como eu”</h4><p>Centralizar parece mais rápido. Até virar gargalo.</p></div>
  <div class="tile"><span class="ti">04</span><h4>Demanda que não para</h4><p>Paciente novo, retorno, dúvida, encaixe, mensagem às 23h.</p></div>
  <div class="tile"><span class="ti">05</span><h4>Plano feito de madrugada</h4><p>O trabalho “invisível” invade a noite e o fim de semana.</p></div>
  <div class="tile"><span class="ti">06</span><h4>Pratos caindo</h4><p>Saúde, família, relacionamento, descanso: sempre depois.</p></div>
</div>
""")

# 9 UM DIA
day = [("Atendimentos", 6, "t"), ("Planos alimentares", 2.5, "t2"), ("WhatsApp e dúvidas", 2, "w"),
       ("Conteúdo", 1.5, "w2"), ("Financeiro e admin.", 1, "w3"), ("Você", 1, "me")]
bar = "".join(f'<div class="seg {c}" style="flex:{h}"><b>{h:g}h</b><span>{n}</span></div>' for n, h, c in day)
add(f"""
<div class="tag">Exemplo · um dia comum</div>
<h2 class="title">14 horas trabalhando. 1 hora para você.</h2>
<div class="daybar">{bar}</div>
<div class="split daynotes">
  <p class="bigserif sm">Quando a agenda é de todo mundo,<br><em>ela não é sua.</em></p>
  <p class="note">Repare: só as 6 horas de atendimento geram receita direta. O resto é trabalho que <b>pode ter processo, modelo ou ajuda.</b></p>
</div>
""")

# 10 INIMIGOS
add("""
<h2 class="title">O inimigo é o sistema, não você</h2>
<div class="errs light-on-cream en">
  <div><span>01</span><p><b>Centralização</b> parece eficiente no começo e vira gargalo.</p></div>
  <div><span>02</span><p><b>Cultura faz-tudo</b> custa em decisões adiadas.</p></div>
  <div><span>03</span><p><b>Falta de processos:</b> decidir a mesma coisa toda vez.</p></div>
  <div><span>04</span><p><b>Gestão por urgência:</b> a urgência come o tempo de planejar.</p></div>
  <div><span>05</span><p><b>“Ninguém faz tão bem quanto eu”:</b> o custo real dos 20% de diferença.</p></div>
  <div><span>06</span><p><b>Trabalhar mais = lucrar mais?</b> Existe um ponto em que a curva vira.</p></div>
</div>
<p class="note">O problema nunca foi você. <b>É a forma como a rotina foi montada</b> e isso se reorganiza.</p>
""")

# 11 QUANTO VALE SUA HORA
add("""
<div class="tag">Exemplo ilustrativo</div>
<h2 class="title">Quanto vale a sua hora?</h2>
<div class="calc">
  <div><span class="v">R$ 12 mil</span><span class="l">faturamento por mês</span></div>
  <div class="op">÷</div>
  <div><span class="v">220 h</span><span class="l">horas trabalhadas no mês</span></div>
  <div class="op">=</div>
  <div class="hl"><span class="v">R$ 54</span><span class="l">valor da sua hora</span></div>
</div>
<div class="calc2">
  <div><b>2 h por dia</b> no WhatsApp <small>≈ 44 h por mês</small></div>
  <div><b>≈ R$ 2.400</b> do seu tempo <small>todo mês, respondendo mensagens</small></div>
  <div><b>Faça a sua conta</b> <small>e decida o que merece a sua hora</small></div>
</div>
<p class="note">Tempo é o único recurso da nutri que não se repõe. <b>Faturamento não é saúde.</b></p>
""")

# 12
section("02", "Os ladrões do seu tempo", "Antes da ferramenta, a mentalidade.")

# 13 LADRÕES
add("""
<h2 class="title">Onde o tempo da nutri vaza</h2>
<div class="errs light-on-cream">
  <div><span>01</span><p>WhatsApp aberto o dia inteiro</p></div>
  <div><span>02</span><p>Plano alimentar feito do zero, toda vez</p></div>
  <div><span>03</span><p>Encaixes e remarcações sem regra</p></div>
  <div><span>04</span><p>Dúvida de paciente respondida fora do horário</p></div>
  <div><span>05</span><p>Conteúdo para o Instagram sem planejamento</p></div>
  <div><span>06</span><p>Cobrança e financeiro feitos “quando der”</p></div>
</div>
<p class="note">Clareza antes de tudo. Não adianta acelerar uma rotina que funciona no improviso.</p>
""")

# 14 PRODUTIVA x OCUPADA
add("""
<h2 class="title">Produtiva ou ocupada?</h2>
<div class="vs">
  <div class="vs-col">
    <h3>Nutri ocupada</h3>
    <ul class="dash">
      <li>Agenda lotada, mas o faturamento não cresce</li>
      <li>Responde tudo na hora, para todo mundo</li>
      <li>Refaz o que poderia ser modelo</li>
      <li>Faz tudo sozinha “porque é mais rápido”</li>
      <li>Descansa com culpa (quando descansa)</li>
    </ul>
  </div>
  <div class="vs-mid">vs</div>
  <div class="vs-col on">
    <h3>Nutri produtiva</h3>
    <ul class="dash">
      <li>Planeja a semana antes dela começar</li>
      <li>Tem horário para atender e para responder</li>
      <li>Usa modelos, protocolos e respostas prontas</li>
      <li>Delega o que não exige o seu CRN</li>
      <li>Descansa sem culpa: descanso está na agenda</li>
    </ul>
  </div>
</div>
<p class="note">Produtividade não é exaustão: é fazer o que importa com menos esforço e menos estresse.</p>
""")

# 15 30 SEGUNDOS
add("""
<div class="center">
  <div class="tag light">Dinâmica</div>
  <h2 class="title light huge c">Quanto tempo têm<br>30 segundos?</h2>
  <p class="lead light">Fechem os olhos. Abram quando acharem que passaram 30 segundos.</p>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.3))

# 16 PRATOS
pratos = ["Saúde e corpo", "Família", "Relacionamento", "Finanças", "Consultório", "Descanso e lazer"]
pl = "".join(f'<div class="plate"><div class="pc"><span>0–10</span></div><p>{p}</p></div>' for p in pratos)
add(f"""
<div class="tag">Dinâmica · 3 min</div>
<h2 class="title">Os pratos da sua vida</h2>
<div class="plates">{pl}</div>
<p class="note">Dê uma nota de 0 a 10 para cada prato. <b>Qual está prestes a cair?</b> É por ele que a sua nova agenda começa.</p>
""")

# 17
section("03", "MBTI e gestão do tempo", "Entender como você funciona para planejar do seu jeito.")

# 18
quote("Por que a mesma agenda não funciona para todo mundo?")

# 19 MBTI
add("""
<h2 class="title">MBTI · as 4 preferências</h2>
<table class="tbl mbti">
  <tr><th>Dimensão</th><th>De um lado</th><th></th><th>Do outro lado</th></tr>
  <tr><td>Energia</td><td><b>E</b> · Extroversão<small>recarrega com pessoas, na ação</small></td><td class="x">×</td><td><b>I</b> · Introversão<small>recarrega no foco, no silêncio</small></td></tr>
  <tr><td>Percepção</td><td><b>S</b> · Sensação<small>concreto, prático, dados</small></td><td class="x">×</td><td><b>N</b> · Intuição<small>ideias, padrões, futuro</small></td></tr>
  <tr><td>Decisão</td><td><b>T</b> · Pensamento<small>lógica, critérios, números</small></td><td class="x">×</td><td><b>F</b> · Sentimento<small>impacto nas pessoas</small></td></tr>
  <tr><td>Organização</td><td><b>J</b> · Julgamento<small>estrutura, prazo, plano</small></td><td class="x">×</td><td><b>P</b> · Percepção<small>flexibilidade, adaptação</small></td></tr>
</table>
<p class="note">Não é rótulo, é <b>manual de uso</b>: mostra como você recupera energia, decide e se organiza.</p>
""")

# 20 J x P
add("""
<h2 class="title">O eixo do tempo: J × P</h2>
<div class="split">
  <div class="card soft">
    <div class="ck">Perfil J · você planeja</div>
    <h3 class="persona dk">Agenda fechada</h3>
    <ul class="dash"><li><b>Potência:</b> organiza a semana, cumpre horários</li><li><b>Risco:</b> sofre com encaixe e remarcação</li><li><b>Dica:</b> reserve 2 horários de encaixe por semana e pare de “abrir exceção”</li></ul>
  </div>
  <div class="card terra">
    <div class="ck">Perfil P · você improvisa</div>
    <h3 class="persona">Agenda flexível</h3>
    <ul class="dash"><li><b>Potência:</b> se adapta, resolve na hora, criatividade</li><li><b>Risco:</b> plano alimentar e conteúdo sempre na última hora</li><li><b>Dica:</b> temas por dia (“quarta é dia de planos”) em vez de horários rígidos</li></ul>
  </div>
</div>
""")

# 21 TESTE
qr_slide("Agora · 15 min", "Hora do teste",
         ["Aponte a câmera para o QR code", "Responda com sinceridade, sem pensar demais", "Anote o seu tipo de <b>4 letras</b> (ex.: ENFJ)"],
         "16personalities.com/br/teste-de-personalidade", QR_TEST)

# 22 RELATÓRIO
add("""
<h2 class="title">O seu relatório personalizado</h2>
<div class="split s55">
  <div>
    <ul class="checks big">
      <li><b>Leitura do seu perfil:</b> sua potência natural e o seu ponto de atenção</li>
      <li><b>Como você planeja melhor</b> a semana de consultório</li>
      <li><b>Rotina ideal:</b> atendimento, planos, conteúdo e autocuidado</li>
      <li><b>Regra das 3 prioridades semanais</b></li>
      <li><b>Plano de ação de 7 dias</b> pensado para o seu perfil</li>
    </ul>
  </div>
  <div class="card dark cta">
    <div class="ck">Quer o seu?</div>
    <p class="formula">Me mande o seu resultado no direct com a palavra <u>LUCRO</u>.</p>
    <div class="hr"></div>
    <p class="handle-big">@martinsscamila</p>
  </div>
</div>
""")

# 23
section("04", "A semana modelo da nutri", "Gestão do tempo do jeito Lucro Anti-Exaustão®.")

# 24 4 PASSOS
add("""
<h2 class="title">Retome a sua agenda em 4 passos</h2>
<div class="anat">
  <div class="an"><span>01</span><h4>Raio-X</h4><p class="w">Para onde vai o seu tempo?</p><p class="ex">Anote tudo o que fizer por <b>7 dias</b>, sem julgar.</p></div>
  <div class="arr">→</div>
  <div class="an"><span>02</span><h4>Extração</h4><p class="w">O que gera lucro e o que só cansa?</p><p class="ex">Marque o que <b>só você</b> pode fazer.</p></div>
  <div class="arr">→</div>
  <div class="an"><span>03</span><h4>Rotina</h4><p class="w">Como fica a semana ideal?</p><p class="ex">Monte a <b>semana modelo</b> com blocos fixos.</p></div>
  <div class="arr">→</div>
  <div class="an hl"><span>04</span><h4>Patrimônio</h4><p class="w">O que trabalha por você?</p><p class="ex">Modelos, protocolos e processos que <b>se repetem sem você</b>.</p></div>
</div>
<p class="statement sm">O objetivo não é fazer mais. É <em>parar de fazer tudo.</em></p>
""")

# 25 SEMANA MODELO
leg = {"at":"Atendimentos","pl":"Planos e devolutivas","ct":"Conteúdo","ad":"Financeiro e admin.","es":"Estudo","vi":"Vida (inegociável)"}
week = {"Seg":["pl","at","vi"],"Ter":["at","at","vi"],"Qua":["pl","ct","vi"],"Qui":["at","at","vi"],"Sex":["ad","es","vi"]}
rows = ["Manhã","Tarde","Noite"]
cells = '<div class="wg-h"></div>' + "".join(f'<div class="wg-h">{d}</div>' for d in week)
for r, rn in enumerate(rows):
    cells += f'<div class="wg-r">{rn}</div>' + "".join(f'<div class="wg-c {week[d][r]}">{leg[week[d][r]]}</div>' for d in week)
legend = "".join(f'<span class="lg {k}">{v}</span>' for k, v in leg.items())
add(f"""
<div class="tag">Exemplo · adapte ao seu perfil</div>
<h2 class="title">A semana modelo da nutri</h2>
<div class="weekgrid">{cells}</div>
<div class="wg-rules">
  <div><b>Dias temáticos:</b> atendimento não divide o dia com planos alimentares</div>
  <div><b>Encaixe tem regra:</b> 2 horários fixos por semana</div>
  <div><b>Noite é vida:</b> plano alimentar não invade a noite</div>
</div>
""")

# 26 SÓ EU POSSO
add("""
<h2 class="title">Só eu posso fazer isso?</h2>
<div class="eis">
  <div class="axis-y"><span>Precisa de você</span><span>Não precisa de você</span></div>
  <div class="eis-grid">
    <div class="q1"><span>Exige o seu CRN</span><h4>Só eu posso</h4><p>Consulta, conduta, plano alimentar, avaliação</p></div>
    <div class="q2"><span>Se repete toda semana</span><h4>Vira modelo</h4><p>Modelos de plano, material pós-consulta, mensagens de confirmação e lembrete</p></div>
    <div class="q3"><span>Operacional</span><h4>Secretária</h4><p>Agendamento, confirmação, cobrança, recepção, remarcação</p></div>
    <div class="q4"><span>Só consome</span><h4>Elimine</h4><p>Encaixe sem regra, áudio de 5 minutos, retrabalho, reunião sem pauta</p></div>
  </div>
</div>
<p class="note"><b>Regra de ouro:</b> se você fez a mesma coisa 3 vezes, ela vira processo.</p>
""")

# 27 WHATSAPP
add("""
<h2 class="title">WhatsApp sob controle</h2>
<div class="cols3">
  <div class="col"><h3>3 janelas</h3><p class="q">Horários fixos para responder</p><p>Ex.: 8h, 12h30 e 18h. Fora delas, notificações desligadas.</p></div>
  <div class="col"><h3>WhatsApp Business</h3><p class="q">Deixe o app trabalhar</p><p>Mensagem de ausência, respostas rápidas e etiquetas: novo, agendado, retorno, pagamento.</p></div>
  <div class="col"><h3>Combinado claro</h3><p class="q">Na primeira consulta</p><p>Explique quando e como você responde. Paciente bem orientado não cobra resposta às 23h.</p></div>
</div>
<p class="note">Disponibilidade total não é cuidado. <b>Cuidado é ter limite e cumprir o combinado.</b></p>
""")

# 28 EISENHOWER
add("""
<h2 class="title">Matriz de Eisenhower da nutri</h2>
<div class="eis">
  <div class="axis-y"><span>Importante</span><span>Não importante</span></div>
  <div class="eis-grid">
    <div class="q1"><span>Urgente e importante</span><h4>Faça agora</h4><p>Paciente com intercorrência, plano com prazo de entrega hoje</p></div>
    <div class="q2"><span>Importante, não urgente</span><h4>Agende</h4><p>Criar modelos e protocolos, conteúdo, estudo, financeiro, descanso</p></div>
    <div class="q3"><span>Urgente, não importante</span><h4>Delegue</h4><p>Confirmações, remarcações, cobrança, dúvidas administrativas</p></div>
    <div class="q4"><span>Nem urgente, nem importante</span><h4>Elimine</h4><p>Rolar o feed entre pacientes, comparar-se com outras nutris</p></div>
  </div>
</div>
""")

# 29
section("05", "Ferramentas", "Não existe ferramenta certa. Existe a que você usa.")

# 30 FERRAMENTAS
tools = [
 ("Google Agenda","Quando","Atendimentos, blocos da semana modelo e lembretes.","Uma cor por tipo de bloco. Agendamento online e lembrete automático para o paciente."),
 ("Trello","O quê","Quadro visual: pacientes em acompanhamento, conteúdos, pendências.","Colunas A fazer · Fazendo · Feito. Um card por paciente ou tarefa."),
 ("Notion","Onde fica","Central do consultório: protocolos, modelos de plano, banco de conteúdo.","Comece com 3 páginas: Protocolos, Modelos e Ideias de conteúdo."),
 ("Agenda física","Foco","As 3 prioridades do dia, longe das notificações.","Escreva à mão, de manhã, antes de abrir o WhatsApp."),
 ("Planner","Visão","Semana e mês inteiros: metas, revisão de domingo, pratos da vida.","15 minutos no domingo para planejar a semana."),
]
tc = "".join(f'<div class="tool"><span class="tk">{k}</span><h4>{n}</h4><p>{u}</p><p class="tip"><b>Dica:</b> {t}</p></div>' for n, k, u, t in tools)
add(f"""
<h2 class="title">Cinco ferramentas, cinco funções</h2>
<div class="tools">{tc}</div>
""")

# 31 COMBINAR
add("""
<h2 class="title">Como combinar sem se perder</h2>
<div class="stack">
  <div><span>Quando</span><h4>Google Agenda</h4><p>tudo o que tem dia e hora</p></div>
  <div class="pl">+</div>
  <div><span>O quê</span><h4>Trello ou Notion</h4><p>tarefas, processos e modelos</p></div>
  <div class="pl">+</div>
  <div class="hl"><span>Foco</span><h4>Planner ou agenda física</h4><p>as 3 prioridades do dia</p></div>
</div>
<div class="tips">
  <div>Uma ferramenta por função</div><div>Comece com uma só</div><div>Revise todo domingo</div><div>Simples que funciona &gt; perfeito</div>
</div>
""")

# 32 POR PERFIL
add("""
<h2 class="title">Ferramentas por perfil</h2>
<div class="cols3">
  <div class="col"><h3>Perfil J</h3><p class="q">Gosta de estrutura</p><p><b>Google Agenda + Planner.</b> Time blocking: blocos fixos para atender, montar planos e criar conteúdo.</p></div>
  <div class="col"><h3>Perfil P</h3><p class="q">Precisa de flexibilidade</p><p><b>Trello + agenda física.</b> Temas por dia e lista curta de prioridades, sem horário rígido.</p></div>
  <div class="col"><h3>Todas</h3><p class="q">Foco curto, dia corrido</p><p><b>Pomodoro:</b> 25 minutos de foco total em um plano alimentar, 5 de pausa.</p></div>
</div>
<p class="note">Perfis <b>S</b> costumam preferir papel e checklists. Perfis <b>N</b> se dão bem com Notion e mapas visuais.</p>
""")

# 33
section("06", "Seu plano de 7 dias", "Da aula para a agenda: começa amanhã.")

# 34 PLANO 7 DIAS
plan = [("Dia 1","Raio-X","Anote tudo o que fizer, hora a hora"),("Dia 2","Ladrões","Marque o que só cansa e não gera resultado"),
        ("Dia 3","Delegar","Liste o que vai para a secretária ou para um modelo"),("Dia 4","Semana modelo","Desenhe os blocos na Google Agenda"),
        ("Dia 5","WhatsApp","Configure as 3 janelas e as respostas rápidas"),("Dia 6","Ferramenta","Escolha uma e configure só o básico"),
        ("Dia 7","Revisão","15 min: o que funcionou e as 3 prioridades da semana"),("Depois","Repita","Toda semana, ajuste. Constância > perfeição")]
pc = "".join(f'<div class="im{" hl" if i==0 else (" dk" if i==7 else "")}"><span class="id">{d}</span><h4>{t}</h4><p>{x}</p></div>' for i,(d,t,x) in enumerate(plan))
add(f"""
<h2 class="title">Seu plano de 7 dias</h2>
<div class="impl">{pc}</div>
""")

# 35 COMPROMISSO
add("""
<div class="tag light">Dinâmica · compromisso</div>
<h2 class="title light">Escreva agora, no papel</h2>
<div class="prompts">
  <div class="prompt"><span class="pn">01</span><p>Uma coisa que eu vou <b>parar</b> de fazer</p></div>
  <div class="prompt"><span class="pn">02</span><p>Uma coisa que eu vou <b>delegar</b> ou transformar em modelo</p></div>
  <div class="prompt"><span class="pn">03</span><p>Um prato da vida que vai <b>entrar na agenda</b> esta semana</p></div>
</div>
""", "dark", waves(900, 460, 16, "#FBF6F1", 0.28))

# 36 CONSTÂNCIA
add("""
<h2 class="title light">Como manter a constância</h2>
<div class="errs">
  <div><span>01</span><p>Volte ao seu porquê</p></div>
  <div><span>02</span><p>Revise a semana todo domingo</p></div>
  <div><span>03</span><p>Adapte, não abandone</p></div>
  <div><span>04</span><p>Aprenda com as recaídas, sem culpa</p></div>
  <div><span>05</span><p>Peça apoio: ninguém cresce sozinha</p></div>
  <div><span>06</span><p>Comemore cada pequena vitória</p></div>
</div>
""", "dark", waves(800, 380, 12, "#B65F3A", 0.45))

# 37
quote("Quem decide, realiza.<br>Quem adia, apenas sonha.")

# 38
add("""
<div class="center">
  <div class="tag light">Encerramento</div>
  <h2 class="title light huge c">Qual palavra define<br>o encontro de hoje?</h2>
</div>
""", "dark nofoot", waves(1100, 480, 18, "#B65F3A", 0.5))

# 39 OBRIGADA
add(f"""
<div class="bye">
  <div>
    <h2 class="mega">Obrigada!</h2>
    <p class="lead light">Seu relatório MBTI: me mande o resultado no direct com a palavra <b>LUCRO</b>.</p>
    <p class="bye-h">@martinsscamila</p>
  </div>
  <div class="qr">{QR_INSTA}</div>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.25))

# ---------------- RENDER ----------------
css = (OUT / "style.css").read_text()
pages = []
for i, (cls, html, deco) in enumerate(SLIDES, 1):
    foot = "" if "nofoot" in cls else f'<div class="foot"><span>Gestão do tempo para nutricionistas</span><span>@martinsscamila &nbsp;·&nbsp; {i:02d}</span></div>'
    pages.append(f'<section class="s {cls}">{deco}{html}{foot}</section>')
doc = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Agenda cheia, vida em equilíbrio</title><style>{css}</style></head><body>{''.join(pages)}</body></html>"
(OUT / "deck.html").write_text(doc)
print("slides:", len(SLIDES))
