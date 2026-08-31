---
tags:
  - regra
  - inimigo
aliases:
  - Reis Fera e a Maré
  - Rei Fera
escopo: sistema
---

# 🐺 Reis Fera e a Maré

Grupos de feras grandes têm um rei, e o tamanho do grupo dá o título — **📕 canônico** (Vol. 1, cap. 114-115): **Rei de Cem Feras** governa centenas, **Rei de Mil Feras** governa ~mil, **Rei de Miríade de Feras** governa dez mil ou mais. O próprio romance calibra a dificuldade: um grupo padrão lida com um Rei de Cem; **três grupos cooperando** mal matam um Rei de Mil; um Rei de Miríade exige os anciãos e o líder do clã juntos.

Esta nota traduz isso em três coisas: o molde de cada Rei, a **regra de ondas** (como uma horda de centenas entra em cena sem rodar centenas de turnos), e a **Varredura** — o jeito de pular uma onda inteira e só marcar o custo.

Tudo aqui **reusa os moldes existentes** de [[⚔️ Ameaças Genéricas por Rank]] (Elite, Chefe, Horda, traços de fera). Nenhuma ficha nova pra aprender.

---

## 👑 Os três Reis — molde e uso

| Rei | Molde *(tudo de [[⚔️ Ameaças Genéricas por Rank]])* | Medido *(mesa de 4, rank igual)* | Como usar |
|---|---|---|---|
| **Rei de Cem Feras** | **Elite** com traços de fera + escolta de **Horda de 8** | **~99% de vitória — mas custa ~55-60% da Vitalidade do grupo e ~7 rodadas** | Cena Difícil de verdade. O grupo ganha, sai mastigado, e o resto da sessão sente |
| **Rei de Mil Feras** | **Chefe** (ações por rank) + **Horda de 12** + **Horda de 8** | **0% — um grupo sozinho NUNCA vence** (simultâneo) | **Não é um encontro.** É o cânone dos "três grupos": ou o grupo traz aliados de peso, ou enfrenta **em ondas** (abaixo), ou a cena é fuga/isca/armadilha |
| **Rei de Miríade de Feras** | O evento que abre ou fecha um arco — a maré inteira | *(não se mede em uma cena)* | **Guerra, não combate**: resolva a maré com 3-4 testes de grupo (a regra da casa pra conflito de larga escala) e reserve o combate rodado pro confronto final contra o Rei em pessoa — que aí é um Chefe normal, jogável |

**O Rei em pessoa é sempre um molde normal** — Elite ou Chefe do rank dele, com os traços de fera. O que muda entre os três títulos não é a ficha do Rei: é **quanta horda vem junto**, e é isso que a regra de ondas administra.

---

## 🌊 A regra de ondas — por que a maré não entra inteira

**Medido: hordas simultâneas não são "mais difícil", são sentença.** Uma Horda de 8 sozinha é a cena Fácil (100% de vitória). **Duas ao mesmo tempo** derrubam a vitória pra 83%/56%/36% (ranks 2/3/4). **Três ao mesmo tempo: 0%.** O motivo é o mesmo penhasco de volume de ações já documentado em [[⚔️ Ameaças Genéricas por Rank]] — cada horda ataca uma vez **por personagem de pé**, então duas hordas dobram o volume por rodada.

Por isso a regra:

> **Uma maré entra em ondas sequenciais, nunca empilhada.** No máximo **uma Horda ativa por vez** (mais o Rei e/ou 1-2 inimigos individuais, se a cena for o clímax). A onda seguinte só entra quando a atual cai — sem descanso entre elas.

O desgaste vem da **sequência sem pausa**, não do empilhamento: cada onda limpa custa em média **~25-30% da Vitalidade do grupo** e ~4 rodadas (medido, rank igual). Duas ondas seguidas deixam o grupo em metade da vida com a cura da cena já gasta; **a terceira onda sem pausa é a zona de morte** — e é exatamente aí que o Rei deve entrar em pessoa, se a mesa quer o clímax.

---

## ⏭️ A Varredura — pular a onda e marcar o custo

Pra maré longa (ou qualquer horda que a mesa não queira rodar), **uma onda inteira se resolve num teste de grupo só**:

```
Cada personagem rola seu ataque principal (acerto melee ou de Gu)
contra CD 12 + 2 × (rank da onda − rank do grupo).
Conta-se quantos passaram.
```

| Resultado *(mesa de 4)* | Custo da onda, aplicado na hora |
|---|---|
| **4 passaram** | **15% da Vitalidade máxima** de cada um · 10% da essência · a onda caiu |
| **2-3 passaram** | **25% da Vitalidade** · 15% da essência · a onda caiu |
| **1 passou** | **40% da Vitalidade** · 20% da essência · a onda caiu, mas **role 1d6: em 1-2, um Gu ativo sorteado de alguém fica Esgotado** ([[💀 A Morte dos Gu]]) |
| **0 passaram** | O custo acima **e a onda não caiu** — ela entra em cena e o combate roda de verdade, com o grupo já pagando esse preço |

**Tempo narrativo: ~meia hora de luta por onda varrida** (uma onda medida dura ~4 rodadas). **Cura por Gu não desconta o custo da Varredura** — o custo já é a média de uma cena com a cura dentro.

**Três limites, e eles são o sistema:**

1. **Onda de rank acima do grupo não se varre.** Joga-se, ou foge-se — Varredura é pra volume, não pra superar patamar.
2. **O Rei nunca é varrido.** Varre-se a escolta; o Rei é sempre combate rodado (ou negociação, ou fuga).
3. Os percentuais **acumulam entre ondas sem zerar** — três ondas varridas custam ~45-75% da Vitalidade, e é essa conta que decide quando o grupo para de varrer e recua. A maré não é difícil numa onda; ela é difícil na **quinta**.

*(Custos calibrados por simulação — 1.500 iterações/cenário sobre o motor da sétima rodada, script `_Processo/simulacoes/2026-08-31-desgaste-hordas-calibracao.py`. A faixa medida de uma onda limpa é 23-32% de Vitalidade conforme o rank; a linha "2-3 passaram" usa a média, as outras escalam dela.)*

---

## 🎯 Montando a cena de maré, na prática

1. **Anuncie o tamanho pela ficção**: centenas = Rei de Cem, milhares = Rei de Mil, o horizonte inteiro = Miríade. O grupo deve saber o que está vendo — feras não emboscam em silêncio aos milhares.
2. **Conte as ondas** (2-4 pra um Rei de Cem chegando ao clímax; 4-6 pra atravessar o território de um Rei de Mil; Miríade nem conta — é guerra).
3. **Deixe o grupo escolher, onda a onda**: rodar, varrer, ou recuar. A escolha É o jogo — varrer economiza relógio da mesa e gasta a ficha; rodar é mais seguro pra quem confia na tática; recuar preserva tudo e entrega o objetivo.
4. **O Rei entra quando a mesa estiver madura** — tipicamente com o grupo a ~50% dos recursos. Aí é um Chefe/Elite normal de [[⚔️ Ameaças Genéricas por Rank]], e as regras de sempre valem.
