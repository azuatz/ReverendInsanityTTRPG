---
tags:
  - regra
  - cultivo
aliases:
  - Materialização e Alquimia Interna
escopo: sistema
---

# ⚗️ Materialização e Alquimia Interna

Um cultivador parado **desperdiça poder**. A Abertura enche, o teto de regeneração impede que ela seja esvaziada rápido o bastante em combate, e o que sobra evapora. As Marcas de Dao acima do teto do rank não só evaporam — elas **corroem** ([[☯️ Marcas de Dao|Retrocesso de Marca]]).

Esta nota é a válvula: como transformar excedente de essência, de Força de Alma e de Marcas em **matéria vendável**, e como isso vira renda contínua de uma [[🗝️ Terra Abençoada|Terra Abençoada]].

> **A tese de design da nota inteira:** materializar é **ruim de câmbio e bom de oportunidade**. Você perde ~70% do valor no processo. Vale mesmo assim, porque a alternativa era perder 100%.

---

## 1. Condensação Elemental — essência vira matéria

### 1.1 A Carga de Excedente

Toda condensação se mede em **Cargas**. Uma Carga = **100 pontos de Verdadeira Essência canalizados**.

Um dia inteiro de reclusão dedicada rende:

```
Cargas por dia = (Essência máxima ÷ 100), arredondado pra baixo, × modificador de condição
```

| Condição *(mesma escala do [[🏛️ Arquitetura do Sistema\|teto de regeneração]])* | Modificador |
|---|---|
| Hostil ao Caminho (sol forte pra um Yin, chuva pra um de Fogo) | **×0,5** |
| Padrão | **×1** |
| Favorável ao Caminho (luar, veia elemental, terreno do próprio elemento) | **×1,5** |
| Ideal ([[🌙 Caminho da Lua\|lua cheia a céu aberto]], coração de vulcão, veia de essência do elemento) | **×2** |

Um rank 3 Pico com 1.920 de Essência máxima rende **19 Cargas/dia** em condição padrão, **38** em condição ideal.

> **Por que a taxa vem do tanque e não do teto de 100/rodada.** O teto de regeneração é regra de **combate** — ele existe pra impedir que um tanque grande vire munição infinita numa luta. Fora de combate, o limitante é o tamanho do tanque e o tempo de reclusão. E é exatamente por causa do teto que o excedente existe: quem tem tanque enorme **não consegue gastá-lo** na velocidade em que ele enche. A Condensação é o ralo que faltava.

**Cargas não se estocam.** Elas existem dentro do lote que você começou. Interromper a reclusão antes de completar o lote perde tudo que foi canalizado.

### 1.2 O procedimento

| | |
|---|---|
| **Teste** | `d20 + AST + treino de Refino` ([[💪 Atributos\|Atributos]]) — **um teste por lote**, rolado ao completar as Cargas |
| **CD** | Pela linha do material na tabela abaixo (12 / 15 / 18 / 21 / 24, a mesma escada de [[🧩 Refino e Precificação\|Refino]]) |
| **Custo** | As Cargas listadas, integralmente gastas antes de rolar |
| **Tempo** | Cargas ÷ taxa diária, em dias de reclusão ininterrupta |
| **Risco** | Falha no teste: role na tabela de Refluxo |

**Vantagem** (2d20, fica com o maior), cumulativa — a segunda em diante vira +2 cada, igual ao Refino:
- Condensar dentro de uma **Terra Abençoada** sintonizada ao Caminho do material
- Condensar sob a **condição ideal** do Caminho (a mesma que dá ×2 de Cargas)
- Ter **nível de domínio Pequeno Feito ou acima** no Caminho ([[☯️ Marcas de Dao|Marcas de Dao]])
- Ter condensado o **mesmo material** com sucesso antes

#### Refluxo de Condensação *(1d6, ao falhar o teste)*

