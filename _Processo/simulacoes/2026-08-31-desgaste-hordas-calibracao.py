"""Calibração da Varredura: desgaste médio do grupo contra hordas e reis fera.

Mede vitória, % de Vitalidade perdida, % de essência gasta e rodadas, para
converter cenas de horda em custos abstratos (sistema de Varredura).
"""
import importlib.util
import random

path = "/home/azuatz/Documentos/REVEREND INSANITY/_Processo/simulacoes/2026-08-31-cura-real-remedicao.py"
spec = importlib.util.spec_from_file_location("motor", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def make_rei_cem(rank):
    # Rei de Cem Feras = Elite com traços de fera (Instinto/Sentidos não modelados
    # — sem efeito no motor sem posição) + escolta Horda de 8
    return [mod.make_elite(rank), mod.make_horda(rank, 8)]


def make_rei_mil(rank):
    # Rei de Mil Feras = Chefe (ações por rank) + Horda de 12 + Horda de 8
    return [mod.make_chefe(rank), mod.make_horda(rank, 12), mod.make_horda(rank, 8)]


def run_instrumented(pcs, enemies, has_boss=False):
    boss = next((e for e in enemies if e.get("is_boss")), None) if has_boss else None
    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    rounds_used = mod.MAX_ROUNDS
    for rnd in range(mod.MAX_ROUNDS):
        if not any(mod.pc_alive(p) for p in pcs) or not any(mod.enemy_alive(e) for e in enemies):
            rounds_used = rnd
            break
        for _, _, ent, side in order:
            if not any(mod.pc_alive(p) for p in pcs) or not any(mod.enemy_alive(e) for e in enemies):
                break
            if side == "pc":
                mod.pc_turn(ent, pcs, enemies, boss)
            else:
                mod.enemy_turn(ent, pcs, enemies)
                mod.update_horda_members(ent)
        rounds_used = rnd + 1

    won = not any(mod.enemy_alive(e) for e in enemies)
    vit_lost = sum(max(0, p["vit_max"] - max(p["vit"], 0)) for p in pcs) / sum(p["vit_max"] for p in pcs)
    ess_spent = sum(max(0, p["ess_max"] - max(p["essence"], 0)) for p in pcs) / sum(p["ess_max"] for p in pcs)
    return won, vit_lost, ess_spent, rounds_used


N = 1500
random.seed(20260830)
cenarios = [
    ("Horda 8 (Fácil)", lambda r: [mod.make_horda(r, 8)], False),
    ("2x Horda 8", lambda r: [mod.make_horda(r, 8), mod.make_horda(r, 8)], False),
    ("3x Horda 8", lambda r: [mod.make_horda(r, 8)] * 1 + [mod.make_horda(r, 8), mod.make_horda(r, 8)], False),
    ("Rei de Cem (Elite + Horda 8)", make_rei_cem, False),
    ("Rei de Mil (Chefe + H12 + H8)", make_rei_mil, True),
]
for nome, factory, has_boss in cenarios:
    print(f"\n=== {nome} ===")
    for rank in (2, 3, 4):
        wins = vit_t = ess_t = rnd_t = 0
        for _ in range(N):
            pcs = mod.make_pcs(rank)
            enemies = factory(rank)
            won, vl, es, rd = run_instrumented(pcs, enemies, has_boss=has_boss)
            wins += won
            vit_t += vl
            ess_t += es
            rnd_t += rd
        print(f"  rank {rank}: vitória {wins/N*100:5.1f}%  vit perdida {vit_t/N*100:4.1f}%  essência gasta {ess_t/N*100:4.1f}%  rodadas {rnd_t/N:.1f}")
