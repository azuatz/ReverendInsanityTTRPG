---
tags:
  - regra
  - inimigo
  - fechado
aliases:
  - Ameaças Genéricas por Rank
escopo: sistema
---

# ⚔️ Ameaças Genéricas por Rank

Estatísticas prontas de inimigo, escaladas pela mesma tabela de M do rank que os personagens usam (ver [[⚔️ Combate|Combate]]). Os números por molde valem pra qualquer tamanho de mesa; o que muda com o número de jogadores é **quantos inimigos por cena** — ver a tabela de composição mais abaixo.

## Os três moldes

> **Todo inimigo tem estágio igual ao do grupo**, salvo quando você quiser o contrário: some `+Grau por dado` no dano dele e `+4 × M × Grau` na Vitalidade, exatamente como um PJ. Sem isso, a mesa atropela o bestiário a partir do estágio Médio.

| Molde | Papel | Vitalidade | Defesa | **Acerto** | RD | Dano por ataque | Quantos por cena (rank igual, mesa de 4) |
|---|---|---|---|---|---|---|---|
| **Recruta** *(só dentro de uma Horda)* | Bucha de canhão, ameaça em número | `6 × M(rank)` | `10 + rank` | **`d20 + rank + 4`** | — | `M d6` | 6 a 8 |
| **Guerreiro** | Oponente individual padrão | `12 × M(rank)` | `12 + rank` | **`d20 + rank + 6`** | `1 × M` | `M d8` | 2 a 3 |
| **Elite** | Rival nomeado, luta de verdade | `21 × M(rank)` | `14 + rank` | **`d20 + rank + 8`** | `2 × M` | `M d10`, costuma ter 1 Golpe Matador próprio | 1 a 2 |

> **Recruta solto é decorativo.** Um personagem do mesmo rank mata um Recruta por golpe, então seis Recrutas soltos são seis ações que nunca acontecem — medido, 100% de vitória e 4 de 4 personagens de pé em todo rank. **Use Recruta só dentro de uma Horda.** Os três moldes continuam aqui porque servem para montar cena sob medida, mas Guerreiro e Elite só ameaçam com a Ação Especial ligada, e Recruta só em bloco.

**A coluna de Acerto não é decorativa — sem ela a ficha não roda.** Ela é a mesma fórmula do jogador (`d20 + atributo + (rank + 2) + rank do Gu`) já resolvida: um Guerreiro de rank 3 acerta com `d20 + 9`, que contra a Defesa 15 de um PJ do mesmo rank é 75%, e contra a Defesa 19 de quem carrega um Gu de movimento é 55%. É a taxa que [[⚔️ Combate|Combate]] promete.

Dano de inimigo usa o mesmo **pool de dados** dos jogadores (ver [[⚔️ Combate|Combate]]): `M` dados do tipo do Caminho dele, mais `M × Grau` se ele tiver estágio. Um Elite com um Gu de Força ativo sobe o **tipo do dado**, exatamente como um PJ faria.

## 🪓 Ação Especial — todo Guerreiro e Elite tem uma

**Uma por inimigo, uma vez por cena.** Um ataque com **+4 no acerto** que também aplica **Lentidão 2**. Não muda nenhuma estatística do molde e é o que separa um inimigo de um saco de pancada, porque **tirar a ação de um personagem vale mais que tirar Vitalidade dele**.

Descreva-a como um Gu: o Batedor solta o Gu do Nevoeiro Cego, a Fera-Gu dá a investida que derruba. O mestre anuncia quando usa — a especial gasta, e o grupo precisa saber que já foi.

## 👥 A Horda — recrutas como uma unidade só

Recrutas individuais **morrem antes de agir**: um personagem do mesmo rank mata um por golpe, e a economia de ação deles nunca acontece. Testado, 6 Recrutas terminam com os quatro personagens de pé em todo rank. A correção é parar de tratá-los como fichas separadas.

| A Horda | |
|---|---|
| **Vitalidade** | `6 × M × (nº de membros)`, somada numa barra só |
| **Defesa** | `10 + rank` |
| **Acerto** | `d20 + rank + 6` — o `+2` é o cerco |
| **Ataques por rodada** | **Um por personagem de pé — com piso de 2 contra dois alvos e 3 contra um alvo só.** Não é iniciativa individual, é estar cercado |
| **Dano** | `M d6`, **e o dado sobe um tipo a cada 4 membros vivos acima dos 4 primeiros**: 4 a 7 membros `M d6` · 8 a 11 `M d8` · 12 a 15 `M d10` · 16 ou mais `M d12` (teto) |

Uma horda de 8 bate em **`M d8`**; uma de 12, em **`M d10`**. Conforme perde Vitalidade, perde membros, e **o dado desce sozinho** — o grupo sente a horda enfraquecendo sem ninguém precisar contar corpos.