| 1d6 | O que acontece |
|---|---|
| 1–3 | **Dispersão.** O lote se perde, as Cargas se perdem. Nada mais |
| 4–5 | **Escória.** Sai matéria impura: metade das unidades, e o material **não** concede a vantagem de "Materiais puros" no Refino. Vende por 1/4 do preço |
| 6 | **Colapso do molde.** O acima, mais **1 Ferimento** e a Abertura fica instável: todo Gu custa o dobro até um descanso longo |

Falhar o teste por **10 ou mais** trata o resultado como 6 automaticamente.

### 1.3 Tabela de materiais condensáveis

O **modificador de Caminho** do [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]] já está aplicado nas Cargas (Sangue ×0,5, elemental ×1, Alma/Sabedoria ×1,25, Tempo/Espaço ×1,5).

| Material | Caminho | Rank | Cargas | CD | Rende | Preço *(Pedras Primordiais)* | Eficiência | Pra que serve |
|---|---|---|---|---|---|---|---|---|
| **Areia de Ferro-Espírito** | Metal | 1 | **5** | 12 | 1 porção | **6** | 24% | Base de qualquer Gu de corte ou armadura de rank 1–2 |
| **Brasa de Núcleo Ígneo** | Fogo | 2 | **10** | 15 | 1 porção | **12** | 24% | Combustível de refino; alimenta Gu de Fogo por um mês |
| **Âmbar de Seiva Viva** | Madeira | 2 | **10** | 15 | 1 porção | **12** | 24% | Gu de cura e regeneração; conserva material vivo |
| **🌙 Cristal de Luz Lunar** | Lua / Yin | 2 | **10** | 15 | 1 porção | **15** | 30% | Foco de Lâminas de Lua; guarda uma noite de luar pra usar de dia (anula −2 de Sol Direto por 1 cena) |
| **Pérola de Água Morta** | Água | 3 | **20** | 18 | 1 porção | **25** | 25% | Gu de veneno, névoa e afogamento; conserva alma fresca por +6 h |
| **🩸 Coral de Sangue Coagulado** | Sangue | 3 | **10** | 18 | 1 porção | **25** | **50%** | Gu de Sangue e Carne; substitui sacrifício humano numa formação |
| **🌙 Jade Fria Yin** | Lua + Alma | 3 | **25** | 18 | 1 porção | **40** | 32% | Aplica **Frio Yin** sem gastar Gu (1 cena por peça); matéria-prima obrigatória de todo Gu de Alma defensivo |
| **Sal de Trovão** | Raio | 4 | **40** | 21 | 1 porção | **60** | 30% | Gu de raio e velocidade; detona formações |
| **Grão de Éter Vazio** | Espaço | 4 | **60** | 21 | 1 porção | **90** | 30% | Bolsas dimensionais, âncoras de teleporte |
| **Pó de Hora Parada** | Tempo | 5 | **120** | 24 | 1 porção | **200** *(leilão — sem mercado aberto)* | 33% | Ajusta o fluxo de tempo de uma Terra Abençoada em ±0,1× por ano |
| **🌑 Núcleo de Noite Eterna** | Yin puro | **6** | **20 UV** *(Essência Imortal)* | 25 | 1 núcleo | **8 Pedras Imortais** | 40% | Material imortal. Só se condensa dentro de uma Terra de Noite Eterna |

**"Eficiência"** é o preço de venda dividido pelo valor bruto da essência gasta, contando **1 Pedra Primordial ≈ 20 pontos de essência** (a taxa de reposição já usada em [[🧩 Refino e Precificação|Refino e Precificação]]).

#### A regra que faz isso funcionar: condensar dá prejuízo

Faça a conta de um lote de **Jade Fria Yin**: 25 Cargas = **2.500 pontos de essência**. Essa mesma essência, se você a tivesse em Pedras Primordiais, seriam **125 Pedras**. A Jade vende por **40**.

**Você queimou 125 Pedras de valor pra produzir 40.** É prejuízo de 68%, e é de propósito.

