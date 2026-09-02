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

### A Densidade é comprada, ativação por ativação

O bônus de dano do estágio (`M × B`) **não vem de graça junto com o estágio**. Ele é uma compra, e a decisão é do jogador **a cada vez que ativa um Gu**:

```
Custo final = custo base × modificador de Caminho × modificador de Densidade
```

| Você quer o Gu com... | Modificador de Densidade |
|---|---|
| **`B` 0** — sem bônus de dano nenhum | **×1** |
| **`B` 1** | **×1,5** |
| **`B` 2** | **×2** |
| **`B` 3** | **×3** |

**O custo base entrega o Gu funcionando, com `B` 0.** Você nunca é obrigado a pagar mais — e nunca pode comprar acima do `B` que o seu estágio já concede. Nas palavras do autor, que é de onde a regra saiu: *o custo escala se você quiser que aumente o dano; caso não, você gasta só a essência inicial e guarda o resto.*

**Na mesa isso é uma pergunta por ativação:** *este disparo precisa do dano cheio?* Contra um recruta, não; contra o Chefe na rodada em que ele está exposto, sim. É a decisão que a regra existe para criar.

> [!warning] O que esta regra **não** faz — e é honesto dizer
> Ela **não iguala a pressão entre estágios**. O tanque de essência multiplica por **oito** do Inicial ao Pico, e este custo só por **três** — então um cultivador no Pico continua com cerca de **2,7 vezes** o fôlego de um no Inicial. A única dose que igualaria (`×2^B`, dobrando por ponto) foi medida em cena e **apaga o combate**: derruba o Clímax de rank 5 de 72% para 6% de vitória. Isto aqui é a dose mais cara que a cena tolera, e ela cobra 9 pontos percentuais no Clímax de rank 3. *(Decisões 235, 258, 267 e 268 — a história inteira dessa calibragem está lá, incluindo as três doses rejeitadas.)*

Cada rank novo devolve ao começo — com ferramentas de outro patamar. E o dano de cada Gu também dobra a cada rank (M ×1 no rank 1 até ×256 no rank 9 — ver [[⚔️ Combate|Combate]]), a correção que faz o custo de ativação combinar com o quanto um Gu novo bate mais forte. Dano de Gu é um **pool de dados**, nunca um número fixo: `M d(dado do Caminho) + (M × B)` — o M do rank diz **quantos dados** se rola, o Caminho diz **qual dado**, e o Grau de Densidade do estágio (B) soma **por dado**. **Dano corpo a corpo sem Gu ativo não entra nessa escala** — é físico, definido pela arma e o Corpo do personagem, e só sobe com um Gu do Caminho da Força ou de Transformação ativo.

**Carregar um Gu não custa essência — custa comida.** Cada Gu come um tipo de coisa do mundo, ou pedras primordiais no lugar. Quantos cabem depende do tamanho da Abertura: `(sua % ÷ 10) + rank`. Gu de rank baixo ficam praticamente de graça de ativar conforme você sobe, então vale carregar os de utilidade pra sempre — mas os de dano, defesa e reforço precisam ser trocados a cada rank, porque o dado deles não cresce sozinho.

> [!important] Gu de Corpo **não ocupam vaga na Abertura**
> Um Gu de Corpo foi assentado na carne por cirurgia: ele não está guardado na Abertura, **ele é o corpo**. Não conta na `(% ÷ 10) + rank`, não conta nas 3 vagas de sustentação, não come e não pode ser roubado.
>
> **Por que de graça nas duas contas:** ele já foi pago três vezes — exige o portão de CON, exige teste de assentamento (falha = 1 Ferimento permanente), e é **irreversível**, com teto de +4 Níveis de Dano para a cadeia inteira. Cobrar vaga por cima seria cobrar de novo pela mesma compra, e é o que fazia o lutador ter o arsenal mais pobre da mesa apesar de ser quem paga mais caro por ele. *(Decisão do autor, 2026-09-01.)*

**Carregar não é o mesmo que manter ativo.** O número acima é quantos Gu cabem na Abertura. Quantos podem estar **ativos ao mesmo tempo** é outra coisa, e é um número pequeno e **fixo**:

```
Gu simultaneamente sustentados = 3      (Mestre de Gu comum: 2)
```

**Não depende de atributo nem de rank.** Este não é um limite do corpo nem da essência: é um limite de **atenção**. Cada Gu ligado é uma tarefa mental separada rodando ao mesmo tempo — manter três de pé sem errar já é a marca de um cultivador excepcional, e é por isso que **3 é o número dos personagens de jogador** e dos inimigos nomeados, enquanto o Mestre de Gu de rua opera em **2**.

