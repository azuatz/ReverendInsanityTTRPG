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

Este é o **checklist de execução**. A regra completa do orçamento de pontos, da Aptidão, da Origem e dos Buffs de Lore mora em [[⚖️ Pontos de Criação|Pontos de Criação]] — leia lá antes de gastar o primeiro ponto; aqui é só a ordem dos passos, com as fórmulas derivadas que não estão em nenhum outro lugar.

## 1. Conceito e Origem

Uma frase: quem é, de onde vem, o que quer. Escolha uma [[🌱 Origens|Origem]] — ela dá contexto social e define de onde vem o seu primeiro Gu. Duas Origens ajustam o orçamento de pontos; tabela completa em [[⚖️ Pontos de Criação|Pontos de Criação]].

## 2. Aptidão — rolada, e ponto final

Role `1d80+20` (ver [[🌟 Aptidão e Abertura|Aptidão e Abertura]]) — piso 21%, teto 100%. **O número que saiu é o número**, sem exceção pelos pontos de criação. As duas formas de mexer nisso (o pacote dos Dez Físicos Extremos, ou um Buff de Lore) estão detalhadas em [[⚖️ Pontos de Criação|Pontos de Criação]] — decida isso **antes** de gastar os pontos do passo 3, porque muda toda a conta.

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

Você entra em jogo **de mãos vazias**. Deixe o espaço de Gu em branco na ficha — o primeiro Gu vem em jogo, na primeira ou segunda sessão, e o porquê disso importar está em [[⚖️ Pontos de Criação|Pontos de Criação]].

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

## Exemplo resolvido, do zero à mesa

Um personagem genérico, sem ligação com nenhum PJ de nenhuma campanha de referência — só pra mostrar os oito passos virando uma ficha.

**1. Conceito e Origem.** Um jovem do ramo secundário de um clã de refino de veneno, criado nos fundos da propriedade principal, tentando provar que o sangue dele vale tanto quanto o do ramo principal. Origem: **Ramo Secundário** → **+1 ponto** (13 no total, em vez de 12).

**2. Aptidão.** Rolada: `1d80` deu 40, +20 fixo = **60%**. Sem pacote de Físico Extremo e sem Buff de Lore nesta ficha — o número fica como caiu.

**3. Atributos** (13 pontos, tabela de custo em [[💪 Atributos|Atributos]]): FOR +1 (1 ponto) · CON +4 (3 pontos até +3, +2 pontos de +3 a +4 = 5 pontos) · DES +2 (2 pontos) · AST +1 (1 ponto) · VON +3 (3 pontos) · CAR +1 (1 ponto). Total gasto: 1+5+2+1+3+1 = **13**.

**4. Derivados** (rank 1, estágio Inicial → Grau de Densidade B = 0, M = 1):

| Número | Conta | Resultado |
|---|---|---|
| Vitalidade máxima | (18 + 3×4 + 4×0) × 1 | **30** |
| Alma máxima | (12 + 2×3 + 3×0) × 1 | **18** |
| Essência máxima | 60 × 4 | **240** |
| Defesa | 11 + 2 (sem Gu de movimento ainda) | **13** |
| Acerto melee | d20 + 1 + 3 | **d20 + 4** |
| Regeneração | 60 ÷ 10 | **6% por minuto de descanso** |
| Gu que cabem na Abertura | (60 ÷ 10) + 1 | **7** |
| Gu ativos ao mesmo tempo | 4 + 1 | **5** |
| Golpes registrados | 1 + 1 | **2** |
| Pontos de Plano | 2 + maior(1, 1) | **3** |

*(Acerto de Gu e CD dos Gu ainda não se aplicam — a ficha não tem nenhum Gu.)*

**5. Arma.** Espada leve (`d6`) — dano melee é `d6 + 1` (FOR), sem multiplicador nenhum, porque não há Gu de Força ou Transformação ativo. Armadura de couro (RD 1) comprada com o que sobrar do orçamento de jogo.

**6. Nenhum Gu.** A ficha entra na mesa com o campo de Gu vazio.

**7. Vínculo.** Uma frase ligando ele a outro PJ do grupo — por exemplo: "devo a vida a ela desde que me tirou de baixo de uma prateleira de potes quebrados; se alguém ameaçar essa pessoa, eu ajo primeiro e penso depois."

**Epílogo — o primeiro Gu.** Na sessão 1, o personagem sobrevive a uma cobra territorial que guardava um posto avançado do clã, e refina o Gu dela: um **Gu de Veneno de rank 1**, cru e sem nome ainda. É esse Gu — não nenhuma linha da ficha de criação — que vira o gancho da campanha quando o ramo principal descobre o que ele trouxe pra casa.

## Recomendação pro grupo

Depois que os personagens estiverem prontos, olhe todos lado a lado antes da sessão 1: o objetivo não é cobrir papéis com Gu (ninguém tem Gu ainda) — é conferir que os **atributos** do grupo não se sobrepõem demais. Se os quatro pegaram Vontade alta e ninguém tem Astúcia nem Carisma, metade do jogo fica travada. Ver [[💪 Atributos|Atributos]].