> **Por que é ruim de propósito.** Se condensar fosse lucrativo por essência gasta, o jogo inteiro viraria uma planilha: todo personagem pararia de aventurar e sentaria a campanha inteira imprimindo dinheiro, e a Pedra Primordial deixaria de ser um recurso escasso. Com 25% de eficiência, **condensar só compensa com essência que ia evaporar de qualquer forma** — e é por isso que a Condensação é a atividade de quem está em reclusão, viajando, escondido ou esperando uma Calamidade, nunca a atividade de quem tem algo melhor pra fazer com o tanque.
>
> A leitura de mesa: **a essência gasta em Condensação é sempre a essência que sobrou.** Se o jogador está condensando enquanto deveria estar lutando, ele está jogando errado — não porque a mesa proíbe, mas porque a matemática já cobrou.

**A exceção deliberada: Sangue a 50%.** O Caminho do Sangue tem ×0,5 no custo, então o Coral condensa com metade das Cargas e é o único material que quase se paga. O contrapeso é duplo e obrigatório: cada lote **custa `1d6 × M` de Vitalidade** além das Cargas (o combustível é o corpo, não a Abertura — coerente com o [[🏛️ Arquitetura do Sistema|modificador de Sangue]]), e **vender Coral de Sangue é crime capital em qualquer facção ortodoxa**. O material mais lucrativo do sistema é o que te enforca. Isso é o Caminho do Sangue funcionando como deve.

**Material condensado é puro e chato.** Todo material desta tabela carrega a impressão de **um único cultivador**, e qualquer comprador competente percebe (AST CD 14). Isso corta o preço em relação ao material natural equivalente — e dá o bônus: material condensado **sempre conta como "Materiais puros"** pra efeito de vantagem no [[🧩 Refino e Precificação|Refino]], sem pagar os 50% a mais de Pedras.

### 1.4 Impressão de Dao — queimar Marcas excedentes

Um Imortal no teto de Marcas do próprio rank está numa situação absurda: cada 1.000 Marcas de excesso vale **1 Ferimento permanente**, e nenhuma Marca nova gruda ([[☯️ Marcas de Dao|Retrocesso de Marca]]). Ele tem excedente de Dao pelo mesmo motivo que tem excedente de essência — a capacidade é menor que a produção.

A **Impressão de Dao** é o ralo desse excedente.

| | |
|---|---|
| **O que faz** | Grava Marcas de Dao num lote de material condensado, elevando-o a **material imortal** do mesmo tipo |
| **Custo** | **100 Marcas de Dao** do Caminho, por lote, além do material |
| **Onde** | Só dentro de uma Terra Abençoada de **camada 2 ou superior** (coerente com [[💠 Economia das Pedras Primordiais\|Economia]]: material imortal só vem de Terra Abençoada ou resíduo de Calamidade) |
| **Teste** | `d20 + AST`, CD **21**. Vantagem se o Caminho da terra é o Caminho das Marcas |
| **Tempo** | 7 dias internos por lote |
| **Rende** | O material passa a valer **em Pedras de Essência Imortal o que valia em Pedras Primordiais, dividido por 5** — uma Jade Fria Yin de 40 Pedras vira uma Jade Imortal de **8 Pedras Imortais** |
| **Risco** | Falha: as Marcas se perdem **e** o material se perde. Falha por 10+: as Marcas se perdem e você leva **1 Ferimento** — a impressão voltou pra dentro |

**As Marcas gastas somem da contagem.** Contam como perda real pro nível de domínio.

> **Por que ninguém sensato faz isso, e por que isso é bom.** 100 Marcas é caro — é a metade do que uma Calamidade Terrestre inteira rende. Um Imortal com espaço no rank nunca deve queimar Marca em material; ele deve guardar. **Mas um Imortal encostado no teto do rank tem 100 Marcas que valem menos que zero** — elas estão literalmente comendo a Abertura dele. Pra ele, e só pra ele, a Impressão de Dao é a jogada certa.
>
> Isso transforma o Retrocesso de Marca de uma punição passiva numa **decisão econômica**: você acumulou rápido demais pro seu rank, e agora tem que escolher entre Ferimentos permanentes e virar fábrica de material imortal até conseguir subir.

---

## 2. Forjamento com a Alma — Fios de Alma e Pedras de Vontade

