#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima primeira rodada — ENCURTAR A CENA (pendência da decisão 160)
===================================================================

Cópia de [[simulacoes/2026-08-31-decima-rodada-alma-rara.py]] (motor mais
atual: mix de Alma rara, correção de densidade da decisão 82, barra de Alma
modelada certo), com DUAS mudanças de motor que apenas sincronizam o script
com a tabela publicada em [[⚔️ Ameaças Genéricas por Rank]] depois da
decisão 207:

  1. "Padrão" no rank 1 é **2 Mestres + 1 Guerreiro** (não 3 Mestres);
  2. a Horda tem **piso de ataques**: 3 contra um alvo só, mínimo 2 contra
     dois alvos, um por personagem de pé acima disso.

E a instrumentação de CONTAGEM DE RODADAS de
[[simulacoes/2026-08-31-duracao-de-cena-vs-fm.py]], que é o que abriu a
pendência (7-12 rodadas medidas contra o alvo declarado de ~3 de F&M).

O autor decidiu **encurtar de verdade — alvo ~4-6 rodadas** — sabendo que é
recalibração de motor. A pendência lista três alavancas; o método pedido (o
mesmo que funcionou nos três mixes de Alma da décima rodada) é medir cada
uma ISOLADA, mesma semente, antes de aplicar qualquer coisa.

AS ALAVANCAS MEDIDAS
--------------------
L1 — RD menor, dois graus:
     L1a `RD × 0,5` (PJ e inimigo: o `1 × M` do molde vira `0,5 × M`, o
          `2 × M` de Elite/Chefe vira `1 × M`)
     L1b `RD = 0` (o extremo: nenhuma RD na cena)
     O **piso** de dano (`nunca abaixo de M`) fica intacto nos dois — ele
     não é RD, é o chão que impede a anulação; baixar RD só faz o piso
     deixar de ser atingido.

L2 — mais dano por Nível, dois graus. NÃO usei "B conta dobrado": no rank 1
     `B = 0` (estágio Inicial), então dobrar B é rigorosamente nulo em
     metade da bateria — mediria nada onde a cena mais dói. Usei a moeda
     que a decisão 79 já define e que funciona em todo rank:
     L2a **+1 Nível de Dano em todo ataque** (dos dois lados): sobe o tipo
          do dado (d6→d8→d10→d12) e, já em d12, vira `+1 por dado` em B;
     L2b **+2 Níveis** na mesma regra.

L3 — menos inimigos por cena: **tira uma peça de cada composição**
     (Padrão r1 2M+1G→2M · Padrão 3M→2M · Padrão pesado 2M+Horda→1M+Horda ·
      Difícil 3M+1G→3M / 4M→3M · Clímax Chefe+Guerreiro→Chefe sozinho).
     É exatamente o penhasco de ações da decisão 137 sendo descido de
     propósito — por isso a vitória é reportada junto com a duração.

OS DOIS GUARDA-CORPOS (o ponto da rodada)
-----------------------------------------
G1 — **Curva de letalidade por Caminho (decisão 78)**: `d6≈5 · d8≈4 ·
     d10≈3,3 · d12≈2,8` acertos pra derrubar um alvo de rank igual com CON
     padrão. Medida por Monte Carlo direto (rolar o pool até a barra zerar),
     em duas leituras:
       · **sem RD** — é a definição literal da decisão 78 (`18 × M` de
         Vitalidade ÷ média do pool: 18/6,5=2,77 · 18/5,5=3,27 · 18/4,5=4,0
         · 18/3,5=5,14 — confere com a escada publicada);
       · **com RD `1 × M`** — a leitura de mesa de verdade, contra um alvo
         com o Gu de defesa sustentado que todo molde carrega.

G2 — **Penhasco de ações (decisão 137)**: o swing de vitória ao somar UMA
     peça (um Guerreiro) à composição, remedido sob cada alavanca. Se uma
     alavanca deixa o penhasco mais íngreme, a tabela de composição inteira
     (que repousa nele) fica pior, não melhor.

