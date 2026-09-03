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

> [!example] Um exemplo, do início ao fim
> As três seções abaixo vivem em escalas diferentes (grau mortal, rank Imortal, tripulação) e raramente aparecem juntas na mesma cena — mas para não deixar cada subsistema abstrato, este exemplo segue **o mesmo Mestre de Gu genérico** ao longo da carreira: monta uma Formação Terrestre para defender o próprio clã ainda mortal, décadas depois abre um Domínio de Campo de Batalha ao virar Imortal, e por fim comanda a Casa-Gu que o clã dele possui. Cada seção retoma o fio num bloco **"Exemplo, parte N"**.

---

# 🏯 Formações Terrestres

*Subsistema 1 de 3 — mortal, rank 3+. Termina em "Formação e Supressão Regional", logo antes de Domínios de Campo de Batalha abaixo.*

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

> [!example]+ Exemplo, parte 1 — montando a Formação Terrestre
> Ainda mortal, rank 3, o Mestre de Gu decide proteger o pátio principal do clã. Escolhe **Grau II — Recinto**: 2 Gu-núcleo + 4 Gu de apoio, 200 m de raio, 6 horas de montagem ininterrupta. Um núcleo vira **Defesa de área**, o outro **Detecção** — juntos, a formação blinda quem está dentro (RD `2×M`) e avisa o fundador de quem se aproxima. Manutenção diária: `(2+4)² × 5 = 180` de essência, ~5 Pedras Primordiais/dia, pagas por um veio de essência natural que corre sob o pátio.

**Cada Gu-núcleo escolhe uma função** da tabela abaixo, e a formação faz todas as funções dos núcleos que tiver. Uma formação de grau III com três núcleos pode ser Detecção + Supressão + Armadilha, ou três núcleos de Defesa empilhados (e aí a RD não empilha — vale a regra de [[⚔️ Combate|Combate]]: vale só a maior, e a segunda não soma nada — decisão 223).

## O que uma formação faz

Nas contas abaixo, **`M`** é o Multiplicador de Rank da formação (tabela de [[⚔️ Combate|Combate]]) e **`G`** é o grau (I=1 a IV=4).

| Função | Efeito dentro do raio |
|---|---|
| **Defesa de área** | Todos os defensados ganham **RD `2 × M`**. Ataques vindos de fora do raio sofrem **−2 no acerto**. Atravessar a fronteira à força exige teste de FOR ou VON, **CD `10 + 2G + rank da formação`** — falhou, não passou e leva **`M d6`** de dano (rank 3 = `4d6`) |
| **Detecção** | O fundador sabe posição, rank aproximado e número de Gu ativos de tudo que está dentro. Furtividade contra a formação: **DES vs. CD `10 + 2G + rank da formação`**. A informação chega ao fundador com atraso de `4 − G` horas se ele estiver fora do raio |
| **Supressão** | Gu de rank **igual ou inferior** ao da formação custam **o dobro** pra ativar (só pra quem o fundador não autorizou). Gu de movimento de intrusos operam **1 rank abaixo** — o que derruba a Defesa deles pela conta padrão. Não afeta quem a formação reconhece |
| **Armadilha** | **Uma vez por cena**, a formação dispara o efeito do próprio Gu-núcleo contra uma zona escolhida na montagem: dano **`M d(dado do Caminho do núcleo, já com o passo dele)`**, com o `M` da **formação** e não o do Gu, ou o efeito de controle dele com **CD `10 + VON do fundador + rank da formação`**. Recarrega em 24 horas |

**Uma formação não é um Gu sustentado do fundador.** Ela está ancorada no solo, não na Abertura dele — não ocupa nenhuma das **3 vagas** de sustentação e não entra na Manutenção por rodada. É isso que permite a um Mestre de Gu de rank 4 ter uma formação de grau II em casa **e** lutar com o arsenal completo.

## Manutenção — a fórmula quadrática, em cadência diária

A formação usa a mesma conta de [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]], só que o relógio é outro:

```
Manutenção da Formação = (Gu-núcleo + Gu de apoio)² × 5 de essência,
                          UMA VEZ POR DIA
```

| Grau | Gu na matriz | Custo diário | Em Pedras Primordiais (1 pedra ≈ 20 de essência — a taxa única do sistema, ver [[🧩 Refino e Precificação]]) |
|---|---|---|---|
| I | 3 | 45 | ~2–3 pedras/dia |
| II | 6 | 180 | ~9 pedras/dia |
| III | 11 | 605 | ~30 pedras/dia |
| IV | 20 | **2.000** | **100 pedras/dia** |