O que a essência não faz: matéria **espectral**. Ela atravessa parede, não tem peso, obedece ordem, e não aparece em nenhuma detecção que procure metal. É a matéria-prima de construtos, marionetes e selos — e o preço dela não é essência.

### 2.1 O custo: Força de Alma

Forjar consome **Força de Alma em homens** ([[👻 Caminho da Alma|Caminho da Alma]]) — o mesmo número que multiplica sua Alma máxima.

> **A decisão de design: o gasto é permanente na ficha, mas recuperável pela mesma fonte que o criou.**
>
> **Por que não temporário.** Se a Força voltasse sozinha com descanso, forjar seria de graça e o material espectral inundaria o mercado — exatamente o oposto de "alta raridade". Não haveria decisão.
>
> **Por que não irrecuperável.** Força de Alma **é** o poder do Caminho da Alma. Um custo puramente permanente significaria que nenhum cultivador de Alma jamais forjaria, e a regra morreria na página.
>
> **A solução:** a Força gasta some da ficha e **não volta com descanso, tempo ou cura** — só volta **devorando de novo** (ou com Gu das Tripas). Forjar é reciclar as almas que você comeu em objetos. O preço não é o número: é ter que **comer mais gente** pra repor, e cada refeição custa Contaminação. O Caminho da Alma paga em identidade, como sempre pagou.

**Três travas duras:**

1. **Não se forja abaixo de Força de Alma 1.** Chegar a 0 é a alma dissolvida: morte, sem Teste de Morte.
2. **Cair de degrau custa o multiplicador.** Gastar de 52 pra 48 te tira de Alma de Dez Homens (×1,75) pra Alma Reforçada (×1,5) — a Alma máxima cai na hora, e o dano atual pode te matar se a nova máxima ficar abaixo do dano já sofrido. **Confira antes de forjar.**
3. **Contaminação 50+ dobra o custo.** Com vozes demais lá dentro, metade do que você tenta forjar sai com a vontade errada.

**A válvula do teto.** Forjar é o **único método voluntário do sistema de baixar a Força de Alma**. Um mortal em 96 homens, a um `1d6` da morte, pode forjar um Osso Fantasma e voltar pra 88. Isso não é um bug — é o único freio que um cultivador de Alma tem antes do teto de Cem Homens, e ele custa exatamente o que deveria custar.

### 2.2 O procedimento

| | |
|---|---|
| **Teste** | `d20 + VON + treino` — Alma é atributo de Vontade ([[💪 Atributos\|Atributos]]) |
| **CD** | Pela linha do material |
| **Custo** | A Força de Alma listada, **paga antes de rolar** (some da ficha mesmo se falhar) |
| **Tempo** | Dias de reclusão ininterrupta, listados por material |
| **Risco** | Falha: tabela de Rasgo |

**Vantagem** se: forjar **sob lua cheia** · usar uma alma armazenada como molde · ter nível de domínio **Mestre** ou acima em Alma.

#### Rasgo de Alma *(1d6, ao falhar o teste)*

| 1d6 | O que acontece |
|---|---|
| 1–2 | **Molde vazio.** A Força se perde, o item não sai. Nada mais |
| 3–4 | **Recuo.** O acima, mais `2d6 × M` de dano de **Alma** (ignora RD e armadura) e **+2 de Contaminação** |
| 5 | **Fenda.** O acima, e a Alma máxima cai **−1 permanente** |
| 6 | **Vazamento.** O acima, e o item **sai vivo e errado**: um construto hostil de rank igual ao seu −1 aparece na cena e não te obedece. Ele sabe o que você fez |

### 2.3 Tabela de materiais espectrais

