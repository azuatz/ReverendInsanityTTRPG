#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima quarta rodada — A BATERIA ESTENDIDA (solo, PvP, e o híbrido do treino)
=============================================================================

Cópia de [[simulacoes/2026-08-31-decima-terceira-validacao-final.py]] (o motor
mais atual: contabilidade do Colapso Espiritual da decisão 205, mix de Alma
rara "C" da decisão 206, piso de ataques da Horda e Padrão escalado da
decisão 207, suporte imortal ΔB da oitava rodada, knobs de treino da bateria 5
da décima terceira). **Nada do motor foi reescrito** — só uma extensão nos
knobs de treino (abaixo) e as baterias novas. Lote pedido pelo autor: quatro
medições que as rodadas anteriores deixaram para trás.

O QUE MUDOU NO MOTOR
--------------------
Uma coisa só: `treino_inimigo()` ganhou `TREINO_INIMIGO_MIN_RANK` — o knob que
permite ligar a escada de treino SÓ nos moldes de rank imortal (6+), que é o
híbrido da bateria 4. Com o piso em 1 (default), o comportamento é idêntico
ao da décima terceira; com o knob desligado, os caminhos de código devolvem 0
sem consumir nenhum número aleatório, então as baterias de baseline reproduzem
a décima terceira bit-a-bit (verificado dentro da própria bateria 4).

AS QUATRO BATERIAS
------------------
B1 — **Horda solo, remedida com o piso (decisão 207)**: a nona rodada mediu
     1 PJ × Horda de 8 ANTES do piso de ataques existir (10-19 rodadas,
     vitória 10-99% conforme o perfil). Remedido: 4 PJs × ranks 1/3/5 com o
     piso ativo (3 ataques/rodada contra alvo único). Alvo do autor pra
     batalha solo: **7-9 rodadas**. Se o piso sozinho não entregar o alvo,
     medem-se também as hipóteses de escala à la F&M: Horda proporcional à
     mesa (1 PJ → Horda de 2 e de 3) e escala só-de-Vitalidade
     (`VIT × n/4`, mantendo o dado dos 8 membros).

B2 — **Rei de Cem solo, remedido**: mesma razão — a nona mediu pré-207
     (melhor caso 8,4%, quase tudo 0-6%). Expectativa: continua sentença
     (é o desenho publicado, "cena Difícil pra mesa de 4"); confirmar.

B3 — **PJ × PJ — primeira medição no motor atual**: as rodadas 1-4 mediram
     duelos no motor Perl antigo (pré-pool) e nunca mais. Os 6 pares dos
     4 PJs × ranks 1/3/5: vitória, rodadas médias, % de duelos decididos em
     1-2 rodadas (o aviso do Livro do Mestre de F&M) e % de quedas por Alma.
     SÓ MEDIÇÃO — nenhuma regra muda.

B4 — **O híbrido do fork do treino (item 🔴 da decisão 213)**: a décima
     terceira mediu as saídas (a)/(b)/(c); existe um híbrido óbvio que o Log
     não listou — **(a) na fase mortal + (c) restrita aos moldes de rank
     6+**: treino fica FORA da matemática mortal (tabelas publicadas seguem
     certas como estão), mas os moldes imortais ganham a escada de treino no
     acerto fechado (`d20 + rank + N` → `+ treino escalado`), atacando a
     assimetria exata que a decisão 202 diagnosticou (acerto de inimigo
     +1/rank vs Defesa de PJ +2/rank). Medido: a matriz ΔB (ranks 6-9 ×
     ΔB 0/+1/+3) com treino do molde LIGADO e treino de PJ DESLIGADO, mais
     as 5 composições a ΔB 0 (o "passeio") sob o híbrido, mais a bateria
     mortal completa sob o híbrido (deve ser IDÊNTICA ao baseline — o
     híbrido não toca rank ≤ 5 por construção). SÓ MEDIÇÃO — o número vai
     pro item de fork do autor, nada é aplicado.

Bateria: semente 20260830, 3.000 iterações/célula, mix de Alma "C",
premissa das tabelas publicadas (treino = 0 dos dois lados) em TUDO exceto a
bateria 4, que é explicitamente sobre o knob do treino.

Uso: python3 "2026-08-31-decima-quarta-bateria-estendida.py"
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
# COLAPSO ESPIRITUAL (decisão 205)
# ---------------------------------------------------------------------------
# True  = regra atual: Alma 0 tira o personagem da cena, mas NÃO é morte
#         (primeira queda nunca mata; morte real é a segunda, fora da cena).
# False = modelo antigo do motor (Alma 0 = baixa), mantido só para medir a
#         diferença com a mesma semente. NÃO altera nenhuma rolagem.
COLAPSO_ESPIRITUAL = True