**Quem paga:** qualquer fonte de essência ancorada — o fundador em reclusão, um veio de essência natural, um tesouro de Pedras Primordiais, ou um turno de discípulos alimentando a matriz. Ver [[💠 Economia das Pedras Primordiais|Economia das Pedras Primordiais]].

> **Calibragem contra a economia.** Uma Pedra Primordial sustenta **uma família de três pessoas por um mês**. Então: um grau I (~2–3 pedras/dia) é despesa de um cultivador individual bem estabelecido; um grau III (~30/dia ≈ 900 pedras/mês) já é orçamento de um clã médio inteiro; e um **grau IV (100/dia = 3.000 pedras/mês) engole o orçamento de um clã grande com folga**, sustentável apenas por quem controla um Ponto de Origem ou um veio de essência natural. Isso é de propósito: formações de grau IV são propriedade de potências, e um grupo de jogadores que tomar uma vai descobrir que **manter** é mais difícil que conquistar.

**Formação sem pagamento** entra em Dormência ao fim do dia: nenhuma função opera, mas os Gu não morrem. Sete dias seguidos em Dormência e os Gu de apoio começam a morrer de fome (1 por dia — ver [[🍖 Sustento e Alimento|Sustento e Alimento]]).

### Sobrecarga — puxar a formação pra dentro do combate

Uma vez por cena, o fundador **dentro do raio** pode sobrecarregar a formação: ela passa a operar **um grau acima** (raio, CDs e RD da linha seguinte) por uma cena inteira.

Durante a sobrecarga, a formação **deixa de ser infraestrutura e vira Gu sustentado**: **ocupa `G + 1` das vagas de sustentação do fundador**. Se ele não tiver as vagas, não pode sobrecarregar.

Com o teto de sustentação em **3**, a conta fica dura de propósito:

| Grau sobrecarregado | Vagas que come | O que sobra do fundador |
|---|---|---|
| **I** | 2 | Uma vaga. Ele fica com **um** Gu de combate ligado |
| **II** | 3 | **Nenhuma.** Ele desliga tudo e vira o operador da casa |
| **III ou mais** | 4+ | **Impossível** sem Gu de multitarefa ou Força de Alma de Cem Homens |

Isso é o que faz uma invasão a uma formação virar decisão dos dois lados: o defensor pode transformar a casa em arma, mas o preço é **ele mesmo ficar nu** enquanto a casa luta por ele. E é a razão de existir de um grande fundador de formações comprar linhas de atenção antes de comprar mais Gu de ataque: a sobrecarga de grau III é literalmente a coisa que ele não consegue fazer sozinho.

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

> [!tip] Formação de Cálculo Estelar — ideia de ativo de facção, não regra nova
> Uma formação de grau IV+ pode ser ampliada pra cobrir uma região inteira como rede viva de inteligência: terreno, clima, movimento de facções e localização de indivíduos, tudo visível de um único ponto de comando. Poder de combate próprio é básico — o valor real é **coordenação centralizada**. Efeito colateral de mesa: a formação expõe sem querer quem precisa de quê, e vira mercado natural de trocas entre os membros da facção que a possui. Ideia pronta pra um PJ Venerável construir ou disputar, não mecânica nova (🔧 adaptado — *Origem: digest 18, Cap. 2283, 2293*).

---

# 🌐 Domínios de Campo de Batalha

*Subsistema 2 de 3 — Imortal, rank 6+. Termina em "Como o alvo rompe", logo antes de Casa-Gu tripulada abaixo.*

A versão imortal: em vez de ancorar Gu no solo ao longo de semanas, o Imortal **desdobra as próprias Marcas de Dao no espaço** durante o combate. O resultado não é uma parede — é uma região do mundo temporariamente reescrita, onde as leis do Caminho dele valem mais que as leis de fora.

> Um Domínio não mata ninguém. Ele **garante que a luta aconteça e que ninguém saia dela.** É a razão pela qual Imortais matam Imortais e o mundo não fica sabendo.

**Requisitos:** rank 6+, e nível de domínio **Mestre** naquele Caminho (ver [[☯️ Marcas de Dao|Marcas de Dao]]).