**O piso existe porque oito feras cercando uma pessoa devem assustar, não cansar.** Sem ele, a nona rodada de simulação mediu a horda contra um alvo solitário virando guerra de atrito de 10 a 19 rodadas — um ataque por rodada contra uma parede de Vitalidade dimensionada para quatro. Com o piso, o cerco volta a ser cerco — e é bom saber o tamanho dele, medido na décima quarta rodada: **uma Horda de 8 derruba um personagem sozinho em ~5 rodadas, com 0-37% de chance de vitória solo** (a maioria dos perfis fica em ~0%). Oito feras contra um não é uma cena de vitória, é fuga ou resgate; se a mesa quiser uma caçada solo *jogável*, use uma matilha menor (uma Horda de 2-3) — dimensionar a Horda pra mesa é a mesma lógica da linha "com 3 jogadores" mais abaixo.

> [!warning] Horda contra UM personagem é cena de fuga, não encontro
> Com o piso, a matilha executa: medido, um PJ sozinho contra uma Horda de 8 vence **0-37% das vezes** (dez de doze células abaixo de 1%) em cerca de 5 rodadas. É o desenho funcionando — a Horda é ameaça de cerco, e cerco contra uma pessoa só é como cerco deve ser. **Não existe configuração que faça essa cena durar** e continuar ganhável: as variantes medidas (Horda de 2, de 3, Vitalidade escalada pela mesa) devolvem cenas de 3-4 rodadas. Se um personagem se separar do grupo e a matilha o encontrar, o jogo ali é [[🏃 Fuga e Perseguição|fugir]] — e a mesa deve saber disso antes de se separar.

**Área é a resposta.** Um Gu de área contra uma horda tira Vitalidade da barra inteira; é a única situação do jogo em que dano em área supera dano concentrado, e é o que faz esses Gu valerem uma vaga na Abertura.

## 🐺 Feras — três traços, cole em qualquer molde

O Grimório não tem uma criatura sequer porque não precisa: uma fera é qualquer molde acima (Recruta, Guerreiro, Elite, Horda) com estes três traços colados por cima. Nada de bestiário separado pra manter.