# ---------------------------------------------------------------------------
# BÔNUS DE TREINO ESCALADO (decisão 211) — aplicado às regras HOJE, sem medição
# ---------------------------------------------------------------------------
# [[💪 Atributos]]: "+2, e sobe +1 a cada rank PAR", teto +6.
# O motor de TODAS as rodadas anteriores modela `treino = 0` no acerto
# (`d20 + atributo + 2×rank + 2` = `(rank+2) + rank do Gu`, sem treino), então
# ligar isto é medir a decisão 211 pela primeira vez. Os moldes de inimigo
# trazem o acerto fechado (`d20 + rank + 4/6/7/8`), que embute atributo e rank
# de Gu mas NÃO treino — por isso o lado do inimigo é um knob separado.
TREINO = {1: 2, 2: 3, 3: 3, 4: 4, 5: 4, 6: 5, 7: 5, 8: 6, 9: 6}
# ATENÇÃO — premissa histórica do motor, descoberta nesta rodada: o acerto de
# PJ é `d20 + atributo + 2×rank + 2`, que decompõe em `(rank+2) + rank do Gu`
# e portanto modela `treino = 0`. Mas [[💪 Atributos]] põe `+ treino` na
# fórmula de acerto de Gu desde MUITO antes da decisão 211 (quando o bônus era
# +2 fixo). Ou seja: parte do swing medido abaixo é a decisão 211, e parte é
# uma lacuna de modelagem antiga. `TREINO_FLAT` isola as duas.
TREINO_PJ = False       # decisão 211 como está publicada hoje (só o lado do PJ)
TREINO_INIMIGO = False  # a correção simétrica candidata que a própria 211 nomeia
TREINO_FLAT = None      # se != None, usa este valor fixo (a regra pré-211: +2)
# NOVO nesta rodada — o knob do HÍBRIDO da bateria 4: com TREINO_INIMIGO
# ligado, só moldes de rank >= este piso recebem a escada. 1 = comportamento
# da décima terceira (todos); 6 = "(a) mortal + (c) imortal".
TREINO_INIMIGO_MIN_RANK = 1


def treino_pj(rank):
    if TREINO_FLAT is not None:
        return TREINO_FLAT
    return TREINO[rank] if TREINO_PJ else 0


def treino_inimigo(rank):
    if not TREINO_INIMIGO or rank < TREINO_INIMIGO_MIN_RANK:
        return 0
    return TREINO[rank]


def set_treino(pj=False, inimigo=False, flat=None, inimigo_min_rank=1):
    global TREINO_PJ, TREINO_INIMIGO, TREINO_FLAT, TREINO_INIMIGO_MIN_RANK
    TREINO_PJ, TREINO_INIMIGO, TREINO_FLAT = pj, inimigo, flat
    TREINO_INIMIGO_MIN_RANK = inimigo_min_rank

# Níveis de domínio de Marca por rank imortal (oitava rodada, decisões 194-195)
DOMINIO = {
    (6, "recem"): dict(B=0, pool_mult=1, nome="Vislumbre"),
    (6, "denso"): dict(B=1, pool_mult=1, nome="Pequeno Feito"),
    (7, "recem"): dict(B=2, pool_mult=1, nome="Mestre"),
    (7, "denso"): dict(B=3, pool_mult=1, nome="Grão-Mestre"),
    (8, "recem"): dict(B=3, pool_mult=1, nome="Grão-Mestre"),
    (8, "denso"): dict(B=4, pool_mult=1, nome="Quase-Supremo"),
    (9, "recem"): dict(B=5, pool_mult=2, nome="Grande Mestre Supremo"),
    (9, "denso"): dict(B=5, pool_mult=2, nome="Grande Mestre Supremo"),
}

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


def make_pc(name, rank, imortal=False, terreno_delta=0, dom_B=None, pool_mult=1):
    """`dom_B`/`pool_mult` portados da oitava rodada (bateria imortal)."""
    b = PCS_BASE[name]
    M = M_TABLE[rank]
    if imortal:
        dom_bonus = 0 if dom_B is None else dom_B
        stage_idx = 4
        dado = b["dado"] if b["dado"] >= 12 else b["dado"] + 2
        dado = min(dado, 12)
    else:
        pool_mult = 1
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
        pool_mult=pool_mult,
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


def make_pcs(rank, imortal=False, terreno_delta=0, dom_B=None, pool_mult=1):
    return [make_pc(n, rank, imortal, terreno_delta, dom_B=dom_B,
                    pool_mult=pool_mult) for n in PCS_BASE]


# ---------------------------------------------------------------------------
# Moldes de inimigo (⚔️ Ameaças Genéricas por Rank)
# ---------------------------------------------------------------------------
def enemy_common(name, rank, vit_mult, alma_ratio, defense, acerto_bonus, rd_mult,
                  dado, actions=1, B=None, pool_mult=1):
    M = M_TABLE[rank]
    grau = STAGE_B.get(rank, 3) if B is None else B
    vit = vit_mult * M + 4 * M * grau
    return dict(
        name=name, side="enemy", rank=rank, M=M, B=grau, dado=dado,
        pool_mult=pool_mult,
        vit=vit, vit_max=vit, alma=round(alma_ratio * vit), alma_max=round(alma_ratio * vit),
        essence=None, ess_max=None,
        rd=RD_MULT * rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
        acerto_bonus=acerto_bonus + rank,
        vazamento=False, skip_turns=0, fallback_raw=False,
        actions=actions, alive=True, used_special=False,
        controle_ignorado_usado=False,
    )


def make_guerreiro(rank, especial=True, B=None, pool_mult=1):
    e = enemy_common("Guerreiro", rank, 12, 0.7, 12, 6, 1, 8, B=B, pool_mult=pool_mult)
    e["especial"] = especial
    return e


def make_elite(rank, B=None, pool_mult=1):
    e = enemy_common("Elite", rank, 21, 0.7, 14, 8, 2, 10, B=B, pool_mult=pool_mult)
    e["especial"] = True
    return e


def make_mestre_de_gu(rank, idx=0, special="alma", B=None, pool_mult=1):
    e = enemy_common(f"Mestre de Gu {idx}", rank, 21, 15 / 21, 13, 7, 1, 8, actions=2,
                     B=B, pool_mult=pool_mult)
    e["special_type"] = special
    return e


