---
tags:
  - regra
  - combate
  - fechado
aliases:
  - Recursos e Dano (v1 — VIT 12+3CON, sem estágio)
escopo: sistema
---

# ❤️ Recursos e Dano

## Os dois trilhos: Vitalidade e Alma

Todo personagem tem **dois medidores de HP separados**:

- **Vitalidade** — o corpo. Dano físico, dano de Gu de ataque comum, veneno, fogo.
- **Alma** — a mente. Dano de Gu do Caminho da Alma, golpes mortais de sonho/ilusão, certas maldições.

Os dois escalam pela mesma tabela de M do rank (ver [[⚔️ Combate|Combate]]):

```
Vitalidade máxima = (12 + 3 × CON) × M do rank
Alma máxima       = (8  + 2 × VON) × M do rank
```

| CON | Vitalidade | Tapas de um Gu do seu rank *(1d6 × M, média 3,5)* |
|---|---|---|
| −1 | `9 × M` | 2,5 |
| **0** | **`12 × M`** | **3,4** |
| +2 | `18 × M` | 5,1 |
| +4 | `24 × M` | 6,9 |

**A calibragem:** mesmo com Constituição zero, você aguenta **três golpes** de um Gu do próprio rank antes de cair — e isso **sem contar RD**. Com um Gu de defesa decente, dobra. Investir em CON leva de 3 pra 7 tapas, que é uma diferença que se sente na mesa sem tornar um personagem imortal.

**Sem níveis de ferimento pra rastrear em combate.** Nada de tabela de penalidade por faixa de HP — é coisa demais pra lembrar no meio de uma cena. Os dois trilhos são só um número que desce. Fora zerar (ver abaixo), a ficha não aplica penalidade automática por estar "machucado" — é a mesa que decide o quanto isso pesa na narração.

## Vitalidade zerada — Teste de Morte

Zerar Vitalidade **não mata na hora**. O personagem cai, inconsciente, à beira da morte. No início de cada um dos turnos seguintes dele, role um **Teste de Morte**: `d20 sem bônus nenhum`.

| Resultado | Efeito |
|---|---|
| 10 ou mais | Estabiliza — não piora neste turno, continua inconsciente |
| 9 ou menos | Piora um degrau |
| 1 natural | Piora dois degraus de uma vez |
| 20 natural | Acorda com 1 de Vitalidade, ainda em perigo mas de pé |

Três degraus de piora (por acúmulo de falhas) = morte. Um aliado pode estabilizar o personagem caído com uma ação dedicada perto dele (socorro, um Gu de cura, qualquer coisa que a cena aceite como cuidado real) — estabilizado, ele para de rolar Teste de Morte, mas continua inconsciente até tratamento de verdade ou descanso longo.

**Falhar o Teste de Morte pelo menos uma vez** (mesmo que estabilize depois) deixa sequela — a escolha é da mesa, mas o padrão recomendado é **−1 permanente num atributo à escolha do jogador dentre os afetados pela cena**, ou **perder o estágio mais recente conquistado** (regride um estágio dentro do rank atual) — nunca os dois ao mesmo tempo por um único Teste de Morte falho. Um personagem que se aproximou da morte sai da cena mais fraco, mesmo sobrevivendo — é o preço de sobrevivente que o tom do jogo pede.

## Descanso curto e longo

Vitalidade e Verdadeira Essência recuperam pelo mesmo padrão simples:

| Descanso | Recupera |
|---|---|
| **Curto** (uma pausa dentro da cena/sessão — minutos a algumas horas) | Metade do máximo de Vitalidade e de Essência |
| **Longo** (descanso de verdade — durante a narrativa entre cenas, geralmente sono de uma noite) | Tudo — Vitalidade e Essência cheias de novo |

Alma segue a mesma regra de descanso curto/longo, exceto quando a mesa decidir que um dano de Alma específico deixou sequela (algo permanente, tratado à parte, não por descanso).

## Cura por Gu

Gu de cura rola dado, igual a dano — mesma Escada e mesmo M (ver [[⚔️ Combate|Combate]]):

```
Cura = (dado do passo do Gu) × M do rank dele
```

O passo padrão de um Gu de cura é **+1 (1d8)**. Um Gu de cura de rank 4 devolve `1d8 × 8` (8 a 64). Gu de cura excepcionais ficam em +2 ou +3; está na ficha de cada um no [[📖 Catálogo de Gu|Catálogo de Gu]].

Níveis de Dano **não** afetam cura; o que afeta é um Gu de amplificação do Caminho da Água/Vida especificamente, que sobe o passo do Gu de cura da mesma forma.

## 🩹 Ferimento

Várias regras do sistema cobram "1 Ferimento" — Ativação Forçada, a Ascensão, o Retrocesso de Marca, o contragolpe de Golpe Matador, falha grave de refino. Isto é o que a palavra significa:

> **Um Ferimento é −5% permanente na Vitalidade máxima e na Alma máxima.** Cumulativo. Não impõe penalidade em teste nenhum.

Não é uma condição pra rastrear em combate, não tem tabela de faixa, não muda nada além dos dois números do topo da ficha — é coerente com a decisão de não ter níveis de ferimento (ver acima). É só um teto que desce e não volta sozinho.

**Como se cura:** um Gu de cura de **rank 3 ou superior**, numa cena dedicada fora de combate (não vale no meio da luta), remove **1 Ferimento**. Fora isso, um arco inteiro de recuperação de verdade — reclusão, tratamento, um Gu específico caçado pra isso — remove todos.

## Retrocesso (o contragolpe)

Falhar num refino de Gu ou num Golpe Matador machuca de volta. O dano de retrocesso é `(soma dos ranks dos Gu envolvidos) × 2` em Vitalidade e `(soma dos ranks dos Gu envolvidos) × 1` em Alma — quanto mais ambicioso o combo, mais caro sai errar.
