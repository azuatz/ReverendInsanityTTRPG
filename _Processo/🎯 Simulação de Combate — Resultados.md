---
tags:
  - processo
  - balanceamento
  - simulação
aliases:
  - Simulação de Combate — Resultados
escopo: processo
---

# 🎯 Simulação de Combate — Resultados

Auditoria quantitativa do sistema em Monte Carlo, **3.000 combates por cenário**, com os quatro personagens da mesa, rodada nos **ranks 1, 2, 3 e 5**.

> [!info] O que o modelo implementa
> Ordem de turno por Destreza sem rolagem · `Acerto = d20 + atributo + (rank + 2) + rank do Gu + treino` contra Defesa · Escada de Dano completa com `× M` · RD com piso de `1 × M` e não-empilhamento · dano de Alma ignorando RD · Essência com **escala por estágio** (`% × 4 × 2^(estágio−1)`), regeneração base (`% ÷ 10`) e teto · Manutenção de Sustentação quadrática, com o personagem **desligando um Gu sustentado** quando a Essência cai abaixo de 25% · dano melee pela decisão 64 (`(dado × M) + FOR`) · **Golpe Matador** com custo, teste de conjuração, multiplicador híbrido e Retaliação · **cura** (`1d8 × M` quando um aliado cai abaixo de 40%) · **condições de controle** (Lentidão custando ação, e o Chefe ignorando a primeira) · **terreno** Wu Xing (±2 Níveis) · **hordas** e **ações especiais** de inimigo.
>
> **Premissa de catálogo:** todo personagem tem o Gu de ataque do próprio rank, em todo rank. O catálogo do vault é para ser completo — onde o tipo de Gu faz sentido para o Caminho, ele existe. Uma lacuna é item a escrever, nunca um dado de balanceamento.

---

## As quatro fichas simuladas

| | **Xie Lang** | **Jiāotáng** | **Lee** | **Demvi** |
|---|---|---|---|---|
| Caminho | Lua + Alma | Sangue + Força | Cinco Elementos | Vento |
| Aptidão | 86% | 76% | 63% | 56% |
| FOR/CON/DES | −1 / +3 / +3 | +4 / +3 / +2 | +3 / +2 / +2 | −1 / +1 / +4 |
| AST/VON/CAR | +2 / +3 / +2 | +1 / +1 / 0 | +1 / +3 / +1 | +2 / +3 / +2 |
| Papel no modelo | Controle + Golpe híbrido | Melee, paga em Vitalidade | Melee versátil + cura | Defesa alta, controle |

Estágio acompanha o rank (rank 1 → Inicial, rank 4+ → Pico), que é o que a progressão do vault espera.

---

## 🔴 O achado principal: os moldes atuais não ameaçam

Linha de base, com as composições que a nota de [[⚔️ Ameaças Genéricas por Rank|Ameaças]] recomenda hoje:

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** — 6 Recrutas | 100% · 4,0 vivos | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Padrão** — 2 Guerreiros + 4 Recrutas | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Difícil** — 1 Elite + 2 Guerr + 2 Recr | 100% · 3,9 | 100% · 3,9 | 100% · 3,8 | 100% · 3,8 |
| **Clímax** — 1 Chefe + 1 Guerreiro | 96% · 3,3 | 92% · 3,0 | 48% · 1,2 | 76% · 2,0 |

*(vitória do grupo · sobreviventes de 4)*

**Fácil, Padrão e Difícil terminam com os quatro personagens de pé, em todos os ranks, sem exceção.** Não é que sejam fáceis — é que três das quatro categorias não existem mecanicamente. Só o Clímax ameaça, e mesmo ele só a partir do rank 3.

A causa é simples e está na própria nota de Ameaças: o que machuca é **ação inimiga por rodada**, e as composições atuais entregam de 2 a 6. Aumentar a Vitalidade ou o dano do molde não resolve — inimigo com mais vida só alonga a cena. O que falta é *volume de ações* e *dano que a RD não coma*.

---

## 🟢 Os três moldes novos

### 1. A Horda — recrutas como uma unidade só

Recrutas individuais morrem antes de agir: um PJ de rank N mata um Recruta por golpe. A economia de ação deles nunca se materializa. A correção é tratá-los como **uma entidade**:

- **Vitalidade somada:** `4 × M × (nº de membros)`.
- **Um ataque por personagem de pé** — cerco, não iniciativa individual.
- **O passo sobe com o tamanho:** `−1, +1 Nível a cada 4 membros vivos`. Uma horda de 12 bate no passo **+2** (`1d10 × M`); conforme morre, o passo desce sozinho.
- **Acerto `d20 + rank + 6`** (o +2 é o cerco).

O passo decrescente é a peça boa: o grupo **sente** a horda enfraquecendo, sem ninguém precisar contar cadáveres.

### 2. Ação Especial — uma por inimigo, uma vez por cena

Todo Guerreiro e Elite ganha **uma** ação especial, usada uma vez por cena: um ataque com **+2 Níveis** que também aplica **Lentidão 2**. Custa nada de estatística e muda a cena, porque tirar ação de um PJ vale mais que tirar Vitalidade.

### 3. Mestre de Gu humano — o molde que faltava

Inimigo humano cultivador, e não uma fera com números. É o molde mais útil do conjunto porque é o que o cenário produz o tempo todo.

| | Mestre de Gu |
|---|---|
| **Vitalidade** | `14 × M` |
| **Defesa** | `13 + rank` |
| **RD** | `1 × M` (Gu de defesa sustentado) |
| **Acerto** | `d20 + rank + 7` |
| **Ações** | **2 por rodada** |
| **Ataque** | Gu do próprio rank, passo 0 (`1d6 × M`) |
| **Ação Especial** | Gu de **Alma**: `1d8 × M`, **ignora RD**, e aplica Lentidão 2 |

**A especial de Alma é o que faz o molde funcionar.** A RD `1 × M` que todo PJ carrega come ~40% de um golpe comum; o dano de Alma passa inteiro e ainda bate num trilho que quase ninguém protege. Um Mestre de Gu com 2 ações e um golpe que ignora armadura é uma ameaça real com metade da Vitalidade de um Chefe.

---

## 📊 A curva: vitória do grupo por ações inimigas/rodada

| Composição | ações/rodada | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|---|
| Horda de 8 | 4 | 100% | 100% | 100% | 100% |
| Horda de 12 + 1 Guerreiro especial | 5 | 100% | 100% | 97% | 99% |
| **3 Mestres de Gu** | **6** | **99%** | **98%** | **97%** | **98%** |
| 2 Mestres + Horda de 8 | 8 | 97% | 94% | 93% | 96% |
| **4 Mestres de Gu** | **8** | **76%** | **63%** | **56%** | **60%** |
| 1 Elite especial + 3 Mestres | 7 | 67% | 53% | 44% | 44% |
| 3 Mestres + Horda de 12 | 10 | 31% | 19% | 6% | 10% |
| 1 Chefe + 1 Guerreiro | 5 | 96% | 92% | **48%** | 76% |
| Chefe + 2 Mestres | 7 | 24% | 12% | 0,7% | 2,4% |

Três leituras que importam:

**1. Fora o Chefe, a curva é estável entre ranks.** Uma vez corrigido o uso do Golpe Matador (ver abaixo), a mesma composição entrega dificuldade parecida do rank 1 ao 5 — a variação restante é de 10 a 20 pontos na ponta difícil, com o rank 1 sendo o mais leve. **A exceção é o Chefe**, que oscila de 96% no rank 1 a 48% no rank 3 e 76% no rank 5: as 3 ações fixas dele não acompanham nada que escala.

**2. Nem toda ação vale o mesmo.** Oito ações de 4 Mestres (56–76%) são muito piores para o grupo que oito ações de 2 Mestres + Horda (93–97%), porque as do Mestre vêm com dano de Alma que ignora RD e com Lentidão, e as da horda não. **Conte ações ponderadas: uma ação com especial vale duas comuns.**

**3. O Golpe Matador contra alvo errado perde a luta.** Na primeira rodada desta auditoria, a IA dos personagens disparava o Golpe Matador contra qualquer alvo de Elite ou acima. Isso sozinho derrubava a vitória do grupo de **97% para 76%** no rank 3, e criava um "vale do rank 3" que parecia propriedade do sistema e não era. Restringindo o disparo a alvos de Chefe, o vale desaparece por completo. **Não é bug do sistema — é o sistema funcionando:** o custo `(soma dos custos) × nº de Gu`, dobrado se híbrido, torna o Golpe Matador um recurso de arco, e gastá-lo com um inimigo mediano custa a cena. Vale documentar isso para os jogadores, porque a punição é severa e não é óbvia na ficha.