def make_chefe(rank, vit_mult=63, dado=10, B=None, defense_base=16, acerto_bonus=8,
               pool_mult=1):
    e = enemy_common("Chefe", rank, vit_mult, 0.7, defense_base, acerto_bonus, 2, dado,
                     B=B, pool_mult=pool_mult)
    e["actions"] = CHEFE_ACOES.get(rank, 4)
    e["is_boss"] = True
    return e


def make_horda(rank, n_members, B=None, pool_mult=1):
    M = M_TABLE[rank]
    grau = STAGE_B.get(rank, 3) if B is None else B
    vit = (6 * M + 4 * M * grau) * n_members
    return dict(
        name="Horda", side="enemy", rank=rank, M=M, B=grau, pool_mult=pool_mult,
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


def _mestres(rank, n, n_alma_mix_a, mix, B=None, pool_mult=1):
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
        out.append(make_mestre_de_gu(rank, i, special=special, B=B, pool_mult=pool_mult))
    return out


def make_scenario(rank, comp, mix="C", enemy_B=None, enemy_pool_mult=1):
    """Composições PUBLICADAS de [[⚔️ Ameaças Genéricas por Rank]] (pós-207).

    Com DROP_PIECE ligado (alavanca L3), cada composição perde uma peça.
    Sufixo `_mais1g` = a mesma composição + 1 Guerreiro (medição do penhasco
    de ações da decisão 137) — imune ao DROP_PIECE de propósito.
    """
    drop = DROP_PIECE
    kw = dict(B=enemy_B, pool_mult=enemy_pool_mult)
    mkw = dict(mix=mix, B=enemy_B, pool_mult=enemy_pool_mult)

    if comp == "facil":
        return [make_horda(rank, 8 if not drop else 6, **kw)]

    if comp == "padrao":
        if rank == 1:  # decisão 207: Padrão de rank 1 é 2 Mestres + 1 Guerreiro
            if drop:
                return _mestres(rank, 2, 1, **mkw)
            return _mestres(rank, 2, 1, **mkw) + [make_guerreiro(rank, especial=True, **kw)]
        return _mestres(rank, 2 if drop else 3, 1, **mkw)

    if comp == "padrao_pesado":
        return _mestres(rank, 1 if drop else 2, 1, **mkw) + [make_horda(rank, 8, **kw)]

    if comp == "dificil":
        if rank <= 4:
            base = _mestres(rank, 3, 1, **mkw)
            return base if drop else base + [make_guerreiro(rank, especial=True, **kw)]
        return _mestres(rank, 3 if drop else 4, 2, **mkw)

    if comp == "climax":
        base = [make_chefe(rank, **kw)]
        return base if drop else base + [make_guerreiro(rank, especial=True, **kw)]

    # --- medição do penhasco de ações: a composição publicada + 1 Guerreiro ---
    if comp == "padrao_mais1g":
        if rank == 1:
            return _mestres(rank, 2, 1, **mkw) + [make_guerreiro(rank, especial=True, **kw) for _ in range(2)]
        return _mestres(rank, 3, 1, **mkw) + [make_guerreiro(rank, especial=True, **kw)]
    if comp == "dificil_mais1g":
        if rank <= 4:
            return _mestres(rank, 3, 1, **mkw) + [make_guerreiro(rank, especial=True, **kw) for _ in range(2)]
        return _mestres(rank, 4, 2, **mkw) + [make_guerreiro(rank, especial=True, **kw)]

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
    n = pc["M"] * pc.get("pool_mult", 1) * (2 if crit else 1)
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
    acerto = acerto_roll + attr_val + 2 * pc["rank"] + 2 + treino_pj(pc["rank"])

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
    acerto = (acerto_roll + enemy["acerto_bonus"] + bonus_acerto
              + treino_inimigo(enemy["rank"]))
    def_val = target["alma_def"] if alma_shot else target["defense"]
    hit = crit or acerto >= def_val
    if not hit:
        return False

    n = enemy["M"] * enemy.get("pool_mult", 1) * (2 if crit else 1)
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
    """Quem AGE e É ALVO na cena — deliberadamente INALTERADO.

    Decisão 205: Alma zerada = inconsciente. Nos dois modelos (Colapso ligado
    ou desligado) o personagem sai da cena do mesmo jeito, então nenhuma
    rolagem muda e o fluxo aleatório é o mesmo das rodadas anteriores.
    """
    return pc["vit"] > 0 and pc["alma"] > 0


def pc_baixa_real(pc):
    """Baixa DE VERDADE ao fim da cena — é aqui que a decisão 205 muda tudo.

    Com o Colapso ligado (regra atual), só Vitalidade zerada conta como baixa:
    o caído por Alma está inconsciente com uma sequela, e a PRIMEIRA queda
    nunca mata (a morte real seria uma segunda queda de Alma com a sequela
    ainda aberta — outra cena, por definição). O Teste de Morte físico segue
    exatamente como o motor sempre modelou.

    Com o flag desligado, reproduz o modelo antigo (`alma <= 0` = morte), que
    é o que o motor fazia antes desta rodada. Serve só para medir a diferença.
    """
    if pc["vit"] <= 0:
        return True
    if not COLAPSO_ESPIRITUAL and pc["alma"] <= 0:
        return True
    return False


def pc_caido_por_alma(pc):
    """Fora da cena por Colapso Espiritual, com o corpo intacto."""
    return pc["alma"] <= 0 and pc["vit"] > 0


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
        acerto = acerto_roll + xie["VON"] + 2 * xie["rank"] + 2 + treino_pj(xie["rank"])
        def_val = boss["alma_def"]
        if crit or acerto >= def_val:
            n = xie["M"] * xie.get("pool_mult", 1) * (2 if crit else 1)
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
        acerto = (acerto_roll + nucleo["VON"] + 2 * nucleo["rank"] + 2
                  + treino_pj(nucleo["rank"]))
        def_val = boss["alma_def"]
        if crit or acerto >= def_val:
            n = nucleo["M"] * nucleo.get("pool_mult", 1) * (2 if crit else 1)
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
    de_pe = sum(1 for p in pcs if pc_alive(p))
    baixas = sum(1 for p in pcs if pc_baixa_real(p))
    caidos_alma = sum(1 for p in pcs if pc_caido_por_alma(p))
    vit_lost = (sum(max(0, p["vit_max"] - max(p["vit"], 0)) for p in pcs)
                / sum(p["vit_max"] for p in pcs))
    ess_spent = (sum(max(0, p["ess_max"] - max(p["essence"], 0)) for p in pcs)
                 / sum(p["ess_max"] for p in pcs))
    stats = dict(de_pe=de_pe, baixas=baixas, caidos_alma=caidos_alma,
                 sobreviventes=4 - baixas, vit_lost=vit_lost, ess_spent=ess_spent)
    return won, de_pe, rounds_used, stats


def simulate(rank, comp, mix="C", n_iter=N_ITER, golpe_mode="solo",
             scenario_factory=None, imortal=False, dom_B=None, pool_mult=1,
             has_boss=None, enemy_B=None, enemy_pool_mult=1):
    """Bateria genérica. `scenario_factory(rank)` sobrepõe `make_scenario` para
    as cenas de [[🐺 Reis Fera e a Maré]] (Reis, ondas), que não estão na
    tabela de composição."""
    wins = 0
    rounds_total = 0
    rounds_won = []
    timeouts = 0
    acc = dict(de_pe=0, baixas=0, caidos_alma=0, sobreviventes=0,
               vit_lost=0.0, ess_spent=0.0)
    cenas_com_colapso = 0
    derrotas = 0
    derrotas_sem_baixa = 0
    vit_lost_won = []
    ess_spent_won = []
    rounds_won_only = []
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=imortal, dom_B=dom_B, pool_mult=pool_mult)
        if scenario_factory is not None:
            enemies = scenario_factory(rank)
        else:
            enemies = make_scenario(rank, comp, mix=mix, enemy_B=enemy_B,
                                    enemy_pool_mult=enemy_pool_mult)
        boss_flag = ("climax" in comp) if has_boss is None else has_boss
        won, de_pe, rnds, st = run_combat(pcs, enemies, has_boss=boss_flag,
                                          golpe_mode=golpe_mode)
        wins += int(won)
        rounds_total += rnds
        for k in acc:
            acc[k] += st[k]
        if st["caidos_alma"]:
            cenas_com_colapso += 1
        if not won:
            derrotas += 1
            if st["baixas"] == 0:
                derrotas_sem_baixa += 1
        if rnds >= MAX_ROUNDS:
            timeouts += 1
        if won:
            rounds_won.append(rnds)
            vit_lost_won.append(st["vit_lost"])
            ess_spent_won.append(st["ess_spent"])
            rounds_won_only.append(rnds)

    def _mean(xs):
        return (sum(xs) / len(xs)) if xs else float("nan")

    return dict(
        win=wins / n_iter,
        surv=acc["de_pe"] / n_iter,               # de pé ao fim (métrica histórica)
        sobreviventes=acc["sobreviventes"] / n_iter,  # não-baixas (decisão 205)
        baixas=acc["baixas"] / n_iter,
        caidos_alma=acc["caidos_alma"] / n_iter,
        cenas_com_colapso=cenas_com_colapso / n_iter,
        derrotas_sem_baixa=(derrotas_sem_baixa / derrotas) if derrotas else float("nan"),
        rounds=rounds_total / n_iter,
        rounds_won=_mean(rounds_won),
        vit_lost=acc["vit_lost"] / n_iter,
        ess_spent=acc["ess_spent"] / n_iter,
        vit_lost_won=_mean(vit_lost_won),
        ess_spent_won=_mean(ess_spent_won),
        timeout=timeouts / n_iter,
    )