> [!important] No rank 6, isso é o padrão dos fortes — não rotina, mas não é raridade histórica
> O teto de Marcas do rank 6 é 9.999 **no total** (decisão 109), e Mestre pede
> 10.000 naquele Caminho. Pela contagem, portanto, **nenhum rank 6 alcança
> Mestre** por acúmulo real — a via é a **regra do gênio pobre** (ver
> [[☯️ Marcas de Dao]]): um rank 6 denso, real Pequeno Feito, que empilhe **um**
> feito de compreensão reconhecido opera como Mestre e abre Domínios; com
> **dois** feitos empilhados, opera como Grão-Mestre. Do **rank 7 em diante** a
> contagem normal basta.
>
> Isso é canônico e comum entre os rank 6 fortes do romance, não exceção
> histórica: *"strength path and blood path were at grandmaster attainment
> realm... he was only rank six"* é o próprio Fang Yuan; a Espadachim You Lan,
> "famosa" e rank 6 com Grão-Mestre em Espada, é descrita como notável, não como
> única na história. Ver [[📚 Fonte Primária — O Romance]].

## O custo

```
Abrir     = selar 1% das suas Marcas do Caminho (mínimo 100) + 100 de Essência Imortal
Sustentar = 50 de Essência Imortal por rodada
```

**Marcas seladas não são gastas — mas também não são suas enquanto o Domínio estiver aberto.** Elas saem da contagem: um Mestre com 10.000 Marcas que sela 100 luta o combate inteiro com 9.900, o que não muda nada; um Imortal no piso exato de 50.000 Marcas que sela 500 **cai de faixa e perde 1 Nível de Potência** durante a própria luta que ele escolheu isolar.

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

> [!example]+ Exemplo, parte 2 — abrindo o Domínio de Campo de Batalha
> Décadas depois, o mesmo Mestre de Gu já é Imortal de rank 6, com **10.000 Marcas** no próprio Caminho e domínio de **Mestre** — dois números diferentes, e é de propósito (decisão 254). Num duelo contra outro Imortal, abre o Domínio: sela 100 Marcas (1%, o mínimo) + gasta 100 de Essência Imortal pra erguê-lo, e paga 50 EI por rodada de sustento. O Domínio cobre 100 m por 5 rodadas — o bastante pra garantir que o duelo aconteça sem interrupção externa e sem que o oponente fuja antes da hora.

## O que ele bloqueia — e o que não bloqueia

| Coisa | Dentro do Domínio |
|---|---|
| **Teleporte e Gu de Espaço** | Gu de rank **inferior** ao do dono simplesmente não ativam. Rank igual ou superior exigem **VON CD `10 + VON do dono + rank do dono`** e custam o dobro. Falhou, a essência foi embora e você continua aqui |
| **Gu de movimento** (voo, velocidade, sombra) | Operam **2 ranks abaixo** dentro do raio. Continuam funcionando pra manobrar; não servem pra sair |
| **Sair pela borda** | Teste **oposto de VON** contra o dono. Sucesso atravessa e o Domínio se fecha atrás de você; falha custa a ação e **`(2 × M) d12`** de dano de fronteira — o dobro do pool do rank do dono (rank 6 = `128d12`, média 832) |
| **Comunicação** | **Cortada por completo.** Gu de informação, mensageiros, marcas de alma, sinais visuais — nada sai, nada entra |
| **Socorro externo** | Ninguém de fora entra sem passar pela fronteira (mesmo teste da saída, contra o dono). Aliado que estava fora quando abriu, fica fora |
| **Percepção externa** | Quem está de fora não vê, não ouve e não sente o que acontece dentro. O mundo vê um borrão parado |
| **Ataque, defesa, cura, transformação** | **Nada disso é bloqueado.** O Domínio isola — ele não desarma. O alvo continua com o arsenal inteiro; só não tem pra onde ir |

## Como o alvo rompe — quatro saídas, todas escritas

**1. Força bruta na fronteira.** A fronteira tem `Marcas do Caminho ÷ 10` de Vitalidade, **até o teto de 5.000**, e **RD `2 × M`** do rank do dono. Contra um Mestre de 10.000 Marcas são **1.000 de Vitalidade** — trabalho de Golpe Matador, não de ataque avulso. Zerada, a fronteira abre um rombo permanente e o Domínio termina.

> **Por que o teto de 5.000 existe.** Sem ele, a fórmula escala com a contagem de Marcas e um Imortal com 150.000 Marcas teria uma fronteira de 15.000 de Vitalidade — força bruta deixaria de ser uma saída, e o Domínio viraria a única regra do sistema que **remove fuga, socorro e comunicação sem contrapartida jogável**. Isso contradiz frontalmente o pilar de sobreviventes ("fugir tem regra própria", ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]]): sempre tem que dar pra sacrificar alguma coisa e sair. Com o teto, um Domínio de Venerável continua sendo pesadelo, mas um grupo determinado com um Golpe Matador Coletivo ainda enxerga a porta.

