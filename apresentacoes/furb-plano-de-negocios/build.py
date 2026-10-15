import math, pathlib

OUT = pathlib.Path(__file__).parent

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

FOOT = True

# ---------- 1 CAPA ----------
add(f"""
<div class="cover-l">
  <div class="kicker light">FURB · Graduação em Farmácia · Administração e Economia Farmacêutica</div>
  <h1 class="mega">Do sonho<br>ao plano</h1>
  <p class="lead light">Como construir um Plano de Negócios farmacêutico viável — e apresentá-lo com segurança.</p>
  <div class="cover-meta">
    <div><b>Camila Martins Finger</b><br>@martinsscamila</div>
    <div class="vr"></div>
    <div>16 de outubro de 2026<br>09h30 – 11h30</div>
  </div>
</div>
<div class="cover-card">
  {waves(620, 760, 22, "#B65F3A", 0.85, 90, 1.1, 0.55, 1.6)}
  <div class="cc-txt"><span class="script">plano</span><br><span>11 blocos · 1 história</span></div>
</div>
""", "terra", waves(1000, 420, 14, "#FBF6F1", 0.35))

# ---------- 2 QUOTE ----------
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

quote("Quem não define seu caminho acaba vivendo o plano de outra pessoa.")

# ---------- 3 DINÂMICA ABERTURA ----------
add("""
<div class="tag">Dinâmica · 5 min</div>
<h2 class="title light">Quero conhecer vocês</h2>
<div class="prompts">
  <div class="prompt"><span class="pn">01</span><p>Em <b>uma palavra</b>: o que é empreender para você?</p></div>
  <div class="prompt"><span class="pn">02</span><p>Se você abrisse um negócio <b>amanhã</b>, o que ele seria?</p></div>
</div>
""", "dark", waves(900, 460, 16, "#FBF6F1", 0.28))

# ---------- 4 QUEM SOU EU ----------
add("""
<h2 class="title">Prazer, Camila.</h2>
<p class="sub">Uma jornada que começou exatamente onde vocês estão: na saúde.</p>
<div class="timeline">
  <div class="tl"><div class="dot"></div><div class="tl-k">Origem</div><h4>Técnica de enfermagem</h4><p>Conheço a rotina do cuidado na prática — e o peso de um atendimento bem ou mal feito.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Virada</div><h4>Empresária na pandemia</h4><p>Aprendi a empreender empreendendo: errando, ajustando e estruturando.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Método</div><h4>Lucro Anti-Exaustão®</h4><p>Raio-X Operacional, Extração Comportamental, Rotina Anti-Exaustão e Ativação de Patrimônio.</p></div>
  <div class="tl"><div class="dot"></div><div class="tl-k">Hoje</div><h4>Mentora de empresárias</h4><p>Programas de aceleração, workshops in company e palestras.</p></div>
</div>
<p class="statement">Cuidar do negócio também é uma forma de cuidar das pessoas.</p>
""")

# ---------- 5 AGENDA ----------
add("""
<h2 class="title">Como vamos trabalhar hoje</h2>
<div class="agenda">
  <div class="ag"><span class="t">09h30</span><span class="n"></span><span class="d">Abertura e conexão</span></div>
  <div class="ag"><span class="t">09h45</span><span class="n">01</span><span class="d">Por que planejar</span></div>
  <div class="ag"><span class="t">09h55</span><span class="n">02</span><span class="d">O mapa do plano · blocos 1 a 7</span></div>
  <div class="ag pause"><span class="t">10h30</span><span class="n"></span><span class="d">Pausa · 10 min</span></div>
  <div class="ag"><span class="t">10h40</span><span class="n">03</span><span class="d">Os números · blocos 8 a 11</span></div>
  <div class="ag"><span class="t">11h05</span><span class="n">04</span><span class="d">Mão na massa · plano em 1 página</span></div>
  <div class="ag"><span class="t">11h20</span><span class="n">05</span><span class="d">Como apresentar + encerramento</span></div>
</div>
""", "cream", waves(700, 380, 12, "#B65F3A", 0.35))

def section(num, title, sub):
    add(f"""
<div class="sec">
  <div class="sec-n">{num}</div>
  <h2 class="sec-t">{title}</h2>
  <p class="sec-s">{sub}</p>
</div>
""", "dark nofoot", waves(1100, 520, 18, "#B65F3A", 0.55))

