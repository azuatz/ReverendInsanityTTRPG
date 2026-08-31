#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação completa pós-decisão 133 — sexta rodada de simulação
================================================================

Rodada de VALIDAÇÃO FINAL: testa juntas todas as mudanças de regra do dia
(decisões 103 a 145 do [[🧭 Log de Decisões]]) nos 4 personagens da mesa, em
todos os ranks jogáveis (1-5, mais o cenário duplo-gênio de rank 6), e
acrescenta as quatro peças que NUNCA foram modeladas em nenhuma simulação
anterior:

  1. Golpe Matador COLETIVO (combo dos 4 PJs) — só o individual (Xie Lang
     sozinho) tinha sido medido até aqui.
  2. Cura — já existia como heurística de IA ("Lee cura abaixo de 40%"), mas
     nunca teve a TAXA DE ACIONAMENTO medida nem a base de dado conferida
     contra a decisão 14 (M d8, não M d10).
  3. Condições de controle — Lentidão nunca foi mecanicamente implementada
     nas rodadas 2-6 anteriores (ficava só documentada como "não modelada,
     pendência aberta"). Esta rodada implementa.
  4. Terreno — só tinha sido medido contra a composição ANTIGA de "Difícil"
     (1 Elite + 2 Guerreiros + 2 Recrutas, decisão 75, ±2 Níveis). O dial foi
     reduzido a ±1 Nível pela decisão 98, e a composição de "Difícil" mudou
     desde então (decisão 137). Esta rodada remedia com a composição ATUAL.

Este script ESTENDE o motor de
[[simulacoes/2026-08-30-motor-v2-pos-decisao-133.py]] e
[[simulacoes/2026-08-30-dificil-rank-escalado.py]] — não reinventa o motor de
dano, ataque/defesa, crítico, Fratura da Abertura, essência sem regen em
combate, Golpe Matador solo, nem a correção de composição de "Padrão"/
"Difícil". Todo esse bloco é copiado com o mínimo de mudança necessária para
plugar as quatro peças novas.

COMPOSIÇÕES DE CENA — a fonte é [[⚔️ Ameaças Genéricas por Rank]] tal como
está HOJE (pós decisão 137), não as composições antigas de rodadas anteriores:

  Fácil          = Horda de 8
  Padrão         = 3 Mestres de Gu, no máx. 1 com especial de Alma (os outros
                    2 com especial física de rank equivalente)
  Padrão pesado  = 2 Mestres de Gu (ambos com especial de Alma — esta
                    composição NUNCA recebeu a correção de limite de Alma que
                    "Padrão" e "Difícil" receberam; ela segue marcada ✝ "não
                    retestada" na nota. Modelada aqui como está documentada,
                    sem correção não-autorizada, e o resultado é reportado
                    para o autor decidir se ela também precisa da correção)
                    + Horda de 8
  Difícil        = ranks 1-4: 3 Mestres de Gu (1 com Alma) + 1 Guerreiro
                    especial · rank 5+: 4 Mestres de Gu (2 com Alma)
  Clímax         = 1 Chefe (ações por CHEFE_ACOES, por rank) + 1 Guerreiro
                    especial

RANKS: 1, 2, 3, 4 e 5. O rank 4 nunca foi simulado em nenhuma rodada anterior
— as tabelas de STAGE_B/STAGE_IDX/CHEFE_ACOES já previam rank 4 (o motor da
quinta rodada só não incluía 4 no laço principal), então é inclusão de
cobertura, não motor novo.

PEÇA NOVA 1 — GOLPE MATADOR COLETIVO
-------------------------------------
Regras-fonte: [[⚡ Golpes Matadores#🤝 Golpe Matador Coletivo]] e a decisão 32.
Núcleo = Xie Lang (maior AST da mesa, e o golpe híbrido Lua+Alma já é o
exemplo usado na ficha dele). Os outros 3 PJs entram como apoio, cada um
contribuindo 1 Gu. Com 4 participantes o bônus é **+6 Níveis** (fixo pela
decisão 32/150, não pelo Teto de Combo individual de ninguém) e a CD de
conjuração usa a linha "5 Gu (coletivo)" da tabela = **22** (a nota do Golpe
Matador rotula essa linha especificamente para o caso coletivo de 4).
Custo = (soma dos custos-base dos 4 participantes) × (nº de participantes) ×
2 (híbrido — os 4 usam Caminhos diferentes), pago proporcionalmente por cada
um (a nota manda "todos pagam o custo de essência da própria parte"; a soma
dá o total, a proporção dá quem paga quanto). Falha aplica a Retaliação
**a todos os 4** (regra explícita da Golpe Matador Coletivo), com a
severidade de golpe híbrido (×3 em Vitalidade na regra textual — aproximado
aqui como um corte de 15% no teto de Vitalidade de cada participante numa
falha por 5+, o triplo do corte de 5% usado no Golpe Matador solo do Xie
Lang nas rodadas anteriores).

Cenário dedicado "Chefe vs Golpe Matador Coletivo": mede o Clímax (Chefe +
Guerreiro) com três variantes de abertura — nenhum Golpe Matador, Golpe
Matador SOLO (só o Xie Lang, como nas rodadas 5-6 anteriores), e Golpe
Matador COLETIVO (os 4) — para isolar quanto o coletivo muda sobre o solo E
sobre não usar golpe nenhum.

PEÇA NOVA 2 — CURA
-------------------
Mantida a heurística já existente (Lee cura o aliado mais ferido abaixo de
40% de Vitalidade, com `M d8`, quando tem essência para isso) — CONFIRMADO
que o script já usa `roll_pool(pc["M"], 8)`, ou seja, `M d8`, batendo com a
decisão 14 (a base é d8, não d10; a Folha de Referência tinha o bug de d10 e
foi corrigida pela decisão 102). O que esta rodada ACRESCENTA é a
INSTRUMENTAÇÃO: contar quantas vezes a cura de fato dispara por combate
(taxa de acionamento), não só rodar o efeito às cegas.

Achado a registrar (não é bug de script, é fato de ficha): NENHUM dos 4 PJs
tem um Gu de cura registrado na ficha oficial em
[[🎲 A Mesa — Personagens dos Jogadores]]. O papel de curandeiro atribuído ao
Lee nas rodadas 1-6 é uma escolha de MODELAGEM, não uma linha de ficha — é
justificável (Lee tem acesso ao Gu do Broto Restaurador, Madeira, dentro do
arsenal de Cinco Elementos que a ficha dele já usa — ver
[[☯️ Os Cinco Caminhos Wu Xing]]), mas o Gu real é mais fraco que a heurística
modelada: `M d6` (não `M d8`), **uma vez por cena** (não toda vez que alguém
cai abaixo de 40%), e só à distância de toque. A heurística desta e das
rodadas anteriores super-representa a cura disponível ao grupo. Sinalizado
no relatório final para o autor decidir se registra oficialmente um Gu de
cura no Lee (e qual) ou se aceita a taxa de cura como "o grupo deveria ter
isso, e ainda não tem por escrito".

PEÇA NOVA 3 — CONDIÇÕES DE CONTROLE (LENTIDÃO)
------------------------------------------------
Implementada pela primeira vez em qualquer rodada (as rodadas 2-6 anteriores
tratavam Lentidão como "não modelada", pendência aberta no Log). Fonte:
[[⚔️ Ameaças Genéricas por Rank]] — a Ação Especial de Guerreiro/Elite e a
especial de Alma do Mestre de Gu aplicam "Lentidão 2" no acerto.

Simplificação de modelagem, documentada: Lentidão é implementada como "o
alvo perde a ação da rodada seguinte" (um turno de skip), não como "metade
do deslocamento por 2 rodadas" (a leitura literal de outros Gu do Catálogo,
ex. Gu do Cristal de Gelo). A leitura de turno-perdido é a mais direta de
simular num modelo sem posição/deslocamento, e é consistente com o texto
"tirar a ação de um personagem vale mais que tirar Vitalidade dele" que a
própria nota de Ameaças usa para justificar a regra.

O Chefe **ignora a primeira Condição de controle que sofrer em cada cena**
(regra já escrita na nota do Chefe) — implementado via flag
`controle_ignorado_usado`.

PEÇA NOVA 4 — TERRENO
-----------------------
Fonte: [[☯️ Os Cinco Caminhos Wu Xing]], pós decisão 98 (dial reduzido de ±2
para ±1 Nível, e -25%/+50% de custo — o custo não é modelado aqui, só o
Nível, pela mesma razão que as rodadas anteriores não modelam custo
percentual de ativação por terreno). Testado no Lee dentro do cenário
"Difícil" ATUAL de rank 3 (3 Mestres [1 Alma] + 1 Guerreiro) — a composição
antiga usada no teste de terreno das rodadas 3-4 (1 Elite + 2 Guerreiros + 2
Recrutas) está obsoleta e não existe mais na tabela de Ameaças.

Uso: python3 "2026-08-31-validacao-completa.py"
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


def make_scenario(rank, comp):
    """Composições ATUAIS de [[⚔️ Ameaças Genéricas por Rank]], pós decisão 137."""
    if comp == "facil":
        return [make_horda(rank, 8)]
    if comp == "padrao":
        # 3 Mestres, no máx. 1 com especial de Alma (correção da decisão 135/137)
        return (
            [make_mestre_de_gu(rank, 0, special="alma")]
            + [make_mestre_de_gu(rank, i, special="physical") for i in (1, 2)]
        )
    if comp == "padrao_pesado":
        # 2 Mestres + Horda de 8. Composição NUNCA corrigida (marcada ✝ na
        # nota) — modelada como documentada, ambos com especial de Alma.
        return (
            [make_mestre_de_gu(rank, i, special="alma") for i in (0, 1)]
            + [make_horda(rank, 8)]
        )
    if comp == "dificil":
        if rank <= 4:
            mestres = [make_mestre_de_gu(rank, i, special="alma" if i == 0 else "physical")
                       for i in range(3)]
            return mestres + [make_guerreiro(rank, especial=True)]
        return (
            [make_mestre_de_gu(rank, i, special="alma") for i in (0, 1)]
            + [make_mestre_de_gu(rank, i, special="physical") for i in (2, 3)]
        )
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
        if candidates and not pc["fallback_raw"] and pc["essence"] is not None and pc["essence"] >= cost:
            pc["essence"] -= cost
            target = min(candidates, key=lambda p: p["vit"] / p["vit_max"])
            heal = roll_pool(pc["M"], 8)  # decisão 14: M d8, não M d10
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


def simulate(rank, comp, imortal=False, n_iter=N_ITER, golpe_mode="solo",
             terreno_delta=0, track_cura=False):
    wins = 0
    surv_total = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=imortal, terreno_delta=terreno_delta)
        enemies = make_scenario(rank, comp)
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
def main():
    print("=" * 90)
    print("SEXTA RODADA — VALIDAÇÃO COMPLETA PÓS-DECISÃO 133 (decisões 103-145)")
    print(f"{N_ITER} iterações por cenário, limite de {MAX_ROUNDS} rodadas, semente 20260830")
    print("=" * 90)

    # --- 1. Bateria principal: ranks 1-5, todos os tipos de cena ---
    print("\n### 1. BATERIA PRINCIPAL — ranks 1-5, composições atuais ###")
    principal = {}
    for rank in (1, 2, 3, 4, 5):
        print(f"\n--- RANK {rank} ---")
        for comp in ("facil", "padrao", "padrao_pesado", "dificil", "climax"):
            win, surv = simulate(rank, comp)
            principal[(rank, comp)] = (win, surv)
            print(f"  {comp:15s}  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    # --- 2. Rank 6 duplo-gênio, revalidado com o motor completo ---
    print("\n### 2. RANK 6 — Imortal Denso Duplo-Gênio, motor completo (Lentidão + cura) ###")
    win_dg, surv_dg = simulate_rank6(make_double_genius_boss)
    win_pf, surv_pf = simulate_rank6(make_pequeno_feito_boss)
    print(f"  Duplo-gênio (B=+3):        vitória {win_dg*100:5.1f}%   sobreviventes {surv_dg:.2f}/4")
    print(f"  Controle Pequeno Feito (B=+1): vitória {win_pf*100:5.1f}%   sobreviventes {surv_pf:.2f}/4")

    # --- 3. Golpe Matador Coletivo vs Chefe ---
    print("\n### 3. GOLPE MATADOR COLETIVO — Chefe + Guerreiro, nenhum / solo / coletivo ###")
    golpe_rows = {}
    for rank in (1, 2, 3, 4, 5):
        row = {}
        for mode in ("none", "solo", "coletivo"):
            win, surv = simulate(rank, "climax", golpe_mode=mode)
            row[mode] = (win, surv)
        golpe_rows[rank] = row
        print(f"  rank {rank}:  nenhum {row['none'][0]*100:5.1f}%   "
              f"solo {row['solo'][0]*100:5.1f}%   coletivo {row['coletivo'][0]*100:5.1f}%")

    # --- 4. Cura: taxa de acionamento ---
    print("\n### 4. CURA — taxa de acionamento (M d8, decisão 14) ###")
    cura_rows = {}
    for rank, comp in ((1, "dificil"), (3, "dificil"), (3, "climax"), (5, "dificil")):
        CURA_STATS["disparos"] = 0
        CURA_STATS["oportunidades"] = 0
        win, surv = simulate(rank, comp, n_iter=N_ITER, track_cura=True)
        taxa = CURA_STATS["disparos"] / max(1, CURA_STATS["oportunidades"])
        cura_rows[(rank, comp)] = (win, surv, CURA_STATS["disparos"], CURA_STATS["oportunidades"], taxa)
        print(f"  rank {rank} {comp:10s}: {CURA_STATS['disparos']} disparos em "
              f"{CURA_STATS['oportunidades']} oportunidades ({taxa*100:.1f}%) — vitória {win*100:.1f}%")

    # --- 5. Controle (Lentidão): liga vs desliga ---
    print("\n### 5. CONTROLE (LENTIDÃO) — liga vs desliga ###")
    global CONTROLE_ENABLED
    controle_rows = {}
    for rank, comp in ((1, "dificil"), (3, "dificil"), (3, "climax"), (5, "dificil")):
        CONTROLE_ENABLED = True
        win_on, surv_on = simulate(rank, comp)
        CONTROLE_ENABLED = False
        win_off, surv_off = simulate(rank, comp)
        CONTROLE_ENABLED = True
        delta = (win_off - win_on) * 100
        controle_rows[(rank, comp)] = (win_on, win_off, delta)
        print(f"  rank {rank} {comp:10s}  com={win_on*100:5.1f}%  sem={win_off*100:5.1f}%  "
              f"Δletalidade(grupo)={delta:+5.1f}pp")

    # --- 6. Terreno — Lee, rank 3, Difícil atual ---
    print("\n### 6. TERRENO — Lee, rank 3, Difícil atual (3 Mestres [1 Alma] + 1 Guerreiro) ###")
    terreno_rows = {}
    for delta, label in ((-1, "hostil (-1 Nível)"), (0, "neutro"), (1, "favorável (+1 Nível)")):
        win, surv = simulate(3, "dificil", terreno_delta=delta)
        terreno_rows[delta] = (win, surv)
        print(f"  {label:22s}  vitória {win*100:5.1f}%   sobreviventes {surv:.2f}/4")

    # --- 7. Fratura da Abertura: reconfirmação rápida com o motor completo ---
    print("\n### 7. FRATURA DA ABERTURA — reconfirmação com o motor completo (rank 3, Difícil/Clímax) ###")
    global FRATURA_ENABLED
    fratura_rows = {}
    for rank, comp in ((3, "dificil"), (3, "climax")):
        FRATURA_ENABLED = True
        win_on, surv_on = simulate(rank, comp)
        FRATURA_ENABLED = False
        win_off, surv_off = simulate(rank, comp)
        FRATURA_ENABLED = True
        delta = (win_off - win_on) * 100
        fratura_rows[(rank, comp)] = (win_on, win_off, delta)
        print(f"  rank {rank} {comp:10s}  com={win_on*100:5.1f}%  sem={win_off*100:5.1f}%  Δ={delta:+5.1f}pp")

    return dict(principal=principal, rank6=(win_dg, surv_dg, win_pf, surv_pf),
                golpe=golpe_rows, cura=cura_rows, controle=controle_rows,
                terreno=terreno_rows, fratura=fratura_rows)


if __name__ == "__main__":
    main()