# ---------------------------------------------------------------------------
# Cenas de [[🐺 Reis Fera e a Maré]] (decisão 200) — fora da tabela de composição
# ---------------------------------------------------------------------------
def rei_de_cem(rank):
    """Elite com traços de fera + escolta de Horda de 8.

    Instinto/Sentidos não são modelados (não têm efeito num motor sem posição
    nem via social) — igual à calibração original de 2026-08-31."""
    return [make_elite(rank), make_horda(rank, 8)]


def rei_de_mil(rank):
    """Chefe (ações por rank) + Horda de 12 + Horda de 8, simultâneos."""
    return [make_chefe(rank), make_horda(rank, 12), make_horda(rank, 8)]


def onda_unica(rank):
    return [make_horda(rank, 8)]


def duas_hordas(rank):
    return [make_horda(rank, 8), make_horda(rank, 8)]


def tres_hordas(rank):
    return [make_horda(rank, 8), make_horda(rank, 8), make_horda(rank, 8)]


# ---------------------------------------------------------------------------
# Âncora imortal da oitava rodada — o dial ΔB da decisão 205
# ---------------------------------------------------------------------------
def make_chefe_imortal(rank, B, pool_mult=1):
    """Mesmo Chefe da âncora da oitava rodada (Gu Imortal de ataque no d12),
    com o nível de domínio `B` como único dial."""
    return make_chefe(rank, dado=12, B=B, pool_mult=pool_mult)


