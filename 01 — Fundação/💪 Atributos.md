---
tags:
  - regra
  - fechado
aliases:
  - Atributos
escopo: sistema
---

# 💪 Atributos

Seis atributos. Cada um manda em uma coisa que aparece de verdade na mesa, e nenhum é atributo de despejo.

| Atributo | Sigla | No combate | Fora do combate |
|---|---|---|---|
| **Força** | FOR | **Acerto e dano corpo a corpo** | Erguer, quebrar, arrombar, segurar alguém |
| **Constituição** | CON | **Vitalidade**, quantos Gu você sustenta ativos, e **o que seu corpo aguenta receber** | Veneno, doença, fadiga, frio, fome, tortura |
| **Destreza** | DES | **Defesa**, deslocamento, **acerto à distância** (arco, arremesso) | Furtividade, acrobacia, mãos leves, escapar, fugir |
| **Astúcia** | AST | Perceber emboscada, ler o campo, achar a Brecha de um golpe | Percepção, investigação, **perceber mentira**, conhecimento, refino, criar Golpe Matador |
| **Vontade** | VON | **Acerto dos seus Gu e a CD que eles impõem**, mais Alma | Resistir a controle mental, medo e loucura; Ativação Forçada |
| **Carisma** | CAR | Intimidar, comandar aliados e escravos em cena | Persuadir, **mentir e enganar**, liderar, negociar, política de clã |

## Os eixos de build

**Força e Vontade são as duas formas de fazer dano.** Um personagem de Força bate com arma e corpo; um de Vontade mata com os Gu que carrega.

**Constituição é o que o corpo aguenta** — e isso não é só vida. É **o portão dos Gu de Corpo**: os Gu que se instalam permanentemente na carne e no osso exigem um mínimo de Constituição pra não rasgar o hospedeiro. Um lutador sem Constituição não consegue equipar as coisas que fariam ele valer a pena.

**Destreza é o imposto que todo mundo paga** — é a sua Defesa. Ignorar Destreza é escolher morrer rápido.

**Astúcia e Carisma são as duas formas de resolver as coisas sem rolar dano**, e o jogo tem dois pilares dedicados a isso: preparação (Astúcia lê o mundo) e política (Carisma lê as pessoas).

## Ponto de compra

**12 pontos pra distribuir**, todo atributo começa em 0.

| Custo | De → Para |
|---|---|
| 1 ponto | 0 → +1, +1 → +2, +2 → +3 |
| 2 pontos | +3 → +4 |
| Devolve 1 ponto | 0 → −1 *(deliberadamente fraco nisso)* |

Faixa normal na criação: **−1 a +4**. Acima de +4 só através de jogo (Gu, treino, Marcas de Dao), nunca na ficha inicial.

**Distribuições de exemplo, todas legais:**

| Conceito               | FOR | CON | DES | AST | VON | CAR |
| ---------------------- | --- | --- | --- | --- | --- | --- |
| Lutador de clã         | +4  | +3  | +2  | +1  | +1  | 0   |
| Mestre de Gu clássico  | 0   | +1  | +2  | +2  | +4  | +1  |
| Estrategista           | 0   | +1  | +2  | +4  | +2  | +2  |
| Político do clã        | 0   | +1  | +2  | +2  | +2  | +4  |
| Bruto que aguenta tudo | +3  | +4  | +1  | +1  | +1  | 0   |
| Generalista            | +2  | +2  | +2  | +2  | +2  | +2  |

Nenhuma combinação legal deixa o personagem morto de fábrica — mesmo −1 é jogável, só desfavorecido naquilo.

**O lutador custa mais caro que o usuário de Gu, e isso é de propósito:** ele precisa de Força (bater), Constituição (equipar os Gu de Corpo que fazem ele bater forte) e Destreza (sobreviver). Em troca, o corpo dele não gasta essência nenhuma pra funcionar, e os Gu de Corpo são permanentes — não comem, não podem ser roubados no meio da luta, não precisam ser reativados.

## Onde cada atributo entra em número

