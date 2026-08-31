#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima rodada — Alma RARA entre inimigos (diretiva do autor)
================================================================

Este script é uma CÓPIA de
[[simulacoes/2026-08-31-cura-real-remedicao.py]] (sétima rodada) com o
motor INTACTO. O que muda é só a BATERIA: a diretiva do autor — "os
inimigos muito raramente terão poder de alma, a maior parte dos inimigos
são normais ou de outros caminhos" — invalida o default de especial de
Alma do molde Mestre de Gu, e com ele toda a calibração das decisões
135/137/154 (os limites "máx. 1 de 3 com Alma" etc. só existem PORQUE
Alma era o default).

A bateria mortal completa (ranks 1-5 × 5 cenas, 3.000 iterações, semente
20260830) roda sob TRÊS mixes de especial dos Mestres de Gu:

  A — MIX ATUAL (baseline): os limites como publicados em
      [[⚔️ Ameaças Genéricas por Rank]] — Padrão máx. 1 Alma de 3,
      Padrão pesado 1 de 2, Difícil 1 de 3 (ranks 1-4) / 2 de 4 (rank 5).
      NOTA: o script da sétima rodada modelava Padrão pesado com os DOIS
      Mestres de Alma (comentário "nunca corrigida" herdado da sexta,
      anterior à correção da decisão 154); aqui o mix A segue a TABELA
      PUBLICADA (1 de 2), então a linha de Padrão pesado do baseline pode
      diferir levemente da sétima rodada.
  B — ALMA RARA (a diretiva ao pé da letra): ZERO especiais de Alma em
      Fácil/Padrão/Padrão pesado/Difícil; todos os Mestres usam a
      especial física (a troca de Caminho que a nota já documenta).
      Clímax (Chefe + Guerreiro) não tem Mestre de Gu nenhum — nada muda.
  C — ALMA RARA COM EXCEÇÃO ROLADA: igual a B, mas cada Mestre de Gu tem
      1 chance em 6 (1d6 = 6, o mesmo gancho do loadout de bagagem) de
      ser um cultivador de Alma DE VERDADE — rolado por inimigo, na
      montagem da cena.

Depois da bateria, a seção de RECALIBRAÇÃO mede as compensações
candidatas para devolver cada tier à faixa-alvo publicada
(Fácil ≈ 100% · Padrão 75-99% · Difícil ~40-52% · Clímax 56-87%),
usando SÓ peças que já existem (mais um Guerreiro, mais um Mestre) —
nenhum molde nem mecânica nova.

Motor idêntico à sétima rodada: dano, crítico, Fratura da Abertura,
Golpe Matador solo, controle/Lentidão, cura real do Lee (M d6, 1×/cena).

