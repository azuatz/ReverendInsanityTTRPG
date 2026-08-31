"""Quanto a heurística de alvo dos PJs distorce as composições MISTAS?

Motor mira menor FRAÇÃO de vida (peça frágil intacta é atacada por último).
Jogador real foca o pool menor primeiro. Mede a diferença nas cenas mistas.
"""
import importlib.util
import random

path = "/home/azuatz/Documentos/REVEREND INSANITY/_Processo/simulacoes/2026-08-31-cura-real-remedicao.py"
spec = importlib.util.spec_from_file_location("motor", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

orig_pick = mod.pick_weakest


def pick_absoluto(cands):
    """Jogador esperto: contra inimigos, mata o menor pool absoluto primeiro."""
    living = [c for c in cands if (mod.pc_alive(c) if c["side"] == "pc" else mod.enemy_alive(c))]
    if not living:
        return None
    if living[0]["side"] == "pc":
        return orig_pick(cands)  # aliados: cura continua por fração
    return min(living, key=lambda c: c["vit"])


def bateria(modo_absoluto):
    mod.pick_weakest = pick_absoluto if modo_absoluto else orig_pick
    out = {}
    for comp in ("padrao", "padrao_pesado", "dificil", "climax"):
        for rank in (1, 3, 5):
            random.seed(20260830)
            win, _ = mod.simulate(rank, comp, n_iter=2000)
            out[(comp, rank)] = win * 100
    return out


base = bateria(False)
esperto = bateria(True)

print("Heurística de alvo: fração de vida (atual) vs. menor pool absoluto (jogador esperto)")
print(f"{'cena':16s} {'rank':>4s} {'fração':>8s} {'absoluto':>9s} {'delta':>7s}")
for k in base:
    comp, rank = k
    d = esperto[k] - base[k]
    flag = "  <-- MISTA" if comp in ("padrao_pesado", "dificil", "climax") else ""
    print(f"{comp:16s} {rank:>4d} {base[k]:7.1f}% {esperto[k]:8.1f}% {d:+6.1f}pp{flag}")
