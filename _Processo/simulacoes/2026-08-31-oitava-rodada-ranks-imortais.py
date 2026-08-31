#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oitava rodada — bateria de grupo nos ranks imortais (6, 7, 8, 9)
================================================================

Este script é uma CÓPIA de
[[simulacoes/2026-08-31-cura-real-remedicao.py]] (sétima rodada — o motor
mais atual: cura real M d6 1×/cena, Lentidão implementada, Fratura da
Abertura, sem regen de essência em combate, composições corrigidas), com o
`make_pc(..., imortal=True)` da sexta rodada GENERALIZADO para os quatro
ranks imortais e para dois perfis de densidade de Marca por rank. Nada do
motor de dano/ataque/defesa/crítico/controle/composições foi reescrito.

A LACUNA que esta rodada fecha: os ranks 1-5 têm bateria completa de grupo
(rodadas 5-7); o rank 6 só tinha o cenário-Chefe do duplo-gênio (decisão
133) e o rank 8 só um duelo 1v1 (decisão 164). NUNCA houve bateria
grupo×cena nos ranks 6-9 — os 4 PJs contra as 5 composições de cena
(Fácil/Padrão/Padrão pesado/Difícil/Clímax) de [[⚔️ Ameaças Genéricas por
Rank]].

PREMISSAS DE MODELAGEM (todas documentadas também no write-up em
[[🎯 Simulação de Combate — Resultados]]):

