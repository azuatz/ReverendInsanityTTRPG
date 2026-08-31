---
tags:
  - regra
  - fechado
aliases:
  - Arquitetura do Sistema
escopo: sistema
---

# 🏛️ Arquitetura do Sistema

> A nota mais importante do vault: é aqui que as peças do sistema aparecem juntas, e é por aqui que se entende como uma mexe na outra. **A autoridade final é o [[🧭 Log de Decisões]]** — se esta página contradiz o Log, é esta página que está errada e precisa ser corrigida.

---

## 🧱 Dois eixos, uma pessoa só

| | **Cultivo (Rank)** | **Gu** |
|---|---|---|
| O que é | O cofre: **capacidade e permissão** | O conteúdo: **as ferramentas vivas** |
| Mede | O rank de Gu que você comanda e o tamanho da sua Abertura | O que você é capaz de fazer |
| Como cresce | Estágio (frequente, material) e Rank (raro: material + anos de vida + provação) | Jogando: caçar, roubar, refinar, herdar, comprar |
| Velocidade | Estágio a cada 1–3 sessões; rank a cada 8–12 | Rápida. Algo novo quase toda sessão |
| Se perde? | Raramente — e é tragédia | O tempo todo: morrem de fome, são roubados, se gastam |

**Todo cultivador participa dos dois eixos.** Não existe personagem que treina o corpo e nunca toca num Gu — isso não é mais uma opção de build. Todo mundo abre a Abertura, todo mundo caça e alimenta Gu desde o rank 1. O que varia é o quanto: aptidões diferentes abrem Aberturas de tamanhos diferentes (ver abaixo), e o estilo de cada personagem — mais corpo a corpo, mais à distância, mais armadilhas — nasce de quais Gu ele escolhe carregar, não de uma escolha de classe.

---

## 🌉 A Ponte — as regras que ligam Rank e Gu

### 1. A Porta — seu rank define o rank de Gu que você consegue usar

São **9 ranks, sem compressão** — igual ao cânone. Ranks 1–5 são a fase mortal (Mestre de Gu), cada um com quatro estágios (Inicial, Médio, Alto, Pico). Rank 6 é a Ascensão Imortal. **Rank 9 é o teto do mundo: Venerável** (ou Venerável Demônio, pelo Caminho proibido) — e não existe nada acima. Ver [[🪜 Ranks e Estágios|Ranks e Estágios]] pra tabela completa.

Um cultivador de rank X ativa normalmente Gu de rank igual ou menor. Um Gu 1 rank acima pode ser **forçado** — custa metade da essência máxima, um teste de Vontade e um Ferimento. Um de 2 ranks acima custa o tanque inteiro. Atravessar a linha mortal/imortal (usar um Gu de rank 6+ sendo mortal) nunca é possível — Gu Imortais não rodam com essência mortal, combustível errado, não preço alto.

Gu de rank baixo ficam obsoletos em combate conforme você sobe — o número é do Gu, não seu. O que eles não perdem é utilidade fora de combate: o mesmo Gu de rastreamento ou infiltração resolve a mesma cena no rank 6 que resolvia no rank 1, e continua custando quase nada de sustentar. A coleção velha vira caixa de ferramentas, não arsenal.

### 2. A Abertura — um espectro, não uma escolha binária

Não existe número fixo de espaços. Existe uma conta:

```
Essência = sua % de abertura × 4 × 2^(estágio − 1)
```

*(Exemplo: aptidão 25%, estágio Alto (3) → 25 × 4 × 2² = 400 de essência máxima.)*

A **% de abertura** vem da aptidão de cada personagem — construída na criação (ver [[🧑‍🎤 Trilhas de Personagem|04 — Trilhas de Personagem]]), não escolhida como "bruxo" ou "marcial". Uma aptidão alta abre mais; uma baixa abre menos, mas ninguém fica de fora do sistema.

Cada estágio **dobra** a essência, e o contador volta ao começo a cada rank novo.

O custo de ativar um Gu depende de **duas coisas: o que ele faz, e a diferença de rank.** O estágio não muda nada:

| O Gu é... | do seu rank | 1 rank abaixo | 2 ranks abaixo | 3+ ranks abaixo |
|---|---|---|---|---|
| **Custo base** | **40** | **10** | **4** | **1** |

### O modificador de Caminho — nem todo Gu custa igual

Sobre o custo base, aplique o multiplicador do que o Gu faz. É o que dá identidade econômica a cada Caminho:

| Categoria | Custo |
|---|---|
| **Sangue, Carne, Osso** | **×0,5** |
| **Elementais e físicos** (fogo, água, metal, madeira, terra, vento, gelo, raio, luz, força, transformação) | **×1** |
| **Alma, Sabedoria, Escravidão, Informação, Sorte** | **×1,25** |
| **Tempo, Espaço, Sonho, Leis, e qualquer coisa que altere a realidade** | **×1,5** |

