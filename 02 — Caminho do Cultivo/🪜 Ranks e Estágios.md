---
tags:
  - regra
  - cultivo
  - fechado
aliases:
  - Ranks e Estágios
escopo: sistema
---

# 🪜 Ranks e Estágios

O cultivo tem **nove ranks** (Nove Giros) — sem compressão, sem teto artificial abaixo do nono. Ranks 1 a 5 são a fase mortal (Mestre de Gu). Ranks 6 a 9 são a fase imortal (Imortal de Gu), e o rank 9 é o topo absoluto: **Venerável** (ou **Venerável Demônio**, para quem chega lá por fora das facções estabelecidas). Cada rank mortal tem quatro estágios — Inicial, Médio, Alto, Pico.

## Fase mortal — Mestre de Gu (rank 1 a 5)

| Rank | Nome | Essência | Papel de combate |
|---|---|---|---|
| 1 | Primeiro Giro | Essência de Cobre Verde | Suporte/logística — acabou de deixar a camada de gente comum |
| 2 | Segundo Giro | Essência de Aço Vermelho | Tropa de combate principal de qualquer família |
| 3 | Terceiro Giro | Essência de Prata | Ancião/pilar — aqui o personagem escolhe sua linha e monta seu conjunto de Gu de verdade |
| 4 | Quarto Giro | Essência de Ouro | Nível de patriarca |
| 5 | Quinto Giro | Essência de Cristal Roxo | Teto do nível mortal — pico é o limiar da Ascensão Imortal |

**Avanço de estágio** (Inicial→Médio→Alto→Pico) é trabalho gradual: acumular Verdadeira Essência de qualidade suficiente. Não exige teste — acontece com o jogo, entre sessões, conforme a mesa narra o tempo passando.

---

## 💠 A Densidade da Essência — o que o estágio dá de verdade

> O estágio **purifica a essência**, e essência mais densa atravessa mais — é isso que a Densidade representa. O porquê do desenho está nas decisões 77–82 do [[🧭 Log de Decisões]]; a versão anterior, em [[_Arquivo/🪜 Ranks e Estágios (v1 — estágio só dobrava essência)|_Arquivo]].

O estágio não é uma barra que enche — é **qualidade de combustível**. Cada estágio tem um **Grau de Densidade** de 0 a 3, e esse número é a única coisa que você precisa anotar na ficha.

### A tabela mestre do estágio

| Estágio | **Grau (B)** | **Dano** | **Vitalidade** | **Alma** | **Vagas de Suporte** | **Teto de Combo** |
|---|---|---|---|---|---|---|
| **Inicial** | **0** | — | base | base | 0 | 2 Gu |
| **Médio** | **1** | **+1 por dado** | **+4 × M** | **+3 × M** | +1 | 3 Gu |
| **Alto** | **2** | **+2 por dado** | **+8 × M** | **+6 × M** | +2 | 4 Gu |
| **Pico** | **3** | **+3 por dado** | **+12 × M** | **+9 × M** | +3 | 5 Gu |

> Os "desbloqueios" extras por estágio (bônus em resistência e ordem de turno, ativações com desconto, Pico ignorar ½ RD) **foram removidos** (decisão 106): eram mais coisa pra lembrar do que efeito que se sentia, e a iniciativa agora é rolada. O estágio dá exatamente o que está na tabela acima, nada além.

**Reserva de essência:** continua dobrando a cada estágio (`% × 4 × 2^(estágio−1)`) — ela não é mais a atração principal, mas é o que paga os Golpes Matadores grandes que o Teto de Combo destrava.

### 1️⃣ Dano — o Grau é bônus por dado

O Grau entra direto no **B** da fórmula de [[⚔️ Combate|Combate]]:

```
DANO = M d(dado do Caminho) + (M × B)
```

**Por dado.** É isso que faz o estágio continuar importando no rank 9: no rank 1 o Pico soma +3 num dado só; no rank 9 soma +3 em 256 dados, ou **+768**.

