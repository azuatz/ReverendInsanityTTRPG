---
tags:
  - regra
  - personagem
  - fechado
aliases:
  - Guia de Criação de Ficha
escopo: sistema
---

# 📋 Guia de Criação de Ficha

Passo a passo, do zero até a mesa. Todo personagem novo começa **rank 1, estágio inicial** — sem exceção (ver [[🧭 Log de Decisões]]).

> **O orçamento é um só: 12 pontos.** Não existe moeda separada de criação. Você não compra Gu — **todo personagem começa de mãos vazias** e conquista o primeiro Gu em jogo. Ver [[⚖️ Pontos de Criação|Pontos de Criação]].

## 1. Conceito e Origem

Uma frase: quem é, de onde vem, o que quer. Escolha uma [[🌱 Origens|Origem]] — ela dá contexto social (qual ramo do clã, ou se nem é do clã), define de onde vem o seu primeiro Gu, e em dois casos dá **+1 ponto** (Ramo Secundário e Errante, como compensação por não terem rede de apoio).

## 2. Aptidão — rolada, e ponto final

A Aptidão foi rolada (`1d80+20`, ver [[🌟 Aptidão e Abertura|Aptidão e Abertura]]) e **o número que saiu é o número**: não se compra pra cima nem se vende pra baixo com pontos de criação (decisão 111). Piso 20%, teto 99%.

A única exceção é o **pacote dos Dez Físicos Extremos** — 100% de aptidão por **−8 pontos** e a Dívida do Destino. Não é comprar aptidão; é assumir outra categoria de existência. Ver [[⚖️ Pontos de Criação|Pontos de Criação]].

**Antes de decidir, pergunte ao mestre qual é o seu Buff de Lore.** Cada jogador tem direito a **um**, de graça, e ele pode ser exatamente a coisa que você ia pagar aqui (ver [[⚖️ Pontos de Criação|Pontos de Criação]]). Fechar o buff primeiro muda toda a conta dos pontos.

A Aptidão define sua % de Abertura, e portanto a Essência máxima:

```
Essência = % de abertura × 4 × 2^(estágio − 1)
```

No estágio inicial (estágio 1), isso simplifica pra `% de abertura × 4`.

## 3. Atributos

Distribua o que sobrou dos **12 pontos** entre Força, Constituição, Destreza, Astúcia, Vontade e Carisma. Ver [[💪 Atributos|Atributos]] pra tabela de custo e exemplos de distribuição.

## 4. Os números derivados

```
Vitalidade máxima  = (18 + 3 × CON + 4 × B) × M
Alma máxima        = (12 + 2 × VON + 3 × B) × M
                     (B = Grau de Densidade — no estágio Inicial, B = 0)
Defesa             = 10 + DES + rank + rank do Gu de movimento ativo
                                            (no rank 1, sem Gu: 11 + DES)
Acerto melee       = d20 + FOR + rank + 2   (no rank 1: d20 + FOR + 3)
                     (não existem armas à distância mundanas — alcance é Gu)
Acerto de Gu       = d20 + VON + rank + 2 + rank do Gu
CD dos seus Gu     = 10 + VON + rank do Gu
Regeneração        = (% de aptidão ÷ 10) por minuto de descanso
                     (a Essência NÃO regenera durante o combate)
Gu que cabem na Abertura   = (% de aptidão ÷ 10) + rank
Gu ativos ao mesmo tempo   = CON + rank
Golpes registrados         = AST + 1
Pontos de Plano            = 2 + maior(AST, CAR)
```

**O erro mais comum é a Defesa.** Ela tem *quatro* parcelas, não duas — e a quarta (`rank do Gu de movimento ativo`) é a razão mecânica pra Gu de movimento existirem. Sem um, você apanha 80% das vezes em vez de 65%.

No rank 1, M é 1 — o multiplicador só começa a importar a partir do rank 2.

## 5. Arma

Escolha uma. Ela define **o dado do seu golpe corpo a corpo** (tabela em [[⚔️ Combate|Combate]]): desarmado/improvisada `d4`, leve `d6`, média `d8`, pesada `d10`. O dano soma FOR.

**Sem Gu de Força ou Transformação ativo, o dano melee não multiplica por nada** — é humano batendo em humano. Isso é normal no rank 1 e é o que o primeiro Gu vai mudar.

**Compre armadura também, e compre a melhor que puder.** Ela dá RD fixa (couro 1 · batido 2 · malha 3 · placas 4) que **não multiplica por M** — ou seja, é decisiva no rank 1, boa no rank 2, e decoração a partir do rank 4. É a única vez na campanha em que dinheiro compra sobrevivência direta. Preços em [[🏪 O Mercado]], regra em [[⚔️ Combate]].

## 6. Nenhum Gu

Você entra em jogo **de mãos vazias**. O primeiro Gu é conquistado na primeira ou segunda sessão, e a cena em que isso acontece é o começo de verdade do personagem. Deixe o espaço em branco na ficha — ele vai ser preenchido.

## 7. Vínculo com o grupo

Uma frase ligando seu personagem ao personagem de **outro jogador**, e ela precisa dizer **o que você arriscaria** — colega de infância, dívida, rivalidade, parentesco. Não precisa ser recíproco, e funciona melhor quando não é.

**O Vínculo é regra, não sabor.** Uma vez por sessão, quando você age por causa dele aceitando um custo que não aceitaria de outra forma, ganha **vantagem** num teste — ou dá **+2** no teste do vinculado, se estiver ajudando ele. Agir **contra** o Vínculo o quebra, e a quebra vira um [[🤝 O Débito\|Débito]] em favor de quem foi deixado. Regra completa, e o Acordo de Mesa que vem junto, em [[🤝 Vínculos e Acordo de Mesa]].

## 8. O que preencher na ficha

| Campo | Vem de |
|---|---|
| Nome, Origem, conceito | Passo 1 |
| Aptidão % e Grau | Passo 2 |
| FOR / CON / DES / AST / VON / CAR | Passo 3 |
| Vitalidade, Alma, Essência, Defesa, acertos, limites de Gu | Passo 4 |
| Arma e o dado dela | Passo 5 |
| Rank 1, Estágio Inicial | Sempre, pra todo personagem novo |
| Gu | **vazio** — vem em jogo |
| Vínculo | Passo 7 |
| Anos de vida: 100 | Sempre |

## Recomendação pro grupo

Depois que os personagens estiverem prontos, olhe todos lado a lado antes da sessão 1: o objetivo não é cobrir papéis com Gu (ninguém tem Gu ainda) — é conferir que os **atributos** do grupo não se sobrepõem demais. Se os quatro pegaram Vontade alta e ninguém tem Astúcia nem Carisma, metade do jogo fica travada. Ver [[💪 Atributos|Atributos]].
