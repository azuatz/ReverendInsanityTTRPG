#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulação de combate — motor v2 pós-decisão 133
=================================================

Rodada de simulação para medir o motor de combate ATUAL do vault, depois das
decisões 103-133 do [[🧭 Log de Decisões]] (crítico no 20, iniciativa rolada,
essência sem regen em combate, conversão de 41 fontes de Nível, Fratura da
Abertura em crítico, e o gênio pobre duplo do rank 6).

A rodada anterior ([[🎯 Simulação de Combate — Resultados]], 1a-4a rodadas) foi
escrita em Perl e usava o motor v1 (ordem de turno por DES sem rolar, sem
crítico, com regeneração de essência em combate). Este script reimplementa o
motor em Python, com o mesmo padrão da casa (3.000 iterações/cenário), e
reproduz as MESMAS composições de cena (Fácil = Horda de 8, Padrão = 3 Mestres
de Gu, Difícil = 4 Mestres de Gu, Clímax = 1 Chefe + 1 Guerreiro especial) para
que a comparação rank a rank seja limpa.

SIMPLIFICAÇÕES DELIBERADAS (documentadas para auditoria futura):

  - Cada PJ é representado por UM Gu de ataque "de assinatura" (o que a ficha
    dele já usa como identidade em [[🎲 A Mesa — Personagens dos Jogadores]]):
      Xie Lang -> Caminho da Alma, d12, ignora RD, dano na barra de ALMA do alvo
      Jiãotáng -> melee com Gu de Força ativo, arma pesada d10, FOR fora do pool
      Lee      -> Gu elemental genérico, d8 (perfil "moderado" dos 5 elementos)
      Demvi    -> Caminho do Vento, d10
    Isso é uma simplificação de "todo Caminho tem Gu de ataque em todo rank"
    (decisão 69) — não modela o dial de Wu Xing do Lee nem a Fase Lunar do Xie
    Lang, que já foram medidos à parte e fechados (decisões 97-98).
  - Dano do Caminho da Alma (e a Ação Especial de Alma do Mestre de Gu) drena a
    barra de ALMA do alvo, não a de Vitalidade, com Defesa própria
    (10 + VON + rank) e ignorando RD por completo — é o texto literal de
    [[⚔️ Combate]]. Zerar Alma conta como "fora de combate", análogo a zerar
    Vitalidade (Teste de Morte não é modelado, como nas rodadas anteriores).
  - Lentidão e outras Condições de controle NÃO são modeladas (como nas rodadas
    2-4 anteriores) — o item já está registrado como pendência aberta no Log.
  - Custo de ativação de Gu = 40 (rank próprio) × modificador de Caminho,
    cobrado a cada ativação (não é "liga uma vez e usa de graça"), com a
    Manutenção quadrática dos Gu sustentados OMITIDA (Gu de movimento/defesa
    tratado como custo fixo já embutido na RD/Defesa da ficha, não avaliado
    rodada a rodada) — é a mesma simplificação de custo que a rodada 1-3 usou.
  - Essência de Imortal (rank 6) não tem fórmula própria no Log; por
    analogia ao Grau de Densidade (que para de existir no rank 6), assume-se
    que um Imortal recém-ascendido carrega o equivalente ao Grau Pico mortal
    (fator ×8) — documentado aqui porque é uma extrapolação, não uma regra
    escrita.
  - Golpe Matador do grupo só é tentado nos cenários Clímax (rank 1/2/3/5,
    contra o Chefe) pelo Xie Lang (maior AST da mesa, e o Golpe Matador
    Lua+Alma híbrido é o exemplo usado na própria ficha dele). Não modelado no
    cenário de rank 6 por falta de regra explícita de Teto de Combo pós-estágio
    para imortais.
  - Enemy essência não é rastreada (como nas rodadas anteriores) — só a dos PJs.