| Material | Força de Alma | CD `d20+VON` | Tempo | O que constrói | Preço *(Pedras Imortais)* |
|---|---|---|---|---|---|
| **Fio de Alma** | **2** | 15 | 1 dia | O sistema nervoso de qualquer construto. Um fio = um cabo de comando de até **1 km**, invisível, que não corta com lâmina física. **10 fios = uma marionete completa** | **2** |
| **Véu Espectral** | **3** | 15 | 2 dias | Selos de ocultação. Cobre **30 m de raio**: dentro dele, Gu de detecção de alma de rank igual ou menor ao seu falham automaticamente. Dura 1 mês | **3** |
| **Pedra de Vontade** | **5** | 18 | 3 dias | O **núcleo** de um construto. Guarda **uma ordem de até 12 palavras** e a executa sem supervisão, indefinidamente. Sem ela, marionete não anda sozinha — alguém tem que segurar os fios | **8** |
| **Osso Fantasma** | **8** | 18 | 5 dias | O esqueleto. **6 ossos + 1 Pedra de Vontade + 10 Fios = um construto espectral de rank 4** (ataca com Força de Alma, ignora RD física, é imune a veneno, medo e Gu de Alma) | **10** |
| **Selo de Nome** | **15** | 21 | 10 dias | Sela **um ser nomeado**. É a base física de um Gu de Juramento de rank alto ([[🤝 O Débito\|O Débito]]) — ou uma barreira que impede **uma pessoa específica**, pelo nome verdadeiro, de entrar num lugar. Uso único | **40** |
| **Coração de Marionete** | **25** | 24 | 30 dias | Um construto com **julgamento**: interpreta ordens em vez de executá-las, e continua funcionando quando o dono morre. **Exige Força de Alma ≥ 1.000 após o pagamento** — ou seja, Alma de Monstro: só Imortal forja | **150** |

**A escala de preço não é acidente.** Um Osso Fantasma vale 10 Pedras Imortais e custa 8 homens de Força de Alma — que é o mesmo que devorar um cultivador de rank 4–5 (`2d10`) e pagar **+8 de Contaminação** por isso. Material espectral é caro no mercado porque é caro na alma de alguém.

### 2.4 Via alternativa: forjar com almas armazenadas

Numa **Terra de Noite Eterna**, as almas devoradas e não digeridas não dispersam ([[👻 Caminho da Alma|Caminho da Alma]]). Elas podem substituir a Força de Alma:

```
2 homens de Força de Alma  ⟷  1 alma armazenada  +  2 de Contaminação
```

| | |
|---|---|
| **A vantagem** | Você não perde nada da própria ficha. Um Osso Fantasma custa 4 almas do estoque em vez de 8 homens seus |
| **O preço** | **+8 de Contaminação** pelo mesmo Osso — e Contaminação só sobe |
| **O contrapeso** | Cada alma queimada em forja **sai** da reserva de Golpes Matadores defensivos (*Recolher o Que Sobrou* precisa de estoque). Você está gastando a sua única defesa |
| **A saída** | A purificação por lua cheia (`1d6 + domínio em Lua`) e a purga passiva da Noite Eterna (−1/mês interno) rodam em paralelo. Uma Terra de Noite Eterna com um cultivador de Lua dentro é a **única configuração do sistema onde forjar em escala é sustentável** |

> **Por que essa via existe.** É a peça que fecha a build Lua+Alma como uma economia, não só como um combo de combate: a terra produz almas, a lua limpa a Contaminação, e a forja converte as duas coisas em objetos que ninguém mais no mundo consegue fabricar. É o motivo pelo qual essa combinação vale um arco inteiro de campanha.

---

## 3. Aplicação no mercado imortal — o Treasure Yellow Heaven

Uma Terra Abençoada de camada 4 é "comércio externo" ([[🗝️ Terra Abençoada|Terra Abençoada]]). Esta seção diz **quanto** e, mais importante, **como se recebe**.

### 3.1 Produção anual bruta, cotada em Pedras de Essência Imortal

> **Esta tabela é o teto, e continua valendo.** [[🌾 Ecologia e Economia da Terra Abençoada]] **decompõe** estes números — de qual canteiro, rebanho ou veia cada Pedra sai — e dá ao jogador as alavancas pra mexer neles (mineração predatória, desviar produção pra Ração, Teste de Gestão anual). Se a soma do detalhamento estourar muito a linha da camada, foi instalado mais do que a camada comporta.

