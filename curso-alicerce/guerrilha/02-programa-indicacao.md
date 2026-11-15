# Programa "Indique uma Empresária"
### Método Lucro Anti-Exaustão®

> **Para quem:** mais de 400 mentoradas (atuais e antigas), alunas do Alicerce, membros da Comunidade Impulso e embaixadoras.
> **Objetivo:** transformar quem já confia em você no canal de vendas mais barato e mais qualificado.
> **Princípio:** a indicação é um **favor para a amiga**, não um "esquema". A recompensa é um agradecimento e a transparência vem sempre em primeiro lugar.

---

## 1. Mecânica (simples de explicar em 1 frase)

> **"Indique uma empresária que precisa sair da exaustão: ela ganha [10%] de desconto no Alicerce e você ganha experiências comigo a cada indicação que virar aluna."**

| Elemento | Como funciona |
|---|---|
| **Cupom pessoal** | Cada indicadora recebe um cupom com o nome dela (ex.: `INDICA-ANA`, `INDICA-JULIA`) que dá [10%] de desconto (R$ 447,30) para a indicada. |
| **Alternativa sem cupom** | Para indicações de Comunidade, Consultoria ou PAD (vendas fora da Kiwify), a indicada diz "vim pela [nome]" na conversa, e a assistente registra na planilha. |
| **Quando conta** | A indicação conta quando a compra é aprovada **e passa dos 7 dias de garantia** sem reembolso. |
| **Validade** | O programa fica sempre ativo. As recompensas são revisadas a cada trimestre. |
| **Transparência** | A indicadora avisa a amiga que ganha um agradecimento seu (o script já faz isso). |

> **Por que cupom e não afiliação Kiwify para as alunas?** O cupom com nome é simples, a amiga recebe um benefício e o relatório de cupons da Kiwify mostra quem indicou. A afiliação com comissão em dinheiro fica para **parceiras profissionais** (contadoras, consultoras; tática 30 do plano).

---

## 2. Recompensas (alto valor percebido, baixo custo)

| Indicações que viraram alunas | Recompensa para a indicadora | Seu custo real |
|---|---|---|
| **1** | Áudio ou vídeo personalizado seu sobre o desafio atual dela + destaque nos stories (se ela quiser) | 10 min |
| **2** | **Hot seat de 20 min** comigo (online) | 20 min |
| **3** | 1 mês da Comunidade Impulso ou um almoço da comunidade por sua conta (escolha **uma**, conforme a sua estrutura) | R$ 97 ou o almoço |
| **5** | **Sessão estratégica individual de 60 min** + título de **Embaixadora Anti-Exaustão** | 60 min |
| **Indicação para Comunidade, Consultoria ou PAD** | Uma recompensa definida por você para cada caso (ex.: sessão de 60 min ou condição especial na renovação dela) | [definir] |

> **Recompensa para quem foi indicada:** [10%] de desconto no Alicerce + "chegou por indicação", ou seja, você manda uma mensagem pessoal de boas-vindas citando quem indicou.

> **Não use** dinheiro vivo para alunas: isso muda a relação. Experiências com você valem mais e fortalecem a comunidade.

---

## 3. Configuração na Kiwify (passo a passo)

1. **Produtos → Método Lucro Anti-Exaustão® – Alicerce → Cupons → Novo cupom.**
2. **Código:** `INDICA-[PRIMEIRONOME]` (sem acento, em maiúsculas). Se houver nomes repetidos, use `INDICA-ANA-S` / `INDICA-ANA-R`.
3. **Desconto:** percentual de [10%].
4. **Limite de uso:** sem limite (ou 20 usos, para revisar depois).
5. **Validade:** 6 meses (renovável).
6. Repita para cada indicadora. **Com a extensão do Chrome**, cole este prompt:

```
Na Kiwify, no produto "Método Lucro Anti-Exaustão® – Alicerce", vá em Cupons e crie,
um por vez, os cupons abaixo: tipo percentual, desconto 10%, sem limite de usos,
validade até [DATA]. Me mostre cada um antes de salvar.
INDICA-ANA
INDICA-JULIA
INDICA-[...]
```

7. **Link pronto com cupom:** se a Kiwify aceitar o cupom na URL do checkout, gere um link por indicadora (ex.: `LINK_CHECKOUT?coupon=INDICA-ANA`, **confirme o parâmetro exato na Kiwify**) e acrescente `&utm_source=indicacao&utm_content=ana`.
8. **Relatório:** uma vez por semana, a assistente abre **Vendas → filtrar por cupom** e atualiza a planilha.

---

## 4. Planilha de controle: "Indicações Anti-Exaustão"

**Aba 1: Indicadoras**

| Nome | WhatsApp | Origem (Mentoria/Comunidade/Alicerce/PAD) | Cupom | Link com cupom | Data de entrada no programa | Indicações válidas | Recompensas entregues | Próxima recompensa | Embaixadora? |
|---|---|---|---|---|---|---|---|---|---|

**Aba 2: Indicações**

| Data | Indicadora | Nome da indicada | Produto | Cupom/Origem | Valor | Data fim da garantia | Válida? (S/N) | Recompensa liberada? | Obs. |
|---|---|---|---|---|---|---|---|---|---|

**Fórmulas úteis (Google Planilhas):**
- `Data fim da garantia` = `=A2+7`
- `Indicações válidas` (aba 1) = `=CONT.SES('Indicações'!B:B; A2; 'Indicações'!H:H; "S")`
- `Próxima recompensa` = `=SE(G2>=5;"Sessão 60 min + Embaixadora";SE(G2>=3;"Comunidade/almoço";SE(G2>=2;"Hot seat 20 min";SE(G2>=1;"Áudio/vídeo + destaque";"—"))))`

