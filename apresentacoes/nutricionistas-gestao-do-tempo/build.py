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


def ill(kind):
    T, S, C, I, L = "#B65F3A", "#F2E1D5", "#FBF6F1", "#272322", "#DCD3C9"
    if kind == "gcal":
        cells = "".join(f'<rect x="{30+j*48}" y="{70+i*34}" width="42" height="28" rx="5" fill="{C}" stroke="{L}"/>' for i in range(3) for j in range(5))
        ev = f'<rect x="30" y="70" width="42" height="28" rx="5" fill="{T}"/><rect x="126" y="104" width="42" height="28" rx="5" fill="{T}"/><rect x="78" y="138" width="42" height="28" rx="5" fill="{I}"/><rect x="222" y="70" width="42" height="62" rx="5" fill="{S}" stroke="{T}"/>'
        return f'<rect x="20" y="20" width="260" height="160" rx="16" fill="#fff" stroke="{L}" stroke-width="2"/><rect x="20" y="20" width="260" height="40" rx="16" fill="{T}"/><rect x="20" y="44" width="260" height="16" fill="{T}"/><circle cx="60" cy="16" r="6" fill="{I}"/><circle cx="240" cy="16" r="6" fill="{I}"/>{cells}{ev}'
    if kind == "trello":
        cols = ""
        for k,(x,n) in enumerate([(24,3),(116,2),(208,1)]):
            cols += f'<rect x="{x}" y="22" width="80" height="156" rx="12" fill="{S if k<2 else "#E8D5C4"}"/>' + "".join(f'<rect x="{x+8}" y="{40+c*38}" width="64" height="30" rx="6" fill="#fff"/><rect x="{x+8}" y="{40+c*38}" width="5" height="30" rx="2" fill="{T}"/>' for c in range(n))
        return cols
    if kind == "notion":
        lines = "".join(f'<rect x="70" y="{84+i*22}" width="{170-i*25}" height="8" rx="4" fill="{L}"/><path d="M50 {84+i*22} l8 4 l-8 4z" fill="{T}"/>' for i in range(4))
        return f'<rect x="30" y="18" width="240" height="164" rx="14" fill="#fff" stroke="{L}" stroke-width="2"/><rect x="50" y="36" width="34" height="34" rx="8" fill="{S}"/><text x="67" y="61" font-family="Gilda" font-size="24" text-anchor="middle" fill="{T}">N</text><rect x="96" y="44" width="130" height="14" rx="7" fill="{I}"/>{lines}'
    if kind == "agenda":
        spiral = "".join(f'<circle cx="150" cy="{40+i*20}" r="5" fill="none" stroke="{I}" stroke-width="2"/>' for i in range(7))
        lines = "".join(f'<rect x="{x}" y="{60+i*20}" width="90" height="4" rx="2" fill="{L}"/>' for x in (45,165) for i in range(5))
        return f'<path d="M30 30 h110 v150 h-110z" fill="#fff" stroke="{L}" stroke-width="2"/><path d="M160 30 h110 v150 h-110z" fill="#fff" stroke="{L}" stroke-width="2"/><rect x="45" y="40" width="50" height="8" rx="4" fill="{T}"/><rect x="165" y="40" width="50" height="8" rx="4" fill="{T}"/>{lines}{spiral}<path d="M250 20 v40 l8 -8 l8 8 v-40z" fill="{T}"/>'
    if kind == "planner":
        days = "".join(f'<rect x="{34+i*34}" y="62" width="28" height="100" rx="6" fill="{S if i%2 else C}" stroke="{L}"/>' for i in range(7))
        return f'<rect x="20" y="20" width="260" height="160" rx="16" fill="#fff" stroke="{L}" stroke-width="2"/><rect x="34" y="34" width="120" height="12" rx="6" fill="{I}"/>{days}<path d="M254 32 c-6 -10 -20 -4 -14 6 l14 12 l14 -12 c6 -10 -8 -16 -14 -6z" fill="{T}"/>'
    if kind == "lista":
        items = ""
        for i, done in enumerate([1,1,0,0]):
            y = 46 + i*34
            box = f'<rect x="52" y="{y}" width="22" height="22" rx="5" fill="{T if done else "#fff"}" stroke="{T}" stroke-width="2"/>'
            chk = f'<path d="M57 {y+11} l5 5 l9 -10" stroke="#fff" stroke-width="3" fill="none"/>' if done else ""
            bar = f'<rect x="86" y="{y+7}" width="{150-i*15}" height="8" rx="4" fill="{L if done else I}"/>'
            items += box + chk + bar
        return f'<rect x="34" y="18" width="232" height="168" rx="14" fill="#fff" stroke="{L}" stroke-width="2"/><rect x="120" y="10" width="60" height="18" rx="6" fill="{T}"/>{items}'
    return ""