A produção acontece em **tempo interno**, então o fluxo de tempo da terra já está embutido. Os números abaixo são **por ano de tempo externo**, prontos pra usar:

| Camada | Mesquinha *(0,5×)* | Comum *(1×)* | Boa *(1,5×)* | Excelente *(2×)* | Especial *(3×)* |
|---|---|---|---|---|---|
| **1** — produção básica | 100 PP | 400 PP | 900 PP | 1.600 PP | 3.600 PP |
| **2** — materiais imortais | **1 PEI** *(autoconsumo)* | **5 PEI** | **11 PEI** | **20 PEI** | **45 PEI** |
| **3** — ecossistema vivo | **5 PEI** | **20 PEI** | **45 PEI** | **80 PEI** | **180 PEI** |
| **4** — comércio externo | **20 PEI** | **80 PEI** | **180 PEI** | **320 PEI** | **720 PEI** |

*PP = Pedras Primordiais (moeda mortal). PEI = Pedras de Essência Imortal.*

**A camada 2 é autoconsumo, não renda.** Ela zera a despesa de alimentar os próprios Gu Imortais (~10 PEI/ano pra um rank 6 típico) e nada mais. Vender a produção da camada 2 significa **deixar os próprios Gu Imortais com fome** — ver [[🍖 Sustento e Alimento|Sustento e Alimento]].

**A escada é quadrática de propósito.** A qualidade entra duas vezes: uma pelo tamanho/fertilidade e outra pelo fluxo de tempo. Uma terra Especial produz **nove vezes** o que uma Comum produz na mesma camada. Isso é coerente com [[💠 Economia das Pedras Primordiais|Economia das Pedras Primordiais]], onde a riqueza salta ordens de grandeza junto com o poder — e é a razão mecânica pela qual a distribuição das 10 Porções na Ascensão define o personagem por séculos.

**Ferimentos da Terra cortam a renda antes de tudo:**

| Ferimento | Efeito na renda |
|---|---|
| **Rachada** | A camada 4 **para**. Você cai pra renda de camada 3 |
| **Ferida** | O acima, e o fluxo cai pra 1× — recalcule a coluna como **Comum** |
| **Dilacerada** | Perde uma camada. A renda de material imortal **para** |
| **Colapsada** | Zero |

Reparar custa 50 PEI e 3 meses internos por nível. **Uma terra camada 4 Comum leva menos de um ano de renda pra se reparar; uma Mesquinha leva dois anos e meio.** É assim que uma sequência ruim de Calamidades vira uma espiral econômica.

### 3.2 A regra que importa: no nível imortal ninguém paga com moeda

> **Toda transação imortal é uma cena com um NPC nomeado. Não existe "vender a produção do ano".**

Um Imortal não precisa de dinheiro. Ele tem uma Terra Abençoada que produz o que ele come, o que ele veste e o que ele queima. O que ele **não** tem é o que a terra dele não produz — e é isso, e só isso, que ele negocia.

**Formas de pagamento aceitas, e o que cada uma vale:**

| Forma | Valor recebido | O custo real |
|---|---|---|
| **Escambo** — material por material | **100%** do valor cotado, ou **80%** se o comprador não precisa especificamente do que você tem | Nenhum, quando funciona. O problema é achar quem precise |
| **Favor selado** — um Débito de um favor, sem risco de vida | **30 PEI** | Você agora tem alguém devendo. Cobrar é outra cena, e o que ele quer em troca muda com o tempo ([[🤝 O Débito\|O Débito]]) |
| **Favor selado com risco de vida** | **150 PEI** | O credor vai cobrar exatamente quando for pior pra você. É assim que se compra um aliado numa guerra |
| **Anos de Longevidade** | **10 PEI por ano** | O comprador paga com anos dele, ou você paga com os seus. Nunca é indolor ([[⏳ Longevidade\|Longevidade]]) |
| **Pedras de Essência Imortal em espécie** | **70%** do valor cotado | **Pagar em moeda é uma ofensa velada.** Significa "não quero te dever nada e não quero nada seu". Aceite, mas entenda o que foi dito |

