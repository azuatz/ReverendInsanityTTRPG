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
| **Ataques por rodada** | **Um por personagem de pé.** Não é iniciativa individual, é estar cercado |
| **Dano** | `M d6`, **e o dado sobe um tipo a cada 4 membros vivos acima dos 4 primeiros**: 4 a 7 membros `M d6` · 8 a 11 `M d8` · 12 a 15 `M d10` · 16 ou mais `M d12` (teto) |

Uma horda de 8 bate em **`M d8`**; uma de 12, em **`M d10`**. Conforme perde Vitalidade, perde membros, e **o dado desce sozinho** — o grupo sente a horda enfraquecendo sem ninguém precisar contar corpos.

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
| **Ação Especial** | Gu do **Caminho da Alma**: **`M d12`**, **ignora RD por completo**, e aplica Lentidão 2 |

**A especial de Alma é o que faz o molde funcionar.** A `RD 1 × M` que quase todo personagem carrega come cerca de 40% de um golpe comum; dano de Alma passa inteiro, e ainda bate num trilho que quase ninguém defende. Um Mestre de Gu com 2 ações e um golpe que ignora armadura ameaça de verdade com **metade da Vitalidade de um Chefe**.

**Como variar sem refazer a ficha:** troque o Caminho da especial. Vento vira reposicionamento que quebra o cerco do grupo; Força vira um melee de `M d10`; Sabedoria vira o inimigo que age primeiro toda rodada. A estrutura (`21 × M`, 2 ações, uma especial) não muda.

**Ele também tem os limites de um cultivador**, e usá-los é o que torna a luta interessante: a Essência dele acaba, os Gu dele podem ser roubados depois, e ele tem um Golpe Matador com **Brecha** que o grupo pode ter descoberto antes da cena.

## O Chefe — a regra especial pra combate solo

Um único inimigo contra um grupo perde a ação por turno na maioria dos sistemas — 3 ou 4 personagens agem, ele age uma vez, e a luta acaba rápido demais pra ser memorável. Pra qualquer inimigo que a cena trata como **Chefe** (rival de arco, vilão de sessão):

1. **Vitalidade × 3** sobre o valor de Elite — `63 × M(rank)`.
2. **Age várias vezes por rodada, e o número vem da tabela abaixo** — não é fixo.
3. **Ignora a primeira Condição de controle** que sofrer em cada cena (atordoamento, lentidão, medo) — descreva como ele resiste, não como ela simplesmente falha.
4. Tem pelo menos **um Golpe Matador** e **um Gu de defesa sustentado** — um chefe sem defesa própria morre rápido demais quando o grupo foca fogo nele.

### Quantas ações o Chefe tem

| Rank do Chefe | Ações por rodada | Vitória do grupo *(mesa de 4, com 1 Guerreiro de apoio)* |
|---|---|---|
| **1** | **4** | 57% |
| **2** | **2** | 62% |
| **3** | **2** | 79% · com 3 ações vira 45%, que é o clímax mais duro do jogo |
| **4–5** | **3** | 75% |
| **6+** | **4** | não simulado |

**Por que não é uma escala limpa.** A dificuldade de um Chefe não é governada por ele, e sim por **quantos Golpes Matadores o grupo consegue pagar naquele rank**. No rank 1 ninguém paga um, e o Chefe precisa de 4 ações para ameaçar. Nos ranks 2 e 3 o grupo paga um combo cada, esvazia o tanque, e **duas ações do Chefe já bastam**. Do rank 4 em diante o combo fica barato de novo e o Chefe precisa de 3. A tabela acima é medida, não deduzida — use os números dela e ignore a intuição.

**Onde isso cai, medido:** contra uma mesa de 4 do mesmo rank, um Chefe com as ações da tabela acima mais um Guerreiro de apoio é uma luta de **7 a 10 rodadas** que o grupo ganha em **56% a 80% das vezes**, terminando com **1,5 a 2,1 personagens de pé**. Esse é o alvo de um clímax de arco. Para apertar sem sair do jogável, **suba a Vitalidade do Chefe** (`63 × M` → `94 × M`) em vez de subir o rank dele: alonga a luta sem dobrar o dano que entra no grupo. Subir pra 4 ações por rodada leva a vitória do grupo pra ~50% e é o teto do que a mesa aguenta.

