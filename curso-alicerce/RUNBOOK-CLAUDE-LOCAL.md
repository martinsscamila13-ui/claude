# RUNBOOK: execução do curso Alicerce pelo Claude local

> **Para o Claude que vai executar este arquivo:** você está no computador da Camila Martins Finger, com acesso a esta pasta e a um navegador que você controla: o **navegador embutido do app Claude para computador** (ícone de globo, Ctrl/Cmd+Shift+B) ou a extensão **Claude in Chrome**. Sua missão é publicar e configurar o curso **Método Lucro Anti-Exaustão® – Alicerce** (R$ 497) na **Kiwify** e no **Google Classroom**, revisar todos os materiais e deixar tudo pronto para vender e para liberar as mentoradas gratuitamente.
>
> Siga as fases **na ordem**. Cada fase tem: objetivo, passos, critério de pronto e pontos de parada (🛑) em que você **precisa** da Camila. Registre tudo em `progresso.md` (modelo no final).

---

## 0. Regras de ouro (leia antes de qualquer ação)

1. **Leia primeiro:** `contexto-marca.md` (fatos, prova social e tom de voz), `README.md` (mapa de arquivos) e `complementares/00-diagnostico-e-plano-10x.md` (estratégia da oferta).
2. **Prova social oficial:** **+400 mentoradas** e **+2 mil mulheres impactadas com palestras e treinamentos**. Nunca escreva "+200".
3. **As aulas são curtas de propósito** (5 a 8 min, diretas e com uma ação no final). Não sugira alongar, juntar ou "completar" aulas.
4. **Nunca invente** depoimentos, números de resultado, "preço de", escassez ou prazo falso. Se faltar dado real, deixe o espaço reservado e pergunte.
5. **Dados sensíveis são da Camila.** Nunca digite CPF, CNPJ, dados bancários, senhas, códigos 2FA ou cartão. Pare e peça para ela fazer.
6. **Antes de publicar, salvar oferta, enviar convite ou e-mail, ou ativar cupom,** mostre um resumo e espere o "ok" dela.
7. **Nunca exclua** nada (aula, aluna, produto, arquivo) sem confirmação explícita. Janelas de confirmação do navegador podem travar a extensão: peça para a Camila clicar.
8. **Não publique nomes de clientes ou mentoradas** sem autorização por escrito.
9. **Uploads do computador:** o navegador (embutido ou extensão) normalmente não consegue escolher arquivos na janela do sistema. Quando precisar subir um arquivo local, diga exatamente qual arquivo e onde arrastar, e espere a Camila. Anexos do **Google Drive** você consegue fazer pelo seletor do Drive.
10. **Na dúvida, pergunte.** Uma pergunta custa menos do que desfazer uma publicação.
11. Se uma ação falhar 2 vezes, pare, explique o que aconteceu e proponha alternativas.

---

## 1. Inventário dos arquivos

| Pasta / arquivo | O que é | Onde vai |
|---|---|---|
| `contexto-marca.md` | Fonte única de verdade da marca | Referência para todas as revisões |
| `Guia_Classroom_Kiwify_Lucro_Anti-Exaustao.md` (na pasta pai ou em `docs/`) | Guia humano passo a passo, com textos de aulas e módulos | Referência de textos |
| `landing-page.html` | Página de vendas | Hospedagem (Fase 7) e campo "Página de vendas" da Kiwify |
| `obrigado.html` | Página pós-compra | Página de obrigado da Kiwify |
| `emails/*.html` | Sequências de e-mail em HTML | Ferramenta de e-mail (Fase 8) |
| `copy-divulgacao.md` | Textos da Kiwify, bio, posts, stories, anúncios | Kiwify, Instagram, Meta Ads |
| `complementares/` | Diagnóstico 10x, e-book, caderno de exercícios, avaliações e kit de IA | Área de membros (Kiwify e Classroom) e bônus |
| `complementares/ia/` | Instruções do assistente, base de conhecimento e prompts por aula | GPT / Projeto Claude / Gem (Fase 6) |
| `guerrilha/` | Plano de 90 dias, quiz, indicação, scripts e palestra, conteúdo de 30 dias | Quiz na hospedagem; o resto é operação da Camila |
| `ferramentas/mapa-aulas.csv` | Mapa oficial: aula, título, arquivo original e nome final | Fases 2, 4 e 5 |
| `ferramentas/organizar-e-converter-videos.py` | Converte .mov em .mp4 e organiza por módulo | Fase 2 |
| `ferramentas/aplicar-valores.py` + `valores.exemplo.json` | Preenche links e campos em todos os arquivos | Fase 3 |
| `ferramentas/verificar-materiais.py` | Revisão automática (prova social, campos vazios, links quebrados) | Fases 1, 3 e 10 |