def cena_delta_b(rank, dom, delta):
    """Chefe a ΔB + escolta de Guerreiro no domínio DO GRUPO (escolta é textura,
    como a régua publicada diz)."""
    return [make_chefe_imortal(rank, dom["B"] + delta, dom["pool_mult"]),
            make_guerreiro(rank, especial=True, B=dom["B"], pool_mult=dom["pool_mult"])]



# ---------------------------------------------------------------------------
# Fábricas das cenas SOLO (baterias 1-2)
# ---------------------------------------------------------------------------
def horda8(rank):
    """A regra publicada: Horda de 8, com o piso de 3 ataques vs. alvo único
    (o piso já vive em horda_n_ataques(), decisão 207)."""
    return [make_horda(rank, 8)]


def horda_n(n):
    """Hipótese F&M nº 1 — a Horda escala com a mesa: 1 PJ → Horda de n."""
    def f(rank):
        return [make_horda(rank, n)]
    return f


def horda_vit_escalada(n_pcs):
    """Hipótese F&M nº 2 — só a Vitalidade escala (`VIT × n/4`), mantendo o
    dado dos 8 membros: a matilha PARECE cheia (bate como 8, d8) mas a barra
    é dimensionada pra quem está lá. O dado degrada junto com a barra, como
    na Horda normal (update_horda_members recalcula membros pela fração)."""
    def f(rank):
        h = make_horda(rank, 8)
        h["vit"] = h["vit_max"] = round(h["vit_max"] * n_pcs / 4)
        return [h]
    return f


def simulate_solo(name, rank, scenario_factory, n_iter=N_ITER):
    """1 PJ contra a cena — mesmas leituras da nona rodada (vitória, rodadas
    médias nas vitórias, % de Vitalidade restante nas vitórias), mais a média
    de rodadas de TODAS as cenas (é contra ela que o alvo 7-9 se lê)."""
    wins = 0
    rounds_all = []
    rounds_won = []
    vit_rest_won = []
    timeouts = 0
    caidos_alma = 0
    for _ in range(n_iter):
        pcs = [make_pc(name, rank)]
        enemies = scenario_factory(rank)
        won, _, rnds, _st = run_combat(pcs, enemies, has_boss=False)
        rounds_all.append(rnds)
        if rnds >= MAX_ROUNDS and not won:
            timeouts += 1
        if won:
            wins += 1
            rounds_won.append(rnds)
            vit_rest_won.append(max(pcs[0]["vit"], 0) / pcs[0]["vit_max"])
        if pc_caido_por_alma(pcs[0]):
            caidos_alma += 1

    def _mean(xs):
        return (sum(xs) / len(xs)) if xs else float("nan")

    return dict(win=wins / n_iter, rounds=_mean(rounds_all),
                rounds_won=_mean(rounds_won), vit_rest_won=_mean(vit_rest_won),
                timeout=timeouts / n_iter, caidos_alma=caidos_alma / n_iter)


# ---------------------------------------------------------------------------
# Os números da NONA RODADA (pré-piso) — a comparação da bateria 1 e 2
# ---------------------------------------------------------------------------
# (vitória %, rodadas médias nas vitórias) — 🥷 Nona rodada, tabela "Horda de 8"
NONA_HORDA = {
    ("Xie Lang", 1): (69.6, 9.7), ("Xie Lang", 3): (56.6, 13.0), ("Xie Lang", 5): (57.5, 14.5),
    ("Jiaotang", 1): (99.1, 5.8), ("Jiaotang", 3): (51.6, 12.6), ("Jiaotang", 5): (34.3, 15.7),
    ("Lee", 1): (71.6, 10.2), ("Lee", 3): (10.2, 17.3), ("Lee", 5): (12.3, 19.0),
    ("Demvi", 1): (15.2, 12.1), ("Demvi", 3): (30.3, 14.5), ("Demvi", 5): (39.2, 16.1),
}
# vitória % — 🥷 Nona rodada, tabela "Rei de Cem Feras"
NONA_REI = {
    ("Xie Lang", 1): 3.7, ("Xie Lang", 3): 3.0, ("Xie Lang", 5): 6.0,
    ("Jiaotang", 1): 8.4, ("Jiaotang", 3): 0.1, ("Jiaotang", 5): 0.1,
    ("Lee", 1): 0.0, ("Lee", 3): 0.0, ("Lee", 5): 0.0,
    ("Demvi", 1): 0.0, ("Demvi", 3): 0.0, ("Demvi", 5): 0.1,
}

RANKS_SOLO = (1, 3, 5)
ALVO_SOLO = (7.0, 9.0)  # rodadas — alvo do autor pra batalha solo
RANKS_MORTAIS = (1, 2, 3, 4, 5)
COMPS = ("facil", "padrao", "padrao_pesado", "dificil", "climax")