**Rotina da assistente (sexta-feira, 20 min):**
1. Puxar as vendas com cupom `INDICA-` na Kiwify.
2. Marcar como válidas as que passaram dos 7 dias.
3. Avisar a Camila das recompensas a entregar.
4. Mandar a mensagem de agradecimento (script 5.4).

---

## 5. Scripts de WhatsApp

### 5.1 Convite para a mentorada entrar no programa (enviado por você)
> Oi, [NOME]! 💛 Tô criando algo especial para as minhas mentoradas e lembrei de você na hora.
> Sabe aquela amiga, sócia, irmã ou cliente que é empresária e vive dizendo "se eu não fizer, ninguém faz"? Agora você pode presentear ela com **[10%] de desconto** no curso do Método Lucro Anti-Exaustão®, com o seu cupom pessoal: **INDICA-[NOME]**.
> E a cada indicação que virar aluna, eu te agradeço com experiências comigo: áudio personalizado, hot seat, sessão estratégica…
> Posso te mandar o seu link pronto para encaminhar?

### 5.2 Mensagem pronta para a mentorada encaminhar (transparente)
> Amiga, lembrei de você! Eu fiz a mentoria com a Camila Martins e ela organizou a minha rotina de um jeito que eu não imaginava. Ela tem um curso com o método inteiro, o Lucro Anti-Exaustão®, e com o meu cupom **INDICA-[NOME]** você ganha [10%] de desconto. (Sendo sincera: se você entrar, eu ganho uma sessão com ela 😅)
> Se quiser ver antes se faz sentido, tem um teste de 2 minutos que mostra o quanto a empresa depende de você: [LINK_QUIZ?utm_source=indicacao&utm_content=NOME]
> Página do curso: [LINK_LP]

**Versão curta (para stories ou Status):**
> Se a sua empresa para quando você para, faz esse teste de 2 min 👇 Se quiser o curso da Camila, usa o meu cupom INDICA-[NOME] 💛

### 5.3 Para a aluna do Alicerce, depois de concluir a Fase 1 (gatilho: progresso)
> [NOME], vi que você terminou o Raio-X Operacional! 🎉 Como foi enxergar os seus gargalos?
> Se você conhece outra empresária que precisa desse choque de clareza, agora você tem um cupom pessoal: **INDICA-[NOME]**, com [10%] para ela e experiências comigo para você a cada indicação. Quer o link pronto?

### 5.4 Agradecimento quando a indicação é validada
> [NOME]!!! A [INDICADA] entrou no método por sua causa 💛 Obrigada pela confiança de me indicar para alguém que você gosta.
> Isso te dá direito a: **[RECOMPENSA]**. Me fala o melhor dia e horário?
> (Você está com [X] indicação(ões); com [Y] você desbloqueia [PRÓXIMA RECOMPENSA].)

### 5.5 Boas-vindas para a indicada (você manda pessoalmente)
> Oi, [INDICADA]! Aqui é a Camila 💛 A [INDICADORA] me contou que te indicou, e eu fiquei muito feliz. Ela é uma das mulheres que mais me inspiram.
> Comece pelo Módulo 0 e, quando terminar a Aula 6 (Roda da Vida), me manda uma mensagem contando a sua nota mais baixa. Eu quero acompanhar você.

### 5.6 Lembrete trimestral (para indicadoras ativas)
> Oi, [NOME]! Passando para lembrar que o seu cupom **INDICA-[NOME]** continua ativo 💛 Se surgir alguma amiga empresária na sua vida reclamando que "não dá conta", já sabe. Obrigada por espalhar o movimento #EmpresaSemExaustão!

---

## 6. Momentos ideais para pedir indicação

1. **Logo depois de uma vitória da aluna:** fim de fase, delegou a primeira tarefa, tirou um dia de folga.
2. **No fim da mentoria ou do curso:** no e-mail de conclusão e na última sessão.
3. **No almoço da comunidade:** "Na próxima, traga uma empresária que precisa ouvir isso."
4. **Datas de presente:** Natal, Dia Internacional da Mulher (8/3) e Dia do Empreendedorismo Feminino (19/11).
5. **Depois de um depoimento autorizado:** "Obrigada por compartilhar! Quer o seu cupom para indicar?"

---

## 7. Divulgação do programa (lançamento)

- **Semana 2 do plano:** bilhetes para as mais de 400 mentoradas (tática 24), com o convite 5.1.
- **Grupo da Comunidade:** post fixado com a explicação e a tabela de recompensas.
- **Área de membros (Kiwify):** um card ou aula "🎁 Indique uma empresária" no fim do Módulo 4, com o texto 5.3.
- **E-mail 06 (conclusão):** incluir o P.S. de indicação (ver arquivo 05).
- **Ranking (opcional, só com consentimento):** "Embaixadoras do mês" nos stories, sem expor números de venda.

---

## 8. Cuidados
- **LGPD:** nunca peça à mentorada a lista de contatos dela. Ela mesma envia a mensagem.
- **Transparência:** a indicadora deve dizer à amiga que ganha um agradecimento. O script 5.2 já faz isso.
- **Sem pressão:** "não tenho ninguém para indicar" é uma resposta 100% ok.
- **Recompensa só depois da garantia:** isso evita indicação de fachada.
- **Revisão trimestral:** veja quais recompensas foram mais desejadas e ajuste.
