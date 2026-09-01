#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIGÉSIMA SEGUNDA RODADA — o Chefe mais duro
===========================================

O autor fechou a escolha do reforço do molde Chefe: **barra maior**
(`Vitalidade 63 × M → 94 × M`), e não ações a mais nem rank acima. As outras
duas caem por motivo já medido — mais ações bate no contador da decisão 137
(a 209 desenhou, mediu e rejeitou uma peça em torno disso), e Chefe de rank
acima é TPK medido e proibido pela própria nota.

DUAS SAÍDAS, NÃO UMA
--------------------
O alvo é **duplo**, e é isso que esta rodada testa:

  · **vitória do grupo em 56-87%** (a faixa do molde)
  · **cena em 6-8 rodadas** (o ritmo que a decisão 208 fixou)

Se a vitória entrar na faixa mas a cena for a 10 rodadas, **o número está
errado mesmo acertando o alvo declarado**. A décima oitava remediu as durações
e o Clímax mede 4,7-6,7 rodadas, abaixo do ritmo desejado — então a barra maior
tem de empurrar a cena *de volta para dentro* da faixa, não estourá-la. É por
isso que as duas saídas andam juntas aqui.

O RISCO SINALIZADO: O RANK 1
----------------------------
O rank 1 já é a célula mais dura da tabela e mede **abaixo** da faixa. Aplicar
`94 × M` uniformemente afunda ele mais. Esta rodada varre a escada inteira de
`vit_mult` por rank, justamente para descobrir se a correção pode ser uniforme
ou se precisa ser por rank.

*(Escolha do autor e sinalização dos dois riscos: sessão `reverend-insanity-8a`.)*

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

VIT_ESCADA = [63, 72, 80, 87, 94, 105]
RANKS = [1, 2, 3, 4, 5]

ALVO_WIN = (0.56, 0.87)
ALVO_RODADAS = (6.0, 8.0)


def cena_climax(vit_mult):
    """A composição publicada de Clímax: Chefe + Guerreiro."""
    def f(rank):
        return [V.make_chefe(rank, vit_mult=vit_mult),
                V.make_guerreiro(rank, especial=True)]
    return f


def marca(win, rodadas):
    ok_w = ALVO_WIN[0] <= win <= ALVO_WIN[1]
    ok_r = ALVO_RODADAS[0] <= rodadas <= ALVO_RODADAS[1]
    if ok_w and ok_r:
        return "✅ os dois"
    if ok_w:
        return "◐ só vitória"
    if ok_r:
        return "◑ só ritmo"
    return "✗"


def varredura():
    print(f"\n{'='*86}")
    print("A ESCADA — vitória do grupo E duração da cena, por Vitalidade do Chefe")
    print(f"alvo: vitória {ALVO_WIN[0]:.0%}-{ALVO_WIN[1]:.0%} · cena "
          f"{ALVO_RODADAS[0]:.0f}-{ALVO_RODADAS[1]:.0f} rodadas")
    print("=" * 86)
    tab = {}
    for rank in RANKS:
        print(f"\n  rank {rank}")
        print(f"  {'VIT':>6} {'vitória':>9} {'rodadas(v)':>11} {'baixas':>8} "
              f"{'TPK-ish':>9} {'timeout':>9}  {'alvo':<14}")
        print("  " + "-" * 80)
        for vm in VIT_ESCADA:
            random.seed(SEED + rank * 131 + vm)
            r = V.simulate(rank, "climax", n_iter=N_ITER,
                           scenario_factory=cena_climax(vm), has_boss=True)
            tab[(rank, vm)] = r
            tpk = 1 - r["sobreviventes"] / 4
            flag = "  ← publicado" if vm == 63 else ("  ← escolhido" if vm == 94 else "")
            print(f"  {vm:>6} {r['win']:>8.1%} {r['rounds_won']:>11.2f} "
                  f"{r['baixas']:>8.2f} {tpk:>8.1%} {r['timeout']:>8.1%}  "
                  f"{marca(r['win'], r['rounds_won']):<14}{flag}")
    return tab


def veredito(tab):
    print(f"\n\n{'='*86}\nO VEREDITO POR RANK\n{'='*86}")
    print(f"{'rank':>4} {'publicado (63)':>22} {'escolhido (94)':>22} "
          f"{'melhor da escada':>26}")
    print("-" * 86)
    escolhas = {}
    for rank in RANKS:
        a, b = tab[(rank, 63)], tab[(rank, 94)]
        # melhor = o que acerta os dois alvos; desempate pela distância do centro
        cand = []
        for vm in VIT_ESCADA:
            r = tab[(rank, vm)]
            ok = (ALVO_WIN[0] <= r["win"] <= ALVO_WIN[1]
                  and ALVO_RODADAS[0] <= r["rounds_won"] <= ALVO_RODADAS[1])
            dist = (abs(r["win"] - 0.715) / 0.155
                    + abs(r["rounds_won"] - 7.0) / 1.0)
            cand.append((not ok, dist, vm, r))
        cand.sort()
        _, _, vm_best, rb = cand[0]
        escolhas[rank] = (vm_best, rb)
        f = lambda r: f"{r['win']:.1%} / {r['rounds_won']:.2f}r"
        print(f"{rank:>4} {f(a):>22} {f(b):>22} "
              f"{('VIT ' + str(vm_best) + ' → ' + f(rb)):>26}")
    print("-" * 86)
    print("\nFormato: vitória / rodadas em cenas vencidas.\n")

    uniforme_ok = all(
        ALVO_WIN[0] <= tab[(r, 94)]["win"] <= ALVO_WIN[1]
        and ALVO_RODADAS[0] <= tab[(r, 94)]["rounds_won"] <= ALVO_RODADAS[1]
        for r in RANKS)
    print(f"O `94 × M` uniforme acerta os dois alvos em TODOS os ranks? "
          f"{'SIM' if uniforme_ok else 'NÃO'}")
    fora = [r for r in RANKS
            if not (ALVO_WIN[0] <= tab[(r, 94)]["win"] <= ALVO_WIN[1])]
    if fora:
        print(f"  ranks fora da faixa de vitória com 94: {fora}")
        for r in fora:
            print(f"    rank {r}: {tab[(r,94)]['win']:.1%} "
                  f"(publicado: {tab[(r,63)]['win']:.1%})")
    fora_r = [r for r in RANKS
              if not (ALVO_RODADAS[0] <= tab[(r, 94)]["rounds_won"] <= ALVO_RODADAS[1])]
    if fora_r:
        print(f"  ranks fora do ritmo 6-8 rodadas com 94: {fora_r}")
        for r in fora_r:
            print(f"    rank {r}: {tab[(r,94)]['rounds_won']:.2f}r "
                  f"(publicado: {tab[(r,63)]['rounds_won']:.2f}r)")
    print()
    print("Escada por rank, se a uniforme não servir:")
    for rank in RANKS:
        vm, rb = escolhas[rank]
        print(f"  rank {rank}: VIT {vm} × M  →  {rb['win']:.1%} · "
              f"{rb['rounds_won']:.2f} rodadas  {marca(rb['win'], rb['rounds_won'])}")


if __name__ == "__main__":
    random.seed(SEED)
    V.configura(lee="melee — foice + Wu Xing", teste_publicado=True,
                heuristica="cauda", portao=3, dobra="sim", abertura=True,
                col_ret_todos=True)
    print(__doc__)
    t = varredura()
    veredito(t)