# ---------------------------------------------------------------------------
# BATERIA 1 — Horda solo, remedida com o piso (decisão 207)
# ---------------------------------------------------------------------------
def bateria_1():
    print("=" * 108)
    print("BATERIA 1 — HORDA SOLO REMEDIDA COM O PISO (decisão 207)")
    print("Nona rodada (pré-piso): 10-19 rodadas, vitória 10-99% conforme o perfil.")
    print(f"Alvo do autor pra batalha solo: {ALVO_SOLO[0]:.0f}-{ALVO_SOLO[1]:.0f} rodadas.")
    print("=" * 108)

    variantes = (
        ("piso", "Horda de 8 + piso (a regra publicada hoje)", horda8),
        ("h2", "Horda de 2 (proporcional à mesa: 8 × 1/4)", horda_n(2)),
        ("h3", "Horda de 3 (proporcional, teto da faixa 2-3)", horda_n(3)),
        ("vit", "Horda 8 com VIT × 1/4 (dado dos 8 membros)", horda_vit_escalada(1)),
    )
    out = {}
    for key, label, factory in variantes:
        print(f"\n### {label} ###")
        print(f"  {'PJ':10s} {'rank':>4s} {'vitória':>8s} {'nona':>7s} {'Δpp':>7s} "
              f"{'rodadas':>8s} {'rod(vit.)':>10s} {'nona':>6s} {'vit.rest':>9s} {'timeout':>8s}")
        for rank in RANKS_SOLO:
            for name in PCS_BASE:
                random.seed(20260830)
                r = simulate_solo(name, rank, factory)
                out[(key, name, rank)] = r
                if key == "piso":
                    pub_w, pub_r = NONA_HORDA[(name, rank)]
                    reftxt = f"{pub_w:6.1f}%"
                    dtxt = f"{r['win']*100 - pub_w:+7.1f}"
                    refr = f"{pub_r:5.1f}"
                else:
                    reftxt, dtxt, refr = "     —", "      —", "    —"
                print(f"  {name:10s} {rank:4d} {r['win']*100:7.1f}% {reftxt} {dtxt} "
                      f"{r['rounds']:7.2f}  {r['rounds_won']:9.2f} {refr:>6s} "
                      f"{r['vit_rest_won']*100:8.1f}% {r['timeout']*100:7.1f}%")

    print("\n" + "-" * 108)
    print("RESUMO CONTRA O ALVO (7-9 rodadas, sem trivializar a cena)")
    print("-" * 108)
    for key, label, _f in variantes:
        rs = [out[(key, n, rk)]["rounds"] for rk in RANKS_SOLO for n in PCS_BASE]
        ws = [out[(key, n, rk)]["win"] * 100 for rk in RANKS_SOLO for n in PCS_BASE]
        dentro = sum(1 for r in rs if ALVO_SOLO[0] <= r <= ALVO_SOLO[1])
        print(f"  {label:46s} rodadas {min(rs):4.1f}-{max(rs):4.1f} "
              f"(média {sum(rs)/len(rs):4.1f}, {dentro}/12 células em 7-9) · "
              f"vitória {min(ws):4.1f}-{max(ws):4.1f}%")
    return out


# ---------------------------------------------------------------------------
# BATERIA 2 — Rei de Cem solo, remedido com o piso
# ---------------------------------------------------------------------------
def bateria_2():
    print("\n" + "=" * 108)
    print("BATERIA 2 — REI DE CEM SOLO REMEDIDO (Elite + Horda de 8, agora com o piso)")
    print("Nona rodada (pré-piso): melhor caso 8,4% (Jiaotang r1), quase tudo 0-6%.")
    print("Expectativa de design: continua sentença ('cena Difícil pra mesa de 4').")
    print("=" * 108)
    print(f"  {'PJ':10s} {'rank':>4s} {'vitória':>8s} {'nona':>7s} {'Δpp':>7s} "
          f"{'rodadas':>8s} {'timeout':>8s}")
    piores = []
    for rank in RANKS_SOLO:
        for name in PCS_BASE:
            random.seed(20260830)
            r = simulate_solo(name, rank, rei_de_cem)
            pub = NONA_REI[(name, rank)]
            piores.append(r["win"] * 100)
            print(f"  {name:10s} {rank:4d} {r['win']*100:7.1f}% {pub:6.1f}% "
                  f"{r['win']*100 - pub:+7.1f} {r['rounds']:7.2f} {r['timeout']*100:7.1f}%")
    print(f"\n  Melhor caso da mesa inteira: {max(piores):.1f}%  "
          f"(nona, pré-piso: 8,4%) — sentença confirmada se continuar ≤ ~10%")


# ---------------------------------------------------------------------------
# BATERIA 3 — PJ × PJ no motor atual (primeira vez desde as rodadas Perl 1-4)
# ---------------------------------------------------------------------------
def run_duel(a, b):
    """Duelo 1v1 com o MESMO motor do grupo: iniciativa d20+DES, pc_turn dos
    dois lados (cada um vê o outro como 'enemies'). Sem Chefe na cena, o
    Golpe Matador não dispara (gatilho do motor, como em todas as baterias);
    o Lee se cura (único candidato — a leitura solo da nona rodada)."""
    ia = random.randint(1, 20) + a["DES"]
    ib = random.randint(1, 20) + b["DES"]
    if ib > ia or (ib == ia and random.randint(0, 1) == 1):
        order = (b, a)
    else:
        order = (a, b)
    for rnd in range(MAX_ROUNDS):
        for p in order:
            if not (pc_alive(a) and pc_alive(b)):
                break
            opp = b if p is a else a
            pc_turn(p, [p], [opp], None)
        if not pc_alive(a) or not pc_alive(b):
            winner = a if pc_alive(a) else (b if pc_alive(b) else None)
            return winner, rnd + 1
    return None, MAX_ROUNDS


