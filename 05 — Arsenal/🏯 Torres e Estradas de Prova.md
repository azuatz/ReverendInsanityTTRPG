---
tags:
  - regra
  - item
  - guia
aliases:
  - Torres e Estradas de Prova
escopo: sistema
---

# 🏯 Torres e Estradas de Prova

**Role uma masmorra de andares inteira em minutos** — irmã do [[🎲 Gerador de Heranças]], mas pra "coisa que se explora em grupo", não "coisa que se herda sozinho". Duas ferramentas nesta nota: um **gerador** de torre/masmorra de rounds crescentes (Parte 1) e uma **variante de regra** de dificuldade auto-escalada (Parte 2), útil pra qualquer masmorra ou expedição — a Parte 2 resolve especificamente o problema de desafiar personagens de poder muito diferente com o mesmo conteúdo, comum em rank 7–9. Criada na consolidação da Frente 3 da leitura integral do romance (decisão 145).

---

## Quando usar qual

| Situação | Use |
|---|---|
| Precisa de "uma masmorra pra explorar hoje", com andares, recompensa e talvez PvP | **Parte 1 — o gerador** |
| O grupo tem personagens de rank bem diferente (um rank 7, um rank 9) e a mesma CD fixa deixaria um entediado e o outro morto | **Parte 2 — a variante de dificuldade auto-escalada**, sobre qualquer masmorra (inclusive uma rolada na Parte 1) |
| Já tem uma herança rolada em [[🎲 Gerador de Heranças]] e só falta a "provação" dela | Use a provação de lá — esta nota é pra estrutura maior, multi-sessão, feita pra grupo, não pra herança pessoal |

---

## Parte 1 — O gerador de masmorra de andares

**Sequência:** rank e andares → recompensa por round → sala de tesouros → pilares temáticos (opcional) → PvP e a exceção de autodetonação (opcional) → token de dono e arestas (opcional) → entrada. Cada passo é uma rolagem.

### 1º — O rank e a CD base

Escolha o rank da masmorra (mortal ou imortal) pelo que a campanha precisa. **CD base do 1º andar**, mesma fórmula do [[🎲 Gerador de Heranças]]:

```
CD = 12 + 2 × (rank da masmorra − 4) + severidade (1d4 − 2)
```

### 2º — Quantos andares — `1d6`

| 1d6 | Andares | Uso |
|---|---|---|
| 1–3 | **1 andar** | Masmorra de sessão única |
| 4–5 | `1d4 + 1` andares | Arco de médio prazo |
| 6 | `1d6 + 3` andares | Arco de campanha inteira |

Cada andar novo soma **+2 na CD base** do anterior (mesmo passo que separa um rank do próximo nas tabelas do vault). Dentro de cada andar, não role round a round: divida-o em **`1d4 + 2` blocos** narrados em montagem (cada bloco resume um punhado de rounds); a CD sobe **+1 por bloco avançado** — o último bloco do andar é sempre o mais duro, o primeiro é o mais fácil.

### 3º — Recompensa por bloco vencido — `1d6`

| 1d6 | Faixa | Efeito |
|---|---|---|
| 1–3 | **Baixa** | Recompensa comum pro rank do andar ([[🏪 O Mercado]] / [[🏪 Céu Amarelo do Tesouro]] pra preço de referência) |
| 4–5 | **Média** | O dobro da faixa baixa |
| 6 | **Alta** | **2× a faixa média** e acesso a uma **sala de tesouros** à parte (passo 4) |

### 4º — A sala de tesouros

Um cômodo separado do bloco, alcançado só por resultado Alto no passo 3. Tudo lá dentro se troca por **valor equivalente** — o grupo entrega algo (Gu, receita, material) e recebe algo de preço igual ou menor da mesma sala; nada sai de graça, e nada de fora entra sem essa troca.

### 5º — Pilares temáticos e supressão *(opcional)* — `1d6`

| 1d6 | Estrutura |
|---|---|
| 1–4 | **Aberta.** Qualquer Gu funciona normalmente em qualquer bloco |
| 5–6 | **Dividida em pilares.** `1d3 + 1` pilares, cada um role/escolha um Caminho ([[🛤️ Os Caminhos]]). **Dentro de um pilar, só um Gu de rank 1–2 daquele Caminho funciona — todo o resto é suprimido** (supressão absoluta, mais dura que a de [[🗺️ Supressão Regional]], que só rebaixa um rank) |

