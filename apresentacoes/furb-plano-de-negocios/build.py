import math, pathlib

OUT = pathlib.Path(__file__).parent
QR = (OUT / "qr.svg").read_text()
TEST_URL = "16personalities.com/br/teste-de-personalidade"

def waves(w=900, h=520, n=14, color="#FBF6F1", op=0.55, amp=70, freq=1.25, tilt=0.35, sw=1.4):
    paths = []
    for i in range(n):
        pts = []
        off = i * (h / (n * 1.6))
        ph = i * 0.18
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
<div class="sec">
  <div class="sec-n">{num}</div>
  <h2 class="sec-t">{title}</h2>
  <p class="sec-s">{sub}</p>
</div>
""", "dark nofoot", waves(1100, 520, 18, "#B65F3A", 0.55))

# ---------- 1 CAPA ----------
add(f"""
<div class="cover-l">
  <div class="kicker light">FURB · Farmácia · Administração e Economia Farmacêutica</div>
  <h1 class="mega">Do papel<br>à entrega</h1>
  <p class="lead light">Gestão do tempo, produtividade e um plano de ação para tirar o seu Plano de Negócios do papel.</p>
  <div class="cover-meta">
    <div><b>Camila Martins Finger</b><br>@martinsscamila</div>
    <div class="vr"></div>
    <div>16 de outubro de 2026<br>09h30 – 11h30</div>
  </div>
</div>
<div class="cover-card">
  {waves(620, 760, 22, "#B65F3A", 0.85, 90, 1.1, 0.55, 1.6)}
  <div class="cc-txt"><span class="script">entrega</span><br><span>13 de novembro</span></div>
</div>
""", "terra", waves(1000, 420, 14, "#FBF6F1", 0.35))

# ---------- 2 ----------
quote("Quem não define seu caminho acaba vivendo o plano de outra pessoa.")

# ---------- 3 ----------
add("""
<div class="tag light">Dinâmica · 5 min</div>
<h2 class="title light">Quero conhecer vocês</h2>
<div class="prompts">
  <div class="prompt"><span class="pn">01</span><p>Qual <b>palavra</b> define o seu momento hoje?</p></div>
  <div class="prompt"><span class="pn">02</span><p>De 0 a 10: quanto do projeto do seu grupo <b>já saiu do papel</b>?</p></div>
</div>
""", "dark", waves(900, 460, 16, "#FBF6F1", 0.28))

# ---------- 4 ----------
add("""
<h2 class="title">Prazer, Camila.</h2>
<p class="sub">Uma jornada que começou exatamente onde vocês estão: na saúde.</p>
<div class="timeline">
  <div class="tl"><div class="dot"></div><div class="tl-k">Origem</div><h4>Técnica de enfermagem</h4><p>Rotina das 7h às 17h, ônibus, plantão. Sei o que é não ter tempo.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Virada</div><h4>Maternidade e empresa na pandemia</h4><p>Aprendi a empreender empreendendo — com pouco tempo e muita coisa ao mesmo tempo.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Método</div><h4>Lucro Anti-Exaustão®</h4><p>Rotina, perfil comportamental e planejamento a serviço de resultados sem exaustão.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Hoje</div><h4>Mentora de empresárias</h4><p>Programas de aceleração, workshops in company e palestras.</p></div>
</div>
<p class="statement">Se eu saí da exaustão sem tempo sobrando, <em>vocês também conseguem.</em></p>
""")

# ---------- 5 AGENDA ----------
add("""
<h2 class="title">Como vamos trabalhar hoje</h2>
<div class="agenda">
  <div class="ag"><span class="t">09h30</span><span class="n"></span><span class="d">Abertura e conexão</span></div>
  <div class="ag"><span class="t">09h45</span><span class="n">01</span><span class="d">O desafio · 11 blocos em 4 semanas</span></div>
  <div class="ag"><span class="t">09h55</span><span class="n">02</span><span class="d">Gestão do tempo e produtividade</span></div>
  <div class="ag"><span class="t">10h20</span><span class="n">03</span><span class="d">MBTI · teste ao vivo</span></div>
  <div class="ag pause"><span class="t">10h45</span><span class="n"></span><span class="d">Pausa · 10 min</span></div>
  <div class="ag"><span class="t">10h55</span><span class="n">04</span><span class="d">Ferramentas de planejamento</span></div>
  <div class="ag"><span class="t">11h05</span><span class="n">05</span><span class="d">Plano de ação até 13/11 · mão na massa</span></div>
  <div class="ag"><span class="t">11h25</span><span class="n"></span><span class="d">Encerramento</span></div>
