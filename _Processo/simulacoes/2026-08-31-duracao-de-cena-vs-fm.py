import importlib.util
import random

path = "/home/azuatz/Documentos/REVEREND INSANITY/_Processo/simulacoes/2026-08-31-validacao-completa.py"
spec = importlib.util.spec_from_file_location("valcompleta", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def run_combat_counted(pcs, enemies, has_boss=False, golpe_mode="solo"):
    boss = next((e for e in enemies if e.get("is_boss")), None) if has_boss else None
    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    coletivo_tentado = golpe_mode != "coletivo"
    rounds_used = mod.MAX_ROUNDS
    for rnd in range(mod.MAX_ROUNDS):
        if not any(mod.pc_alive(p) for p in pcs) or not any(mod.enemy_alive(e) for e in enemies):
            rounds_used = rnd
            break
        skip_pc_this_round = set()
        if not coletivo_tentado and boss is not None and mod.enemy_alive(boss):
            coletivo_tentado = True
            disparou = mod.golpe_matador_coletivo(pcs, boss)
            if disparou:
                skip_pc_this_round = {id(p) for p in pcs}
        for _, _, entity, side in order:
            if not any(mod.pc_alive(p) for p in pcs) or not any(mod.enemy_alive(e) for e in enemies):
                break
            if side == "pc":
                if id(entity) in skip_pc_this_round:
                    continue
                mod.pc_turn(entity, pcs, enemies, boss if golpe_mode == "solo" else None)
            else:
                mod.enemy_turn(entity, pcs, enemies)
                mod.update_horda_members(entity)
        rounds_used = rnd + 1

    won = not any(mod.enemy_alive(e) for e in enemies)
    return won, rounds_used


random.seed(20260830)
N = 2000
print("Rodadas médias até a resolução (vitória ou derrota do grupo), N=%d" % N)
for comp in ("padrao", "padrao_pesado", "dificil", "climax"):
    print(f"\n--- {comp} ---")
    for rank in (1, 3, 5):
        wins = 0
        total_rounds = 0
        won_rounds = []
        for _ in range(N):
            pcs = mod.make_pcs(rank)
            enemies = mod.make_scenario(rank, comp)
            has_boss = comp == "climax"
            won, rnds = run_combat_counted(pcs, enemies, has_boss=has_boss)
            wins += int(won)
            total_rounds += rnds
            if won:
                won_rounds.append(rnds)
        avg_all = total_rounds / N
        avg_won = sum(won_rounds) / len(won_rounds) if won_rounds else float("nan")
        print(f"  rank {rank}: vitória {wins/N*100:5.1f}%  rodadas médias (todas) {avg_all:.2f}  rodadas médias (só vitórias) {avg_won:.2f}")
