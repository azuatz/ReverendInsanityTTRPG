#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima terceira rodada — VALIDAÇÃO FINAL CONJUNTA (decisões 146-210)
===================================================================

Cópia de [[simulacoes/2026-08-31-decima-primeira-duracao.py]] (motor mais
atual publicado: mix de Alma rara da decisão 206, piso de ataques da Horda e
Padrão escalado da decisão 207, instrumentação de rodadas), com as mudanças
abaixo. Mesmo papel que a sexta rodada teve para as decisões 103-133: provar
que o lote inteiro de hoje continua de pé como UMA máquina, e não só peça
por peça.

O QUE MUDOU NO MOTOR
--------------------
1. **COLAPSO ESPIRITUAL (decisão 205) — a correção que abriu esta rodada.**
   O motor modelava Alma zerada como MORTE (`pc_alive = vit > 0 and alma > 0`,
   com o resultado contado como baixa). A regra desde a decisão 205 é outra:
   Alma 0 = **inconsciente + Teste de Morte espiritual**, a primeira queda
   **nunca mata**, três degraus = coma espiritual (ainda não é morte), e a
   morte real só vem numa **segunda** queda de Alma com a sequela aberta —
   coisa que, por definição, não cabe dentro de uma cena só.

   Como foi modelado, explicitamente:
     · `pc_ativo(pc)` (`vit > 0 and alma > 0`) continua sendo quem **age e é
       alvo** — o caído por Alma sai da cena, exatamente como antes. Nenhuma
       rolagem nova entra no loop (o Teste de Morte espiritual não muda o
       combate: perder ou passar, o personagem segue fora da cena), então o
       fluxo de números aleatórios é bit-a-bit o mesmo das rodadas
       anteriores — a comparação com o publicado é limpa.
     · O que muda é a **contabilidade**: `baixa_real(pc)` passa a ser só
       `vit <= 0` (o Teste de Morte FÍSICO segue como sempre esteve); o caído
       por Alma conta em `caidos_alma`, **não** em baixas.
     · Consequência declarada: a condição de vitória do grupo (limpar os
       inimigos) **não pode mudar** — o caído por Alma não age nos dois
       modelos. A rodada mede isso em vez de assumir: a bateria 1 roda com o
       flag `COLAPSO_ESPIRITUAL` ligado e desligado, mesma semente, e o efeito
       aparece onde ele existe de verdade — **sobreviventes e mortalidade**,
       não vitória.
     · Interage com a decisão 206 (Alma rara = 1d6 = 6 por Mestre de Gu),
       então o efeito deve ser pequeno e não-nulo. Medido, não suposto.

2. **Suporte imortal portado da oitava rodada**: `dom_B` (nível de domínio de
   Marca) e `pool_mult` (o pool 2×M do Grande Mestre Supremo) em PJ e em
   inimigo, para a régua ΔB que a decisão 205 tornou regra oficial.

3. **Instrumentação de desgaste** portada de
   [[simulacoes/2026-08-31-desgaste-hordas-calibracao.py]]: % de Vitalidade
   perdida e % de essência gasta pelo grupo, que é o que calibra a Varredura
   de [[🐺 Reis Fera e a Maré]].

AS QUATRO BATERIAS
------------------
B1 — **Bateria mortal completa**: ranks 1-5 × facil/padrao/padrao_pesado/
     dificil/climax, contra CADA número publicado em
     [[⚔️ Ameaças Genéricas por Rank]] (tabela de composição e tabela de
     ações do Chefe). Rodada duas vezes (Colapso ligado/desligado).

