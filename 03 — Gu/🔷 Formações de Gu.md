---
tags:
  - regra
  - gu
aliases:
  - Formações de Gu
escopo: sistema
---

# 🔷 Formações de Gu

Um [[⚡ Golpes Matadores|Golpe Matador]] é vários Gu agindo como uma jogada. Uma **Formação** é vários Gu agindo como um **lugar**. Em vez de empurrar o núcleo na Escada de Dano por uma rodada, a formação prende o efeito no chão e o mantém ligado por dias, semanas ou séculos.

Três coisas nesta nota, em ordem de rank:

- **Formações Terrestres** — mortal, rank 3+. Matriz fixa num território.
- **Domínios de Campo de Batalha** — imortal, rank 6+. Marcas de Dao desdobradas no espaço durante um combate.
- **Casa-Gu tripulada** — uma estrutura que várias pessoas operam juntas. **Uma por campanha.**

---

# 🏯 Formações Terrestres

Uma matriz montada com Gu ancorados no solo de um território: **Gu-núcleo** (que definem o que a formação faz) mais **Gu de apoio** (que a sustentam e a escondem). É a infraestrutura defensiva de um clã, a armadilha de uma seita e o cofre de um Mestre de Gu.

**Requisito:** rank 3 ou superior pra fundar. O rank da formação é o rank do Gu-núcleo mais fraco dela.

## Os quatro graus

| Grau | Nome | Gu-núcleo | Gu de apoio | Raio coberto | Tempo de montagem |
|---|---|---|---|---|---|
| **I** | Cerco | 1 | 2 | 30 m | 1 hora |
| **II** | Recinto | 2 | 4 | 200 m | 6 horas |
| **III** | Domínio | 3 | 8 | 1 km | 3 dias |
| **IV** | Território | 4 | 16 | 10 km | 3 semanas |

**A montagem é ininterrupta.** Interromper (combate no local, um núcleo movido, o fundador ferido) perde metade dos Gu de apoio já assentados — eles morrem — e o tempo recomeça do zero. É por isso que ninguém monta uma formação de grau III em território disputado sem alguém segurando o perímetro.

**Cada Gu-núcleo escolhe uma função** da tabela abaixo, e a formação faz todas as funções dos núcleos que tiver. Uma formação de grau III com três núcleos pode ser Detecção + Supressão + Armadilha, ou três núcleos de Defesa empilhados (e aí a RD não empilha — vale a regra de [[⚔️ Combate|Combate]]: a maior mais metade da segunda).

## O que uma formação faz

Nas contas abaixo, **`M`** é o Multiplicador de Rank da formação (tabela de [[⚔️ Combate|Combate]]) e **`G`** é o grau (I=1 a IV=4).

| Função | Efeito dentro do raio |
|---|---|
| **Defesa de área** | Todos os defensados ganham **RD `2 × M`**. Ataques vindos de fora do raio sofrem **−2 no acerto**. Atravessar a fronteira à força exige teste de FOR ou VON, **CD `10 + 2G + rank da formação`** — falhou, não passou e leva `1d6 × M` de dano |
| **Detecção** | O fundador sabe posição, rank aproximado e número de Gu ativos de tudo que está dentro. Furtividade contra a formação: **DES vs. CD `10 + 2G + rank da formação`**. A informação chega ao fundador com atraso de `4 − G` horas se ele estiver fora do raio |
| **Supressão** | Gu de rank **igual ou inferior** ao da formação custam **o dobro** pra ativar (só pra quem o fundador não autorizou). Gu de movimento de intrusos operam **1 rank abaixo** — o que derruba a Defesa deles pela conta padrão. Não afeta quem a formação reconhece |
| **Armadilha** | **Uma vez por cena**, a formação dispara o efeito do próprio Gu-núcleo contra uma zona escolhida na montagem: dano `(passo do núcleo) × M`, ou o efeito de controle dele com **CD `10 + VON do fundador + rank da formação`**. Recarrega em 24 horas |

**Uma formação não é um Gu ativo do fundador.** Ela está ancorada no solo, não na Abertura dele — não ocupa vaga no limite de `CON + rank` e não entra na Manutenção por rodada. É isso que permite a um Mestre de Gu de rank 4 ter uma formação de grau II em casa **e** lutar com o arsenal completo.