### 6º — PvP e a exceção de autodetonação *(opcional)* — `1d6`

| 1d6 | PvP interno |
|---|---|
| 1–3 | **Cooperativa.** Sem PvP — as únicas ameaças são as do mestre |
| 4–6 | **Liberado a partir da metade dos blocos do andar** (ex.: bloco 3 de 5) |

Se liberado, role de novo pra saber se a masmorra muda a regra de saque de PvP: **`1d6`: 1–3 segue o padrão normal** ([[⚰️ Espólio]] — a vontade do morto destrói os próprios Gu); **4–6 é uma EXCEÇÃO LOCAL**: a Vontade da estrutura suprime a autodetonação de quem morre lá dentro, e o vencedor simplesmente extrai tudo do cadáver, na hora. **Isto não muda a regra em nenhum outro lugar do mundo** — é uma propriedade da masmorra, não uma revisão de [[⚰️ Espólio]], e a mesa deveria anunciar isso aos jogadores antes de entrarem: muda completamente o cálculo de risco de caçar outro grupo lá dentro em vez de só explorar.

### 7º — Token de dono e arestas *(opcional, trilha secundária)*

Qualquer personagem pode gastar uma ação de exploração (teste de AST contra a CD do bloco atual) pra achar uma **falha estrutural** — não conta como o desafio normal do bloco, é bônus à parte. Sucesso dá **1 aresta**. Acumular `1d6 + 4` arestas (5–10, decida no início e não revele o número exato) destrava um **domínio secreto**: uma sala extra com prêmio **um tier acima** do normal daquele andar (se o andar dá tesouro de rank 4, o domínio secreto dá rank 5). Decida se as arestas são por personagem ou por grupo.

### 8º — Entrada — `1d6`

| 1d6 | Custo de entrada |
|---|---|
| 1–2 | **Pedras fixas** na porta (referência: `~100 × rank²`, [[💠 Economia das Pedras Primordiais]]) |
| 3–4 | **Percentual dos ganhos** prometido ao controlador da estrutura, selado em Gu de Juramento (10–30%, ver [[🎲 Gerador de Heranças]] 6º passo) |
| 5–6 | **Os dois** |

Convidados sem token próprio entram com **token emprestado** de um membro — normalmente restrito aos andares mais baixos, nunca ao domínio secreto do passo 7.

---

## Parte 2 — Estrada de Prova (dificuldade auto-escalada)

**Não é uma estrutura nova — é uma variante de regra** que troca a CD fixa de qualquer masmorra, trial ou expedição por uma régua que se ajusta a quem anda. Use quando precisa desafiar personagens de poder muito diferente com o **mesmo** conteúdo, sem nivelar artificialmente pra baixo nem instamatar o mais fraco — o problema clássico de rank 7–9, onde a distância de poder entre PJs (ou entre PJ e NPC) fica grande demais pra uma CD única funcionar pros dois.

### Como a régua se ajusta

A CD de cada trecho não vem do rank da masmorra — vem do rank de **quem anda**. Mesma fórmula do 🎲 Gerador de Heranças, rank do personagem no lugar do rank da herança:

```
CD do trecho = 12 + 2 × (rank do andarilho − 4) + variância (1d4 − 2)
```

Um rank 9 e um rank 7 na mesma estrada rolam contra CDs diferentes ao mesmo tempo, cada um contra a própria régua. Ninguém acha a estrada trivial; ninguém a acha impossível.

### O custo é proporcional, não fixo

Cada trecho gasta uma fatia de um recurso — Vitalidade, Alma **ou** Essência (escolha pelo tema do trecho, ou `1d3`) — sempre em **porcentagem do máximo**, nunca número fixo:

- **Sucesso:** −10% do recurso escolhido
- **Falha:** −25% do recurso escolhido. A estrada desgasta — não mata. Quem mata é o Predicament, abaixo

### Recompensa: só o difícil paga