B2 — **Spot-check imortal (ranks 6-9)**: a régua ΔB da decisão 205
     (`ΔB 0 ≈ passeio · +1 ≈ 20% · +3 ≈ 6%`) sobreviveu às decisões 206-207?
     Duas leituras: as 5 composições a ΔB 0 (a alegação "toda cena vira
     passeio") e a âncora de Chefe da oitava rodada a ΔB 0/+1/+3.

B3 — **Rei de Cem Feras** ([[🐺 Reis Fera e a Maré]], decisão 200): o
     "~99% de vitória a ~55-60% da Vitalidade" foi medido ANTES do piso da
     Horda (207) e de Alma rara (206). Remedido aqui, junto do Rei de Mil e
     da regra de ondas (hordas simultâneas).

B4 — **Tabela de custo da Varredura**: a atrição de uma onda de Horda 8
     limpa (% de Vitalidade, % de essência, rodadas), que é a média de que a
     tabela de custo publicada deriva.

Bateria: semente 20260830, 3.000 iterações/célula, mix de Alma "C"
(o publicado pela decisão 206).

Uso: python3 "2026-08-31-decima-terceira-validacao-final.py"
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


def treino_pj(rank):
    if TREINO_FLAT is not None:
        return TREINO_FLAT
    return TREINO[rank] if TREINO_PJ else 0


def treino_inimigo(rank):
    return TREINO[rank] if TREINO_INIMIGO else 0


def set_treino(pj=False, inimigo=False, flat=None):
    global TREINO_PJ, TREINO_INIMIGO, TREINO_FLAT
    TREINO_PJ, TREINO_INIMIGO, TREINO_FLAT = pj, inimigo, flat

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
# Os números PUBLICADOS hoje — a rodada é uma comparação, então eles ficam aqui
# ---------------------------------------------------------------------------
# [[⚔️ Ameaças Genéricas por Rank]], tabela "Como montar uma cena de combate"
PUB_COMPOSICAO = {
    "facil":         {1: 100, 2: 100, 3: 100, 5: 100},
    "padrao":        {1: 92,  2: 77,  3: 85,  5: 99},
    "padrao_pesado": {1: 63,  2: 57,  3: 50,  5: 76},
    "dificil":       {1: 30,  2: 35,  3: 46,  5: 38},
    "climax":        {1: 3,   2: 54,  3: 86,  5: 90},
}
# mesma nota, tabela "Quantas ações o Chefe tem" (Chefe + 1 Guerreiro de apoio)
PUB_CHEFE = {1: 57, 2: 62, 3: 79, 4: 75, 5: 75}
# mesma nota, linha "Quanto tempo a cena dura, medido"
PUB_DURACAO = {
    "facil": (2.5, 4.6), "padrao": (6.0, 7.7), "padrao_pesado": (7.6, 10.4),
    "dificil": (8.3, 8.9), "climax": (6.8, 10.7),
}
TOL = 3.0  # pontos percentuais: o limiar de "moveu" pedido pela rodada

RANKS_MORTAIS = (1, 2, 3, 4, 5)
COMPS = ("facil", "padrao", "padrao_pesado", "dificil", "climax")


def _flag(medido, publicado):
    if publicado is None:
        return "—", ""
    d = medido - publicado
    marca = "  <<< MOVEU" if abs(d) > TOL else ""
    return f"{d:+5.1f}", marca


# ---------------------------------------------------------------------------
# BATERIA 1 — bateria mortal completa contra tudo que está publicado
# ---------------------------------------------------------------------------
def bateria_1():
    global COLAPSO_ESPIRITUAL
    print("=" * 108)
    print("BATERIA 1 — BATERIA MORTAL COMPLETA (ranks 1-5 × 5 composições)")
    print("Comparada célula a célula com [[⚔️ Ameaças Genéricas por Rank]]. "
          f"Limiar de alerta: {TOL:.0f}pp")
    print("=" * 108)

    resultados = {}
    for modo, flag in (("COLAPSO LIGADO (decisão 205)", True),
                       ("colapso desligado (modelo antigo do motor)", False)):
        COLAPSO_ESPIRITUAL = flag
        random.seed(20260830)
        print(f"\n### {modo} ###")
        print(f"  {'cena':16s} {'rank':>4s} {'vitória':>8s} {'publ.':>6s} {'Δpp':>6s}  "
              f"{'de pé':>6s} {'sobrev':>7s} {'baixas':>7s} {'p/Alma':>7s} "
              f"{'rodadas':>8s} {'timeout':>8s}")
        for comp in COMPS:
            for rank in RANKS_MORTAIS:
                r = simulate(rank, comp)
                resultados[(flag, comp, rank)] = r
                pub = PUB_COMPOSICAO[comp].get(rank)
                d, marca = _flag(r["win"] * 100, pub)
                pubtxt = f"{pub:5d}%" if pub is not None else "    —"
                print(f"  {comp:16s} {rank:4d} {r['win']*100:7.1f}% {pubtxt} {d:>6s}  "
                      f"{r['surv']:5.2f}  {r['sobreviventes']:6.2f}  {r['baixas']:6.2f}  "
                      f"{r['caidos_alma']:6.2f}  {r['rounds']:7.2f} {r['timeout']*100:7.1f}%"
                      f"{marca}")
    COLAPSO_ESPIRITUAL = True

    # --- o efeito medido do Colapso Espiritual ---
    print("\n" + "-" * 108)
    print("O EFEITO DO COLAPSO ESPIRITUAL — mesma semente, os dois modelos")
    print("-" * 108)
    print(f"  {'cena':16s} {'rank':>4s} {'Δ vitória':>10s} {'Δ sobrev':>9s} "
          f"{'caídos p/Alma':>14s} {'cenas c/ colapso':>17s} {'derrotas s/ baixa':>18s}")
    dv_max = 0.0
    ds_tot = []
    for comp in COMPS:
        for rank in RANKS_MORTAIS:
            a = resultados[(True, comp, rank)]
            b = resultados[(False, comp, rank)]
            dv = (a["win"] - b["win"]) * 100
            ds = a["sobreviventes"] - b["sobreviventes"]
            dv_max = max(dv_max, abs(dv))
            ds_tot.append(ds)
            dsb = a["derrotas_sem_baixa"]
            dsbtxt = "n/a" if dsb != dsb else f"{dsb*100:16.1f}%"
            print(f"  {comp:16s} {rank:4d} {dv:9.2f}pp {ds:+9.3f} "
                  f"{a['caidos_alma']:13.3f} {a['cenas_com_colapso']*100:16.1f}% {dsbtxt}")
    print(f"\n  Maior |Δ vitória| em 25 células: {dv_max:.2f}pp  "
          f"(esperado 0,00 — o caído por Alma já saía da cena nos dois modelos)")
    print(f"  Δ sobreviventes médio: {sum(ds_tot)/len(ds_tot):+.3f} de 4 "
          f"(personagens que o motor antigo matava e a decisão 205 devolve vivos)")

    # --- duração publicada ---
    print("\n" + "-" * 108)
    print("DURAÇÃO — faixa medida vs. faixa publicada na nota")
    print("-" * 108)
    for comp in COMPS:
        vals = [resultados[(True, comp, r)]["rounds"] for r in RANKS_MORTAIS]
        lo, hi = PUB_DURACAO[comp]
        print(f"  {comp:16s} medido {min(vals):5.2f}-{max(vals):5.2f}   "
              f"publicado {lo:.1f}-{hi:.1f}")

    # --- tabela de ações do Chefe (mesma cena que "climax") ---
    print("\n" + "-" * 108)
    print("TABELA DE AÇÕES DO CHEFE — 'Chefe + 1 Guerreiro de apoio', a MESMA cena de Clímax")
    print("-" * 108)
    print(f"  {'rank':>4s} {'ações':>6s} {'medido':>8s} {'publ. (tab. Chefe)':>19s} {'Δpp':>7s} "
          f"{'de pé':>6s} {'rodadas':>8s}")
    for rank in RANKS_MORTAIS:
        r = resultados[(True, "climax", rank)]
        pub = PUB_CHEFE[rank]
        d, marca = _flag(r["win"] * 100, pub)
        print(f"  {rank:4d} {CHEFE_ACOES[rank]:6d} {r['win']*100:7.1f}% {pub:18d}% {d:>7s} "
              f"{r['surv']:5.2f} {r['rounds']:7.2f}{marca}")

    return resultados


# ---------------------------------------------------------------------------
# BATERIA 2 — spot-check imortal: a régua ΔB da decisão 205
# ---------------------------------------------------------------------------
def bateria_2():
    print("\n" + "=" * 108)
    print("BATERIA 2 — RANKS IMORTAIS (6-9): a régua ΔB da decisão 205 sobreviveu às 206-207?")
    print("Publicado: ΔB 0 ≈ passeio (77-100%) · ΔB +1 ≈ 20% · ΔB +3 ≈ 6%")
    print("=" * 108)

    print("\n### (a) ΔB 0 — as 5 composições mortais no rank imortal (a alegação 'passeio') ###")
    print("Estas SIM passam pelas decisões 206 (Mestres) e 207 (Horda).")
    print(f"  {'rank':>4s} {'domínio':16s} {'cena':16s} {'vitória':>8s} {'de pé':>6s} "
          f"{'sobrev':>7s} {'rodadas':>8s} {'timeout':>8s}")
    delta0 = []
    for rank in (6, 7, 8, 9):
        dom = DOMINIO[(rank, "recem")]
        for comp in COMPS:
            random.seed(20260830)
            r = simulate(rank, comp, imortal=True, dom_B=dom["B"],
                         pool_mult=dom["pool_mult"], enemy_B=dom["B"],
                         enemy_pool_mult=dom["pool_mult"])
            delta0.append(r["win"] * 100)
            print(f"  {rank:4d} {dom['nome']:16s} {comp:16s} {r['win']*100:7.1f}% "
                  f"{r['surv']:5.2f}  {r['sobreviventes']:6.2f}  {r['rounds']:7.2f} "
                  f"{r['timeout']*100:7.1f}%")
    print(f"\n  Faixa medida a ΔB 0: {min(delta0):.1f}% – {max(delta0):.1f}%   "
          f"(publicado: 77-100%, 'passeio')")

    print("\n### (b) A âncora de Chefe da oitava rodada, ΔB 0 / +1 / +3, nos quatro ranks ###")
    print("Chefe (Gu Imortal d12) + escolta de Guerreiro no domínio do grupo; golpe_mode='none'.")
    print("Sem Mestre de Gu e sem Horda: por construção, as decisões 206-207 NÃO tocam esta cena.")
    print(f"  {'rank':>4s} {'domínio do grupo':18s} {'ΔB':>4s} {'vitória':>8s} {'de pé':>6s} "
          f"{'sobrev':>7s} {'rodadas':>8s}")
    escada = {0: [], 1: [], 3: []}
    for rank in (6, 7, 8, 9):
        dom = DOMINIO[(rank, "recem")]
        for delta in (0, 1, 3):
            random.seed(20260830)
            r = simulate(rank, "climax", imortal=True, dom_B=dom["B"],
                         pool_mult=dom["pool_mult"], golpe_mode="none", has_boss=True,
                         scenario_factory=lambda rk, d=delta, dm=dom: cena_delta_b(rk, dm, d))
            escada[delta].append(r["win"] * 100)
            print(f"  {rank:4d} {dom['nome']:18s} {delta:+4d} {r['win']*100:7.1f}% "
                  f"{r['surv']:5.2f}  {r['sobreviventes']:6.2f}  {r['rounds']:7.2f}")
    print("\n  ESCADA MEDIDA (média dos ranks 6-9)   vs.   PUBLICADA")
    for delta, pub in ((0, "77-100% (passeio)"), (1, "~20%"), (3, "~6%")):
        v = escada[delta]
        print(f"    ΔB {delta:+d}: {sum(v)/len(v):5.1f}%  (faixa {min(v):.1f}-{max(v):.1f}%)"
              f"   vs. publicado {pub}")


# ---------------------------------------------------------------------------
# BATERIA 3 — Reis Fera e a regra de ondas (decisão 200)
# ---------------------------------------------------------------------------
def bateria_3():
    print("\n" + "=" * 108)
    print("BATERIA 3 — [[🐺 Reis Fera e a Maré]]: os números publicados foram medidos ANTES")
    print("das decisões 206 (Alma rara) e 207 (piso de ataques da Horda). Remedidos aqui.")
    print("=" * 108)

    cenas = (
        ("Rei de Cem (Elite + Horda 8)", rei_de_cem, False),
        ("Rei de Mil (Chefe + H12 + H8)", rei_de_mil, True),
        ("1× Horda 8 (uma onda)", onda_unica, False),
        ("2× Horda 8 (simultâneas)", duas_hordas, False),
        ("3× Horda 8 (simultâneas)", tres_hordas, False),
    )
    out = {}
    for nome, factory, has_boss in cenas:
        print(f"\n### {nome} ###")
        print(f"  {'rank':>4s} {'vitória':>8s} {'vit perd.':>10s} {'vit(vit.)':>10s} "
              f"{'ess gasta':>10s} {'rodadas':>8s} {'de pé':>6s} {'sobrev':>7s} {'timeout':>8s}")
        for rank in RANKS_MORTAIS:
            random.seed(20260830)
            r = simulate(rank, "reis", scenario_factory=factory, has_boss=has_boss)
            out[(nome, rank)] = r
            print(f"  {rank:4d} {r['win']*100:7.1f}% {r['vit_lost']*100:9.1f}% "
                  f"{r['vit_lost_won']*100:9.1f}% {r['ess_spent']*100:9.1f}% "
                  f"{r['rounds']:7.2f} {r['surv']:5.2f}  {r['sobreviventes']:6.2f} "
                  f"{r['timeout']*100:7.1f}%")

    print("\n" + "-" * 108)
    print("CONTRA O PUBLICADO em [[🐺 Reis Fera e a Maré]]")
    print("-" * 108)
    rc = [out[("Rei de Cem (Elite + Horda 8)", r)] for r in RANKS_MORTAIS]
    print(f"  Rei de Cem — publicado: '~99% de vitória, ~55-60% da Vitalidade, ~7 rodadas'")
    print(f"    medido: vitória {min(x['win'] for x in rc)*100:.1f}-{max(x['win'] for x in rc)*100:.1f}%"
          f" · Vitalidade perdida {min(x['vit_lost'] for x in rc)*100:.1f}-"
          f"{max(x['vit_lost'] for x in rc)*100:.1f}%"
          f" · rodadas {min(x['rounds'] for x in rc):.1f}-{max(x['rounds'] for x in rc):.1f}")
    rm = [out[("Rei de Mil (Chefe + H12 + H8)", r)] for r in RANKS_MORTAIS]
    print(f"  Rei de Mil — publicado: '0% — um grupo sozinho NUNCA vence'")
    print(f"    medido: vitória {min(x['win'] for x in rm)*100:.1f}-{max(x['win'] for x in rm)*100:.1f}%")
    print(f"  Regra de ondas — publicado: 2× Horda 8 = 83/56/36% nos ranks 2/3/4 · 3× = 0%")
    for rank in (2, 3, 4):
        print(f"    rank {rank}: 2× medido {out[('2× Horda 8 (simultâneas)', rank)]['win']*100:5.1f}%"
              f"   3× medido {out[('3× Horda 8 (simultâneas)', rank)]['win']*100:5.1f}%")
    return out


# ---------------------------------------------------------------------------
# BATERIA 4 — a calibração da tabela de custo da Varredura
# ---------------------------------------------------------------------------
def bateria_4(out_b3):
    print("\n" + "=" * 108)
    print("BATERIA 4 — CUSTO DA VARREDURA: a atrição de UMA onda de Horda 8 limpa")
    print("Publicado: '~25-30% da Vitalidade por onda limpa e ~4 rodadas' · "
          "'faixa medida 23-32% conforme o rank'")
    print("Tabela publicada: 4 passaram 15%/10% ess · 2-3 passaram 25%/15% · 1 passou 40%/20%")
    print("=" * 108)
    print(f"  {'rank':>4s} {'vitória':>8s} {'% Vitalidade perdida':>21s} "
          f"{'% essência gasta':>17s} {'rodadas':>8s}")
    vits, esss, rnds = [], [], []
    for rank in RANKS_MORTAIS:
        r = out_b3[("1× Horda 8 (uma onda)", rank)]
        # a onda limpa: só as iterações em que a onda caiu
        vits.append(r["vit_lost_won"] * 100)
        esss.append(r["ess_spent_won"] * 100)
        rnds.append(r["rounds_won"])
        print(f"  {rank:4d} {r['win']*100:7.1f}% {r['vit_lost_won']*100:20.1f}% "
              f"{r['ess_spent_won']*100:16.1f}% {r['rounds_won']:7.2f}")
    print(f"\n  Onda limpa, faixa medida: Vitalidade {min(vits):.1f}-{max(vits):.1f}% "
          f"(média {sum(vits)/len(vits):.1f}%) · essência {min(esss):.1f}-{max(esss):.1f}% "
          f"(média {sum(esss)/len(esss):.1f}%) · {min(rnds):.1f}-{max(rnds):.1f} rodadas")
    print(f"  A linha '2-3 passaram' da tabela usa a MÉDIA; as outras escalam dela "
          f"(0,6× para '4 passaram', 1,6× para '1 passou').")
    media_v = sum(vits) / len(vits)
    media_e = sum(esss) / len(esss)
    print(f"\n  Tabela recalibrada pela mesma regra de escala:")
    print(f"    4 passaram : {media_v*0.6:5.1f}% Vitalidade · {media_e*0.667:4.1f}% essência "
          f"(publicado 15% / 10%)")
    print(f"    2-3 passaram: {media_v:5.1f}% Vitalidade · {media_e:4.1f}% essência "
          f"(publicado 25% / 15%)")
    print(f"    1 passou   : {media_v*1.6:5.1f}% Vitalidade · {media_e*1.333:4.1f}% essência "
          f"(publicado 40% / 20%)")


# ---------------------------------------------------------------------------
# GUARDA-CORPO — a curva de letalidade da decisão 78 continua de pé?
# ---------------------------------------------------------------------------
def guarda_corpo_78():
    print("\n" + "=" * 108)
    print("GUARDA-CORPO — CURVA DE LETALIDADE POR CAMINHO (decisão 78)")
    print("Publicado (sem RD): d6 5,14 · d8 4,00 · d10 3,27 · d12 2,77 — razão d6/d12 = 1,86")
    print("=" * 108)
    random.seed(20260830)
    for rank in (1, 3, 5):
        for com_rd in (False, True):
            tag = f"rank {rank} " + ("com RD 1×M (leitura de mesa)" if com_rd else "sem RD (definição da 78)")
            razoes = [hits_to_kill(d, rank, com_rd, n_iter=12000)[0] for d in (6, 8, 10, 12)]
            print(f"  {tag:38s} d6 {razoes[0]:5.2f} · d8 {razoes[1]:5.2f} · "
                  f"d10 {razoes[2]:5.2f} · d12 {razoes[3]:5.2f}   "
                  f"(razão d6/d12 = {razoes[0]/razoes[3]:.2f})")


# ---------------------------------------------------------------------------
# BATERIA 5 — a decisão 211 (bônus de treino escalado), medida pela 1ª vez
# ---------------------------------------------------------------------------
def bateria_5():
    print("\n" + "=" * 108)
    print("BATERIA 5 — DECISÃO 211: o bônus de treino escalado (+2 a +6), medido pela PRIMEIRA vez")
    print("A decisão foi aplicada às regras ANTES de simulação, com a obrigação explícita de que")
    print("'a próxima rodada deve medir'. O motor de todas as rodadas anteriores usa treino = 0,")
    print("então a coluna 'sem treino' abaixo É a bateria 1 (e é o que a nota publica hoje).")
    print("=" * 108)

    modos = (
        ("sem treino (motor histórico)", dict(pj=False, inimigo=False)),
        ("treino +2 fixo (regra pré-211)", dict(flat=2)),
        ("só PJ (a 211 como publicada)", dict(pj=True, inimigo=False)),
        ("simétrico (PJ + inimigo)", dict(pj=True, inimigo=True)),
    )
    res = {}
    for label, kw in modos:
        set_treino(**kw)
        random.seed(20260830)
        print(f"\n### {label} ###")
        print(f"  {'cena':16s} {'rank':>4s} {'vitória':>8s} {'de pé':>6s} {'rodadas':>8s}")
        for comp in COMPS:
            for rank in RANKS_MORTAIS:
                r = simulate(rank, comp)
                res[(label, comp, rank)] = r
                print(f"  {comp:16s} {rank:4d} {r['win']*100:7.1f}% {r['surv']:5.2f} "
                      f"{r['rounds']:7.2f}")
    set_treino()

    print("\n" + "-" * 108)
    print("O SWING — quanto a decisão 211 move cada célula publicada")
    print("-" * 108)
    print(f"  {'cena':16s} {'rank':>4s} {'motor':>8s} {'+2 fixo':>9s} {'Δpp':>6s} "
          f"{'só PJ':>8s} {'Δpp':>6s} {'Δ vs +2':>8s} {'simétr.':>9s} {'Δpp':>7s}")
    sw_flat, sw_pj, sw_sim, sw_211 = [], [], [], []
    for comp in COMPS:
        for rank in RANKS_MORTAIS:
            b = res[("sem treino (motor histórico)", comp, rank)]["win"] * 100
            f2 = res[("treino +2 fixo (regra pré-211)", comp, rank)]["win"] * 100
            a = res[("só PJ (a 211 como publicada)", comp, rank)]["win"] * 100
            c = res[("simétrico (PJ + inimigo)", comp, rank)]["win"] * 100
            sw_flat.append(f2 - b)
            sw_pj.append(a - b)
            sw_sim.append(c - b)
            sw_211.append(a - f2)
            print(f"  {comp:16s} {rank:4d} {b:7.1f}% {f2:8.1f}% {f2-b:+6.1f} "
                  f"{a:7.1f}% {a-b:+6.1f} {a-f2:+8.1f} {c:8.1f}% {c-b:+7.1f}")
    print(f"\n  DECOMPOSIÇÃO DO SWING, em 25 células:")
    print(f"    lacuna antiga do motor (+2 fixo vs. treino 0): médio "
          f"{sum(sw_flat)/len(sw_flat):+.1f}pp · máximo {max(sw_flat):+.1f}pp")
    print(f"    a decisão 211 propriamente (escalado vs. +2 fixo): médio "
          f"{sum(sw_211)/len(sw_211):+.1f}pp · máximo {max(sw_211):+.1f}pp")
    print(f"    total só PJ (o que a nota publica errado hoje): médio "
          f"{sum(sw_pj)/len(sw_pj):+.1f}pp · máximo {max(sw_pj):+.1f}pp")
    print(f"    simétrico (a correção candidata): médio "
          f"{sum(sw_sim)/len(sw_sim):+.1f}pp · máximo {max(sw_sim):+.1f}pp · "
          f"mínimo {min(sw_sim):+.1f}pp")

    # --- o risco que a própria decisão 211 nomeia: os ranks imortais ---
    print("\n" + "-" * 108)
    print("O RISCO NOMEADO PELA DECISÃO 211 — a assimetria de acerto nos ranks imortais")
    print("A 211 avisa que somar +5/+6 ao acerto dos PJs AGRAVA o colapso da bateria 2.")
    print("-" * 108)
    print(f"  {'rank':>4s} {'ΔB':>4s} {'sem treino':>11s} {'só PJ':>9s} {'Δpp':>7s} "
          f"{'simétrico':>10s} {'Δpp':>7s}")
    for rank in (6, 7, 8, 9):
        dom = DOMINIO[(rank, "recem")]
        for delta in (1, 3):
            linha = {}
            for label, kw in modos:
                set_treino(**kw)
                random.seed(20260830)
                r = simulate(rank, "climax", imortal=True, dom_B=dom["B"],
                             pool_mult=dom["pool_mult"], golpe_mode="none", has_boss=True,
                             scenario_factory=lambda rk, d=delta, dm=dom: cena_delta_b(rk, dm, d))
                linha[label] = r["win"] * 100
            b = linha["sem treino (motor histórico)"]
            a = linha["só PJ (a 211 como publicada)"]
            c = linha["simétrico (PJ + inimigo)"]
            print(f"  {rank:4d} {delta:+4d} {b:10.1f}% {a:8.1f}% {a-b:+7.1f} "
                  f"{c:9.1f}% {c-b:+7.1f}")
    set_treino()
    return res


def main():
    print("=" * 108)
    print("DÉCIMA TERCEIRA RODADA — VALIDAÇÃO FINAL CONJUNTA (decisões 146-212)")
    print(f"{N_ITER} iterações/célula · teto {MAX_ROUNDS} rodadas · semente 20260830 · mix de Alma C")
    print("Correção de motor desta rodada: COLAPSO ESPIRITUAL (decisão 205) — Alma 0 não é morte")
    print("=" * 108)
    b1 = bateria_1()
    bateria_2()
    b3 = bateria_3()
    bateria_4(b3)
    b5 = bateria_5()
    guarda_corpo_78()
    return b1, b3, b5


if __name__ == "__main__":
    main()