</div>
""", "cream", waves(700, 380, 12, "#B65F3A", 0.35))

# ---------- 6 ----------
section("01", "O desafio", "Um projeto, 11 blocos, 4 semanas.")

# ---------- 7 COUNTDOWN ----------
add("""
<div class="count">
  <div class="cd"><span class="v">28</span><span class="l">dias</span></div>
  <div class="cd"><span class="v">4</span><span class="l">semanas</span></div>
  <div class="cd"><span class="v">11</span><span class="l">blocos</span></div>
  <div class="cd hl"><span class="v">1</span><span class="l">entrega</span></div>
</div>
<div class="range"><span>Hoje · 16/10</span><div class="bar"><i></i></div><span><b>Entrega · 13/11</b></span></div>
<p class="statement">Parece muito tempo. <em>É exatamente por isso que costuma faltar.</em></p>
""")

# ---------- 8 BLOCOS ----------
blocks = [("Resumo executivo","O negócio em 1 minuto"),("Descrição do negócio","Missão, visão, valores, problema"),
          ("Análise de mercado","Público, concorrência, oportunidades"),("Legal e regulatório","Normas, licenças, RT"),
          ("Produtos e serviços","O que vende e o que diferencia"),("Estrutura e operação","Espaço, pessoas, tecnologia"),
          ("Plano de marketing","Posicionamento e fidelização"),("Planejamento financeiro","Investimento, custos, receita"),
          ("O primeiro ano","Como a empresa nasce e cresce"),("Análise SWOT","Só no documento escrito"),("Conclusão","É viável? Por quê?")]
cells = "".join(f'<div class="bk{" off" if i==9 else ""}"><span>{i+1:02d}</span><h5>{t}</h5><p>{d}</p></div>' for i,(t,d) in enumerate(blocks))
add(f"""
<h2 class="title">O que vocês vão entregar</h2>
<div class="blocks">{cells}<div class="bk legend"><p>Visto inteiro, assusta. Dividido em semanas, cabe na rotina.</p></div></div>
""")

# ---------- 9 ----------
quote("Projeto grande não se faz de uma vez.<br>Projeto grande se divide.")

# ---------- 10 ----------
section("02", "Gestão do tempo e produtividade", "Antes da ferramenta, a mentalidade.")

# ---------- 11 ----------
add("""
<div class="split">
  <div>
    <h2 class="title">O que é gestão do tempo?</h2>
    <p class="bigserif sm">Não é organizar a agenda.<br><em>É decidir o que realmente importa</em> — e proteger tempo para isso.</p>
  </div>
  <div class="card soft">
    <div class="ck">Sem gestão do tempo</div>
    <ul class="dash">
      <li><b>Estresse:</b> sensação constante de atraso e sobrecarga</li>
      <li><b>Desempenho:</b> entregas feitas às pressas, abaixo do que você é capaz</li>
      <li><b>Saúde:</b> noites viradas, ansiedade, cansaço</li>
      <li><b>Grupo:</b> conflitos, retrabalho e “eu fiz tudo sozinha”</li>
    </ul>
  </div>
</div>
""")

# ---------- 12 ----------
add("""
<h2 class="title">Produtiva ou ocupada?</h2>
<div class="vs">
  <div class="vs-col">
    <h3>Ocupada</h3>
    <ul class="dash">
      <li>Acumula tarefas e não sabe por onde começar</li>
      <li>Lota a agenda, mas o projeto não anda</li>
      <li>Quer dar conta de tudo sozinha</li>
      <li>Deixa tudo para a última semana</li>
      <li>Sempre sente que “falta tempo”</li>
    </ul>
  </div>
  <div class="vs-mid">vs</div>
  <div class="vs-col on">
    <h3>Produtiva</h3>
    <ul class="dash">
      <li>Planeja a semana com antecedência</li>
      <li>Faz primeiro o que é prioridade</li>
      <li>Divide e delega no grupo</li>
      <li>Entrega por partes, com folga</li>
      <li>Descansa sem culpa</li>
    </ul>
  </div>