> [!important] O Grau é o seu **teto** de bônus, não o bônus que você recebe de graça
> O estágio diz **até quanto** você pode comprar, e nada mais. Cada ativação você escolhe com que `B` quer o Gu, e paga por isso: **×1 (B 0) · ×1,5 · ×2 · ×3** sobre o custo ([[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]]). O custo base sempre entrega o Gu funcionando, com `B` 0. Subir de estágio não engorda o seu dano sozinho — **destrava uma compra mais cara**, e a decisão de fazê-la é por disparo.

| Caminho | Rank 1 Inicial | Rank 1 Pico | Crescimento |
|---|---|---|---|
| d6 (utilitário) | `1d6` — média 3,5 | `1d6+3` — média 6,5 | **+86%** |
| d8 (moderado) | `1d8` — média 4,5 | `1d8+3` — média 7,5 | **+67%** |
| d10 (dano alto) | `1d10` — média 5,5 | `1d10+3` — média 8,5 | **+55%** |
| d12 (letal) | `1d12` — média 6,5 | `1d12+3` — média 9,5 | **+46%** |

> **Repare que os Caminhos utilitários ganham mais.** Isso é de propósito: a Densidade é a compensação estrutural de quem rola o dado pequeno. Um Caminho de Terra no Pico bate quase como um de Lua no Inicial.

**A trava que mantém a escada honesta:** o Pico de um rank **nunca alcança o Inicial do rank seguinte**. Um d8 no Pico do rank 1 faz 7,5; no Inicial do rank 2 faz 9. Subir de rank continua sendo o salto grande — o estágio preenche o vale entre eles, que antes era plano.

### 2️⃣ Corpo e Alma — a pressão da essência endurece o cultivador

As fórmulas de [[❤️ Recursos e Dano|Recursos e Dano]] passam a incluir o estágio:

```
Vitalidade = (18 + 3 × CON + 4 × Grau) × M
Alma       = (16 + 3 × VON + 3 × Grau) × M
```

Isso mantém intacta a calibragem central do sistema: **um alvo com atributo 0 continua caindo em ~3 acertos de um Gu d10 do próprio rank, em qualquer estágio.** O dano e a carne crescem no mesmo compasso — o que cresce de verdade entre estágios é a distância pra quem ficou pra trás.

### 3️⃣ Vagas de Suporte — sustentar mais sem sobrecarregar a cabeça

O limite geral de Gu sustentados **não muda**: continua **3**, em qualquer rank e qualquer estágio. O que o estágio dá é uma segunda categoria de vaga, exclusiva:

```
Vagas de Suporte = Grau de Densidade    (0 · 1 · 2 · 3)
```

**Só entram nelas Gu de suporte:** movimento, sentidos, informação, comunicação, furtividade, utilidade logística. **Nunca** defesa (RD), amplificação (Níveis de Dano), ataque ou controle — essas continuam disputando as vagas normais, e é o que impede alguém de ligar seis Gu de defesa e virar invulnerável.

**Gu numa Vaga de Suporte não ocupam nenhuma das 3 vagas normais** e pagam só o custo individual deles. É literalmente "sustentar mais sem penalidade mental": a essência densa segura os Gu passivos sozinha, e a atenção do cultivador fica livre para as três coisas que decidem a luta.

> [!important] É por aqui que um cultivador maduro parece poderoso — não pelo teto de 3
> O teto de sustentação é de **atenção**, e atenção não cresce com o rank: um Venerável liga três Gu de combate, igual a um rank 1. O que muda é tudo em volta — os Gu são de outro patamar, a essência é densa, e o **estágio devolve até três Vagas de Suporte** que o corpo carrega sem pensar. Um rank 5 no Pico anda com voo, sentidos e comunicação ligados **de graça**, e ainda tem as três vagas inteiras livres pra luta. É a diferença entre ter mais mãos e ter mãos melhores.

### 4️⃣ Teto de Combo — Golpes Matadores mais complexos

```
Teto de Combo = número máximo de Gu num único Golpe Matador
Inicial 2  ·  Médio 3  ·  Alto 4  ·  Pico 5
```