Arredonde pra cima. O modificador vale pro custo de ativação **e** pra manutenção por rodada. *(Exemplo: um Gu de teleporte de rank igual ao seu custa 40 × 1,5 = 60; um de fogo do mesmo rank custa 40.)*

Cada rank novo devolve ao começo — com ferramentas de outro patamar. E o dano de cada Gu também dobra a cada rank (M ×1 no rank 1 até ×256 no rank 9 — ver [[⚔️ Combate|Combate]]), a correção que faz o custo de ativação combinar com o quanto um Gu novo bate mais forte. Dano de Gu é um **pool de dados**, nunca um número fixo: `M d(dado do Caminho) + (M × B)` — o M do rank diz **quantos dados** se rola, o Caminho diz **qual dado**, e o Grau de Densidade do estágio (B) soma **por dado**. **Dano corpo a corpo sem Gu ativo não entra nessa escala** — é físico, definido pela arma e o Corpo do personagem, e só sobe com um Gu do Caminho da Força ou de Transformação ativo.

**Carregar um Gu não custa essência — custa comida.** Cada Gu come um tipo de coisa do mundo, ou pedras primordiais no lugar. Quantos cabem depende do tamanho da Abertura: `(sua % ÷ 10) + rank`. Gu de rank baixo ficam praticamente de graça de ativar conforme você sobe, então vale carregar os de utilidade pra sempre — mas os de dano, defesa e reforço precisam ser trocados a cada rank, porque o dado deles não cresce sozinho.

**Carregar não é o mesmo que manter ativo.** O número acima é quantos Gu cabem na Abertura. Quantos podem estar **ativos ao mesmo tempo** é outra conta, bem menor:

```
Gu simultaneamente ativos = Constituição (CON) + rank
```

Um rank 3 com CON +2 sustenta 5 Gu ativos. Gu de ativação instantânea (um ataque que dispara e acaba) não ocupam vaga; os que ocupam são os **sustentados** — defesa, reforço, voo, transformação, formação. É essa trava que impede alguém de ligar seis Gu de defesa e virar invulnerável.

### A Manutenção — o preço de manter tudo ligado

Cada Gu sustentado tem o custo por rodada listado na ficha dele. Além disso, **manter vários ao mesmo tempo cobra por si só**, e o preço cresce ao quadrado:

```
Manutenção de Sustentação = (número de Gu sustentados)² × 5 de essência por rodada
```

| Gu sustentados | Custo por rodada |
|---|---|
| 1 | 5 |
| 2 | 20 |
| 3 | 45 |
| 4 | 80 |
| 5 | 125 |
| 6 | **180** |

Isso é **somado** aos custos individuais dos Gu. Um personagem com quatro Gu sustentados paga 80 de Sustentação mais o que cada um cobra separadamente.

### A regeneração — fora de combate, salvo o Físico Extremo

**Essência não regenera durante o combate** (decisão 107). O que se recupera, recupera-se entre cenas: **uma % da Essência máxima por hora, pelo Grau de Aptidão** (D 2%/h · C 4%/h · B 6%/h · A 8%/h — tanque cheio leva de ~12 h a ~50 h, o ritmo do romance) — ver [[🌟 Aptidão e Abertura|Aptidão e Abertura]]. A **única** fonte de essência dentro de uma luta é o [[🌠 Os Dez Físicos Extremos|Físico Extremo]] (10% do tanque por rodada), e é exatamente essa exclusividade que faz dele outra categoria de coisa.

### O teto de regeneração

Vale pra qualquer efeito que devolva essência em combate (na prática, o Físico Extremo e raros Gu). Nenhuma fonte devolve mais do que isto por rodada, **independente da conta que a produziu**:

| Condição | Teto por rodada |
|---|---|
| Padrão | **100** |
| Sob luar / condição favorável ao Caminho | **150** |
| Sob lua cheia / condição ideal | **200** |
| Sob condição hostil ao Caminho (sol forte pra um Yin, chuva pra um de Fogo) | **50** |

### As paredes da Abertura

A Abertura tem paredes, e é rompendo e reconstruindo essas paredes que o cultivo mortal acontece (a Quebra de Paredes — ver [[🪜 Ranks e Estágios|Ranks e Estágios]]). Certas coisas as danificam de forma permanente:

| Estado da parede     | Origem                                               | Efeito                                                                                                                                            |
| -------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Paredes Mortas**   | Transformação em zumbi, ou dano de Alma catastrófico | Interrompe cultivo e regeneração de essência por completo. O personagem para de progredir                                                         |
| **Paredes de Pedra** | Gu de Dantian de Pedra e similares                   | +50% de Essência máxima, mas a parede perde flexibilidade: **teto de rank permanente onde estiver**. Atalho clássico de quem desistiu de ascender |

### 3. A Ativação Forçada — a única forma de furar a Porta

Um Gu acima do seu rank resiste. Dá pra empurrar com muito da sua própria essência — ou com essência que não é sua, em pedras.