---

## 🌍 Terreno

Difícil (1 Elite + 2 Guerreiros + 2 Recrutas), rank 3, variando só o dial de terreno do Lee:

| Terreno | Vitória | Sobreviventes |
|---|---|---|
| **−2** (hostil ao elemento dele) | 92,2% | 2,64 |
| **0** (neutro) | 94,8% | 2,75 |
| **+2** (favorável) | 95,9% | 2,81 |

**O terreno mexe pouco quando só um personagem o sente** — cerca de 4 pontos percentuais de ponta a ponta. É o esperado, e é a favor do desenho: o dial dos Cinco Elementos é uma alavanca tática do Lee, não um botão que decide a cena. Numa mesa com dois ou mais personagens elementais o efeito dobra, e aí vale o mestre declarar o terreno antes da iniciativa.

---

## ✅ O que mudou por causa desta rodada

1. **Três moldes novos** — Horda, Ação Especial e Mestre de Gu — escritos em [[⚔️ Ameaças Genéricas por Rank]].
2. **A tabela de composição passou a ser por rank**, porque a curva acima mostra que uma tabela única erra.
3. **A contagem de ações virou ponderada:** ação com especial conta como duas.

### Correção de uma conclusão anterior

A rodada anterior concluiu que *"o que decide o poder de um personagem é se o Caminho dele tem um Gu de ataque no rank em que ele está"* e recomendava conferir isso antes de subir a mesa de rank. **Isso estava errado como princípio de design.** O catálogo do vault é para ser completo: todo personagem tem o Gu de ataque do próprio rank. Onde falta um, o que falta é escrevê-lo — não é um fato sobre o sistema nem um risco que o mestre precise contornar. Ver a decisão 69 no [[🧭 Log de Decisões]].

---

## 🔁 Terceira rodada — com o arsenal completo

Depois que os **50 Gu novos** fecharam a cobertura de ataque e de utilidade do catálogo, a simulação foi rodada de novo com as ações de Chefe da decisão 72:

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** — Horda de 8 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Padrão** — 3 Mestres de Gu | 99% · 3,6 | 98% · 3,5 | 98% · 3,4 | 98% · 3,3 |
| **Padrão pesado** — 2 Mestres + Horda de 8 | 97% · 3,0 | 94% · 2,7 | 94% · 2,5 | 95% · 2,4 |
| **Difícil** — 4 Mestres de Gu | 75% · 2,3 | 63% · 1,8 | 56% · 1,5 | 59% · 1,5 |
| **Clímax** — 1 Elite especial + 3 Mestres | 68% · 2,0 | 53% · 1,4 | 44% · 1,1 | 46% · 1,1 |
| **Clímax** — 1 Chefe + 1 Guerreiro especial | 56% · 1,7 | 62% · 1,5 | 80% · 2,1 | 73% · 2,0 |

**Os números praticamente não se moveram**, e isso é o resultado que importa. A simulação sempre assumiu que todo personagem tinha o Gu de ataque do próprio rank — que é a premissa correta do projeto. **Escrever os 50 Gu não mudou a matemática; fez o catálogo entregar o que a matemática já assumia.** A tabela de encontros continua válida, e agora está apoiada num arsenal que existe de verdade.

A única linha que se mexeu foi a do **Chefe**, por causa das ações medidas por rank: ela saiu de 96%/92%/48%/76% para **56%/62%/80%/73%**, bem mais perto de um clímax de verdade nas três primeiras faixas. O rank 3 com 2 ações ficou o mais leve dos quatro — se a mesa quiser apertar, **3 ações no rank 3 leva a vitória a 45%**, e é o clímax mais duro que o sistema entrega sem sair do jogável.

---

---

## 🌠 Quarta rodada — o Físico Extremo vale o que cobra? *(2026-08-28)*

20.000 carreiras por cenário, do rank 6 até 10.000 Marcas (o piso do rank 7), em tempo interno.

