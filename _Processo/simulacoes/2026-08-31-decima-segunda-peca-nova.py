#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima segunda rodada — A PEÇA DE MUITAS AÇÕES (opção 4 da pendência da 208)
===========================================================================

Cópia de [[simulacoes/2026-08-31-decima-primeira-duracao.py]] (motor mais
atual: mix de Alma rara da décima rodada, contagem de rodadas, piso de
ataques da Horda e Padrão de rank 1 escalado da decisão 207). O motor de
dano, as fichas dos PJs, os Golpes Matadores e os moldes existentes NÃO
foram tocados — a única adição é um molde novo e a instrumentação que o
julga.

O QUE ESTA RODADA MEDE
----------------------
A décima primeira rodada (decisão 208) fechou com o achado de que **duração
e dificuldade são o mesmo botão** (o número de corpos) e deixou uma única
hipótese estrutural sem medir, a opção 4 da pendência: uma peça NOVA com
**muitas ações e pouca Vitalidade** — o inverso do Chefe. A teoria é que ela
DESACOPLA os dois botões: mantém a pressão por rodada (dificuldade) cortando
as rodadas necessárias pra limpar a mesa (duração).

O desenho veio pronto do autor:

    MOLDE "ENXAME"
      Vitalidade   7 × M   (+ o `4 × M × Grau` de estágio que todo molde leva)
      Defesa       11 + rank
      Acerto       d20 + rank + 6
      RD           nenhuma
      Ações        2 por rodada
      Dano         M d4 por ataque
      Especial     nenhuma
      Por cena     2 a 4

Lógica declarada: duas ações a `M d4` entregam ~a mesma pressão por rodada
que uma ação de Guerreiro a `M d8`, com um terço da Vitalidade do Mestre de
Gu pra remover da mesa.

AS COMPOSIÇÕES
--------------
  padrao_e   — 2 Mestres + 2 Enxames  (6 ações, a mesma contagem do Padrão
               de 3 Mestres)
  dificil_e  — 3 Mestres + 2 Enxames  (nos ranks 1-4 isto é EXATAMENTE a
               substituição pura: o Difícil vigente é 3 Mestres + 1
               Guerreiro, e aqui o Guerreiro virou 2 Enxames)
  climax_e   — Chefe + 2 Enxames      (a segunda substituição pura:
               Clímax vigente é Chefe + 1 Guerreiro)

OS TRÊS GUARDA-CORPOS
---------------------
G1 — **Curva de letalidade da decisão 78**. Intocada por construção (a peça
     é composição, não motor — como o L3 da rodada anterior). Medida mesmo
     assim, pra deixar o "por construção" verificado e não afirmado.

G2 — **Penhasco de ações da decisão 137**. Swing de vitória ao somar UMA
     peça. Medido em quatro sabores: +1 Guerreiro e +1 Enxame sobre as
     composições publicadas, e +1 Enxame sobre as composições novas. Se o
     Enxame faz o penhasco mais íngreme que o Guerreiro, é desqualificante.

G3 — **NOVO: o Enxame não pode virar "Recruta solto 2.0"**. A própria nota
     de [[⚔️ Ameaças Genéricas por Rank]] chama o Recruta solto de
     decorativo porque morre antes de agir. Instrumentado direto: quantas
     ações cada Enxame EXECUTA antes de morrer (média por peça por cena),
     que fração deles morre com ZERO ação executada, e quantas rodadas cada
     um fica de pé. Comparado com Guerreiro, Mestre de Gu e — como piso de
     referência do que "decorativo" significa em número — 6 Recrutas soltos.

AS VARIANTES DE VITALIDADE
--------------------------
  E7   — o desenho do autor: `7 × M`, dano `M d4`
  E9   — `9 × M`, dano `M d4`
  E10  — `10 × M`, dano `M d4`
  E7d6 — `7 × M` com dano `M d6` (o dado do Recruta): o d4 não existe em
         nenhum outro lugar do vault, e a escada por Caminho da decisão 78
         começa no d6 — vale saber quanto o dado de baixo custa
  E7pr — `7 × M` com o bônus de estágio PROPORCIONAL (`4 × M × Grau × 7/21`)
         em vez do `4 × M × Grau` fixo. Diagnóstico: o bônus de estágio é
         igual pra todo molde, então ele DILUI a diferença de Vitalidade
         conforme o rank sobe (no rank 1 o Enxame tem 58% da Vitalidade do
         Guerreiro; no rank 5, 79%). Esta variante mede quanto dessa erosão
         importa.