# ---------- 6 SEÇÃO 01 ----------
section("01", "Por que planejar", "Antes da planilha, a mentalidade.")

# ---------- 7 ----------
add("""
<div class="split">
  <div>
    <p class="bigserif">A faculdade nos forma para cuidar do paciente.<br><em>Quase ninguém nos ensina a cuidar do negócio.</em></p>
  </div>
  <div class="card soft">
    <p class="card-lead">O plano de negócios é o lugar onde você <b>erra no papel</b> — antes de errar com dinheiro.</p>
    <ul class="checks">
      <li>Testa a ideia antes do investimento</li>
      <li>Mostra se os números fecham</li>
      <li>Organiza a operação antes da inauguração</li>
      <li>Comunica a proposta a sócios, bancos e investidores</li>
    </ul>
  </div>
</div>
""")

# ---------- 8 IMPROVISO x PLANO ----------
add("""
<h2 class="title">Improviso ou plano?</h2>
<div class="vs">
  <div class="vs-col">
    <h3>Empreender no improviso</h3>
    <ul class="dash">
      <li>Abre porque “tem movimento na rua”</li>
      <li>Descobre os custos depois da inauguração</li>
      <li>Quer atender “todo mundo”</li>
      <li>Confunde faturamento com lucro</li>
      <li>O dono faz tudo — e se esgota</li>
    </ul>
  </div>
  <div class="vs-mid">vs</div>
  <div class="vs-col on">
    <h3>Empreender com plano</h3>
    <ul class="dash">
      <li>Valida público e localização antes</li>
      <li>Conhece o ponto de equilíbrio desde o dia 1</li>
      <li>Tem um público e um diferencial claros</li>
      <li>Acompanha margem, caixa e lucro</li>
      <li>Estrutura processos e equipe</li>
    </ul>
  </div>
</div>
""")

# ---------- 9 ONDE EMPREENDER ----------
add("""
<h2 class="title">Onde o farmacêutico pode empreender</h2>
<div class="grid3">
  <div class="tile"><span class="ti">01</span><h4>Farmácia comunitária</h4><p>Dispensação com cuidado e serviços no bairro.</p></div>
  <div class="tile"><span class="ti">02</span><h4>Consultório farmacêutico</h4><p>Cuidado clínico, revisão da farmacoterapia, acompanhamento.</p></div>
  <div class="tile"><span class="ti">03</span><h4>Farmácia de manipulação</h4><p>Personalização de doses, formas e fórmulas.</p></div>
  <div class="tile"><span class="ti">04</span><h4>Startup / healthtech</h4><p>Tecnologia aplicada à adesão, ao acesso e à gestão.</p></div>
  <div class="tile"><span class="ti">05</span><h4>Consultoria e treinamento</h4><p>Regularização sanitária, boas práticas, capacitação de equipes.</p></div>
  <div class="tile"><span class="ti">06</span><h4>Serviços de saúde</h4><p>Vacinação, testes rápidos, cuidado ao paciente crônico.</p></div>
</div>
<p class="note">Desde a Lei 13.021/2014, a farmácia é <b>estabelecimento de saúde</b> — não apenas comércio.</p>
""")

# ---------- 10 SEÇÃO 02 ----------
section("02", "O mapa do plano", "11 blocos que contam uma única história.")

# ---------- 11 VISÃO GERAL ----------
blocks = [("Resumo executivo","O negócio em 1 minuto"),("Descrição do negócio","Missão, visão, valores, problema"),
          ("Análise de mercado","Público, concorrência, oportunidades"),("Legal e regulatório","Normas, licenças, RT"),
          ("Produtos e serviços","O que vende e o que diferencia"),("Estrutura e operação","Espaço, pessoas, tecnologia"),
          ("Plano de marketing","Posicionamento e fidelização"),("Planejamento financeiro","Investimento, custos, receita"),
          ("O primeiro ano","Como a empresa nasce e cresce"),("Análise SWOT","Só no documento escrito"),("Conclusão","É viável? Por quê?")]