</div>
<p class="note">Produtividade não é exaustão: é fazer o que importa com menos esforço e menos estresse.</p>
""")

# ---------- 13 ----------
add("""
<div class="center">
  <div class="tag light">Dinâmica</div>
  <h2 class="title light huge c">Quanto tempo têm<br>30 segundos?</h2>
  <p class="lead light">Fechem os olhos. Abram quando acharem que passaram 30 segundos.</p>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.3))

# ---------- 14 ----------
quote("O que é procrastinar?", "É adiar o que é importante, colocando tarefas menores ou distrações no lugar.<br><b>Procrastinação não é preguiça. É um sintoma.</b>")

# ---------- 15 ----------
add("""
<h2 class="title">Por que adiamos o que importa?</h2>
<div class="grid4">
  <div class="tile"><span class="ti">01</span><h4>Falta de clareza</h4><p>“Fazer o plano de negócios” não é tarefa. É um projeto inteiro.</p></div>
  <div class="tile"><span class="ti">02</span><h4>Medo de errar</h4><p>Esperar a ideia perfeita para começar a escrever.</p></div>
  <div class="tile"><span class="ti">03</span><h4>Distrações</h4><p>Celular, notificações, multitarefa.</p></div>
  <div class="tile"><span class="ti">04</span><h4>Recompensa distante</h4><p>A nota só vem em novembro. O celular recompensa agora.</p></div>
</div>
<div class="band"><span>No trabalho em grupo</span><p>Ainda tem o clássico: <b>“alguém vai fazer”</b>. Quando é de todo mundo, não é de ninguém.</p></div>
""")

# ---------- 16 ----------
add("""
<h2 class="title">Onde a sua energia está vazando?</h2>
<div class="errs light-on-cream">
  <div><span>01</span><p>Celular e redes sociais entre uma tarefa e outra</p></div>
  <div><span>02</span><p>Reunião de grupo sem pauta e sem decisão</p></div>
  <div><span>03</span><p>Retrabalho por falta de combinado</p></div>
  <div><span>04</span><p>Multitarefa: estudar, responder, rolar o feed</p></div>
  <div><span>05</span><p>“Vou fazer tudo no último fim de semana”</p></div>
  <div><span>06</span><p>Perfeccionismo no layout antes do conteúdo</p></div>
</div>
<p class="note">Clareza antes de tudo. Não adianta acelerar uma rotina que funciona no improviso.</p>
""")

# ---------- 17 ----------
section("03", "MBTI e gestão do tempo", "Entender como você funciona para planejar do seu jeito.")

# ---------- 18 ----------
quote("Por que a mesma agenda não funciona para todo mundo?")

# ---------- 19 ----------
add("""
<h2 class="title">MBTI · as 4 preferências</h2>
<table class="tbl mbti">
  <tr><th>Dimensão</th><th>De um lado</th><th></th><th>Do outro lado</th></tr>
  <tr><td>Energia</td><td><b>E</b> · Extroversão<small>recarrega na troca, na ação</small></td><td class="x">×</td><td><b>I</b> · Introversão<small>recarrega no foco, no silêncio</small></td></tr>
  <tr><td>Percepção</td><td><b>S</b> · Sensação<small>concreto, prático, dados</small></td><td class="x">×</td><td><b>N</b> · Intuição<small>ideias, padrões, futuro</small></td></tr>
  <tr><td>Decisão</td><td><b>T</b> · Pensamento<small>lógica, critérios, números</small></td><td class="x">×</td><td><b>F</b> · Sentimento<small>impacto nas pessoas</small></td></tr>
  <tr><td>Organização</td><td><b>J</b> · Julgamento<small>estrutura, prazo, plano</small></td><td class="x">×</td><td><b>P</b> · Percepção<small>flexibilidade, adaptação</small></td></tr>
</table>
<p class="note">Não é rótulo, é <b>manual de uso</b>: mostra como você recupera energia, decide e se organiza.</p>
""")