O núcleo conta no total. Um personagem no Alto monta núcleo + 3 apoios (**+3 Níveis**); no Pico, núcleo + 4 apoios (**+4 Níveis**). Antes do Alto, um Golpe Matador de verdade simplesmente não cabe na cabeça do cultivador.

Custo e teste de conjuração seguem [[⚡ Golpes Matadores|Golpes Matadores]] sem alteração — e lembre que o custo cresce ao quadrado com o número de Gu, então o Teto de Combo destrava uma possibilidade, não uma rotina.

**O Golpe Matador Coletivo usa o Teto de Combo mais alto entre os participantes.**

### 5️⃣ Os nomes da essência por estágio

Puramente narrativo, e vale a pena usar: cultivadores **reconhecem a densidade alheia de vista**, e chamar a essência pelo nome certo é como esse mundo mede alguém sem perguntar.

| Rank | Inicial | Médio | Alto | Pico |
|---|---|---|---|---|
| **1** — Cobre Verde | Turvo | Claro | Puro | **Cristalino** |
| **2** — Aço Vermelho | Bruto | Temperado | Polido | **Espelhado** |
| **3** — Prata | Opaca | Clara | Pura | **Viva** |
| **4** — Ouro | Fosco | Batido | Puro | **Radiante** |
| **5** — Cristal Roxo | Nublado | Translúcido | Límpido | **Perfeito** |

---

### A Quebra de Paredes — o teste pra subir de rank

Ao acumular Essência suficiente no Pico, o personagem força a ruptura da própria Abertura contra a parede do próximo rank. Isso é um **teste real, com risco real** — não uma formalidade:

```
Teste de Ruptura = 1d20 + bônus de Aptidão vs. CD do salto
```

| Bônus por grau de Aptidão | D | C | B | A | Dez Físicos Extremos *(só NPC)* |
|---|---|---|---|---|---|
| **Bônus** | +0 | +2 | +4 | +6 | +10 |

| Salto | CD |
|---|---|
| Rank 1 → 2 | 10 |
| Rank 2 → 3 | 14 |
| Rank 3 → 4 | 18 |
| Rank 4 → 5 | 22 |

**Vantagem no teste** (rola 2d20, fica com o maior) se o personagem usar um Gu de impacto/ruptura apropriado, ou receber ajuda direta de outro cultivador infundindo essência.

> [!warning] Essência emprestada cobra o preço depois
> A ajuda de outro cultivador dá vantagem, mas **essência alheia não é gratuita**. Se o teste **falhar** com essência emprestada em uso, além do resultado normal o personagem **perde um grau de Aptidão permanentemente** (A → B → C → D; quem já é D perde 5 pontos percentuais da porcentagem dele). A Abertura foi forçada por uma essência que não era dela e a fundação não voltou ao que era.
>
> 📕 *Canônico:* o romance é explícito de que essências que se chocam dentro de uma Abertura causam *"great damage to the aperture"*, e que uma Abertura danificada tem consequências que *"range from having one's cultivation lowered to **having their latent talent lowered as well**"*. É a rota canônica do talento fraco que sobe porque alguém investiu nele — com o preço que a obra cobra. *(Decisão 255.)*

### O que acontece quando a ruptura falha

Falhar não é só perder o turno: é a essência acumulada do Pico inteiro ricocheteando dentro da Abertura.

| Resultado | O que acontece |
|---|---|
| **Passa** | Sobe de rank. O estágio volta ao Inicial e o M dobra — ver [[📈 O Que Muda ao Subir]] |
| **Falha por menos de 10** | **Escolha do jogador:** *(a)* **esperar** — a tentativa se encerra e ele só pode tentar de novo depois de reacumular a reserva do Pico ([[🧘 Ritmo de Cultivo e Cultivo Fechado]]); ou *(b)* **forçar agora** — sofre **1 Ferimento** e rola de novo imediatamente |
| **Falha por 10 ou mais** | **Retrocesso** (ver [[❤️ Recursos e Dano]]) e **a espera é obrigatória** — não dá pra forçar por cima de um ricochete desses |
| **1 natural** | **Regride um rank.** A parede não só resiste: a fundação abaixo dela racha. O personagem cai para o rank anterior, no estágio Pico dele |