Bateria: semente 20260830, 3.000 iterações/célula, ranks 1/3/5, mix de Alma
"C" (o publicado pela decisão 206: 1d6 = 6 por Mestre).

Uso: python3 "2026-08-31-decima-segunda-peca-nova.py"
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
# Knobs herdados da rodada anterior (mantidos neutros aqui) + os do Enxame
# ---------------------------------------------------------------------------
RD_MULT = 1.0
NIVEL_DELTA = 0
DROP_PIECE = False

# --- parâmetros do molde novo, variados pela bateria ---
ENX_VIT = 7          # multiplicador de Vitalidade (`ENX_VIT × M`)
ENX_DADO = 4         # dado de dano (`M dX`)
ENX_ACOES = 2        # ações por rodada
ENX_STAGE_PROP = False  # bônus de estágio proporcional em vez de `4 × M × Grau`

# --- como os PJs escolhem alvo (só PJ → inimigo; o inimigo continua igual) ---
#   "fracao"   = o motor de todas as rodadas anteriores: bate em quem está com a
#                MENOR FRAÇÃO de Vitalidade, ou seja, termina o ferido. Com todos
#                inteiros ele bate no primeiro da lista (os Mestres), e a peça
#                nova é atacada por ÚLTIMO.
#   "absoluto" = bate em quem tem a MENOR Vitalidade ABSOLUTA restante, ou seja,
#                mata a peça frágil primeiro. É a premissa que a hipótese da
#                opção 4 assume ("o grupo mata rápido, mas dói enquanto vive") —
#                e sem medir os dois a hipótese é julgada por um artefato do motor.
TARGET_MODE = "fracao"

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


def set_enxame(vit=7, dado=4, acoes=2, stage_prop=False):
    global ENX_VIT, ENX_DADO, ENX_ACOES, ENX_STAGE_PROP
    ENX_VIT, ENX_DADO, ENX_ACOES, ENX_STAGE_PROP = vit, dado, acoes, stage_prop


def set_target_mode(mode):
    global TARGET_MODE
    TARGET_MODE = mode


# ---------------------------------------------------------------------------
# Fichas dos 4 PJs (A Mesa — Personagens dos Jogadores) — INTOCADAS
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
# Moldes de inimigo (⚔️ Ameaças Genéricas por Rank) + o Enxame
# ---------------------------------------------------------------------------
def enemy_common(name, rank, vit_mult, alma_ratio, defense, acerto_bonus, rd_mult,
                  dado, actions=1, B=None, stage_mult=4.0):
    M = M_TABLE[rank]
    grau = STAGE_B.get(rank, 3) if B is None else B
    vit = vit_mult * M + stage_mult * M * grau
    return dict(
        name=name, side="enemy", rank=rank, M=M, B=grau, dado=dado,
        vit=vit, vit_max=vit, alma=round(alma_ratio * vit), alma_max=round(alma_ratio * vit),
        essence=None, ess_max=None,
        rd=RD_MULT * rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
        acerto_bonus=acerto_bonus + rank,
        vazamento=False, skip_turns=0, fallback_raw=False,
        actions=actions, alive=True, used_special=False,
        controle_ignorado_usado=False,
        acoes_executadas=0, rodadas_de_pe=0,
    )


def make_guerreiro(rank, especial=True):
    e = enemy_common("Guerreiro", rank, 12, 0.7, 12, 6, 1, 8)
    e["especial"] = especial
    return e


def make_recruta(rank):
    """Só existe aqui como PISO DE REFERÊNCIA do guarda-corpo 3 — a nota de
    Ameaças chama o Recruta solto de decorativo, e é isso que dá escala ao
    número de 'ações executadas antes de morrer'."""
    return enemy_common("Recruta", rank, 6, 0.7, 10, 4, 0, 6)


def make_elite(rank):
    e = enemy_common("Elite", rank, 21, 0.7, 14, 8, 2, 10)
    e["especial"] = True
    return e


def make_mestre_de_gu(rank, idx=0, special="alma"):
    e = enemy_common(f"Mestre de Gu {idx}", rank, 21, 15 / 21, 13, 7, 1, 8, actions=2)
    e["special_type"] = special
    return e