# ---------- 20 ----------
add("""
<h2 class="title">O eixo do tempo: J × P</h2>
<div class="split">
  <div class="card soft">
    <div class="ck">Perfil J · você planeja</div>
    <h3 class="persona dk">Estrutura e prazo</h3>
    <ul class="dash"><li><b>Potência:</b> organiza, antecipa, cumpre combinados</li><li><b>Risco:</b> rigidez e ansiedade quando o plano muda</li><li><b>Dica:</b> deixe 20% da semana livre para imprevistos</li></ul>
  </div>
  <div class="card terra">
    <div class="ck">Perfil P · você improvisa</div>
    <h3 class="persona">Flexibilidade e pressão</h3>
    <ul class="dash"><li><b>Potência:</b> criatividade, adaptação, rende sob pressão</li><li><b>Risco:</b> tudo na última hora</li><li><b>Dica:</b> crie prazos internos antes do prazo real</li></ul>
  </div>
</div>
""")

# ---------- 21 TESTE ----------
add(f"""
<div class="qr-wrap">
  <div>
    <div class="tag light">Agora · 15 min</div>
    <h2 class="title light huge">Hora do teste</h2>
    <ol class="steps-v">
      <li>Aponte a câmera para o QR code</li>
      <li>Responda com sinceridade — não existe resposta certa</li>
      <li>Anote o seu tipo de <b>4 letras</b> (ex.: ENFJ)</li>
    </ol>
    <p class="url">{TEST_URL}</p>
  </div>
  <div class="qr">{QR}</div>
</div>
""", "dark nofoot", "")

# ---------- 22 RELATÓRIO ----------
add("""
<h2 class="title">O seu relatório personalizado</h2>
<div class="split s55">
  <div>
    <ul class="checks big">
      <li><b>Leitura essencial do perfil:</b> sua potência natural e o seu ponto de atenção</li>
      <li><b>Como você planeja melhor:</b> o que a sua personalidade precisa para render</li>
      <li><b>Rotina ideal:</b> blocos de estudo, execução e autocuidado</li>
      <li><b>Regra das 3 prioridades semanais</b></li>
      <li><b>Plano de ação de 7 dias</b> pensado para o seu perfil</li>
    </ul>
  </div>
  <div class="card dark cta">
    <div class="ck">Quer o seu?</div>
    <p class="formula">Me mande o seu resultado no direct com a palavra <u>FURB</u>.</p>
    <div class="hr"></div>
    <p class="handle-big">@martinsscamila</p>
  </div>
</div>
""")

# ---------- 23 ----------
add("""
<h2 class="title">Ferramentas por perfil</h2>
<div class="cols3">
  <div class="col"><h3>Time blocking</h3><p class="q">Ideal para perfil J</p><p>Blocos fixos na agenda para cada atividade. Ex.: terça, 19h–21h · Bloco 3, análise de mercado.</p></div>
  <div class="col"><h3>Temas do dia</h3><p class="q">Ideal para perfil P</p><p>Cada dia tem um tema, não um horário rígido. Ex.: “quarta é dia de pesquisa”.</p></div>
  <div class="col"><h3>Pomodoro</h3><p class="q">Para foco curto · todos os perfis</p><p>25 minutos de foco total, 5 de pausa. A cada 4 ciclos, uma pausa maior.</p></div>
</div>
<p class="note">Não existe ferramenta certa ou errada. Existe a ferramenta que você realmente usa.</p>
""")

# ---------- 24 PERFIS NO GRUPO ----------
add("""
<h2 class="title">Usem os perfis para dividir o trabalho</h2>
<div class="roles">
  <div><b>E</b><p>Entrevistas, contato com farmácias, apresentação oral</p></div>
  <div><b>I</b><p>Pesquisa aprofundada e redação</p></div>
  <div><b>S</b><p>Legislação, números, detalhes e revisão</p></div>
  <div><b>N</b><p>Diferencial, visão, marketing</p></div>
  <div><b>T</b><p>Planejamento financeiro e análise</p></div>
  <div><b>F</b><p>Público-alvo, persona, missão e valores</p></div>
  <div><b>J</b><p>Guardiã do cronograma e dos prazos</p></div>
  <div><b>P</b><p>Soluções criativas quando o plano muda</p></div>
</div>
<p class="note">Preferência não é limite: é por onde cada uma rende mais com menos desgaste.</p>
""")