## Referência rápida por rank (M já aplicado)

| Rank | M | Recruta VIT | Guerreiro VIT | **Mestre de Gu VIT** | Elite VIT | Chefe VIT | **Horda de 8 VIT** |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 6 | 12 | **21** | 21 | 63 | **48** |
| 2 | 2 | 12 | 24 | **42** | 42 | 126 | **96** |
| 3 | 4 | 24 | 48 | **84** | 84 | 252 | **192** |
| 4 | 8 | 48 | 96 | **168** | 168 | 504 | **384** |
| 5 | 16 | 96 | 192 | **336** | 336 | 1.008 | **768** |

A Horda usa `6 × M × nº de membros` — a coluna acima é o caso de 8. O Mestre de Gu tem a mesma Vitalidade de um Elite, e a diferença entre os dois está nas **duas ações** e na especial de Alma.

## Como montar uma cena de combate

Os números entre parênteses são a **vitória medida do grupo** numa mesa de 4, pela [[🎯 Simulação de Combate — Resultados\|simulação]]. As composições valem em qualquer rank: fora o Chefe, a curva se mostrou estável do rank 1 ao 5. **O rank 1–2 é a faixa mais leve** — se quiser a mesma pressão lá, use a linha de baixo.

| Tipo de cena | **rank 1** | **rank 2** | **rank 3** | **rank 5** |
|---|---|---|---|---|
| **Fácil** | Horda de 8 *(100%)* | Horda de 8 *(100%)* | Horda de 8 *(100%)* | Horda de 8 *(100%)* |
| **Padrão** | 3 Mestres de Gu *(68%)* ⚠️ | 3 Mestres de Gu *(77%)* ⚠️ | 3 Mestres de Gu *(85%)* | 3 Mestres de Gu *(96%)* |
| **Padrão pesado** | 2 Mestres + Horda de 8 *(97%)*✝ | 2 Mestres + Horda de 8 *(94%)*✝ | 2 Mestres + Horda de 8 *(93%)*✝ | 2 Mestres + Horda de 8 *(96%)*✝ |
| **Difícil** | 4 Mestres de Gu *(12%)* 🔴 | 4 Mestres de Gu *(10%)* 🔴 | 4 Mestres de Gu *(11%)* 🔴 | 4 Mestres de Gu *(30%)* 🔴 |
| **Clímax** | 1 Elite especial + 3 Mestres *(68%)*✝, ou Chefe + Guerreiro *(4%)* 🔴 | idem, Chefe + Guerreiro *(57%)* | 1 Elite especial + 3 Mestres *(44%)*✝, ou Chefe + Guerreiro *(86%)* | 1 Elite especial + 3 Mestres *(46%)*✝, ou Chefe + Guerreiro *(87%)* |

*(✝ não retestado na quinta rodada — número da terceira rodada, pode estar igualmente desatualizado.)*