## Manutenção — a fórmula quadrática, em cadência diária

A formação usa a mesma conta de [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]], só que o relógio é outro:

```
Manutenção da Formação = (Gu-núcleo + Gu de apoio)² × 5 de essência,
                          UMA VEZ POR DIA
```

| Grau | Gu na matriz | Custo diário | Em Pedras Primordiais (1 pedra = 40 de essência) |
|---|---|---|---|
| I | 3 | 45 | ~2 pedras/dia |
| II | 6 | 180 | ~5 pedras/dia |
| III | 11 | 605 | ~16 pedras/dia |
| IV | 20 | **2.000** | **50 pedras/dia** |

**Quem paga:** qualquer fonte de essência ancorada — o fundador em reclusão, um veio de essência natural, um tesouro de Pedras Primordiais, ou um turno de discípulos alimentando a matriz. Ver [[💠 Economia das Pedras Primordiais|Economia das Pedras Primordiais]].

> **Calibragem contra a economia.** Uma Pedra Primordial sustenta **uma família de três pessoas por um mês**. Então: um grau I (2 pedras/dia) é despesa de um cultivador individual bem estabelecido; um grau III (16/dia) é o orçamento de uma família forte dentro de um clã; e um **grau IV (50/dia ≈ 1.500 pedras/mês) é o orçamento inteiro de um clã grande**, sustentável apenas por quem controla um Ponto de Origem. Isso é de propósito: formações de grau IV são propriedade de potências, e um grupo de jogadores que tomar uma vai descobrir que **manter** é mais difícil que conquistar.

**Formação sem pagamento** entra em Dormência ao fim do dia: nenhuma função opera, mas os Gu não morrem. Sete dias seguidos em Dormência e os Gu de apoio começam a morrer de fome (1 por dia — ver [[🍖 Sustento e Alimento|Sustento e Alimento]]).

### Sobrecarga — puxar a formação pra dentro do combate

Uma vez por cena, o fundador **dentro do raio** pode sobrecarregar a formação: ela passa a operar **um grau acima** (raio, CDs e RD da linha seguinte) por uma cena inteira.

Durante a sobrecarga, a formação **deixa de ser infraestrutura e vira Gu ativo**: conta como `G + 1` Gu sustentados na Manutenção por rodada do fundador **e** ocupa esse tanto de vagas no limite de `CON + rank` dele. Se ele não tiver as vagas, não pode sobrecarregar.

Isso é o que faz uma invasão a uma formação virar decisão dos dois lados: o defensor pode transformar a casa em arma, mas só desligando quase tudo que ele mesmo carrega.

## 🔨 Como se quebra uma formação

Isto é uma **cena de invasão inteira**, com quatro etapas. Escreva os núcleos no mapa antes da sessão.

### 1. Encontrar os núcleos

Cada núcleo está enterrado, embutido numa rocha, escondido dentro de uma árvore ou plantado sob um piso. Um personagem dentro do raio pode procurar: **teste de AST, CD `12 + 2G`**, um teste por hora. Cada sucesso localiza **um** núcleo.

- Um Gu de detecção de rank igual ou superior ao da formação dá **vantagem**.
- **Falha por 5 ou mais alerta o fundador** — e se a formação tem núcleo de Detecção, ele já sabia desde que você entrou.
- **Núcleos falsos:** o defensor pode plantar **1 falso por grau**, gastando 1 Gu de apoio extra em cada. Um falso parece idêntico até ser destruído — e destruir um falso **não** rebaixa a formação, só queima o tempo e a posição do invasor.

### 2. Chegar até ele

A parte de jogo: guardas, terreno, a função de Armadilha da própria formação, e o fundador possivelmente sobrecarregando a matriz enquanto você cava. Não há teste único aqui — é a cena.

### 3. Destruir

| Estatística do núcleo | Valor |
|---|---|
| Vitalidade | `20 × M` |
| RD | `2 × M` |
| Defesa | **10** — é um objeto ancorado, não desvia |