1. NÍVEL DE DOMÍNIO DOS PJs POR RANK — dois perfis por rank, tirados
   direto da escada e dos tetos de [[☯️ Marcas de Dao]] (e da regra do
   degrau, decisão 194):

     rank | recém-chegado                    | denso (veterano do rank)
     -----+----------------------------------+---------------------------------
      6   | Vislumbre  (B+0) — entra com     | Pequeno Feito (B+1) — o TETO do
           |  800-900 Marcas (nota: "Quantas |  rank 6 é 9.999; um rank 6 no
           |  Marcas se começa")             |  teto ainda é Pequeno Feito
           |                                  |  (decisão 194 corrigiu o mito do
           |                                  |  veterano; Mestre no rank 6 só
           |                                  |  via gênio pobre, decisão 133 —
           |                                  |  excepcional, não é o perfil)
      7   | Mestre (B+2) — "um rank 7        | Grão-Mestre (B+3) — teto 99.999
           |  recém-chegado especialista      |  está na faixa 50k-149.999
           |  cruzou os 10.000 no mesmo       |
           |  Caminho e já é Mestre (+2)"     |
           |  (texto literal da nota)         |
      8   | Grão-Mestre (B+3) — satura o     | Quase-Supremo (B+4) — teto
           |  teto de 99.999 do rank 7 num    |  299.999 está na faixa
           |  Caminho só -> faixa 50k-149.999 |  150k-299.999
      9   | Grande Mestre Supremo (B+5,      | idem — a escada não tem degrau
           |  pool 2×M) — pela decisão 195,   |  acima do GMS; no rank 9 os dois
           |  o GMS nasce NO rompimento pra   |  perfis COINCIDEM por regra
           |  Venerável (as condições se      |  (diferenças entre as duas
           |  consolidam no salto): TODO      |  linhas medidas = ruído de
           |  rank 9 é GMS desde o primeiro   |  reamostragem, não efeito)
           |  dia, e NENHUM rank 8 jamais é   |
           |  GMS — por isso o denso de rank  |
           |  8 para no Quase-Supremo         |

   Todos os 4 PJs são tratados como ESPECIALISTAS no Caminho de assinatura
   (a norma canônica, decisão 194 — quem divide fica um degrau atrás).
   O pool 2×M do Grande Mestre Supremo segue a Escada de [[⚔️ Combate]]
   ("o único lugar do jogo onde o pool dobra"): pool 2×M dX, bônus M×B
   (o bônus NÃO dobra — calibrado no exemplo `256d12+640` da nota, mesmo
   modelo do script da decisão 164). Crítico continua dobrando o pool
   (GMS crítico = 4×M dados). "Quase-Supremo ignora RD de fontes de rank
   inferior" não se aplica: inimigos são sempre do MESMO rank do grupo.

2. DADO DOS PJs IMORTAIS — igual à sexta rodada (`make_pc(imortal=True)`):
   Gu Imortal sobe o dado de ataque em +2 passos, teto d12 (Xie Lang já
   está em d12; Jiaotang/Demvi d10->d12; Lee d8->d10).

3. INIMIGOS — os MESMOS moldes e composições de cena de [[⚔️ Ameaças
   Genéricas por Rank]] (make_scenario, pós decisão 137), com o B (nível
   de domínio) casado com o perfil do grupo: grupo recém-chegado enfrenta
   inimigos recém-chegados (mesmo B), grupo denso enfrenta inimigos densos.
   É a instrução da própria nota ("Declare rank + nível de domínio no
   Caminho principal") — o exemplo "Imortal Recém-Ascendido (Elite, rank 6,
   Vislumbre)" da nota fecha exatamente com o molde Elite B=0 daqui
   (VIT 21×32=672). No rank 9 os inimigos também são Grande Mestre Supremo
   (B+5, pool 2×M) — mesma régua dos PJs. O Chefe de ranks 7-9 usa 4
   ações/rodada (CHEFE_ACOES já usava .get(rank, 4); o rank 6 já tinha 4).

4. ESSÊNCIA NOS RANKS IMORTAIS — mantida a simplificação documentada da
   sexta rodada: o pool usa o fator do estágio Pico mortal por analogia
   (`aptidão × 4 × 8`), porque o Log não tem fórmula própria de essência
   imortal (a tabela de Ranks e Estágios só dá o GRAU da essência — Uva
   Verde/Jujuba/Lichia/Damasco — e a conversão econômica 100:1, não um
   pool de combate). Custo de ativação segue 40 × ess_mod, sem regen em
   cena (decisão 141).

5. GOLPE MATADOR — golpe_mode="solo" (Xie Lang vs Chefe no Clímax), o
   padrão da bateria; o coletivo é jogada de desespero documentada
   (decisão 161) e fica fora. Teto de Combo acima de B+3 não é modelado:
   para B+4/B+5 o golpe solo continua usando 5 Gu (4 apoios) — a maior
   configuração que a essência do Xie Lang paga (6 Gu custariam
   40×36×2=2.880 > pool de 2.752); é o fallback que o motor já tinha.

6. RANK 9 — os dois lados a M=256 (pool 2×M = 512 dados por ataque).
   Combates que atingem MAX_ROUNDS=20 contam como DERROTA do grupo (o
   `won` do motor já faz isso) e a taxa de timeout é medida e reportada em
   separado, como manda o desenho da rodada: estagnação é achado, não erro.

Bateria: rank (6,7,8,9) × perfil (recém-chegado, denso) × cena (facil,
padrao, padrao_pesado, dificil, climax) — 3.000 iterações por célula,
semente 20260830, MAX_ROUNDS 20.

Uso: python3 "2026-08-31-oitava-rodada-ranks-imortais.py"
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
# OITAVA RODADA — nível de domínio (Marcas de Dao) por rank × perfil.
# Justificativa completa no cabeçalho (premissa 1). pool_mult=2 só no
# Grande Mestre Supremo (Escada de Dano de [[⚔️ Combate]], decisão 164).
# ---------------------------------------------------------------------------
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


def make_pc(name, rank, imortal=False, terreno_delta=0, dom_B=None, pool_mult=1):
    """
    OITAVA RODADA: `dom_B` generaliza o nível de domínio imortal (a sexta
    rodada fixava B=0, Vislumbre, só pro rank 6); `pool_mult` implementa o
    pool 2×M do Grande Mestre Supremo. Sem os dois args, comportamento
    idêntico às rodadas anteriores.
    """
    b = PCS_BASE[name]
    M = M_TABLE[rank]
    if imortal:
        dom_bonus = 0 if dom_B is None else dom_B
        stage_idx = 4  # premissa 4 do cabeçalho: fator do Pico mortal, por analogia
        dado = b["dado"] if b["dado"] >= 12 else b["dado"] + 2
        dado = min(dado, 12)
    else:
        pool_mult = 1
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
        pool_mult=pool_mult,
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
        rd=rd_mult * M, defense=defense + rank, alma_def=10 + rank + 3,
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


def make_scenario(rank, comp, enemy_B=None, enemy_pool_mult=1):
    """
    Composições ATUAIS de [[⚔️ Ameaças Genéricas por Rank]], pós decisão 137.

    OITAVA RODADA: `enemy_B`/`enemy_pool_mult` dão aos inimigos o nível de
    domínio de Marca casado com o perfil do grupo (premissa 3 do cabeçalho).
    Sem os args, comportamento idêntico às rodadas anteriores.
    """
    kw = dict(B=enemy_B, pool_mult=enemy_pool_mult)
    if comp == "facil":
        return [make_horda(rank, 8, **kw)]
    if comp == "padrao":
        # 3 Mestres, no máx. 1 com especial de Alma (correção da decisão 135/137)
        return (
            [make_mestre_de_gu(rank, 0, special="alma", **kw)]
            + [make_mestre_de_gu(rank, i, special="physical", **kw) for i in (1, 2)]
        )
    if comp == "padrao_pesado":
        # 2 Mestres + Horda de 8. Composição NUNCA corrigida (marcada ✝ na
        # nota) — modelada como documentada, ambos com especial de Alma.
        return (
            [make_mestre_de_gu(rank, i, special="alma", **kw) for i in (0, 1)]
            + [make_horda(rank, 8, **kw)]
        )
    if comp == "dificil":
        if rank <= 4:
            mestres = [make_mestre_de_gu(rank, i, special="alma" if i == 0 else "physical",
                                          **kw)
                       for i in range(3)]
            return mestres + [make_guerreiro(rank, especial=True, **kw)]
        return (
            [make_mestre_de_gu(rank, i, special="alma", **kw) for i in (0, 1)]
            + [make_mestre_de_gu(rank, i, special="physical", **kw) for i in (2, 3)]
        )
    if comp == "climax":
        return [make_chefe(rank, **kw), make_guerreiro(rank, especial=True, **kw)]
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
    # pool_mult=2 só no Grande Mestre Supremo (bônus M×B NÃO dobra — cabeçalho)
    n = pc["M"] * pc.get("pool_mult", 1) * (2 if crit else 1)
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

    n = enemy["M"] * enemy.get("pool_mult", 1) * (2 if crit else 1)
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
            n = xie["M"] * xie.get("pool_mult", 1) * (2 if crit else 1)
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
            n = nucleo["M"] * nucleo.get("pool_mult", 1) * (2 if crit else 1)
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
    # OITAVA RODADA (premissa 6): timeout = os dois lados de pé após
    # MAX_ROUNDS. Já conta como derrota do grupo em `won`; medido em
    # separado pra reportar estagnação como achado.
    timeout = (not won) and any(pc_alive(p) for p in pcs)
    return won, survivors, timeout


def simulate(rank, comp, imortal=False, n_iter=N_ITER, golpe_mode="solo",
             terreno_delta=0, track_cura=False, dom_B=None, pool_mult=1,
             enemy_B=None, enemy_pool_mult=1):
    """
    OITAVA RODADA: retorna também a taxa de timeout (MAX_ROUNDS com os dois
    lados de pé — já contada como derrota na taxa de vitória).
    """
    wins = 0
    surv_total = 0
    timeouts = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=imortal, terreno_delta=terreno_delta,
                       dom_B=dom_B, pool_mult=pool_mult)
        enemies = make_scenario(rank, comp, enemy_B=enemy_B,
                                enemy_pool_mult=enemy_pool_mult)
        has_boss = comp == "climax"
        won, survivors, timeout = run_combat(pcs, enemies, has_boss=has_boss,
                                              golpe_mode=golpe_mode, track_cura=track_cura)
        wins += int(won)
        surv_total += survivors
        timeouts += int(timeout)
    return wins / n_iter, surv_total / n_iter, timeouts / n_iter


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
        won, survivors, _timeout = run_combat(pcs, enemies, has_boss=True,
                                               golpe_mode="none")
        wins += int(won)
        surv_total += survivors
    return wins / n_iter, surv_total / n_iter


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------
PERFIL_LABEL = {"recem": "Recém-chegado", "denso": "Denso"}


def main():
    print("=" * 96)
    print("OITAVA RODADA — BATERIA DE GRUPO NOS RANKS IMORTAIS (6, 7, 8, 9)")
    print(f"{N_ITER} iterações por célula, limite de {MAX_ROUNDS} rodadas, semente 20260830")
    print("golpe_mode='solo' (decisão 161: o coletivo é desespero, fora da bateria padrão)")
    print("=" * 96)

    resultados = {}
    for perfil in ("recem", "denso"):
        print(f"\n### PERFIL: {PERFIL_LABEL[perfil].upper()} "
              f"(grupo e inimigos com o mesmo nível de domínio — premissa 3) ###")
        for rank in (6, 7, 8, 9):
            dom = DOMINIO[(rank, perfil)]
            print(f"\n--- RANK {rank} · {dom['nome']} (B+{dom['B']}"
                  f"{', pool 2×M' if dom['pool_mult'] == 2 else ''}) ---")
            for comp in ("facil", "padrao", "padrao_pesado", "dificil", "climax"):
                win, surv, tout = simulate(
                    rank, comp, imortal=True,
                    dom_B=dom["B"], pool_mult=dom["pool_mult"],
                    enemy_B=dom["B"], enemy_pool_mult=dom["pool_mult"],
                )
                resultados[(perfil, rank, comp)] = (win, surv, tout)
                extra = f"   timeout {tout*100:4.1f}%" if tout > 0 else ""
                print(f"  {comp:15s}  vitória {win*100:5.1f}%   "
                      f"sobreviventes {surv:.2f}/4{extra}")

    # Âncora de comparação: o cenário rank 6 do duplo-gênio (decisões 133/154),
    # rerodado com este mesmo binário pra confirmar que o motor continua o mesmo.
    print("\n### ÂNCORA — rank 6 Duplo-Gênio (decisão 133), pro motor conferir com a 7ª rodada ###")
    win_dg, surv_dg = simulate_rank6(make_double_genius_boss)
    win_pf, surv_pf = simulate_rank6(make_pequeno_feito_boss)
    print(f"  Duplo-gênio (B=+3):            vitória {win_dg*100:5.1f}%   sobreviventes {surv_dg:.2f}/4  (7ª rodada: 6,5%)")
    print(f"  Controle Pequeno Feito (B=+1): vitória {win_pf*100:5.1f}%   sobreviventes {surv_pf:.2f}/4  (7ª rodada: 19,8%)")

    # DIAGNÓSTICO — por que a escada de dificuldade colapsa nos ranks imortais.
    # Duas assimetrias estruturais entre PJ e molde de inimigo, medidas em
    # isolamento e juntas (não é proposta de regra — é instrumentação do achado):
    #   +dado   = inimigos ganham o MESMO upgrade de dado dos PJs imortais
    #             (+2 passos, teto d12 — os moldes ficam no d8/d10 mortal);
    #   +acerto = acerto do inimigo escala 2/rank como a Defesa dos PJs escala
    #             (os moldes dão +1/rank; a Defesa de PJ sobe +2/rank, então o
    #             hit% inimigo derrete de ~50% no rank 5 pra ~25-35% no rank 9).
    print("\n### DIAGNÓSTICO — as duas assimetrias PJ×molde, isoladas (perfil recém-chegado) ###")
    diag = {}
    for rank in (6, 8):
        dom = DOMINIO[(rank, "recem")]
        for comp in ("dificil", "climax"):
            row = {}
            for label, up_die, up_ac in (("base", False, False), ("+dado", True, False),
                                          ("+acerto", False, True), ("ambos", True, True)):
                win, surv, _ = simulate_diag(rank, comp, dom, up_die, up_ac)
                row[label] = (win, surv)
            diag[(rank, comp)] = row
            print(f"  rank {rank} {comp:8s}  base {row['base'][0]*100:5.1f}%   "
                  f"+dado {row['+dado'][0]*100:5.1f}%   +acerto {row['+acerto'][0]*100:5.1f}%   "
                  f"ambos {row['ambos'][0]*100:5.1f}%")

    return dict(resultados=resultados, ancora=(win_dg, surv_dg, win_pf, surv_pf),
                diag=diag)


def simulate_diag(rank, comp, dom, up_die, up_acerto, n_iter=N_ITER):
    """Variante instrumentada do simulate() só pro diagnóstico do main()."""
    wins = surv_total = timeouts = 0
    for _ in range(n_iter):
        pcs = make_pcs(rank, imortal=True, dom_B=dom["B"], pool_mult=dom["pool_mult"])
        enemies = make_scenario(rank, comp, enemy_B=dom["B"],
                                enemy_pool_mult=dom["pool_mult"])
        for e in enemies:
            if up_die and not e.get("is_horda"):
                e["dado"] = min(12, e["dado"] + 2)
            if up_acerto:
                e["acerto_bonus"] += rank  # vira base + 2×rank, paridade com a Defesa de PJ
        won, survivors, timeout = run_combat(pcs, enemies, has_boss=(comp == "climax"))
        wins += int(won)
        surv_total += survivors
        timeouts += int(timeout)
    return wins / n_iter, surv_total / n_iter, timeouts / n_iter


if __name__ == "__main__":
    main()