def tool_card(kind, name, func, use, tip):
    return f'<div class="tcard"><svg viewBox="0 0 300 200" class="till">{ill(kind)}</svg><span class="tk">{func}</span><h4>{name}</h4><p>{use}</p><p class="tip"><b>Dica:</b> {tip}</p></div>'

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

def section_photo(num, title, sub, img):
    add(f"""
<div class="secp">
  <div class="sec"><div class="sec-n">{num}</div><h2 class="sec-t">{title}</h2><p class="sec-s">{sub}</p></div>
</div>
<div class="secp-img" style="background-image:url('img/{img}')"></div>
""", "dark nofoot", "")

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
<div class="story">
  <div class="st-c"><div class="pola r1"><div class="pimg" style="background-image:url('img/c_enfermagem.jpg')"></div></div>
    <span class="tl-k">Origem</span><h4>Técnica de enfermagem</h4><p>Rotina das 7h às 17h, ônibus, plantão. Cuidando de todo mundo.</p></div>
  <div class="st-c"><div class="pola r2"><div class="pimg" style="background-image:url('img/c_familia_herbert.jpg')"></div></div>
    <span class="tl-k">Virada</span><h4>Maternidade e empresa</h4><p>Na pandemia, mãe e empreendedora: aprendi a fazer muito com pouco tempo.</p></div>
  <div class="st-c"><div class="pola r3 method"><span>Lucro<br>Anti-Exaustão®</span></div>
    <span class="tl-k">Método</span><h4>Criei o meu método</h4><p>Para mulheres que querem crescer sem pagar com a própria saúde.</p></div>
  <div class="st-c"><div class="pola r4"><div class="pimg" style="background-image:url('img/c_grupo2.jpg')"></div></div>
    <span class="tl-k">Hoje</span><h4>Mentora de empresárias</h4><p>Centenas de mulheres em workshops, eventos e programas.</p></div>
</div>
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
<p class="note">Se você marcou mais de duas, <b>esta aula foi feita para você.</b></p>
""")

# 9 UM DIA
day = [("Atendimentos", 6, "t"), ("Planos alimentares", 2.5, "t2"), ("WhatsApp e dúvidas", 2, "w"),
       ("Conteúdo", 1.5, "w2"), ("Financeiro e admin.", 1, "w3"), ("Você", 1, "me")]
bar = "".join(f'<div class="seg {c}" style="flex:{h}"><b>{h:g}h</b><span>{n}</span></div>' for n, h, c in day)
add(f"""
<div class="tag">Exemplo · um dia comum</div>
<h2 class="title">13 horas trabalhando. 1 hora para você.</h2>
<div class="daybar">{bar}</div>
<div class="split daynotes">
  <p class="bigserif sm">Quando a agenda é de todo mundo,<br><em>ela não é sua.</em></p>
  <p class="note">Repare: só as 6 horas de atendimento geram receita direta. O resto é trabalho que <b>pode ter processo, modelo ou ajuda.</b></p>
</div>
""")

# 10 INIMIGOS
mitos = [("“Se eu não fizer, ninguém faz.”","Centralização","Parece eficiente no começo e vira gargalo: o consultório não cresce além das suas horas."),
         ("“É mais rápido eu mesma fazer.”","Cultura faz-tudo","Rápido hoje, caro amanhã: você paga com decisões adiadas e noites ocupadas."),
         ("“Cada paciente é único.”","Falta de processos","O paciente é único; o agendamento, o lembrete e o pós-consulta não precisam ser."),
         ("“Depois eu organizo.”","Gestão por urgência","A urgência come o tempo de planejar, e a falta de plano gera mais urgência."),
         ("“Mais pacientes, mais lucro.”","Trabalhar mais = lucrar mais","Existe um ponto em que mais horas trazem mais cansaço, não mais lucro.")]
rows = "".join(f'<div class="mv"><p class="m">{m}</p><span class="arrow">→</span><div><h4>{t}</h4><p>{v}</p></div></div>' for m, t, v in mitos)
add(f"""
<h2 class="title">O inimigo é o sistema, não você</h2>
<div class="mitos wide">{rows}</div>
""")

# 11 QUANTO VALE SUA HORA (detalhado)
add("""
<div class="tag">Exemplo ilustrativo · faça com os seus números</div>
<h2 class="title">Quanto vale a sua hora, de verdade?</h2>
<div class="hour">
  <div class="hc"><span class="hn">1</span><h4>Faturamento</h4><p class="big">R$ 15.000</p><p>consultas, retornos e acompanhamentos no mês</p></div>
  <div class="hc"><span class="hn">2</span><h4>Custos do mês</h4>
    <ul class="costs">
      <li><span>Sala / aluguel</span><b>R$ 1.800</b></li>
      <li><span>Secretária</span><b>R$ 2.000</b></li>
      <li><span>Impostos (Simples ~6%)</span><b>R$ 900</b></li>
      <li><span>Marketing e anúncios</span><b>R$ 600</b></li>
      <li><span>Contador</span><b>R$ 400</b></li>
      <li><span>Sistemas e apps</span><b>R$ 200</b></li>
      <li class="tot"><span>Total</span><b>R$ 5.900</b></li>
    </ul></div>
  <div class="hc"><span class="hn">3</span><h4>Lucro</h4><p class="big">R$ 9.100</p><p>o que sobra para você: R$ 15.000 − R$ 5.900</p></div>
  <div class="hc"><span class="hn">4</span><h4>Horas reais</h4><p class="big">286 h</p><p>13 h por dia × 22 dias. Conte <b>todas</b>: planos, WhatsApp, conteúdo, financeiro</p></div>