**Passo 1.1:** rode `python3 ferramentas/verificar-materiais.py` e salve a saída em `progresso.md`. Isso mostra o estado inicial.

**Passo 1.2:** abra no navegador (`file://`) e veja, no desktop e no modo celular do DevTools (390 px):
- `landing-page.html` e `obrigado.html`
- `guerrilha/01-quiz-indice-exaustao.html`: responda o quiz inteiro
- `complementares/ebook-raio-x-empresaria-exausta.pdf` e `complementares/workbook-metodo-alicerce.pdf`

Anote qualquer erro visual.

✅ **Pronto quando:** o inventário e o estado inicial estiverem registrados em `progresso.md`.

---

## 1A. Provas sociais e autorizações (antes de publicar qualquer case com nome)

1. Leia `prova-social-e-autoridade.md` (versão pública) e `privado/banco-de-provas.md` (nomes, fontes e status).
   - A pasta `privado/` **não pode** ir para o GitHub nem para a hospedagem. Ao montar `site/`, nunca copie `privado/`.
2. 🛑 Pergunte à Camila quais cases ela quer pedir autorização primeiro. A ordem sugerida está no §5 do banco de provas.
3. Para cada mentorada, monte a mensagem de WhatsApp do §5 com o texto do case.
   - 🛑 A Camila envia pelo WhatsApp dela. Você **não** envia.
4. Registre as respostas no banco de provas: **com nome e @**, **só primeiro nome** ou **sem nome**.
5. Com a autorização, atualize nos cards da página de vendas (seção `#cases`): o campo `.quem` com o primeiro nome e o @, e o depoimento com as palavras dela.
6. Confirme dois pontos antes de publicar:
   - o **prêmio da ACIF** (Case C);
   - a frase "parou de correr atrás do tempo e nada mais fica atrasado" (Case B).
7. Nunca publique faturamento de mentorada sem o ok dela.

✅ **Pronto quando:** cada case estiver marcado como autorizado (com o nível) ou mantido sem nome.

---

## 2. Vídeos: localizar, conferir e converter

**Contexto:** as aulas gravadas estão no Google Drive, na pasta *"Metodologia - Lucro Anti-Exaustão (Camila Martins)"*, que pertence à conta de quem editou (luizaramosmarketing). A Camila só tem permissão de leitura. Os arquivos são .mov, somam cerca de 5,3 GB e há aulas com mais de 500 MB.

### 2.1 Obter os arquivos
- 🛑 Pergunte à Camila qual caminho ela prefere:
  - **A (melhor):** pedir à editora a transferência de propriedade ou permissão de **Editor** da pasta;
  - **B:** baixar tudo pelo navegador (botão direito na pasta → **Fazer download**, que gera vários .zip);
  - **C:** usar o Google Drive para computador e sincronizar a pasta.
- Se for a opção B, depois do download extraia os .zip para `~/Alicerce/videos-originais/`.

### 2.2 Conferir contra o mapa
- `ferramentas/mapa-aulas.csv` tem as 34 entradas: 31 aulas mais 3 introduções de fase.
- Pontos conhecidos:
  - **Aula 19** (Plano Anti-Exaustão): **FALTA**.
  - **Aula 23** (Protocolo de Disciplina Sustentável): **FALTA**.
  - **Aula 30** (Visão de Legado): **CONFIRMAR**. Pode ser que a numeração esteja deslocada e a "Introdução Fase 4" seja a Aula 25.
  - **"Finalização fase 3"**: só 6 MB, **CONFERIR** se está completa.
- Rode em modo simulação:
  ```bash
  python3 ferramentas/organizar-e-converter-videos.py --origem ~/Alicerce/videos-originais --destino ~/Alicerce/videos-final --simular
  ```