> [!danger] Forçar escala, e escala rápido
> Cada forçada **seguida na mesma cena** custa mais que a anterior: a primeira cobra **1 Ferimento**, a segunda **2**, a terceira **3**, e assim por diante. Um personagem que insista quatro vezes paga **dez Ferimentos** — metade da Vitalidade e da Alma máximas, para sempre.
>
> **É por isso que esperar é o normal e forçar é desespero.** Na obra, cultivadores passam anos no Pico juntando coragem para uma tentativa; quem força é quem não tem tempo — o perseguido, o moribundo, o demoníaco. A regra deve fazer o jogador sentir isso na ficha, não só na narração. *(Decisão 255.)*

**Falha crítica (1 natural):** ver a tabela acima — o personagem **regride um rank** e cai para o Pico do rank anterior (decisão 255). *(A nota publicava aqui uma segunda versão desta regra, anterior e mais branda; arquivada em [[Regras removidas (2026-09-01 — varredura de texto)]].)*

Um **Gu Relíquia** avança um **estágio** na hora, sem teste — mas **não salta rank** (ver [[🚀 Gu de Avanço de Rank]]). Pro salto de rank não existe compra limpa: uma dose absurda de Pedras Primordiais infundida na ruptura concede **vantagem e +2** no Teste de Ruptura, e é o máximo que dinheiro faz aqui.

## A Ascensão Imortal (rank 5 → 6)

**O maior gargalo do jogo.** Ver [[♾️ A Ascensão Imortal|A Ascensão Imortal]] para o evento completo. Em resumo: a Abertura mortal se rompe, os Três Ares (Celestial, Terrestre, Humano) se equilibram, e o Gu Vital é catalisado, virando o primeiro Gu Imortal. Nasce a Abertura Imortal e, com ela, a [[🗝️ Terra Abençoada|Terra Abençoada]].

Chegar ao rank 5 Pico **não** dá direito de tentar. É preciso passar por um de dois portões: ter refinado um **Gu Imortal** (o que exige a cooperação de um [[🧿 Espíritos da Terra|Espírito da Terra]] — um mortal não refina Gu Imortal sozinho, nunca), ou ter usado com sucesso um **Golpe Matador de rank 5** contra alguém do próprio rank ou acima. A segunda rota funciona e é bem pior.

## Fase imortal — Imortal de Gu (rank 6 a 9)

**A partir daqui os estágios acabam.** Não existe "rank 6 inicial, intermediário, avançado, pico" — isso é estrutura de Abertura mortal, e a Abertura mortal se despedaçou na Ascensão. O que mede um Imortal é **quantas Marcas de Dao ele tem, e de qual Caminho** — ver [[☯️ Marcas de Dao|Marcas de Dao]], que é a nota principal de progressão daqui pra frente.

| Rank | Nome | Essência | Marcas de Dao | Provações |
|---|---|---|---|---|
| 6 | Sexto Giro | Uva Verde | 0 – 9.999 | Calamidade Terrestre (10 em 10 anos) / Provação Celestial (100 em 100 anos) |
| 7 | Sétimo Giro | Jujuba Vermelha (100 Uvas Verdes = 1) | 10.000 – 99.999 | + Grande Calamidade (100 em 100 anos, cada uma ordens de grandeza pior que a anterior) |
| 8 | Oitavo Giro | Lichia Branca (100 Jujubas = 1) | 100.000 – 299.999 | + Calamidade das Dez Mil Calamidades (100 em 100 anos) |
| 9 | Nono Giro — **Venerável** | Damasco Amarelo (1 = ~100.000.000 de Pedras Primordiais) | 300.000+ | Calamidade do Caos (a cada 100 anos) — quem morre por ela não pode ser ressuscitado |

### ⬆️ Como se sobe de rank depois da imortalidade *(decisão 108 — calibrado pelo cânone)*