</div>
<div class="band"><span>A conta</span><p>Lucro ÷ horas reais = <b>R$ 9.100 ÷ 286 h ≈ R$ 32 por hora</b></p></div>
""")

add("""
<h2 class="title">A hora que você acha × a hora real</h2>
<div class="hvs">
  <div class="hv"><span>O que você pensa</span><p class="hbig">R$ 200</p><p>“Minha consulta custa R$ 200, então ganho R$ 200 por hora.”</p></div>
  <div class="hv real"><span>O que acontece</span><p class="hbig">R$ 32</p><p>Para cada hora de consulta, há mais de 1 hora de trabalho invisível: <b>154 h por mês</b> sem receita direta.</p></div>
  <div class="hv up"><span>Devolvendo 2 h por dia</span><p class="hbig">R$ 38</p><p>Janelas de WhatsApp + modelos de plano: <b>44 h a menos</b> no mês e a hora sobe <b>18%</b>, com o mesmo faturamento.</p></div>
</div>
<p class="note">E as 44 horas devolvidas viram o que você escolher: <b>descanso, família ou crescimento do consultório.</b></p>
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
section("04", "O método na sua agenda", "Lucro Anti-Exaustão®: quatro fases para sair do modo “faço tudo sozinha”.")

# 24 VISÃO GERAL
add("""
<h2 class="title">Método Lucro Anti-Exaustão®</h2>
<p class="sub">Quatro fases, nesta ordem. Pular uma é o motivo de tanta agenda nova não durar.</p>
<div class="anat">
  <div class="an"><span>01</span><h4>Raio-X</h4><p class="w">Operacional</p><p class="ex">Enxergar para onde vão o seu <b>tempo, energia e dinheiro</b>.</p></div>
  <div class="arr">→</div>
  <div class="an"><span>02</span><h4>Extração</h4><p class="w">Comportamental Lucrativa</p><p class="ex">Separar o que <b>gera lucro</b> do que só gera cansaço.</p></div>
  <div class="arr">→</div>
  <div class="an"><span>03</span><h4>Rotina</h4><p class="w">Anti-Exaustão</p><p class="ex">Uma semana que funciona <b>sem depender do seu esgotamento</b>.</p></div>
  <div class="arr">→</div>
  <div class="an hl"><span>04</span><h4>Patrimônio</h4><p class="w">Ativação de Patrimônio Valioso</p><p class="ex">O que você criou passa a <b>trabalhar por você</b>.</p></div>
</div>
<p class="statement sm">O objetivo não é fazer mais. É <em>parar de fazer tudo.</em></p>
""")