**Cada núcleo destruído rebaixa a formação um grau:** raio, CDs, RD e funções descem uma linha, e o defensor escolhe qual função se perde. Destruir o **último** núcleo colapsa a matriz: todos os Gu de apoio morrem (não voltam, não se recuperam) e o fundador sofre **1 Ferimento**.

### 4. A alternativa sem invasão — arrombar pela essência

Quem tem tanque e nenhum tempo: despejar dentro do raio, numa única rodada, essência hostil igual a **três vezes a manutenção diária** da formação queima **um núcleo à escolha do mestre**. Custa **1 Ferimento** a quem despeja, e a essência sai do tanque dele ou de Pedras.

Contra um grau II (180/dia) são 540 de essência — caro mas viável pra um rank 4. Contra um grau IV são **6.000**, o que é território de Golpe Matador Coletivo ou de Imortal. A conta escala sozinha e o mestre não precisa de tabela extra.

## Formação e Supressão Regional

Uma formação montada **fora da região de refino** dos Gu que a compõem opera **um grau abaixo** — mesma lógica de [[🗺️ Supressão Regional|Supressão Regional]], aplicada à matriz inteira de uma vez. Reancorar a formação é reancorar cada Gu dela, em lote, pelas regras daquela nota.

É a razão mecânica pela qual exércitos não levam fortalezas junto, e pela qual invadir a casa de alguém é sempre pior do que emboscá-lo na estrada.

---

# 🌐 Domínios de Campo de Batalha

A versão imortal: em vez de ancorar Gu no solo ao longo de semanas, o Imortal **desdobra as próprias Marcas de Dao no espaço** durante o combate. O resultado não é uma parede — é uma região do mundo temporariamente reescrita, onde as leis do Caminho dele valem mais que as leis de fora.

> Um Domínio não mata ninguém. Ele **garante que a luta aconteça e que ninguém saia dela.** É a razão pela qual Imortais matam Imortais e o mundo não fica sabendo.

**Requisitos:** rank 6+, e nível de domínio **Mestre** (10.000+ Marcas naquele Caminho — ver [[☯️ Marcas de Dao|Marcas de Dao]]).

## O custo

```
Abrir     = selar 1% das suas Marcas do Caminho (mínimo 100) + 100 de Essência Imortal
Sustentar = 50 de Essência Imortal por rodada
            + o Domínio conta como 3 Gu sustentados na Manutenção quadrática (45/rodada)
```

**Marcas seladas não são gastas — mas também não são suas enquanto o Domínio estiver aberto.** Elas saem da contagem: um Mestre com 10.000 Marcas que sela 100 luta o combate inteiro com 9.900, o que não muda nada; um Grão-Mestre no piso exato de 50.000 que sela 500 **recua pro nível Mestre** e perde 1 Nível de Dano durante a própria luta que ele escolheu isolar.

**Se o Domínio for rompido por outro Imortal ou pela fronteira, 10% das Marcas seladas se perdem permanentemente.** Fechar por vontade própria ou por fim de duração devolve tudo.

## Raio e duração

```
Raio     = 10 metros × (Marcas do Caminho ÷ 1.000), máximo 1 km
Duração  = (Marcas do Caminho ÷ 2.000) rodadas, mínimo 5, máximo 20
```

| Nível de domínio | Marcas | Raio | Duração |
|---|---|---|---|
| Mestre | 10.000 | 100 m | 5 rodadas |
| Mestre alto | 40.000 | 400 m | 20 rodadas |
| Grão-Mestre | 50.000+ | 500 m – 1 km | 20 rodadas (teto) |

O Domínio fecha antes se a Essência Imortal acabar. Segurar além do tanque custa **1 Ferimento por rodada**, e o Imortal escolhe rodada a rodada se paga.

## O que ele bloqueia — e o que não bloqueia