cells = "".join(f'<div class="bk{" off" if i==9 else ""}"><span>{i+1:02d}</span><h5>{t}</h5><p>{d}</p></div>' for i,(t,d) in enumerate(blocks))
add(f"""
<h2 class="title">Os 11 blocos do seu plano</h2>
<div class="blocks">{cells}<div class="bk legend"><p>Cada bloco responde a uma pergunta que a banca — ou o banco — vai fazer.</p></div></div>
""")

# ---------- 12 CASO ----------
add("""
<div class="tag light">Exemplo ilustrativo · criado para esta aula</div>
<h2 class="title light huge">Nosso caso de hoje:<br>Farmácia Bem Viver</h2>
<div class="case-row">
  <div><span>Tipo</span><p>Farmácia comunitária com consultório farmacêutico</p></div>
  <div><span>Onde</span><p>Bairro residencial de Blumenau/SC</p></div>
  <div><span>Para quem</span><p>Idosos e pacientes com doenças crônicas</p></div>
</div>
<p class="lead light small">Vamos usá-la para preencher cada bloco junto — e vocês aplicam no projeto do grupo.</p>
""", "terra", waves(900, 420, 14, "#FBF6F1", 0.3))

# ---------- 13 BLOCO 1 ----------
def bh(n, t):
    return f'<div class="bh"><span>Bloco {n:02d}</span></div><h2 class="title">{t}</h2>'

add(f"""
{bh(1,"Resumo executivo")}
<div class="split s46">
  <div>
    <ul class="checks big">
      <li>Nome do negócio</li><li>Tipo de empreendimento</li><li>Local de atuação</li>
      <li>Público-alvo</li><li>Diferencial</li><li>Breve descrição da proposta</li>
    </ul>
    <p class="pill">Escreva por último. Apresente primeiro.</p>
  </div>
  <div class="card dark">
    <div class="ck">A fórmula do pitch em 1 frase</div>
    <p class="formula">Ajudamos <u>[público]</u> a <u>[resolver um problema]</u> por meio de <u>[solução]</u>, diferente de <u>[alternativa]</u> porque <u>[diferencial]</u>.</p>
    <div class="hr"></div>
    <p class="ex">“Ajudamos idosos e pacientes crônicos de Blumenau a usar seus medicamentos com segurança, por meio de uma farmácia com consultório farmacêutico — diferente das grandes redes, porque cada paciente tem acompanhamento individual.”</p>
  </div>
</div>
""")

# ---------- 14 BLOCO 2 ----------
add(f"""
{bh(2,"Descrição do negócio")}
<div class="cols3">
  <div class="col"><h3>Missão</h3><p class="q">Por que existimos?</p><p class="ex">Cuidar da saúde de quem mais precisa, com atenção farmacêutica próxima e humanizada.</p></div>
  <div class="col"><h3>Visão</h3><p class="q">Onde queremos chegar?</p><p class="ex">Ser referência em cuidado ao paciente crônico no Vale do Itajaí até 2031.</p></div>
  <div class="col"><h3>Valores</h3><p class="q">Como agimos?</p><p class="ex">Ética · Acolhimento · Segurança do paciente · Proximidade</p></div>
</div>
<div class="band"><span>Problema que resolvemos</span><p>Pacientes polimedicados, sem orientação, com baixa adesão ao tratamento.</p></div>
""")

# ---------- 15 BLOCO 3.1 ----------
add(f"""
{bh(3,"Público-alvo × persona")}
<div class="split">
  <div class="card soft">
    <div class="ck">Público-alvo · um grupo</div>
    <ul class="dash">
      <li>Adultos com 60 anos ou mais</li><li>Classes B e C, bairro residencial</li>
      <li>Hipertensão, diabetes, dislipidemia</li><li>Uso contínuo de medicamentos</li>
    </ul>
  </div>
  <div class="card terra">
    <div class="ck">Persona · uma pessoa</div>
    <h3 class="persona">Dona Marli, 68</h3>
    <p>Aposentada, hipertensa e diabética. Toma 6 medicamentos por dia e confunde os horários. A filha mora em outra cidade.</p>
    <p class="want">O que ela procura: <b>alguém que conheça a história dela.</b></p>
  </div>
</div>
<p class="note">A persona pode se parecer com você — mas não pode ser você.</p>
""")