fases = [
 ("01","Raio-X Operacional","Mapear com clareza onde o seu tempo, a sua energia e o seu dinheiro estão indo, antes de mudar qualquer coisa.",
  ["Registre a semana real, hora a hora, por 7 dias","Dê nota aos pratos da vida","Mapeie a rotina: consultas, planos, WhatsApp, conteúdo, financeiro"],
  "O que consome o meu tempo sem gerar lucro proporcional?","O mapa da sua semana real, sem filtro."),
 ("02","Extração Comportamental Lucrativa","Descobrir os comportamentos que já geram resultado e os hábitos que estão sabotando o seu lucro.",
  ["Entenda o seu perfil (MBTI): como você decide e se organiza","Liste as atividades de maior retorno × maior desgaste","Separe: eliminar, delegar, transformar em modelo"],
  "O que só eu, com o meu CRN, posso fazer?","A lista do que fica com você e do que sai da sua mesa."),
 ("03","Rotina Anti-Exaustão","Construir uma rotina sustentável, em que você atua com intenção e o consultório para de depender do seu cansaço.",
  ["Monte a semana modelo com dias temáticos","Crie processos: agendamento, confirmação, pós-consulta","Delegue à secretária e defina as janelas de WhatsApp"],
  "A minha semana cabe na minha vida?","Uma nova rotina implementada e testada."),
 ("04","Ativação de Patrimônio Valioso","Transformar o seu método, a sua autoridade e o que você já construiu em patrimônio que gera lucro recorrente.",
  ["Protocolos e modelos de plano que você não refaz do zero","Programas de acompanhamento em vez de consultas avulsas","Conteúdo que atrai o paciente certo enquanto você atende"],
  "O que pode gerar resultado mesmo quando eu não estou?","Um ativo estruturado e o plano dos próximos 90 dias."),
]
for i,(n,t,obj,pr,q,res) in enumerate(fases):
    lis = "".join(f"<li>{x}</li>" for x in pr)
    add(f"""
<div class="phase">
  <div class="ph-l{' last' if i==3 else ''}">
    <span class="ph-k">Fase {n} de 04</span>
    <div class="ph-n">{n}</div>
    <h2>{t}</h2>
    <p>{obj}</p>
  </div>
  <div class="ph-r">
    <div class="ph-b"><span>Na prática, para a nutri</span><ul class="checks">{lis}</ul></div>
    <div class="ph-b q"><span>Pergunta-chave</span><p>{q}</p></div>
    <div class="ph-b res"><span>Você sai com</span><p>{res}</p></div>
  </div>
</div>
""")

add("""
<div class="tag">Programa de Aceleração</div>
<h2 class="title">Aplicar o método com acompanhamento</h2>
<div class="prog">
  <div><span class="pn2">12</span><p><b>semanas</b>, em 4 fases de 3 semanas cada</p></div>
  <div><span class="pn2">3</span><p><b>sessões individuais</b>: abertura, meio e fechamento</p></div>
  <div><span class="pn2">2×</span><p><b>hot seats por mês</b> para destravar o que emperrou</p></div>
  <div class="hl"><span class="pn2">4</span><p><b>kits de ferramentas</b>, um por fase, com acompanhamento no Trello</p></div>
</div>
<p class="note">Quer saber se faz sentido para o seu consultório? <b>Me chama no direct: @martinsscamila</b></p>
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

# 30 FERRAMENTAS DIGITAIS
add(f"""
<div class="tag">No celular e no computador</div>
<h2 class="title">Ferramentas digitais</h2>
<div class="tgrid">
  {tool_card("gcal","Google Agenda","Quando","Atendimentos, blocos da semana modelo e lembretes.","uma cor por tipo de bloco e lembrete automático para o paciente.")}
  {tool_card("trello","Trello","O quê","Quadro visual: pacientes em acompanhamento, conteúdos e pendências.","colunas A fazer, Fazendo e Feito, um cartão por tarefa.")}
  {tool_card("notion","Notion","Onde fica","A central do consultório: protocolos, modelos de plano e ideias de conteúdo.","comece com 3 páginas: Protocolos, Modelos e Conteúdo.")}
</div>
""")

add(f"""
<div class="tag">No papel</div>
<h2 class="title">Ferramentas analógicas</h2>
<div class="tgrid">
  {tool_card("agenda","Agenda física","Foco do dia","Compromissos e as 3 prioridades do dia, longe das notificações.","escreva de manhã, antes de abrir o WhatsApp.")}
  {tool_card("planner","Planner","Visão","Semana e mês inteiros: metas, pratos da vida e revisão de domingo.","15 minutos no domingo para planejar a semana.")}
  {tool_card("lista","Lista de tarefas","Execução","Tudo o que precisa ser feito, em um só lugar, para tirar da cabeça.","no máximo 3 itens prioritários por dia. Riscar dá energia!")}
</div>
""")

# 31 COMBINAR
add("""
<h2 class="title">Como combinar sem se perder</h2>
<div class="stack">
  <div><span>Quando</span><h4>Google Agenda</h4><p>tudo o que tem dia e hora</p></div>
  <div class="pl">+</div>
  <div><span>O quê</span><h4>Trello ou Notion</h4><p>tarefas, processos e modelos</p></div>
  <div class="pl">+</div>
  <div class="hl"><span>Foco</span><h4>Planner, agenda ou lista</h4><p>as 3 prioridades do dia</p></div>
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