| Coisa | Dentro do Domínio |
|---|---|
| **Teleporte e Gu de Espaço** | Gu de rank **inferior** ao do dono simplesmente não ativam. Rank igual ou superior exigem **VON CD `10 + VON do dono + rank do dono`** e custam o dobro. Falhou, a essência foi embora e você continua aqui |
| **Gu de movimento** (voo, velocidade, sombra) | Operam **2 ranks abaixo** dentro do raio. Continuam funcionando pra manobrar; não servem pra sair |
| **Sair pela borda** | Teste **oposto de VON** contra o dono. Sucesso atravessa e o Domínio se fecha atrás de você; falha custa a ação e `2d12 × M` de dano de fronteira |
| **Comunicação** | **Cortada por completo.** Gu de informação, mensageiros, marcas de alma, sinais visuais — nada sai, nada entra |
| **Socorro externo** | Ninguém de fora entra sem passar pela fronteira (mesmo teste da saída, contra o dono). Aliado que estava fora quando abriu, fica fora |
| **Percepção externa** | Quem está de fora não vê, não ouve e não sente o que acontece dentro. O mundo vê um borrão parado |
| **Ataque, defesa, cura, transformação** | **Nada disso é bloqueado.** O Domínio isola — ele não desarma. O alvo continua com o arsenal inteiro; só não tem pra onde ir |

## Como o alvo rompe — quatro saídas, todas escritas

**1. Força bruta na fronteira.** A fronteira tem `Marcas do Caminho ÷ 10` de Vitalidade, **até o teto de 5.000**, e **RD `2 × M`** do rank do dono. Contra um Mestre de 10.000 Marcas são **1.000 de Vitalidade** — trabalho de Golpe Matador, não de ataque avulso. Zerada, a fronteira abre um rombo permanente e o Domínio termina.

> **Por que o teto de 5.000 existe.** Sem ele, a fórmula escala com a contagem de Marcas e um Grão-Mestre de 150.000 teria uma fronteira de 15.000 de Vitalidade — força bruta deixaria de ser uma saída, e o Domínio viraria a única regra do sistema que **remove fuga, socorro e comunicação sem contrapartida jogável**. Isso contradiz frontalmente o pilar de sobreviventes ("fugir tem regra própria", ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]]): sempre tem que dar pra sacrificar alguma coisa e sair. Com o teto, um Domínio de Venerável continua sendo pesadelo, mas um grupo determinado com um Golpe Matador Coletivo ainda enxerga a porta.

**2. Domínio contra Domínio.** Outro Imortal abre o dele por cima. **Teste oposto de Marcas no Caminho respectivo**: quem tiver mais vence, e o perdedor perde 10% das Marcas que selou. Se a diferença entre os dois for **menor que 10%**, os dois Domínios colapsam juntos e ninguém sela nada de volta.

**3. A Brecha.** Um Domínio **é um Golpe Matador de campo** e herda a regra: **nenhum Domínio pode ser registrado sem Brecha declarada** ([[⚡ Golpes Matadores|Golpes Matadores]]), nas mesmas quatro categorias. Quem conhece a Brecha e a explora faz o **raio cair pela metade** e o **custo por rodada dobrar** — o que normalmente encerra o Domínio em duas ou três rodadas. Descobrir a Brecha alheia segue o mesmo procedimento: AST CD 14, três sucessos antes de duas falhas, tendo visto o Domínio ao menos uma vez.

**4. O fio combinado antes.** Comunicação combinada **antes** do combate atravessa: um sinal pré-acordado ("se eu não voltar em uma hora"), um Gu Imortal de ancoragem deixado com um aliado, um horário marcado. O Domínio corta mensagens novas, não planos velhos. É a recompensa mecânica de [[🕵️ Preparação e Informação|Preparação e Informação]] contra a ferramenta mais opressiva do jogo, e é deliberada.

---

# 🚢 Casa-Gu tripulada

Uma estrutura refinada — barco, carruagem, fortaleza móvel, besta oca — que **não funciona sozinha**. Ela tem três estações, e o que ela consegue fazer depende de quantas estão ocupadas por gente que sabe operá-las.

**Uma Casa-Gu por campanha.** Não é sugestão: é a regra. Duas Casas viram contabilidade de frota, e a cena de "todo mundo dentro da mesma máquina, cada um numa função" perde inteiramente o sentido quando existe uma segunda máquina.

## As três estações

O **rank da Casa** é definido no refino, tipicamente o rank do fundador.