> **Ativação Forçada** — só é possível com uma fonte externa que cubra o custo inteiro: pedras de essência primordial, um aliado canalizando, ou essência drenada de outro cultivador.
> **Duas portas:** metade da sua essência máxima (1 rank acima) ou o tanque inteiro (2 acima), com teste de Vontade — ou 120 pedras do rank do Gu, sem risco. **1 Ferimento nos dois casos.**
> **Nunca atravessa a linha mortal/imortal:** essência mortal não força um Gu Imortal em hipótese nenhuma.
> **E o Gu pode não sobreviver:** teste de Vontade CD `12 + (3 × diferença de rank)`. Falhou, o Gu morre depois de agir.

Nunca é rotina. É a jogada de quem já decidiu pagar caro — e é sempre uma cena que a mesa vai lembrar.

### 4. O Caminho — sua identidade se firma na Ascensão, não na criação

No rank mortal (1–5), o Caminho de um personagem é uma tendência: os Gu que ele caça, o estilo de combate que desenvolve, o tipo de problema que resolve. Nada disso é travado ainda. **Só ao ascender a Imortal (rank 6) o personagem escolhe e cristaliza um Caminho de verdade** — e a partir daí, Golpes Matadores, Marcas de Dao e boa parte da identidade mecânica do personagem passam a girar em torno dele. Ver [[🛤️ Os Caminhos|Os Caminhos]].

### 5. A Ascensão Imortal — o gargalo, não a compra

Virar Imortal é **o maior gargalo do jogo**, e a maioria dos cultivadores do mundo morre sem chegar perto. Não basta chegar ao rank 5 Pico: é preciso atravessar um de dois portões — ter refinado um **Gu Imortal** (impossível pra um mortal sozinho: exige a cooperação de um [[🧿 Espíritos da Terra|Espírito da Terra]] dentro de uma Terra Abençoada) ou ter usado com sucesso um **Golpe Matador de rank 5** contra alguém do próprio rank ou acima. Depois disso ainda vem reunir os recursos, distribuir os Três Ares que definem a [[🗝️ Terra Abençoada|Terra Abençoada]] resultante, e sobreviver a cinco testes que matam de verdade. É o clímax de um ato inteiro da campanha. Ver [[♾️ A Ascensão Imortal|A Ascensão Imortal]].

### 6. Depois da imortalidade, o rank para de medir — as Marcas medem

Da Ascensão em diante não existem mais estágios. O que define um Imortal é **quantas Marcas de Dao ele tem e de qual Caminho** — elas dão Níveis de Dano nos Gu daquele Caminho, destravam o refino de Gu Imortais mais altos, e cobram o preço de reescrever a personalidade de quem as carrega. Rank vira só "o que eu consigo ativar"; Marca vira "o que eu sou". Ver [[☯️ Marcas de Dao|Marcas de Dao]].

---

## 🩸 O tom de sobreviventes, traduzido em mecânica

1. **Sem essência, você ainda luta — mas fraco.** Reforço físico e manobras aprendidas são o chão; um Gu bem colocado é o golpe caro que decide a cena.
2. **Cura tem ritmo, não é infinita.** Descanso curto devolve metade; só um descanso longo de verdade devolve tudo — e um descanso longo em território hostil é, por si só, uma cena de risco.
3. **Preparação é recurso mecânico.** Fichas de Plano geram Pontos de Plano gastáveis — e informação pode ser plantada. Ver [[🕵️ Preparação e Informação|Preparação e Informação]].
4. **Fugir tem regra própria** — perseguição em 3 rodadas, e sempre dá pra sacrificar algo pra escapar. Ver [[🏃 Fuga e Perseguição|Fuga e Perseguição]].
5. **Seus Gu podem morrer de fome.** O poder não é seu: está emprestado de criaturas que dependem de você e que você tem que alimentar.
6. **Todo mundo nasce com 100 anos, e avançar de rank não queima nenhum** — só leva tempo de calendário. Passar dos 100 exige Gu de Longevidade. Ver [[⏳ Longevidade|Longevidade]].
7. **Defesa é um Gu, não um direito.** Só se defende quem comprou, carregou e alimentou um Gu de defesa — e ele é sustentado: paga pra ligar e paga por rodada pra manter.
8. **Combate fica mais letal conforme se sobe.** Nos ranks altos, uma luta se decide antes de começar.
9. **Rank vem na roupa, sem exceção.** A maioria dos clãs e seitas borda o rank na vestimenta — é informação pública, sem teste. O que o mundo acha de você além disso é narrativa pura.

---

## 🚫 O que este sistema deliberadamente **não** tem

Trilha de personagem sem Gu · espaços/slots de técnica · tabela de XP e níveis · sobrecarga barata · Ascensão Imortal como compra de nível · tabela de níveis de ferimento com penalidade em teste · falha crítica punitiva. O porquê de cada rejeição está no [[🧭 Log de Decisões|Log de Decisões]].