Gu de ativação instantânea (um ataque que dispara e acaba) **não ocupam vaga**; os que ocupam são os **sustentados** — defesa, reforço, voo, transformação, percepção contínua, formação sobrecarregada. É essa trava que impede alguém de ligar seis Gu de defesa e virar invulnerável, e ela vale **fora do combate também**: quem está sustentando três Gu não tem cabeça sobrando pra refinar.

> [!warning] O quarto Gu — possível, e é onde os erros acontecem
> Você **pode** sustentar **um** acima do seu teto. Enquanto estiver assim, role **`1d6` no início de cada turno** (ou por hora, fora de combate): em **1–2**, a atenção escorrega e **um dos Gu sustentados desliga** — o mestre escolhe qual, e a essência de reativação sai do zero na sua próxima ação.
>
> Não há quinto. Passar de um acima do teto só com **Gu de multitarefa** (abaixo), e o que eles dão conta como teto pra tudo: um personagem com teto 4 rola erro no quinto, não no quarto.

**A rota de subir o teto é comprada, não rolada na ficha.** Existe uma família de Gu dedicada a dividir a atenção — cada posto dela dá **+1 vaga permanente** enquanto o Gu estiver carregado. É o instrumento clássico do **Caminho da Escravidão** ([[🛤️ Os Caminhos|Os Caminhos]]) — quem comanda feras e escravos precisa de linhas mentais sobrando —, e é o que explica em ficção por que um domador sustenta mais coisa que um espadachim do mesmo rank. Isso transforma *"quantos Gu eu sustento"* num **eixo de arsenal e de economia** em vez de um número que vem de graça com o rank.

> [!note] Por que fixo em vez de `CON + rank`
> A fórmula antiga entregava **8 Gu simultâneos** a um rank 5 com CON +3 — quase o triplo do que o mundo suporta, e o efeito colateral era que a Manutenção quadrática virava decoração, porque ninguém chegava perto do teto. Com teto 3, ela morde exatamente onde deve: no especialista que **comprou** o direito de empilhar. Ver decisão 260 no [[🧭 Log de Decisões]].

### A Manutenção — REMOVIDA (decisão 266)

> [!warning] A Manutenção de Sustentação quadrática **não existe mais**
> A regra era `(nº de Gu sustentados)² × 5 de essência por rodada`, por cima do custo de cada Gu. **Foi removida**, e por três razões que se somam:
>
> 1. **Ela nunca entrou em simulação nenhuma, e o motor dizia isso por escrito.** Vinte e seis rodadas de balanceamento — a tabela de composição inteira, os moldes, o Chefe, os Golpes Matadores — rodaram **sem** a Manutenção; três scripts chegam a trazer na própria docstring a linha *"Manutenção quadrática dos Gu sustentados OMITIDA"*, incluindo o motor de que todos os posteriores descendem. Ela nunca sustentou o balanceamento que o vault publica, e removê-la **não move um único número medido**.
> 2. **Ela não era o freio que dizia ser.** Medida, quatro Gu sustentados bancavam **2,8 a 4,3 rodadas no estágio Inicial** e **22 a 34 no Pico**, contra uma cena de 7 a 9 — punia demais no começo e virava decoração no fim. É exatamente o defeito que a decisão 235 diagnosticou no custo de ativação.
> 3. **A Densidade paga já faz o trabalho, e melhor.** Desde a decisão 258 o bônus de `B` é comprado por ativação (`×1 / ×1,5 / ×2 / ×3`, acima), e isso põe o preço onde a decisão acontece. Manter as duas regras empilhava dois custos calibrados isoladamente e secava o tanque em 2 a 6 rodadas, abaixo da cena inteira.
>
> **O que segura o número de Gu ligados agora são duas coisas, não três:** o **teto de 3 Gu sustentados** (a regra de ficção, decisão 260) e o **custo de ativação com Densidade paga** (a regra de economia, decisão 258). Uma diz quantos você consegue coordenar; a outra diz quantos você consegue pagar. A Manutenção era um terceiro número por rodada que o mestre rastreava sem que ele decidisse nada.

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

> **Ativação Forçada** — duas formas de pagar, e você escolhe: **a sua própria essência**, ou uma **fonte externa** que cubra o custo inteiro (pedras de essência primordial, um aliado canalizando, ou essência drenada de outro cultivador).
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