# ---------- 16 BLOCO 3.2 ----------
add(f"""
{bh(3,"Concorrência")}
<table class="tbl">
  <tr><th>Concorrente</th><th>O que oferece</th><th>Ponto forte</th><th>Ponto fraco</th></tr>
  <tr><td>Grandes redes</td><td>Mix amplo, app, programas de desconto</td><td>Preço e conveniência</td><td>Atendimento impessoal, alta rotatividade</td></tr>
  <tr><td>Farmácias do bairro</td><td>Dispensação e relacionamento</td><td>Proximidade</td><td>Pouca estrutura de serviços</td></tr>
  <tr><td>E-commerce e apps</td><td>Entrega rápida</td><td>Comodidade</td><td>Nenhum acompanhamento clínico</td></tr>
</table>
<p class="pill">Visite como cliente oculto: atendimento, preço, espera e serviços.</p>
""")

# ---------- 17 BLOCO 3.3 ----------
add(f"""
{bh(3,"Oportunidades de mercado")}
<div class="grid3 trends">
  <div class="tile"><h4>Envelhecimento da população</h4><p>Mais pessoas usando mais medicamentos por mais tempo.</p></div>
  <div class="tile"><h4>Doenças crônicas</h4><p>Demanda contínua por acompanhamento e adesão.</p></div>
  <div class="tile"><h4>Serviços farmacêuticos clínicos</h4><p>O farmacêutico assumindo o cuidado, não só a dispensação.</p></div>
  <div class="tile"><h4>Saúde digital e delivery</h4><p>WhatsApp, entrega, lembretes, telessaúde.</p></div>
  <div class="tile"><h4>Prevenção e vacinação</h4><p>A farmácia como porta de entrada do cuidado.</p></div>
  <div class="tile"><h4>Personalização</h4><p>Manipulação, dermocosméticos, nutrição.</p></div>
</div>
<p class="note">Qual dessas tendências o negócio do seu grupo aproveita?</p>
""")

# ---------- 18 BLOCO 4 ----------
add(f"""
{bh(4,"Aspectos legais e regulatórios")}
<div class="split s55">
  <div>
    <div class="ck dk">Legislação de referência</div>
    <ul class="law">
      <li><b>Lei 5.991/1973</b> controle sanitário do comércio de medicamentos</li>
      <li><b>Lei 13.021/2014</b> farmácia como estabelecimento de saúde</li>
      <li><b>RDC 44/2009</b> Boas Práticas Farmacêuticas e serviços</li>
      <li><b>RDC 67/2007</b> Boas Práticas de Manipulação (se aplicável)</li>
      <li><b>Portaria SVS/MS 344/1998</b> medicamentos sujeitos a controle especial</li>
      <li><b>RDC 222/2018</b> gerenciamento de resíduos de serviços de saúde</li>
      <li><b>Res. CFF 585 e 586/2013</b> atribuições clínicas e prescrição farmacêutica</li>
    </ul>
  </div>
  <div class="card soft">
    <div class="ck">Checklist de licenças</div>
    <ul class="checks">
      <li>CNPJ e alvará de funcionamento municipal</li>
      <li>Licença sanitária (Vigilância Sanitária)</li>
      <li>AFE na Anvisa (+ AE para controlados)</li>
      <li>Registro no CRF-SC e Certidão de Regularidade Técnica</li>
      <li>Farmacêutico RT presente em todo o horário de funcionamento</li>
      <li>Vistoria do Corpo de Bombeiros</li>
    </ul>
  </div>
</div>
<p class="note">Licenças levam tempo: coloque-as no cronograma <b>antes</b> da inauguração.</p>
""")

# ---------- 19 BLOCO 5 ----------
add(f"""
{bh(5,"Produtos e serviços")}
<div class="split">
  <div class="card soft">
    <div class="ck">Produtos · o que você vende</div>
    <ul class="dash">
      <li>Medicamentos: referência, genéricos e similares</li><li>MIPs</li>
      <li>Dermocosméticos</li><li>Higiene e cuidados pessoais</li><li>Nutrição e suplementos</li>
    </ul>
  </div>
  <div class="card terra">
    <div class="ck">Serviços · o que te diferencia</div>
    <ul class="dash">
      <li>Aferição de pressão e glicemia capilar</li><li>Revisão da farmacoterapia</li>
      <li>Acompanhamento farmacoterapêutico</li><li>Testes rápidos e vacinação</li>
      <li>Organização de medicamentos e tabela de horários</li>
    </ul>
  </div>
</div>
<p class="statement sm">Produto se compara por preço. <em>Serviço se escolhe por confiança.</em></p>
""")