Não é automático, não é ritual comprado e não exige Gu específico. O salto tem **três condições e um evento**, nesta ordem:

1. **Saturar o teto de Marcas do rank atual** — a Abertura "cheia" (9.999 no rank 6; 99.999 no rank 7). No teto, Marcas novas simplesmente não grudam mais: o cofre não fecha mais nada até ser trocado por um maior.
2. **Ter sobrevivido às provações do patamar:** **3 Provações Celestiais** para 6→7 · **3 Grandes Calamidades** para 7→8 · as **quatro condições de Venerável** para 8→9 (ver abaixo). É a régua canônica: dentro de um rank, o que mede um Imortal é quantas provações ele já atravessou — dá tipicamente ~300 anos de tempo interno por salto, menos pra quem acelera o fluxo da própria terra.
3. **Declarar a tentativa.** O céu responde na hora com a **Provação de Avanço**: uma Calamidade sob medida, nas 5 etapas completas de [[🌩️ Calamidades e Provações]], com a **CD do rank seguinte +2**. Preparação vale como sempre (presságios, terra Inabalável, Gu de Estabilização).

**Sucesso:** a Abertura converte. A essência muda de grau (a reserva de Uvas Verdes vira Jujubas a 100:1), o **teto de Marcas expande** pro patamar seguinte, as Marcas do próprio evento entram — é por isso que **todo rank 7 recém-convertido carrega ~10.000 Marcas**: o teto cheio do rank 6 mais o que a Provação de Avanço rendeu. No salto pro rank 8, a Terra Abençoada se transforma qualitativamente em **Gruta-Céu** (grotto-heaven — canônico).

**Falha:** sem avanço. 1 Ferimento, 1 Ferimento da Terra, e a próxima janela só abre depois de mais um ciclo de provação do patamar (~100 anos internos). Falhar duas Provações de Avanço seguidas marca o Imortal como **Estagnado** — o mundo inteiro passa a saber que ele bateu no teto.

> **O caso que confunde à primeira leitura:** um rank 6 "denso", com 9.000+ Marcas num Caminho só, **despacha um rank 7 recém-convertido com poucas Marcas naquele Caminho** — os Níveis de Dano que a densidade dá superam a diferença de M. Não há contradição: o rank 7 novo tem ~10.000 Marcas *somadas*, mas se estão espalhadas (ou se o Caminho relevante não é o dele), a densidade *naquele* confronto é menor. Rank diz o que se ativa; densidade de Marca no Caminho certo diz o quanto dói.

A mesa decide o ritmo real da campanha; os ~300 anos internos são o relógio do mundo, não obrigação de jogar 300 anos por sessão.

### A hierarquia da Essência Imortal

Cada grau vale **100 do grau abaixo**, e a conversão é o motor da economia imortal inteira:

| Rank | Essência | Vale | Em Pedras Primordiais comuns |
|---|---|---|---|
| 6 | **Uva Verde** (UV) | — | ~100 |
| 7 | **Jujuba Vermelha** (JV) | 100 UV | ~10.000 |
| 8 | **Lichia Branca** (LB) | 100 JV | ~1.000.000 |
| 9 | **Damasco Amarelo** (AA) | 100 LB | ~100.000.000 |

> *Nota de tradução: no romance o termo é **"red date"**, que a referência canônica do vault registra como **Tâmara Vermelha** ("red jujube" não aparece na obra). Alguns resumos traduzem como "lótus vermelha". É tudo a mesma essência de rank 7 — o vault padronizou **Jujuba Vermelha** por convenção interna, não por canonicidade.*

**Você produz apenas a essência do seu rank.** Um Imortal de rank 6 gera Uva Verde e mais nada; se ele quiser Jujuba, tem que comprar, roubar ou receber.

### Ativar um Gu Imortal acima do seu rank

Dá pra queimar essência de grau inferior pra alimentar um Gu Imortal de rank superior — mas o câmbio é **ruinoso de propósito**:

```
Custo em essência de grau inferior = custo normal × 100 por rank de diferença,
E MAIS um agravante de 50% sobre o total.
```