| Estação | Atributo | Custo por rodada | O que faz |
|---|---|---|---|
| **Ataque** | VON | 40 × modificador de Caminho | Um ataque por rodada: `d20 + VON do operador + (rank operante + 2) + rank operante`. Dano: **passo +2 na Escada × M do rank operante** |
| **Defesa** | CON | 40 | **RD `3 × M`** do rank operante pra tudo e todos dentro. A Casa tem Vitalidade `40 × M` e Defesa `10 + rank da Casa` |
| **Movimento** | DES | 40 | A Casa se desloca. Concede Defesa `10 + DES do operador + rank operante` à estrutura, e permite tentar Fuga ([[🏃 Fuga e Perseguição\|Fuga e Perseguição]]) com o teste do operador |

## O rank operante

```
Rank operante = rank da Casa − (número de estações vazias)
```

| Estações ocupadas | Rank operante | Leitura |
|---|---|---|
| 3 | **rank pleno** | A Casa como foi refinada |
| 2 | rank − 1 | Metade do dano (M cai pela metade), −1 em acerto e Defesa |
| 1 | rank − 2 | Um quarto do dano. Funciona, mal |
| 0 | — | **Objeto inerte.** Não se move, não atira, não defende |

O rank operante vale pras **três** estações ao mesmo tempo, não só pras vazias. Uma Casa de rank 5 com duas estações ocupadas atira como rank 4 — o dano cai de `× 16` pra `× 8`. **A máquina inteira desanda junta**, e é isso que torna tirar um tripulante de cena uma jogada tática de verdade contra o grupo.

## Quem tripula e o que paga

- **Um PJ opera uma estação por rodada.** Trocar de estação gasta a ação de movimento da rodada.
- **Cada operador paga os 40 de essência da própria estação**, do próprio tanque, por rodada. Não é o fundador que banca todo mundo.
- **O fundador, se estiver dentro da Casa,** paga a Manutenção de Sustentação como se a Casa fossem **3 Gu sustentados** (45/rodada) — mesmo que ele não esteja operando estação nenhuma. A Casa está ancorada na Abertura dele.
- **NPCs podem tripular**, mas o atributo deles nunca conta acima de **+1** naquela estação. A Casa responde a quem a conhece — e é por isso que encher de discípulos não substitui os PJs.

**Custo total de uma Casa em combate:** 45 (fundador) + 3 × 40 (estações) = **165 de essência por rodada**, dividida entre quatro pessoas. Contra o teto de regeneração de 100/rodada ([[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]]), isso é sustentável por um grupo que se organizou e ruinoso pra um que improvisou. É o ponto.

## Como se derruba uma Casa

**Por fora:** zerar a Vitalidade `40 × M`. Quando cai, quem estiver dentro leva **metade do dano excedente**.

**Por dentro:** uma Casa é uma Formação Terrestre móvel de grau III — ela tem **três núcleos, um por estação**, com as estatísticas de núcleo da primeira seção (`20 × M` de Vitalidade, RD `2 × M`, Defesa 10). Destruir um núcleo **desliga aquela estação** e reduz o rank operante como se ela estivesse vazia.

Isto existe pra tornar a **abordagem** uma cena: em vez de trocar dano com a estrutura por seis rodadas, o inimigo inteligente entra, procura o núcleo do Movimento e a Casa vira um alvo parado. Um grupo que descobre isso na pele nunca mais deixa o corredor interno desguarnecido.

## Como criar uma Casa (mestre)

1. Escolha o rank e a forma (barco de guerra do clã, carruagem-besta, torre andante).
2. Defina o **passo inicial** do ataque na Escada e a natureza do dano — a estação de Ataque usa o passo +2 por padrão, mas uma Casa especializada pode entrar em +3 e perder RD na de Defesa em troca.
3. Escreva onde estão os três núcleos por dentro. Desenhe a planta antes da sessão em que ela será abordada.
4. Escreva o que ela **come** ([[🍖 Sustento e Alimento|Sustento e Alimento]]) — uma Casa parada ainda é uma criatura, e uma Casa faminta é um gancho de arco.