> **Por que pagar em dinheiro vale menos.** É a inversão que define o tom do nível imortal: entre mortais, dinheiro é o pagamento limpo; entre Imortais, dinheiro é o pagamento **estéril**. Um Imortal que só te dá pedras não está construindo nada com você — e daqui a duzentos anos, quando você precisar de alguém, ele não vai estar lá. A rede de Débitos **é** o poder. A pilha de pedras é só uma pilha.

**O teste da transação:**

```
Negociação = d20 + CAR + treino
```

| Valor da transação | CD |
|---|---|
| até 50 PEI | **14** |
| 51 – 200 PEI | **18** |
| 201 PEI ou mais | **22** |

| Resultado | O que acontece |
|---|---|
| **Sucesso** | Valor cheio, na forma que você escolheu |
| **Falha por 1–4** | **−25%** no valor, ou valor cheio na forma que **ele** escolher |
| **Falha por 5+** | Role o **Preço Oculto** |

#### Preço Oculto *(1d6)*

| 1d6 | O que você descobre depois |
|---|---|
| 1 | O comprador **revende** pra alguém que você não venderia. Uma facção que te odeia agora tem seu material |
| 2 | O favor que você aceitou tinha redação vaga. A mesa reescreve o pacto **a favor dele** ([[🤝 O Débito\|O Débito]]) |
| 3 | Ele agora sabe a **camada e a qualidade** da sua Terra Abençoada. Isso é a informação que precede uma anexação |
| 4 | Os anos de Longevidade vieram de alguém que não os deu de boa vontade. **+2 na CD** da sua próxima Calamidade |
| 5 | Ele plantou algo no material que você recebeu: um rastreador, um Gu adormecido, ou uma Marca alheia |
| 6 | Você foi pago em material **impresso com o Dao de outro Imortal**. Usá-lo em refino funciona — e deixa a assinatura dele nos seus Gu |

#### A Rede de Compradores — por que Carisma importa no nível imortal

```
Compradores nomeados que você sustenta = CAR + 2
```

**Cada comprador absorve no máximo 25% da sua produção anual, e negocia com você no máximo uma vez por ano.** Um Imortal com CAR 0 tem **dois** compradores: ele consegue escoar 50% do que a terra dele produz, e o resto apodrece no estoque.

> **Por que essa regra existe.** Sem ela, a renda da tabela 3.1 seria um número que aparece na ficha todo ano sem que ninguém jogue nada — e a Terra Abençoada, que é metade da identidade de um Imortal, viraria uma linha de planilha. Com ela, **produzir e vender são dois problemas diferentes**: a terra resolve o primeiro, e só a política resolve o segundo. Um Imortal recluso com uma terra Especial é rico no papel e pobre na prática, e essa é uma das figuras mais canônicas do cenário.
>
> Também é o que faz o CAR do [[💪 Atributos|ponto de compra]] continuar valendo depois da Ascensão, quando o combate já se decide por Marcas.

### 3.3 O canal anônimo

A Rede de Compradores é o canal **político**: valor cheio, pago em escambo e favores, limitado a `CAR + 2` pessoas. O excedente que ela não absorve escoa pelo [[🏪 Céu Amarelo do Tesouro]] — o mercado imortal remoto, que compra tudo, paga **60%** em pedras, e não constrói relação nenhuma. As regras de balcão, leilão, monopólio e guerra de preços estão lá.

### 3.4 A Terra de Noite Eterna — monopólio Yin

A Terra Abençoada Especial do [[🌠 Os Dez Físicos Extremos|Físico da Lua Antiga]] só produz **material Yin**: Cristal de Luz Lunar, Jade Fria Yin, Núcleo de Noite Eterna, e todo o catálogo espectral da seção 2.