Antes de cada trecho, role a dificuldade narrativa: `1d6` → **1–3 trecho fácil** (sem recompensa — é o respiro) · **4–5 trecho médio** (faixa baixa/média do passo 3 da Parte 1) · **6 trecho difícil** (faixa alta — 2× e acesso à sala de tesouros, se a estrada tiver uma).

### Predicaments — os mini-chefes que isolam

Em qualquer trecho, `1d6` = 6: o trecho vira um **Predicament**. O andarilho é puxado sozinho pra um combate isolado — ninguém mais entra, nem pra ajudar — contra um guardião montado com os moldes de [[⚔️ Ameaças Genéricas por Rank]] (molde Chefe), **no rank do próprio andarilho**, não no rank nominal da estrada. Vence: sai com a recompensa do trecho ×2. Perde: ejetado com o pior resultado de falha (−50% do recurso escolhido, e um Ferimento se a mesa quiser letalidade real).

### Cooperação e o preço de quebrar

Vários personagens podem andar a mesma edição da estrada juntos e combinar dividir o que acharem — cooperar não muda as réguas individuais, cada um ainda rola contra o próprio CD. **Quebrar um acordo de divisão dispara perseguição coletiva**: todo outro participante daquela edição — PJ ou NPC — fica sabendo e vira, coletivamente, inimigo do traidor até o fim da expedição ou até ele compensar. Trate como Débito automático e público (ver [[🤝 O Débito]], "Débito sem Gu") — a palavra quebrada em público já é a prova, não precisa de juramento prévio.

### Quando usar

Rank 7–9, sempre que o grupo tiver poder desigual e a mesma peça de conteúdo precisar valer pros dois extremos. Também serve **dentro** de um andar da Parte 1: troque a CD fixa do bloco pela CD pessoal desta seção, e a mesma torre vira jogável por personagens de ranks bem diferentes ao mesmo tempo.

---

## Exemplo rolado em minutos

`1d6`=5 → **rank 6** (imortal) · andares: `1d6`=4 → `1d4+1`=**3 andares** (CD sobe +2 por andar) · blocos por andar: `1d4+2`=**5** · pilares: `1d6`=6 → **dividida em 3 pilares** (`1d3+1`): Refino, Formações e Leis — cada um só libera Gu rank 1–2 daquele Caminho · PvP: `1d6`=5 → liberado a partir do bloco 3 de 5 · autodetonação: `1d6`=5 → **exceção local**, o vencedor extrai tudo do cadáver · arestas: trilha ativa, `1d6+4`=7 destravam o domínio secreto · entrada: `1d6`=4 → **20% dos ganhos** jurados ao controlador, em Gu de Juramento.

*Ponta a ponta, isto é a estrutura de um evento de attainment coletivo: rodadas de dificuldade crescente, disputa por posto que afunila quanto mais alto o bloco, e um prêmio raríssimo no topo. O romance tem exatamente isso — a Convenção do Caminho de Refino do Continente Central, evento a cada 100 anos —, e o vault já fichou o prêmio de topo dela: o [[🚀 Gu de Avanço de Rank|Gu das Cem Batalhas Invicto]] (r5, Refino), sucesso automático garantido no próximo refino, um por campanha no máximo. A mesa não precisa reconstruir a Convenção do zero — é este gerador, rolado uma vez, com o prêmio já fichado no catálogo do vault.*

---

**🔧 adaptado do romance** (decisão 145 — ver Frente 3 da [[🔍 Síntese — Atividades Jogáveis por Rank]]). Consolida três padrões de masmorra do romance num gerador só, sem nomes de personagens: uma torre de andares/rounds com sala de tesouros e trilha oculta de "arestas"; uma herança dividida em pilares temáticos onde quem morre em PvP interno não autodetona os próprios Gu (a exceção local do passo 6); e uma expedição cuja dificuldade se ajusta à força de cada andarilho, com mini-chefes que isolam o desafiante (Parte 2). Números novos, calibrados pela fórmula de CD já validada do [[🎲 Gerador de Heranças]] e pelas faixas de preço de [[🏪 O Mercado]] / [[🏪 Céu Amarelo do Tesouro]]; sem simulação própria.