| Situação | Custo |
|---|---|
| Rank 6 ativando um Gu de **rank 7** que custaria 5 JV | `5 × 100 × 1,5` = **750 UV** |
| Rank 6 ativando um Gu de **rank 8** que custaria 2 LB | `2 × 100 × 100 × 1,5` = **30.000 UV** — inviável, e é pra ser |

**Mais:** o Gu **não coopera**. Teste de VON `CD 20 + (5 × diferença de rank)` — falhando, o Gu age uma vez e **entra em coma místico por `1d6` meses**. E cada ativação assim custa **1 Ferimento**, como toda Ativação Forçada.

### As quatro condições pra virar Venerável (rank 8 → 9)

Um Imortal de Oitavo Giro só se torna Venerável cumprindo **todas** estas condições ao mesmo tempo:

1. Já produzir Essência Imortal de Lichia Branca (ou seja, estar de fato no Oitavo Giro).
2. Ter pelo menos 300 mil Marcas de Dao no seu Caminho principal.
3. Ter atingido, nesse Caminho, o nível de domínio de **Grande Mestre Supremo** ([[☯️ Marcas de Dao|Marcas de Dao]]).

> [!important] As condições 2 e 3 são coisas **diferentes**, e é aí que a maioria falha
> Elas parecem redundantes e não são: **Marcas são estoque, Domínio é compreensão**, e desde a decisão 254 os dois eixos sobem por caminhos separados. Juntar 300.000 Marcas é questão de séculos e de sobreviver; chegar a Grande Mestre Supremo é questão de **entender o Caminho**, e não acontece por acúmulo nenhum.
>
> O romance mostra exatamente esse fracasso: um candidato que **tinha as Marcas** e mesmo assim não ascendeu, porque lhe faltava o domínio. **É a forma mais comum de um Imortal poderosíssimo nunca virar Venerável** — e é o tema do romance dito em regra: compreender vale mais que possuir.
4. Romper o bloqueio do Dao Celestial — uma provação ainda mais brutal que a Calamidade das Dez Mil Calamidades.

Cumprir três das quatro e falhar na última é uma tragédia de campanha em si — existe precedente narrativo de cultivadores poderosíssimos que nunca conseguiram completar a quarta condição.