Uso: python3 "2026-08-31-decima-rodada-alma-rara.py"
"""

import random
from collections import Counter

random.seed(20260830)

N_ITER = 3000
MAX_ROUNDS = 20

M_TABLE = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256}

STAGE_B = {1: 0, 2: 1, 3: 2, 4: 3, 5: 3}
STAGE_IDX = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}

COMBO_TETO = {0: 2, 1: 3, 2: 4, 3: 5}
SOLO_APOIOS_MAX = {b: COMBO_TETO[b] - 1 for b in COMBO_TETO}

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

ACT_COST_BASE = 40

# Flags globais de liga/desliga, pra medir impacto isolado de cada peça
FRATURA_ENABLED = True
CONTROLE_ENABLED = True

# Contadores de instrumentação (resetados a cada simulate() dedicado à cura)
CURA_STATS = {"disparos": 0, "oportunidades": 0}


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

    # Terreno Wu Xing (decisão 98): só afeta o Lee, ±1 Nível = ±1 no B por dado
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
        rd=1 * M,
        defense=10 + b["DES"] + 2 * rank,
        alma_def=10 + b["VON"] + rank,
        vazamento=False, skip_turns=0, fallback_raw=False,
        used_golpe=False, actions=1, alive=True,
        cura_usada=False,  # SÉTIMA RODADA: Gu do Broto Restaurador, 1×/cena
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
        rd=rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
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


def _mestres(rank, n, n_alma_mix_a, mix):
    """n Mestres de Gu sob o mix pedido.

    mix "A": os primeiros `n_alma_mix_a` com especial de Alma (os limites
             publicados das decisões 135/137/154);
    mix "B": zero Alma — todos com a especial física (troca de Caminho);
    mix "C": cada Mestre rola 1d6 na montagem da cena — em 6, ele é um
             cultivador de Alma de verdade (o gancho do loadout).
    """
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


def make_scenario(rank, comp, mix="A"):
    """Composições de [[⚔️ Ameaças Genéricas por Rank]] sob o mix de Alma.

    Compensações candidatas da recalibração (só peças existentes):
      padrao_mais_guerreiro   — Padrão + 1 Guerreiro (7 ações/rodada)
      dificil_mais_guerreiro  — Difícil + 1 Guerreiro (8 ações/rodada)
      dificil_quarto_mestre   — troca o Guerreiro por um 4º Mestre
                                (ranks 1-4; 8 ações, todas de Mestre) /
                                5 Mestres no rank 5 (10 ações)
    """
    if comp == "facil":
        return [make_horda(rank, 8)]
    if comp == "padrao":
        return _mestres(rank, 3, 1, mix)
    if comp == "padrao_pesado":
        # Tabela publicada (decisão 154): 1 dos 2 Mestres com Alma no mix A.
        return _mestres(rank, 2, 1, mix) + [make_horda(rank, 8)]
    if comp == "dificil":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)]
        return _mestres(rank, 4, 2, mix)
    if comp == "climax":
        # Chefe + Guerreiro: sem Mestre de Gu — idêntico nos três mixes.
        return [make_chefe(rank), make_guerreiro(rank, especial=True)]
    # --- compensações da recalibração ---
    if comp == "padrao_mais_guerreiro":
        return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True)]
    if comp == "dificil_mais_guerreiro":
        if rank <= 4:
            return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
        return _mestres(rank, 4, 2, mix) + [make_guerreiro(rank, especial=True)]
    if comp == "dificil_quarto_mestre":
        if rank <= 4:
            return _mestres(rank, 4, 1, mix)
        return _mestres(rank, 5, 2, mix)
    # --- compensações PARA BAIXO (medidas depois que a bateria mostrou que
    #     Alma rara torna as cenas MAIS difíceis, não mais fáceis) ---
    if comp == "dificil_g_sem_especial":
        # ranks 1-4: o Guerreiro de apoio SEM Ação Especial (knob existente)
        return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=False)]
    if comp == "dificil_r5_3m2g":
        # rank 5: 3 Mestres + 2 Guerreiros (8 ações, mas 2 delas de Guerreiro)
        return _mestres(rank, 3, 1, mix) + [make_guerreiro(rank, especial=True) for _ in range(2)]
    if comp == "padrao_2m_1g":
        # Padrão aliviado pra rank baixo: 2 Mestres + 1 Guerreiro (5 ações)
        return _mestres(rank, 2, 1, mix) + [make_guerreiro(rank, especial=True)]
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
    """Decisão 132: crítico que deixa o alvo a <=25% de Vitalidade/Alma máxima."""
    if not FRATURA_ENABLED:
        return
    roll = random.randint(1, 6)
    if roll in (1, 2):  # Vazamento
        if target.get("essence") is not None:
            target["vazamento"] = True
        else:
            target["B"] = max(0, target["B"] - 1)
    elif roll in (3, 4):  # Gu Atordoados -> condição de controle
        apply_controle(target, turns=1)
    elif roll == 6:  # Esmagamento
        target["fallback_raw"] = True
    # roll == 5: Fratura funda (Teste de Morte não modelado) -> sem efeito


def apply_controle(target, turns=1):
    """
    Aplica Lentidão/Atordoamento como perda de `turns` ação(ões) seguinte(s).
    Simplificação documentada no cabeçalho: "perde a ação da rodada
    seguinte", não "metade do deslocamento por N rodadas" (a leitura de
    outros Gu do Catálogo) — é a leitura mais direta de simular num modelo
    sem posição/deslocamento.

    O Chefe ignora a PRIMEIRA condição de controle sofrida em cada cena
    (regra escrita em [[⚔️ Ameaças Genéricas por Rank]]).
    """
    if not CONTROLE_ENABLED:
        return
    if target.get("is_boss") and not target.get("controle_ignorado_usado", False):
        target["controle_ignorado_usado"] = True
        return
    target["skip_turns"] = max(target.get("skip_turns", 0), turns)


def pc_attack_dmg(pc, crit=False):
    n = pc["M"] * (2 if crit else 1)
    raw = roll_pool(n, pc["dado"]) + pc["M"] * pc["B"]
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
# Golpe Matador SOLO (Xie Lang) — igual às rodadas anteriores
# ---------------------------------------------------------------------------
def golpe_matador_xie(xie, boss):
    apoios = SOLO_APOIOS_MAX[xie["B"]] if xie["B"] in SOLO_APOIOS_MAX else SOLO_APOIOS_MAX[max(STAGE_B.values())]
    n_gu = apoios + 1
    custo = ACT_COST_BASE * (n_gu ** 2) * 2  # híbrido Lua+Alma
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
        xie["fallback_raw"] = True
        if cd - teste >= 5:
            xie["vit_max"] = round(xie["vit_max"] * 0.95)
            xie["vit"] = min(xie["vit"], xie["vit_max"])


# ---------------------------------------------------------------------------
# PEÇA NOVA — Golpe Matador COLETIVO (os 4 PJs)
# ---------------------------------------------------------------------------
def golpe_matador_coletivo(pcs, boss):
    """
    [[⚡ Golpes Matadores#🤝 Golpe Matador Coletivo]]. Núcleo = Xie Lang (Alma,
    ignora RD). Apoios = os outros PJs vivos. Com 4 participantes: +6 Níveis
    fixo (decisão 32/150), CD 22 (linha "5 Gu, coletivo" da tabela de
    conjuração). Custo = (soma dos custos-base dos participantes) × (nº de
    participantes) × 2 (híbrido — 4 Caminhos diferentes), pago
    proporcionalmente por cada um. Falha: Retaliação em TODOS os
    participantes (regra textual da nota).

    Retorna True se o golpe foi de fato tentado (para consumir a ação de
    todos os participantes na rodada).
    """
    participants = [p for p in pcs if pc_alive(p)]
    if len(participants) < 2 or boss is None or not enemy_alive(boss):
        return False

    nucleo = next((p for p in participants if p["name"] == "Xie Lang"), participants[0])
    apoios_outros = len(participants) - 1
    bonus_levels = {1: 3, 2: 5, 3: 6}.get(apoios_outros, 3 + apoios_outros)
    n_gu_cd = {2: 2, 3: 3, 4: 5}.get(len(participants), len(participants) + 1)
    # Modificador de conjuração −2 aplicado: o combo é lançado ANTES de
    # qualquer troca de golpes na cena (na primeira rodada, antes de as
    # iniciativas agirem) — é exatamente a condição textual "teve uma rodada
    # inteira de preparação sem ser incomodado" de [[⚡ Golpes Matadores]].
    # Sem este modificador a CD efetiva seria 22 e o sucesso cairia pra ~5%
    # (só nat 20, já que o maior AST da mesa é +2) — reportado como achado.
    cd = 12 + 2 * n_gu_cd - 2

    base_shares = {p["name"]: ACT_COST_BASE * p["ess_mod"] for p in participants}
    total_base = sum(base_shares.values())
    n_gu_custo = len(participants)
    custo_total = total_base * n_gu_custo * 2  # híbrido: Caminhos diferentes

    if sum(p["essence"] for p in participants) < custo_total:
        return False  # grupo não consegue pagar -> golpe não é tentado

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
            dmg = roll_pool(n, 12) + nucleo["M"] * (nucleo["B"] + bonus_levels)
            if boss.get("alma") is not None:
                boss["alma"] -= dmg
                if boss["alma"] > 0 and crit and boss["alma"] <= 0.25 * boss["alma_max"]:
                    apply_fratura(boss)
            else:
                dmg = apply_rd(dmg, boss.get("rd", 0), nucleo["M"])
                boss["vit"] -= dmg
    else:
        # Falha: Retaliação em TODOS os participantes (regra do coletivo) —
        # mas "os Gu do combo ficam inutilizáveis" só desliga de fato o
        # ataque do NÚCLEO nesta simulação. Justificativa: cada PJ do modelo
        # só carrega UM Gu de ataque "de assinatura"; os apoios de um Golpe
        # Matador de verdade são Gu BARATOS e FRACOS diferentes do Gu
        # principal de cada um ("Os Gu de apoio são Gu mais fracos, baratos,
        # cuja única função é garantir que o núcleo acerte" —
        # [[⚡ Golpes Matadores]]) — não o próprio Gu de ataque do
        # personagem. Aplicar fallback_raw aos 4 (como uma primeira versão
        # deste script fazia) forçava os 3 apoios a perder o ÚNICO Gu de
        # ataque que o modelo dá a eles, o que não é o que a regra descreve,
        # e produzia um colapso de vitória do grupo pra ~0,3-4% em todo rank
        # — um artefato do modelo (Gu único por PJ), não um efeito real da
        # regra. Corrigido: só o núcleo perde o ataque; os apoios sofrem só
        # a penalidade de Retaliação abaixo.
        nucleo["fallback_raw"] = True
        if cd - teste >= 5:
            for p in participants:
                p["vit_max"] = round(p["vit_max"] * 0.85)
                p["vit"] = min(p["vit"], p["vit_max"])

    return True


# ---------------------------------------------------------------------------
# Turnos
# ---------------------------------------------------------------------------
def pc_turn(pc, pcs, enemies, boss, track_cura=False):
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
        if track_cura:
            CURA_STATS["oportunidades"] += 1 if candidates else 0
        # SÉTIMA RODADA — Gu do Broto Restaurador (decisão 155), não mais a
        # heurística de M d8 sem limite: M d6, e só UMA VEZ POR CENA
        # (`cura_usada`, resetado a cada combate porque make_pc() cria um
        # dict novo por iteração de simulate()). Alcance de toque não é
        # modelado — o motor não tem posição, mesma simplificação já
        # documentada para Terreno na sexta rodada.
        if (candidates and not pc["fallback_raw"] and not pc["cura_usada"]
                and pc["essence"] is not None and pc["essence"] >= cost):
            pc["essence"] -= cost
            pc["cura_usada"] = True
            target = min(candidates, key=lambda p: p["vit"] / p["vit_max"])
            heal = roll_pool(pc["M"], 6)  # Gu do Broto Restaurador: M d6, não M d8
            target["vit"] = min(target["vit_max"], target["vit"] + heal)
            if track_cura:
                CURA_STATS["disparos"] += 1
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
            aplica_lentidao = True  # Ação Especial do Mestre de Gu aplica Lentidão 2
            if e.get("special_type", "alma") == "alma":
                alma_shot = True
                dado_override = 12
            else:
                bonus = 4
                dado_override = 10
        elif e.get("especial") and not e["used_special"]:
            e["used_special"] = True
            bonus = 4
            aplica_lentidao = True  # Ação Especial de Guerreiro/Elite aplica Lentidão 2

        resolve_enemy_hit(e, tgt, dado_override=dado_override, bonus_acerto=bonus,
                           alma_shot=alma_shot, aplica_lentidao=aplica_lentidao)


def update_horda_members(e):
    if not e.get("is_horda"):
        return
    frac = e["vit"] / e["vit_max"] if e["vit_max"] else 0
    e["n_members"] = max(0, round(e["n_members_max"] * max(frac, 0)))


def run_combat(pcs, enemies, has_boss=False, golpe_mode="solo", track_cura=False):
    """
    golpe_mode: "none" (nenhum Golpe Matador), "solo" (só Xie Lang, igual às
    rodadas 5-6 anteriores), "coletivo" (os 4 PJs, peça nova desta rodada).
    """
    boss = next((e for e in enemies if e.get("is_boss")), None) if has_boss else None

    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    coletivo_tentado = golpe_mode != "coletivo"  # se não é coletivo, "já foi tentado" (não dispara)

    for rnd in range(MAX_ROUNDS):
        if not any(pc_alive(p) for p in pcs):
            break
        if not any(enemy_alive(e) for e in enemies):
            break

        # Golpe Matador Coletivo: tentado uma vez, na primeira rodada em que
        # o Chefe está vivo — consome a ação dos 4 PJs naquela rodada.
        skip_pc_this_round = set()
        if not coletivo_tentado and boss is not None and enemy_alive(boss):
            coletivo_tentado = True
            disparou = golpe_matador_coletivo(pcs, boss)
            if disparou:
                skip_pc_this_round = {id(p) for p in pcs}

        for _, _, entity, side in order:
            if not any(pc_alive(p) for p in pcs) or not any(enemy_alive(e) for e in enemies):
                break
            if side == "pc":
                if id(entity) in skip_pc_this_round:
                    continue
                pc_turn(entity, pcs, enemies, boss if golpe_mode == "solo" else None,
                        track_cura=track_cura)
            else:
                enemy_turn(entity, pcs, enemies)
                update_horda_members(entity)

    won = not any(enemy_alive(e) for e in enemies)
    survivors = sum(1 for p in pcs if pc_alive(p))
    return won, survivors


def simulate(rank, comp, mix="A", imortal=False, n_iter=N_ITER, golpe_mode="solo",
             terreno_delta=0, track_cura=False):
    wins = 0
    surv_total = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=imortal, terreno_delta=terreno_delta)
        enemies = make_scenario(rank, comp, mix=mix)
        has_boss = comp == "climax"
        won, survivors = run_combat(pcs, enemies, has_boss=has_boss,
                                     golpe_mode=golpe_mode, track_cura=track_cura)
        wins += int(won)
        surv_total += survivors
    return wins / n_iter, surv_total / n_iter


# ---------------------------------------------------------------------------
# Rank 6 — NPC "Imortal Denso Duplo-Gênio" (decisão 133), com o motor completo
# ---------------------------------------------------------------------------
def make_double_genius_boss(rank=6):
    M = M_TABLE[rank]
    vit = 63 * M
    return dict(
        name="Imortal Denso Duplo-Gênio", side="enemy", rank=rank, M=M, B=3,
        dado=12, vit=vit, vit_max=vit, alma=round(0.7 * vit), alma_max=round(0.7 * vit),
        essence=None, ess_max=None, rd=2 * M, defense=16 + rank, alma_def=10 + rank + 3,
        acerto_bonus=8 + rank, actions=CHEFE_ACOES.get(rank, 4),
        vazamento=False, skip_turns=0, fallback_raw=False, alive=True,
        is_boss=True, controle_ignorado_usado=False,
    )


def make_pequeno_feito_boss(rank=6):
    e = dict(make_double_genius_boss(rank))
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
        won, survivors = run_combat(pcs, enemies, has_boss=True, golpe_mode="none")
        wins += int(won)
        surv_total += survivors
    return wins / n_iter, surv_total / n_iter


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------
RANKS = (1, 2, 3, 4, 5)
COMPS = ("facil", "padrao", "padrao_pesado", "dificil", "climax")


def main():
    print("=" * 90)
    print("DÉCIMA RODADA — ALMA RARA ENTRE INIMIGOS (diretiva do autor)")
    print(f"{N_ITER} iterações por cenário, limite de {MAX_ROUNDS} rodadas, semente 20260830")
    print("=" * 90)

    # --- 1. Bateria principal: ranks 1-5 × 5 cenas × 3 mixes ---
    results = {}
    for mix, label in (("A", "MIX A — atual (limites publicados)"),
                        ("B", "MIX B — Alma rara: zero Alma fora do Clímax"),
                        ("C", "MIX C — Alma rara com exceção rolada (1d6=6 por Mestre)")):
        print(f"\n### {label} ###")
        for rank in RANKS:
            print(f"--- RANK {rank} ---")
            for comp in COMPS:
                win, surv = simulate(rank, comp, mix=mix)
                results[(mix, rank, comp)] = (win, surv)
                print(f"  {comp:15s}  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    # --- 2. Recalibração PARA CIMA: mais inimigos, sob os mixes B e C ---
    # (a hipótese original: "Alma rara deixa as cenas mais fáceis, compense
    # adicionando peça". A bateria acima mostrou o CONTRÁRIO — estas células
    # ficam como evidência de que adicionar peça despenca no penhasco de
    # ações da decisão 137, com ou sem Alma.)
    # Faixas-alvo publicadas: Padrão 75-99% · Difícil ~40-52%.
    print("\n### RECALIBRAÇÃO (para cima) — mais inimigos, sob os mixes B e C ###")
    for mix in ("B", "C"):
        print(f"\n--- mix {mix} ---")
        for comp in ("padrao_mais_guerreiro", "dificil_mais_guerreiro", "dificil_quarto_mestre"):
            for rank in RANKS:
                win, surv = simulate(rank, comp, mix=mix)
                results[(mix, rank, comp)] = (win, surv)
                print(f"  {comp:24s} rank {rank}:  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    # --- 3. Recalibração PARA BAIXO: como a bateria mostrou que Alma rara
    # torna as cenas MAIS difíceis (a especial física rende mais que uma
    # especial de Alma isolada), as células fora da faixa estão ABAIXO dela.
    # Compensações que aliviam, só com knobs existentes.
    print("\n### RECALIBRAÇÃO (para baixo) — aliviar as células que caíram abaixo da faixa ###")
    alvo = (
        ("dificil_g_sem_especial", (1, 2, 3, 4)),   # Guerreiro sem Ação Especial
        ("dificil_r5_3m2g", (5,)),                   # rank 5: 3 Mestres + 2 Guerreiros
        ("padrao_2m_1g", (1, 2)),                    # Padrão aliviado: 2 Mestres + 1 Guerreiro
    )
    for mix in ("B", "C"):
        print(f"\n--- mix {mix} ---")
        for comp, ranks in alvo:
            for rank in ranks:
                win, surv = simulate(rank, comp, mix=mix)
                results[(mix, rank, comp)] = (win, surv)
                print(f"  {comp:24s} rank {rank}:  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    return results


if __name__ == "__main__":
    main()