# ---------- 20 BLOCO 6 ----------
add(f"""
{bh(6,"Estrutura e operação")}
<div class="cols3">
  <div class="col"><h3>Espaço</h3><ul class="dash">
    <li>Área de dispensação</li><li>Sala de serviços farmacêuticos</li><li>Estoque e área de controlados</li><li>Área administrativa</li><li>Sanitário e DML</li></ul></div>
  <div class="col"><h3>Pessoas</h3><ul class="dash">
    <li>Farmacêuticos cobrindo 100% do horário</li><li>Atendentes</li><li>Apoio administrativo e financeiro</li></ul></div>
  <div class="col"><h3>Tecnologia</h3><ul class="dash">
    <li>Sistema de gestão (ERP) e PDV</li><li>Escrituração de controlados</li><li>Geladeira para termolábeis com registro de temperatura</li><li>Termo-higrômetro, esfigmomanômetro, glicosímetro</li></ul></div>
</div>
<div class="band"><span>Conta rápida</span><p>Aberta 12 h × 7 dias = <b>84 h/semana</b> ÷ 44 h por farmacêutico ≈ <b>2 farmacêuticos</b> + cobertura de folgas e férias.</p></div>
""")

# ---------- 21 BLOCO 7 ----------
add(f"""
{bh(7,"Plano de marketing")}
<div class="quad">
  <div><span>Posicionamento</span><h4>Como quero ser lembrada?</h4><p>“A farmácia que conhece você pelo nome.”</p></div>
  <div><span>Divulgação</span><h4>Como as pessoas me encontram?</h4><p>Conteúdo educativo no Instagram, ações de saúde no bairro, parcerias com médicos, UBS, academias e grupos de idosos.</p></div>
  <div><span>Canais</span><h4>Como conversamos?</h4><p>Balcão, WhatsApp, telefone e delivery.</p></div>
  <div><span>Fidelização</span><h4>Por que o paciente volta?</h4><p>Lembrete de recompra, programa de acompanhamento, cartão fidelidade, contato pós-atendimento.</p></div>
</div>
<p class="note">A imagem que você transmite fica no subconsciente do cliente.</p>
""")