# ---------- 25 PAUSA ----------
add("""
<div class="center">
  <div class="tag light">10h45 · 10 minutos</div>
  <h2 class="mega">Pausa</h2>
  <p class="lead light">Voltamos às 10h55. Compartilhe o seu tipo com o seu grupo:<br><b>quem é J e quem é P?</b></p>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.3))

# ---------- 26 ----------
section("04", "Ferramentas de planejamento", "Planejamento não é burocracia. É ferramenta de liberdade.")

# ---------- 27 EISENHOWER ----------
add("""
<h2 class="title">Matriz de Eisenhower</h2>
<div class="eis">
  <div class="axis-y"><span>Importante</span><span>Não importante</span></div>
  <div class="eis-grid">
    <div class="q1"><span>Urgente e importante</span><h4>Faça agora</h4><p>Definir a ideia do negócio e dividir os blocos entre o grupo</p></div>
    <div class="q2"><span>Importante, não urgente</span><h4>Agende</h4><p>Pesquisa de mercado, legislação, planilha financeira</p></div>
    <div class="q3"><span>Urgente, não importante</span><h4>Delegue</h4><p>Formatação, padronização, revisão de texto</p></div>
    <div class="q4"><span>Nem urgente, nem importante</span><h4>Elimine</h4><p>Reunião sem pauta, layout perfeito antes do conteúdo</p></div>
  </div>
</div>
""")

# ---------- 28 KANBAN ----------
add("""
<h2 class="title">Quadro do grupo · kanban</h2>
<div class="kanban">
  <div><h4>A fazer</h4><i>Bloco 5 · Produtos e serviços<small>Ana · até 30/10</small></i><i>Bloco 7 · Marketing<small>Júlia · até 30/10</small></i></div>
  <div><h4>Fazendo</h4><i>Bloco 3 · Concorrência<small>Bia · até 23/10</small></i></div>
  <div><h4>Revisão</h4><i>Bloco 2 · Missão e visão<small>Carol · até 23/10</small></i></div>
  <div class="done"><h4>Feito</h4><i>Ideia e nome do negócio<small>grupo · 18/10</small></i></div>
</div>
<div class="tips">
  <div>1 card = 1 entrega</div><div>1 responsável</div><div>1 prazo</div><div>Trello · Notion · post-its</div>
</div>
""")

# ---------- 29 RITUAIS ----------
add("""
<h2 class="title">Três hábitos que sustentam o plano</h2>
<div class="cols3 qs">
  <div class="col"><span class="bign">3</span><h3>Prioridades por semana</h3><p>No máximo três. Se tudo é prioridade, nada é.</p></div>
  <div class="col"><span class="bign">15′</span><h3>Revisão de domingo</h3><p>O que foi feito? O que travou? Quais as 3 prioridades da semana?</p></div>
  <div class="col"><span class="bign">1×</span><h3>Check-in do grupo</h3><p>Um dia fixo por semana, 20 minutos, com pauta e decisões anotadas.</p></div>
</div>
""")

# ---------- 30 ----------
section("05", "Plano de ação até 13/11", "Do conceito para o cronograma do seu grupo.")

# ---------- 31 CRONOGRAMA ----------
weeks = [
  ("Semana 0","16 – 18/10","Largada",["Fechar ideia e nome","Dividir papéis pelo MBTI","Criar quadro e documento compartilhado"],"Plano do grupo pronto"),
  ("Semana 1","19 – 25/10","Fundamentos",["Bloco 2 · Descrição","Bloco 3 · Mercado","Bloco 4 · Legal"],"Pesquisa concluída"),
  ("Semana 2","26/10 – 01/11","Operação",["Bloco 5 · Produtos e serviços","Bloco 6 · Estrutura","Bloco 7 · Marketing"],"Metade do plano escrita"),
  ("Semana 3","02 – 08/11","Números",["Bloco 8 · Financeiro","Bloco 9 · Primeiro ano","Bloco 10 · SWOT"],"Feriado 02/11: planeje!"),
  ("Semana 4","09 – 13/11","Fechamento",["Bloco 11 · Conclusão","Bloco 1 · Resumo (por último)","Revisão, slides e ensaio"],"Entrega 13/11"),
]
wk = "".join(
  f'<div class="wk{" last" if i==4 else ""}"><span class="wn">{n}</span><span class="wd">{d}</span><h4>{t}</h4>'
  + "".join(f"<p>{x}</p>" for x in items) + f'<div class="ms">{m}</div></div>'
  for i,(n,d,t,items,m) in enumerate(weeks))
add(f"""
<h2 class="title">O cronograma até a entrega</h2>
<div class="weeks">{wk}</div>
""")

# ---------- 32 DINÂMICA PLANO ----------
add("""
<div class="tag">Dinâmica · em grupos · 15 min</div>
<h2 class="title">Montem o plano do grupo</h2>
<div class="split s55">
  <table class="tbl plan">
    <tr><th>Bloco</th><th>Responsável</th><th>Prazo</th><th>Status</th></tr>
    <tr><td>02 · Descrição</td><td></td><td>23/10</td><td></td></tr>
    <tr><td>03 · Mercado</td><td></td><td>25/10</td><td></td></tr>
    <tr><td>04 · Legal</td><td></td><td>25/10</td><td></td></tr>
    <tr><td>…</td><td></td><td></td><td></td></tr>
    <tr><td>01 · Resumo</td><td></td><td>11/11</td><td></td></tr>
  </table>
  <div class="card soft">
    <div class="ck">Combinados do grupo</div>
    <ul class="checks">
      <li>Dia e horário fixos do check-in semanal</li>
      <li>Onde fica o documento e o quadro</li>
      <li>Prazo interno: 2 dias antes do real</li>
      <li>O que fazemos se alguém atrasar</li>
    </ul>
  </div>
</div>
<p class="note"><b>Filtro de energia:</b> esse plano respeita a agenda, a energia e a fase de vida de cada uma?</p>
""")

# ---------- 33 ----------
add("""
<h2 class="title light">Como manter a constância</h2>
<div class="errs">
  <div><span>01</span><p>Volte ao seu porquê</p></div>
  <div><span>02</span><p>Faça a revisão semanal, mesmo curta</p></div>
  <div><span>03</span><p>Tenha coragem de adaptar, não de abandonar</p></div>
  <div><span>04</span><p>Aprenda com as recaídas, sem culpa</p></div>
  <div><span>05</span><p>Cobre e apoie: ninguém entrega sozinha</p></div>
  <div><span>06</span><p>Comemore cada bloco entregue</p></div>
</div>
""", "dark", waves(800, 380, 12, "#B65F3A", 0.45))

# ---------- 34 ----------
quote("Quem decide, realiza.<br>Quem adia, apenas sonha.")

# ---------- 35 ----------
add("""
<div class="center">
  <div class="tag light">Encerramento</div>
  <h2 class="title light huge c">Qual palavra define<br>o encontro de hoje?</h2>
</div>
""", "dark nofoot", waves(1100, 480, 18, "#B65F3A", 0.5))

# ---------- 36 ----------
add("""
<div class="center">
  <h2 class="mega">Obrigada!</h2>
  <p class="lead light">Transforme sua visão em ação: o futuro começa agora.</p>
  <div class="cover-meta c">
    <div><b>Seu relatório MBTI</b><br>direct com a palavra FURB</div>
    <div class="vr"></div>
    <div>Instagram<br><b>@martinsscamila</b></div>
  </div>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.32))

# ---------------- RENDER ----------------
css = (OUT / "style.css").read_text()
pages = []
for i, (cls, html, deco) in enumerate(SLIDES, 1):
    foot = "" if "nofoot" in cls else f'<div class="foot"><span>Do papel à entrega · FURB</span><span>@martinsscamila &nbsp;·&nbsp; {i:02d}</span></div>'
    pages.append(f'<section class="s {cls}">{deco}{html}{foot}</section>')
doc = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Do papel à entrega</title><style>{css}</style></head><body>{''.join(pages)}</body></html>"
(OUT / "deck.html").write_text(doc)
print("slides:", len(SLIDES))
