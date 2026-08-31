#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marcas de Dao — a escada de domínio precisa ser não-linear no topo?
=====================================================================

Testa a pendência de "Em aberto" do [[🧭 Log de Decisões]] ("a amplificação
por Marca pode ser não-linear no topo, e a escada de domínio de
[[☯️ Marcas de Dao]] é linear"). Fonte canônica citada no Log (Cap. 852,
Volume 4) verificada por grep antes deste script:

  - "Two hundred dao marks can increase power by twenty percent. Six hundred
    would mean a sixty percent increase." — confirma a leitura de +20% de
    poder a cada 200 Marcas na faixa baixa, ~linear (dobra por volta de
    1.000 Marcas se a taxa continuar constante).
  - "The dao marks on a Gu Immortal could amplify the power of Immortal Gu
    and immortal killer moves. This amplification was quite terrifying,
    rank eights could have an amplification with a multiplier of hundreds
    or even thousands, that was also why rank seven Gu Immortals could
    rarely beat rank eight Gu Immortals." (linha 32839, mesmo arco da Vol.
    4, poucos capítulos antes do 852) — confirma a leitura de "salto pra
    centenas/milhares de vezes" no topo, tratado como a explicação canônica
    de por que rank 7 quase nunca vence rank 8.

A escada ATUAL de [[⚔️ Combate#☯️ Marcas de Dao — o dano depois do rank 6]]:

  Vislumbre (1-999):              B+0, pool M
  Pequeno Feito (1.000-9.999):    B+1, pool M
  Mestre (10.000-49.999):         B+2, pool M
  Grão-Mestre (50.000-149.999):   B+3, pool M
  Quase-Supremo (150.000-299.999):B+4, pool M
  Grande Mestre Supremo (300k+):  B+5, pool 2×M  <- único degrau que dobra

É uma progressão em degraus (+1 de B por patamar, um único dobramento de
pool no topo) — não uma curva que acelera. Este script mede se essa escada
JÁ produz "o nível de domínio mais alto vence de forma esmagadora" nos três
confrontos do topo, ou se produz lutas mais equilibradas do que a ficção
descreve.

MOTOR: reaproveita a MESMA fórmula de dano/ataque/defesa/crítico/RD de
[[simulacoes/2026-08-31-validacao-completa.py]] (pool `M dX`, bônus `M × B`,
`acerto = d20 + atributo + 2×rank + 2` contra Defesa, RD com piso `1×M`,
crítico no 20 natural dobra os dados) — não reinventa o motor de combate,
só troca o cenário (grupo vs. inimigos) por um duelo 1v1 simétrico em tudo
menos o nível de domínio.

COMBATENTES: dois Gu Immortals de rank 8 (M=128), estatísticas idênticas
(CON, DES, atributo de ataque, dado — Caminho médio d10) EXCETO o nível de
domínio de Marcas de Dao, que muda B e o multiplicador de pool. Isola
exatamente a variável que a pendência de "Em aberto" questiona.

Uso: python3 "2026-08-31-marcas-de-dao-nao-linear.py"
"""

import random
from collections import Counter

random.seed(20260830)

N_ITER = 5000
MAX_ROUNDS = 60

M_TABLE = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256}
RANK = 8
M = M_TABLE[RANK]

CON = 3
DES = 2
ATTR_VAL = 2
DADO = 10  # Caminho de letalidade média

# ---------------------------------------------------------------------------
# Escada ATUAL (linear em degraus) — [[⚔️ Combate]] hoje
# ---------------------------------------------------------------------------
LADDER_LINEAR = {
    "vislumbre":              dict(B=0, pool_mult=1),
    "pequeno_feito":          dict(B=1, pool_mult=1),
    "mestre":                 dict(B=2, pool_mult=1),
    "grao_mestre":            dict(B=3, pool_mult=1),
    "quase_supremo":          dict(B=4, pool_mult=1),
    "grande_mestre_supremo":  dict(B=5, pool_mult=2),
}

# ---------------------------------------------------------------------------
# Escada ALTERNATIVA (não-linear, acelera nos dois últimos degraus) — a
# variante proposta por este script para testar a pendência. Vislumbre até
# Grão-Mestre ficam INTOCADOS (a faixa onde o cânone dá um número concreto
# e ~linear, Cap. 852: +20%/200 Marcas). Só os dois últimos degraus mudam,
# e mudam nos dois eixos que a Escada de Dano já usa (B e o multiplicador
# de pool) — não é um terceiro mecanismo novo, só o mesmo dial girado mais
# forte onde o cânone diz que o salto é grande:
#
#   Quase-Supremo:          B+3 -> B+4 (igual), pool ×1 -> ×2 (novo)
#   Grande Mestre Supremo:  B+5 -> B+6,          pool ×2 -> ×8
# ---------------------------------------------------------------------------
LADDER_NAO_LINEAR = {
    "vislumbre":              dict(B=0, pool_mult=1),
    "pequeno_feito":          dict(B=1, pool_mult=1),
    "mestre":                 dict(B=2, pool_mult=1),
    "grao_mestre":            dict(B=3, pool_mult=1),
    "quase_supremo":          dict(B=4, pool_mult=2),
    "grande_mestre_supremo":  dict(B=6, pool_mult=8),
}

MATCHUPS = [
    ("grao_mestre", "quase_supremo"),
    ("quase_supremo", "grande_mestre_supremo"),
    ("grao_mestre", "grande_mestre_supremo"),
]


# ---------------------------------------------------------------------------
# Motor de dano — idêntico em espírito ao de 2026-08-31-validacao-completa.py
# ---------------------------------------------------------------------------
def roll_pool(n, sides):
    return sum(random.randint(1, sides) for _ in range(n))


def apply_rd(dmg, rd, m_floor):
    if rd <= 0:
        return dmg
    return max(dmg - rd, m_floor)


def make_combatant(tier, ladder):
    t = ladder[tier]
    B, pool_mult = t["B"], t["pool_mult"]
    vit_max = (18 + 3 * CON + 4 * B) * M
    return dict(
        tier=tier, B=B, pool_mult=pool_mult, M=M,
        vit=vit_max, vit_max=vit_max,
        defense=10 + DES + 2 * RANK,
        rd=1 * M,
        dado=DADO,
    )


def attack(a, b):
    acerto_roll = random.randint(1, 20)
    crit = acerto_roll == 20
    acerto = acerto_roll + ATTR_VAL + 2 * RANK + 2
    if not (crit or acerto >= b["defense"]):
        return
    n = a["M"] * a["pool_mult"] * (2 if crit else 1)
    dmg = roll_pool(n, a["dado"]) + a["M"] * a["pool_mult"] * a["B"]
    dmg = apply_rd(dmg, b["rd"], a["M"])
    b["vit"] -= dmg


def run_duel(tier_a, tier_b, ladder, max_rounds=MAX_ROUNDS):
    a = make_combatant(tier_a, ladder)
    b = make_combatant(tier_b, ladder)
    first = a if random.random() < 0.5 else b
    second = b if first is a else a

    for _ in range(max_rounds):
        if a["vit"] <= 0 or b["vit"] <= 0:
            break
        attack(first, second)
        if second["vit"] <= 0:
            break
        attack(second, first)

    if a["vit"] <= 0 and b["vit"] <= 0:
        return "empate"
    if b["vit"] <= 0:
        return "a"
    if a["vit"] <= 0:
        return "b"
    return "empate"  # limite de rodadas sem decisão


def simulate_matchup(tier_a, tier_b, ladder, n_iter=N_ITER):
    outcomes = Counter()
    for _ in range(n_iter):
        outcomes[run_duel(tier_a, tier_b, ladder)] += 1
    win_a = outcomes["a"] / n_iter
    win_b = outcomes["b"] / n_iter
    empate = outcomes["empate"] / n_iter
    return win_a, win_b, empate


def main():
    print("=" * 90)
    print("MARCAS DE DAO — ESCADA LINEAR ATUAL vs. VARIANTE NÃO-LINEAR (rank 8, M=128)")
    print(f"{N_ITER} duelos por confronto, limite de {MAX_ROUNDS} trocas, semente 20260830")
    print("=" * 90)

    results = {}
    for label, ladder in (("LINEAR (atual)", LADDER_LINEAR), ("NÃO-LINEAR (proposta)", LADDER_NAO_LINEAR)):
        print(f"\n### Escada {label} ###")
        results[label] = {}
        for tier_a, tier_b in MATCHUPS:
            win_a, win_b, empate = simulate_matchup(tier_a, tier_b, ladder)
            results[label][(tier_a, tier_b)] = (win_a, win_b, empate)
            print(f"  {tier_a:22s} vs {tier_b:22s}  "
                  f"{tier_a}={win_a*100:5.1f}%  {tier_b}={win_b*100:5.1f}%  empate/limite={empate*100:4.1f}%")

    return results


if __name__ == "__main__":
    main()