> [!danger] Achado da quinta rodada de simulação — a tabela acima estava otimista demais
> A quinta rodada corrigiu como o motor simula **dano de Alma** (que sempre foi
> regra — "ignora RD física e Defesa de armadura", [[👻 Caminho da Alma]] — só
> nunca tinha sido medido certo): a especial de Alma de vários Mestres de Gu
> disparando na mesma rodada é um alfa-strike quase simultâneo contra as quatro
> barras de Alma do grupo, pequenas e sem RD nenhuma. O efeito é estrutural, não
> um ajuste fino — **"Padrão" (3 Mestres) caiu de ~98% pra 68–96%**, e
> **"Difícil" (4 Mestres) caiu de 56–76% pra 10–30%, mais letal que a maioria dos
> Chefes**. Ver [[🎯 Simulação de Combate — Resultados#🆕 Quinta rodada — motor v2 pós-decisão 133 (2026-08-30)|a quinta rodada]] e a
> pendência registrada no [[🧭 Log de Decisões|Log]] — **isto ainda não tem
> correção aplicada**, é decisão do autor entre: reduzir o nº de Mestres por
> cena, dar aos PJs acesso mais barato a RD de Alma, ou aceitar que "Difícil"
> hoje é na prática nível Clímax e ajustar o rótulo.

> **"Fácil" é cena de abertura, não metade das cenas.** Uma Horda de 8 termina com os quatro personagens de pé em qualquer rank, e é isso que ela deve fazer: abrir uma sessão, gastar essência antes da cena que importa, ou mostrar que o grupo ficou mais forte. **Se metade das cenas for Fácil, a mesa cansa** — o padrão real de uma sessão é uma Fácil, uma ou duas Padrão, e uma Difícil, com o Clímax guardado para o fim do arco. **Até a pendência acima ser resolvida, trate "Difícil" com o cuidado que hoje só o Clímax merecia.**

**Com 3 jogadores**, tire uma unidade de cada linha (um Mestre, ou 4 membros da horda). A horda se ajusta sozinha, porque o número de ataques dela é **um por personagem de pé**.

> ### ⚠️ Nunca use um Chefe de rank acima do grupo
>
> A linha "rank do grupo ou até +1 acima" estava aqui e **matava a mesa inteira, sempre**. A conta é simples e não tem jeito: subir o Chefe um rank **dobra a Vitalidade dele e dobra o dano dele ao mesmo tempo**, enquanto o grupo não muda. Contra um Chefe de rank +1, um grupo de rank 3 leva **15 rodadas** pra derrubá-lo e **morre em 4,6** — não é uma luta difícil, é uma execução com dados.
>
> Pior: a `RD 2 × M` do Chefe superior come inteiro o ataque de qualquer PJ que esteja usando um Gu de rank inferior ao próprio. Metade do grupo entrega o **piso de `1 × M`**, ou seja, 2 pontos de dano por acerto.
>
> **Se você quer um inimigo acima do grupo, ele não é um encontro — é uma cena de fuga**, uma negociação, ou um Golpe Matador com a Brecha já descoberta. Ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]] e [[⚡ Golpes Matadores|a Brecha]].

**A regra de ouro antiga ("nunca dois Elites") foi removida** — ela proibia uma cena confortável e não protegia de nada. O que mata personagem é **volume de ações por rodada, ponderado pela qualidade delas** — ver a tabela logo abaixo. Não conte inimigos, e não confie na intuição de "orçamento": quatro Mestres de Gu, que somam oito ações com dano de Alma, são muito mais perigosos que um Chefe de três ações.

### O contador que importa de verdade: ações inimigas por rodada

Não conte inimigos, conte **quantas vezes eles rolam ataque por rodada**. É esse número que decide se a cena machuca:

**E conte ponderado: uma ação que vem com Ação Especial ou dano de Alma vale mais que duas comuns.** A quinta rodada de simulação mostrou isso com mais força do que a terceira imaginava — oito ações de 4 Mestres de Gu não apenas "levam o grupo ao limite", **derrubam a vitória do grupo pra 11% no rank 3**, enquanto as mesmas oito ações vindas de 2 Mestres + uma Horda seguem ganháveis com folga (93%, número da terceira rodada, não retestado). O que machuca não é rolar mais dados, é **rolar dados que a RD não come e que custam a ação do jogador** — e a quinta rodada mediu esse efeito maior do que se pensava. Ver o achado no bloco acima.

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

**Ancião Renegado (Chefe, rank 3)** — VIT 252 (`63 × M`, M 4), Defesa 18, RD 8 (Gu do Dossel Celestial sustentado), dois ataques por rodada: Gu do Cristal de Gelo (`4d10`, aplica Lentidão) ou golpe melee `4d12+FOR` (arma média + 2 Níveis do Gu de Força ativo). Ignora a primeira Lentidão/Confuso sofrida na cena.

### Imortais (rank 6+) — some a densidade de Marca

Um Imortal não se descreve só pelo rank. Declare **rank + nível de domínio no Caminho principal** (ver [[☯️ Marcas de Dao|Marcas de Dao]]) — é o nível de domínio que diz quantos Níveis de Dano ele soma nos Gu do Caminho dele, e é isso que decide se a luta é difícil ou impossível.

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