- 🛑 Mostre à Camila a lista de **FALTA / CONFERIR** e pergunte: gravar as que faltam, publicar sem elas (ajustando a estrutura) ou adiar o lançamento?

### 2.3 Converter
- Instale o ffmpeg se precisar (macOS: `brew install ffmpeg`; Windows: `winget install ffmpeg`).
- Rode sem `--simular`:
  ```bash
  python3 ferramentas/organizar-e-converter-videos.py --origem ~/Alicerce/videos-originais --destino ~/Alicerce/videos-final
  ```
- Confira o `relatorio-videos.csv`:
  - toda aula com menos de 60 s ou com "ERRO" precisa ser revista;
  - o tamanho final deve ficar entre 20% e 50% do original.
- Abra 3 vídeos convertidos ao acaso e confira som, imagem e começo e fim.

### 2.4 Revisão de qualidade dos vídeos (amostragem)
Para cada módulo, assista ao **primeiro e ao último minuto** de cada aula e anote:
- se a aula começa com a frase padrão de abertura;
- se termina com uma ação clara;
- se há problema de áudio, corte errado ou tela preta.

Não critique a duração, porque as aulas são curtas de propósito.

✅ **Pronto quando:** existir `~/Alicerce/videos-final/` organizado por módulo, o relatório estiver revisado e a Camila tiver decidido sobre as aulas faltantes.

---

## 3. Preencher links e campos

1. Copie `ferramentas/valores.exemplo.json` para `ferramentas/valores.json`.
2. 🛑 Peça à Camila os valores que só ela tem:
   - WhatsApp com DDD;
   - link do grupo de avisos;
   - prazo de acesso (12 meses ou vitalício);
   - cupom de lançamento, só se houver prazo real;
   - foto oficial;
   - ferramenta de e-mail, para o link de descadastro.
3. Os links da Kiwify (checkout, área de membros) e da hospedagem (LP e quiz) **só existem depois das Fases 5 e 7**. Preencha o que der agora e volte aqui depois.
4. Rode `python3 ferramentas/aplicar-valores.py`. Ele gera uma cópia preenchida em `publicar/` e lista os campos pendentes.
5. Rode `python3 ferramentas/verificar-materiais.py --publicar` até restarem só pendências conhecidas, como depoimentos aguardando autorização.

✅ **Pronto quando:** `publicar/` existir e as pendências estiverem listadas em `progresso.md`.

---

## 4. Google Classroom (turma de teste e plano B para as mentoradas)

> **Pré-requisitos:**
> - a Camila logada no Gmail pessoal, em classroom.google.com;
> - os vídeos finais no **Drive dela** (suba `~/Alicerce/videos-final/` para uma pasta "Alicerce – CURSO FINAL" no Drive);
> - os PDFs do e-book e do caderno de exercícios também no Drive.

### 4.1 Criar e configurar a turma
1. Abra classroom.google.com → **+** → **Criar turma**.
   - Nome: `Método Lucro Anti-Exaustão® – Alicerce`
   - Seção: `Turma Mentoradas`
   - Assunto: `Gestão, Rotina e Lucro para Empresárias`
2. Abra a **engrenagem (Configurações)**:
   - código da turma **oculto** no cabeçalho;
   - Mural: alunos **só comentam**;
   - **sem** sistema de notas.