def make_enxame(rank, idx=0):
    """MOLDE NOVO — muitas ações, pouca Vitalidade. Sem RD e sem Ação Especial.

    Defesa `11 + rank` e Acerto `d20 + rank + 6` interpolam Recruta (10/+4) e
    Guerreiro (12/+6): mais fácil de acertar que um Guerreiro, mas com a mesma
    chance de acertar que ele — é a peça que ameaça pelo volume, não pela ficha.
    """
    stage_mult = 4.0 * (ENX_VIT / 21.0) if ENX_STAGE_PROP else 4.0
    e = enemy_common(f"Enxame {idx}", rank, ENX_VIT, 0.7, 11, 6, 0, ENX_DADO,
                     actions=ENX_ACOES, stage_mult=stage_mult)
    e["is_enxame"] = True
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
        acoes_executadas=0, rodadas_de_pe=0,
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


def _enxames(rank, n):
    return [make_enxame(rank, i) for i in range(n)]


def make_scenario(rank, comp, mix="C"):
    """Composições PUBLICADAS (pós-207) + as três do Enxame + as do penhasco."""

    # ---------- as publicadas, o baseline desta rodada ----------
    if comp == "facil":
        return [make_horda(rank, 8)]

    if comp == "padrao":
        if rank == 1:  # decisão 207
            return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True)]
        return _mestres(rank, 3, 1, mix)

    if comp == "padrao_pesado":
        return _mestres(rank, 2, 1, mix) + [make_horda(rank, 8)]

    if comp == "dificil":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)]
        return _mestres(rank, 4, 2, mix)

    if comp == "climax":
        return [make_chefe(rank), make_guerreiro(rank, especial=True)]

    # ---------- as três com a peça nova ----------
    if comp == "padrao_e":          # 2 Mestres + 2 Enxames — 6 ações
        return _mestres(rank, 2, 1, mix) + _enxames(rank, 2)

    if comp == "dificil_e":         # 3 Mestres + 2 Enxames
        return _mestres(rank, 3, 1, mix) + _enxames(rank, 2)

    if comp == "climax_e":          # Chefe + 2 Enxames (Guerreiro → 2 Enxames)
        return [make_chefe(rank)] + _enxames(rank, 2)

    # ---------- substituição 1:1 (uma peça vira UM Enxame, não dois) ----------
    if comp == "padrao_e1":         # rank 1: 2M+1G → 2M+1E · demais: 3M → 2M+1E
        return _mestres(rank, 2, 1, mix) + _enxames(rank, 1)
    if comp == "dificil_e1":        # ranks 1-4: 3M+1G → 3M+1E · rank 5: 4M → 3M+1E
        return _mestres(rank, 3, 1, mix) + _enxames(rank, 1)
    if comp == "climax_e1":         # Chefe+1G → Chefe+1E
        return [make_chefe(rank)] + _enxames(rank, 1)

    # ---------- piso de referência do guarda-corpo 3 ----------
    if comp == "recruta_solto":     # 6 Recrutas soltos: o "decorativo" medido
        return [make_recruta(rank) for _ in range(6)]

    # ---------- guarda-corpo 2: o penhasco, quatro sabores ----------
    if comp == "padrao_mais1g":
        if rank == 1:
            return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
        return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)]
    if comp == "padrao_mais1e":
        if rank == 1:
            return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True)] + _enxames(rank, 1)
        return _mestres(rank, 3, 1, mix) + _enxames(rank, 1)
    if comp == "padrao_e_mais1e":
        return _mestres(rank, 2, 1, mix) + _enxames(rank, 3)

    if comp == "dificil_mais1g":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
        return _mestres(rank, 4, 2, mix) + [make_guerreiro(rank, especial=True)]
    if comp == "dificil_mais1e":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)] + _enxames(rank, 1)
        return _mestres(rank, 4, 2, mix) + _enxames(rank, 1)
    if comp == "dificil_e_mais1e":
        return _mestres(rank, 3, 1, mix) + _enxames(rank, 3)

    raise ValueError(comp)


# ---------------------------------------------------------------------------
# Motor de dano — IDÊNTICO ao da décima primeira rodada
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