### ⚠️ Dois artefatos do modelo, corrigidos antes de qualquer conclusão

**Nenhum dos dois é problema do sistema.** Ficam registrados porque a primeira rodada de números estava errada por causa deles.

1. **A primeira versão matava todo mundo por Ferimento da Terra.** O modelo acumulava Ferimentos da Terra sem nunca reparar — mas reparo é regra explícita (50 PEI e 3 meses internos por nível), e qualquer Imortal com renda de camada 3 paga isso sem sentir. Corrigido para reparar 1 nível por década.
2. **A segunda versão matava todo mundo na Provação Celestial** — 93% a 100% de morte, para o Imortal comum inclusive. O modelo estava simulando um Imortal **despreparado**: sem Gu de Estabilização, sem presságio respondido, sem terra Inabalável, sem aliado. A nota de [[🌩️ Calamidades e Provações]] trata os três presságios como obrigatórios e as reduções como o caso normal.

### 📊 A preparação **é** o sistema

Chance de atravessar o rank 6 vivo, do mesmo personagem, mudando só a preparação:

| | Despreparado | Típico *(−3 e 2 presságios)* | Bem preparado *(−3, 3 presságios, Inabalável, aliado)* |
|---|---|---|---|
| **Imortal comum** | **2,2%** | 48,3% | **70,2%** |
| **Físico Extremo** | 0,0% | 4,2% | **20,2%** |

**Isto valida o pilar inteiro**, e vale mais que qualquer outro número desta nota: sem preparação, o ato imortal é intransponível para qualquer um. Não há ajuste a fazer.

### 🔴 Achado 1 — a Pressão da Abertura é matematicamente fatal depois da Ascensão

| Cenário *(bem preparado, terra Inabalável)* | Chega ao rank 7 | Anos internos | Perda de Vitalidade |
|---|---|---|---|
| Imortal comum | **70,2%** | 292 | — |
| Físico, +5 de CD, **Pressão desligada** | 20,7% | 233 | — |
| Físico, +5 de CD, **Pressão ligada** | **0,0%** | — | **100%** |
| Físico, com **Selo de Limite Sombrio** | 20,4% | 232 | — |

A Pressão sobe **+1 a cada 6 meses** e só zera ao **subir de rank**. Na fase mortal isso funciona: rank sobe a cada 1–2 anos, a Pressão chega a 2–4 e o teste de CON passa. Na fase imortal o próximo rank leva ~250 anos internos — **500 testes com a CD subindo sem teto**. Por volta do vigésimo teste a CD é 30 e a falha é automática; vinte falhas são −100% de Vitalidade máxima e autoexplosão. **Todo portador de Físico Extremo que ascende morre em cerca de uma década, sempre.**

O Selo de Limite Sombrio resolve, e a nota já o descreve — mas como recurso opcional e caro, não como obrigação. **A regra não diz o que acontece com a Pressão depois da Ascensão, e é essa omissão que produz o zero.** Ver decisão 97.

### 🟡 Achado 2 — o +5 de CD é caro, e compra velocidade

O Físico troca **70,2% → 20,7%** de chance de atravessar o rank, e recebe em troca **61 anos internos a menos** (233 contra 292) por causa das Marcas em dobro. Ele não é melhor nem pior: é **três vezes e meia mais mortal e um quarto mais rápido**. Isso é coerente com o que a nota do físico promete — *quase nenhum chega velho* — e **não é recomendado alterar**.

### 🟢 Achado 3 — a isenção de Caminho duplo compra exatamente 61 anos

| Penalidade sobre o custo de progressão | Chega ao rank 7 | Anos internos | Diferença vs. Imortal comum |
|---|---|---|---|
| **0% — a regra atual do Xie Lang** | 20,2% | **231** | **−61 anos** |
| +15% em ambos | 15,3% | 265 | −27 anos |
| **+25% em ambos** | 12,4% | **288** | **−4 anos** |
| +50% em ambos *(a penalidade cheia)* | 8,2% | 338 | +46 anos |
| *Imortal comum, 1 Caminho* | *70,1%* | *292* | *—* |