3. **Personalizar** → cor próxima do terracota (#9C4A3A).
   - 🛑 Se a Camila quiser um banner próprio, peça para ela subir o arquivo.

### 4.2 Tópicos (um por módulo, nesta ordem)
1. Módulo 0 — Comece por aqui
2. Módulo 1 — Fase 1: Raio-X Operacional
3. Módulo 2 — Fase 2: Extração Comportamental Lucrativa
4. Módulo 3 — Fase 3: Rotina Anti-Exaustão
5. Módulo 4 — Fase 4: Ativação de Patrimônio Valioso
6. Materiais e bônus
7. Assistente de IA

### 4.3 Aulas (Criar → Material)
Para **cada linha** do `mapa-aulas.csv` que não estiver marcada como FALTA:
- **Título:** `Aula 05 — Por que você está aqui agora?` (sempre com 2 dígitos; introduções como `Aula 00 — Introdução à Fase 2`).
- **Descrição:** a descrição da aula na seção 3 do guia, mais a linha `📌 Depois da aula: preencha a ferramenta correspondente no Caderno de Exercícios (página X).` Use a página real do caderno.
- **Tópico:** o do módulo.
- **Anexo:** Adicionar → Google Drive → o vídeo `.mp4` final.
- **Publicar.**

> O Classroom mostra o item mais recente no topo do tópico. **Crie de trás para frente** (a última aula primeiro), ou reordene arrastando no fim.

### 4.4 Materiais e bônus
No tópico "Materiais e bônus", crie um material para cada item:
- Caderno de Exercícios (PDF);
- E-book "Raio-X da Empresária Exausta" (PDF);
- Planilhas de ferramentas por fase. Use links que forçam a aluna a fazer uma cópia: troque `/edit` por `/copy` no fim do link.

### 4.5 Avaliações por módulo
- Use `complementares/avaliacoes-por-modulo.md`.
- No Classroom: **Criar → Teste com perguntas**, que abre um Google Forms já ligado à turma.
  - Uma avaliação por módulo, com as questões e o gabarito.
  - Em Forms → Configurações → **Transformar em teste** → mostrar a nota e as respostas certas depois do envio.
  - No Classroom, coloque **sem nota** (é só fixação).
- A **autoavaliação Índice Anti-Exaustão** de entrada fica no Módulo 0 e a de saída no Módulo 4, com as mesmas perguntas, para comparar.
  - Ative "coletar e-mails" para cruzar entrada e saída.
  - 🛑 Confirme com a Camila o texto de consentimento: "Suas respostas podem ser usadas, sem identificação, para melhorar o curso".

### 4.6 Assistente de IA
No tópico "Assistente de IA", crie um material com:
- o link do GPT ou Gem da Camila (Fase 6), ou os arquivos `base-conhecimento-metodo.md` e `biblioteca-prompts-por-aula.md`;
- o passo a passo para a aluna usar na própria conta.

### 4.7 Mural e convites
- **Mural**, aviso de boas-vindas:
  > Bem-vinda ao Método Lucro Anti-Exaustão®! 💛 Comece pelo Módulo 0, na aba Atividades. As aulas são curtas de propósito: assista, faça a ação do final e siga. Você não precisa fazer tudo de uma vez, só dar o próximo passo. — Camila
- **Pessoas → Convidar alunos:**
  - 🛑 Peça a lista de e-mails das mentoradas e mostre a lista antes de clicar em **Convidar**.

### 4.8 Teste como aluna
- 🛑 Peça um segundo e-mail da Camila. Convide esse e-mail e abra a turma numa janela anônima.
- Confira se todos os vídeos e PDFs abrem **sem pedir permissão**.
- Se algum pedir, ajuste o compartilhamento no Drive: "Qualquer pessoa com o link: Leitor", ou compartilhe com os e-mails das alunas.

✅ **Pronto quando:** a turma estiver completa, testada como aluna, com as avaliações funcionando e os convites aprovados pela Camila.

---

## 5. Kiwify (plataforma oficial: venda + acesso gratuito)

### 5.1 Conta (só a Camila)
🛑 A Camila cria e configura a conta. Você **não** preenche:
- conta em kiwify.com.br, com o e-mail profissional;
- CPF/CNPJ, dados bancários e documento;
- 2FA em Segurança.

Espere a aprovação da conta antes de seguir.

### 5.2 Produto
Em Produtos → Criar produto → Curso / Área de membros Kiwify:
- **Nome:** `Método Lucro Anti-Exaustão® – Alicerce`
- **Descrição curta e completa:** use `copy-divulgacao.md` §1, revisado pelo agente de vendas.
- **Preço:** R$ 497,00, pagamento único.
- **Garantia:** 7 dias.
- **E-mail de suporte:** 🛑 pergunte à Camila.
- **Imagem do produto:** 🛑 peça o upload. Sugestão: redimensionar no Canva a "Capa Notion - Fase 1" ou criar uma capa com a foto oficial.
- **Página de vendas:** deixe em branco por enquanto (preenche na Fase 7).
- 🛑 Mostre o resumo antes de salvar.

### 5.3 Área de membros
- **Nome:** `Lucro Anti-Exaustão®`
- **Mensagem de boas-vindas:** `copy-divulgacao.md` §1.
- **Ative:** comentários nas aulas, progresso, marcar como concluída e **certificado de conclusão**, se disponível.
  - Certificado: carga horária conforme a soma real das durações do `relatorio-videos.csv`, arredondada para cima; assinatura "Camila Martins Finger".
- **Prazo de acesso:** o valor de PRAZO_ACESSO.
- **Liberação dos módulos:** recomendado **imediata** para quem compra.
- **Capas dos módulos:** reaproveite os designs do Canva "Capa Notion - Fase 1 a 4", redimensionados para o tamanho que a Kiwify pedir na tela.
  - 🛑 O upload é da Camila. Confirme antes o tamanho exato na tela da Kiwify.

### 5.4 Módulos e aulas
Crie a estrutura conforme `mapa-aulas.csv`, com módulos M0 a M4 e mais **"Bônus e Materiais"** e **"Assistente de IA"**:
- Título da aula com 2 dígitos e descrição da seção 3 do guia.
- **Bloco "Ação da aula"** na descrição: a ação final que a aula pede, retirada do caderno de exercícios.
- **Materiais da aula:** PDF do caderno de exercícios no M0, e o link /copy da planilha da fase na primeira aula de cada módulo.
- **Vídeo:**
  - 🛑 A Camila arrasta o `.mp4` de `~/Alicerce/videos-final/<módulo>/` para cada aula. Você indica qual arquivo vai em qual aula, um por vez.
  - Depois, confira se todos processaram.
- **Avaliações:** se a Kiwify oferecer quiz ou questionário na aula, use `avaliacoes-por-modulo.md`. Se não oferecer, crie no Google Forms e coloque o link na última aula de cada módulo.
- **Não publique** módulos sem ok.

### 5.5 Checkout
- **Pagamento:** cartão em até 12x, Pix e boleto (vencimento 2 dias).
- **Campos:** nome, e-mail e WhatsApp.
- **Visual:**
  - banner 1200×400 (🛑 upload da Camila);
  - botão "Quero começar agora";
  - selo de garantia de 7 dias;
  - **sem** contador e **sem** notificações falsas de compra.
- **Depoimentos:** só reais e autorizados. Até lá, use a faixa de credenciais (+400 mentoradas · +2 mil mulheres impactadas).
- **Order bump e upsell:** siga `complementares/00-diagnostico-e-plano-10x.md`.
  - O produto do bump precisa existir na Kiwify antes.
  - 🛑 Confirme preços com a Camila.
- **Página de obrigado:** URL de `obrigado.html` hospedado (Fase 7).
- **Pixels:** Meta Pixel e GA4, 🛑 IDs com a Camila.

### 5.6 Acesso gratuito das mentoradas
- **Caminho oficial, custo R$ 0:** área de membros → **Alunos → Adicionar aluno**, uma por vez ou por importação, se houver.
  - 🛑 Peça a lista (nome e e-mail) e mostre antes de confirmar.
- Crie e mantenha a planilha **"Controle de Acessos – Alicerce"**: Nome | E-mail | Origem | Data | Validade | Status.
- Depois de liberar, envie o e-mail `emails/01-acesso-gratuito-mentorada.html` e a mensagem de WhatsApp de `copy-divulgacao.md`.
- **Cupom de 100% é opcional e só depois de testar:**
  - crie `MENTORADA2026` com 100%, uso limitado e validade;
  - 🛑 a Camila faz uma compra de teste;
  - confira se o checkout aceita R$ 0 e se há taxa;
  - se cobrar ou travar, desative e use só a liberação manual.

### 5.7 Cupons comerciais
Crie conforme o guia (§7.3) e `guerrilha/02-programa-indicacao.md` (cupons `INDICA-[NOME]`).
- 🛑 Mostre cada cupom antes de salvar.
- Nunca crie cupom de "último dia" sem prazo real.

### 5.8 Publicar e testar
1. 🛑 Com o ok da Camila, publique.
2. **Compra de teste real:** a Camila compra com o próprio cartão ou Pix e depois pede reembolso. Confira:
   - e-mail de acesso;
   - login;
   - vídeos;
   - PDFs;
   - Pixel (Meta Events Manager → Testar eventos);
   - página de obrigado.

✅ **Pronto quando:** o produto estiver publicado, a compra de teste aprovada, as mentoradas liberadas e a planilha de controle criada.

---

## 6. Kit de IA (assistente do método)

Use `complementares/ia/assistente-anti-exaustao-instrucoes.md`, que tem as instruções de sistema e o passo a passo de cada ferramenta.
- **ChatGPT (GPT personalizado):**
  - precisa de plano pago para **criar**;
  - Explorar GPTs → Criar → colar as instruções → subir `base-conhecimento-metodo.md` → definir os iniciadores de conversa a partir de `biblioteca-prompts-por-aula.md`;
  - compartilhar como "Qualquer pessoa com o link".
- **Claude (Projeto):** criar o Projeto → colar as instruções no campo do projeto → subir a base de conhecimento.
  - Compartilhar Projeto pode exigir plano de equipe. Se não der, entregue os arquivos para cada aluna criar o próprio projeto.
- **Gemini (Gem):** criar o Gem → instruções → arquivo de conhecimento.
  - Verifique se o compartilhamento está disponível no plano.
- 🛑 Teste os 3 com 3 perguntas reais da biblioteca de prompts e mostre as respostas à Camila antes de liberar.
- Coloque os links e o tutorial no módulo "Assistente de IA" da Kiwify e do Classroom.

✅ **Pronto quando:** pelo menos um assistente estiver publicado, testado e linkado nas plataformas.

---

## 7. Hospedar a landing page, a página de obrigado e o quiz

**Opção recomendada: Netlify Drop** (grátis, sem código).
1. Monte a pasta `~/Alicerce/site/`:
   ```
   site/
     index.html         <- publicar/landing-page.html
     obrigado.html      <- publicar/obrigado.html
     quiz/index.html    <- publicar/guerrilha/01-quiz-indice-exaustao.html
     img/               <- foto oficial, foto da enfermagem, fotos de eventos (otimizadas, até 300 KB cada)
   ```
2. Ajuste os caminhos de imagem no HTML para `img/...`.
3. Acesse app.netlify.com/drop. 🛑 A Camila cria a conta e faz login.
4. Arraste a pasta `site/`. Copie as URLs geradas e renomeie o site para algo como `metodo-lucro-anti-exaustao`.
5. Volte à Fase 3: preencha `LINK_LP`, `QUIZ_URL`, `LINK_OBRIGADO`, rode `aplicar-valores.py` de novo, remonte `site/` e publique outra vez (arrastar de novo atualiza).
6. Na Kiwify: cole a URL da LP em "Página de vendas" e a de obrigado na página pós-compra.
7. **Formulário do quiz:**
   - 🛑 pergunte onde guardar os leads (Google Forms, MailerLite, Brevo ou planilha);
   - configure `FORM_ACTION_URL` conforme o comentário no próprio HTML do quiz;
   - teste uma resposta real e veja se o lead chegou.
8. **Domínio próprio:** opcional, 🛑 decisão da Camila.

**Alternativa:** Canva Sites, recriando a LP no Canva com os mesmos textos. Use se a Camila preferir editar sozinha depois.

**Fotos:**
- **Story / enfermagem:** a foto "Camila como técnica de enfermagem" do Canva (design "TEMP - fotos Camila").
- **Eventos e prova social:** as fotos dos workshops e eventos.
  - 🛑 Pergunte se há autorização de uso de imagem das participantes para uso comercial. Sem autorização, use fotos em que ninguém seja identificável, ou só a Camila no palco.
- **Hero:** uma foto profissional recente, 🛑 escolha da Camila.
- Revise cada foto: resolução mínima de 1080 px no lado menor, sem marca d'água de terceiros, sem dados de clientes visíveis.

✅ **Pronto quando:** LP, obrigado e quiz estiverem no ar, com os links funcionando no celular e os leads do quiz chegando.

---

## 8. E-mails automáticos

- A Kiwify envia sozinha o e-mail de acesso. As sequências do kit precisam de uma ferramenta de e-mail.
  - 🛑 Pergunte qual a Camila prefere: **MailerLite** ou **Brevo** (ambas têm plano gratuito).
- **Integração Kiwify → ferramenta:** veja em Kiwify → Apps / Integrações se há integração nativa. Se não houver, use Zapier ou Make com o webhook "compra aprovada" e "carrinho abandonado".
- Monte as automações conforme a tabela de sequência do `README.md`:
  - boas-vindas;
  - D+3, D+7, D+14;
  - conclusão;
  - carrinho abandonado;
  - nutrição dos leads do quiz.
- Cole o HTML de cada arquivo `publicar/emails/*.html` no editor "HTML personalizado" da ferramenta e troque `{{NOME}}` pela variável de nome dela.
- **Envie um teste** de cada e-mail para a Camila e confira no Gmail do celular.
- 🛑 Ative as automações só depois do ok dela.

✅ **Pronto quando:** as automações estiverem ativas e os e-mails de teste conferidos no celular.

---

## 9. Canva: palestra e peças

A palestra **"Raio-X da Empresária Exausta"** já está no Canva da Camila, com 16 slides. O slide 3 tem a foto real e o slide 14 a prova social corrigida.
1. **Notas do apresentador:** a Camila decidiu **não** colocá-las no Canva. Elas ficam em `guerrilha/03-scripts-parcerias-e-palestra.md` (Parte 3). Não cole notas nos slides, a menos que ela peça.
2. Gere os **QR codes** em Apps → QR Code:
   - slide 15 aponta para a LP;
   - slide 16 aponta para o quiz.
   Teste com a câmera do celular.
3. **Slide 14:** use 3 cases curtos de `prova-social-e-autoridade.md` §4 (15 minutos por atendimento · meta por vendedor · preço de R$ 5 mil para R$ 8 mil), marcados como "caso real, nome preservado". Com autorização, inclua o primeiro nome.
4. Gere as capas da Kiwify (produto, módulos, banner do checkout) com **Redimensionar**, a partir das "Capas Notion - Fase 1 a 4" existentes.
5. 🛑 Mostre os slides finais à Camila antes de qualquer apresentação.

---

## 10. Revisão final e entrega

1. `python3 ferramentas/verificar-materiais.py --publicar`: zero problemas, exceto pendências autorizadas.
2. **Checklist de fumaça (no celular):**
   - LP → botão → checkout → compra de teste → obrigado → e-mail de acesso → área de membros → aula 1 toca → PDF abre → certificado configurado.
   - Quiz → captura → resultado → botão para a LP.
   - Classroom: aluna-teste vê tudo sem pedir permissão.
3. **Tom e marca:** leia a LP e os 3 primeiros e-mails em voz alta. Precisam soar como a Camila (frases-assinatura e "você", com "tu" só em stories).
4. Atualize `progresso.md` com:
   - links finais;
   - pendências;
   - decisões tomadas;
   - próximos passos do plano de guerrilha (`guerrilha/00-plano-guerrilha-90-dias.md`, semana 1).

---

## Modelo de `progresso.md`

```markdown
# Progresso — Alicerce
## Links finais
- LP:
- Checkout:
- Área de membros:
- Quiz:
- Classroom:
- Assistente de IA:
## Fases
- [ ] 1 Inventário   - [ ] 2 Vídeos   - [ ] 3 Valores   - [ ] 4 Classroom   - [ ] 5 Kiwify
- [ ] 6 IA           - [ ] 7 Hospedagem - [ ] 8 E-mails - [ ] 9 Canva       - [ ] 10 Revisão
## Decisões da Camila (data — decisão)
## Pendências (o quê — quem — até quando)
## Log (data/hora — ação — resultado)
```

---

## Prompt para começar (a Camila cola no Claude local)

```
Leia CLAUDE.md, RUNBOOK-CLAUDE-LOCAL.md e contexto-marca.md desta pasta.
Execute o runbook a partir da Fase 1, respeitando todas as regras de ouro e
parando em cada 🛑 para me perguntar. Crie e mantenha progresso.md.
Use o navegador embutido do app Claude (ou a extensão Claude in Chrome) para Kiwify, Classroom, Canva e Netlify.
```