def pick_target_enemy(enemies):
    """Escolha de alvo do PJ. Ver TARGET_MODE lá em cima."""
    living = [e for e in enemies if enemy_alive(e)]
    if not living:
        return None
    if TARGET_MODE == "absoluto":
        return min(living, key=lambda c: c["vit"])
    return min(living, key=lambda c: c["vit"] / c["vit_max"])


# ---------------------------------------------------------------------------
# Golpes Matadores — INTOCADOS
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

    target = pick_target_enemy(enemies)
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
        e["rodadas_de_pe"] += 1
        living_pcs = [p for p in pcs if pc_alive(p)]
        n_atk = horda_n_ataques(len(living_pcs))
        for _ in range(n_atk):
            living_pcs = [p for p in pcs if pc_alive(p)]
            if not living_pcs:
                return
            tgt = random.choice(living_pcs)
            dado = horda_dado(e["n_members"])
            e["acoes_executadas"] += 1
            resolve_enemy_hit(e, tgt, dado_override=dado)
        return

    if not enemy_alive(e):
        return
    e["rodadas_de_pe"] += 1
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

        # --- GUARDA-CORPO 3: a ação foi EXECUTADA (rolou o d20), acertando ou não ---
        e["acoes_executadas"] += 1
        resolve_enemy_hit(e, tgt, dado_override=dado_override, bonus_acerto=bonus,
                           alma_shot=alma_shot, aplica_lentidao=aplica_lentidao)


def update_horda_members(e):
    if not e.get("is_horda"):
        return
    frac = e["vit"] / e["vit_max"] if e["vit_max"] else 0
    e["n_members"] = max(0, round(e["n_members_max"] * max(frac, 0)))


def run_combat(pcs, enemies, has_boss=False, golpe_mode="solo"):
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


# ---------------------------------------------------------------------------
# Bateria
# ---------------------------------------------------------------------------
def _familia(nome):
    if nome.startswith("Enxame"):
        return "Enxame"
    if nome.startswith("Mestre de Gu"):
        return "Mestre de Gu"
    return nome


def simulate(rank, comp, mix="C", n_iter=N_ITER, golpe_mode="solo"):
    wins = 0
    surv_total = 0
    rounds_total = 0
    rounds_won = []
    timeouts = 0
    # guarda-corpo 3: por família de molde
    acoes = {}     # familia -> [total_acoes, n_pecas, n_pecas_zero_acao, rodadas_de_pe, n_mortas]
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
        for e in enemies:
            f = _familia(e["name"])
            slot = acoes.setdefault(f, [0, 0, 0, 0, 0])
            slot[0] += e["acoes_executadas"]
            slot[1] += 1
            if e["acoes_executadas"] == 0:
                slot[2] += 1
            slot[3] += e["rodadas_de_pe"]
            if not enemy_alive(e):
                slot[4] += 1

    g3 = {}
    for f, (tot, npec, nzero, rdp, nmortas) in acoes.items():
        g3[f] = dict(
            acoes_por_peca=tot / npec,
            frac_zero=nzero / npec,
            rodadas_de_pe=rdp / npec,
            frac_morta=nmortas / npec,
        )

    return dict(
        win=wins / n_iter,
        surv=surv_total / n_iter,
        rounds=rounds_total / n_iter,
        rounds_won=(sum(rounds_won) / len(rounds_won)) if rounds_won else float("nan"),
        timeout=timeouts / n_iter,
        g3=g3,
    )


# ---------------------------------------------------------------------------
# GUARDA-CORPO 1 — a curva de letalidade por Caminho (decisão 78)
# ---------------------------------------------------------------------------
def hits_to_kill(dado, rank, com_rd, n_iter=12000):
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
    return vit_max / dano_medio


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------
RANKS = (1, 3, 5)

VARIANTES = (
    ("E7",   "E7 — o desenho do autor: VIT 7×M · dano M d4 · 2 ações",
     dict(vit=7, dado=4)),
    ("E9",   "E9 — VIT 9×M · dano M d4 · 2 ações",
     dict(vit=9, dado=4)),
    ("E10",  "E10 — VIT 10×M · dano M d4 · 2 ações",
     dict(vit=10, dado=4)),
    ("E7d6", "E7d6 — VIT 7×M · dano M d6 (o dado do Recruta) · 2 ações",
     dict(vit=7, dado=6)),
    ("E7pr", "E7pr — VIT 7×M com bônus de estágio PROPORCIONAL · M d4 · 2 ações",
     dict(vit=7, dado=4, stage_prop=True)),
)