```
Defesa              = 10 + DES + rank + rank do Gu de movimento ativo
Acerto melee        = d20 + FOR + (rank + 2)
Acerto à distância  = d20 + DES + (rank + 2)
Dano melee          = 1 dado da arma + FOR   [sem Gu de Força ativo]
Acerto de Gu        = d20 + VON + (rank + 2) + rank do Gu
CD dos seus Gu      = 10 + VON + rank do Gu
Vitalidade máxima   = (18 + 3 × CON + 4 × B) × M
Alma máxima         = (16 + 3 × VON + 3 × B) × M
                      [B = Grau de Densidade do estágio: 0 · 1 · 2 · 3]
Gu ativos ao mesmo tempo   = CON + rank
Golpes Matadores registrados = AST + 1
Aliados/escravos comandados  = CAR + 1
Pontos de Plano máximos      = 2 + (o maior entre AST e CAR)
Iniciativa          = d20 + DES, rolada no início do combate
```

**Astúcia e Carisma têm número derivado de propósito.** Sem isso os dois viravam atributos de despejo — dava pra zerar os dois e financiar FOR+4/CON+4/DES+3 sem perder nada mecânico. Agora zerar Astúcia significa **um único Golpe Matador registrado** a campanha inteira (ver [[⚡ Golpes Matadores|Golpes Matadores]]), e zerar Carisma significa comandar **um** aliado e ter o teto mínimo de Pontos de Plano (ver [[🕵️ Preparação e Informação|Preparação e Informação]]). Continua sendo uma escolha legítima — só não é mais de graça.

## Testes

`d20 + atributo relevante + treino (se tiver) vs. Dificuldade`, ou contra o teste do adversário numa disputa.

| Dificuldade | Exemplo |
|---|---|
| 10 | Trivial sob pressão |
| 14 | Padrão |
| 18 | Difícil |
| 22+ | Quase impossível sem ajuda ou preparação |

### O bônus de treino cresce com o rank

Ser treinado em algo não vale o mesmo no rank 1 e no rank 8 — a diferença entre um novato competente e alguém com séculos de prática precisa aparecer no dado.

```
Bônus de treino = +2, e sobe +1 a cada rank PAR
```

| Rank | 1 | 2–3 | 4–5 | 6–7 | 8–9 |
|---|---|---|---|---|---|
| **Bônus de treino** | **+2** | **+3** | **+4** | **+5** | **+6** |

O bônus vale nos **testes de perícia** — e só neles.

> [!important] Ataque não é ação treinada — o treino fica fora do combate
> **Rolagem de ataque não soma treino**, nem melee, nem à distância, nem de Gu. É a mesma regra que [[🎯 Perícias]] enuncia do outro lado ("perícia não rola em combate"): combate resolve por ataque contra Defesa, e as duas escadas não se somam. As fórmulas em "Onde cada atributo entra em número" já refletem isso.
>
> Sem essa trava, cada rank par empurraria o acerto de todo mundo pra cima sem a Defesa acompanhar: medido, **+12,6 pontos percentuais de vitória do grupo em média, até +30,9** (decisões 213-215). A escada existe pra separar quem estudou de quem improvisa **fora** da luta, que é onde ela não desequilibra nada.

*(Calibrado contra *Feiticeiros e Maldições*, que usa a mesma escada: base +2, subindo +1 nos níveis 5, 9, 13 e 17, chegando a +6 — cinco degraus. Os nove ranks deste sistema com "+1 a cada rank par" reproduzem os mesmos cinco degraus e a mesma faixa +2 a +6.)*

**A lista de perícias** — o que existe, o que cada uma cobre, e quantas um personagem treina — mora em [[🎯 Perícias]]. A regra daqui é só o número: treinado soma o bônus da tabela acima; sem treino, só o atributo.

## 📝 Changelog

- `2026-08-26` — Atributos reestruturados de FOR/COR/DES/INT/VON (8 pontos) pra **FOR/CON/DES/AST/VON/CAR (12 pontos)**. Astúcia e Carisma foram criados porque o jogo tem política de clã e um pilar de preparação sem nenhum atributo servindo os dois; Constituição e Força ficaram separadas porque fundidas concentravam vida, acerto e dano num atributo só.