| Traço | O que muda |
|---|---|
| **Instinto** | Não negocia, não se intimida, não é enganado por blefe verbal — mata de saída qualquer via social. Detectar a real intenção dela (fugir, caçar, defender ninhada) é teste de AST, não de CAR |
| **Sentidos** | Vantagem pra detectar movimento, cheiro e essência. Emboscar uma fera custa 1 grau de dificuldade a mais que emboscar gente do mesmo rank |
| **Sem Abertura** | Não tem Gu, não usa Golpe Matador, não dá Essência pra drenar nem receita pra saquear. Ação sem Ação Especial e sem dano de Alma conta como **ação comum** no [[#O contador que importa de verdade ações inimigas por rodada\|contador ponderado]] — uma fera vale menos ação por rodada que um Mestre de Gu do mesmo rank |

Uma matilha revezando pra desgastar um alvo mais forte é só uma **Horda com Instinto e Sentidos** — nenhuma regra nova.

### Maré de feras — o evento de abertura de arco

Três ondas, com a Horda que já existe:

1. **Batedores** — Horda de 4 (`M d6`), Instinto + Sentidos. Só testam a defesa.
2. **O bando** — Horda de 8 a 12 (`M d8`–`M d10`), Instinto + Sentidos. A onda de verdade.
3. **O que as trouxe** — um Elite ou Chefe com Instinto + Sentidos comandando à distância (nunca no meio da matilha) — é o gancho que sobra pra depois: por que as feras vieram pra cá?

**Maré grande de verdade** — centenas ou milhares de feras sob um Rei de Cem/Mil/Miríade de Feras, com a regra de ondas e a resolução abstrata pra não rodar tudo turno a turno: [[🐺 Reis Fera e a Maré]].

## 🧑‍🦱 Mestre de Gu — o inimigo humano

O molde mais útil do conjunto, porque é o que o cenário produz o tempo todo: um cultivador rival, não uma fera com números. **É a ameaça padrão de uma cena entre pessoas.**

| Mestre de Gu | |
|---|---|
| **Vitalidade** | `21 × M` |
| **Alma** | `15 × M` |
| **Defesa** | `13 + rank` |
| **RD** | `1 × M` — um Gu de defesa sustentado |
| **Acerto** | `d20 + rank + 7` |
| **Ações** | **2 por rodada** |
| **Ataque** | Gu de ataque do próprio rank — **`M d8`** |
| **Ação Especial** | Gu do **próprio Caminho**: **+4 no acerto**, **`M d10`**, e aplica Lentidão 2 |

**A Ação Especial é o que separa o molde de um saco de pancada** — e a versão acima, medida, é a mais perigosa quando aparece sozinha: o +4 quase garante o acerto (e com ele a Lentidão), e o dano soma na mesma Vitalidade que o resto da cena já está batendo. Um Mestre de Gu com 2 ações e uma especial ameaça de verdade com **metade da Vitalidade de um Chefe**.

**A exceção rara — o cultivador do Caminho da Alma.** Inimigo com poder de Alma é raro: a maioria dos Mestres de Gu inimigos é de outros Caminhos. Ao montar a cena, **role 1d6 por Mestre de Gu — só em 6 ele é um cultivador de Alma de verdade**, e a Ação Especial dele vira **`M d12`, ignora RD por completo e mira a barra de Alma** (mantendo a Lentidão 2). Sozinho, esse golpe abre uma barra que nada mais na cena vai tocar; **várias especiais de Alma juntas, empilhadas na mesma barra, são um alfa-strike** — por isso "todos de Alma" é ferramenta de Clímax, nunca composição casual (ver a tabela de composição de cena mais abaixo).

**Como variar sem refazer a ficha:** troque o Caminho da especial. Vento vira reposicionamento que quebra o cerco do grupo; Força vira o melee de `M d10` do molde; Sabedoria vira o inimigo que age primeiro toda rodada. A estrutura (`21 × M`, 2 ações, uma especial) não muda — e a tabela de composição de cena mais abaixo já assume especiais de Caminhos variados, com o cultivador de Alma entrando só pela exceção rolada de 1d6.

**Ele também tem os limites de um cultivador**, e usá-los é o que torna a luta interessante: a Essência dele acaba, os Gu dele podem ser roubados depois, e ele tem um Golpe Matador com **Brecha** que o grupo pode ter descoberto antes da cena.

### 🎒 O que ele carrega — loadout em três rolagens

Todo Mestre de Gu morto, rendido ou extorquido tem uma bagagem, e ela é o motivo de rendição valer mais que execução (ver [[⚰️ Espólio]]). Role na hora, só quando importar:

```
Gu carregados = rank + 1d3          (metade do rank dele, resto 1 abaixo)
Papéis: 1 ataque · 1 defesa ou movimento · o resto utilidade/investigação
Receita: role 1d6 → em 5-6, ele sabe UMA receita de valor
         (em 6, ela é rara — sorteie no [[📜 Livro de Receitas de Gu]])
```

Escolha os Gu concretos no [[📖 Catálogo de Gu]] pelo Caminho que a especial dele já declarou — ou deixe genérico ("um Gu de fuga, dois de utilidade") até alguém perguntar. **A receita não está escrita num papel no bolso**: está na cabeça dele, e é isso que faz um Mestre de Gu capturado valer uma cena de interrogatório ou barganha em vez de um saque.

## O Chefe — a regra especial pra combate solo

Um único inimigo contra um grupo perde a ação por turno na maioria dos sistemas — 3 ou 4 personagens agem, ele age uma vez, e a luta acaba rápido demais pra ser memorável. Pra qualquer inimigo que a cena trata como **Chefe** (rival de arco, vilão de sessão):

1. **Vitalidade — o multiplicador vem da tabela abaixo**, junto com as ações. Não é um número só: vai de `63 × M` no rank 1 a `80 × M` no rank 5.
2. **Age várias vezes por rodada, e o número vem da tabela abaixo** — não é fixo.
3. **Ignora a primeira Condição de controle** que sofrer em cada cena (atordoamento, lentidão, medo) — descreva como ele resiste, não como ela simplesmente falha.
4. Tem pelo menos **um Golpe Matador** e **um Gu de defesa sustentado** — um chefe sem defesa própria morre rápido demais quando o grupo foca fogo nele.

### Vitalidade e ações do Chefe, por rank

| Rank do Chefe | Vitalidade | Ações por rodada | Vitória do grupo *(mesa de 4, com 1 Guerreiro de apoio)* | Duração |
|---|---|---|---|---|
| **1** | `63 × M` | **2** | **70%** | 7,2 rodadas |
| **2** | `72 × M` | **2** | **78%** | 7,9 |
| **3** | `78 × M` | **2** | **84%** | 8,8 |
| **4** | `72 × M` | **3** | **78%** | 7,5 |
| **5** | `80 × M` | **3** | **87%** | 7,4 |
| **6+** | `63 × M` | **4** | ver a régua ΔB dos imortais, mais abaixo | — |

**As cinco células caem dentro da faixa de 56-87% que "Clímax" promete**, e a cena dura 7,2 a 8,8 rodadas — o ritmo de 6-8 da decisão 208, com o rank 3 estourando 0,8 rodada. *(Vigésima segunda e vigésima terceira rodadas, decisões 249 e 250. O rank 6+ segue em `63 × M` de propósito: a fase imortal é dimensionada pela régua ΔB, não por esta tabela.)*

> [!danger] 🔴 Estes números foram corrigidos na décima oitava rodada, e o Chefe deixou de ameaçar
> A tabela publicava **3 / 54 / 87 / 75 / 90%**; remedida com o motor consertado, ela dá **28 / 96 / >99 / 98 / >99%** *(faixa entre os três dials de ficha: 17-38 · 90-98 · 98-100 · 96-99 · 99-100)*. A causa não é o Chefe — é que dezessete rodadas de simulação rodaram com **três dos quatro PJs sem os Níveis de Potência que as fichas deles concedem** (ver [[🎯 Simulação de Combate — Resultados#🔧 Décima oitava rodada — os três consertos de motor e a revalidação (2026-09-01)|a décima oitava rodada]]). Com o grupo modelado inteiro, **um Chefe do rank do grupo não é mais um clímax do rank 2 em diante.**
>
> **✅ Resolvido para o molde Chefe (decisão 250).** O autor escolheu a alavanca da Vitalidade, ela foi medida, e o `94 × M` uniforme que se propunha **foi rejeitado por medição**: ele derruba a vitória *abaixo* do piso de 56% nos ranks 1, 2 e 4 e estoura o teto de 8 rodadas em todos os cinco. A escada aplicada é `63/72/78/72/80 × M`, e o rank 1 trocou quatro ações por duas — ver a tabela de Vitalidade e ações acima. As outras quatro composições **não se moveram uma casa decimal** na revalidação, o que era o controle da rodada.
>
> **✅ Revalidado pela décima nona rodada (decisão 242), com o Golpe Matador finalmente disparando.** A suspeita registrada era que o Chefe só parecia fácil porque o combo nunca entrava na cena que foi construída em torno dele. **Medido: os dois problemas são independentes.** Com a regra da decisão 240 e o gatilho contado por ação, o combo dispara e a tabela acima anda **−0,6 / 0,0 / −0,4 / −0,7 / −1,7 pontos percentuais**. **O molde do Chefe fica intocado por decisão do autor**, e o número que vai dimensioná-lo agora está livre da variável do combo.
>
> **✅✅ Revalidado outra vez pela vigésima rodada (decisão 246), agora com o portão de rank 3, a Abertura do disparo e o pool dobrado ligados** — e o veredito ficou **mais forte, não mais fraco**. Com todas as regras vivas o Clímax mede **99,3 / 98,5 / 96,8%** nos ranks 3/4/5: o rank 5 anda **+1,4pp na direção errada**. **Um Golpe Matador mais forte torna a cena de Chefe mais difícil para o GRUPO, não para o Chefe** — porque disparar custa o arsenal, e o grupo que dispara sempre perde 14 pontos de vitória em média. **O Golpe Matador não segura a cena de Chefe em nenhuma versão da regra; o reforço do Chefe tem de vir do Chefe.**

> [!success] ✅ O Chefe de rank 1 deixou de ser a exceção — e a causa não era falta de calibragem
> Ele media **17-28%**, de longe a célula mais dura da tabela inteira e a única abaixo da faixa que "Clímax" promete. **A causa era um número fora da escada:** o Chefe de rank 1 tinha **quatro** ações por rodada, enquanto os ranks 2-3 têm duas e os 4-5 têm três — subia e voltava a descer. Com **duas ações e a Vitalidade publicada intacta**, ele mede **70,3% de vitória em 7,22 rodadas**, o centro dos dois alvos, sem tocar em nenhuma outra alavanca.
>
> Com isso, **a variante "1 Elite + 3 Mestres" deixa de ser a recomendação para o clímax de rank 1** e volta a ser só uma alternativa de sabor. *(Decisão 250. A rejeição da alavanca de ações registrada nas decisões 137 e 209 é sobre **somar** ações; subtrair do rank 1 é o movimento oposto, e aquelas rodadas não o mediram.)*

**Por que não é uma escala limpa.** *(Justificativa revista pela décima nona rodada.)* A explicação antiga dizia que a dificuldade do Chefe era governada por **quantos Golpes Matadores o grupo consegue pagar naquele rank**. **A medição refuta isso — mas não pelo motivo que a décima oitava publicou.** Aquela rodada tinha concluído que o combo *"não compensa contra Chefe publicado nenhum, porque a essência que ele custa compra 16 a 40 ataques comuns"*; **essa conclusão foi retirada** (decisão 242): ela era artefato da métrica do gatilho, não propriedade do sistema. Remedido com a regra da decisão 240 e o custo-benefício contado **por ação**, o combo **dispara** — até 3,21 vezes por cena de Clímax no rank 5 — e a vitória do grupo cai de 99,7% para apenas **95,4%**. **O Golpe Matador não é o que governa a escala do Chefe, nem quando dispara.** O que governa é o **volume de ações contra o arsenal do grupo** — e a vigésima segunda rodada fechou a prova disso pela outra ponta: o rank 1 era a célula mais dura do jogo **por causa das quatro ações**, e devolvê-lo a duas o levou de 17% a 70% de vitória sem mexer em mais nada. A escada de ações é o botão real da dificuldade do Chefe; a Vitalidade é o botão do **ritmo**.

**Onde isso cai, medido:** contra uma mesa de 4 do mesmo rank, um Chefe com a Vitalidade e as ações da tabela acima mais um Guerreiro de apoio é uma luta de **7,2 a 8,8 rodadas**, com o grupo vencendo em **70 a 87%** das vezes — dentro da faixa em todos os cinco ranks. *(Antes da recalibragem eram 4,7-6,8 rodadas e 88-97% de vitória do rank 2 em diante, o que já não era alvo de clímax de arco.)* Se ainda quiser apertar uma cena específica, **suba a Vitalidade** em vez de subir o rank do Chefe: alonga a luta sem dobrar o dano que entra no grupo. Subir o rank é TPK medido, e a nota o proíbe.

## Referência rápida por rank (M já aplicado)

| Rank | M | Recruta VIT | Guerreiro VIT | **Mestre de Gu VIT** | Elite VIT | Chefe VIT | **Horda de 8 VIT** |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 6 | 12 | **21** | 21 | 63 | **48** |
| 2 | 2 | 12 | 24 | **42** | 42 | 126 | **96** |
| 3 | 4 | 24 | 48 | **84** | 84 | 252 | **192** |
| 4 | 8 | 48 | 96 | **168** | 168 | 504 | **384** |
| 5 | 16 | 96 | 192 | **336** | 336 | 1.008 | **768** |

A Horda usa `6 × M × nº de membros` — a coluna acima é o caso de 8. O Mestre de Gu tem a mesma Vitalidade de um Elite, e a diferença entre os dois está nas **duas ações** e na Ação Especial própria.

## Como montar uma cena de combate

Os números entre parênteses são a **vitória medida do grupo** numa mesa de 4, pela [[🎯 Simulação de Combate — Resultados\|simulação]]. A maioria das composições vale em qualquer rank; **"Difícil" é a exceção — muda de composição por faixa de rank**, como o Chefe (abaixo) já muda de número de ações. A causa é a mesma nos dois casos — **volume bruto de ações contra o arsenal do grupo** (ver o achado na quinta rodada de simulação) —, e a lição é que nem toda composição escala limpo do rank 1 ao 5. *(A explicação anterior atribuía a escala do Chefe ao "custo relativo do Golpe Matador"; a décima nona rodada mediu o combo disparando e mostrou que ele move menos de 5pp em qualquer célula de Chefe — decisão 242.)*

| Tipo de cena | **rank 1** | **rank 2** | **rank 3** | **rank 5** |
|---|---|---|---|---|
| **Fácil** | Horda de 8 *(100%)* | Horda de 8 *(100%)* | Horda de 8 *(100%)* | Horda de 8 *(100%)* |
| **Padrão** | **2 Mestres + 1 Guerreiro** *(99%)* | 3 Mestres de Gu *(97%)* | idem *(99%)* | idem *(100%)* |
| **Padrão pesado** | 2 Mestres + Horda de 8 *(89%)* | idem *(91%)* | idem *(91%)* | idem *(99%)* |
| **Difícil** | 3 Mestres + 1 Guerreiro *(70%)* | idem *(83%)* | idem *(88%)* | 4 Mestres *(86%)* |
| **Clímax** | 1 Elite especial + 3 Mestres *(68%)*✝, ou **Chefe + Guerreiro *(70%)*** | idem, **Chefe + Guerreiro *(78%)*** | 1 Elite especial + 3 Mestres *(44%)*✝, ou **Chefe + Guerreiro *(84%)*** | 1 Elite especial + 3 Mestres *(46%)*✝, ou **Chefe + Guerreiro *(87%)*** |

*(✝ não retestado desde a terceira rodada — e sob a regra de Alma rara os 3 Mestres dessa variante também mudam de especial, então o número está duplamente desatualizado.)*

> [!danger] 🔴 Tabela corrigida na décima oitava rodada — e a escada de dificuldade colapsou (2026-09-01)
> Dezessete rodadas de simulação rodaram com **três dos quatro PJs sem os Níveis de Potência que as fichas deles concedem** — só a Lee recebia a escada do Wu Xing, enquanto Jiāotáng (Caminho da Força), Xie Lang (Fase da Lua) e Demvi (Corrente + Altitude do Vento) rodavam com zero. Com os quatro modelados, **8 das 16 células acima mudaram** e três das cinco composições saíram da faixa que prometem.
>
> **A faixa entre os três dials de ficha** (as escadas de Lua, Vento e Wu Xing dependem de fase, posição e terreno — o número da tabela é a leitura de **cena ordinária**, e a faixa vai do dial zerado ao teto):
>
> | Composição | faixa que a nota promete | rank 1 | rank 2 | rank 3 | rank 5 |
> |---|---|---|---|---|---|
> | Fácil | ≈100% | 100 | 100 | 100 | 100 |
> | Padrão | 75-99% | 98-99 | 94-99 | 97-99 | 100 |
> | **Padrão pesado** | **53-77%** | **83-91** | **83-94** | **85-95** | **97-99** |
> | **Difícil** | **~40-52%** | **59-78** | **68-90** | **80-94** | **79-95** |
> | **Clímax** *(Chefe + Guerreiro)* | **56-87%** | **70** ✅ | **78** ✅ | **84** ✅ | **87** ✅ |
>
> *(A linha do Clímax foi **recalibrada e revalidada** pela vigésima terceira rodada — decisão 250. As quatro linhas acima dela seguem como a décima oitava as mediu: são as que ainda esperam redesenho de peças.)*
>
> **O que NÃO foi feito:** redesenhar as composições para voltarem às faixas — **as quatro acima do Clímax**, que é a única já resolvida (decisão 250). Isso é decisão de design do autor, não conserto de motor, e a alavanca dessas quatro é o **número de peças**, não o molde. *(A alavanca "Chefe de `94 × M`" que esta nota sugeria está **rejeitada por medição** — ver a tabela de Vitalidade e ações do Chefe.)* Detalhe e método em [[🎯 Simulação de Combate — Resultados#🔧 Décima oitava rodada — os três consertos de motor e a revalidação (2026-09-01)|a décima oitava rodada]].
>
> **✅ Revalidada pela décima nona rodada** ([[🎯 Simulação de Combate — Resultados#🎯 Décima nona rodada — o Golpe Matador medido por ação (2026-09-01)|2026-09-01]], decisão 242): com o Golpe Matador disparando pela primeira vez, **nenhuma das quinze células anda mais de 3pp**. A tabela acima segue valendo.

> [!success] Tabela revalidada em conjunto — décima terceira rodada (2026-08-31)
> As 20 células publicadas acima foram remedidas de uma vez só, com todas as regras de hoje ligadas ao mesmo tempo (3.000 iterações/célula). **Dezenove conferem dentro de 3 pontos percentuais**; a única que se moveu foi **Difícil de rank 2 (35% → 31%)**, corrigida acima. As faixas de duração também conferem. Ver [[🎯 Simulação de Combate — Resultados#✅ Décima terceira rodada — validação final conjunta (2026-08-31)|a décima terceira rodada]]. *(Registro histórico: os números que esta caixa validou foram substituídos pela décima oitava rodada, acima.)*

> [!success] Resolvido — a tabela acima está certa como está *(decisão 215)*
> A décima terceira rodada descobriu que o motor de simulação sempre modelou `treino = 0` no acerto, enquanto [[💪 Atributos]] trazia `+ treino` na fórmula. O autor decidiu: **ataque não é ação treinada** — o bônus de treino vale só em teste de perícia, nunca em rolagem de ataque. A fórmula de Atributos foi corrigida para refletir isso, e **a premissa segue válida**: `treino = 0` continua sendo o que todas as rodadas medem, inclusive a décima oitava. *(A alternativa — ligar treino só nos PJs — moveria esta tabela +12,6 pontos percentuais em média, até +30,9.)* ⚠️ **O que caducou é a frase "os números acima seguem válidos sem nenhuma republicação":** eles foram republicados pela décima oitava rodada, por causa da paridade de Níveis de ficha — nada a ver com treino.

**A linha de "Padrão pesado" caiu 8-13 pontos porque o piso de ataques da Horda a endurece** — os 71/64/63/85 anteriores eram medição feita **antes** do piso, e os 63/57/50/76 vieram da décima primeira rodada. *(Os dois conjuntos são históricos: a décima oitava rodada, com os quatro PJs modelados, mede 89/91/91/99% — ver a caixa 🔴 acima.)*

**Quanto tempo a cena dura, medido** *(ranks 1 a 5, décima oitava rodada)*: Fácil 2,2-3,9 rodadas · Padrão 4,2-5,1 · Padrão pesado 6,0-7,5 · Difícil 6,5-6,8 · Clímax **7,2-8,8** *(recalibrado — ver a tabela do Chefe; antes da decisão 250 media 4,7-6,7)*. **As cenas encurtaram 1,5 a 4 rodadas** em relação ao que se publicava (Fácil 2,5-4,6 · Padrão 6,0-7,7 · Padrão pesado 7,5-10,5 · Difícil 8,3-9,1 · Clímax 6,8-10,7), pela mesma causa: o grupo bate mais forte do que o motor supunha. **Isso reabre a decisão 208** — o autor tinha fechado o fork de duração escolhendo "6-8 rodadas é o ritmo real do sistema", e o ritmo real agora é 4-7. Se a mesa quiser cenas curtas, o botão **não** é dano nem RD — é o número de peças, e ele é o mesmo botão da dificuldade (ver [[🎯 Simulação de Combate — Resultados#⏱️ Décima primeira rodada — encurtando a cena (2026-08-31)|a décima primeira rodada]]).

**Os números acima já assumem a regra de Alma rara** (décima rodada de simulação): todo Mestre de Gu com a Ação Especial do próprio Caminho, e o cultivador de Alma entrando só pela exceção rolada de 1d6 (ver o molde acima). Contraintuitivo mas medido: **tirar o Alma do padrão deixou as cenas um pouco MAIS difíceis, não mais fáceis** (2-10 pontos) — uma especial de Alma isolada gasta o golpe numa barra que nada mais ataca, enquanto a especial física soma no foco de fogo e aplica Lentidão com mais frequência. Histórico completo em [[🎯 Simulação de Combate — Resultados#🔇 Décima rodada — Alma rara entre inimigos (2026-08-31)|a décima rodada]].

> [!note] Duas exceções por rank, e as duas são deliberadas
> **Padrão muda de composição no rank 1** (2 Mestres + 1 Guerreiro em vez de 3 Mestres) pelo mesmo motivo que Difícil já muda desde a decisão 137: o penhasco de volume de ações não deixa composição intermediária, e 3 Mestres no rank 1 dão 62% — abaixo da faixa de 75-99% que "Padrão" promete. Do rank 2 em diante, 3 Mestres volta a ser a composição certa.
>
> **Difícil de rank baixo é quase-Clímax, e está aceito assim** (decisão do autor): nessa faixa o grupo ainda não tem arsenal pra amortecer 7 ações por rodada, e a cena Difícil de rank baixo é legitimamente a mais perigosa da fase inicial.
>
> ⚠️ **As duas exceções foram calibradas contra números que a décima oitava rodada substituiu** (Difícil r1-2 media 31%/31% e agora mede 70%/83%; "3 Mestres no rank 1" media 62%). A *lógica* das duas — o penhasco de volume de ações — segue valendo; os *limiares* precisam ser recalibrados pelo autor junto com o resto da tabela.

**Clímax é o único nível onde uma cena inteira de cultivadores de Alma é intencional.** É lá, e só lá, que o alfa-strike total contra as quatro barras de Alma do grupo deve acontecer — a promessa do Caminho da Alma ("ignora RD por completo", [[👻 Caminho da Alma]]) continua absoluta; a regra de Alma rara muda a **frequência** do inimigo de Alma, não o poder dele. Fora do Clímax, cultivador de Alma inimigo é a exceção de 1d6 do [[#🧑‍🦱 Mestre de Gu — o inimigo humano|Mestre de Gu]] mais acima.

**"Fácil" é cena de abertura, não metade das cenas.** Uma Horda de 8 termina com os quatro personagens de pé em qualquer rank, e é isso que ela deve fazer: abrir uma sessão, gastar essência antes da cena que importa, ou mostrar que o grupo ficou mais forte. **Se metade das cenas for Fácil, a mesa cansa** — o padrão real de uma sessão é uma Fácil, uma ou duas Padrão, e uma Difícil, com o Clímax guardado para o fim do arco.

**Com 3 jogadores**, tire uma unidade de cada linha (um Mestre, ou 4 membros da horda). A horda se ajusta sozinha, porque o número de ataques dela é **um por personagem de pé**.

> ### ⚠️ Nunca use um Chefe de rank acima do grupo
>
> A linha "rank do grupo ou até +1 acima" estava aqui e **matava a mesa inteira, sempre**. A conta é simples e não tem jeito: subir o Chefe um rank **dobra a Vitalidade dele e dobra o dano dele ao mesmo tempo**, enquanto o grupo não muda. Contra um Chefe de rank +1, um grupo de rank 3 leva **15 rodadas** pra derrubá-lo e **morre em 4,6** — não é uma luta difícil, é uma execução com dados.
>
> Pior: a `RD 2 × M` do Chefe superior come inteiro o ataque de qualquer PJ que esteja usando um Gu de rank inferior ao próprio. Metade do grupo entrega o **piso de `1 × M`**, ou seja, 2 pontos de dano por acerto.
>
> **Se você quer um inimigo acima do grupo, ele não é um encontro — é uma cena de fuga**, uma negociação, ou um Golpe Matador com a Brecha já descoberta. Ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]] e [[⚡ Golpes Matadores|a Brecha]].

**O que mata personagem é volume de ações por rodada, ponderado pela qualidade delas** — não conte inimigos, conte quantas vezes eles rolam ataque. Quatro Mestres de Gu com oito ações no total são muito mais perigosos que um Chefe de três ações, mesmo "contando menos inimigos".

### O contador que importa de verdade: ações inimigas por rodada

**Conte ponderado: uma ação com Ação Especial ou dano de Alma vale mais que duas comuns** — dano de Alma ignora RD e Defesa de armadura por completo ([[👻 Caminho da Alma]]), então várias especiais de Alma disparando na mesma rodada é um alfa-strike quase simultâneo contra as quatro barras de Alma do grupo. É por isso que cultivador de Alma inimigo é raro fora do Clímax (a exceção de 1d6 do Mestre de Gu) — mas Alma não é o único perigo: acima de 8 ações/rodada, o volume bruto já é o problema, com ou sem Alma envolvida. Histórico completo de como essa curva foi medida em [[🎯 Simulação de Combate — Resultados#🆕 Quinta rodada — motor v2 pós-decisão 133 (2026-08-30)|a quinta rodada]].

| Ações ponderadas / rodada | O que a mesa sente (grupo de 4, rank igual) |
|---|---|
| 2 a 4 | Trâmite. Ninguém chega perto de cair |
| 5 a 7 | Padrão. Um ou dois personagens ficam abaixo da metade |
| 8 a 11 | Difícil. Alguém cai, e o grupo gasta recurso de verdade |
| **12 ou mais** | Clímax. Risco real de morte — use só quando a cena valer isso |

**Numa mesa de 4, o Golpe Matador Coletivo fica perigoso** — quatro participantes chegam a **+6 Níveis de Dano** no núcleo (ver [[⚡ Golpes Matadores|Golpes Matadores]]). Construa encontros contando com isso: um inimigo que separa o grupo neutraliza o combo inteiro, e é essa a defesa mais interessante que um chefe pode ter.

---

## Exemplos prontos

**Bandido da Estrada (Recruta, rank 1)** — VIT 6, Defesa 11, arma leve `1d6+FOR` (é o `M d6` do molde, com M 1). Anda em bando de 3 a 5.

**Batedor do Culto (Guerreiro, rank 2)** — VIT 24, Defesa 14, RD 2, Gu do Fulgor Lunar (`2d10`, o pool do [[📖 Catálogo de Gu|Catálogo]]) + Gu de Escamas Ocultas ativo.

**Fera-Gu Selvagem de Presas Longas (Elite, rank 2)** — VIT 42, Defesa 16, RD 4, mordida `2d12+FOR` (arma pesada + 1 Nível natural), investida que aplica Lentidão.

**Ancião Renegado (Chefe, rank 3)** — VIT 312 (`78 × M`, M 4), Defesa 18, RD 8 (Gu do Dossel Celestial sustentado), dois ataques por rodada: Gu do Cristal de Gelo (`4d10`, aplica Lentidão) ou golpe melee `4d12+FOR` (arma média + 2 Níveis do Gu de Força ativo). Ignora a primeira Lentidão/Confuso sofrida na cena.

### Imortais (rank 6+) — some a densidade de Marca

Um Imortal não se descreve só pelo rank. Declare **rank + nível de domínio no Caminho principal** (ver [[☯️ Marcas de Dao|Marcas de Dao]]) — é o nível de domínio que diz quantos Níveis de Dano ele soma nos Gu do Caminho dele, e é isso que decide se a luta é difícil ou impossível.

> [!important] A régua imortal é o ΔB, não a quantidade — a tabela de composição acima NÃO vale no rank 6+
> Medido na oitava rodada de simulação: nos ranks 6-9, **toda** composição da
> tabela mortal vira passeio (≥93% de vitória, chegando a 100% no rank 9) —
> a escada de dificuldade por quantidade colapsa na fase imortal. O que regula
> dificuldade lá é **uma coisa só: o diferencial de nível de domínio (ΔB)**
> entre o inimigo e o grupo:
>
> | ΔB do inimigo vs. o grupo | **rank 6** | **rank 7** | **rank 8** | **rank 9** |
> |---|---|---|---|---|
> | **igual (ΔB 0)** | 52% | 34% | 59% | 85% |
> | **+1 nível de domínio** | **23%** | **16%** | **36%** | 80% |
> | **+3 níveis** | **3%** | **1%** | **5%** | **57%** |
>
> Monte a cena imortal escolhendo o ΔB do inimigo principal, não contando
> cabeças. Escolta (Guerreiros/Hordas do rank) é textura — não muda a conta.
> A fase mortal (ranks 1-5) segue a tabela de composição normalmente.
>
> **O que faz a matriz funcionar nos ranks 7-9: o molde imortal soma treino.**
> Até a décima quarta rodada o ΔB só era dial de verdade no rank 6 — do 7 em
> diante ele perdia força até sumir (no rank 9, um inimigo três níveis acima
> ainda perdia 98% das vezes), pela assimetria que a oitava rodada
> diagnosticou: o acerto do inimigo escala `+1/rank` e a Defesa dos
> personagens `+2/rank`, então o inimigo passa a errar tanto que nenhum bônus
> de dano compensa. A correção, medida e adotada *(decisão 215)*:
>
> ```
> Molde de rank 7 ou mais soma o bônus de treino do rank dele no acerto
>       (+5 nos ranks 6-7 · +6 nos ranks 8-9 — tabela em 💪 Atributos)
> ```
>
> **Só do rank 7 pra cima**, e **só no lado do inimigo**: a fase mortal e o
> rank 6 ficam **exatamente** como estavam (0,00pp de diferença medida), e os
> ranks 7-9 recuperam a escada — é a linha "+3 níveis" da matriz acima saindo
> de 43/79/98% para **1/5/57%**.
>
> *(As 5 composições rodadas a ΔB 0 no rank 6 seguem em 76-100% — o "passeio"
> da oitava rodada continua de pé lá. Nos ranks 7-9, com o treino do molde, a
> tabela de composição volta a ter gradação: Fácil 100% · Padrão 96-99% ·
> Padrão pesado 53-77% · Difícil 23-36% · Clímax 55-94%.)*

**Imortal Recém-Ascendido (Elite, rank 6, Vislumbre)** — VIT `21 × 32` = 672, Defesa 20, RD 64, Gu Imortal de ataque `32d8` no passo padrão. Perigoso, mas ainda "novo".

**Imortal Denso (Chefe, rank 6, real Pequeno Feito · ~9.000 Marcas · dois feitos de gênio pobre empilhados = opera como Grão-Mestre, decisão 133)** — VIT `63 × 32` = 2.016, Defesa 22, RD 64, mesmo Gu Imortal mas **+3 Níveis** pela densidade emprestada: passo padrão d8 sobe três degraus até `d12 + 1/dado` = **`32d12 + 32`**. É o exemplo de por que a contagem de Marca importa mais que o número do rank — e por que, no romance, é o mesmo Fang Yuan de rank 6 que bate como Grão-Mestre.

> [!danger] Medido — este perfil é sentença, não encontro
> A quinta rodada de simulação testou este exato NPC como Chefe de Clímax
> contra um grupo recém-ascendido de rank 6: o grupo venceu em **apenas 5,2%
> das vezes** (contra 20% do mesmo Imortal sem o gênio pobre duplo). **É um
> inimigo acima do rank do grupo, não um encontro** — trate como uma cena de
> fuga, negociação, ou um Golpe Matador com a Brecha já descoberta (ver
> [[🏃 Fuga e Perseguição]] e [[⚡ Golpes Matadores|a Brecha]]). Nunca ponha um
> duplo-gênio como oponente padrão de uma cena Difícil ou Clímax comum.