Uso: python3 "2026-08-30-motor-v2-pos-decisao-133.py"
"""

import random
import copy
from collections import Counter

random.seed(20260830)

N_ITER = 3000
MAX_ROUNDS = 20

M_TABLE = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256}

# Grau de Densidade (B) e índice de estágio (pra essência) por rank mortal.
# rank1 -> Inicial, rank2 -> Médio, rank3 -> Alto, rank4+ -> Pico
# (é a mesma regra que a Mesa já usa: "estágio acompanha o rank").
STAGE_B = {1: 0, 2: 1, 3: 2, 4: 3, 5: 3}
STAGE_IDX = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}  # pra essMax = pct*4*2^(idx-1)

# Teto de Combo por estágio (decisão 80) e teto do Golpe Matador solo
# = Teto de Combo do estágio - 1 (decisão 119)
COMBO_TETO = {0: 2, 1: 3, 2: 4, 3: 5}  # por B
SOLO_APOIOS_MAX = {b: COMBO_TETO[b] - 1 for b in COMBO_TETO}  # 1,2,3,4

CHEFE_ACOES = {1: 4, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4}

# ---------------------------------------------------------------------------
# Fichas dos 4 PJs (A Mesa — Personagens dos Jogadores)
# ---------------------------------------------------------------------------
PCS_BASE = {
    "Xie Lang": dict(FOR=-1, CON=3, DES=3, AST=2, VON=3, CAR=2, aptidao=86,
                     dado=12, alma_dmg=True, atk_attr="VON", ess_mod=1.25,
                     raw_die=6, role="caster"),
    "Jiaotang": dict(FOR=4, CON=3, DES=2, AST=1, VON=1, CAR=0, aptidao=76,
                      dado=10, alma_dmg=False, atk_attr="FOR", ess_mod=1.0,
                      raw_die=10, role="melee"),
    "Lee": dict(FOR=3, CON=2, DES=2, AST=1, VON=3, CAR=1, aptidao=63,
                dado=8, alma_dmg=False, atk_attr="VON", ess_mod=1.0,
                raw_die=6, role="healer"),
    "Demvi": dict(FOR=-1, CON=1, DES=4, AST=2, VON=3, CAR=2, aptidao=56,
                  dado=10, alma_dmg=False, atk_attr="VON", ess_mod=1.0,
                  raw_die=4, role="striker"),
}

ACT_COST_BASE = 40  # custo de ativação de um Gu do rank próprio (decisão 26)


def make_pc(name, rank, imortal=False):
    b = PCS_BASE[name]
    M = M_TABLE[rank]
    if imortal:
        B = None  # substituído por domínio; PJ recém-ascendido = Vislumbre (B efetivo 0)
        dom_bonus = 0
        stage_idx = 4  # pressuposto: essência de imortal recém-ascendido ~ Grau Pico mortal
        dado = b["dado"] if b["dado"] >= 12 else b["dado"] + 2  # Gu Imortal sobe 1 tipo (teto d12)
        dado = min(dado, 12)
    else:
        B = STAGE_B[rank]
        dom_bonus = B
        stage_idx = STAGE_IDX[rank]
        dado = b["dado"]

    vit_max = (18 + 3 * b["CON"] + 4 * dom_bonus) * M
    alma_max = (12 + 2 * b["VON"] + 3 * dom_bonus) * M
    ess_max = b["aptidao"] * 4 * (2 ** (stage_idx - 1))

    return dict(
        name=name, side="pc", rank=rank, M=M, B=dom_bonus, dado=dado,
        FOR=b["FOR"], CON=b["CON"], DES=b["DES"], AST=b["AST"], VON=b["VON"],
        CAR=b["CAR"], atk_attr=b["atk_attr"], alma_dmg=b["alma_dmg"],
        ess_mod=b["ess_mod"], raw_die=b["raw_die"], role=b["role"],
        vit=vit_max, vit_max=vit_max, alma=alma_max, alma_max=alma_max,
        essence=ess_max, ess_max=ess_max,
        rd=1 * M,  # todo PJ carrega um Gu de defesa sustentado do próprio rank
        defense=10 + b["DES"] + 2 * rank,
        alma_def=10 + b["VON"] + rank,
        vazamento=False, skip_next=False, fallback_raw=False,
        used_golpe=False, actions=1, alive=True,
    )


def make_pcs(rank, imortal=False):
    return [make_pc(n, rank, imortal) for n in PCS_BASE]


# ---------------------------------------------------------------------------
# Moldes de inimigo (⚔️ Ameaças Genéricas por Rank)
# ---------------------------------------------------------------------------
def enemy_common(name, rank, vit_mult, alma_ratio, defense, acerto_bonus, rd_mult,
                  dado, actions=1, B=None):
    """
    Decisão 82: "todo inimigo usa o mesmo Grau de Densidade do grupo" — soma
    +Grau por dado no dano (B) e +4×M×Grau na Vitalidade, exatamente como um PJ.
    Sem isso a mesa (e a simulação) atropela o bestiário a partir do estágio
    Médio, porque só o dano dos PJs cresce dentro do rank.
    """
    M = M_TABLE[rank]
    # rank 6+ não tem mais estágio (decisão 83); um Guerreiro/Elite de apoio num
    # cenário imortal é tratado com o Grau-teto mortal (3), análogo ao Pico.
    grau = STAGE_B.get(rank, 3) if B is None else B
    vit = vit_mult * M + 4 * M * grau
    return dict(
        name=name, side="enemy", rank=rank, M=M, B=grau, dado=dado,
        vit=vit, vit_max=vit, alma=round(alma_ratio * vit), alma_max=round(alma_ratio * vit),
        essence=None, ess_max=None,
        rd=rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
        acerto_bonus=acerto_bonus + rank,
        vazamento=False, skip_next=False, fallback_raw=False,
        actions=actions, alive=True, used_special=False,
    )


def make_guerreiro(rank, especial=True):
    e = enemy_common("Guerreiro", rank, 12, 0.7, 12, 6, 1, 8)
    e["especial"] = especial
    return e


def make_elite(rank):
    e = enemy_common("Elite", rank, 21, 0.7, 14, 8, 2, 10)
    e["especial"] = True
    return e


def make_mestre_de_gu(rank, idx=0):
    e = enemy_common(f"Mestre de Gu {idx}", rank, 21, 15 / 21, 13, 7, 1, 8, actions=2)
    return e


def make_chefe(rank, vit_mult=63, dado=10, B=None, defense_base=16, acerto_bonus=8):
    e = enemy_common("Chefe", rank, vit_mult, 0.7, defense_base, acerto_bonus, 2, dado, B=B)
    e["actions"] = CHEFE_ACOES.get(rank, 4)
    e["is_boss"] = True
    return e


def make_horda(rank, n_members):
    M = M_TABLE[rank]
    grau = STAGE_B[rank]
    vit = (6 * M + 4 * M * grau) * n_members  # decisão 82, aplicado por membro
    return dict(
        name="Horda", side="enemy", rank=rank, M=M, B=grau,
        vit=vit, vit_max=vit, alma=None, alma_max=None,  # dano de Alma não afeta a Horda (enxame)
        essence=None, ess_max=None, rd=0, defense=10 + rank, alma_def=None,
        acerto_bonus=6 + rank, n_members=n_members, n_members_max=n_members,
        vazamento=False, skip_next=False, fallback_raw=False,
        actions=0, alive=True, is_horda=True,
    )


def horda_dado(n_members):
    if n_members >= 16:
        return 12
    if n_members >= 12:
        return 10
    if n_members >= 8:
        return 8
    return 6


def make_scenario(rank, comp):
    if comp == "facil":
        return [make_horda(rank, 8)]
    if comp == "padrao":
        return [make_mestre_de_gu(rank, i) for i in range(3)]
    if comp == "dificil":
        return [make_mestre_de_gu(rank, i) for i in range(4)]
    if comp == "climax":
        return [make_chefe(rank), make_guerreiro(rank, especial=True)]
    raise ValueError(comp)


# ---------------------------------------------------------------------------
# Motor de dano
# ---------------------------------------------------------------------------
def roll_pool(n, sides):
    return sum(random.randint(1, sides) for _ in range(n))


def apply_rd(dmg, rd, m_floor):
    if rd <= 0:
        return dmg
    return max(dmg - rd, m_floor)


FRATURA_ENABLED = True  # flag global, usada pra medir o impacto isolado da regra


def apply_fratura(target):
    """Decisão 132: crítico que deixa o alvo a <=25% de Vitalidade/Alma máxima."""
    if not FRATURA_ENABLED:
        return
    roll = random.randint(1, 6)
    if roll in (1, 2):  # Vazamento
        if target.get("essence") is not None:
            target["vazamento"] = True
        else:
            target["B"] = max(0, target["B"] - 1)
    elif roll in (3, 4):  # Gu Atordoados
        target["skip_next"] = True
    elif roll == 6:  # Esmagamento
        target["fallback_raw"] = True
    # roll == 5: Fratura funda (Teste de Morte não modelado) -> sem efeito


def pc_attack_dmg(pc, crit=False):
    n = pc["M"] * (2 if crit else 1)
    raw = roll_pool(n, pc["dado"]) + pc["M"] * pc["B"]
    if pc["atk_attr"] == "FOR":
        raw += pc["FOR"]
    return raw, n


def pc_raw_dmg(pc):
    return max(0, random.randint(1, pc["raw_die"]) + pc["FOR"])


def resolve_pc_hit(pc, target, is_boss_target=False):
    """Retorna True se o alvo caiu (vit ou alma <=0)."""
    used_raw = pc["fallback_raw"] or (pc["essence"] is not None and pc["essence"] < ACT_COST_BASE * pc["ess_mod"])
    attr_val = pc[pc["atk_attr"]]
    acerto_roll = random.randint(1, 20)
    crit = acerto_roll == 20
    acerto = acerto_roll + attr_val + 2 * pc["rank"] + 2

    if not used_raw:
        pc["essence"] -= ACT_COST_BASE * pc["ess_mod"]

    alma_shot = pc["alma_dmg"] and not used_raw
    def_val = target["alma_def"] if (alma_shot and target.get("alma_def") is not None) else target["defense"]
    hit = crit or acerto >= def_val

    if not hit:
        return False

    if used_raw:
        dmg = pc_raw_dmg(pc)
        dmg = apply_rd(dmg, target.get("rd", 0), 1)
        pool_name = "vit"
    elif alma_shot and target.get("alma") is not None:
        dmg, n = pc_attack_dmg(pc, crit)
        pool_name = "alma"
        # dano de Alma ignora RD por completo
    else:
        dmg, n = pc_attack_dmg(pc, crit)
        dmg = apply_rd(dmg, target.get("rd", 0), pc["M"])
        pool_name = "vit"

    if pool_name == "alma" and target.get("alma") is None:
        pool_name = "vit"  # alvo sem barra de Alma modelada (ex.: Horda) -> vai na Vitalidade

    target[pool_name] -= dmg
    max_pool = target[pool_name + "_max"]

    downed = False
    if target[pool_name] <= 0:
        downed = True
    elif crit and max_pool and target[pool_name] <= 0.25 * max_pool:
        apply_fratura(target)

    return downed


def enemy_attack_dmg(enemy, dado_override=None, bonus_acerto=0, alma_shot=False):
    n = enemy["M"]
    dado = dado_override or enemy["dado"]
    dmg = roll_pool(n, dado) + n * enemy.get("B", 0)
    return dmg


def resolve_enemy_hit(enemy, target, dado_override=None, bonus_acerto=0, alma_shot=False):
    acerto_roll = random.randint(1, 20)
    crit = acerto_roll == 20
    acerto = acerto_roll + enemy["acerto_bonus"] + bonus_acerto
    def_val = target["alma_def"] if alma_shot else target["defense"]
    hit = crit or acerto >= def_val
    if not hit:
        return False

    n = enemy["M"] * (2 if crit else 1)
    dado = dado_override or enemy["dado"]
    dmg = roll_pool(n, dado) + enemy["M"] * enemy.get("B", 0)

    if alma_shot:
        pool = "alma"
    else:
        pool = "vit"
        dmg = apply_rd(dmg, target.get("rd", 0), enemy["M"])

    target[pool] -= dmg
    max_pool = target[pool + "_max"]
    downed = target[pool] <= 0
    if not downed and crit and max_pool and target[pool] <= 0.25 * max_pool:
        apply_fratura(target)
    return downed


def pc_alive(pc):
    return pc["vit"] > 0 and pc["alma"] > 0


def enemy_alive(e):
    if e.get("is_horda"):
        return e["vit"] > 0 and e["n_members"] > 0
    alive_vit = e["vit"] > 0
    alive_alma = e["alma"] is None or e["alma"] > 0
    return alive_vit and alive_alma


def pick_weakest(cands):
    living = [c for c in cands if (pc_alive(c) if c["side"] == "pc" else enemy_alive(c))]
    if not living:
        return None
    def frac(c):
        if c["side"] == "pc":
            return min(c["vit"] / c["vit_max"], c["alma"] / c["alma_max"])
        if c.get("is_horda"):
            return c["vit"] / c["vit_max"]
        return c["vit"] / c["vit_max"]
    return min(living, key=frac)


def golpe_matador_xie(xie, boss):
    apoios = SOLO_APOIOS_MAX[xie["B"]] if xie["B"] in SOLO_APOIOS_MAX else SOLO_APOIOS_MAX[max(STAGE_B.values())]
    n_gu = apoios + 1
    custo = ACT_COST_BASE * (n_gu ** 2) * 2  # híbrido Lua+Alma: x2
    if xie["essence"] < custo:
        return
    xie["essence"] -= custo
    cd = 12 + 2 * n_gu
    teste = random.randint(1, 20) + xie["AST"]
    if teste >= cd:
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = acerto_roll + xie["VON"] + 2 * xie["rank"] + 2
        def_val = boss["alma_def"]
        if crit or acerto >= def_val:
            n = xie["M"] * (2 if crit else 1)
            dmg = roll_pool(n, 12) + xie["M"] * (xie["B"] + apoios)
            if boss.get("alma") is not None:
                boss["alma"] -= dmg
                if boss["alma"] > 0 and crit and boss["alma"] <= 0.25 * boss["alma_max"]:
                    apply_fratura(boss)
            else:
                dmg = apply_rd(dmg, boss.get("rd", 0), xie["M"])
                boss["vit"] -= dmg
    else:
        # Retaliação: falha na conjuração -> Gu inutilizáveis pelo resto da cena
        xie["fallback_raw"] = True
        if cd - teste >= 5:
            xie["vit_max"] = round(xie["vit_max"] * 0.95)
            xie["vit"] = min(xie["vit"], xie["vit_max"])


def pc_turn(pc, pcs, enemies, boss):
    if not pc_alive(pc):
        return
    if pc["skip_next"]:
        pc["skip_next"] = False
        return
    if pc["vazamento"] and pc["essence"] is not None:
        pc["essence"] = max(0, pc["essence"] - pc["M"])

    # cura: papel do Lee, quando alguém (incl. ele) está <40%
    if pc["role"] == "healer":
        candidates = [p for p in pcs if pc_alive(p) and p["vit"] / p["vit_max"] < 0.4]
        cost = ACT_COST_BASE * pc["ess_mod"]
        if candidates and not pc["fallback_raw"] and pc["essence"] is not None and pc["essence"] >= cost:
            pc["essence"] -= cost
            target = min(candidates, key=lambda p: p["vit"] / p["vit_max"])
            heal = roll_pool(pc["M"], 8)
            target["vit"] = min(target["vit_max"], target["vit"] + heal)
            return

    # Golpe Matador: só o Xie Lang, só contra o Chefe, uma vez por cena (decisão 71/119)
    if pc["name"] == "Xie Lang" and boss is not None and enemy_alive(boss) and not pc["used_golpe"]:
        pc["used_golpe"] = True
        golpe_matador_xie(pc, boss)
        return

    target = pick_weakest(enemies)
    if target is None:
        return
    downed = resolve_pc_hit(pc, target)
    if downed:
        if target.get("is_horda"):
            pass
        else:
            target["alive"] = False


def enemy_turn(e, pcs, enemies):
    if e.get("is_horda"):
        if e["vit"] <= 0:
            return
        update_horda_members(e)  # o dado sobe/desce ANTES de rolar o ataque
        living_pcs = [p for p in pcs if pc_alive(p)]
        n_atk = len(living_pcs)
        for _ in range(n_atk):
            living_pcs = [p for p in pcs if pc_alive(p)]
            if not living_pcs:
                return
            tgt = random.choice(living_pcs)
            dado = horda_dado(e["n_members"])
            resolve_enemy_hit(e, tgt, dado_override=dado)
        return

    if not enemy_alive(e):
        return
    if e["skip_next"]:
        e["skip_next"] = False
        return
    if e["vazamento"]:
        e["B"] = max(0, e["B"] - 1)
        e["vazamento"] = False

    n_actions = e["actions"]
    is_mestre = e["name"].startswith("Mestre de Gu")

    for act_i in range(n_actions):
        living_pcs = [p for p in pcs if pc_alive(p)]
        if not living_pcs:
            return
        tgt = pick_weakest(living_pcs)

        bonus = 0
        alma_shot = False
        dado_override = None

        if is_mestre and not e["used_special"]:
            e["used_special"] = True
            alma_shot = True
            dado_override = 12
        elif e.get("especial") and not e["used_special"]:
            e["used_special"] = True
            bonus = 4

        resolve_enemy_hit(e, tgt, dado_override=dado_override, bonus_acerto=bonus, alma_shot=alma_shot)


def update_horda_members(e):
    if not e.get("is_horda"):
        return
    frac = e["vit"] / e["vit_max"] if e["vit_max"] else 0
    e["n_members"] = max(0, round(e["n_members_max"] * max(frac, 0)))


def run_combat(pcs, enemies, has_boss=False):
    boss = next((e for e in enemies if e.get("is_boss")), None) if has_boss else None

    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    for rnd in range(MAX_ROUNDS):
        if not any(pc_alive(p) for p in pcs):
            break
        if not any(enemy_alive(e) for e in enemies):
            break
        for _, _, entity, side in order:
            if not any(pc_alive(p) for p in pcs) or not any(enemy_alive(e) for e in enemies):
                break
            if side == "pc":
                pc_turn(entity, pcs, enemies, boss)
            else:
                enemy_turn(entity, pcs, enemies)
                update_horda_members(entity)

    won = any(enemy_alive(e) for e in enemies) is False
    survivors = sum(1 for p in pcs if pc_alive(p))
    return won, survivors


def simulate(rank, comp, imortal=False, n_iter=N_ITER):
    wins = 0
    surv_total = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=imortal)
        enemies = make_scenario(rank, comp)
        has_boss = comp == "climax"
        won, survivors = run_combat(pcs, enemies, has_boss=has_boss)
        wins += int(won)
        surv_total += survivors
    return wins / n_iter, surv_total / n_iter


# ---------------------------------------------------------------------------
# Cenário novo: NPC rank 6 "Imortal denso duplo-gênio" (decisão 133)
# ---------------------------------------------------------------------------
def make_double_genius_boss(rank=6):
    """
    Rank 6, real Pequeno Feito (~9.000 Marcas no Caminho principal, d12 —
    Espada/Alma/Relâmpago), mas com os DOIS feitos de compreensão da decisão
    133 empilhados: opera como Grão-Mestre (+3 Níveis de Dano / B=+3), apesar
    da contagem real (que travaria ele em Pequeno Feito, B=+1).
    """
    M = M_TABLE[rank]
    vit = 63 * M
    e = dict(
        name="Imortal Denso Duplo-Gênio", side="enemy", rank=rank, M=M, B=3,
        dado=12, vit=vit, vit_max=vit, alma=round(0.7 * vit), alma_max=round(0.7 * vit),
        essence=None, ess_max=None, rd=2 * M, defense=16 + rank, alma_def=10 + rank + 3,
        acerto_bonus=8 + rank, actions=CHEFE_ACOES.get(rank, 4),
        vazamento=False, skip_next=False, fallback_raw=False, alive=True,
        is_boss=True,
    )
    return e


def make_pequeno_feito_boss(rank=6):
    """Controle: o MESMO NPC sem o empilhamento do gênio pobre (B=+1, Pequeno Feito real)."""
    e = make_double_genius_boss(rank)
    e = dict(e)
    e["B"] = 1
    e["name"] = "Imortal Denso (Pequeno Feito real, sem gênio pobre)"
    return e


def make_scenario_rank6(boss_factory):
    rank = 6
    return [boss_factory(rank), make_guerreiro(rank, especial=True)]


def simulate_rank6(boss_factory, n_iter=N_ITER):
    wins = 0
    surv_total = 0
    for _ in range(n_iter):
        pcs = make_pcs(6, imortal=True)
        enemies = make_scenario_rank6(boss_factory)
        won, survivors = run_combat(pcs, enemies, has_boss=True)
        wins += int(won)
        surv_total += survivors
    return wins / n_iter, surv_total / n_iter


def simulate_all():
    print("=" * 78)
    print("SIMULAÇÃO DE COMBATE — MOTOR v2 PÓS-DECISÃO 133")
    print(f"{N_ITER} iterações por cenário, limite de {MAX_ROUNDS} rodadas, semente 20260830")
    print("=" * 78)

    results = {}
    for rank in (1, 2, 3, 5):
        print(f"\n--- RANK {rank} ---")
        for comp in ("facil", "padrao", "dificil", "climax"):
            win, surv = simulate(rank, comp)
            results[(rank, comp)] = (win, surv)
            print(f"  {comp:10s}  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    print("\n--- RANK 6 — NPC Imortal Denso Duplo-Gênio (Grão-Mestre por empilhamento) ---")
    win_dg, surv_dg = simulate_rank6(make_double_genius_boss)
    print(f"  Clímax (Chefe duplo-gênio + Guerreiro especial): vitória {win_dg*100:5.1f}%   sobreviventes {surv_dg:.2f}/4")

    print("\n--- RANK 6 — controle: mesmo NPC SEM o empilhamento (Pequeno Feito real) ---")
    win_pf, surv_pf = simulate_rank6(make_pequeno_feito_boss)
    print(f"  Clímax (Chefe Pequeno Feito real + Guerreiro especial): vitória {win_pf*100:5.1f}%   sobreviventes {surv_pf:.2f}/4")

    # ---- Impacto isolado da Fratura da Abertura (liga/desliga) ----
    global FRATURA_ENABLED
    print("\n--- Impacto da Fratura da Abertura (decisão 132) — liga vs desliga ---")
    fratura_rows = []
    for rank in (1, 3, 5):
        for comp in ("padrao", "dificil", "climax"):
            FRATURA_ENABLED = True
            win_on, surv_on = simulate(rank, comp, n_iter=N_ITER)
            FRATURA_ENABLED = False
            win_off, surv_off = simulate(rank, comp, n_iter=N_ITER)
            FRATURA_ENABLED = True
            delta = (win_off - win_on) * 100
            fratura_rows.append((rank, comp, win_on, win_off, delta, surv_on, surv_off))
            print(f"  rank {rank} {comp:10s}  com={win_on*100:5.1f}%  sem={win_off*100:5.1f}%  "
                  f"Δletalidade(grupo)={delta:+5.1f}pp  surv com={surv_on:.2f} sem={surv_off:.2f}")

    return results, (win_dg, surv_dg), (win_pf, surv_pf), fratura_rows


if __name__ == "__main__":
    simulate_all()