def simulate_duel(name_a, name_b, rank, n_iter=N_ITER):
    wa = wb = draws = rapidos = quedas_alma = 0
    rounds = []
    for _ in range(n_iter):
        a = make_pc(name_a, rank)
        b = make_pc(name_b, rank)
        w, rnds = run_duel(a, b)
        rounds.append(rnds)
        if w is a:
            wa += 1
        elif w is b:
            wb += 1
        else:
            draws += 1
        if w is not None:
            if rnds <= 2:
                rapidos += 1
            loser = b if w is a else a
            if pc_caido_por_alma(loser):
                quedas_alma += 1
    return dict(win_a=wa / n_iter, win_b=wb / n_iter, draw=draws / n_iter,
                rounds=sum(rounds) / len(rounds), rapidos=rapidos / n_iter,
                quedas_alma=quedas_alma / n_iter)


def bateria_3():
    print("\n" + "=" * 108)
    print("BATERIA 3 — PJ × PJ NO MOTOR ATUAL (rodadas 1-4 mediram duelos só no motor Perl antigo)")
    print("Duas perguntas: (a) algum par degenera em 1-2 rodadas (o aviso de PvP do Livro do")
    print("Mestre de F&M)? (b) algum PJ é dominante/sem-saída na tabela inteira?")
    print("SÓ MEDIÇÃO — nenhuma regra muda; o conserto de F&M (metade de dano/cura/RD em PvP")
    print("+ condição Ferido escalonada) já está catalogado como padrão NÃO aplicado na Síntese.")
    print("=" * 108)

    nomes = list(PCS_BASE)
    pares = [(nomes[i], nomes[j]) for i in range(len(nomes)) for j in range(i + 1, len(nomes))]
    out = {}
    for rank in RANKS_SOLO:
        print(f"\n### rank {rank} ###")
        print(f"  {'duelo':26s} {'vit. A':>8s} {'vit. B':>8s} {'empate':>7s} "
              f"{'rodadas':>8s} {'≤2 rod.':>8s} {'queda p/Alma':>13s}")
        for na, nb in pares:
            random.seed(20260830)
            r = simulate_duel(na, nb, rank)
            out[(na, nb, rank)] = r
            print(f"  {na:>11s} × {nb:12s} {r['win_a']*100:7.1f}% {r['win_b']*100:7.1f}% "
                  f"{r['draw']*100:6.1f}% {r['rounds']:7.2f} {r['rapidos']*100:7.1f}% "
                  f"{r['quedas_alma']*100:12.1f}%")

    print("\n" + "-" * 108)
    print("PLACAR GERAL (média de vitória de cada PJ nos 3 duelos dele, por rank)")
    print("-" * 108)
    print(f"  {'PJ':10s} " + " ".join(f"{'rank ' + str(rk):>8s}" for rk in RANKS_SOLO))
    for nome in nomes:
        linha = []
        for rank in RANKS_SOLO:
            tot = []
            for (na, nb, rk), r in out.items():
                if rk != rank:
                    continue
                if na == nome:
                    tot.append(r["win_a"] / (r["win_a"] + r["win_b"]) if (r["win_a"] + r["win_b"]) else 0.5)
                elif nb == nome:
                    tot.append(r["win_b"] / (r["win_a"] + r["win_b"]) if (r["win_a"] + r["win_b"]) else 0.5)
            linha.append(sum(tot) / len(tot) * 100)
        print(f"  {nome:10s} " + " ".join(f"{v:7.1f}%" for v in linha))
    rapid_max = max(r["rapidos"] for r in out.values())
    print(f"\n  Duelos decididos em 1-2 rodadas, pior célula: {rapid_max*100:.1f}%  "
          f"(o aviso de F&M dispara se isso for a norma, não a cauda)")
    return out


# ---------------------------------------------------------------------------
# BATERIA 4 — o HÍBRIDO do fork do treino: (a) mortal + (c) só moldes rank 6+
# ---------------------------------------------------------------------------
# Referências da décima terceira (mesma semente, mesmas células):
REF13_SEM_TREINO = {  # âncora ΔB, "sem treino" (o publicado)
    (6, 0): 51.8, (7, 0): 91.3, (8, 0): 99.0, (9, 0): 99.6,
    (6, 1): 23.3, (7, 1): 79.9, (8, 1): 96.5, (9, 1): 99.0,
    (6, 3): 3.1, (7, 3): 43.4, (8, 3): 79.4, (9, 3): 98.0,
}
REF13_SIMETRICO = {  # saída (c) medida na décima terceira (células publicadas)
    (7, 3): 3.8, (8, 3): 9.4, (9, 1): 84.3, (9, 3): 63.3,
}