# ---------- 22 PAUSA ----------
add("""
<div class="center">
  <div class="tag light">10h30 · 10 minutos</div>
  <h2 class="mega">Pausa</h2>
  <p class="lead light">Voltamos às 10h40. Enquanto isso, pense:<br><b>qual seria o diferencial do seu negócio?</b></p>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.3))

# ---------- 23 SEÇÃO 03 ----------
section("03", "Os números", "Faturamento não é saúde.")

# ---------- 24 BLOCO 8 ----------
add(f"""
{bh(8,"Planejamento financeiro")}
<div class="fin">
  <div><span>8.1</span><h4>Investimento inicial</h4><p>Reforma · equipamentos · estoque inicial · licenças e registros</p><p class="warn">+ capital de giro</p></div>
  <div><span>8.2</span><h4>Custos fixos</h4><p>Aluguel · salários e encargos · energia, água, internet · sistema de gestão · contabilidade</p></div>
  <div><span>8.3</span><h4>Custos variáveis</h4><p>Reposição de estoque (CMV) · insumos · impostos sobre a venda</p><p class="warn">+ taxas de cartão</p></div>
  <div><span>8.4</span><h4>Faturamento</h4><p>Receita mensal estimada · fontes: medicamentos, não medicamentos e serviços</p></div>
</div>
<p class="note">Capital de giro e taxas de cartão são os esquecidos que mais custam caro.</p>
""")

# ---------- 25 4 NÚMEROS ----------
add("""
<h2 class="title light">Os 4 números que dizem se o negócio é saudável</h2>
<div class="nums">
  <div><span>1</span><h4>Margem de contribuição</h4><p class="f">Vendas − custos variáveis</p><p>Quanto cada venda deixa para pagar a estrutura.</p></div>
  <div><span>2</span><h4>Ponto de equilíbrio</h4><p class="f">Custos fixos ÷ % de margem</p><p>Quanto preciso vender para não ter prejuízo.</p></div>
  <div><span>3</span><h4>Capital de giro</h4><p class="f">Estoque + prazos − fornecedores</p><p>O fôlego para operar até a venda virar caixa.</p></div>
  <div><span>4</span><h4>Lucro líquido</h4><p class="f">O que sobra depois de tudo</p><p>E em quantos meses ele paga o investimento (payback).</p></div>
</div>
""", "dark", waves(800, 360, 12, "#B65F3A", 0.45))

# ---------- 26 EXEMPLO ----------
add("""
<div class="tag">Exemplo ilustrativo · Farmácia Bem Viver</div>
<h2 class="title">Quanto preciso vender?</h2>
<div class="calc">
  <div><span class="v">R$ 45 mil</span><span class="l">custos fixos por mês</span></div>
  <div class="op">÷</div>
  <div><span class="v">30%</span><span class="l">margem de contribuição média</span></div>
  <div class="op">=</div>
  <div class="hl"><span class="v">R$ 150 mil</span><span class="l">ponto de equilíbrio mensal</span></div>
</div>
<div class="calc2">
  <div><b>≈ R$ 5.770</b> por dia <small>(26 dias úteis)</small></div>
  <div><b>≈ 77 atendimentos</b> por dia <small>(ticket médio de R$ 75)</small></div>
  <div><b>≈ 29 meses</b> de payback <small>(R$ 350 mil investidos ÷ R$ 12 mil de lucro/mês)</small></div>
</div>
<p class="note">Isso é realista para a sua localização? Se não for, o plano mudou <b>antes</b> de você perder dinheiro.</p>
""")

# ---------- 27 BLOCO 9 ----------
add(f"""
{bh(9,"Como você pensa o primeiro ano")}
<div class="year">
  <div class="yr pre"><span>Pré-abertura</span><h4>Preparar</h4><p>Licenças, reforma, equipe, estoque e sistema.</p></div>
  <div class="yr"><span>Meses 1–3</span><h4>Abrir as portas</h4><p>Captação, rotina da equipe, primeiros indicadores.</p></div>
  <div class="yr"><span>Meses 4–6</span><h4>Ajustar a rota</h4><p>Rever mix, preços, escalas e o que não vende.</p></div>
  <div class="yr"><span>Meses 7–9</span><h4>Ganhar ritmo</h4><p>Ampliar serviços e parcerias.</p></div>
  <div class="yr"><span>Meses 10–12</span><h4>Consolidar</h4><p>Fidelização, revisão do plano, metas do ano 2.</p></div>
</div>
<p class="statement sm">Um negócio saudável <em>não depende da exaustão do dono.</em></p>
""")

# ---------- 28 BLOCO 10 SWOT ----------
add(f"""
{bh(10,"Análise SWOT")}
<p class="pill warnpill">Vai no documento escrito · não entra na apresentação</p>
<div class="split s46">
  <div class="swot">
    <div><b>Forças</b><span>interno · ajuda</span></div>
    <div><b>Fraquezas</b><span>interno · atrapalha</span></div>
    <div><b>Oportunidades</b><span>externo · ajuda</span></div>
    <div><b>Ameaças</b><span>externo · atrapalha</span></div>
  </div>
  <div>
    <div class="ck dk">Cruze os quadrantes (TOWS)</div>
    <ul class="law">
      <li><b>F + O · Ofensiva</b> use as forças para aproveitar as oportunidades</li>
      <li><b>F + A · Confrontativa</b> use as forças para se proteger das ameaças</li>
      <li><b>Fr + O · Reforço</b> corrija fraquezas para não perder oportunidades</li>
      <li><b>Fr + A · Defensiva</b> reduza fraquezas onde as ameaças batem</li>
    </ul>
  </div>
</div>
""")

# ---------- 29 BLOCO 11 ----------
add(f"""
{bh(11,"Conclusão")}
<div class="cols3 qs">
  <div class="col"><span class="bign">?</span><h3>É viável?</h3><p>Justifique com números: ponto de equilíbrio, payback e demanda.</p></div>
  <div class="col"><span class="bign">!</span><h3>Quais os desafios?</h3><p>Seja honesto. A banca confia em quem conhece os próprios riscos.</p></div>
  <div class="col"><span class="bign">→</span><h3>Quais as perspectivas?</h3><p>Para onde o negócio cresce em 3 a 5 anos?</p></div>
</div>
""")

# ---------- 30 SEÇÃO 04 ----------
section("04", "Mão na massa", "Do conceito para o projeto do seu grupo.")

# ---------- 31 DINÂMICA ----------
items = ["Nome do negócio","Tipo de empreendimento","Persona","Problema que resolve","Diferencial","Serviço-âncora","Custo fixo estimado","Pitch de 30 segundos"]
cells = "".join(f'<div><span>{i+1:02d}</span><p>{t}</p></div>' for i,t in enumerate(items))
add(f"""
<div class="tag">Dinâmica · em grupos · 15 min</div>
<h2 class="title">Plano em 1 página</h2>
<div class="onepage">{cells}</div>
<p class="note">No final, 2 ou 3 grupos apresentam o pitch. <b>Quanto tempo têm 30 segundos?</b></p>
""")

# ---------- 32 SEÇÃO 05 ----------
section("05", "Como apresentar", "O plano precisa convencer — não só existir.")

# ---------- 33 PITCH ----------
steps = [("Gancho","O problema, contado pela persona"),("Solução","O que o negócio faz"),("Mercado","Quem compra e quanto"),
         ("Operação","Como funciona na prática"),("Números","Investimento, equilíbrio, payback"),("Por que vai dar certo","Diferencial + equipe")]
st = "".join(f'<div class="st"><span>{i+1}</span><h4>{a}</h4><p>{b}</p></div>' for i,(a,b) in enumerate(steps))
add(f"""
<h2 class="title">A estrutura de uma boa apresentação</h2>
<div class="steps">{st}</div>
<div class="tips">
  <div>Uma ideia por slide</div><div>Números grandes, texto pequeno</div><div>Conte a história da persona</div><div>Ensaie com cronômetro</div>
</div>
""")

# ---------- 34 ERROS ----------
add("""
<h2 class="title light">Os erros mais comuns</h2>
<div class="errs">
  <div><span>01</span><p>Faturamento otimista demais</p></div>
  <div><span>02</span><p>Esquecer capital de giro e taxas</p></div>
  <div><span>03</span><p>Subestimar o prazo das licenças</p></div>
  <div><span>04</span><p>Público-alvo “todo mundo”</p></div>
  <div><span>05</span><p>Copiar o concorrente sem diferencial</p></div>
  <div><span>06</span><p>O dono que faz tudo sozinho</p></div>
</div>
""", "dark", waves(800, 380, 12, "#B65F3A", 0.45))

# ---------- 35 QUOTE ----------
quote("Quem decide, realiza.<br>Quem adia, apenas sonha.")

# ---------- 36 PALAVRA ----------
add("""
<div class="center">
  <div class="tag light">Encerramento</div>
  <h2 class="title light huge c">Qual palavra define<br>o encontro de hoje?</h2>
</div>
""", "dark nofoot", waves(1100, 480, 18, "#B65F3A", 0.5))

# ---------- 37 OBRIGADA ----------
add("""
<div class="center">
  <h2 class="mega">Obrigada!</h2>
  <p class="lead light">Transforme sua visão em ação: o futuro começa agora.</p>
  <div class="cover-meta c">
    <div><b>Camila Martins Finger</b><br>Método Lucro Anti-Exaustão®</div>
    <div class="vr"></div>
    <div>Instagram<br><b>@martinsscamila</b></div>
  </div>
</div>
""", "terra nofoot", waves(1100, 480, 16, "#FBF6F1", 0.32))

# ---------------- RENDER ----------------
css = (OUT / "style.css").read_text()
pages = []
total = len(SLIDES)
for i, (cls, html, deco) in enumerate(SLIDES, 1):
    foot = "" if "nofoot" in cls else f'<div class="foot"><span>Plano de Negócios Farmacêutico · FURB</span><span>@martinsscamila &nbsp;·&nbsp; {i:02d}</span></div>'
    pages.append(f'<section class="s {cls}">{deco}{html}{foot}</section>')
doc = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Do sonho ao plano</title><style>{css}</style></head><body>{''.join(pages)}</body></html>"
(OUT / "deck.html").write_text(doc)
print("slides:", total)
