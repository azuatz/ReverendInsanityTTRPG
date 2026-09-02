#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIGÉSIMA TERCEIRA RODADA — o Chefe recalibrado, aplicado e revalidado
=====================================================================

O autor aprovou a recomendação da vigésima segunda (decisão 249):

  · rank 1 — **2 ações** (era 4), Vitalidade `63 × M` **inalterada**
  · ranks 2-5 — Vitalidade por rank: **72 · 78 · 72 · 80 × M** (era 63 uniforme,
    e o `94 × M` uniforme está rejeitado por medição)

Esta rodada **aplica** os números e revalida a tabela de composição inteira,
porque o molde Chefe é a linha "Clímax" dela. As outras quatro composições não
usam o molde e servem de controle: se elas se moverem, o motor mudou de
comportamento e o resultado do Clímax não é confiável.

Duas saídas, como na vigésima segunda: vitória em 56-87% E cena em 6-8 rodadas.

3.000 iterações por célula, semente 20260830.
"""

import importlib.util
import os
import random
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
_MOTOR = os.path.join(_AQUI, "2026-09-01-vigesima-escolha-ou-obrigacao.py")
_spec = importlib.util.spec_from_file_location("motor20", _MOTOR)
V = importlib.util.module_from_spec(_spec)
sys.modules["motor20"] = V
_spec.loader.exec_module(V)

SEED = 20260830
N_ITER = 3000
RANKS = [1, 2, 3, 4, 5]

# ███ A REGRA NOVA (decisão 250) ███
CHEFE_VIT = {1: 63, 2: 72, 3: 78, 4: 72, 5: 80}
CHEFE_ACOES_NOVA = {1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4}

FAIXAS = {   # (piso, teto) de vitória prometida por composição
    "facil": (0.95, 1.00),
    "padrao": (0.75, 0.99),
    "padrao_pesado": (0.60, 0.90),
    "dificil": (0.40, 0.75),
    "climax": (0.56, 0.87),
}
ROTULO = {"facil": "Fácil", "padrao": "Padrão", "padrao_pesado": "Padrão pesado",
          "dificil": "Difícil", "climax": "Clímax"}


def aplica_regra_nova():
    """Sobrepõe o molde Chefe no motor, sem tocar no arquivo da vigésima."""
    V.CHEFE_ACOES.clear()
    V.CHEFE_ACOES.update(CHEFE_ACOES_NOVA)
    orig = V.make_chefe

    def novo(rank, vit_mult=None, **kw):
        if vit_mult is None:
            vit_mult = CHEFE_VIT.get(rank, 63)
        return orig(rank, vit_mult=vit_mult, **kw)
    V.make_chefe = novo
    return orig


def varre(rotulo):
    print(f"\n{'='*84}\n{rotulo}\n{'='*84}")
    print(f"{'composição':<16} {'rank':>4} {'vitória':>9} {'faixa':>13} "
          f"{'rodadas(v)':>11} {'baixas':>8}  {'veredito':<12}")
    print("-" * 84)
    tab = {}
    for comp in ("facil", "padrao", "padrao_pesado", "dificil", "climax"):
        piso, teto = FAIXAS[comp]
        for rank in RANKS:
            random.seed(SEED + rank * 311 + sum(ord(c) for c in comp)   # determinístico entre processos (hash() de string é aleatorizado))
            r = V.simulate(rank, comp, n_iter=N_ITER)
            tab[(comp, rank)] = r
            dentro = piso <= r["win"] <= teto
            print(f"{ROTULO[comp]:<16} {rank:>4} {r['win']:>8.1%} "
                  f"{f'{piso:.0%}-{teto:.0%}':>13} {r['rounds_won']:>11.2f} "
                  f"{r['baixas']:>8.2f}  {'✅' if dentro else '✗':<12}")
        print("-" * 84)
    return tab


def compara(antes, depois):
    print(f"\n\n{'='*84}\nANTES × DEPOIS — o controle é que só o Clímax pode se mover\n{'='*84}")
    print(f"{'composição':<16} {'rank':>4} {'antes':>9} {'depois':>9} {'Δ':>9} "
          f"{'rodadas antes':>14} {'rodadas depois':>15}")
    print("-" * 84)
    for comp in ("facil", "padrao", "padrao_pesado", "dificil", "climax"):
        for rank in RANKS:
            a, b = antes[(comp, rank)], depois[(comp, rank)]
            d = (b["win"] - a["win"]) * 100
            marca = " ←" if abs(d) > 0.5 else ""
            print(f"{ROTULO[comp]:<16} {rank:>4} {a['win']:>8.1%} {b['win']:>8.1%} "
                  f"{d:>+8.1f}pp {a['rounds_won']:>13.2f} {b['rounds_won']:>14.2f}{marca}")
        print("-" * 84)
    movidas = {comp for comp in FAIXAS for rank in RANKS
               if abs(depois[(comp, rank)]["win"] - antes[(comp, rank)]["win"]) > 0.005}
    print(f"\nComposições que se moveram: {sorted(ROTULO[c] for c in movidas)}")
    print("Esperado: apenas Clímax. Qualquer outra indica contaminação do motor.")


if __name__ == "__main__":
    random.seed(SEED)
    V.configura(lee="melee — foice + Wu Xing", teste_publicado=True,
                heuristica="cauda", portao=3, dobra="sim", abertura=True,
                col_ret_todos=True)
    print(__doc__)
    acoes_orig = dict(V.CHEFE_ACOES)
    antes = varre("ANTES — molde publicado (63 × M uniforme · rank 1 com 4 ações)")
    orig = aplica_regra_nova()
    depois = varre("DEPOIS — molde recalibrado (63/72/78/72/80 · rank 1 com 2 ações)")
    V.make_chefe = orig
    V.CHEFE_ACOES.clear(); V.CHEFE_ACOES.update(acoes_orig)
    compara(antes, depois)
