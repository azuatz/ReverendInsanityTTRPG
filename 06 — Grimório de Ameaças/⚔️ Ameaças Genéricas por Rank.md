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

Estatísticas prontas de inimigo, escaladas pela mesma tabela de M do rank que os personagens usam (ver [[⚔️ Combate|Combate]]). Os números por molde valem pra qualquer tamanho de mesa; o que muda com o número de jogadores é **quantos inimigos por cena** — ver a tabela de composição mais abaixo. O histórico de medição de tudo o que está aqui vive em [[🎯 Simulação de Combate — Resultados#🗃️ Arqueologia movida da ficha de ameaças (2026-09-06)|Simulação de Combate — Resultados]].

## Os três moldes

> **Todo inimigo tem estágio igual ao do grupo**, salvo quando você quiser o contrário: some `+Grau por dado` no dano dele e `+4 × M × Grau` na Vitalidade, exatamente como um PJ. Sem isso, a mesa atropela o bestiário a partir do estágio Médio.

| Molde | Papel | Vitalidade | Defesa | **Acerto** | RD | Dano por ataque | Quantos por cena (rank igual, mesa de 4) |
|---|---|---|---|---|---|---|---|
| **Recruta** *(só dentro de uma Horda)* | Bucha de canhão, ameaça em número | `6 × M(rank)` | `10 + rank` | **`d20 + rank + 4`** | — | `M d6` | 6 a 8 |
| **Guerreiro** | Oponente individual padrão | `12 × M(rank)` | `12 + rank` | **`d20 + rank + 6`** | `1 × M` | `M d8` | 2 a 3 |
| **Elite** | Rival nomeado, luta de verdade | `21 × M(rank)` | `14 + rank` | **`d20 + rank + 8`** | `2 × M` | `M d10`, e **do rank 3 em diante** costuma ter 1 Golpe Matador próprio | 1 a 2 |

> **Recruta solto é decorativo** — um personagem do mesmo rank mata um por golpe, e seis Recrutas soltos são seis ações que nunca acontecem. **Use Recruta só dentro de uma Horda.** Os três moldes continuam aqui porque servem para montar cena sob medida, mas Guerreiro e Elite só ameaçam com a Ação Especial ligada, e Recruta só em bloco.

**A coluna de Acerto é a fórmula do jogador** (`d20 + atributo + (rank + 2) + rank do Gu`) já resolvida: um Guerreiro de rank 3 acerta com `d20 + 9` — 75% contra a Defesa 15 de um PJ do mesmo rank, 55% contra a Defesa 19 de quem carrega um Gu de movimento. É a taxa que [[⚔️ Combate|Combate]] promete. O **dano** usa o mesmo pool de dados dos jogadores: `M` dados do tipo do Caminho dele, mais `M × Grau` se tiver estágio; um Gu de Força ativo sobe o **tipo do dado**, como faria num PJ.

## 🪓 Ação Especial — todo Guerreiro e Elite tem uma

**Uma por inimigo, uma vez por cena.** Um ataque com **+4 no acerto** que também aplica **Lentidão 2**. Não muda nenhuma estatística do molde e é o que separa um inimigo de um saco de pancada, porque **tirar a ação de um personagem vale mais que tirar Vitalidade dele**. Descreva-a como um Gu — o Batedor solta o Gu do Nevoeiro Cego, a Fera-Gu dá a investida que derruba — e **anuncie quando usar**: a especial gasta, e o grupo precisa saber que já foi.

## 👥 A Horda — recrutas como uma unidade só

Recrutas individuais morrem antes de agir. A Horda para de tratá-los como fichas separadas e os junta numa peça só.

| A Horda | |
|---|---|
| **Vitalidade** | `6 × M × (nº de membros)`, somada numa barra só |
| **Defesa** | `10 + rank` |
| **Acerto** | `d20 + rank + 6` — o `+2` é o cerco |
| **Ataques por rodada** | **Um por personagem de pé — com piso de 2 contra dois alvos e 3 contra um alvo só.** Não é iniciativa individual, é estar cercado |
| **Dano** | `M d6`, **e o dado sobe um tipo a cada 4 membros vivos acima dos 4 primeiros**: 4 a 7 membros `M d6` · 8 a 11 `M d8` · 12 a 15 `M d10` · 16 ou mais `M d12` (teto) |

Uma horda de 8 bate em **`M d8`**; uma de 12, em **`M d10`**. Conforme perde Vitalidade, perde membros, e **o dado desce sozinho** — o grupo sente a horda enfraquecendo sem contar corpos. O **piso de ataques** existe porque oito feras cercando uma pessoa devem assustar, não cansar: sem ele, a Horda contra um alvo solitário vira guerra de atrito, um ataque por rodada contra uma barra dimensionada para quatro.

> [!warning] Horda contra UM personagem é cena de fuga, não encontro
> Com o piso, a matilha executa: medido, um PJ sozinho contra uma Horda de 8 vence **0-37% das vezes** (dez de doze células abaixo de 1%) em cerca de 5 rodadas. É o desenho funcionando — cerco contra uma pessoa só é como cerco deve ser. **Não existe configuração que faça essa cena durar** e continuar ganhável: as variantes medidas (Horda de 2, de 3, Vitalidade escalada pela mesa) devolvem cenas de 3-4 rodadas. Para uma caçada solo *jogável*, use uma matilha de 2-3; se um personagem se separar do grupo e a matilha o encontrar, o jogo ali é [[🏃 Fuga e Perseguição|fugir]] — e a mesa deve saber disso antes de se separar.

**Área é a resposta.** Um Gu de área contra uma horda tira Vitalidade da barra inteira; é a única situação do jogo em que dano em área supera dano concentrado, e é o que faz esses Gu valerem uma vaga na Abertura.

## 🐺 Feras — três traços, cole em qualquer molde

O Grimório não tem uma criatura sequer porque não precisa: uma fera é qualquer molde acima (Recruta, Guerreiro, Elite, Horda) com estes três traços colados por cima.

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

> [!info] Quantos Gu ele sustenta: **2**
> O teto de sustentação de um **Mestre de Gu comum é 2**, não 3 ([[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]]) — sustentar três tarefas sem errar é a marca de um cultivador excepcional, e o inimigo de rua não é um. Na prática ele entra em cena com o **Gu de defesa** (a RD `1 × M` acima) e **um segundo** à escolha do mestre: movimento, percepção ou reforço. **Inimigo nomeado — Elite com nome, rival de arco, Chefe — sustenta 3**, como os jogadores. Essa diferença de uma vaga é a forma mais barata de fazer um vilão parecer diferente do capanga sem mexer em nenhum número de dano.

**A Ação Especial é o que separa o molde de um saco de pancada**, e é mais perigosa ainda quando ele aparece sozinho: o +4 quase garante o acerto (e com ele a Lentidão), e o dano soma na mesma Vitalidade que o resto da cena já está batendo. Com 2 ações e uma especial, ele ameaça de verdade com **metade da Vitalidade de um Chefe**.

**A exceção rara — o cultivador do Caminho da Alma.** Inimigo com poder de Alma é raro: a maioria dos Mestres de Gu inimigos é de outros Caminhos. Ao montar a cena, **role 1d6 por Mestre de Gu — só em 6 ele é um cultivador de Alma de verdade**, e a Ação Especial dele vira **`M d12`, ignora RD por completo e mira a barra de Alma** (mantendo a Lentidão 2). Sozinho, esse golpe abre uma barra que nada mais na cena vai tocar; **várias especiais de Alma empilhadas na mesma barra são um alfa-strike** — por isso "todos de Alma" é ferramenta de Clímax, nunca composição casual.

**Como variar sem refazer a ficha:** troque o Caminho da especial. Vento vira reposicionamento que quebra o cerco do grupo; Força vira o melee de `M d10` do molde; Sabedoria vira o inimigo que age primeiro toda rodada. A estrutura (`21 × M`, 2 ações, uma especial) não muda, e a tabela de composição já assume especiais de Caminhos variados. **Ele também tem os limites de um cultivador**, e usá-los é o que torna a luta interessante: a Essência dele acaba, os Gu dele podem ser roubados depois, e ele tem um Golpe Matador com **Brecha** que o grupo pode ter descoberto antes da cena.

### 🎒 O que ele carrega — loadout em três rolagens

Todo Mestre de Gu morto, rendido ou extorquido tem uma bagagem, e ela é o motivo de rendição valer mais que execução (ver [[⚰️ Espólio]]). Role na hora, só quando importar:

```
Gu carregados = rank + 1d3          (metade do rank dele, resto 1 abaixo)
Papéis: 1 ataque · 1 defesa ou movimento · o resto utilidade/investigação
Receita: role 1d6 → em 5-6, ele sabe UMA receita de valor
         (em 6, ela é rara — sorteie no [[📜 Livro de Receitas de Gu]])
```

Escolha os Gu concretos no [[📖 Catálogo de Gu]] pelo Caminho que a especial dele já declarou — ou deixe genérico ("um Gu de fuga, dois de utilidade") até alguém perguntar. **A receita não está escrita num papel no bolso**: está na cabeça dele, e é isso que faz um Mestre de Gu capturado valer uma cena de interrogatório ou barganha em vez de um saque.

## 🎲 Os números que faltavam em toda ficha de inimigo

### Destreza, e onde ela NÃO entra

| Molde | DES |
|---|---|
| **Horda** | **0** — massa não esquiva |
| **Recruta** | **0** |
| **Guerreiro** | **+1** |
| **Mestre de Gu** | **+1** — treinou a mente, não o corpo |
| **Elite** | **+2** |
| **Chefe** | **+3** |
| **Imortal (6+)** | **+4** |

A DES do molde serve para **três coisas e só elas**: **iniciativa** (`d20 + DES`), **desempate** em disputa de movimento, e a **Perseguição** ([[🏃 Fuga e Perseguição]]). **Ela não entra na Defesa** — a Defesa de cada molde é o número publicado na ficha dele.

### A barra de Alma, e a Defesa dela

> **Barra de Alma de qualquer molde = 95% da Vitalidade dele.**
> **Defesa contra Alma de qualquer molde = `13 + 2 × rank`.**

| Molde | Alma no rank 1 | rank 3 | rank 5 | Defesa contra Alma |
|---|---|---|---|---|
| Guerreiro | 11 | 76 | 363 | `13 + 2 × rank` |
| Elite | 20 | 109 | 500 | idem |
| Mestre de Gu | 20 | 112 | 509 | idem |
| Chefe | 59 | 408 | 1.920 | idem |
| **Horda** | — | — | — | **não tem** |

**A Horda é a única exceção: massa não tem alma única**, e por isso não tem barra de Alma nem se ataca por ela. Contra Horda, Alma é dano desperdiçado — escolha de desenho, não esquecimento.

### Quando a Alma de um inimigo zera

**Ele sai da cena na hora, com o corpo intacto.** Não rola Teste de Morte, não agoniza, não se levanta: a mente apagou e o corpo continua ali. **Isso não é a mesma regra dos personagens** — um PJ que zera a Alma entra em [[❤️ Recursos e Dano#Alma zerada — Colapso Espiritual|Colapso Espiritual]], com Teste de Morte espiritual e a primeira queda nunca matando, porque a mesa precisa que ele volte. Um molde não tem essa rede: é peça de cena, e a cena acaba para ele.

> [!tip] É isto que faz o Caminho da Alma ser a via de **captura**, e não só de dano
> Um inimigo derrubado pela Vitalidade está morrendo. **Um inimigo derrubado pela Alma está inteiro, inconsciente e no chão** — dá para amarrar, interrogar, entregar, vender ou carregar. É a diferença entre um cadáver e um prisioneiro, e ela custa **a mesma quantidade de acertos**. Casa com o exemplo canônico do Golpe Matador Coletivo — *"busca e travamento ilimitados"*, que o romance chama de **"o método de captura número um"** e que **não causa dano nenhum** ([[⚡ Golpes Matadores]]). O Caminho da Alma é a versão individual daquilo.

### O molde Chefe, por inteiro

O Chefe é **um Elite com quatro números próprios**. Tudo o mais — Ação Especial, condições, comportamento — segue o Elite.

| | Chefe |
|---|---|
| **Vitalidade** | pela tabela de ranks abaixo (`63 / 80 / 100 / 94 / 115 × M`) |
| **Ações por rodada** | pela mesma tabela (2 / 2 / 2 / 3 / 3) |
| **Defesa** | **`16 + rank`** |
| **Acerto** | **`+8 + rank`** |
| **RD** | **`2 × M`** |
| **Dano** | **`M d10`** |
| **DES** | +3 |
| **Alma** | 95% da Vitalidade · Defesa `13 + 2 × rank` |

## O Chefe — a regra especial pra combate solo

Um único inimigo contra um grupo perde a ação por turno: 3 ou 4 personagens agem, ele age uma vez, e a luta acaba rápido demais pra ser memorável. Pra qualquer inimigo que a cena trata como **Chefe** (rival de arco, vilão de sessão):

1. **Vitalidade e ações vêm da tabela abaixo** — nenhuma das duas é número fixo: a barra vai de `63 × M` no rank 1 a `115 × M` no rank 5.
2. **Ignora a primeira Condição de controle** que sofrer em cada cena (atordoamento, lentidão, medo) — descreva como ele resiste, não como ela simplesmente falha.
3. Tem **um Gu de defesa sustentado** e, **se for de rank 3 ou mais**, pelo menos **um Golpe Matador** (ranks 1 e 2 não montam combo — decisão 243; um Chefe de rank baixo compensa com ações) — um chefe sem defesa própria morre rápido demais quando o grupo foca fogo nele.

### Vitalidade e ações do Chefe, por rank

| Rank do Chefe | Vitalidade | Ações por rodada | Vitória do grupo *(mesa de 4, com 1 Guerreiro de apoio)* | Duração |
|---|---|---|---|---|
| **1** | `63 × M` | **2** | **69%** | 6,5 rodadas |
| **2** | `80 × M` | **2** | **68%** | 7,5 |
| **3** | `100 × M` | **2** | **75%** | 8,3 |
| **4** | `94 × M` | **3** | **71%** | 7,2 |
| **5** | `115 × M` | **3** | **72%** | 7,7 |
| **6+** | `63 × M` | **4** | ver a régua ΔB dos imortais, mais abaixo | — |

As cinco células caem dentro da faixa de **56-87%** que "Clímax" promete, e a cena dura 6,5 a 8,3 rodadas — o ritmo alvo de 6-8, com o rank 3 estourando 0,3. O rank 6+ segue em `63 × M` de propósito: a fase imortal se dimensiona pela régua ΔB, não por esta tabela.

**São dois botões, e não se confundem: ações governam a dificuldade, Vitalidade governa o ritmo.** Para apertar uma cena, **suba a Vitalidade** — alonga a luta sem dobrar o dano que entra no grupo. **Nunca suba o rank do Chefe: é TPK medido**, e a advertência mais abaixo diz por quê.

## Referência rápida por rank (M já aplicado)

| Rank | M | Recruta VIT | Guerreiro VIT | **Mestre de Gu VIT** | Elite VIT | Chefe VIT | **Horda de 8 VIT** |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 6 | 12 | **21** | 21 | 63 | **48** |
| 2 | 2 | 12 | 24 | **42** | 42 | 126 | **96** |
| 3 | 4 | 24 | 48 | **84** | 84 | 252 | **192** |
| 4 | 8 | 48 | 96 | **168** | 168 | 504 | **384** |
| 5 | 16 | 96 | 192 | **336** | 336 | 1.008 | **768** |

A Horda usa `6 × M × nº de membros` — a coluna acima é o caso de 8. O Mestre de Gu tem a mesma Vitalidade de um Elite; a diferença está nas **duas ações** e na Ação Especial própria.

## Como montar uma cena de combate

Os números entre parênteses são a **vitória medida do grupo** numa mesa de 4, pela [[🎯 Simulação de Combate — Resultados\|simulação]]. A maioria das composições vale em qualquer rank; **"Difícil" é a exceção — muda de composição por faixa de rank**, como o Chefe muda de número de ações. A causa é a mesma nos dois casos — **volume bruto de ações contra o arsenal do grupo** —, e a lição é que nem toda composição escala limpo do rank 1 ao 5.

| Tipo de cena | **rank 1** | **rank 2** | **rank 3** | **rank 4** | **rank 5** |
|---|---|---|---|---|---|
| **Fácil** | Horda de 8 *(100%)* | idem *(100%)* | idem *(100%)* | idem *(100%)* | idem *(100%)* |
| **Padrão** | **2 Mestres + 1 Guerreiro** *(98%)* | 3 Mestres de Gu *(93%)* | idem *(97%)* | idem **+1 ação em 1 deles** *(98%)* | idem **+1 ação em 2 deles** *(98%)* |
| **Padrão pesado** | 2 Mestres + Horda de 8 *(83%)* | idem *(82%)* | idem *(82%)* | idem **+1 ação em 1 Mestre** *(85%)* | idem **+1 ação em 2 Mestres** *(89%)* |
| **Difícil** | 3 Mestres + 1 Guerreiro *(64%)* | idem *(69%)* | idem **+1 ação em 1 Mestre** *(71%)* | idem **+1 ação em 2 Mestres** *(71%)* | 4 Mestres **+1 ação em 2 deles** *(60%)* |
| **Clímax** | Chefe + Guerreiro *(69%)* | idem *(68%)* | idem *(75%)* | idem *(71%)* | idem *(72%)* — ou 1 Elite especial + 3 Mestres ✝ |

**Faixa que cada linha promete:** Fácil 95-100% · Padrão 75-99% · Padrão pesado 60-90% · Difícil 40-75% · Clímax 56-87% — as 25 células acima estão dentro dela. **Duração medida** *(ranks 1 a 5)*: Fácil 2,2-3,9 rodadas · Padrão 4,2-5,1 · Padrão pesado 6,0-7,5 · Difícil 6,5-6,8 · Clímax **6,5-8,3**.

**Para apertar uma cena sem alongá-la, dê uma ação extra a um dos inimigos** em vez de acrescentar outro inimigo: peça a mais derruba a vitória do grupo demais **e** estoura o ritmo, porque mais inimigos é mais barra para mastigar. Para alongar sem apertar, suba a Vitalidade. São os mesmos dois botões do molde Chefe.

Duas premissas embutidas nesses números: **ataque não é ação treinada** (o bônus de treino só vale em teste de perícia — a única exceção é o molde imortal de rank 7+, mais abaixo), e **a regra de Alma rara** já está aplicada, isto é, todo Mestre de Gu com a especial do próprio Caminho e o cultivador de Alma entrando só pela exceção de 1d6. *(✝ variante não retestada; sob a Alma rara os 3 Mestres dela também mudam de especial, então o número está duplamente desatualizado.)*

> [!note] Duas exceções por rank, e as duas são deliberadas
> **Padrão muda de composição no rank 1** (2 Mestres + 1 Guerreiro em vez de 3 Mestres): o penhasco de volume de ações não deixa composição intermediária, e 3 Mestres no rank 1 ficam abaixo da faixa de 75-99% que "Padrão" promete. Do rank 2 em diante, 3 Mestres volta a ser a composição certa.
>
> **Difícil de rank baixo é quase-Clímax, e está aceito assim** (decisão do autor): nessa faixa o grupo ainda não tem arsenal pra amortecer 7 ações por rodada, e a cena Difícil de rank baixo é legitimamente a mais perigosa da fase inicial.

**Clímax é o único nível onde uma cena inteira de cultivadores de Alma é intencional.** É lá, e só lá, que o alfa-strike total contra as quatro barras de Alma do grupo deve acontecer — a promessa do Caminho da Alma ("ignora RD por completo", [[👻 Caminho da Alma]]) continua absoluta; a Alma rara muda a **frequência** do inimigo de Alma, não o poder dele. Fora do Clímax, ele é a exceção de 1d6 do [[#🧑‍🦱 Mestre de Gu — o inimigo humano|Mestre de Gu]].

**"Fácil" é cena de abertura, não metade das cenas.** Uma Horda de 8 termina com os quatro personagens de pé em qualquer rank, e é isso que ela deve fazer: abrir uma sessão, gastar essência antes da cena que importa, ou mostrar que o grupo ficou mais forte. **Se metade das cenas for Fácil, a mesa cansa** — o padrão real de uma sessão é uma Fácil, uma ou duas Padrão e uma Difícil, com o Clímax guardado para o fim do arco.

**Com 3 jogadores**, tire uma unidade de cada linha (um Mestre, ou 4 membros da horda). A horda se ajusta sozinha, porque o número de ataques dela é **um por personagem de pé**.

> ### ⚠️ Nunca use um Chefe de rank acima do grupo
>
> A conta é simples e não tem jeito: subir o Chefe um rank **dobra a Vitalidade dele e dobra o dano dele ao mesmo tempo**, enquanto o grupo não muda. Contra um Chefe de rank +1, um grupo de rank 3 leva **15 rodadas** pra derrubá-lo e **morre em 4,6** — não é uma luta difícil, é uma execução com dados. Pior: a `RD 2 × M` do Chefe superior come inteiro o ataque de qualquer PJ que use um Gu de rank inferior ao próprio, e metade do grupo entrega o **piso de `1 × M`** — 2 pontos de dano por acerto.
>
> **Se você quer um inimigo acima do grupo, ele não é um encontro — é uma cena de fuga**, uma negociação, ou um Golpe Matador com a Brecha já descoberta. Ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]] e [[⚡ Golpes Matadores|a Brecha]].

### O contador que importa de verdade: ações inimigas por rodada

**O que mata personagem é volume de ações por rodada, ponderado pela qualidade delas** — não conte inimigos, conte quantas vezes eles rolam ataque. Quatro Mestres de Gu com oito ações no total são muito mais perigosos que um Chefe de três ações. **Conte ponderado: uma ação com Ação Especial ou dano de Alma vale mais que duas comuns** — dano de Alma ignora RD e Defesa de armadura por completo ([[👻 Caminho da Alma]]), e várias especiais de Alma na mesma rodada são um alfa-strike quase simultâneo contra as quatro barras do grupo. Acima de 8 ações/rodada, porém, o volume bruto já é o problema com ou sem Alma envolvida. Como essa curva foi medida: [[🎯 Simulação de Combate — Resultados#🆕 Quinta rodada — motor v2 pós-decisão 133 (2026-08-30)|a quinta rodada]].

| Ações ponderadas / rodada | O que a mesa sente (grupo de 4, rank igual) |
|---|---|
| 2 a 4 | Trâmite. Ninguém chega perto de cair |
| 5 a 7 | Padrão. Um ou dois personagens ficam abaixo da metade |
| 8 a 11 | Difícil. Alguém cai, e o grupo gasta recurso de verdade |
| **12 ou mais** | Clímax. Risco real de morte — use só quando a cena valer isso |

> [!warning] A régua mede **volume**, e um Chefe não é volume — confira sempre contra a tabela de composição
> **Chefe + Guerreiro no rank 1 conta 3 ações ponderadas**, o que esta régua chamaria de *"trâmite"* — e a composição medida diz **Clímax, 69% de vitória em 6,5 rodadas**. Não é contradição: a régua conta **quantas** ações vêm, e o Chefe concentra numa peça só o que ela pressupõe espalhado — Vitalidade alta, dano grande por golpe, primeira condição de controle ignorada. **Para cena de um inimigo forte, use a tabela de composição.**

**Numa mesa de 4, o Golpe Matador Coletivo fica perigoso** — quatro participantes chegam a **+6 Níveis de Dano** no núcleo (ver [[⚡ Golpes Matadores|Golpes Matadores]]). Construa encontros contando com isso: um inimigo que separa o grupo neutraliza o combo inteiro, e é essa a defesa mais interessante que um chefe pode ter.

---

## Exemplos prontos

**Bandido da Estrada (Recruta, rank 1)** — VIT 6, Defesa 11, arma leve `1d6+FOR` (é o `M d6` do molde, com M 1). Anda em bando de 3 a 5.

**Batedor do Culto (Guerreiro, rank 2)** — VIT 24, Defesa 14, RD 2, Gu do Fulgor Lunar (`2d10`, o pool do [[📖 Catálogo de Gu|Catálogo]]) + Gu de Escamas Ocultas ativo.

**Fera-Gu Selvagem de Presas Longas (Elite, rank 2)** — VIT 42, Defesa 16, RD 4, mordida `2d12+FOR` (arma pesada + 1 Nível natural), investida que aplica Lentidão.

**Ancião Renegado (Chefe, rank 3)** — VIT 400 (`100 × M`, M 4), Defesa 18, RD 8 (Gu do Dossel Celestial sustentado), dois ataques por rodada: Gu do Cristal de Gelo (`4d10`, aplica Lentidão) ou golpe melee `4d12+FOR` (arma média + 2 Níveis do Gu de Força ativo). Ignora a primeira Lentidão/Confuso sofrida na cena.

### Imortais (rank 6+) — some a densidade de Marca

Um Imortal não se descreve só pelo rank. Declare **rank + nível de domínio no Caminho principal** (ver [[☯️ Marcas de Dao|Marcas de Dao]]) — é o nível de domínio que diz quantos Níveis de Dano ele soma nos Gu do Caminho dele, e é isso que decide se a luta é difícil ou impossível.

> [!important] A régua imortal é o ΔB, não a quantidade — a tabela de composição NÃO vale no rank 6+
> Nos ranks 6-9, **toda** composição da tabela mortal vira passeio (≥93% de vitória, chegando a 100% no rank 9): a escada de dificuldade por quantidade colapsa na fase imortal. O que regula dificuldade lá é **uma coisa só: o diferencial de nível de domínio (ΔB)** entre o inimigo e o grupo.
>
> | ΔB do inimigo vs. o grupo | **rank 6** | **rank 7** | **rank 8** | **rank 9** |
> |---|---|---|---|---|
> | **igual (ΔB 0)** | 52% | 34% | 59% | 85% |
> | **+1 nível de domínio** | **23%** | **16%** | **36%** | 80% |
> | **+3 níveis** | **3%** | **1%** | **5%** | **57%** |
>
> Monte a cena imortal escolhendo o ΔB do inimigo principal, não contando cabeças. Escolta (Guerreiros/Hordas do rank) é textura — não muda a conta. A fase mortal (ranks 1-5) segue a tabela de composição normalmente.
>
> **O que faz a matriz funcionar nos ranks 7-9 é o molde imortal somar treino:**
>
> ```
> Molde de rank 7 ou mais soma o bônus de treino do rank dele no acerto
>       (+5 nos ranks 6-7 · +6 nos ranks 8-9 — tabela em 💪 Atributos)
> ```
>
> **Só do rank 7 pra cima**, e **só no lado do inimigo**: a fase mortal e o rank 6 ficam exatamente como estavam. Com o treino do molde, a tabela de composição volta a ter gradação nos ranks 7-9 — Fácil 100% · Padrão 96-99% · Padrão pesado 53-77% · Difícil 23-36% · Clímax 55-94% — enquanto no rank 6, a ΔB 0, as cinco composições seguem em 76-100%.

**Imortal Recém-Ascendido (Elite, rank 6, Vislumbre)** — VIT `21 × 32` = 672, Defesa 20, RD 64, Gu Imortal de ataque `16d8 + 104` *(teto de 16 dados, decisão 225)* no passo padrão. Perigoso, mas ainda "novo".

**Imortal Denso (Chefe, rank 6, real Pequeno Feito · ~9.000 Marcas · dois feitos de gênio pobre empilhados = opera como Grão-Mestre, decisão 133)** — VIT `63 × 32` = 2.016, Defesa 22, RD 64, mesmo Gu Imortal mas **+3 Níveis** pela densidade emprestada: o passo padrão d8 sobe três degraus até `d12 + 1/dado` = **`16d12 + 136` *(teto de 16 dados, decisão 225)***. É o exemplo de por que a contagem de Marca importa mais que o número do rank — e por que, no romance, é o mesmo Fang Yuan de rank 6 que bate como Grão-Mestre.

> [!danger] Medido — este perfil é sentença, não encontro
> Contra um grupo recém-ascendido de rank 6, este exato NPC como Chefe de Clímax deixa o grupo vencer em **apenas 5,2% das vezes** (contra 20% do mesmo Imortal sem o gênio pobre duplo). **É um inimigo acima do rank do grupo, não um encontro** — trate como cena de fuga, negociação, ou um Golpe Matador com a Brecha já descoberta (ver [[🏃 Fuga e Perseguição]] e [[⚡ Golpes Matadores|a Brecha]]). Nunca ponha um duplo-gênio como oponente padrão de uma cena Difícil ou Clímax comum.

> [!note] Por que este Grimório para no rank 6 — e isso é decisão, não lacuna
> Dos **ranks 7 a 9** o sistema oferece a **matriz de diferencial de domínio** e o **molde por `M`**, que escalam sozinhos, e **não oferece exemplos prontos**. É deliberado: nesse patamar o confronto não se resolve por ficha. Um Imortal de rank 8 contra um grupo não é encontro de combate, é situação política, e se resolve por **trava, terreno e relógio** — ver o [[🎬 Como Criar Suas Sessões#🔒 O cardápio de travas — por que os poderosos não resolvem isso|cardápio de travas]], as [[🗺️ Supressão Regional|Muralhas Regionais]] e a [[🌩️ Calamidades e Provações|Calamidade marcada no calendário dele]]. Fichas de rank 7 a 9 dariam ao mestre a impressão errada de que aquilo é para ser rolado.
>
> **Se você precisar mesmo de números nesse patamar:** pegue qualquer molde acima, aplique o `M` do rank e some o diferencial de domínio. É o que uma ficha pronta faria, e ela não saberia nada que você não saiba.