def bateria_4():
    print("\n" + "=" * 108)
    print("BATERIA 4 — O HÍBRIDO DO FORK DO TREINO (item 🔴 da decisão 213)")
    print("Híbrido = saída (a) na fase mortal (treino fora da conta, tabelas ficam como estão)")
    print("+ saída (c) SÓ nos moldes de rank 6+ (a escada de treino entra no acerto fechado deles).")
    print("PJ nunca recebe treino em nenhuma das duas fases. SÓ MEDIÇÃO — nada é aplicado.")
    print("=" * 108)

    configs = (
        ("baseline (sem treino — deve reproduzir a 13ª)", dict()),
        ("HÍBRIDO (molde 6+ com treino, PJ sem)", dict(inimigo=True, inimigo_min_rank=6)),
    )

    # --- (i) a matriz ΔB, ranks 6-9 × ΔB 0/+1/+3 ---
    print("\n### (i) A matriz ΔB (Chefe imortal d12 + escolta no domínio do grupo, golpe_mode='none') ###")
    res = {}
    for label, kw in configs:
        set_treino(**kw)
        print(f"\n  --- {label} ---")
        print(f"  {'rank':>4s} {'ΔB':>4s} {'vitória':>8s} {'13ª s/treino':>13s} "
              f"{'13ª simétr.':>12s} {'de pé':>6s} {'rodadas':>8s}")
        for rank in (6, 7, 8, 9):
            dom = DOMINIO[(rank, "recem")]
            for delta in (0, 1, 3):
                random.seed(20260830)
                r = simulate(rank, "climax", imortal=True, dom_B=dom["B"],
                             pool_mult=dom["pool_mult"], golpe_mode="none", has_boss=True,
                             scenario_factory=lambda rk, d=delta, dm=dom: cena_delta_b(rk, dm, d))
                res[(label, rank, delta)] = r
                ref = REF13_SEM_TREINO.get((rank, delta))
                refc = REF13_SIMETRICO.get((rank, delta))
                reftxt = f"{ref:12.1f}%" if ref is not None else "           —"
                refctxt = f"{refc:11.1f}%" if refc is not None else "          —"
                print(f"  {rank:4d} {delta:+4d} {r['win']*100:7.1f}% {reftxt} {refctxt} "
                      f"{r['surv']:5.2f} {r['rounds']:7.2f}")
    set_treino()

    print("\n  A PERGUNTA DA RODADA — o híbrido recupera a dificuldade imortal como a (c)?")
    print(f"  {'célula':12s} {'sem treino':>11s} {'híbrido':>9s} {'simétrico (c)':>14s}")
    for rank, delta in ((6, 3), (7, 3), (8, 3), (9, 1), (9, 3)):
        b = res[(configs[0][0], rank, delta)]["win"] * 100
        h = res[(configs[1][0], rank, delta)]["win"] * 100
        c = REF13_SIMETRICO.get((rank, delta))
        ctxt = f"{c:13.1f}%" if c is not None else "            —"
        print(f"  rank {rank} ΔB+{delta}  {b:10.1f}% {h:8.1f}% {ctxt}")

    # --- (ii) o "passeio" a ΔB 0 sob o híbrido (5 composições, ranks 6-9) ---
    print("\n### (ii) As 5 composições a ΔB 0 sob o híbrido — o 'passeio' (75,9-100%) vira o quê? ###")
    print("Aqui o híbrido toca TUDO (Mestres, Guerreiro, Chefe E Horda de rank 6+ ganham treino).")
    comp_res = {}
    for label, kw in configs:
        set_treino(**kw)
        print(f"\n  --- {label} ---")
        print(f"  {'rank':>4s} " + " ".join(f"{c:>15s}" for c in COMPS))
        for rank in (6, 7, 8, 9):
            dom = DOMINIO[(rank, "recem")]
            linha = []
            for comp in COMPS:
                random.seed(20260830)
                r = simulate(rank, comp, imortal=True, dom_B=dom["B"],
                             pool_mult=dom["pool_mult"], enemy_B=dom["B"],
                             enemy_pool_mult=dom["pool_mult"])
                comp_res[(label, rank, comp)] = r
                linha.append(r["win"] * 100)
            print(f"  {rank:4d} " + " ".join(f"{v:14.1f}%" for v in linha))
    set_treino()
    hib = [comp_res[(configs[1][0], rk, c)]["win"] * 100 for rk in (6, 7, 8, 9) for c in COMPS]
    print(f"\n  Faixa a ΔB 0 sob o híbrido: {min(hib):.1f}% – {max(hib):.1f}%  "
          f"(baseline/publicado: 75,9-100%)")

    # --- (iii) a fase mortal sob o híbrido — deve ser IDÊNTICA ao baseline ---
    print("\n### (iii) Fase mortal sob o híbrido — a metade '(a)' da promessa: NADA pode mudar ###")
    dmax = 0.0
    for comp in COMPS:
        for rank in RANKS_MORTAIS:
            vals = []
            for label, kw in configs:
                set_treino(**kw)
                random.seed(20260830)
                r = simulate(rank, comp)
                vals.append(r["win"] * 100)
            dmax = max(dmax, abs(vals[1] - vals[0]))
    set_treino()
    print(f"  Maior |Δ vitória| nas 25 células mortais, híbrido vs. baseline: {dmax:.2f}pp")
    print("  (esperado 0,00 — treino_inimigo devolve 0 pra rank < 6 sem consumir rolagem,")
    print("   então o fluxo aleatório é bit-a-bit o mesmo e as tabelas publicadas ficam intactas)")
    return res


def main():
    print("=" * 108)
    print("DÉCIMA QUARTA RODADA — A BATERIA ESTENDIDA (solo com piso · Rei de Cem solo · PvP · híbrido do treino)")
    print(f"{N_ITER} iterações/célula · teto {MAX_ROUNDS} rodadas · semente 20260830 · mix de Alma C")
    print("Premissa: treino = 0 dos dois lados (as tabelas publicadas), exceto a bateria 4 — o knob é o assunto dela")
    print("=" * 108)
    b1 = bateria_1()
    bateria_2()
    b3 = bateria_3()
    b4 = bateria_4()
    return b1, b3, b4


if __name__ == "__main__":
    main()