**2. Domínio contra Domínio.** Outro Imortal abre o dele por cima. **Teste oposto de Marcas no Caminho respectivo**: quem tiver mais vence, e o perdedor perde 10% das Marcas que selou. Se a diferença entre os dois for **menor que 10%**, os dois Domínios colapsam juntos e ninguém sela nada de volta.

**3. A Brecha.** Um Domínio **é um Golpe Matador de campo** e herda a regra: **nenhum Domínio pode ser registrado sem Brecha declarada** ([[⚡ Golpes Matadores|Golpes Matadores]]), nas mesmas quatro categorias. Quem conhece a Brecha e a explora faz o **raio cair pela metade** e o **custo por rodada dobrar** — o que normalmente encerra o Domínio em duas ou três rodadas. Descobrir a Brecha alheia segue o mesmo procedimento: AST CD 14, três sucessos antes de duas falhas, tendo visto o Domínio ao menos uma vez.

**4. O fio combinado antes.** Comunicação combinada **antes** do combate atravessa: um sinal pré-acordado ("se eu não voltar em uma hora"), um Gu Imortal de ancoragem deixado com um aliado, um horário marcado. O Domínio corta mensagens novas, não planos velhos. É a recompensa mecânica de [[🕵️ Preparação e Informação|Preparação e Informação]] contra a ferramenta mais opressiva do jogo, e é deliberada.

---

# 🚢 Casa-Gu tripulada

*Subsistema 3 de 3 — qualquer rank, refinada como estrutura própria. Uma por campanha.*

Uma estrutura refinada — barco, carruagem, fortaleza móvel, besta oca — que **não funciona sozinha**. Ela tem três estações, e o que ela consegue fazer depende de quantas estão ocupadas por gente que sabe operá-las.

**Uma Casa-Gu por campanha.** Não é sugestão: é a regra. Duas Casas viram contabilidade de frota, e a cena de "todo mundo dentro da mesma máquina, cada um numa função" perde inteiramente o sentido quando existe uma segunda máquina.

## As três estações

O **rank da Casa** é definido no refino, tipicamente o rank do fundador.

| Estação | Atributo | Custo por rodada | O que faz |
|---|---|---|---|
| **Ataque** | VON | 40 × modificador de Caminho | Um ataque por rodada: `d20 + VON do operador + (rank operante + 2) + rank operante`. Dano: **`M d(dado do Caminho da Casa) com +2 Níveis`**, `M` do **rank operante** — uma Casa de Caminho d8 atira `M d12`; uma de Caminho d12 atira `M d12 + 2 × M` |
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

O rank operante vale pras **três** estações ao mesmo tempo, não só pras vazias. Uma Casa de rank 5 com duas estações ocupadas atira como rank 4 — o pool cai de **16 dados para 8**, e a RD e a Vitalidade dela caem junto. **A máquina inteira desanda junta**, e é isso que torna tirar um tripulante de cena uma jogada tática de verdade contra o grupo.

> [!example]+ Exemplo, parte 3 — comandando a Casa-Gu do clã
> Nessa altura da campanha, o clã do mesmo Mestre de Gu tem a única Casa-Gu da mesa: um barco de guerra de rank 5. Com as três estações ocupadas por discípulos, ela opera em rank pleno (`M=16`): a estação de Ataque dispara o pool cheio, a de Defesa dá RD `3×16 = 48`. Um dos discípulos cai em combate e a estação de Movimento fica vazia — rank operante cai pra 4 (`M=8`): o pool de Ataque cai de 16 dados pra 8, a RD e a Vitalidade caem junto, e a Casa não consegue mais tentar Fuga. A máquina inteira desanda com um só tripulante a menos.

## Quem tripula e o que paga

- **Um PJ opera uma estação por rodada.** Trocar de estação gasta a ação de movimento da rodada.
- **Cada operador paga os 40 de essência da própria estação**, do próprio tanque, por rodada. Não é o fundador que banca todo mundo.
- **O fundador paga a manutenção diária da própria Casa** (`(núcleo + apoio)² × 5`, a fórmula desta nota) mesmo que não esteja operando estação nenhuma. A Casa está ancorada na Abertura dele e não deixa de comer porque ele cruzou os braços. **É o único custo que ela cobra dele** — não há taxa por rodada por cima disso.
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

