"""Variante d' do fork do treino: escada nos moldes SÓ a partir do rank 7.

A (d) da 14ª (min_rank=6) recuperou 7-9 mas superaqueceu o rank 6
(ΔB 0: 51,8 → 4,4%). A d' desloca o piso pra 7: rank 6 fica idêntico ao
baseline por construção; 7-9 mantêm a recuperação. Mede a matriz ΔB e o
"passeio" a ΔB 0 nos 4 ranks.
"""
import importlib.util
import random

path = ("/home/azuatz/Documentos/REVEREND INSANITY/_Processo/simulacoes/"
        "2026-08-31-decima-quarta-bateria-estendida.py")
spec = importlib.util.spec_from_file_location("motor14", path)
mod = importlib.util.module_from_spec(spec)
mod.__name__ = "motor14"
import sys
sys.modules["motor14"] = mod
spec.loader.exec_module(mod)

N = 3000

REF_SEM = {(6, 0): 51.8, (6, 1): None, (6, 3): 3.1,
           (7, 3): 43.4, (8, 3): 79.4, (9, 3): 98.0}
REF_D14 = {(6, 0): 4.4, (6, 3): None, (7, 3): 1.4, (8, 3): 5.4, (9, 3): 57.3}
REF_C = {(6, 3): 3.8, (7, 3): None, (8, 3): 9.4, (9, 3): 63.3}

print("=== VARIANTE d' — treino nos moldes só a partir do rank 7 (min_rank=7) ===")
print("\n--- Matriz ΔB (Chefe imortal + escolta, perfil recém-chegado) ---")
mod.set_treino(pj=False, inimigo=True, inimigo_min_rank=7)
print(f"{'rank':>4s} {'ΔB':>4s} {'d-linha':>8s} {'sem treino (13ª)':>17s} {'d (14ª)':>9s}")
for rank in (6, 7, 8, 9):
    dom = mod.DOMINIO[(rank, "recem")]
    for delta in (0, 1, 3):
        random.seed(20260830)
        r = mod.simulate(rank, "climax", imortal=True, dom_B=dom["B"],
                         pool_mult=dom["pool_mult"], golpe_mode="none", has_boss=True,
                         scenario_factory=lambda rk, d=delta, dm=dom: mod.cena_delta_b(rk, dm, d),
                         n_iter=N)
        ref = REF_SEM.get((rank, delta))
        d14 = REF_D14.get((rank, delta))
        rt = f"{ref:16.1f}%" if ref is not None else "                —"
        dt = f"{d14:8.1f}%" if d14 is not None else "        —"
        print(f"{rank:4d} {delta:+4d} {r['win']*100:7.1f}% {rt} {dt}")

print("\n--- O 'passeio' a ΔB 0 sob a d' (5 composições, ranks 6-9; baseline 75,9-100%) ---")
vals = []
print(f"{'rank':>4s} " + " ".join(f"{c:>15s}" for c in mod.COMPS))
for rank in (6, 7, 8, 9):
    dom = mod.DOMINIO[(rank, "recem")]
    linha = []
    for comp in mod.COMPS:
        random.seed(20260830)
        r = mod.simulate(rank, comp, imortal=True, dom_B=dom["B"],
                         pool_mult=dom["pool_mult"], enemy_B=dom["B"],
                         enemy_pool_mult=dom["pool_mult"], n_iter=N)
        linha.append(r["win"] * 100)
        vals.append((rank, comp, r["win"] * 100))
    print(f"{rank:4d} " + " ".join(f"{v:14.1f}%" for v in linha))
mod.set_treino()

r6 = [v for rk, c, v in vals if rk == 6]
r79 = [v for rk, c, v in vals if rk >= 7]
print(f"\nrank 6 sob a d': {min(r6):.1f}–{max(r6):.1f}%  (deve = baseline 75,9-100% por construção)")
print(f"ranks 7-9 sob a d': {min(r79):.1f}–{max(r79):.1f}%  (a d da 14ª derrubava; queremos dificuldade real SEM zerar)")
