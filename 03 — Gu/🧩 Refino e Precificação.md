---
tags:
  - regra
  - gu
  - fechado
aliases:
  - Refino e Precificação
escopo: sistema
---

# 🧩 Refino e Precificação

Três pilares do trabalho com Gu: **alimentar** (ver [[🍖 Sustento e Alimento|Sustento e Alimento]]), **usar** (ativação em combate, ver [[⚔️ Combate|Combate]]) e **refinar** — tornar um Gu seu, ou fundir vários num só mais forte. Esta nota cobre refino e preço.

---

## Refino único — tornar um Gu bruto seu

Refinar um Gu recém-obtido (caçado, comprado, herdado) é uma disputa de vontade entre o cultivador e o Gu, não um teste único de dado.

**Custo de Verdadeira Essência:** `Rank do Gu × 20`, ajustado pela vontade dele: +10 se for um Gu de vontade forte (predador, criatura combativa), −10 se for fraca (planta, inseto passivo).

**Ritmo:** o cultivador infunde essência por rodadas/cenas; se a velocidade de infusão dele (aptidão) for maior que a velocidade de resistência do Gu, o refino avança e eventualmente termina. Se for menor, o esforço se perde e o Gu volta ao estado bruto — não há meio-termo permanente. Aptidão alta permite refinar só com recuperação natural; aptidão baixa exige gastar Pedras Primordiais como reforço (cada pedra cobre cerca de 20 pontos).

## Refino como teste estendido

Quando o refino é uma **cena** (e não pano de fundo entre sessões), rode como teste estendido — o personagem acumula sucessos ao longo de várias rolagens, e a tensão é chegar lá antes de acumular falhas.

```
Teste = d20 + AST + treino de Refino
Acumule N sucessos antes de 2 falhas
```

| Refinar/elevar para | Sucessos necessários | CD por teste |
|---|---|---|
| Rank 1 | 2 | 12 |
| Rank 2 | 3 | 15 |
| Rank 3 | 4 | 18 |
| Rank 4 | 5 | 21 |
| Rank 5 | 6 | 24 |
| **Gu Imortal (rank 6)** | 3 | 25 — **só com Espírito da Terra**, que concede vantagem. Ver [[🧿 Espíritos da Terra\|Espíritos da Terra]] |

**Vantagem no teste** (2d20, fica com o maior), cumulativa por condição atendida — cada uma vale uma vez:

- **Receita exata em mãos** — herança, sala de receitas, ou um refino anterior bem-sucedido do mesmo Gu.
- **Materiais puros** — gastar 50% a mais em Pedras Primordiais nos ingredientes.
- **Local condizente** — refinar um Gu de Fogo num vulcão, um de Água numa nascente, um Imortal numa Terra Abençoada.
- **Assistentes qualificados** — outro cultivador de rank igual ou superior canalizando junto.

*(Mecanicamente, vantagens acima da primeira viram +2 cada no teste — não role três dados.)*

### Quando o refino falha

Acumular 2 falhas encerra o refino. Role `1d6` pra gravidade:

| 1d6 | O que acontece |
|---|---|
| 1–2 | **Desperdício** — os materiais se perdem, o Gu base sobrevive. Pode tentar de novo |
| 3–4 | **Morte do material** — todos os Gu ingredientes morrem, menos o Gu Vital |
| 5 | **Contragolpe** — o acima, mais o Retrocesso completo (ver [[❤️ Recursos e Dano\|Recursos e Dano]]) |
| 6 | **Colapso do Dao** — o acima, mais 1 Ferimento permanente e a Abertura fica instável: todo Gu custa o dobro até um descanso longo |

**Modificador de rank na gravidade:** some **+1 ao `1d6`** por cada rank do Gu que estava sendo refinado acima de 3. Refinar rank 4 rola `1d6+1`; rank 5, `1d6+2`. Resultados acima de 6 contam como 6 e ainda somam a Explosão abaixo.

### 💥 A Explosão de Refino

Um `1 natural` em qualquer rolagem do teste estendido — a qualquer momento, mesmo que você fosse ganhar — encerra o refino na hora com **Explosão**:

> A essência acumulada no processo não tem pra onde ir e sai de uma vez.

| Efeito | |
|---|---|
| **Dano** | `1d12 × M do rank do Gu que estava sendo refinado`, em Vitalidade, **sem RD** — a explosão vem de dentro da fornalha, e a fornalha é você |
| **Materiais** | Tudo perdido, **inclusive o Gu Vital**, que fica ferido e **inutilizável por `1d6` semanas** (é a única circunstância que tira o Gu Vital de jogo sem matá-lo) |
| **Área** | Raio de 3 m. Quem estiver assistindo sofre metade — refino não é atividade de sala cheia |
| **A Abertura** | **1 Ferimento permanente**, sempre |
| **O local** | Se você refinava numa Terra Abençoada, ela ganha **1 Ferimento da Terra** (ver [[🗝️ Terra Abençoada\|Terra Abençoada]]) |

**Refino de Gu Imortal** (com Espírito da Terra, ver [[🧿 Espíritos da Terra|Espíritos da Terra]]) usa a mesma regra, com `M` de rank 6 — `1d12 × 32`. É por isso que ninguém tenta sem a vantagem do espírito.

## Combo-refino — fundir Gu num de rank superior

Sintetizar dois ou mais Gu conhecidos num Gu novo, de rank mais alto. Isso é o motor da progressão de arsenal — trocar uma dúzia de Gu médios por um punhado de Gu fortes.

**Taxa de sucesso base**, antes de modificadores:

| Fusão | Chance base |
|---|---|
| Rank 1 → Rank 2 | ~70% |
| Rank 2 → Rank 3 | ~55% |
| Rank 3 → Rank 4 | ~40% |
| Rank 4 → Rank 5 | ~25% |
| Rank 5 → Gu Imortal (rank 6) | <10% |

**Modificadores:** ter uma receita já validada (+15%); nunca ter usado nenhum dos Gu envolvidos em combate antes (−20%); ser o Gu Vital do personagem, que nunca morre num combo-refino falho — só fica ferido (proteção única do Gu Vital).

**Falha:** todos os Gu usados na fusão morrem, exceto o Gu Vital (que só sofre ferimento). Isso torna combo-refino sempre uma aposta real — mesmo com receita e experiência, nunca é garantido.

## O Gu Vital — proteção extra

Além de nunca morrer num combo-refino falho, o Gu Vital tem duas proteções a mais:

- **Nunca é o primeiro a cair.** Se um efeito de combate destruir um Gu do personagem "ao acaso" (um golpe que esmaga o ecossistema da Abertura, por exemplo — ver [[⚔️ Combate|Combate]]), o Gu Vital é sempre o **último** escolhido, não o primeiro.
- **Elevação Direta** — uma alternativa ao combo-refino só pra ele: em vez de fundir com outro Gu (risco de virar outra coisa), o jogador pode alimentá-lo à força com o dobro do material normal pra ele subir de rank **mantendo a identidade**. A vontade dele já é domada, então o teste ganha **vantagem** (2d20, fica com o maior). Se falhar mesmo assim, o Gu Vital não morre — entra em Coma Místico por `1d6+1` semanas, incapaz de ser usado até acordar.

## Preços de referência (em Pedras Primordiais)

| Gu | Preço |
|---|---|
| Rank 1 | Algumas a dezenas |
| Rank 2 | Dezenas a centenas |
| Rank 2, raríssimo (tipo Relíquia) | Milhares — supera um Gu comum de rank 3 |
| Rank 3 | Centenas |
| Rank 3, raríssimo | Dezenas de milhares |
| Rank 4 | Milhares a dezenas de milhares |
| Rank 5 | Sem mercado — quem tem, não vende |
| Rank 6+ (Imortal) | Preço astronômico, cotado em Pedras de Essência Imortal, não em Pedras comuns |

Ver [[💠 Economia das Pedras Primordiais|Economia das Pedras Primordiais]] pra como isso se converte em despesa de mesa.