## 🌌 A versão imortal — Casa-Gu Imortal (rank 6+)

Símbolo de grande potência: *"toda super-facção possui uma."* Muda em três coisas em relação à versão mortal:

- **Cinco estações, não três** — Ataque, Defesa, Movimento e mais **Sensores** (detecção/comunicação à distância) e **Núcleo de Suporte** (cura ou reforço de essência pra tripulação). O rank operante se calcula igual: `rank da Casa − estações vazias`, agora sobre cinco.
- **Essência é acelerador, não só penalidade.** Além do custo fixo por estação, cada operador pode **despejar essência extra na própria rodada**: cada `20 × M` adicional dá **+1 Nível de Dano** (Ataque) ou **+1 RD** (Defesa), sem teto além do próprio tanque. Mais gente competente a bordo não só evita penalidade — **arma a Casa de verdade**.
- **Casco de blindagem ablativa.** Gu mortais acoplados ao casco absorvem dano primeiro e **regeneram entre cenas** enquanto os núcleos-Gu Imortais internos estiverem intocados — a Casa só morre de verdade quando alguém **toma um núcleo**, não por atrito continuado de fora.
- **Livro-caixa embutido.** A própria Casa registra quanta essência cada tripulante despejou nela — resolve a divisão de espólio de uma campanha inteira **dentro da ficção**, sem planilha de mesa.
- **Manobra de aríete**, exclusiva do rank 6+: a estação de Movimento pode arremessar a Casa inteira contra um alvo — dano `Vitalidade da Casa ÷ 10` (arredondado pra baixo) em vez do ataque normal daquela rodada, ignorando RD do alvo se ele for menor que a Casa.

Tudo o mais (como se deriva, como se aborda, como se cria) segue igual à versão mortal — só a escala e as cinco estações mudam.

---

## 📕 A Casa é o único lugar do mundo onde a essência de vários Imortais vira uma coisa só

Este é o corolário que fecha o circuito aberto pela regra de que **essência imortal é pessoal e intransferível** ([[💠 Economia das Pedras Primordiais]]). Ninguém empresta combustível a ninguém — **exceto aqui**.

> [!important] A Casa absorve essência de **qualquer** origem, e a obra trata isso como a definição da categoria
> 📕 *"Immortal Gu Houses could absorb immortal essence of others"* — e a razão de existirem é **integrar o poder de um grupo de imortais em um só**.
>
> **Isso dá à Casa o papel que nada mais no sistema ocupa: ela é a única razão mecânica para um grupo de Imortais agir junto.** Fora dela, cada um queima do próprio tanque e ninguém socorre ninguém.
>
> **E dá destino ao espólio que não tem uso.** As contas de essência tomadas de um Imortal morto são inertes na mão de qualquer personagem ([[⛓️ Espólio de Gu Imortal]]) — **dentro de uma Casa, são combustível.** É o único destino que elas têm no mundo inteiro.

**A trava, e ela existe para o saque não virar abastecimento.** A Casa queima essência de terceiros até um **teto por cena**: até `2 × rank da Casa` em contas por cena de combate. O excedente fica guardado no reservatório e serve nas cenas seguintes, mas **nunca numa só**. Sem esse teto, um grupo que caça Imortais nunca mais fica sem gasolina — e o ponto de a essência ser pessoal era justamente que combustível é escasso.

> [!note] Três detalhes canônicos que valem a pena
> **O combustível de uma Casa se conta em contas, não em porcentagem** — e isso é uma barra pronta para a mesa. 📕 Um Pavilhão de rank 7 foi deixado com **vinte contas**; anos de operação depois **restavam cinco**, e a dona diz que com isso não vira batalha nenhuma. **Uma Casa herdada vem com um número de contas, e esse número é o relógio do arco.**
>
> **O livro-caixa embutido é canônico** — a Casa registra quanta essência cada um pôs dentro. Esta nota já tinha a regra e agora tem a procedência: é a peça que transforma cooperação entre Imortais em contabilidade, e contabilidade em intriga.
>
> **Nem toda Casa tem Gu de Permanência.** 📕 Existe uma classe cujo núcleo são **golpes matadores imortais** em vez de um Gu central — *"the essence of an Immortal Gu House was immortal killer moves"*. Para essas, a regra de "matar o Gu de Permanência apaga a Casa" **não vale**, e é exatamente o que o mestre quer quando precisa de uma Casa que não caia num tiro certeiro.