Bateria: semente 20260830, 3.000 iterações/célula, ranks 1/3/5,
composições padrao/padrao_pesado/dificil/climax, mix de Alma "C" (o
publicado pela decisão 206: 1d6 = 6 por Mestre).

Uso: python3 "2026-08-31-decima-primeira-duracao.py"
"""

import random

N_ITER = 3000
MAX_ROUNDS = 20

M_TABLE = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256}

STAGE_B = {1: 0, 2: 1, 3: 2, 4: 3, 5: 3}
STAGE_IDX = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}

COMBO_TETO = {0: 2, 1: 3, 2: 4, 3: 5}
SOLO_APOIOS_MAX = {b: COMBO_TETO[b] - 1 for b in COMBO_TETO}

CHEFE_ACOES = {1: 4, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4}

# ---------------------------------------------------------------------------
# AS ALAVANCAS — knobs globais, lidos pelo motor
# ---------------------------------------------------------------------------
RD_MULT = 1.0      # L1: multiplicador global de toda RD (PJ e inimigo)
NIVEL_DELTA = 0    # L2: Níveis de Dano somados a todo ataque dos dois lados
DROP_PIECE = False  # L3: tira uma peça de cada composição

DIE_LADDER = [4, 6, 8, 10, 12]


def apply_niveis(dado, delta=None):
    """Decisão 79 em duas etapas: enquanto < d12 sobe o tipo; em d12, +1 por dado."""
    d = delta if delta is not None else NIVEL_DELTA
    if d <= 0:
        return dado, 0
    extra_b = 0
    cur = dado
    for _ in range(d):
        if cur >= 12:
            extra_b += 1
        else:
            cur = DIE_LADDER[DIE_LADDER.index(cur) + 1]
    return cur, extra_b


def set_lever(rd_mult=1.0, nivel_delta=0, drop_piece=False):
    global RD_MULT, NIVEL_DELTA, DROP_PIECE
    RD_MULT, NIVEL_DELTA, DROP_PIECE = rd_mult, nivel_delta, drop_piece


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

ACT_COST_BASE = 40

FRATURA_ENABLED = True
CONTROLE_ENABLED = True


def make_pc(name, rank, imortal=False, terreno_delta=0):
    b = PCS_BASE[name]
    M = M_TABLE[rank]
    if imortal:
        dom_bonus = 0
        stage_idx = 4
        dado = b["dado"] if b["dado"] >= 12 else b["dado"] + 2
        dado = min(dado, 12)
    else:
        dom_bonus = STAGE_B[rank]
        stage_idx = STAGE_IDX[rank]
        dado = b["dado"]

    if name == "Lee" and terreno_delta:
        dom_bonus = max(0, dom_bonus + terreno_delta)

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
        rd=RD_MULT * 1 * M,
        defense=10 + b["DES"] + 2 * rank,
        alma_def=10 + b["VON"] + rank,
        vazamento=False, skip_turns=0, fallback_raw=False,
        used_golpe=False, actions=1, alive=True,
        cura_usada=False,
    )


def make_pcs(rank, imortal=False, terreno_delta=0):
    return [make_pc(n, rank, imortal, terreno_delta) for n in PCS_BASE]


# ---------------------------------------------------------------------------
# Moldes de inimigo (⚔️ Ameaças Genéricas por Rank)
# ---------------------------------------------------------------------------
def enemy_common(name, rank, vit_mult, alma_ratio, defense, acerto_bonus, rd_mult,
                  dado, actions=1, B=None):
    M = M_TABLE[rank]
    grau = STAGE_B.get(rank, 3) if B is None else B
    vit = vit_mult * M + 4 * M * grau
    return dict(
        name=name, side="enemy", rank=rank, M=M, B=grau, dado=dado,
        vit=vit, vit_max=vit, alma=round(alma_ratio * vit), alma_max=round(alma_ratio * vit),
        essence=None, ess_max=None,
        rd=RD_MULT * rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
        acerto_bonus=acerto_bonus + rank,
        vazamento=False, skip_turns=0, fallback_raw=False,
        actions=actions, alive=True, used_special=False,
        controle_ignorado_usado=False,
    )


def make_guerreiro(rank, especial=True):
    e = enemy_common("Guerreiro", rank, 12, 0.7, 12, 6, 1, 8)
    e["especial"] = especial
    return e


def make_elite(rank):
    e = enemy_common("Elite", rank, 21, 0.7, 14, 8, 2, 10)
    e["especial"] = True
    return e


def make_mestre_de_gu(rank, idx=0, special="alma"):
    e = enemy_common(f"Mestre de Gu {idx}", rank, 21, 15 / 21, 13, 7, 1, 8, actions=2)
    e["special_type"] = special
    return e


def make_chefe(rank, vit_mult=63, dado=10, B=None, defense_base=16, acerto_bonus=8):
    e = enemy_common("Chefe", rank, vit_mult, 0.7, defense_base, acerto_bonus, 2, dado, B=B)
    e["actions"] = CHEFE_ACOES.get(rank, 4)
    e["is_boss"] = True
    return e


def make_horda(rank, n_members):
    M = M_TABLE[rank]
    grau = STAGE_B[rank]
    vit = (6 * M + 4 * M * grau) * n_members
    return dict(
        name="Horda", side="enemy", rank=rank, M=M, B=grau,
        vit=vit, vit_max=vit, alma=None, alma_max=None,
        essence=None, ess_max=None, rd=0, defense=10 + rank, alma_def=None,
        acerto_bonus=6 + rank, n_members=n_members, n_members_max=n_members,
        vazamento=False, skip_turns=0, fallback_raw=False,
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


def horda_n_ataques(n_pcs_vivos):
    """Regra publicada: um ataque por personagem de pé, com PISO de 3 contra um
    alvo só e 2 contra dois alvos (decisão 207)."""
    if n_pcs_vivos <= 1:
        return 3
    return max(2, n_pcs_vivos)


def _mestres(rank, n, n_alma_mix_a, mix):
    out = []
    for i in range(n):
        if mix == "A":
            special = "alma" if i < n_alma_mix_a else "physical"
        elif mix == "B":
            special = "physical"
        elif mix == "C":
            special = "alma" if random.randint(1, 6) == 6 else "physical"
        else:
            raise ValueError(mix)
        out.append(make_mestre_de_gu(rank, i, special=special))
    return out


def make_scenario(rank, comp, mix="C"):
    """Composições PUBLICADAS de [[⚔️ Ameaças Genéricas por Rank]] (pós-207).

    Com DROP_PIECE ligado (alavanca L3), cada composição perde uma peça.
    Sufixo `_mais1g` = a mesma composição + 1 Guerreiro (medição do penhasco
    de ações da decisão 137) — imune ao DROP_PIECE de propósito.
    """
    drop = DROP_PIECE

    if comp == "facil":
        return [make_horda(rank, 8 if not drop else 6)]

    if comp == "padrao":
        if rank == 1:  # decisão 207: Padrão de rank 1 é 2 Mestres + 1 Guerreiro
            if drop:
                return _mestres(rank, 2, 1, mix)
            return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True)]
        return _mestres(rank, 2 if drop else 3, 1, mix)

    if comp == "padrao_pesado":
        return _mestres(rank, 1 if drop else 2, 1, mix) + [make_horda(rank, 8)]

    if comp == "dificil":
        if rank <= 4:
            base = _mestres(rank, 3, 1, mix)
            return base if drop else base + [make_guerreiro(rank, especial=True)]
        return _mestres(rank, 3 if drop else 4, 2, mix)

    if comp == "climax":
        base = [make_chefe(rank)]
        return base if drop else base + [make_guerreiro(rank, especial=True)]

    # --- medição do penhasco de ações: a composição publicada + 1 Guerreiro ---
    if comp == "padrao_mais1g":
        if rank == 1:
            return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
        return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)]
    if comp == "dificil_mais1g":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
        return _mestres(rank, 4, 2, mix) + [make_guerreiro(rank, especial=True)]

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


def apply_fratura(target):
    if not FRATURA_ENABLED:
        return
    roll = random.randint(1, 6)
    if roll in (1, 2):
        if target.get("essence") is not None:
            target["vazamento"] = True
        else:
            target["B"] = max(0, target["B"] - 1)
    elif roll in (3, 4):
        apply_controle(target, turns=1)
    elif roll == 6:
        target["fallback_raw"] = True


def apply_controle(target, turns=1):
    if not CONTROLE_ENABLED:
        return
    if target.get("is_boss") and not target.get("controle_ignorado_usado", False):
        target["controle_ignorado_usado"] = True
        return
    target["skip_turns"] = max(target.get("skip_turns", 0), turns)


def pc_attack_dmg(pc, crit=False):
    n = pc["M"] * (2 if crit else 1)
    dado, extra_b = apply_niveis(pc["dado"])
    raw = roll_pool(n, dado) + pc["M"] * (pc["B"] + extra_b)
    if pc["atk_attr"] == "FOR":
        raw += pc["FOR"]
    return raw, n


def pc_raw_dmg(pc):
    # dano cru sem Gu: um dado só. NÃO recebe os Níveis da alavanca L2 —
    # a alavanca é sobre Níveis de Dano de Gu, e a força humana não escala.
    return max(0, random.randint(1, pc["raw_die"]) + pc["FOR"])


def resolve_pc_hit(pc, target):
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
    else:
        dmg, n = pc_attack_dmg(pc, crit)
        dmg = apply_rd(dmg, target.get("rd", 0), pc["M"])
        pool_name = "vit"

    if pool_name == "alma" and target.get("alma") is None:
        pool_name = "vit"

    target[pool_name] -= dmg
    max_pool = target[pool_name + "_max"]

    downed = False
    if target[pool_name] <= 0:
        downed = True
    elif crit and max_pool and target[pool_name] <= 0.25 * max_pool:
        apply_fratura(target)

    return downed


def resolve_enemy_hit(enemy, target, dado_override=None, bonus_acerto=0, alma_shot=False,
                       aplica_lentidao=False):
    acerto_roll = random.randint(1, 20)
    crit = acerto_roll == 20
    acerto = acerto_roll + enemy["acerto_bonus"] + bonus_acerto
    def_val = target["alma_def"] if alma_shot else target["defense"]
    hit = crit or acerto >= def_val
    if not hit:
        return False

    n = enemy["M"] * (2 if crit else 1)
    dado = dado_override or enemy["dado"]
    dado, extra_b = apply_niveis(dado)
    dmg = roll_pool(n, dado) + enemy["M"] * (enemy.get("B", 0) + extra_b)

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

    if aplica_lentidao and not downed:
        apply_controle(target, turns=1)

    return downed


def pc_alive(pc):
    return pc["vit"] > 0 and pc["alma"] > 0


def enemy_alive(e):
    if e.get("is_horda"):
        return e["vit"] > 0 and e["n_members"] > 0
    return e["vit"] > 0 and (e["alma"] is None or e["alma"] > 0)


def pick_weakest(cands):
    living = [c for c in cands if (pc_alive(c) if c["side"] == "pc" else enemy_alive(c))]
    if not living:
        return None
    def frac(c):
        if c["side"] == "pc":
            return min(c["vit"] / c["vit_max"], c["alma"] / c["alma_max"])
        return c["vit"] / c["vit_max"]
    return min(living, key=frac)


# ---------------------------------------------------------------------------
# Golpes Matadores
# ---------------------------------------------------------------------------
def golpe_matador_xie(xie, boss):
    apoios = SOLO_APOIOS_MAX[xie["B"]] if xie["B"] in SOLO_APOIOS_MAX else SOLO_APOIOS_MAX[max(STAGE_B.values())]
    n_gu = apoios + 1
    custo = ACT_COST_BASE * (n_gu ** 2) * 2
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
            dado, extra_b = apply_niveis(12)
            dmg = roll_pool(n, dado) + xie["M"] * (xie["B"] + apoios + extra_b)
            if boss.get("alma") is not None:
                boss["alma"] -= dmg
                if boss["alma"] > 0 and crit and boss["alma"] <= 0.25 * boss["alma_max"]:
                    apply_fratura(boss)
            else:
                dmg = apply_rd(dmg, boss.get("rd", 0), xie["M"])
                boss["vit"] -= dmg
    else:
        xie["fallback_raw"] = True
        if cd - teste >= 5:
            xie["vit_max"] = round(xie["vit_max"] * 0.95)
            xie["vit"] = min(xie["vit"], xie["vit_max"])


def golpe_matador_coletivo(pcs, boss):
    participants = [p for p in pcs if pc_alive(p)]
    if len(participants) < 2 or boss is None or not enemy_alive(boss):
        return False

    nucleo = next((p for p in participants if p["name"] == "Xie Lang"), participants[0])
    apoios_outros = len(participants) - 1
    bonus_levels = {1: 3, 2: 5, 3: 6}.get(apoios_outros, 3 + apoios_outros)
    n_gu_cd = {2: 2, 3: 3, 4: 5}.get(len(participants), len(participants) + 1)
    cd = 12 + 2 * n_gu_cd - 2

    base_shares = {p["name"]: ACT_COST_BASE * p["ess_mod"] for p in participants}
    total_base = sum(base_shares.values())
    n_gu_custo = len(participants)
    custo_total = total_base * n_gu_custo * 2

    if sum(p["essence"] for p in participants) < custo_total:
        return False

    for p in participants:
        share = base_shares[p["name"]] / total_base
        p["essence"] = max(0, p["essence"] - custo_total * share)

    teste = random.randint(1, 20) + nucleo["AST"]
    if teste >= cd:
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = acerto_roll + nucleo["VON"] + 2 * nucleo["rank"] + 2
        def_val = boss["alma_def"]
        if crit or acerto >= def_val:
            n = nucleo["M"] * (2 if crit else 1)
            dado, extra_b = apply_niveis(12)
            dmg = roll_pool(n, dado) + nucleo["M"] * (nucleo["B"] + bonus_levels + extra_b)
            if boss.get("alma") is not None:
                boss["alma"] -= dmg
                if boss["alma"] > 0 and crit and boss["alma"] <= 0.25 * boss["alma_max"]:
                    apply_fratura(boss)
            else:
                dmg = apply_rd(dmg, boss.get("rd", 0), nucleo["M"])
                boss["vit"] -= dmg
    else:
        nucleo["fallback_raw"] = True
        if cd - teste >= 5:
            for p in participants:
                p["vit_max"] = round(p["vit_max"] * 0.85)
                p["vit"] = min(p["vit"], p["vit_max"])

    return True


# ---------------------------------------------------------------------------
# Turnos
# ---------------------------------------------------------------------------
def pc_turn(pc, pcs, enemies, boss):
    if not pc_alive(pc):
        return
    if pc["skip_turns"] > 0:
        pc["skip_turns"] -= 1
        return
    if pc["vazamento"] and pc["essence"] is not None:
        pc["essence"] = max(0, pc["essence"] - pc["M"])

    if pc["role"] == "healer":
        candidates = [p for p in pcs if pc_alive(p) and p["vit"] / p["vit_max"] < 0.4]
        cost = ACT_COST_BASE * pc["ess_mod"]
        if (candidates and not pc["fallback_raw"] and not pc["cura_usada"]
                and pc["essence"] is not None and pc["essence"] >= cost):
            pc["essence"] -= cost
            pc["cura_usada"] = True
            target = min(candidates, key=lambda p: p["vit"] / p["vit_max"])
            heal = roll_pool(pc["M"], 6)
            target["vit"] = min(target["vit_max"], target["vit"] + heal)
            return

    if pc["name"] == "Xie Lang" and boss is not None and enemy_alive(boss) and not pc["used_golpe"]:
        pc["used_golpe"] = True
        golpe_matador_xie(pc, boss)
        return

    target = pick_weakest(enemies)
    if target is None:
        return
    downed = resolve_pc_hit(pc, target)
    if downed and not target.get("is_horda"):
        target["alive"] = False


def enemy_turn(e, pcs, enemies):
    if e.get("is_horda"):
        if e["vit"] <= 0:
            return
        update_horda_members(e)
        living_pcs = [p for p in pcs if pc_alive(p)]
        n_atk = horda_n_ataques(len(living_pcs))
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
    if e["skip_turns"] > 0:
        e["skip_turns"] -= 1
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
        aplica_lentidao = False

        if is_mestre and not e["used_special"]:
            e["used_special"] = True
            aplica_lentidao = True
            if e.get("special_type", "alma") == "alma":
                alma_shot = True
                dado_override = 12
            else:
                bonus = 4
                dado_override = 10
        elif e.get("especial") and not e["used_special"]:
            e["used_special"] = True
            bonus = 4
            aplica_lentidao = True

        resolve_enemy_hit(e, tgt, dado_override=dado_override, bonus_acerto=bonus,
                           alma_shot=alma_shot, aplica_lentidao=aplica_lentidao)


def update_horda_members(e):
    if not e.get("is_horda"):
        return
    frac = e["vit"] / e["vit_max"] if e["vit_max"] else 0
    e["n_members"] = max(0, round(e["n_members_max"] * max(frac, 0)))


def run_combat(pcs, enemies, has_boss=False, golpe_mode="solo"):
    """Igual ao motor da décima rodada, mas devolve TAMBÉM a rodada em que a
    cena resolveu (instrumentação de 2026-08-31-duracao-de-cena-vs-fm.py)."""
    boss = next((e for e in enemies if e.get("is_boss")), None) if has_boss else None

    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    coletivo_tentado = golpe_mode != "coletivo"
    rounds_used = MAX_ROUNDS

    for rnd in range(MAX_ROUNDS):
        if not any(pc_alive(p) for p in pcs) or not any(enemy_alive(e) for e in enemies):
            rounds_used = rnd
            break

        skip_pc_this_round = set()
        if not coletivo_tentado and boss is not None and enemy_alive(boss):
            coletivo_tentado = True
            if golpe_matador_coletivo(pcs, boss):
                skip_pc_this_round = {id(p) for p in pcs}

        for _, _, entity, side in order:
            if not any(pc_alive(p) for p in pcs) or not any(enemy_alive(e) for e in enemies):
                break
            if side == "pc":
                if id(entity) in skip_pc_this_round:
                    continue
                pc_turn(entity, pcs, enemies, boss if golpe_mode == "solo" else None)
            else:
                enemy_turn(entity, pcs, enemies)
                update_horda_members(entity)
        rounds_used = rnd + 1

    won = not any(enemy_alive(e) for e in enemies)
    survivors = sum(1 for p in pcs if pc_alive(p))
    return won, survivors, rounds_used


def simulate(rank, comp, mix="C", n_iter=N_ITER, golpe_mode="solo"):
    wins = 0
    surv_total = 0
    rounds_total = 0
    rounds_won = []
    timeouts = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank)
        enemies = make_scenario(rank, comp, mix=mix)
        has_boss = "climax" in comp
        won, survivors, rnds = run_combat(pcs, enemies, has_boss=has_boss, golpe_mode=golpe_mode)
        wins += int(won)
        surv_total += survivors
        rounds_total += rnds
        if rnds >= MAX_ROUNDS:
            timeouts += 1
        if won:
            rounds_won.append(rnds)
    return dict(
        win=wins / n_iter,
        surv=surv_total / n_iter,
        rounds=rounds_total / n_iter,
        rounds_won=(sum(rounds_won) / len(rounds_won)) if rounds_won else float("nan"),
        timeout=timeouts / n_iter,
    )


# ---------------------------------------------------------------------------
# GUARDA-CORPO 1 — a curva de letalidade por Caminho (decisão 78)
# ---------------------------------------------------------------------------
def hits_to_kill(dado, rank, com_rd, n_iter=20000):
    """Acertos pra derrubar um alvo de rank igual com CON padrão (0).

    Alvo: Vitalidade `(18 + 3×0 + 4×Grau) × M`, RD `1 × M` (o Gu de defesa
    sustentado que todo molde carrega) ou 0. Atacante: pool `M dX + M×B` no
    mesmo Grau do rank, sem crítico — é o acerto MÉDIO que a decisão 78 declara.

    Devolve DOIS números, medidos, não inferidos:
      `razao`  = Vitalidade ÷ dano médio por acerto (dano médio medido por
                 Monte Carlo de golpes isolados, já com RD e piso aplicados).
                 É a definição literal da decisão 78 — no Grau 0 e sem RD ela
                 reproduz a escada publicada: 5,14 · 4,00 · 3,27 · 2,77.
      `mc`     = acertos até a barra zerar de fato (rolar até cair), que é
                 sempre ~0,5 acerto acima da razão pelo excedente do último golpe.
    """
    M = M_TABLE[rank]
    grau = STAGE_B[rank]
    vit_max = (18 + 4 * grau) * M
    rd = (RD_MULT * 1 * M) if com_rd else 0
    d, extra_b = apply_niveis(dado)

    soma = 0
    for _ in range(n_iter):
        dmg = roll_pool(M, d) + M * (grau + extra_b)
        soma += apply_rd(dmg, rd, M)
    dano_medio = soma / n_iter

    total = 0
    n_mc = max(2000, n_iter // 4)
    for _ in range(n_mc):
        vit = vit_max
        hits = 0
        while vit > 0 and hits <= 200:
            dmg = roll_pool(M, d) + M * (grau + extra_b)
            vit -= apply_rd(dmg, rd, M)
            hits += 1
        total += hits

    return vit_max / dano_medio, total / n_mc


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------
RANKS = (1, 3, 5)
COMPS = ("padrao", "padrao_pesado", "dificil", "climax")

LEVERS = (
    ("BASE", "BASELINE — regras publicadas (pós-decisão 207)", dict()),
    ("L1a", "L1a — RD × 0,5 (PJ e inimigo)", dict(rd_mult=0.5)),
    ("L1b", "L1b — RD = 0 (nenhuma RD na cena)", dict(rd_mult=0.0)),
    ("L2a", "L2a — +1 Nível de Dano em todo ataque (dois lados)", dict(nivel_delta=1)),
    ("L2b", "L2b — +2 Níveis de Dano em todo ataque (dois lados)", dict(nivel_delta=2)),
    ("L3", "L3 — menos inimigos: uma peça a menos por composição", dict(drop_piece=True)),
)


def main():
    print("=" * 100)
    print("DÉCIMA PRIMEIRA RODADA — ENCURTAR A CENA (pendência da decisão 160)")
    print(f"{N_ITER} iterações/célula · teto {MAX_ROUNDS} rodadas · semente 20260830 · mix de Alma C")
    print("Alvo do autor: ~4-6 rodadas (hoje 7-12). Guarda-corpos: decisão 78 e decisão 137.")
    print("=" * 100)

    battery = {}
    cliff = {}

    for key, label, kwargs in LEVERS:
        random.seed(20260830)          # MESMA semente pra toda alavanca
        set_lever(**{**dict(rd_mult=1.0, nivel_delta=0, drop_piece=False), **kwargs})
        print(f"\n### {label} ###")
        print(f"  {'cena':16s} {'rank':>4s}  {'vitória':>8s} {'rodadas':>8s} {'rod(vit)':>9s} "
              f"{'sobrev':>7s} {'timeout':>8s}")
        for comp in COMPS:
            for rank in RANKS:
                r = simulate(rank, comp)
                battery[(key, comp, rank)] = r
                print(f"  {comp:16s} {rank:4d}  {r['win']*100:7.1f}% {r['rounds']:8.2f} "
                      f"{r['rounds_won']:9.2f} {r['surv']:6.2f}/4 {r['timeout']*100:7.1f}%")

        # --- guarda-corpo 2: penhasco de ações (uma peça a mais) ---
        # Medido sempre sobre a composição PUBLICADA (o DROP_PIECE de L3 não
        # se aplica às células `_mais1g`), pra que o degrau seja o mesmo degrau
        # em todas as alavancas.
        random.seed(20260830)
        cliff_kwargs = {**dict(rd_mult=1.0, nivel_delta=0, drop_piece=False), **kwargs}
        cliff_kwargs["drop_piece"] = False
        set_lever(**cliff_kwargs)
        for comp, comp_plus in (("padrao", "padrao_mais1g"), ("dificil", "dificil_mais1g")):
            for rank in RANKS:
                base_r = simulate(rank, comp)
                plus_r = simulate(rank, comp_plus)
                cliff[(key, comp, rank)] = (base_r["win"], plus_r["win"],
                                            base_r["rounds"], plus_r["rounds"])

    # --- resumo comparativo de duração ---
    print("\n" + "=" * 100)
    print("RESUMO — RODADAS MÉDIAS (todas as resoluções) por alavanca")
    print("=" * 100)
    header = f"{'cena / rank':22s}" + "".join(f"{k:>10s}" for k, _, _ in LEVERS)
    print(header)
    for comp in COMPS:
        for rank in RANKS:
            row = f"{comp + ' r' + str(rank):22s}"
            for k, _, _ in LEVERS:
                row += f"{battery[(k, comp, rank)]['rounds']:10.2f}"
            print(row)

    print("\n" + "=" * 100)
    print("RESUMO — VITÓRIA DO GRUPO por alavanca")
    print("=" * 100)
    print(header)
    for comp in COMPS:
        for rank in RANKS:
            row = f"{comp + ' r' + str(rank):22s}"
            for k, _, _ in LEVERS:
                row += f"{battery[(k, comp, rank)]['win']*100:9.1f}%"
            print(row)

    # --- guarda-corpo 1 ---
    print("\n" + "=" * 100)
    print("GUARDA-CORPO 1 — CURVA DE LETALIDADE POR CAMINHO (decisão 78)")
    print("Acertos pra derrubar alvo de rank igual, CON padrão (0). Vitalidade ÷ dano médio")
    print("por acerto (medido). Escada publicada, rank 1 sem RD: d6 5,14 · d8 4,00 · d10 3,27 · d12 2,77")
    print("=" * 100)
    for key, label, kwargs in LEVERS:
        random.seed(20260830)
        set_lever(**{**dict(rd_mult=1.0, nivel_delta=0, drop_piece=False), **kwargs})
        print(f"\n--- {label} ---")
        for rank in RANKS:
            for com_rd in (False, True):
                tag = f"rank {rank} " + ("com RD 1×M" if com_rd else "sem RD (def. da decisão 78)")
                razoes, mcs = [], []
                for dado in (6, 8, 10, 12):
                    rz, mc = hits_to_kill(dado, rank, com_rd, n_iter=12000)
                    razoes.append(rz)
                    mcs.append(mc)
                print(f"  {tag:38s} d6 {razoes[0]:5.2f} · d8 {razoes[1]:5.2f} · "
                      f"d10 {razoes[2]:5.2f} · d12 {razoes[3]:5.2f}   "
                      f"(razão d6/d12 = {razoes[0]/razoes[3]:.2f})")
                print(f"  {'  ↳ rolando até cair (MC)':38s} d6 {mcs[0]:5.2f} · d8 {mcs[1]:5.2f} · "
                      f"d10 {mcs[2]:5.2f} · d12 {mcs[3]:5.2f}")

    # --- guarda-corpo 2 ---
    print("\n" + "=" * 100)
    print("GUARDA-CORPO 2 — PENHASCO DE AÇÕES (decisão 137): somar UM Guerreiro")
    print("swing = vitória(composição) − vitória(composição + 1 Guerreiro), em pontos percentuais")
    print("=" * 100)
    print(f"{'alavanca':8s} {'cena':10s} {'rank':>4s} {'base':>8s} {'+1 peça':>9s} {'swing':>8s} "
          f"{'rod base':>9s} {'rod +1':>8s}")
    for key, _, _ in LEVERS:
        for comp in ("padrao", "dificil"):
            for rank in RANKS:
                wb, wp, rb, rp = cliff[(key, comp, rank)]
                print(f"{key:8s} {comp:10s} {rank:4d} {wb*100:7.1f}% {wp*100:8.1f}% "
                      f"{(wb-wp)*100:7.1f} {rb:9.2f} {rp:8.2f}")

    return battery, cliff


if __name__ == "__main__":
    main()