> [!important] As condições 2 e 3 se cumprem ANTES do salto — e é aí que está a dificuldade
> Uma versão anterior desta nota dizia que era *matematicamente impossível* ter 300.000 Marcas num Caminho antes de tentar, porque o rank 8 tinha um teto duro de 299.999. **Esse teto não existe mais** (decisão 218): as faixas por rank viraram descritivas, e um Imortal que fica no rank 8 sobrevivendo a tribulações continua gravando Marcas normalmente.
>
> Então a conta agora é direta, e mais dura do que a antiga: **o candidato precisa chegar aos 300.000 no Caminho principal por acúmulo real, antes de declarar a tentativa.** Como parte das Marcas dele inevitavelmente caiu em outros Caminhos, o **total** dele estará bem acima disso — e cada Marca acima do topo da faixa do rank 8 cobra escalada da [[⛈️ A Vontade do Céu#Excesso de Marcas — o preço de ficar|Vontade do Céu]] sobre todas as Calamidades seguintes. **Virar Venerável é atravessar anos de tribulações agravadas de propósito, para juntar uma contagem que ninguém precisa ter.**
>
> É isso, e não um teto artificial, que torna **Venerável coisa de especialista**: quem repartiu as Marcas entre dois Caminhos precisa de aproximadamente o dobro do total para chegar aos mesmos 300.000 num só — e paga a escalada do céu o caminho inteiro. É possível. É o modo mais difícil que existe de fazer isso.

### 🚧 O bloqueio do Dao Celestial — a quarta condição

**É a única provação do jogo que não está no calendário.** Calamidades e Provações chegam a cada 10, 50 ou 100 anos internos, previsíveis e calculáveis ([[🌩️ Calamidades e Provações]]). O bloqueio não: ele **acontece quando o candidato declara a tentativa**, e é maior que qualquer Calamidade das Dez Mil.

**Por que existe:** o Dao Celestial não quer que o número de Imortais cresça enquanto eles ficam mais fortes. As Calamidades e Provações de toda a fase imortal já são parte desse bloqueio — o freio contínuo. O que vem no salto para o rank 9 é o freio **inteiro de uma vez**, e ele se manifesta em três frentes simultâneas:

| Frente | O que faz |
|---|---|
| **Destino** | O mundo conspira contra a tentativa: coincidências ruins, aliados indisponíveis, inimigos que chegam na hora exata. Trate como a faixa **Alvo do Céu** da [[⛈️ A Vontade do Céu]], com Fichas de Azar sem limite por rodada |
| **Longevidade** | O relógio do candidato encurta durante a prova. Se ele não fecha a tentativa dentro do prazo que lhe resta, morre de velhice no meio dela ([[⏳ Longevidade]]) |
| **A provação** | Uma Calamidade acima de tudo que ele já enfrentou: **cinco etapas, CD 20 + faixa do Contador, e o dano de cada etapa falhada é dobrado** |

**As duas contramedidas conhecidas** — e a existência delas é o que impede o bloqueio de ser uma parede lisa:

- **Caminho Humano.** Todo Venerável da história desenvolveu um golpe supremo de Caminho Humano para atravessar o bloqueio. É a rota "oficial", e explica por que o Caminho Humano — que parece genérico e fraco na fase mortal — é o Caminho que mais aparece no topo.
- **Caminho da Sorte.** A rota alternativa: torcer o próprio destino em vez de resistir a ele. Cara, sutil e impossível de provar a terceiros.

E existe a rota suja, que a mesa deve conhecer porque um vilão pode ter usado: **empilhar tribulação sobre tribulação** — disparar o bloqueio no meio de outra Calamidade, para que ninguém consiga distinguir o que está acontecendo nem interferir. Funciona. É insano.

> **Pro mestre:** esta é a última cena de uma campanha que chegou ao fim do mapa. Não a role no meio de uma sessão — ela é a sessão. E as três frentes existem justamente para que os outros jogadores tenham o que fazer enquanto um deles tenta: alguém segura os inimigos que o Destino trouxe, alguém resolve o problema da Longevidade, e o candidato enfrenta a provação.

### Venerável × Venerável Demônio

Ambos são rank 9 — o mesmo teto de poder. **A diferença é de posição social, não de Caminho e nem de moral:** "reto" e "demoníaco" descrevem como o cultivador se coloca diante das estruturas estabelecidas (clãs, seitas, alianças), e não uma escala simples de bem contra mal. Um Venerável ortodoxo chegou ao topo **dentro** dessas estruturas e com o aval delas; um **Venerável Demônio** chegou **fora** delas — sozinho, contra elas, ou por meios que elas condenam — e é caçado por isso onde quer que vá.

Na mesa isso vira uma pergunta prática, não uma etiqueta de alinhamento: **quem abre a porta pra ele e quem manda matá-lo.** Caminhos como Sangue e Escravidão praticamente garantem o rótulo demoníaco porque nenhuma facção ortodoxa os tolera — mas o rótulo vem da posição, não do Caminho: existe Venerável Demônio de Caminho banal, e existe ortodoxo de mãos muito sujas. Mecanicamente idênticos — narrativamente, um é lenda, o outro é pesadelo.

**Senhor do Dao:** um Venerável que refina por completo as marcas naturais do seu Caminho vira Senhor do Dao — dentro do próprio domínio, cada ação dele recebe amplificação automática do céu e da terra. Só outro Venerável rivaliza com um Senhor do Dao.

## Diferença de rank em combate

1 ponto de Verdadeira Essência de um rank acima vale **10 pontos** de essência de um rank abaixo. Isso significa: rank contra rank adjacente já é brutalmente difícil de virar sem truque; nível mortal contra nível imortal é esmagamento total, sem exceção. Ver [[⚔️ Combate|Combate]] pra como isso vira número de dano na mesa.