| | |
|---|---|
| **O monopólio** | **×2 no preço** de todo material Yin vendido. Não existe segunda fonte no mundo — quem quer, compra de você |
| **Excedente total** | Você não precisa comprar o que produz. **100% da produção Yin é vendável**, não só o que sobra |
| **A dependência** | A terra **não produz nada Yang**: fogo, metal, madeira, luz. Tudo isso você **compra**, sempre, com **+50% de ágio** — porque o vendedor sabe que você não tem alternativa |
| **A conta líquida** | Uma Noite Eterna camada 4 rende **720 PEI × 2 = 1.440 PEI/ano** em cotação bruta, e gasta de volta ~200 PEI/ano em material Yang com ágio. Ainda é a maior renda do sistema — de longe |

**Quem compra:** cultivadores de Alma, de Sombra, de Veneno, de Morte, de Sangue. Ou seja, **os Caminhos que a maioria das facções ortodoxas classifica como demoníacos**. Você não escolhe sua clientela; o Dao da sua terra escolheu por você.

> **Isso é poder político e é um alvo pintado nas costas, e as duas coisas são a mesma coisa.** Você se torna a infraestrutura de um bloco inteiro do mundo. Nenhuma guerra de Caminho escuro acontece sem passar por você — o que significa que ninguém pode te matar sem que os outros percebam, e que **todo mundo tem motivo pra te controlar em vez de te matar.** Controlar é pior.

#### Atenção — o marcador do monopolista

Um número na ficha do Imortal, ao lado das Marcas. **Só sobe**, salvo abaixo.

| Evento | Atenção |
|---|---|
| Cada ano externo comerciando como monopolista | **+1** |
| Vender pra uma facção de Caminho proibido *(Sangue, Escravidão, Morte)* | **+2** por transação |
| Recusar uma venda a uma facção que já comprou de você antes | **+2** |
| Falhar num teste de Negociação por 5+ | **+1** |
| Passar um ano externo **sem vender nada** | **−1** |
| Vender através de um intermediário nomeado que assuma o crédito | **−1** por ano *(e ele fica com 30% do valor)* |

| Atenção | O que acontece, na próxima cena de comércio |
|---|---|
| **3** | Um dos seus compradores **vira credor**: ele oferece um Débito em vez de escambo, e a recusa custa a relação. A rede encolhe em 1 |
| **6** | Uma facção manda um **emissário com proposta de exclusividade**. Aceitar corta sua rede pela metade e garante a renda; recusar declara inimizade com uma facção inteira |
| **8** | Alguém localiza a entrada da sua Terra Abençoada. **Toda Calamidade Terrestre a partir daqui vem com companhia**: role a Calamidade normalmente, e some um invasor Imortal na mesma cena |
| **10** | Uma tentativa de **anexação da sua Abertura** ([[🗝️ Terra Abençoada\|Terra Abençoada]]). Não é ameaça: é a cena, e ela acontece |

> **Por que o marcador existe.** Monopólio sem consequência é renda infinita, e renda infinita mata a tensão que o resto do vault construiu. A Atenção transforma a maior fonte de dinheiro do sistema numa **contagem regressiva** — quanto mais você vende, mais rápido chega o dia em que alguém vem tomar a fábrica. E as duas saídas (parar de vender, ou pagar 30% a um intermediário que pode te trair) são decisões de mesa, não rolagens.

---

## 📌 Resumo de mesa

| Processo | Custo | Tempo | Teste | Falha |
|---|---|---|---|---|
| **Condensação Elemental** | 5–120 Cargas *(100 essência cada)* | Cargas ÷ (Ess. máx ÷ 100) dias | `d20 + AST` vs 12–24 | Refluxo `1d6` |
| **Impressão de Dao** | 100 Marcas + o material | 7 dias internos | `d20 + AST` vs 21 | Marcas e material perdidos; 10+ = 1 Ferimento |
| **Forjamento com a Alma** | 2–25 homens de Força de Alma *(irrecuperável salvo devorando)* | 1–30 dias | `d20 + VON` vs 15–24 | Rasgo `1d6` |
| **Forja com almas armazenadas** | 1 alma + 2 Contaminação por 2 homens | idem | idem | idem |
| **Transação imortal** | Uma cena com NPC nomeado | 1 por comprador por ano | `d20 + CAR` vs 14–22 | Preço Oculto `1d6` |
