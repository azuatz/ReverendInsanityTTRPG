---
tags: [personagem, ficha, modelo]
escopo: sistema
---

# 🧾 Modelo — Ficha Compacta

Versão de mesa, feita pra caber numa mensagem de Discord e ser lida de relance. A [[Modelo — Ficha de Personagem|ficha completa]] continua existindo pra criação e pra guardar o histórico — **esta aqui é a que fica fixada no canal**.

Tudo que está entre parênteses é instrução: apague ao preencher.

---

## O modelo

```
**Nome:**                              **Idade:**
**Vitalidade:**    /                   **Alma:**     /
**QI:**            /                   **Defesa:**
**CD:**                                **M:**        **Rank:**
**Estágio:**                           **Grau (B):**   **Densidade:**

〖   〗**Força**              〖   〗**Destreza**
〖   〗**Constituição**       〖   〗**Vontade**
〖   〗**Astúcia**            〖   〗**Carisma**

**Acertos** 🎯
- Melee: d20 +        · À distância: d20 +        · Gu: d20 +      + rank do Gu

**Ataques** 🎯  *(formato: `M d(dado do Caminho) + (M × B)`)*
-

**Gu** 🪱  (   /    na Abertura ·    /    ativos)
- ⭐
-

**Golpes Matadores** ⚡ (   /    registrados)
-

**Inventário** 🎒
-
- 💠 Pedras:      (pagamento do clã: 10 por semana. O clã alimenta o seu Gu Vital;
  cada Gu extra come 20 por mês.)
- 💠 Gasto semanal de Pedras:

**Trilhos** 🎚️ (só os que se aplicam — a maioria das fichas não usa nenhum)
-

Vínculo com outro PJ:
Vínculo com o mundo:
O preço da minha traição:
```

---

## Como preencher os números

| Campo | Conta | No rank 1 |
|---|---|---|
| **Vitalidade** | `(18 + 3 × CON + 4 × B) × M` | `18 + 3 × CON` |
| **Alma** | `(12 + 2 × VON + 3 × B) × M` | `12 + 2 × VON` |
| **QI** *(Essência)* | `% de aptidão × 4 × 2^(estágio − 1)` | `% × 4` |
| **Defesa** | `10 + DES + rank + rank do Gu de movimento ativo` | `11 + DES` |
| **CD dos seus Gu** | `10 + VON + rank do Gu` | `11 + VON` |
| **Acerto melee** | `d20 + FOR + (rank + 2) + treino` | `d20 + FOR + 3` |
| **Acerto à distância** | `d20 + DES + (rank + 2) + treino` | `d20 + DES + 3` |
| **Acerto de Gu** | `d20 + VON + (rank + 2) + rank do Gu + treino` | `d20 + VON + 3 + rank do Gu` |
| **M** | 1 · 2 · 4 · 8 · 16 · 32 · 64 · 128 · 256 | 1 |
| **Gu na Abertura** | `(% de aptidão ÷ 10) + rank` | — |
| **Gu ativos** | `CON + rank` | — |
| **Vagas de Suporte** | `B` — só Gu passivos de utilidade, fora da Manutenção quadrática | 0 |
| **Teto de Combo** | 2 · 3 · 4 · 5 Gu, por estágio | 2 |
| **Bônus de dano** | **`+B por dado`** — some `M × B` a todo dano | 0 |
| **Golpes registrados** | `AST + 1` | — |

**Grau (B) é o número mais importante da ficha.** Ele vem do estágio (Inicial 0 · Médio 1 · Alto 2 · Pico 3), soma **por dado** em todo dano, e entra na Vitalidade, na Alma, nas Vagas de Suporte, no Teto de Combo, em testes de resistência e na ordem de turno. Ver [[🪜 Ranks e Estágios]].

**QI é o nome de mesa da Essência.** É o mesmo recurso descrito em [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]] — só o rótulo é mais curto de escrever.

**Três erros comuns:** esquecer o `+ rank` na Defesa (no rank 1 ela é **11 + DES**, não 10 + DES); esquecer que **Alma é uma barra separada da Vitalidade** — quem vai pro Caminho da Alma leva dano nela toda sessão; e esquecer de somar `M × B` no dano, que é o que o estágio inteiro faz.

### O que vai em "Trilhos"

Só quem tem. Escreva o número atual, não a regra:

- **Abertura %** *(e o estado: Latente · Desperta · Plena)*, **Pressão da Abertura** e **Perda de Vitalidade %** — Físico Extremo ([[🌠 Os Dez Físicos Extremos|Dez Físicos Extremos]])
- **Força de Alma** *(em homens, teto mortal 100)* e **Contaminação** — Caminho da Alma
- **Vício em Gu das Tripas** *(pedras já consumidas)* — Caminho da Alma
- **Obrigação com o clã** — [[🏛️ Clãs e Seitas|Clãs e Seitas]]
- **Pontos de Plano** — `2 + maior(AST, CAR)`, [[🕵️ Preparação e Informação|Preparação e Informação]]

### As três linhas do rodapé

Não são enfeite — são o que faz a mesa funcionar.

- **Vínculo com outro PJ** — por que você anda com essa gente. Uma frase, e o outro jogador tem que concordar com ela.
- **Vínculo com o mundo** — uma pessoa, um lugar ou uma dívida que o mestre pode ameaçar. Se você não escrever, o mestre escreve.
- **O preço da minha traição** — o que teria que estar em jogo pra você abandonar o grupo. Reverend Insanity é um cenário onde todo mundo trai alguém eventualmente; escrever o preço de antemão transforma isso numa cena boa em vez de numa briga na mesa.

---

## Exemplo preenchido — Gu Yue Xie Lang *(Pepo)*

```
**Nome:** Gu Yue Xie Lang               **Idade:** 15
**Vitalidade:** 21 / 21                **Alma:** 14 / 14
**QI:** 344 / 344                      **Defesa:** 14
**CD:** 14                             **M:** 1     **Rank:** 1 Inicial

〖 -1 〗**Força**             〖 3 〗**Destreza**
〖 3 〗**Constituição**       〖 3 〗**Vontade**
〖 2 〗**Astúcia**            〖 2 〗**Carisma**

**Acertos** 🎯
- Melee: d20 +2 · À distância: d20 +6 · Gu: d20 +6 + rank do Gu

**Ataques** 🎯
- (nenhum — sem Gu e sem arma, ainda)

**Gu** 🪱  (0 / 9 na Abertura · 0 / 4 ativos)
- ⭐ (o Gu Vital vem na primeira sessão)

**Golpes Matadores** ⚡ (0 / 3 registrados)
-

**Inventário** 🎒
- 💠 Pedras: 10
- 💠 Gasto semanal de Pedras: 0

**Trilhos** 🎚️
- Abertura: 86% — **Latente** (0 / 7 Marcos)
- Pressão da Abertura: 0    · Perda de Vitalidade: 0%
- Força de Alma: 1 homem    · Contaminação: 0
- Pontos de Plano: 4 / 4

Vínculo com outro PJ:
Vínculo com o mundo:
O preço da minha traição:
```

**De onde saem esses números:** QI 344 é `86% × 4` — o **Físico da Lua Antiga** dele está **Latente**, e sobe até 100% ao longo da campanha (ver [[🌠 Os Dez Físicos Extremos|Abertura Incompleta]]). Gu que cabem na Abertura: `(86 ÷ 10) + 1 = 9`. Os atributos somam exatamente 12 (o −1 em Força devolve 1 ponto, e os outros custam 13). Vitalidade `18 + 3×3 = 27`; Alma `12 + 2×3 = 18`; Defesa `10 + 3 + 1 = 14`; CD `10 + 3 + 1 = 14` contra um Gu de rank 1. No **estágio Inicial o Grau (B) é 0**, então nada é somado ainda — é a partir do Médio que a ficha começa a crescer dentro do rank.

**A leitura da ficha:** ele tem mais QI que qualquer outro na mesa e mal consegue erguer uma espada. É exatamente o personagem que o Físico Extremo produz — tudo resolvido por Gu, nada resolvido pelo corpo. Com Força −1, ele **precisa** que o primeiro Gu seja ofensivo, ou passa a primeira sessão inteira sem ter o que fazer num combate.

E ele ainda não é o que vai ser: Latente, a regeneração dele é metade da tabela, os Gu de Lua e Alma ganham **+1** Nível de Dano em vez de +2, a *Maré Baixa* não existe ainda, e o teste da Pressão é **2 pontos mais difícil**. O físico inteiro é uma promessa que a campanha vai cumprindo.

---

## 📝 Changelog

- `2026-08-27` — Criado a partir do formato que a mesa já estava usando no Discord. Acrescentados Alma, M, rank, os acertos pré-calculados, os contadores de Gu e golpes, e o bloco de Trilhos; **Defesa corrigida de 13 pra 14** (faltava o `+ rank`).