**A vantagem que a isenção dá é de calendário, não de combate.** Com +25% ele chega ao rank 7 em 288 anos contra os 292 de um Imortal comum — paridade exata no relógio, mantendo Marcas em dobro, +2 Níveis de Dano e terra Especial. Ver decisão 98.

**A variante "penalidade só acima de um nível de domínio" foi testada e descartada:** com limiar em 10.000 Marcas ela nunca entra em vigor durante o rank 6, porque 10.000 **é** o piso do rank 7 (20,1% e 232 anos — idêntico a não ter penalidade). Com limiar em 1.000 ela rende 287 anos, ou seja, o mesmo que um +25% direto, com uma regra a mais para lembrar.

### 🔴 Achado 4 — o problema de ritmo não é o Xie Lang, é o Lee

Marcas acumuladas em 200 anos internos de rank 6, bem preparados:

| Personagem | Marcas | Nível de domínio |
|---|---|---|
| **Xie Lang** *(Físico, Lua+Alma isento)* | **8.702** | Pequeno Feito |
| Demvi *(Vento, um Caminho só)* | 7.201 | Pequeno Feito |
| Jiāotáng *(Sangue+Força isento)* | 7.069 | Pequeno Feito |
| **Lee** *(Cinco Elementos — Marcas ÷ 5)* | **2.187** | Pequeno Feito |

O Xie Lang está **21% à frente** do segundo colocado — margem que se sente e não desequilibra, e que a penalidade de +25% zera. **O outlier real é o Lee, 3,3× atrás de todo mundo**: a regra de dividir as Marcas por cinco custa muito mais do que o acordo dele aparentava, e ele leva mais de 600 anos internos para alcançar o mesmo domínio que os outros alcançam em 200. Item aberto — ver abaixo.

### 🔧 Método desta rodada

Calamidade Terrestre a cada 10 anos internos (3 etapas) e Provação Celestial a cada 100 (5 etapas) · `CD = 14 + 2×(rank−6) + faixa do Contador + 2 se Provação + 5 se Físico Extremo − reduções` · Marcas proporcionais aos sucessos, em dobro para o Físico · Marcas iniciais 850 (comum) e 1.700 (Físico) · Contador de Ameaça começando em 3 e 15 · falha zera as Marcas do evento e soma 1 Ferimento e 1 Ferimento da Terra · Ferimento da Terra reparado a 1 nível por década · 0–1 sucessos numa Provação é morte · 1 natural conta como duas falhas.

## 📌 O que continua em aberto

- [ ] **O Caminho dos Cinco Elementos leva 3,3× mais tempo para acumular domínio** por causa da divisão de Marcas por cinco (achado 4 da quarta rodada). A decisão 76 fechou o Wu Xing como "desenho funcionando" olhando só para dano em PvP; o eixo de **ritmo de Marca** não tinha sido medido. Reabrir.

- **O Chefe continua sendo o molde menos estável**, mesmo com as ações medidas por rank (decisão 72): 56% · 62% · 80% · 73%. O rank 3 é o mais leve dos quatro. Não é erro — é consequência de a dificuldade de um Chefe ser governada por quantos Golpes Matadores o grupo consegue pagar naquele rank, e não por ele. Se a mesa quiser um clímax duro no rank 3, use **3 ações** em vez de 2.
- **O Golpe Matador Coletivo não foi modelado** — só os individuais. Quatro participantes chegam a +6 Níveis no núcleo, e isso muda a conta do clímax.
- **O Lee no fundo do PvP é o desenho funcionando**, não um problema: ele compra versatilidade e resposta a qualquer elemento, e paga em pico de dano. Fica registrado como esperado, não como pendência.
- **A Retaliação por falha de Golpe Matador é rara demais no modelo** para medir bem — os PJs quase sempre passam no teste de conjuração no rank em que têm essência para gastar.

## 🔧 Método

Motor em Perl, semente fixa (`20260827`), 3.000 iterações por cenário, limite de 20 rodadas. IA dos PJs: cura se um aliado está abaixo de 40%; Golpe Matador uma vez por cena contra alvo de Elite ou acima; senão ataque padrão; sem essência, desliga um sustentado e cai para melee cru (sem `× M`). IA dos inimigos: foco de fogo no PJ mais ferido, especial na primeira ação. Os scripts ficam no scratchpad da sessão, não no vault.
