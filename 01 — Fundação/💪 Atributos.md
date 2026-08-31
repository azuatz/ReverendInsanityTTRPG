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
Acerto melee        = d20 + FOR + (rank + 2) + treino
Acerto à distância  = d20 + DES + (rank + 2) + treino
Dano melee          = (dado da arma na Escada) + FOR
Acerto de Gu        = d20 + VON + (rank + 2) + rank do Gu + treino
CD dos seus Gu      = 10 + VON + rank do Gu
Vitalidade máxima   = (12 + 3 × CON) × M
Alma máxima         = (8 + 2 × VON) × M
Gu ativos ao mesmo tempo   = CON + rank
Golpes Matadores registrados = AST + 1
Aliados/escravos comandados  = CAR + 1
Pontos de Plano máximos      = 2 + (o maior entre AST e CAR)
Ordem de turno      = por Destreza, sem rolagem
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

**Perícias/treino** não têm lista fechada: se o personagem tem motivo pra ser bom em algo (a origem dele, a profissão, o que ele passou a campanha fazendo), a mesa concede **+2** naquilo. Escreva na ficha o que ele treinou, não uma tabela.

## 📝 Changelog

- `2026-08-26` — Atributos reestruturados de FOR/COR/DES/INT/VON (8 pontos) pra **FOR/CON/DES/AST/VON/CAR (12 pontos)**. Astúcia e Carisma foram criados porque o jogo tem política de clã e um pilar de preparação sem nenhum atributo servindo os dois; Constituição e Força ficaram separadas porque fundidas concentravam vida, acerto e dano num atributo só.