COMPS_E = ("padrao_e", "dificil_e", "climax_e")
COMPS_BASE = ("padrao", "padrao_pesado", "dificil", "climax")

FAIXAS = {
    "padrao": (75, 99), "padrao_e": (75, 99), "padrao_e1": (75, 99),
    "padrao_pesado": (60, 85),
    "dificil": (40, 52), "dificil_e": (40, 52), "dificil_e1": (40, 52),
    "climax": (56, 87), "climax_e": (56, 87), "climax_e1": (56, 87),
}


def dentro(comp, win_pct):
    lo, hi = FAIXAS.get(comp, (0, 100))
    return lo <= win_pct <= hi


def main():
    print("=" * 108)
    print("DÉCIMA SEGUNDA RODADA — A PEÇA DE MUITAS AÇÕES (opção 4 da pendência da decisão 208)")
    print(f"{N_ITER} iterações/célula · teto {MAX_ROUNDS} rodadas · semente 20260830 · mix de Alma C")
    print("Guarda-corpos: decisão 78 (escada de letalidade) · decisão 137 (penhasco) · G3 (não ser decorativo)")
    print("=" * 108)

    base = {}
    battery = {}

    # ---------------- BASELINE, mesma semente ----------------
    random.seed(20260830)
    set_enxame()
    print("\n### BASELINE — composições publicadas (pós-decisão 207) ###")
    print(f"  {'cena':16s} {'rank':>4s}  {'vitória':>8s} {'rodadas':>8s} {'sobrev':>7s} {'faixa':>7s}")
    for comp in COMPS_BASE:
        for rank in RANKS:
            r = simulate(rank, comp)
            base[(comp, rank)] = r
            print(f"  {comp:16s} {rank:4d}  {r['win']*100:7.1f}% {r['rounds']:8.2f} "
                  f"{r['surv']:6.2f}/4 {'ok' if dentro(comp, r['win']*100) else 'FORA':>7s}")

    # piso de referência do G3: o Recruta solto, que a nota chama de decorativo
    random.seed(20260830)
    print("\n### PISO DE REFERÊNCIA DO GUARDA-CORPO 3 — 6 Recrutas soltos (o 'decorativo' da nota) ###")
    recruta_ref = {}
    for rank in RANKS:
        r = simulate(rank, "recruta_solto")
        recruta_ref[rank] = r
        g = r["g3"]["Recruta"]
        print(f"  rank {rank}: vitória {r['win']*100:5.1f}% · {r['rounds']:.2f} rd · "
              f"ações executadas por Recruta = {g['acoes_por_peca']:.2f} · "
              f"{g['frac_zero']*100:.1f}% morrem com ZERO ação · "
              f"{g['rodadas_de_pe']:.2f} rodadas de pé")

    # ação de referência das peças existentes, nas composições publicadas
    print("\n### Referência — ações executadas pelas peças EXISTENTES nas cenas publicadas ###")
    for comp in ("padrao", "dificil", "climax"):
        for rank in RANKS:
            g = base[(comp, rank)]["g3"]
            partes = " · ".join(
                f"{f}: {v['acoes_por_peca']:.2f} ações / {v['rodadas_de_pe']:.2f} rd de pé / "
                f"{v['frac_zero']*100:.0f}% com zero"
                for f, v in sorted(g.items()))
            print(f"  {comp:14s} r{rank}: {partes}")

    # ---------------- AS VARIANTES DO ENXAME ----------------
    for key, label, kwargs in VARIANTES:
        random.seed(20260830)
        set_enxame(**{**dict(vit=7, dado=4, acoes=2, stage_prop=False), **kwargs})
        print(f"\n### {label} ###")
        print(f"  {'cena':16s} {'rank':>4s}  {'vitória':>8s} {'faixa':>6s} {'rodadas':>8s} "
              f"{'Δrd vs base':>12s} {'sobrev':>7s} {'ações/Enx':>10s} {'zero':>6s} {'rd de pé':>9s}")
        for comp in COMPS_E:
            comp_base = comp[:-2]
            for rank in RANKS:
                r = simulate(rank, comp)
                battery[(key, comp, rank)] = r
                g = r["g3"].get("Enxame", dict(acoes_por_peca=float('nan'), frac_zero=float('nan'),
                                               rodadas_de_pe=float('nan')))
                d_rd = r["rounds"] - base[(comp_base, rank)]["rounds"]
                print(f"  {comp:16s} {rank:4d}  {r['win']*100:7.1f}% "
                      f"{'ok' if dentro(comp, r['win']*100) else 'FORA':>6s} {r['rounds']:8.2f} "
                      f"{d_rd:+11.2f} {r['surv']:6.2f}/4 {g['acoes_por_peca']:10.2f} "
                      f"{g['frac_zero']*100:5.1f}% {g['rodadas_de_pe']:8.2f}")

    # ---------------- RESUMOS ----------------
    print("\n" + "=" * 108)
    print("RESUMO — VITÓRIA DO GRUPO (faixas publicadas: Padrão 75-99 · Difícil 40-52 · Clímax 56-87)")
    print("=" * 108)
    hdr = f"{'cena / rank':18s}{'BASE':>10s}" + "".join(f"{k:>10s}" for k, _, _ in VARIANTES)
    print(hdr)
    for comp in COMPS_E:
        comp_base = comp[:-2]
        for rank in RANKS:
            row = f"{comp + ' r' + str(rank):18s}{base[(comp_base, rank)]['win']*100:9.1f}%"
            for k, _, _ in VARIANTES:
                row += f"{battery[(k, comp, rank)]['win']*100:9.1f}%"
            print(row)

    print("\n" + "=" * 108)
    print("RESUMO — RODADAS MÉDIAS (alvo declarado do autor: 4-6; ele já aceitou 6-8 como o real)")
    print("=" * 108)
    print(hdr)
    medias = {k: [] for k, _, _ in VARIANTES}
    media_base = []
    for comp in COMPS_E:
        comp_base = comp[:-2]
        for rank in RANKS:
            row = f"{comp + ' r' + str(rank):18s}{base[(comp_base, rank)]['rounds']:10.2f}"
            media_base.append(base[(comp_base, rank)]["rounds"])
            for k, _, _ in VARIANTES:
                v = battery[(k, comp, rank)]["rounds"]
                medias[k].append(v)
                row += f"{v:10.2f}"
            print(row)
    row = f"{'MÉDIA das 9':18s}{sum(media_base)/len(media_base):10.2f}"
    for k, _, _ in VARIANTES:
        row += f"{sum(medias[k])/len(medias[k]):10.2f}"
    print(row)
    row = f"{'encurtamento':18s}{'—':>10s}"
    mb = sum(media_base) / len(media_base)
    for k, _, _ in VARIANTES:
        mv = sum(medias[k]) / len(medias[k])
        row += f"{(mv-mb)/mb*100:+9.1f}%"
    print(row)
    row = f"{'células em 4-6':18s}{sum(1 for v in media_base if 4 <= v <= 6):9d}/9"
    for k, _, _ in VARIANTES:
        row += f"{sum(1 for v in medias[k] if 4 <= v <= 6):9d}/9"
    print(row)

    print("\n" + "=" * 108)
    print("GUARDA-CORPO 3 — O ENXAME É DECORATIVO? (ações executadas por peça antes de morrer)")
    print("Piso do 'decorativo': o Recruta solto, medido acima. Teto útil: o Guerreiro das cenas publicadas.")
    print("=" * 108)
    print(f"{'variante':10s}{'cena / rank':18s}{'ações/Enx':>11s}{'% com zero':>12s}{'rd de pé':>10s}{'% morta':>9s}")
    for k, _, _ in VARIANTES:
        for comp in COMPS_E:
            for rank in RANKS:
                g = battery[(k, comp, rank)]["g3"].get("Enxame")
                if not g:
                    continue
                print(f"{k:10s}{comp + ' r' + str(rank):18s}{g['acoes_por_peca']:11.2f}"
                      f"{g['frac_zero']*100:11.1f}%{g['rodadas_de_pe']:10.2f}{g['frac_morta']*100:8.1f}%")

    # ---------------- GUARDA-CORPO 2 — o penhasco ----------------
    print("\n" + "=" * 108)
    print("GUARDA-CORPO 2 — PENHASCO DE AÇÕES (decisão 137): swing ao somar UMA peça")
    print("swing = vitória(base) − vitória(base + peça), em pontos percentuais. Referência: +1 Guerreiro.")
    print("=" * 108)
    random.seed(20260830)
    set_enxame()  # o penhasco é medido com o desenho do autor (E7)
    print(f"{'composição':22s}{'rank':>5s}{'base':>9s}{'+1 Guerreiro':>14s}{'swing G':>9s}"
          f"{'+1 Enxame':>11s}{'swing E':>9s}")
    cliff = {}
    for comp, cg, ce in (("padrao", "padrao_mais1g", "padrao_mais1e"),
                          ("dificil", "dificil_mais1g", "dificil_mais1e")):
        for rank in RANKS:
            b = simulate(rank, comp)
            g = simulate(rank, cg)
            e = simulate(rank, ce)
            cliff[(comp, rank)] = (b["win"], g["win"], e["win"])
            print(f"{comp:22s}{rank:5d}{b['win']*100:8.1f}%{g['win']*100:13.1f}%"
                  f"{(b['win']-g['win'])*100:9.1f}{e['win']*100:10.1f}%"
                  f"{(b['win']-e['win'])*100:9.1f}")

    print("\n  --- e o degrau DENTRO das composições novas (+1 Enxame sobre a cena com Enxame) ---")
    print(f"{'composição':22s}{'rank':>5s}{'base':>9s}{'+1 Enxame':>11s}{'swing':>9s}")
    for comp, cplus in (("padrao_e", "padrao_e_mais1e"), ("dificil_e", "dificil_e_mais1e")):
        for rank in RANKS:
            b = simulate(rank, comp)
            p = simulate(rank, cplus)
            cliff[(comp, rank)] = (b["win"], p["win"])
            print(f"{comp:22s}{rank:5d}{b['win']*100:8.1f}%{p['win']*100:10.1f}%"
                  f"{(b['win']-p['win'])*100:9.1f}")

    # ---------------- GUARDA-CORPO 1 ----------------
    print("\n" + "=" * 108)
    print("GUARDA-CORPO 1 — CURVA DE LETALIDADE POR CAMINHO (decisão 78)")
    print("Intocada POR CONSTRUÇÃO — o Enxame é composição, não motor. Verificado, não afirmado:")
    print("=" * 108)
    random.seed(20260830)
    for rank in RANKS:
        for com_rd in (False, True):
            tag = f"rank {rank} " + ("com RD 1×M" if com_rd else "sem RD (def. da decisão 78)")
            rz = [hits_to_kill(d, rank, com_rd) for d in (6, 8, 10, 12)]
            print(f"  {tag:36s} d6 {rz[0]:5.2f} · d8 {rz[1]:5.2f} · d10 {rz[2]:5.2f} · "
                  f"d12 {rz[3]:5.2f}   (razão d6/d12 = {rz[0]/rz[3]:.2f})")
    print("  publicada (decisão 78), rank 1 sem RD: d6 5,14 · d8 4,00 · d10 3,27 · d12 2,77 (razão 1,86)")

    # =======================================================================
    # FASE 2 — as duas premissas que a Fase 1 deixou por medir
    # =======================================================================
    print("\n\n" + "=" * 108)
    print("FASE 2 — AS DUAS PREMISSAS QUE A FASE 1 NÃO TESTOU")
    print("=" * 108)
    print("""
(a) ESCOLHA DE ALVO. O motor de todas as rodadas anteriores faz o PJ bater em
    quem tem a menor FRAÇÃO de Vitalidade — ou seja, termina o ferido. Com a
    mesa inteira inteira no começo da cena, o desempate é a ordem da lista, e
    a peça frágil acaba sendo atacada por ÚLTIMO. A hipótese da opção 4 diz
    "o grupo mata rápido, mas dói enquanto vive" — e essa premissa só existe
    se o grupo FOCAR a peça frágil. Modo "absoluto" = bate em quem tem menos
    Vitalidade restante em valor absoluto (mata o Enxame primeiro).

(b) DOSAGEM. A Fase 1 trocou 1 Guerreiro por DOIS Enxames. Se dois é demais,
    a substituição 1:1 (uma peça vira UM Enxame) é o teste honesto de
    "ameaça equivalente".
""")

    fase2 = {}
    COMPS_F2 = ("padrao", "padrao_e1", "padrao_e",
                "dificil", "dificil_e1", "dificil_e",
                "climax", "climax_e1", "climax_e")

    for modo in ("fracao", "absoluto"):
        random.seed(20260830)
        set_enxame()          # E7 — o desenho do autor
        set_target_mode(modo)
        rotulo = ("(a) alvo por FRAÇÃO — o motor histórico"
                  if modo == "fracao" else
                  "(b) alvo ABSOLUTO — o grupo foca a peça frágil primeiro")
        print(f"\n### {rotulo} ###")
        print(f"  {'cena':14s}{'rank':>5s}{'vitória':>9s}{'faixa':>7s}{'rodadas':>9s}"
              f"{'sobrev':>8s}{'ações/Enx':>11s}{'zero':>7s}{'rd de pé':>10s}{'% morta':>9s}")
        for comp in COMPS_F2:
            for rank in RANKS:
                r = simulate(rank, comp)
                fase2[(modo, comp, rank)] = r
                g = r["g3"].get("Enxame")
                ge = (f"{g['acoes_por_peca']:11.2f}{g['frac_zero']*100:6.1f}%"
                      f"{g['rodadas_de_pe']:10.2f}{g['frac_morta']*100:8.1f}%") if g else \
                     f"{'—':>11s}{'—':>7s}{'—':>10s}{'—':>9s}"
                print(f"  {comp:14s}{rank:5d}{r['win']*100:8.1f}%"
                      f"{'ok' if dentro(comp, r['win']*100) else 'FORA':>7s}"
                      f"{r['rounds']:9.2f}{r['surv']:7.2f}/4{ge}")
    set_target_mode("fracao")

    print("\n" + "=" * 108)
    print("FASE 2 — COMPARATIVO DIRETO (E7, os dois modos de escolha de alvo)")
    print("=" * 108)
    print(f"{'cena / rank':18s}{'vit fração':>12s}{'rd fração':>11s}{'vit absoluto':>14s}{'rd absoluto':>13s}")
    for comp in COMPS_F2:
        for rank in RANKS:
            a = fase2[("fracao", comp, rank)]
            b_ = fase2[("absoluto", comp, rank)]
            print(f"{comp + ' r' + str(rank):18s}{a['win']*100:11.1f}%{a['rounds']:11.2f}"
                  f"{b_['win']*100:13.1f}%{b_['rounds']:13.2f}")

    # =======================================================================
    # FASE 3 — a varredura de Vitalidade ONDE ELA MORDE
    # =======================================================================
    print("\n\n" + "=" * 108)
    print("FASE 3 — VARREDURA DE VITALIDADE SOB ALVO ABSOLUTO")
    print("A Fase 1 varreu 7/9/10 no modo FRAÇÃO, onde a Vitalidade do Enxame quase não")
    print("importa (ele é atacado por último de qualquer jeito). É sob alvo ABSOLUTO que a")
    print("Vitalidade decide se a peça age ou é decorativa — é aqui que a varredura significa algo.")
    print("Piso do decorativo (Recruta solto): 1,28 · 2,20 · 2,97 ações nos ranks 1/3/5.")
    print("=" * 108)
    fase3 = {}
    print(f"  {'VIT':>6s}{'cena':>12s}{'rank':>5s}{'vitória':>9s}{'faixa':>7s}{'rodadas':>9s}"
          f"{'ações/Enx':>11s}{'zero':>7s}")
    for vit in (7, 9, 10, 14):
        random.seed(20260830)
        set_enxame(vit=vit)
        set_target_mode("absoluto")
        for comp in ("padrao_e", "dificil_e"):
            for rank in RANKS:
                r = simulate(rank, comp)
                fase3[(vit, comp, rank)] = r
                g = r["g3"]["Enxame"]
                print(f"  {str(vit) + '×M':>6s}{comp:>12s}{rank:5d}{r['win']*100:8.1f}%"
                      f"{'ok' if dentro(comp, r['win']*100) else 'FORA':>7s}{r['rounds']:9.2f}"
                      f"{g['acoes_por_peca']:11.2f}{g['frac_zero']*100:6.1f}%")
    set_target_mode("fracao")
    set_enxame()

    return base, battery, cliff, fase2, fase3


if __name__ == "__main__":
    main()
