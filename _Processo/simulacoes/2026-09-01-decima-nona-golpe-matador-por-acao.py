#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima nona rodada — O GOLPE MATADOR MEDIDO POR AÇÃO, E A REGRA NOVA DA DECISÃO 240
===================================================================================

Cópia de [[simulacoes/2026-09-01-decima-oitava-consertos-e-revalidacao.py]].
Duas coisas mudam, e as duas são de fora do motor:

  (A) A REGRA MUDOU NO DISCO (decisão 240, commit 5014315). [[⚡ Golpes Matadores]]
      publica agora:

          Teste de Conjuração = d20 + AST + rank + nível de domínio no Caminho do núcleo
          CD = 10 + (número de Gu no combo)

      Antes era `d20 + AST + domínio` contra `CD = 12 + 2 × nGu`. A causa
      estrutural do conserto: nada na rolagem crescia com o personagem na fase
      mortal (AST é fixa desde a criação, domínio só existe do rank 6), então um
      rank 5 rolava igual a um rank 1 contra uma CD que só subia.

  (B) O GATILHO DA 18ª ESTAVA MEDINDO O EIXO ERRADO, e o erro é meu. Ele
      perguntava "o combo bate o que a MESMA ESSÊNCIA compra em ataques comuns?".
      Essa pergunta só faz sentido se essência for escassa, e a própria 18ª mediu
      que não é: 27 ações de tanque no rank 3, 55 no rank 5, contra cenas de 7 a
      9 rodadas. **O recurso escasso é a AÇÃO.** A seção "Contra quem vale
      disparar" foi reescrita na decisão 240 com o eixo certo: *"a pergunta não é
      'eu tenho essência para isto?' — é 'este alvo merece a minha ação?'"*, com
      a regra de bolso de **disparar contra quem não cairia com um ataque normal**.


A NOVA IMPLEMENTAÇÃO DO TESTE (`GOLPE_REGRA = "240"`)
-----------------------------------------------------
Uma escolha de implementação, e ela é FORÇADA pelos dois números que a nota
publica:

    "nível de domínio" na fase mortal = **0**, não `B`.

A 18ª tinha adotado `domínio = B` por equivalência escrita em
[[📈 O Que Muda ao Subir]] — mas ali o `B` ocupava o lugar do domínio numa
fórmula que NÃO somava rank. A fórmula nova soma o rank explicitamente, e é o
rank que faz o papel de "o personagem cresce". Somar os dois seria contar a
progressão duas vezes — e a aritmética confirma: com domínio 0, a nota bate
EXATAMENTE nos dois números que ela promete.

    registrado, 5 Gu, rank 5, AST +2:  CD 10+5=15, −4 registrado = 11
                                       d20 + 2 + 5 ≥ 11  →  d20 ≥ 4  →  **85%**  ✅ (a nota diz 85%)
    improvisado, 4 Gu, sob pressão:    CD 10+4=14, +4 improviso, +2 dano = 20
                                       d20 + 2 + 5 ≥ 20  →  d20 ≥ 13  →  **40%**  ✅ (a nota diz 40%)

Com `domínio = B` daria 100% e 55% — números que a nota não publica em lugar
nenhum. A leitura fica declarada aqui e vira premissa publicada.


O GATILHO POR AÇÃO (`GOLPE_HEURISTICA = "acao"`)
-------------------------------------------------
O recurso escasso é a ação, então o valor de disparar é medido sobre as AÇÕES
que a cena ainda comporta — não sobre as que a essência bancaria num mundo com
rodadas infinitas.

    barra    = o que resta do alvo no trilho que o golpe atinge
    e_norm   = dano esperado de UM ataque comum do PJ
    e_golpe  = dano esperado do golpe (núcleo + M × apoios)
    e_cru    = dano esperado sem Gu (o estado de Retaliação, `fallback_raw`)
    p        = probabilidade do teste de conjuração passar, pela CD real
    util(x)  = min(x, barra)      ← O EXCEDENTE NÃO VALE NADA (é o overkill que a
                                    regra nova chama de desperdício de ação)

    r        = AÇÕES que este PJ ainda terá NESTA CENA contra este alvo
             = min(rodadas restantes, ⌈vit do alvo / dano esperado do GRUPO por rodada⌉)

    n_a      = ataques comuns bancados SEM disparar   = min(r,   essência/custo_atq)
    n_b      = ataques comuns bancados DEPOIS         = min(r−1, (essência−custo)/custo_atq)

    NÃO DISPARAR:  A = util(n_a × e_norm)
    DISPARAR:      B = p × util(e_golpe + n_b × e_norm) + (1−p) × util((r−1) × e_cru)
    Dispara se B > A.

**A ÚNICA diferença de fórmula em relação à 18ª é o `r`** — e é ela que carrega
o erro inteiro. A 18ª usava `r = ⌈barra / e_norm⌉`: quantas rodadas o PJ SOZINHO
levaria para derrubar a barra. Com esse horizonte, o ataque comum sempre alcança
a barra inteira, os dois ramos empatam no teto `util(...) = barra`, e disparar só
pode PERDER (porque `p < 1`). Era um gatilho que provava que o combo nunca paga
por construção. O horizonte certo é o da CENA: o alvo cai quando o GRUPO o
derruba, e contra um Chefe isso são 2 a 4 rodadas, não 8 a 25.

A variante `"acao_pura"` implementa a regra de bolso da nota ao pé da letra —
dispara sse `p × util(e_golpe) > util(e_norm)`, isto é, "este alvo merece a minha
ação?" sem horizonte nenhum. Ela é reportada como sensibilidade.

A probabilidade de ACERTO é a mesma nos dois ramos e se cancela; a heurística não
consome rolagem nenhuma, então ligar/desligar o gatilho não desalinha o fluxo
aleatório de nada que venha antes.


AS DUAS PERGUNTAS DA RODADA (as que a decisão 240 encomendou)
--------------------------------------------------------------
  1. Com a confiabilidade consertada e o gatilho por ação, o combo PASSA A
     DISPARAR — e contra quem? Só Chefe, ou também Elite?
  2. O que isso move na CENA DE CHEFE, hoje em >99% de vitória do grupo?

O molde do Chefe fica INTOCADO por decisão do autor. Se a cena continuar trivial
com o combo disparando, isso é o achado.

Semente 20260830, 3.000 iterações/célula, mix de Alma "C", treino 0 dos dois
lados (decisão 215). Baseline: decisão 231 (candidata C), 227 (`ess_mod` 1,25),
236 (a Lee de foice), 238 (paridade de Níveis de ficha, gatilho econômico).
"""


import math
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
# FACE RD do "Nível de Potência" (décima quinta) — SÓ NO LADO DO PJ
# ---------------------------------------------------------------------------
# Cláusula anti-dupla-contagem dada pelo autor: a RD impressa dos moldes de
# inimigo já embute o patamar de domínio deles, então os moldes NÃO recebem a
# face. Varia-se só o PJ.
#
#   'zero' — Níveis nunca tocam RD (a regra de hoje: RD do PJ = 1 × M)
#   'per1' — +1 na RD base por Nível          → RD = (1 + N) × M
#   'per2' — +1 na RD base a cada 2 Níveis    → RD = (1 + N // 2) × M
#
# `N` = os Níveis que o motor já calcula pro personagem: `pc["B"]`, que é a
# Densidade da Essência do estágio na fase mortal (0/1/2/3/3 nos ranks 1-5) e
# o nível de domínio de Marca na fase imortal.
RD_FACE_MODE = "zero"


# ---------------------------------------------------------------------------
# ███ O NERF DO CAMINHO DA ALMA (décima sexta) ███
# ---------------------------------------------------------------------------
# Knob global lido por TODO o motor, nos dois lados da mesa. Cinco modos:
#
#   'atual' — a regra de hoje: d12, fura 100% da RD, barra
#             `(12 + 2×VON + 3×B) × M`, Defesa de Alma `10 + VON + 1×rank`.
#   'A'     — alinhamento de degrau: d12, fura só METADE da RD (Espada/Relâmpago).
#   'B'     — queda de dado: d10, fura tudo.
#   'C'     — endurecimento da barra: d12, fura tudo, barra
#             `(16 + 3×VON + 3×B) × M` e Defesa de Alma `10 + VON + 2×rank`.
#   'C_bar' / 'C_def' — as duas metades da C isoladas (diagnóstico).
# DÉCIMA SÉTIMA: o default passa a ser "C" — a decisão 231 APLICOU a candidata C.
# "atual" fica disponível só como referência histórica.
ALMA_MODE = "C"

# 'CA' / 'CB' = os EMPILHAMENTOS (C + A, C + B), medidos depois que a bateria
# principal mostrou que a C é a única que move a agulha sozinha.
_ALMA_DADO = {"atual": 12, "A": 12, "B": 10, "C": 12, "C_bar": 12, "C_def": 12,
              "CA": 12, "CB": 10}
# fração da RD do alvo que o golpe de Alma AINDA sofre (0 = fura tudo)
_ALMA_RD = {"atual": 0.0, "A": 0.5, "B": 0.0, "C": 0.0, "C_bar": 0.0, "C_def": 0.0,
            "CA": 0.5, "CB": 0.0}
_ALMA_BAR_DURA = {"atual": False, "A": False, "B": False,
                  "C": True, "C_bar": True, "C_def": False, "CA": True, "CB": True}
_ALMA_DEF_DURA = {"atual": False, "A": False, "B": False,
                  "C": True, "C_bar": False, "C_def": True, "CA": True, "CB": True}

# Fator de inflação da barra de Alma dos MOLDES sob a C. A barra de molde é
# `razão × Vitalidade`, não a fórmula de PJ, então não dá pra aplicar a fórmula
# nova nele. 1,35 é a média da inflação que a fórmula de PJ sofre nas quatro
# fichas da mesa nos ranks 1-5 (de +29% a +39%).
ALMA_BAR_MOLDE_MULT = 1.35


def alma_dado():
    return _ALMA_DADO[ALMA_MODE]


def alma_rd_frac():
    return _ALMA_RD[ALMA_MODE]


def alma_bar_pc(VON, B, M):
    if _ALMA_BAR_DURA[ALMA_MODE]:
        return (16 + 3 * VON + 3 * B) * M
    return (12 + 2 * VON + 3 * B) * M


def alma_def_pc(VON, rank):
    passo = 2 if _ALMA_DEF_DURA[ALMA_MODE] else 1
    return 10 + VON + passo * rank


def alma_bar_molde(base):
    return round(base * ALMA_BAR_MOLDE_MULT) if _ALMA_BAR_DURA[ALMA_MODE] else base


def alma_def_molde(rank):
    passo = 2 if _ALMA_DEF_DURA[ALMA_MODE] else 1
    return 10 + passo * rank + 3


def aplica_rd_alma(dmg, target, m_floor):
    """A RD que um golpe de Alma sofre. Só o candidato A tem alguma."""
    frac = alma_rd_frac()
    if frac <= 0:
        return dmg
    return apply_rd(dmg, target.get("rd", 0) * frac, m_floor)


def set_alma(mode="atual"):
    global ALMA_MODE
    ALMA_MODE = mode


def rd_face_bonus(n_niveis):
    if RD_FACE_MODE == "per1":
        return n_niveis
    if RD_FACE_MODE == "per2":
        return n_niveis // 2
    return 0


def set_rd_face(mode="zero"):
    global RD_FACE_MODE
    RD_FACE_MODE = mode


# Instrumentação: quanto a RD do PJ MORDE de fato. O motor nunca mediu isso.
# `hits`    = acertos de inimigo na Vitalidade de um PJ (os únicos em que a RD
#             do PJ entra na conta — dano de Alma ignora RD por regra).
# `clamped` = quantos desses caíram no PISO `M` (a RD comeu tudo que podia).
RD_STATS = dict(hits=0, clamped=0, bruto=0.0, liquido=0.0)


def reset_rd_stats():
    for k in RD_STATS:
        RD_STATS[k] = 0 if k in ("hits", "clamped") else 0.0


# Instrumentação nova da décima sexta: quanto dano cada PJ entrega, separado
# por trilho (Vitalidade × Alma). É com ela que se lê se o nerf piorou o
# Caminho da Alma em cena de grupo — que é o ponto fraco dele, não o forte.
DMG_TRACK = None


def reset_dmg_track(on=True):
    global DMG_TRACK
    DMG_TRACK = ({n: dict(vit=0.0, alma=0.0) for n in PCS_BASE} if on else None)


# ---------------------------------------------------------------------------
# Fichas dos 4 PJs (A Mesa — Personagens dos Jogadores)
# ---------------------------------------------------------------------------
# `nivel_bonus` = Níveis de Dano que a FICHA do personagem dá aos Gu do
# Caminho dele. As 14 rodadas anteriores modelavam 0 para todos — inclusive
# para o Xie Lang, que pela ficha publicada tem **+1** (Físico da Lua Antiga
# com a Abertura Latente; +2 quando ela fechar). Esta rodada precisa do knob.
#
# `alma_frac` (NOVO na décima sexta) = fração dos ataques do personagem que é
# golpe de ALMA. `dado` passa a ser o dado do Caminho PRINCIPAL dele (o que ele
# rola nos outros `1 − alma_frac` ataques). Com `alma_frac = 1.0` o
# comportamento é bit-a-bit o das quinze rodadas anteriores (nenhuma rolagem
# nova é consumida — ver `resolve_pc_hit`).
#
# `nivel_bonus_rank` (NOVO na décima sétima) = Níveis de Potência que a ficha dá
# ao golpe, RANK A RANK. É o que a escada de Gu Wu Xing 🔨amplifica concede à
# Lee (ver cabeçalho); quando ausente, cai no `nivel_bonus` escalar de sempre.
PCS_BASE = {
    # Décima sétima: o 80:20 da decisão 231 vira o DEFAULT da ficha dele.
    "Xie Lang": dict(FOR=-1, CON=3, DES=3, AST=2, VON=3, CAR=2, aptidao=86,
                     dado=8, alma_dmg=True, alma_frac=0.20, atk_attr="VON",
                     ess_mod=1.25, raw_die=6, role="caster", nivel_bonus=0),
    "Jiaotang": dict(FOR=4, CON=3, DES=2, AST=1, VON=1, CAR=0, aptidao=76,
                      dado=10, alma_dmg=False, alma_frac=0.0, atk_attr="FOR",
                      ess_mod=1.0, raw_die=10, role="melee", nivel_bonus=0),
    # Décima sétima: a Lee em CORPO A CORPO é o default (diretiva do autor).
    # Foice = arma pesada `d10`; ataque por FOR +3; `raw_die` 10 (o dado da
    # foice sem Gu ativo); `role="healer"` INTACTO — a cura continua na ficha.
    "Lee": dict(FOR=3, CON=2, DES=2, AST=1, VON=3, CAR=1, aptidao=63,
                dado=10, alma_dmg=False, alma_frac=0.0, atk_attr="FOR",
                ess_mod=1.0, raw_die=10, role="healer", nivel_bonus=0,
                nivel_bonus_rank={1: 1, 2: 2, 3: 2, 4: 3, 5: 4}),
    "Demvi": dict(FOR=-1, CON=1, DES=4, AST=2, VON=3, CAR=2, aptidao=56,
                  dado=10, alma_dmg=False, alma_frac=0.0, atk_attr="VON",
                  ess_mod=1.0, raw_die=4, role="striker", nivel_bonus=0),
}

# Os dois perfis do Xie Lang. O primeiro é o que as quinze rodadas mediram
# (e está ERRADO); o segundo é a ficha de verdade (decisão do autor).
XIE_PERFIL = {
    "puro Alma (1ª-15ª)": dict(dado=12, alma_frac=1.0),
    "80:20 Lua:Alma": dict(dado=8, alma_frac=0.20),
}

# Os três perfis da Lee. O primeiro é o que as dezesseis rodadas mediram e que a
# diretiva do autor tornou obsoleto; os outros dois são o TETO e o PISO da
# leitura de corpo a corpo (ver cabeçalho).
LEE_PERFIL = {
    "conjuradora (1ª-16ª)": dict(dado=8, atk_attr="VON", raw_die=6,
                                 nivel_bonus_rank=None),
    "melee — foice + Wu Xing": dict(dado=10, atk_attr="FOR", raw_die=10,
                                    nivel_bonus_rank={1: 1, 2: 2, 3: 2,
                                                      4: 3, 5: 4}),
    "melee — foice crua (piso)": dict(dado=10, atk_attr="FOR", raw_die=10,
                                      nivel_bonus_rank=None),
}


def usa_perfil_lee(rotulo):
    """NÃO reseta a mesa — é composável com o perfil do Xie Lang."""
    set_pc_variant("Lee", **LEE_PERFIL[rotulo])


# ---------------------------------------------------------------------------
# ███ BUG 2 — A ESCADA DE NÍVEIS DE FICHA, PJ A PJ ███
# ---------------------------------------------------------------------------
# Derivação completa no cabeçalho. Resumo das fontes:
#   Lee      — Gu 🔨amplifica do Wu Xing, rank a rank (Catálogo)   {1,2,2,3,4}
#   Jiāotáng — `+1 Nível a cada 2 ranks do próprio Gu` ([[💪 Caminho da Força]])
#              = floor(R/2), + a Mão de Pedra permanente (Corpo) a partir do r3
#   Xie Lang — Fase da Lua ([[🌙 Caminho da Lua]]): 0 / +1 / +2, NÃO escala
#   Demvi    — Corrente + Altitude ([[🌪️ Caminho do Vento]]), teto +4, NÃO escala
_ESC = lambda v: {r: v for r in range(1, 6)}          # escada plana (dial de cena)

LEE_WUXING = {1: 1, 2: 2, 3: 2, 4: 3, 5: 4}
JIAO_AMP = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}             # só o amplificador ativo
JIAO_FICHA = {1: 0, 2: 1, 3: 2, 4: 3, 5: 3}           # + Mão de Pedra permanente

NIVEIS_FICHA = {
    # o estado da décima sétima: SÓ a Lee recebe escada. É o bug.
    "17ª — só a Lee": {"Lee": LEE_WUXING},
    # o estado das rodadas 1ª-16ª: ninguém recebe nada
    "piso — ninguém": {},
    # ▸ O DEFAULT desta rodada: condições ordinárias de cena, cada PJ com o que
    #   a nota publicada dele concede.
    "paridade — ordinária": {"Lee": LEE_WUXING, "Jiaotang": JIAO_FICHA,
                             "Xie Lang": _ESC(1), "Demvi": _ESC(2)},
    # ▸ TETO: lua cheia para o Xie Lang, voando em tempestade para o Demvi,
    #   solo natural sempre para a Lee (e ainda SEM a Descarga do Jiāotáng).
    "paridade — teto": {"Lee": LEE_WUXING, "Jiaotang": JIAO_FICHA,
                        "Xie Lang": _ESC(2), "Demvi": _ESC(4)},
    # ▸ PISO CONDICIONAL: os dois dials de cena zerados (cripta, lua nova); só
    #   o que é permanente/sustentado sobrevive.
    "paridade — dials zerados": {"Lee": LEE_WUXING, "Jiaotang": JIAO_FICHA},
    # ▸ a leitura conservadora do Jiāotáng (só o amplificador, como a 17ª testou)
    "paridade — Jiāotáng só amplificador": {"Lee": LEE_WUXING,
                                            "Jiaotang": JIAO_AMP,
                                            "Xie Lang": _ESC(1), "Demvi": _ESC(2)},
}


def set_niveis_ficha(modo="17ª — só a Lee"):
    """Aplica uma das escadas de `NIVEIS_FICHA`. Sobrescreve `nivel_bonus_rank`
    de TODOS os PJs (quem não está no dicionário volta a zero)."""
    tab = NIVEIS_FICHA[modo]
    for nome in PCS_BASE:
        PCS_BASE[nome]["nivel_bonus_rank"] = tab.get(nome)
        PCS_BASE[nome]["nivel_bonus"] = 0

# Snapshot imutável da ficha original, pra restaurar depois das variantes.
_PCS_ORIG = {k: dict(v) for k, v in PCS_BASE.items()}


def set_pc_variant(name, **kw):
    """Sobrescreve campos da ficha de um PJ (Xie Lang sem o Físico, etc.)."""
    PCS_BASE[name].update(kw)


def reset_pcs():
    for k, v in _PCS_ORIG.items():
        PCS_BASE[k] = dict(v)

ACT_COST_BASE = 40

FRATURA_ENABLED = True
CONTROLE_ENABLED = True


# ---------------------------------------------------------------------------
# ███ A ISENÇÃO DE HÍBRIDO DO XIE LANG (décima sétima, decisão 233) ███
# ---------------------------------------------------------------------------
# [[⚡ Golpes Matadores]]: `Custo = (soma das ativações) × (nº de Gu no combo)`,
# `× 2 se HÍBRIDO`. A Ressonância da Montanha Fria isenta o Xie Lang dessa dobra
# quando o golpe mistura Lua e Alma — e SÓ dela. **`ess_mod` fica em 1,25**: as
# Marcas continuam divididas entre os dois Caminhos (decisões 227 e 233).
#
#   2.0 — a regra de hoje (a dobra de híbrido cheia)
#   1.0 — a ISENÇÃO da decisão 233 (1.280 → 640 no Pico do rank 2)
#   1.5 — o meio-termo que o parecer ofereceu como dial, se a isenção passar do ponto
XIE_HIBRIDO_MULT = 2.0

# A Retaliação agravada de híbrido é `× 3` em Vitalidade contra o `× 2` normal
# ([[⚡ Golpes Matadores]], "A Retaliação de Essência"). O motor abstrai o
# Retrocesso como corte de `vit_max`; com a isenção o corte cai na mesma razão.
XIE_RETALIACAO_AGRAVADA = True
_RETROCESSO_SOLO = 0.05          # 5% de vit_max — o corte agravado de hoje


def set_xie_buff(hibrido_mult=2.0, retaliacao_agravada=True):
    global XIE_HIBRIDO_MULT, XIE_RETALIACAO_AGRAVADA
    XIE_HIBRIDO_MULT = hibrido_mult
    XIE_RETALIACAO_AGRAVADA = retaliacao_agravada


def _corte_retrocesso_xie(pc=None):
    """Fração de `vit_max` que sobra depois do Retrocesso do golpe solo. O
    agravamento (`× 3` em Vitalidade) é do golpe HÍBRIDO — só o Xie Lang monta
    um; para os outros três o combo é de um Caminho só e o corte é o normal."""
    if pc is not None and pc["name"] != "Xie Lang":
        return 1.0 - _RETROCESSO_SOLO * (2.0 / 3.0)
    if XIE_RETALIACAO_AGRAVADA:
        return 1.0 - _RETROCESSO_SOLO            # 0,95 — o `× 3` de híbrido
    return 1.0 - _RETROCESSO_SOLO * (2.0 / 3.0)  # 0,9667 — o `× 2` normal


# ---------------------------------------------------------------------------
# ███ O GOLPE MATADOR NO DUELO (décima sétima) ███
# ---------------------------------------------------------------------------
# Dezesseis rodadas mediram PvP com o gatilho do motor (`boss is not None`), que
# `run_duel` nunca satisfaz — ou seja, SEM Golpe Matador nenhum. Com o knob
# desligado (default) o fluxo aleatório é bit-a-bit o das rodadas anteriores;
# ligado, o oponente do duelo faz as vezes de Chefe e o golpe do Xie Lang
# dispara uma vez por duelo. É a ÚNICA cena do motor em que a isenção de custo
# pode aparecer. Escolha declarada, não dedução.
GOLPE_EM_DUELO = False


def set_golpe_em_duelo(on=False):
    global GOLPE_EM_DUELO
    GOLPE_EM_DUELO = on


# ---------------------------------------------------------------------------
# ███ O TESTE DE CONJURAÇÃO (achado da décima sétima) ███
# ---------------------------------------------------------------------------
# [[⚡ Golpes Matadores]] publica `Teste = d20 + AST + nível de domínio no
# Caminho do núcleo`, com `−4 se você já usou este golpe registrado antes com
# sucesso (a sequência é treinada)` — e a nota diz por extenso: *"um golpe
# registrado, treinado e usado em condições decentes passa quase sempre. O teste
# existe pra punir improviso e pressão"*.
#
# O motor de dezesseis rodadas rola só `d20 + AST`, sem domínio e sem o −4. Isso
# transforma o golpe de rank 5 (CD 22, AST +2) numa loteria de **5%** — o oposto
# exato do que a regra diz. O achado nunca apareceu porque o gatilho é
# `boss is not None` e as baterias de PvP nunca têm Chefe.
#
#   False — o teste histórico do motor (default: as 17 rodadas reproduzem)
#   True  — o teste PUBLICADO INTEIRO (BUG 1 desta rodada; ver cabeçalho)
GOLPE_TESTE_PUBLICADO = False

# Os quatro modificadores da nota, cada um num knob (todos mexem na CD — a
# leitura declarada no cabeçalho, item (b)).
GOLPE_REGISTRADO = True    # −4 na CD: golpe da ficha, já usado com sucesso
GOLPE_IMPROVISO = False    # +4 na CD: combo montado na hora (exclui o −4)
GOLPE_MOD_DANO = True      # +2 na CD se sofreu dano desde a última rodada
GOLPE_MOD_PREP = False     # −2 na CD se teve rodada limpa de preparação
                           # (default OFF: o motor não modela ação de preparação)


# ---------------------------------------------------------------------------
# ███ DÉCIMA NONA — A REGRA NOVA DA DECISÃO 240 ███
# ---------------------------------------------------------------------------
# "18a" — `CD = 12 + 2 × nGu`, rolagem `d20 + AST + B` (a regra até 2026-09-01)
# "240" — `CD = 10 + nGu`, rolagem `d20 + AST + rank` (domínio = 0 na fase
#         mortal; ver a derivação no cabeçalho — é a única leitura que reproduz
#         os 85% e os 40% que a nota publica).
GOLPE_REGRA = "18a"


def set_golpe_regra(regra="18a"):
    global GOLPE_REGRA
    GOLPE_REGRA = regra


def _cd_base(n_gu):
    """A CD crua, antes dos quatro modificadores."""
    return (10 + n_gu) if GOLPE_REGRA == "240" else (12 + 2 * n_gu)


def set_golpe_teste(publicado=False, registrado=True, improviso=False,
                    mod_dano=True, mod_prep=False):
    global GOLPE_TESTE_PUBLICADO, GOLPE_REGISTRADO, GOLPE_IMPROVISO
    global GOLPE_MOD_DANO, GOLPE_MOD_PREP
    GOLPE_TESTE_PUBLICADO = publicado
    GOLPE_REGISTRADO = registrado
    GOLPE_IMPROVISO = improviso
    GOLPE_MOD_DANO = mod_dano
    GOLPE_MOD_PREP = mod_prep


def _cd_conjuracao(pc, cd):
    """A CD depois dos modificadores publicados. NÃO consome rolagem — por isso
    a heurística pode usá-la para calcular `p` sem desalinhar nada."""
    if not GOLPE_TESTE_PUBLICADO and GOLPE_REGRA != "240":
        return cd
    if GOLPE_IMPROVISO:
        cd += 4
    elif GOLPE_REGISTRADO:
        cd -= 4
    if GOLPE_MOD_DANO and pc.get("dano_recente"):
        cd += 2
    if GOLPE_MOD_PREP and pc.get("prep_limpa"):
        cd -= 2
    return cd


def _bonus_conjuracao(pc):
    """Regra 240: `AST + rank + nível de domínio`, com domínio = 0 na fase
    mortal (o rank é que faz o papel de "o personagem cresce" — somar o `B` por
    cima contaria a progressão duas vezes, e daria 100%, número que a nota não
    publica). Regra 18ª: `AST + domínio`, com domínio = `B`."""
    if GOLPE_REGRA == "240":
        return pc["AST"] + pc["rank"]
    return pc["AST"] + (pc["B"] if GOLPE_TESTE_PUBLICADO else 0)


def _p_conjuracao(pc, n_gu):
    """Probabilidade determinística de o teste passar (sem rolar nada)."""
    cd = _cd_conjuracao(pc, _cd_base(n_gu))
    return min(1.0, max(0.0, (21 - (cd - _bonus_conjuracao(pc))) / 20))


def _conjuracao(pc, cd):
    """Devolve (teste, cd) segundo o modo escolhido. Consome UMA rolagem nos
    dois modos, então trocar de modo não desalinha o fluxo aleatório."""
    teste = random.randint(1, 20) + _bonus_conjuracao(pc)
    return teste, _cd_conjuracao(pc, cd)


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

    # DÉCIMA SÉTIMA: Níveis de Potência que a FICHA concede rank a rank (a
    # escada de Gu Wu Xing 🔨amplifica da Lee). Cai no escalar quando ausente.
    nb_rank = b.get("nivel_bonus_rank")
    nivel_bonus = (nb_rank.get(rank, 0) if nb_rank else b.get("nivel_bonus", 0))

    if name == "Lee" and terreno_delta:
        dom_bonus = max(0, dom_bonus + terreno_delta)

    vit_max = (18 + 3 * b["CON"] + 4 * dom_bonus) * M
    alma_max = alma_bar_pc(b["VON"], dom_bonus, M)
    ess_max = b["aptidao"] * 4 * (2 ** (stage_idx - 1))

    return dict(
        name=name, side="pc", rank=rank, M=M, B=dom_bonus, dado=dado,
        pool_mult=pool_mult,
        FOR=b["FOR"], CON=b["CON"], DES=b["DES"], AST=b["AST"], VON=b["VON"],
        CAR=b["CAR"], atk_attr=b["atk_attr"], alma_dmg=b["alma_dmg"],
        ess_mod=b["ess_mod"], raw_die=b["raw_die"], role=b["role"],
        vit=vit_max, vit_max=vit_max, alma=alma_max, alma_max=alma_max,
        essence=ess_max, ess_max=ess_max,
        nivel_bonus=nivel_bonus,
        alma_frac=b.get("alma_frac", 1.0 if b["alma_dmg"] else 0.0),
        rd=RD_MULT * (1 + rd_face_bonus(dom_bonus)) * M,
        defense=10 + b["DES"] + 2 * rank,
        alma_def=alma_def_pc(b["VON"], rank),
        vazamento=False, skip_turns=0, fallback_raw=False,
        used_golpe=False, actions=1, alive=True,
        cura_usada=False,
        # DÉCIMA OITAVA (bug 1): os dois modificadores dinâmicos do teste de
        # conjuração. Marcar/limpar flag não consome rolagem nenhuma.
        dano_recente=False, prep_limpa=False, golpes_disparados=0,
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
    alma_bar = alma_bar_molde(round(alma_ratio * vit))
    return dict(
        name=name, side="enemy", rank=rank, M=M, B=grau, dado=dado,
        pool_mult=pool_mult,
        vit=vit, vit_max=vit, alma=alma_bar, alma_max=alma_bar,
        essence=None, ess_max=None,
        rd=RD_MULT * rd_mult * M, defense=defense + rank, alma_def=alma_def_molde(rank),
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


def pc_attack_dmg(pc, crit=False, dado_override=None):
    n = pc["M"] * pc.get("pool_mult", 1) * (2 if crit else 1)
    dado, extra_b = apply_niveis(dado_override if dado_override else pc["dado"],
                                 NIVEL_DELTA + pc.get("nivel_bonus", 0))
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

    # --- A MOEDA 80:20 (décima sexta) ---------------------------------------
    # Com `alma_frac >= 1` NENHUMA rolagem nova é consumida: o fluxo aleatório
    # fica bit-a-bit igual ao das quinze rodadas anteriores, e por isso o
    # perfil "puro Alma" reproduz os números publicados.
    if not pc["alma_dmg"] or used_raw:
        alma_shot = False
    elif pc.get("alma_frac", 1.0) >= 1.0:
        alma_shot = True
    else:
        alma_shot = random.random() < pc["alma_frac"]

    def_val = target["alma_def"] if (alma_shot and target.get("alma_def") is not None) else target["defense"]
    hit = crit or acerto >= def_val

    if not hit:
        return False

    if used_raw:
        dmg = pc_raw_dmg(pc)
        dmg = apply_rd(dmg, target.get("rd", 0), 1)
        pool_name = "vit"
    elif alma_shot and target.get("alma") is not None:
        dmg, n = pc_attack_dmg(pc, crit, dado_override=alma_dado())
        dmg = aplica_rd_alma(dmg, target, pc["M"])
        pool_name = "alma"
    else:
        dmg, n = pc_attack_dmg(pc, crit)
        dmg = apply_rd(dmg, target.get("rd", 0), pc["M"])
        pool_name = "vit"

    if pool_name == "alma" and target.get("alma") is None:
        pool_name = "vit"

    # instrumentação da décima sexta: quinhão de dano por PJ e por trilho
    if DMG_TRACK is not None:
        DMG_TRACK[pc["name"]][pool_name] += dmg

    # DÉCIMA OITAVA (bug 1): o `+2 se sofreu dano desde a última rodada`. Em
    # duelo o alvo de um PJ é outro PJ, então a marca nasce aqui também.
    if target.get("side") == "pc" and dmg > 0:
        target["dano_recente"] = True

    target[pool_name] -= dmg
    max_pool = target[pool_name + "_max"]

    downed = False
    if target[pool_name] <= 0:
        downed = True
    elif crit and max_pool and target[pool_name] <= 0.25 * max_pool:
        apply_fratura(target)

    # sensibilidade: o atrito do degrau d8 (ver `bateria_sensibilidade`).
    # Com LUA_ATRITO_P = 0 (o default) nenhuma rolagem é consumida.
    if (not downed and not alma_shot and not used_raw and LUA_ATRITO_P > 0
            and pc.get("dado") == 8 and random.random() < LUA_ATRITO_P):
        apply_controle(target, turns=1)

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

    target["dano_recente"] = True
    n = enemy["M"] * enemy.get("pool_mult", 1) * (2 if crit else 1)
    dado = dado_override or enemy["dado"]
    dado, extra_b = apply_niveis(dado)
    dmg = roll_pool(n, dado) + enemy["M"] * (enemy.get("B", 0) + extra_b)

    if alma_shot:
        pool = "alma"
        dmg = aplica_rd_alma(dmg, target, enemy["M"])
    else:
        pool = "vit"
        bruto = dmg
        dmg = apply_rd(dmg, target.get("rd", 0), enemy["M"])
        if target["side"] == "pc":
            RD_STATS["hits"] += 1
            RD_STATS["bruto"] += bruto
            RD_STATS["liquido"] += dmg
            if target.get("rd", 0) > 0 and dmg <= enemy["M"]:
                RD_STATS["clamped"] += 1

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
# ---------------------------------------------------------------------------
# ███ BUG 3 — O GATILHO DO GOLPE MATADOR VIRA DECISÃO ECONÔMICA ███
# ---------------------------------------------------------------------------
# Ver o cabeçalho para a heurística inteira e a citação da regra. Nada aqui
# consome rolagem: ligar/desligar o gatilho não desalinha o fluxo aleatório.
#
#   "chefe"     — o gatilho das 17 rodadas (`boss is not None`)
#   "economico" — a conta da regra, feita na hora
GOLPE_GATILHO = "chefe"
GOLPE_QUEM = ("Xie Lang",)      # quem tem Golpe Matador registrado modelado
GOLPE_DISPAROS = None           # instrumentação: {nome: nº de disparos}


def set_golpe_gatilho(modo="chefe", quem=("Xie Lang",)):
    global GOLPE_GATILHO, GOLPE_QUEM
    GOLPE_GATILHO = modo
    GOLPE_QUEM = tuple(quem)


def reset_golpe_disparos(on=True):
    global GOLPE_DISPAROS
    GOLPE_DISPAROS = ({n: [0, 0] for n in PCS_BASE} if on else None)  # [cenas, disparos]


def _hibrido_mult(pc):
    """A dobra de híbrido só existe para quem monta o golpe com dois Caminhos.
    Na mesa, é o Xie Lang (Lua + Alma) — e é dela que a decisão 233 o isenta.
    Lee (Wu Xing = um Caminho só), Jiāotáng e Demvi montam de um Caminho só."""
    return XIE_HIBRIDO_MULT if pc["name"] == "Xie Lang" else 1.0


def _n_gu_golpe(pc):
    apoios = (SOLO_APOIOS_MAX[pc["B"]] if pc["B"] in SOLO_APOIOS_MAX
              else SOLO_APOIOS_MAX[max(STAGE_B.values())])
    return apoios, apoios + 1


def _custo_golpe(pc):
    _apoios, n_gu = _n_gu_golpe(pc)
    return ACT_COST_BASE * (n_gu ** 2) * _hibrido_mult(pc)


def _e_dano_pool(pc, apoios, alma):
    """Dano MÉDIO de um golpe do PJ (determinístico). Espelha `pc_attack_dmg` e
    o corpo do Golpe Matador — sem o teste de acerto, que se cancela na conta."""
    base = alma_dado() if alma else pc["dado"]
    dado, extra_b = apply_niveis(base, NIVEL_DELTA + pc.get("nivel_bonus", 0))
    n = pc["M"] * pc.get("pool_mult", 1)
    d = n * (dado + 1) / 2.0 + pc["M"] * (pc["B"] + apoios + extra_b)
    if apoios == 0 and not alma and pc["atk_attr"] == "FOR":
        d += pc["FOR"]                       # o `+ FOR` só existe no melee comum
    return d


def _e_dano_normal(pc, alvo):
    """Mistura 80:20 quando o PJ tem `alma_frac` (o Xie Lang)."""
    frac = pc.get("alma_frac", 1.0 if pc["alma_dmg"] else 0.0)
    tem_alma = alvo.get("alma") is not None
    if not pc["alma_dmg"] or not tem_alma:
        return _e_dano_pool(pc, 0, False)
    return (1 - frac) * _e_dano_pool(pc, 0, False) + frac * _e_dano_pool(pc, 0, True)


# ---------------------------------------------------------------------------
# ███ DÉCIMA NONA — A HEURÍSTICA POR AÇÃO ███
# ---------------------------------------------------------------------------
# "essencia"  — a da 18ª: horizonte = quantas rodadas o PJ SOZINHO levaria para
#               derrubar a barra. Com esse horizonte o ataque comum sempre
#               alcança a barra inteira e disparar só pode perder. É o eixo
#               errado, mantido como linha de comparação.
# "acao"      — o horizonte é o da CENA: o alvo cai quando o GRUPO o derruba.
#               É o default desta rodada.
# "acao_pura" — a regra de bolso da nota ao pé da letra: dispara sse
#               `p × util(e_golpe) > util(e_norm)` ("este alvo merece a minha
#               ação?"), sem horizonte nenhum.
GOLPE_HEURISTICA = "essencia"


def set_golpe_heuristica(modo="essencia"):
    global GOLPE_HEURISTICA
    GOLPE_HEURISTICA = modo


def _horizonte_cena(pc, alvo, rodada, pcs):
    """AÇÕES que este PJ ainda terá nesta cena contra este alvo.

    A 18ª usava `⌈barra / e_norm⌉` — o horizonte SOLO. Numa cena de grupo o alvo
    cai quando os QUATRO o derrubam, e é esse o número de ações que existe de
    verdade. Sem `pcs` (uso analítico) o horizonte volta a ser o solo, e isso
    fica dito onde a bateria imprime."""
    restantes = MAX_ROUNDS - rodada
    vivos = [q for q in (pcs or [pc]) if q is pc or pc_alive(q)]
    e_grupo = 0.0
    for q in vivos:
        e_grupo += (max(0.0, (q["raw_die"] + 1) / 2.0 + q["FOR"])
                    if q["fallback_raw"] else _e_dano_normal(q, alvo))
    e_grupo = max(1e-9, e_grupo)
    return max(1, min(restantes, math.ceil(max(0.0, alvo["vit"]) / e_grupo)))


def vale_o_golpe(pc, alvo, rodada, pcs=None):
    """A HEURÍSTICA — ver o cabeçalho. Devolve True/False sem rolar nada."""
    if pc["fallback_raw"] or pc["essence"] is None:
        return False
    custo = _custo_golpe(pc)
    if pc["essence"] < custo:
        return False
    apoios, n_gu = _n_gu_golpe(pc)
    p = _p_conjuracao(pc, n_gu)
    if p <= 0:
        return False

    usa_alma = pc["alma_dmg"] and alvo.get("alma") is not None
    barra = (alvo["alma"] if usa_alma else alvo["vit"])
    if barra <= 0:
        return False

    e_norm = max(1e-9, _e_dano_normal(pc, alvo))
    e_golpe = _e_dano_pool(pc, apoios, usa_alma)
    e_cru = max(0.0, (pc["raw_die"] + 1) / 2.0 + pc["FOR"])
    custo_atq = ACT_COST_BASE * pc["ess_mod"]

    def util(x):
        return min(barra, x)

    # ▸ A regra de bolso da decisão 240, ao pé da letra.
    if GOLPE_HEURISTICA == "acao_pura":
        return p * util(e_golpe) > util(e_norm)

    if GOLPE_HEURISTICA == "acao":
        r = _horizonte_cena(pc, alvo, rodada, pcs)
    else:                                   # "essencia" — o horizonte da 18ª
        r = min(MAX_ROUNDS - rodada, math.ceil(barra / e_norm))
    if r < 1:
        return False

    dano_a = util(min(r, pc["essence"] / custo_atq) * e_norm)
    resto = max(0, r - 1)
    atq_b = min(resto, max(0.0, pc["essence"] - custo) / custo_atq)
    dano_b = (p * util(e_golpe + atq_b * e_norm)
              + (1 - p) * util(resto * e_cru))
    return dano_b > dano_a


def golpe_matador_xie(xie, boss):
    apoios, n_gu = _n_gu_golpe(xie)
    # `(soma das ativações = 40 × n_gu) × n_gu × dobra de híbrido`. A décima
    # sétima parametriza a dobra: 2,0 é a regra, 1,0 é a isenção da decisão 233.
    custo = ACT_COST_BASE * (n_gu ** 2) * _hibrido_mult(xie)
    if xie["essence"] < custo:
        return
    xie["essence"] -= custo
    xie["golpes_disparados"] += 1
    if GOLPE_DISPAROS is not None:
        GOLPE_DISPAROS[xie["name"]][1] += 1
    cd = _cd_base(n_gu)
    teste, cd = _conjuracao(xie, cd)
    if teste >= cd:
        # A MOEDA 80:20 vale também para o Golpe Matador (escolha declarada no
        # cabeçalho): 20% dele é um golpe de Alma, 80% um golpe de Lua.
        if xie.get("alma_frac", 1.0) >= 1.0:
            golpe_alma = True
        else:
            golpe_alma = random.random() < xie["alma_frac"]
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = (acerto_roll + xie[xie["atk_attr"]] + 2 * xie["rank"]
                  + 2 + treino_pj(xie["rank"]))
        usa_alma = golpe_alma and boss.get("alma") is not None
        def_val = boss["alma_def"] if usa_alma else boss["defense"]
        if crit or acerto >= def_val:
            n = xie["M"] * xie.get("pool_mult", 1) * (2 if crit else 1)
            base_dado = alma_dado() if usa_alma else xie["dado"]
            dado, extra_b = apply_niveis(base_dado, NIVEL_DELTA + xie.get("nivel_bonus", 0))
            dmg = roll_pool(n, dado) + xie["M"] * (xie["B"] + apoios + extra_b)
            if usa_alma:
                boss["alma"] -= aplica_rd_alma(dmg, boss, xie["M"])
                if boss["alma"] > 0 and crit and boss["alma"] <= 0.25 * boss["alma_max"]:
                    apply_fratura(boss)
            else:
                dmg = apply_rd(dmg, boss.get("rd", 0), xie["M"])
                boss["vit"] -= dmg
    else:
        xie["fallback_raw"] = True
        if cd - teste >= 5:
            xie["vit_max"] = round(xie["vit_max"] * _corte_retrocesso_xie(xie))
            xie["vit"] = min(xie["vit"], xie["vit_max"])


def golpe_matador_coletivo(pcs, boss):
    participants = [p for p in pcs if pc_alive(p)]
    if len(participants) < 2 or boss is None or not enemy_alive(boss):
        return False

    nucleo = next((p for p in participants if p["name"] == "Xie Lang"), participants[0])
    apoios_outros = len(participants) - 1
    bonus_levels = {1: 3, 2: 5, 3: 6}.get(apoios_outros, 3 + apoios_outros)
    n_gu_cd = {2: 2, 3: 3, 4: 5}.get(len(participants), len(participants) + 1)
    cd = _cd_base(n_gu_cd) - 2

    base_shares = {p["name"]: ACT_COST_BASE * p["ess_mod"] for p in participants}
    total_base = sum(base_shares.values())
    n_gu_custo = len(participants)
    custo_total = total_base * n_gu_custo * 2

    if sum(p["essence"] for p in participants) < custo_total:
        return False

    for p in participants:
        share = base_shares[p["name"]] / total_base
        p["essence"] = max(0, p["essence"] - custo_total * share)

    teste, cd = _conjuracao(nucleo, cd)
    if teste >= cd:
        if nucleo.get("alma_frac", 1.0) >= 1.0:
            golpe_alma = True
        else:
            golpe_alma = random.random() < nucleo["alma_frac"]
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = (acerto_roll + nucleo["VON"] + 2 * nucleo["rank"] + 2
                  + treino_pj(nucleo["rank"]))
        usa_alma = golpe_alma and boss.get("alma") is not None
        def_val = boss["alma_def"] if usa_alma else boss["defense"]
        if crit or acerto >= def_val:
            n = nucleo["M"] * nucleo.get("pool_mult", 1) * (2 if crit else 1)
            base_dado = alma_dado() if usa_alma else nucleo["dado"]
            dado, extra_b = apply_niveis(base_dado, NIVEL_DELTA + nucleo.get("nivel_bonus", 0))
            dmg = roll_pool(n, dado) + nucleo["M"] * (nucleo["B"] + bonus_levels + extra_b)
            if usa_alma:
                boss["alma"] -= aplica_rd_alma(dmg, boss, nucleo["M"])
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
def pc_turn(pc, pcs, enemies, boss, rodada=0):
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

    # ▸ BUG 3: o gatilho do Golpe Matador. "chefe" é o das 17 rodadas;
    #   "economico" é a conta da regra, aplicada ao alvo que o PJ escolheria.
    if GOLPE_GATILHO == "chefe":
        if (pc["name"] == "Xie Lang" and boss is not None and enemy_alive(boss)
                and not pc["used_golpe"]):
            pc["used_golpe"] = True
            golpe_matador_xie(pc, boss)
            pc["dano_recente"] = False
            return
    elif pc["name"] in GOLPE_QUEM and not pc["used_golpe"]:
        alvo = boss if (boss is not None and enemy_alive(boss)) else pick_weakest(enemies)
        if alvo is not None and vale_o_golpe(pc, alvo, rodada, pcs):
            pc["used_golpe"] = True
            golpe_matador_xie(pc, alvo)
            pc["dano_recente"] = False
            return

    target = pick_weakest(enemies)
    if target is None:
        return
    downed = resolve_pc_hit(pc, target)
    if downed and not target.get("is_horda"):
        target["alive"] = False
    pc["dano_recente"] = False


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
                dado_override = alma_dado()   # décima sexta: o nerf vale para os dois lados
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
                pc_turn(entity, pcs, enemies,
                        boss if golpe_mode == "solo" else None, rodada=rnd)
            else:
                enemy_turn(entity, pcs, enemies)
                update_horda_members(entity)
        rounds_used = rnd + 1

    if GOLPE_DISPAROS is not None:
        for p in pcs:
            GOLPE_DISPAROS[p["name"]][0] += 1

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
            # DÉCIMA SÉTIMA: com `GOLPE_EM_DUELO` o oponente faz as vezes de
            # Chefe e o Golpe Matador dispara (uma vez, `used_golpe`). Desligado
            # — o default —, `None` reproduz as dezesseis rodadas bit-a-bit.
            # DÉCIMA OITAVA: com o gatilho econômico o duelo NÃO precisa mais de
            # `GOLPE_EM_DUELO` — `pick_weakest` acha o oponente sozinho e a conta
            # decide. `GOLPE_EM_DUELO` continua valendo só no gatilho "chefe".
            pc_turn(p, [p], [opp], opp if GOLPE_EM_DUELO else None, rodada=rnd)
        if not pc_alive(a) or not pc_alive(b):
            if GOLPE_DISPAROS is not None:
                GOLPE_DISPAROS[a["name"]][0] += 1
                GOLPE_DISPAROS[b["name"]][0] += 1
            winner = a if pc_alive(a) else (b if pc_alive(b) else None)
            return winner, rnd + 1
    if GOLPE_DISPAROS is not None:
        GOLPE_DISPAROS[a["name"]][0] += 1
        GOLPE_DISPAROS[b["name"]][0] += 1
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


# ===========================================================================
# ███  MOTOR DE TRIBULAÇÃO  ███  (novo nesta rodada — nunca existiu em código)
# ===========================================================================
# Fontes, todas já publicadas:
#   [[🌩️ Calamidades e Provações]] — as 5 etapas, a CD, as reduções, a tabela
#       de sucessos, `M d6` por etapa falhada, 1 natural = duas falhas.
#   [[⛈️ A Vontade do Céu]] — Contador de Ameaça, faixas, Fichas de Azar.
#   [[🗝️ Terra Abençoada]] — Ferimentos da Terra (4 níveis), reparo 50 UV +
#       3 meses internos por nível, tanque de Essência Imortal DA TERRA.
#   [[🌾 Ecologia...]] — `1d6` de dano colateral por ETAPA falhada.
#   [[☯️ Marcas de Dao]] — rendimento por evento, escada de domínio, tetos.
# ---------------------------------------------------------------------------

# --- faixas do Contador de Ameaça Celestial --------------------------------
FAIXAS = ("Ignorado", "Notado", "Marcado", "Perseguido", "Alvo do Céu")
FAIXA_CD = {"Ignorado": 0, "Notado": 1, "Marcado": 2, "Perseguido": 3,
            "Alvo do Céu": 5}
FAIXA_FICHAS = {"Ignorado": 0, "Notado": 1, "Marcado": 2, "Perseguido": 3,
                "Alvo do Céu": 4}
# A fórmula RIVAL (⛈️ l.109) só define base pra Marcado/Perseguido/Alvo.
# Abaixo de Marcado ela é indefinida; adotamos 14 (a leitura caridosa: a
# mesma base do primeiro degrau definido). Isso está no relatório.
FAIXA_CD_BASE_RIVAL = {"Ignorado": 14, "Notado": 14, "Marcado": 14,
                       "Perseguido": 18, "Alvo do Céu": 22}


def faixa_de_cac(cac):
    if cac >= 80:
        return "Alvo do Céu"
    if cac >= 50:
        return "Perseguido"
    if cac >= 25:
        return "Marcado"
    if cac >= 10:
        return "Notado"
    return "Ignorado"


# --- escada de domínio (☯️ Marcas de Dao) ----------------------------------
def dominio_de(marcas):
    """Devolve (bônus de Nível, nome). É o `+N Níveis` da escada de domínio."""
    if marcas >= 300000:
        return 5, "Grande Mestre Supremo"
    if marcas >= 150000:
        return 4, "Quase-Supremo"
    if marcas >= 50000:
        return 3, "Grão-Mestre"
    if marcas >= 10000:
        return 2, "Mestre"
    if marcas >= 1000:
        return 1, "Pequeno Feito"
    return 0, "Vislumbre"


# A decisão 218 REVOGOU os tetos duros (9.999 / 99.999 / 299.999): as faixas
# viraram descritivas e dá pra passar do topo continuando no mesmo rank — o
# preço do excesso é exatamente o escalonamento de Calamidade medido na T4.
# `TETO_MARCAS` sobrevive só como o ponto de parada da carreira da T1 (que é
# "até 10.000 Marcas", o topo da faixa do rank 6), pra bater com a 4ª rodada.
TETO_MARCAS = {6: 9999, 7: 99999, 8: 299999, 9: None}
# o topo da FAIXA do rank, do qual o excesso é medido (decisão 218)
BANDA_MARCAS = {6: 10000, 7: 100000, 8: 300000}

# --- rendimento por evento (☯️ Marcas de Dao) -------------------------------
RENDIMENTO = {
    "terrestre": (200, 500),
    "provacao": (1000, 2000),
    "grande": (6000, 8500),
    "dez_mil": (75000, 100000),
    "caos": (30000, 60000),
}
# etapas por evento — Terrestre pula as duas etapas sob medida (2 e 4)
ETAPAS_EVENTO = {
    "terrestre": (1, 3, 5),
    "provacao": (1, 2, 3, 4, 5),
    "grande": (1, 2, 3, 4, 5),
    "dez_mil": (1, 2, 3, 4, 5),
    "caos": (1, 2, 3, 4, 5),
}
# a "categoria acima" que o escalonamento por excesso invoca
CATEGORIA_ACIMA = {"terrestre": "provacao", "provacao": "grande",
                   "grande": "dez_mil", "dez_mil": "caos", "caos": "caos"}


# --- fichas dos personagens usados na tribulação ---------------------------
# O "Imortal comum" é a ficha genérica de 12 pontos usada pra reproduzir a
# quarta rodada; os quatro PJs vêm de PCS_BASE (as fichas publicadas).
FICHA_GENERICA = dict(FOR=1, CON=3, DES=2, AST=2, VON=3, CAR=1)


def ficha_tribulacao(nome):
    if nome == "Imortal comum":
        return dict(FICHA_GENERICA)
    b = _PCS_ORIG[nome]
    return {a: b[a] for a in ("FOR", "CON", "DES", "AST", "VON", "CAR")}


def atributo_da_etapa(ficha, etapa, dom_bonus):
    """1 CON · 2 VON · 3 o atributo MAIS BAIXO · 4 AST · 5 VON + domínio."""
    if etapa == 1:
        return ficha["CON"]
    if etapa == 2:
        return ficha["VON"]
    if etapa == 3:
        return min(ficha.values())
    if etapa == 4:
        return ficha["AST"]
    return ficha["VON"] + dom_bonus


# --- a CD: as DUAS fórmulas em disputa -------------------------------------
def cd_sequencia(rank, faixa, evento, formula="rank", excesso_cd=0):
    """Devolve a CD-base de cada etapa da sequência (antes das reduções).

    formula='rank'   → 🌩️ Calamidades l.49: 14 + 2×(rank−6) + faixa (+2 se
                       Provação ou acima). ESCALA POR RANK.
    formula='faixa'  → ⛈️ Vontade do Céu l.109: base 14/18/22 pela faixa,
                       "mais os bônus de CD da tabela de faixas" — ou seja, a
                       faixa entra DUAS VEZES e o rank não entra nenhuma.
    formula='faixa3' → a leitura ESCOPADA da mesma linha: a base por faixa
                       vale só para a etapa 3 (o "teste central" da Tribulação
                       sob medida que aquela seção descreve); o resto segue a
                       fórmula de rank.
    """
    provacao = evento != "terrestre"
    por_rank = 14 + 2 * (rank - 6) + FAIXA_CD[faixa] + (2 if provacao else 0)
    por_faixa = (FAIXA_CD_BASE_RIVAL[faixa] + FAIXA_CD[faixa]
                 + (2 if provacao else 0))
    etapas = ETAPAS_EVENTO[evento]
    if formula == "rank":
        base = {e: por_rank for e in etapas}
    elif formula == "faixa":
        base = {e: por_faixa for e in etapas}
    elif formula == "faixa3":
        base = {e: por_rank for e in etapas}
        if 3 in base:
            base[3] = por_faixa
    else:
        raise ValueError(formula)
    return {e: v + excesso_cd for e, v in base.items()}


# --- o escalonamento por excesso de Marcas (proposta da sessão paralela) ----
def escalonamento(marcas, rank):
    """(+CD, categoria_acima?, ferimento_auto_por_falha?, cadencia_dobrada?)"""
    banda = BANDA_MARCAS.get(rank)
    if banda is None or marcas <= banda:
        return 0, False, False, False
    exc = (marcas - banda) / banda
    if exc <= 0.10:
        return 1, False, False, False
    if exc <= 0.25:
        return 2, True, False, False
    if exc <= 0.50:
        return 4, False, True, False
    return 6, False, False, True


# --- uma sequência de tribulação -------------------------------------------
def rola_etapa(mod, cd, vantagem, ficha_azar):
    """Devolve (sucesso, falhas_extras, usou_ficha).

    `falhas_extras` = 1 se o dado guardado foi 1 natural (conta como DUAS
    falhas, igual à provação da Ascensão). A Ficha de Azar é jogada só contra
    um SUCESSO, e joga a opção que a nota da Vontade do Céu autoriza:
    converter sucesso marginal (margem ≤ 2) em falha; senão, rerrolar e ficar
    com o pior dos dois.
    """
    d = random.randint(1, 20)
    if vantagem:
        d = max(d, random.randint(1, 20))
    total = d + mod
    sucesso = total >= cd
    usou = False
    if sucesso and ficha_azar:
        usou = True
        if total - cd <= 2:
            sucesso = False                      # sucesso marginal vira falha
        else:
            d2 = random.randint(1, 20)
            d = min(d, d2)                       # rerrola, fica com o pior
            total = d + mod
            sucesso = total >= cd
    return sucesso, (1 if d == 1 else 0), usou


def resolve_sequencia(ficha, rank, marcas, evento, faixa,
                      gu_estabilizacao=False, pressagios=0, inabalavel=False,
                      aliado=False, formula="rank", excesso_cd=0,
                      fisico_extremo=False):
    """Roda a sequência inteira e devolve o dicionário de resultado.

    NUNCA se para no meio: todas as etapas são roladas (regra explícita).
    """
    dom_bonus, _ = dominio_de(marcas)
    etapas = ETAPAS_EVENTO[evento]
    cds = cd_sequencia(rank, faixa, evento, formula, excesso_cd)
    if fisico_extremo:
        cds = {e: v + 5 for e, v in cds.items()}

    # reduções de sequência inteira
    red_seq = (3 if gu_estabilizacao else 0)
    if inabalavel and evento == "terrestre":
        red_seq += 2

    # os presságios: −2 em UMA etapa cada. Jogo ótimo = gastar nas etapas mais
    # difíceis (maior CD efetiva menos modificador).
    mods = {e: atributo_da_etapa(ficha, e, dom_bonus) for e in etapas}
    dificuldade = sorted(etapas, key=lambda e: (cds[e] - red_seq) - mods[e],
                         reverse=True)
    alvo_pressagio = set(dificuldade[:min(pressagios, len(etapas))])
    # a vantagem do aliado vai na etapa mais difícil que sobrou (ou na pior)
    alvo_vantagem = dificuldade[0] if aliado else None

    fichas = FAIXA_FICHAS[faixa]
    sucessos = 0
    falhas_extras = 0
    etapas_falhadas = 0
    for e in etapas:
        cd = cds[e] - red_seq - (2 if e in alvo_pressagio else 0)
        ok, extra, usou = rola_etapa(mods[e], cd, e == alvo_vantagem,
                                     fichas > 0)
        if usou:
            fichas -= 1
        if ok:
            sucessos += 1
        else:
            etapas_falhadas += 1
        falhas_extras += extra

    sucessos_efetivos = max(0, sucessos - falhas_extras)
    n = len(etapas)

    # --- tabela de resultado -----------------------------------------------
    morte = False
    gu_morto = False
    if n == 3:
        if sucessos_efetivos >= 3:
            frac = 1.0
        elif sucessos_efetivos == 2:
            frac = 2 / 3
        else:
            frac = 0.0
            gu_morto = sucessos_efetivos == 0
    else:
        if sucessos_efetivos >= 5:
            frac = 1.0
        elif sucessos_efetivos == 4:
            frac = 4 / 5
        elif sucessos_efetivos == 3:
            frac = 3 / 5
        elif sucessos_efetivos == 2:
            frac = 0.0
        else:
            frac = 0.0
            morte = True

    falhou = frac == 0.0
    lo, hi = RENDIMENTO[evento]
    bruto = random.randint(lo, hi) * (2 if fisico_extremo else 1)
    ganho = int(bruto * frac)

    # --- dano no trilho: M d6 por ETAPA falhada ----------------------------
    M = M_TABLE[rank]
    dano = sum(roll_pool(M, 6) for _ in range(etapas_falhadas))

    # --- colateral 1d6 por ETAPA falhada, mesmo passando -------------------
    n_colat = etapas_falhadas
    if inabalavel and n_colat:
        n_colat -= 1                     # Inabalável ignora a primeira rolagem
    colaterais = [random.randint(1, 6) for _ in range(max(0, n_colat))]

    return dict(sucessos=sucessos_efetivos, etapas=n, etapas_falhadas=etapas_falhadas,
                falhou=falhou, morte=morte, gu_morto=gu_morto, frac=frac,
                marcas=ganho, dano=dano, colaterais=colaterais,
                cd_media=sum(cds.values()) / n, dom_bonus=dom_bonus,
                cac_pago=(-5 if (n == 5 and sucessos_efetivos >= 5) else 0))


# --- um evento completo, com a contabilidade da terra ----------------------
UV_REPARO_POR_NIVEL = 50           # 🗝️ Terra Abençoada: 50 UV + 3 meses/nível
TANQUE_UV_R6 = {"Mesquinha": 200, "Comum": 400, "Boa": 600,
                "Excelente": 800, "Especial": 1200}


def tanque_uv(qualidade, rank):
    return TANQUE_UV_R6[qualidade] * (2 ** (rank - 6))


def evento_completo(ficha, rank, marcas, evento, faixa, prep,
                    formula="rank", marcas_para_escalonar=None,
                    fisico_extremo=False, estabilidade="Firme"):
    """Uma Calamidade, do presságio à conta do reparo.

    `prep` = dict(gu_estabilizacao, pressagios, inabalavel, aliado).
    """
    base_marcas = marcas if marcas_para_escalonar is None else marcas_para_escalonar
    exc_cd, cat_acima, fer_auto, cad_dobrada = escalonamento(base_marcas, rank)
    ev = CATEGORIA_ACIMA[evento] if cat_acima else evento

    r = resolve_sequencia(ficha, rank, marcas, ev, faixa,
                          formula=formula, excesso_cd=exc_cd,
                          fisico_extremo=fisico_extremo, **prep)

    # --- Ferimento da Terra ------------------------------------------------
    fer_terra = 1 if r["falhou"] else 0
    if fer_auto:
        fer_terra += r["etapas_falhadas"]        # banda +25-50%: automático
    if estabilidade == "Frágil":
        # toda Calamidade danifica a terra (uma camada regride) + 1 rolagem
        r["colaterais"].append(random.randint(1, 6))

    ferimento_pj = 1 if r["falhou"] else 0

    r.update(evento_real=ev, excesso_cd=exc_cd, categoria_acima=cat_acima,
             ferimento_auto=fer_auto, cadencia_dobrada=cad_dobrada,
             fer_terra=fer_terra, ferimento_pj=ferimento_pj,
             uv_reparo=fer_terra * UV_REPARO_POR_NIVEL,
             meses_reclusao=fer_terra * 3)
    return r


PREPS = {
    "despreparado": dict(gu_estabilizacao=False, pressagios=0,
                         inabalavel=False, aliado=False),
    "tipico": dict(gu_estabilizacao=True, pressagios=2,
                   inabalavel=False, aliado=False),
    "bem preparado": dict(gu_estabilizacao=True, pressagios=3,
                          inabalavel=True, aliado=True),
}


# ---------------------------------------------------------------------------
# BATERIA T1 — reprodução da QUARTA RODADA (carreira rank 6 → 10.000 Marcas)
# ---------------------------------------------------------------------------
def carreira_rank6(nome, prep, fisico=False, formula="rank",
                   cac_inicial=None, ano_max=1200, cd5_fisico=True):
    """Método transcrito da quarta rodada (Resultados, l.1461).

    Terrestre a cada 10 anos internos, Provação Celestial a cada 100.
    Marcas iniciais 850 (comum) / 1.700 (Físico). CAC inicial 3 / 15.
    Falha zera as Marcas do evento e soma 1 Ferimento e 1 Ferimento da Terra.
    Ferimento da Terra reparado a 1 nível por década. 0-1 sucessos numa
    Provação é morte. Devolve (chegou_ao_rank7, anos, marcas, causa).
    """
    ficha = ficha_tribulacao(nome)
    marcas = 1700 if fisico else 850
    cac = (15 if fisico else 3) if cac_inicial is None else cac_inicial
    fer_terra = 0
    ferimentos = 0
    uv_total = 0
    ano = 0
    falhas_seguidas = 0
    while ano < ano_max:
        ano += 10
        # o CAC sobe com as Marcas acumuladas (+5 a cada 10.000)
        cac_efetivo = cac + 5 * (marcas // 10000)
        faixa = faixa_de_cac(cac_efetivo)
        eventos = ["terrestre"]
        if ano % 100 == 0:
            eventos.append("provacao")
        for ev in eventos:
            r = evento_completo(ficha, 6, marcas, ev, faixa, prep,
                                formula=formula,
                                fisico_extremo=(fisico and cd5_fisico))
            if fisico and not cd5_fisico:
                # sem o +5 flat, mas as Marcas continuam em dobro
                r["marcas"] *= 2
            marcas = min(marcas + r["marcas"], TETO_MARCAS[6] + 1)
            fer_terra += r["fer_terra"]
            ferimentos += r["ferimento_pj"]
            cac += r["cac_pago"]
            if r["falhou"]:
                falhas_seguidas += 1
                if faixa == "Alvo do Céu" and falhas_seguidas >= 2:
                    fer_terra = max(fer_terra, 2)
            else:
                falhas_seguidas = 0
            if r["morte"]:
                return False, ano, marcas, "Provação (0-1 sucessos)", uv_total, ferimentos
            if ferimentos >= 20:
                return False, ano, marcas, "20 Ferimentos", uv_total, ferimentos
        # --- fim da década: repara 1 nível de Ferimento da Terra -----------
        if fer_terra >= 4:
            return False, ano, marcas, "Terra Colapsada", uv_total, ferimentos
        if fer_terra > 0:
            fer_terra -= 1
            uv_total += UV_REPARO_POR_NIVEL
        if marcas >= 10000:
            return True, ano, marcas, "chegou a 10.000 Marcas", uv_total, ferimentos
    return False, ano, marcas, "estourou o calendário", uv_total, ferimentos


N_CARREIRAS = 20000


def bateria_t1():
    print("=" * 112)
    print("BATERIA T1 — REPRODUÇÃO DA QUARTA RODADA (carreira do rank 6 até 10.000 Marcas)")
    print(f"{N_CARREIRAS} carreiras/célula · método transcrito de 🎯 Resultados l.1461")
    print("Alvo publicado (2026-08-28):  Imortal comum 2,2% · 48,3% · 70,2%  |  Físico 0,0% · 4,2% · 20,2%")
    print("=" * 112)
    pub = {("Imortal comum", "despreparado"): 2.2,
           ("Imortal comum", "tipico"): 48.3,
           ("Imortal comum", "bem preparado"): 70.2,
           ("Físico (+5 CD, como a 4ª)", "despreparado"): 0.0,
           ("Físico (+5 CD, como a 4ª)", "tipico"): 4.2,
           ("Físico (+5 CD, como a 4ª)", "bem preparado"): 20.2}
    print(f"  {'perfil':34s} {'preparação':16s} {'vivo r7':>9s} {'4ª rodada':>10s} "
          f"{'Δpp':>7s} {'anos int.':>10s} {'UV reparo':>10s} {'Ferim.':>7s}")
    out = {}
    perfis = (("Imortal comum", False, True),
              ("Físico (+5 CD, como a 4ª)", True, True),
              ("Físico (regra escrita: só CAC 15)", True, False))
    for perfil, fisico, cd5 in perfis:
        for prep_nome, prep in PREPS.items():
            random.seed(20260830)
            viv = 0
            anos, uvs, fers = [], [], []
            for _ in range(N_CARREIRAS):
                ok, ano, mk, causa, uv, fer = carreira_rank6(
                    "Imortal comum", prep, fisico=fisico, cd5_fisico=cd5)
                if ok:
                    viv += 1
                    anos.append(ano)
                uvs.append(uv)
                fers.append(fer)
            taxa = viv / N_CARREIRAS * 100
            ref = pub.get((perfil, prep_nome))
            out[(perfil, prep_nome)] = taxa
            manos = (sum(anos) / len(anos)) if anos else float("nan")
            reft = f"{ref:9.1f}%" if ref is not None else "        —"
            dt = f"{taxa - ref:+7.1f}" if ref is not None else "      —"
            print(f"  {perfil:34s} {prep_nome:16s} {taxa:8.1f}% {reft} "
                  f"{dt} {manos:10.0f} {sum(uvs)/len(uvs):10.0f} "
                  f"{sum(fers)/len(fers):7.2f}")
    print("\n  NOTA — o '+5 se Físico Extremo' do método da quarta rodada NÃO existe em regra")
    print("  nenhuma do vault. [[⛈️ A Vontade do Céu]] dá ao Físico um PISO de +15 no Contador,")
    print("  o que o coloca em Notado (+1 de CD), não em +5. A terceira linha mede a regra")
    print("  como está escrita hoje; a segunda reproduz o método da quarta rodada.")
    return out


# ---------------------------------------------------------------------------
# BATERIA T2 — os TRÊS CENÁRIOS do autor
# ---------------------------------------------------------------------------
CENARIOS = (
    # (rótulo, rank, marcas, evento base, faixa "orgânica")
    ("1 · r6 inicial, 1.000 Marcas", 6, 1000, "terrestre"),
    ("2 · r6 estendido, 12.000 Marcas (+20%)", 6, 12000, "terrestre"),
    ("3a · r7 inicial, 10.000 Marcas", 7, 10000, "terrestre"),
    ("3b · r7 estendido, 120.000 Marcas (+20%)", 7, 120000, "terrestre"),
    ("3c · r7 com 1.000 Marcas (leitura literal)", 7, 1000, "terrestre"),
    ("3d · r7 com 12.000 Marcas (leitura literal)", 7, 12000, "terrestre"),
)


def faixa_organica(marcas):
    """A faixa que o gatilho de Marcas sozinho produz (+5 a cada 10.000)."""
    return faixa_de_cac(5 * (marcas // 10000))


def bateria_t2(formula="rank", prep_nome="tipico", qualidade="Comum"):
    prep = PREPS[prep_nome]
    print("\n" + "=" * 124)
    print(f"BATERIA T2 — OS TRÊS CENÁRIOS (fórmula de CD '{formula}', preparação '{prep_nome}', terra {qualidade})")
    print(f"{N_ITER} iterações/célula · faixa do Contador vinda SÓ do gatilho de Marcas (+5 a cada 10.000)")
    print("=" * 124)
    print(f"  {'cenário':44s} {'PJ':10s} {'faixa':11s} {'ev.':>5s} {'CD':>5s} "
          f"{'sucesso':>8s} {'morte':>6s} {'Marcas':>8s} {'dano%':>7s} "
          f"{'Fer.PJ':>7s} {'FerTerra':>9s} {'UV':>7s} {'colat':>6s}")
    out = {}
    for rot, rank, marcas, ev in CENARIOS:
        faixa = faixa_organica(marcas)
        for nome in ["Imortal comum"] + list(PCS_BASE):
            ficha = ficha_tribulacao(nome)
            random.seed(20260830)
            ac = dict(suc=0, morte=0, marcas=0, dano=0, fer=0, ferter=0,
                      uv=0, colat=0, cd=0, etapas=0)
            dom_b, _ = dominio_de(marcas)
            M = M_TABLE[rank]
            pool = (18 + 3 * ficha["CON"] + 4 * dom_b) * M
            for _ in range(N_ITER):
                r = evento_completo(ficha, rank, marcas, ev, faixa, prep,
                                    formula=formula)
                ac["suc"] += 0 if r["falhou"] else 1
                ac["morte"] += 1 if r["morte"] else 0
                ac["marcas"] += r["marcas"]
                ac["dano"] += r["dano"]
                ac["fer"] += r["ferimento_pj"]
                ac["ferter"] += r["fer_terra"]
                ac["uv"] += r["uv_reparo"]
                ac["colat"] += len(r["colaterais"])
                ac["cd"] += r["cd_media"]
                ac["etapas"] += r["etapas"]
            k = (rot, nome)
            out[k] = {kk: v / N_ITER for kk, v in ac.items()}
            out[k]["dano_pct"] = ac["dano"] / N_ITER / pool * 100
            out[k]["faixa"] = faixa
            print(f"  {rot if nome == 'Imortal comum' else '':44s} {nome:10s} "
                  f"{faixa:11s} {ac['etapas']/N_ITER:5.1f} {ac['cd']/N_ITER:5.1f} "
                  f"{ac['suc']/N_ITER*100:7.1f}% {ac['morte']/N_ITER*100:5.1f}% "
                  f"{ac['marcas']/N_ITER:8.0f} {out[k]['dano_pct']:6.1f}% "
                  f"{ac['fer']/N_ITER:7.2f} {ac['ferter']/N_ITER:9.2f} "
                  f"{ac['uv']/N_ITER:7.1f} {ac['colat']/N_ITER:6.2f}")
    return out


def bateria_t2_calendario(formula="rank", qualidade="Comum"):
    """O que o autor pediu de verdade: dano à Fenda e gasto de UV NÃO são
    grandezas de um evento, são de um CICLO. 100 anos internos = 10 Terrestres
    (+ 1 Provação Celestial no ano 100), que é a década do calendário imortal."""
    print("\n" + "=" * 124)
    print(f"BATERIA T2b — O CICLO DE 100 ANOS INTERNOS (10 Terrestres + 1 Provação), fórmula '{formula}'")
    print(f"Tanque de Essência Imortal DA TERRA (🗝️): r6 {tanque_uv(qualidade, 6)} UV · r7 {tanque_uv(qualidade, 7)} UV (terra {qualidade})")
    print("=" * 124)
    print(f"  {'cenário':44s} {'prep':14s} {'vivo':>7s} {'Marcas':>9s} "
          f"{'FerTerra':>9s} {'pico':>5s} {'UV':>7s} {'% tanque':>9s} "
          f"{'Fer.PJ':>7s} {'meses':>6s}")
    out = {}
    for rot, rank, marcas0, ev in CENARIOS[:4]:
        for prep_nome, prep in PREPS.items():
            random.seed(20260830)
            vivos = 0
            acc = dict(marcas=0, ferter=0, pico=0, uv=0, fer=0, meses=0)
            for _ in range(N_ITER):
                ficha = ficha_tribulacao("Imortal comum")
                marcas = marcas0
                fer_terra = 0
                pico = 0
                uv = 0
                fers = 0
                meses = 0
                vivo = True
                falhas_seguidas = 0
                for ano in range(10, 101, 10):
                    cac = 5 * (marcas // 10000)
                    faixa = faixa_de_cac(cac)
                    eventos = ["terrestre"] + (["provacao"] if ano == 100 else [])
                    for e in eventos:
                        r = evento_completo(ficha, rank, marcas, e, faixa, prep,
                                            formula=formula,
                                            marcas_para_escalonar=marcas0)
                        marcas += r["marcas"]
                        fer_terra += r["fer_terra"]
                        fers += r["ferimento_pj"]
                        if r["falhou"]:
                            falhas_seguidas += 1
                            if faixa == "Alvo do Céu" and falhas_seguidas >= 2:
                                fer_terra = max(fer_terra, 2)
                        else:
                            falhas_seguidas = 0
                        pico = max(pico, fer_terra)
                        if r["morte"]:
                            vivo = False
                            break
                    if not vivo:
                        break
                    if fer_terra >= 4:
                        vivo = False
                        break
                    if fer_terra > 0:      # reparo de 1 nível por década
                        fer_terra -= 1
                        uv += UV_REPARO_POR_NIVEL
                        meses += 3
                vivos += int(vivo)
                acc["marcas"] += marcas - marcas0
                acc["ferter"] += fer_terra
                acc["pico"] += pico
                acc["uv"] += uv
                acc["fer"] += fers
                acc["meses"] += meses
            tanque = tanque_uv(qualidade, rank)
            out[(rot, prep_nome)] = {k: v / N_ITER for k, v in acc.items()}
            out[(rot, prep_nome)]["vivo"] = vivos / N_ITER
            print(f"  {rot if prep_nome == 'despreparado' else '':44s} {prep_nome:14s} "
                  f"{vivos/N_ITER*100:6.1f}% {acc['marcas']/N_ITER:9.0f} "
                  f"{acc['ferter']/N_ITER:9.2f} {acc['pico']/N_ITER:5.2f} "
                  f"{acc['uv']/N_ITER:7.0f} {acc['uv']/N_ITER/tanque*100:8.1f}% "
                  f"{acc['fer']/N_ITER:7.2f} {acc['meses']/N_ITER:6.1f}")
    return out


# ---------------------------------------------------------------------------
# BATERIA T3 — O FORK DA CD (🌩️ l.49 × ⛈️ l.109)
# ---------------------------------------------------------------------------
def bateria_t3():
    print("\n" + "=" * 120)
    print("BATERIA T3 — O FORK DA CD: as duas fórmulas do vault, medidas lado a lado")
    print("  A 'rank'   : CD = 14 + 2×(rank−6) + faixa (+2 se Provação)        — 🌩️ Calamidades l.49")
    print("  B 'faixa'  : CD = 14/14/14/18/22 pela faixa + faixa DE NOVO       — ⛈️ Vontade do Céu l.109")
    print("  C 'faixa3' : B só na etapa 3 (a leitura escopada de 'Passo 2')    — proposta de conciliação")
    print("=" * 120)
    print(f"  {'evento':10s} {'rank':>4s} {'faixa':11s} " +
          "".join(f"{f'CD {t}':>9s}{f'viv {t}':>9s}" for t in ("A", "B", "C")))
    out = {}
    prep = PREPS["bem preparado"]
    ficha = ficha_tribulacao("Imortal comum")
    for ev in ("terrestre", "provacao"):
        for rank in (6, 7, 8, 9):
            for faixa in FAIXAS:
                linha = []
                for f in ("rank", "faixa", "faixa3"):
                    random.seed(20260830)
                    marcas = {6: 5000, 7: 30000, 8: 120000, 9: 400000}[rank]
                    ok = 0
                    mortes = 0
                    cds = 0.0
                    for _ in range(N_ITER):
                        r = evento_completo(ficha, rank, marcas, ev, faixa, prep,
                                            formula=f)
                        ok += 0 if r["falhou"] else 1
                        mortes += 1 if r["morte"] else 0
                        cds += r["cd_media"]
                    out[(ev, rank, faixa, f)] = (ok / N_ITER, mortes / N_ITER,
                                                 cds / N_ITER)
                    linha.append((cds / N_ITER, ok / N_ITER * 100))
                print(f"  {ev:10s} {rank:4d} {faixa:11s} " +
                      "".join(f"{c:9.1f}{w:8.1f}%" for c, w in linha))
    print("\n  LEITURA — a Provação Celestial falhada em 0-1 sucessos é MORTE sem Teste de Morte.")
    print("  Mortalidade por Provação (bem preparado), por fórmula:")
    print(f"  {'rank':>4s} {'faixa':11s} {'A morte':>9s} {'B morte':>9s} {'C morte':>9s}")
    for rank in (6, 7, 8, 9):
        for faixa in FAIXAS:
            vals = [out[("provacao", rank, faixa, f)][1] * 100
                    for f in ("rank", "faixa", "faixa3")]
            print(f"  {rank:4d} {faixa:11s} " + "".join(f"{v:8.1f}%" for v in vals))
    return out


# ---------------------------------------------------------------------------
# BATERIA T4 — a escala de escalonamento por excesso: frouxa, certa ou brutal?
# ---------------------------------------------------------------------------
ESCALA_TESTE = (
    ("0% (no teto, sem excesso)", 10000),
    ("+8% (banda ≤+10%: +1 CD)", 10800),
    ("+20% (banda +10-25%: +2 CD e categoria acima)", 12000),
    ("+40% (banda +25-50%: +4 CD e Ferimento auto/falha)", 14000),
    ("+80% (banda >+50%: +6 CD e cadência dobrada)", 18000),
)


def bateria_t4(formula="rank"):
    print("\n" + "=" * 122)
    print("BATERIA T4 — A ESCALA DE ESCALONAMENTO POR EXCESSO DE MARCAS (proposta da sessão paralela)")
    print("Rank 6, 'Imortal comum', preparação típica. A pergunta: os degraus são frouxos, certos ou brutais?")
    print("=" * 122)
    print(f"  {'excesso':50s} {'ev.':>4s} {'CD':>5s} {'sucesso':>8s} {'morte':>7s} "
          f"{'Marcas':>8s} {'FerTerra':>9s} {'UV/evento':>10s} {'dano%':>7s}")
    prep = PREPS["tipico"]
    ficha = ficha_tribulacao("Imortal comum")
    out = {}
    for rot, marcas in ESCALA_TESTE:
        random.seed(20260830)
        ac = dict(suc=0, morte=0, marcas=0, ferter=0, uv=0, dano=0, cd=0, et=0)
        dom_b, _ = dominio_de(marcas)
        pool = (18 + 3 * ficha["CON"] + 4 * dom_b) * M_TABLE[6]
        for _ in range(N_ITER):
            r = evento_completo(ficha, 6, marcas, "terrestre", faixa_organica(marcas),
                                prep, formula=formula)
            ac["suc"] += 0 if r["falhou"] else 1
            ac["morte"] += 1 if r["morte"] else 0
            ac["marcas"] += r["marcas"]
            ac["ferter"] += r["fer_terra"]
            ac["uv"] += r["uv_reparo"]
            ac["dano"] += r["dano"]
            ac["cd"] += r["cd_media"]
            ac["et"] += r["etapas"]
        out[rot] = {k: v / N_ITER for k, v in ac.items()}
        print(f"  {rot:50s} {ac['et']/N_ITER:4.1f} {ac['cd']/N_ITER:5.1f} "
              f"{ac['suc']/N_ITER*100:7.1f}% {ac['morte']/N_ITER*100:6.1f}% "
              f"{ac['marcas']/N_ITER:8.0f} {ac['ferter']/N_ITER:9.2f} "
              f"{ac['uv']/N_ITER:10.1f} {ac['dano']/N_ITER/pool*100:6.1f}%")
    print("\n  A cadência dobrada da banda >+50% só aparece no calendário — 20 Terrestres em 100 anos:")
    print(f"  {'banda':50s} {'eventos/100a':>13s} {'FerTerra/100a':>14s} {'UV/100a':>9s} {'vivo':>7s}")
    for rot, marcas in ESCALA_TESTE:
        exc_cd, cat, fer_auto, cad = escalonamento(marcas, 6)
        n_ev = 20 if cad else 10
        random.seed(20260830)
        vivos = 0
        tot_ft = tot_uv = 0
        for _ in range(N_ITER):
            fer_terra = 0
            uv = 0
            vivo = True
            for i in range(n_ev):
                r = evento_completo(ficha, 6, marcas, "terrestre",
                                    faixa_organica(marcas), prep, formula=formula)
                fer_terra += r["fer_terra"]
                if r["morte"]:
                    vivo = False
                    break
                if fer_terra >= 4:
                    vivo = False
                    break
                # reparo de 1 nível por década (a cadência dobrada NÃO dobra o reparo)
                if (i + 1) % (2 if cad else 1) == 0 and fer_terra > 0:
                    fer_terra -= 1
                    uv += UV_REPARO_POR_NIVEL
            vivos += int(vivo)
            tot_ft += fer_terra
            tot_uv += uv
        print(f"  {rot:50s} {n_ev:13d} {tot_ft/N_ITER:14.2f} {tot_uv/N_ITER:9.0f} "
              f"{vivos/N_ITER*100:6.1f}%")
    return out


# ---------------------------------------------------------------------------
# BATERIA T5 — a extensão RETIDA da decisão 224: B ilimitado acima da faixa
# ---------------------------------------------------------------------------
# A decisão 224 publicou a Densidade Imortal com teto em B 4 e mandou à bateria
# a continuação: "+1 de B a cada 25% do topo da faixa excedido", sem teto.
# `B` alimenta Vitalidade (`+4 × M` por degrau) E dano por dado (`+M`), então é
# a alavanca mais forte do motor — a decisão diz isso e pede o número.
def b_por_excesso(marcas, rank):
    """+1 de B a cada 25% do topo da faixa excedido (a proposta retida)."""
    banda = BANDA_MARCAS.get(rank)
    if banda is None or marcas <= banda:
        return 0
    return int(((marcas - banda) / banda) / 0.25)


def bateria_t5():
    print("\n" + "=" * 120)
    print("BATERIA T5 — A EXTENSÃO RETIDA DA DECISÃO 224: B ilimitado acima do topo da faixa")
    print("Proposta: +1 de B a cada 25% do topo excedido. B dá +4×M de Vitalidade E +M de dano por dado.")
    print("Grupo de PJs com o B do excesso; inimigo no domínio-base do rank (o Imortal denso contra a cena padrão).")
    print("=" * 120)
    print(f"  {'rank':>4s} {'Marcas':>9s} {'excesso':>8s} {'B extra':>8s} " +
          " ".join(f"{c:>17s}" for c in COMPS))
    out = {}
    casos = ((6, 10000), (6, 12500), (6, 15000), (6, 20000), (6, 30000),
             (7, 100000), (7, 150000), (7, 200000))
    for rank, marcas in casos:
        dom = DOMINIO[(rank, "recem")]
        extra = b_por_excesso(marcas, rank)
        banda = BANDA_MARCAS[rank]
        exc = (marcas - banda) / banda * 100
        linha = []
        for comp in COMPS:
            random.seed(20260830)
            r = simulate(rank, comp, imortal=True, dom_B=dom["B"] + extra,
                         pool_mult=dom["pool_mult"], enemy_B=dom["B"],
                         enemy_pool_mult=dom["pool_mult"])
            out[(rank, marcas, comp)] = r
            linha.append((r["win"] * 100, r["rounds"]))
        print(f"  {rank:4d} {marcas:9d} {exc:7.0f}% {extra:8d} " +
              " ".join(f"{w:8.1f}% {rr:6.2f}r" for w, rr in linha))
    print("\n  O PREÇO DE CADA DEGRAU. A vitória satura em 100% quase de imediato (a escada de")
    print("  composição já colapsa acima do rank 5 — achado da oitava rodada), então quem mede")
    print("  o degrau é a DURAÇÃO e o desgaste, não a vitória.")
    for rank in (6, 7):
        b0w = sum(out[(rank, BANDA_MARCAS[rank], c)]["win"] * 100 for c in COMPS) / len(COMPS)
        b0r = sum(out[(rank, BANDA_MARCAS[rank], c)]["rounds"] for c in COMPS) / len(COMPS)
        b0v = sum(out[(rank, BANDA_MARCAS[rank], c)]["vit_lost"] for c in COMPS) / len(COMPS)
        cl0 = out[(rank, BANDA_MARCAS[rank], "climax")]["rounds"]
        for r2, mk in casos:
            if r2 != rank or mk == BANDA_MARCAS[rank]:
                continue
            v = sum(out[(rank, mk, c)]["win"] * 100 for c in COMPS) / len(COMPS)
            rr = sum(out[(rank, mk, c)]["rounds"] for c in COMPS) / len(COMPS)
            vl = sum(out[(rank, mk, c)]["vit_lost"] for c in COMPS) / len(COMPS)
            cl = out[(rank, mk, "climax")]["rounds"]
            print(f"  rank {rank}, {mk:7d} Marcas (B +{b_por_excesso(mk, rank)}): "
                  f"vitória {v:5.1f}% ({v - b0w:+4.1f}pp) · rodadas {rr:4.2f} "
                  f"({(rr / b0r - 1) * 100:+5.1f}%) · Clímax {cl:4.2f}r vs {cl0:4.2f}r "
                  f"({(cl / cl0 - 1) * 100:+5.1f}%) · Vit. perdida {vl * 100:4.1f}% "
                  f"(base {b0v * 100:4.1f}%)")
    return out


# ===========================================================================
# ███  DELIVERABLE 2 — A FACE RD DO "NÍVEL DE POTÊNCIA"  ███
# ===========================================================================
# A variante (ii) foi DESCARTADA POR DERIVAÇÃO, sem medição de cena, e o
# motivo está no relatório: um Nível vale +1 na média POR DADO, e +1 de RD
# base é −1 POR DADO ATACANTE (`RD = base × M`), então a face RD simétrica é
# um no-op exato — o líquido nunca sai de 4,5/dado — e a (ii) é o mesmo no-op
# em degraus, crescendo aos trancos e nunca acompanhando o dano. O que sobrou
# pra medir é a ASSIMETRIA: como os moldes NÃO recebem a face (cláusula
# anti-dupla-contagem), a (i) deixa de ser neutra e vira inflação pura.
RD_VARIANTES = (
    ("iii", "zero", "(iii) Níveis NUNCA tocam RD — a regra de hoje (controle)"),
    ("i", "per1", "(i) ASSIMÉTRICA: +1 na RD base por Nível, SÓ no PJ"),
)


def hits_to_kill(dado, rank, rd_valor, n_iter=20000):
    """Acertos pra derrubar um alvo de rank igual com CON padrão (0).

    Idêntico ao guarda-corpo 1 da décima primeira rodada, mas com a RD do
    alvo passada por fora (é ela que a face RD move).
    """
    M = M_TABLE[rank]
    grau = STAGE_B[rank]
    vit_max = (18 + 4 * grau) * M
    d, extra_b = apply_niveis(dado, 0)
    soma = 0
    for _ in range(n_iter):
        dmg = roll_pool(M, d) + M * (grau + extra_b)
        soma += apply_rd(dmg, rd_valor, M)
    return vit_max / (soma / n_iter)


def bateria_r5():
    print("\n" + "=" * 122)
    print("BATERIA R5 — A FACE RD DO 'NÍVEL DE POTÊNCIA' (só o lado do PJ; moldes NÃO recebem)")
    print("N de Níveis do PJ = pc['B'] (Densidade da Essência): rank 1 → 0 · rank 3 → 2 · rank 5 → 3")
    print("=" * 122)
    print("\n### (0) O QUE A ARITMÉTICA JÁ RESOLVEU — a (ii) sai sem medição de cena ###")
    print("  Um Nível vale +1 na MÉDIA POR DADO (d6→d8→d10→d12 sobe a média de 3,5 a 6,5; em")
    print("  d12 o Nível excedente é +1 por dado, literalmente). A RD é `base × M`, então +1 de")
    print("  RD base é −1 POR DADO ATACANTE. Com os dois lados escalando igual, a face RD (i) é")
    print("  um NO-OP EXATO; a (ii) é o mesmo no-op em degraus, sempre atrás do dano.")
    print(f"  {'Níveis':>7s} {'dano/dado':>10s} {'RD/dado (i)':>12s} {'líquido (i)':>12s} "
          f"{'RD/dado (ii)':>13s} {'líquido (ii)':>13s}")
    for n in (0, 1, 2, 3, 5):
        dado_med = {0: 4.5, 1: 5.5, 2: 6.5, 3: 7.5, 5: 9.5}[n]
        print(f"  {n:7d} {dado_med:10.1f} {n:12d} {dado_med - n:12.1f} "
              f"{n // 2:13d} {dado_med - n // 2:13.1f}")
    print("  → (ii) DESCARTADA por derivação. O que resta medir é a ASSIMETRIA da (i).")

    # --- (a) duração de cena SOLO, contra o alvo fixo de 7-9 rodadas -------
    print("\n### (a) DURAÇÃO SOLO — 1 PJ com o Gu de defesa, contra a Horda de 8 publicada ###")
    print(f"  alvo do autor: {ALVO_SOLO[0]:.0f}-{ALVO_SOLO[1]:.0f} rodadas")
    solo = {}
    for tag, mode, label in RD_VARIANTES:
        set_rd_face(mode)
        print(f"\n  --- {label} ---")
        print(f"  {'PJ':10s} {'rank':>4s} {'RD do PJ':>9s} {'vitória':>8s} "
              f"{'rodadas':>8s} {'rod(vit.)':>10s} {'timeout':>8s}")
        for rank in RANKS_SOLO:
            for name in PCS_BASE:
                random.seed(20260830)
                r = simulate_solo(name, rank, horda8)
                solo[(tag, name, rank)] = r
                rd = (1 + rd_face_bonus(STAGE_B[rank])) * M_TABLE[rank]
                print(f"  {name:10s} {rank:4d} {rd:9.0f} {r['win']*100:7.1f}% "
                      f"{r['rounds']:7.2f}  {r['rounds_won']:9.2f} {r['timeout']*100:7.1f}%")
    set_rd_face("zero")
    print("\n  RESUMO (a) — rodadas médias e quantas das 12 células caem em 7-9:")
    for tag, mode, label in RD_VARIANTES:
        rs = [solo[(tag, n, rk)]["rounds"] for rk in RANKS_SOLO for n in PCS_BASE]
        ws = [solo[(tag, n, rk)]["win"] * 100 for rk in RANKS_SOLO for n in PCS_BASE]
        dentro = sum(1 for r in rs if ALVO_SOLO[0] <= r <= ALVO_SOLO[1])
        acima = sum(1 for r in rs if r > ALVO_SOLO[1])
        print(f"  {label:56s} {min(rs):5.1f}-{max(rs):5.1f} rodadas "
              f"(média {sum(rs)/len(rs):5.2f}) · {dentro}/12 no alvo · {acima}/12 ACIMA de 9 "
              f"· vitória {min(ws):.1f}-{max(ws):.1f}%")

    # --- (b) a escada de letalidade da decisão 78 -------------------------
    print("\n### (b) GUARDA-CORPO — a escada de letalidade da decisão 78 (d6≈5 · d8≈4 · d10≈3,3 · d12≈2,8) ###")
    print("  Alvo publicado: razão d6/d12 = 5,0/2,8 = 1,79. Sem RD (a definição literal da 78): 1,86.")
    print("  Décima primeira rodada: com RD 1×M a razão é 2,09; com RD×0,5 ela MELHORA pra 1,97.")
    print("  Aqui o alvo é o PJ com a face RD — é ele que muda. (O molde não recebe a face: a")
    print("  escada contra inimigo é, por construção, idêntica em todas as variantes.)")
    print(f"\n  {'alvo':46s} {'d6':>6s} {'d8':>6s} {'d10':>6s} {'d12':>6s} "
          f"{'d6/d12':>8s} {'Δ vs 1,79':>10s}")
    ladder = {}
    for rank in RANKS_SOLO:
        M = M_TABLE[rank]
        n_niv = STAGE_B[rank]
        for tag, mode, label in RD_VARIANTES:
            set_rd_face(mode)
            rd = (1 + rd_face_bonus(n_niv)) * M
            random.seed(20260830)
            rz = [hits_to_kill(d, rank, rd, n_iter=12000) for d in (6, 8, 10, 12)]
            ratio = rz[0] / rz[3]
            ladder[(rank, tag)] = (rz, ratio, rd)
            rot = f"rank {rank} (N={n_niv}), PJ sob {tag} — RD {rd:.0f}"
            print(f"  {rot:46s} {rz[0]:6.2f} {rz[1]:6.2f} {rz[2]:6.2f} {rz[3]:6.2f} "
                  f"{ratio:8.2f} {ratio - 1.786:+10.2f}")
        set_rd_face("zero")
    print("\n  Varredura direta por N (rank 3, M=4) — pra a sessão paralela ler qualquer N:")
    print(f"  {'N':>3s} {'RD (i)':>7s} {'d6/d12 (i)':>11s} {'RD (ii)':>8s} {'d6/d12 (ii)':>12s}")
    for n_niv in range(0, 6):
        M = M_TABLE[3]
        row = []
        for bonus in (n_niv, n_niv // 2):
            rd = (1 + bonus) * M
            random.seed(20260830)
            rz = [hits_to_kill(d, 3, rd, n_iter=12000) for d in (6, 12)]
            row.append((rd, rz[0] / rz[1]))
        print(f"  {n_niv:3d} {row[0][0]:7.0f} {row[0][1]:11.2f} "
              f"{row[1][0]:8.0f} {row[1][1]:12.2f}")

    # --- (c) a bateria de grupo -------------------------------------------
    print("\n### (c) BATERIA DE GRUPO — ranks 1/3/5, as 5 composições publicadas ###")
    grupo = {}
    mordida = {}
    for tag, mode, label in RD_VARIANTES:
        set_rd_face(mode)
        print(f"\n  --- {label} ---")
        print(f"  {'rank':>4s} " + " ".join(f"{c:>17s}" for c in COMPS))
        for rank in RANKS_SOLO:
            lw, lr = [], []
            reset_rd_stats()
            for comp in COMPS:
                random.seed(20260830)
                r = simulate(rank, comp)
                grupo[(tag, rank, comp)] = r
                lw.append(r["win"] * 100)
                lr.append(r["rounds"])
            s = dict(RD_STATS)
            mordida[(tag, rank)] = s
            print(f"  {rank:4d} " + " ".join(f"{w:8.1f}% {rr:6.2f}r" for w, rr in zip(lw, lr)))
    set_rd_face("zero")

    print("\n  QUANTO A RD DO PJ MORDE (a pergunta que nenhuma rodada mediu)")
    print("  Cobertura do Gu de defesa: 100% das rodadas POR CONSTRUÇÃO — a RD do PJ é campo")
    print("  permanente da ficha no motor (`rd = base × M`), nunca um sustentado que se liga")
    print("  e desliga. Todo número abaixo é, portanto, o TETO da inflação, não a média de mesa.")
    print(f"  {'variante':40s} {'rank':>4s} {'RD':>5s} {'acertos':>8s} {'no piso M':>10s} "
          f"{'dano absorvido':>15s}")
    for tag, mode, label in RD_VARIANTES:
        for rank in RANKS_SOLO:
            s = mordida[(tag, rank)]
            rd = (1 + rd_face_bonus(STAGE_B[rank]) if mode != "zero" else 1) * M_TABLE[rank]
            if mode == "zero":
                rd = M_TABLE[rank]
            absorb = (1 - s["liquido"] / s["bruto"]) * 100 if s["bruto"] else 0.0
            print(f"  {label[:40]:40s} {rank:4d} {rd:5.0f} {s['hits']:8d} "
                  f"{s['clamped']/s['hits']*100 if s['hits'] else 0:9.1f}% {absorb:14.1f}%")
    print("\n  RESUMO (c) — deriva contra a variante (iii) (a regra de hoje):")
    print(f"  {'variante':56s} {'Δ vitória média':>16s} {'Δ máx':>8s} {'Δ rodadas médio':>16s}")
    for tag, mode, label in RD_VARIANTES:
        dw = [grupo[(tag, rk, c)]["win"] * 100 - grupo[("iii", rk, c)]["win"] * 100
              for rk in RANKS_SOLO for c in COMPS]
        dr = [grupo[(tag, rk, c)]["rounds"] - grupo[("iii", rk, c)]["rounds"]
              for rk in RANKS_SOLO for c in COMPS]
        print(f"  {label:56s} {sum(dw)/len(dw):+15.2f}pp {max(dw, key=abs):+7.1f} "
              f"{sum(dr)/len(dr):+15.2f}r")
    return solo, ladder, grupo


# ===========================================================================
# ███  DELIVERABLE 3 — XIE LANG SEM O FÍSICO DA LUA ANTIGA  ███
# ===========================================================================
# O que muda na FICHA, em termos do motor:
#   perde  — os Níveis de Dano do Físico em Lua/Alma (+1 Latente, +2 fechado);
#            regeneração violenta, Marcas em dobro, terra Especial garantida e
#            Pressão da Abertura são todos EFEITOS FORA DE COMBATE — o motor
#            de combate nunca os modelou e continua não modelando.
#   mantém — 86% de Aptidão (Grau A): o tanque de essência não muda.
#   ganha  — Lua e Alma contam como UM Caminho só (mesma forma do buff do Lee
#            e do Jiāotáng) → some o +25% de Caminho duplo: ess_mod 1,25 → 1,0.
XIE_VARIANTES = (
    ("ficha atual", dict(nivel_bonus=1, ess_mod=1.25),
     "Físico Latente: +1 Nível em Lua/Alma, +25% de Caminho duplo"),
    ("motor 1ª-14ª", dict(nivel_bonus=0, ess_mod=1.25),
     "como as 14 rodadas anteriores modelaram (Níveis do Físico = 0)"),
    ("NOVO (sem Físico)", dict(nivel_bonus=0, ess_mod=1.0),
     "sem Níveis do Físico; Lua+Alma como um Caminho só (sem o +25%)"),
)


def bateria_x6():
    print("\n" + "=" * 122)
    print("BATERIA X6 — XIE LANG SEM O FÍSICO DA LUA ANTIGA")
    print("Perde o Físico inteiro; mantém 86% (Grau A); ganha Lua+Alma como um Caminho só.")
    print("=" * 122)

    # --- (a) bateria de grupo ---------------------------------------------
    print("\n### (a) BATERIA DE GRUPO — ranks 1/3/5, as 5 composições ###")
    grupo = {}
    for rot, kw, desc in XIE_VARIANTES:
        reset_pcs()
        set_pc_variant("Xie Lang", **kw)
        print(f"\n  --- Xie Lang: {rot} — {desc} ---")
        print(f"  {'rank':>4s} " + " ".join(f"{c:>17s}" for c in COMPS))
        for rank in RANKS_SOLO:
            lw, lr = [], []
            for comp in COMPS:
                random.seed(20260830)
                r = simulate(rank, comp)
                grupo[(rot, rank, comp)] = r
                lw.append(r["win"] * 100)
                lr.append(r["rounds"])
            print(f"  {rank:4d} " + " ".join(f"{w:8.1f}% {rr:6.2f}r" for w, rr in zip(lw, lr)))
    reset_pcs()
    print("\n  Deriva do grupo contra a 'ficha atual':")
    for rot, kw, desc in XIE_VARIANTES:
        dw = [grupo[(rot, rk, c)]["win"] * 100 - grupo[("ficha atual", rk, c)]["win"] * 100
              for rk in RANKS_SOLO for c in COMPS]
        print(f"  {rot:20s} Δ vitória média {sum(dw)/len(dw):+6.2f}pp · Δ máx {max(dw, key=abs):+6.1f}pp")

    # --- (b) solo ----------------------------------------------------------
    print("\n### (b) SOLO — cada PJ contra a Horda de 8 (a cena solo publicada) ###")
    print(f"  {'variante do Xie':20s} {'rank':>4s} " +
          " ".join(f"{n:>10s}" for n in PCS_BASE))
    for rot, kw, desc in XIE_VARIANTES:
        reset_pcs()
        set_pc_variant("Xie Lang", **kw)
        for rank in RANKS_SOLO:
            vals = []
            for name in PCS_BASE:
                random.seed(20260830)
                r = simulate_solo(name, rank, horda8)
                vals.append(r["win"] * 100)
            print(f"  {rot if rank == 1 else '':20s} {rank:4d} " +
                  " ".join(f"{v:9.1f}%" for v in vals))
    reset_pcs()

    # --- (c) a matriz PJ × PJ ---------------------------------------------
    print("\n### (c) MATRIZ PJ × PJ (a medição da décima quarta, refeita) ###")
    print("  Décima quarta: o Xie Lang venceu 84-99,5% de QUALQUER duelo. Sobrevive sem o Físico?")
    nomes = list(PCS_BASE)
    pares = [(nomes[i], nomes[j]) for i in range(len(nomes)) for j in range(i + 1, len(nomes))]
    placar = {}
    for rot, kw, desc in XIE_VARIANTES:
        reset_pcs()
        set_pc_variant("Xie Lang", **kw)
        print(f"\n  --- Xie Lang: {rot} ---")
        print(f"  {'duelo':26s} " + " ".join(f"{'rank ' + str(rk):>16s}" for rk in RANKS_SOLO))
        for na, nb in pares:
            cells = []
            for rank in RANKS_SOLO:
                random.seed(20260830)
                r = simulate_duel(na, nb, rank)
                placar[(rot, na, nb, rank)] = r
                cells.append(f"{r['win_a']*100:5.1f}/{r['win_b']*100:5.1f}%")
            print(f"  {na:>11s} × {nb:12s} " + " ".join(f"{c:>16s}" for c in cells))
        print(f"\n  {'PLACAR (média de vitória nos 3 duelos)':38s} " +
              " ".join(f"{'rank ' + str(rk):>9s}" for rk in RANKS_SOLO))
        for nome in nomes:
            linha = []
            for rank in RANKS_SOLO:
                tot = []
                for (rt, na, nb, rk), r in placar.items():
                    if rt != rot or rk != rank:
                        continue
                    den = r["win_a"] + r["win_b"]
                    if na == nome:
                        tot.append(r["win_a"] / den if den else 0.5)
                    elif nb == nome:
                        tot.append(r["win_b"] / den if den else 0.5)
                linha.append(sum(tot) / len(tot) * 100)
            print(f"  {nome:38s} " + " ".join(f"{v:8.1f}%" for v in linha))
    reset_pcs()
    return grupo, placar


# ===========================================================================
# ███  DÉCIMA SEXTA RODADA — O NERF DO CAMINHO DA ALMA  ███
# ===========================================================================

ALMA_CANDIDATOS = (
    ("atual", "SEM NERF — a regra de hoje (d12, fura 100% da RD, barra 12+2VON+3B, Def +1/rank)"),
    ("A", "A — ALINHAMENTO DE DEGRAU: d12, fura só METADE da RD (como Espada/Relâmpago)"),
    ("B", "B — QUEDA DE DADO: d10, continua furando 100% da RD"),
    ("C", "C — BARRA DURA: d12 furando tudo, barra (16+3VON+3B)×M e Defesa de Alma +2/rank"),
)
ALMA_DIAGNOSTICOS = (
    ("C_bar", "C_bar — só a barra maior (metade da C)"),
    ("C_def", "C_def — só a Defesa de Alma +2/rank (a outra metade da C)"),
)
# Os empilhamentos, medidos DEPOIS da bateria principal (é ela que mostra que
# só a C move a agulha sozinha, e portanto que só empilhamento SOBRE a C faz
# sentido testar).
ALMA_EMPILHAMENTOS = (
    ("CA", "C + A — barra dura E meia RD (a Alma vira Espada/Relâmpago com barra própria)"),
    ("CB", "C + B — barra dura E d10"),
)


def bateria_empilhamento():
    print("\n" + "=" * 122)
    print("EMPILHAMENTOS — a C é a única que move a agulha sozinha; e somada às outras?")
    print("Lidos contra o especialista de Alma e contra a escada da barra (alvo: 2,8 da decisão 78).")
    print("=" * 122)
    print(f"  {'config':6s} {'especialista r1/r3/r5':>28s} {'acertos p/ zerar a barra r1/r3/r5':>36s}")
    for modo in ("atual", "A", "B", "C", "CA", "CB"):
        set_alma(modo)
        usa_perfil_xie("puro Alma (1ª-15ª)")
        _c, p = matriz_pvp(verbose=False)
        esp = " / ".join(f"{p[('Xie Lang', rk)]:5.1f}%" for rk in RANKS_SOLO)
        random.seed(20260830)
        esc = " / ".join(f"{hits_to_kill_alma(rk, 0, 1, n_iter=20000):.2f}" for rk in RANKS_SOLO)
        print(f"  {modo:6s} {esp:>28s} {esc:>36s}")
    set_alma("atual")
    reset_pcs()


def usa_perfil_xie(rotulo):
    reset_pcs()
    set_pc_variant("Xie Lang", **XIE_PERFIL[rotulo])


def mestre_solo(rank):
    """A cena solo pedida: 1 PJ × 1 Mestre de Gu (2 ações/rodada), com o
    especial rolado pelo mix C da decisão 206 (1d6 = 6 → cultivador de Alma)."""
    return _mestres(rank, 1, 0, mix="C")


def matriz_pvp(n_iter=N_ITER, verbose=True):
    """Os 6 pares × ranks 1/3/5. Devolve (celulas, placar)."""
    nomes = list(PCS_BASE)
    pares = [(nomes[i], nomes[j]) for i in range(len(nomes)) for j in range(i + 1, len(nomes))]
    cel = {}
    if verbose:
        print(f"  {'duelo':26s} " + " ".join(f"{'rank ' + str(rk):>16s}" for rk in RANKS_SOLO)
              + f" {'rod.méd':>8s} {'≤2 rod':>7s}")
    for na, nb in pares:
        linha, rods, rap = [], [], []
        for rank in RANKS_SOLO:
            random.seed(20260830)
            r = simulate_duel(na, nb, rank, n_iter=n_iter)
            cel[(na, nb, rank)] = r
            linha.append(f"{r['win_a']*100:5.1f}/{r['win_b']*100:5.1f}%")
            rods.append(r["rounds"])
            rap.append(r["rapidos"] * 100)
        if verbose:
            print(f"  {na:>11s} × {nb:12s} " + " ".join(f"{c:>16s}" for c in linha)
                  + f" {sum(rods)/3:7.2f} {sum(rap)/3:6.1f}%")
    placar = {}
    for nome in nomes:
        for rank in RANKS_SOLO:
            tot = []
            for (na, nb, rk), r in cel.items():
                if rk != rank:
                    continue
                den = r["win_a"] + r["win_b"]
                if na == nome:
                    tot.append(r["win_a"] / den if den else 0.5)
                elif nb == nome:
                    tot.append(r["win_b"] / den if den else 0.5)
            placar[(nome, rank)] = sum(tot) / len(tot) * 100
    if verbose:
        print(f"\n  {'PLACAR (média de vitória nos 3 duelos)':38s} "
              + " ".join(f"{'rank ' + str(rk):>9s}" for rk in RANKS_SOLO))
        for nome in nomes:
            print(f"  {nome:38s} "
                  + " ".join(f"{placar[(nome, rk)]:8.1f}%" for rk in RANKS_SOLO))
    return cel, placar


def bateria_solo_mestre(n_iter=N_ITER, verbose=True):
    """Cada PJ × 1 Mestre de Gu solo, ranks 1/3/5."""
    out = {}
    if verbose:
        print(f"  {'rank':>4s} " + " ".join(f"{n:>18s}" for n in PCS_BASE))
    for rank in RANKS_SOLO:
        linha = []
        for name in PCS_BASE:
            random.seed(20260830)
            r = simulate_solo(name, rank, mestre_solo, n_iter=n_iter)
            out[(name, rank)] = r
            linha.append(f"{r['win']*100:6.1f}% {r['rounds']:5.2f}r")
        if verbose:
            print(f"  {rank:4d} " + " ".join(f"{c:>18s}" for c in linha))
    return out


def bateria_grupo(n_iter=N_ITER, verbose=True):
    """As 5 composições publicadas × ranks 1/3/5, com o quinhão de dano do Xie."""
    out = {}
    quinhao = {}
    if verbose:
        print(f"  {'rank':>4s} " + " ".join(f"{c:>17s}" for c in COMPS)
              + f" {'Xie: dano':>10s} {'dele em Alma':>13s}")
    for rank in RANKS_SOLO:
        linha = []
        reset_dmg_track(True)
        for comp in COMPS:
            random.seed(20260830)
            r = simulate(rank, comp, n_iter=n_iter)
            out[(rank, comp)] = r
            linha.append(f"{r['win']*100:7.1f}% {r['rounds']:5.2f}r")
        tot = sum(v["vit"] + v["alma"] for v in DMG_TRACK.values())
        xie = DMG_TRACK["Xie Lang"]
        share = (xie["vit"] + xie["alma"]) / tot * 100 if tot else 0.0
        frac_alma = xie["alma"] / (xie["vit"] + xie["alma"]) * 100 if (xie["vit"] + xie["alma"]) else 0.0
        quinhao[rank] = (share, frac_alma)
        reset_dmg_track(False)
        if verbose:
            print(f"  {rank:4d} " + " ".join(f"{c:>17s}" for c in linha)
                  + f" {share:9.1f}% {frac_alma:12.1f}%")
    return out, quinhao


# ---------------------------------------------------------------------------
# BATERIA N1 — o Xie Lang corrigido, SEM nerf nenhum
# ---------------------------------------------------------------------------
# A dominância publicada, medida no perfil ERRADO (Alma pura), décima quinta:
REF15_PLACAR = {("Xie Lang", 1): 88.1, ("Xie Lang", 3): 97.8, ("Xie Lang", 5): 99.5,
                ("Jiaotang", 1): 69.9, ("Jiaotang", 3): 54.3, ("Jiaotang", 5): 48.2,
                ("Demvi", 1): 13.3, ("Demvi", 3): 34.9, ("Demvi", 5): 37.7,
                ("Lee", 1): 28.7, ("Lee", 3): 12.9, ("Lee", 5): 14.6}


def bateria_n1():
    print("\n" + "=" * 122)
    print("BATERIA N1 — O XIE LANG CORRIGIDO (80:20 Lua:Alma), AINDA SEM NERF NENHUM")
    print("Perfil errado das 15 rodadas: `dado=12, alma_dmg=True` — 100% dos ataques em Alma.")
    print("Perfil correto: 80% Lua (d8, Vitalidade, RD normal) · 20% Alma (d12, barra de Alma, sem RD).")
    print("=" * 122)
    set_alma("atual")
    saida = {}
    for rot in XIE_PERFIL:
        usa_perfil_xie(rot)
        print(f"\n### Xie Lang: {rot} ###")
        print("\n  -- matriz PJ × PJ --")
        cel, placar = matriz_pvp()
        print("\n  -- solo: cada PJ × 1 Mestre de Gu (2 ações/rodada) --")
        solo = bateria_solo_mestre()
        print("\n  -- grupo: as 5 composições publicadas --")
        grupo, quinhao = bateria_grupo()
        saida[rot] = dict(cel=cel, placar=placar, solo=solo, grupo=grupo, quinhao=quinhao)
    reset_pcs()

    print("\n" + "-" * 122)
    print("A RESPOSTA (a) DO PEDIDO — a dominância de PvP no perfil CERTO")
    print("-" * 122)
    print(f"  {'PJ':12s} " + " ".join(f"{'r' + str(rk) + ' errado':>12s} {'r' + str(rk) + ' CERTO':>12s} {'Δpp':>7s}"
                                       for rk in RANKS_SOLO))
    for nome in PCS_BASE:
        cells = []
        for rk in RANKS_SOLO:
            a = saida["puro Alma (1ª-15ª)"]["placar"][(nome, rk)]
            b = saida["80:20 Lua:Alma"]["placar"][(nome, rk)]
            cells.append(f"{a:11.1f}% {b:11.1f}% {b - a:+6.1f}")
        print(f"  {nome:12s} " + " ".join(cells))
    print("\n  Checagem de reprodução contra a décima quinta (perfil errado, mesma semente):")
    for nome in PCS_BASE:
        d = [saida["puro Alma (1ª-15ª)"]["placar"][(nome, rk)] - REF15_PLACAR[(nome, rk)]
             for rk in RANKS_SOLO]
        print(f"    {nome:12s} Δ vs 15ª: " + " ".join(f"{v:+5.1f}pp" for v in d))

    # ---- o número que a sessão paralela pediu, destacado -------------------
    print("\n" + "*" * 122)
    print("*** PARA A FICHA DA MESA — XIE LANG NA CONFIGURAÇÃO NOVA (80:20, ess_mod 1,25, SEM NERF) ***")
    print("*** Substitui os 88,1 / 97,8 / 99,5% que a décima quinta mediu no perfil errado.         ***")
    print("*" * 122)
    cel = saida["80:20 Lua:Alma"]["cel"]
    pl = saida["80:20 Lua:Alma"]["placar"]
    print(f"  {'Xie Lang contra...':22s} " + " ".join(f"{'rank ' + str(rk):>12s}" for rk in RANKS_SOLO))
    for nome in PCS_BASE:
        if nome == "Xie Lang":
            continue
        linha = []
        for rk in RANKS_SOLO:
            r = cel.get(("Xie Lang", nome, rk)) or cel.get((nome, "Xie Lang", rk))
            v = r["win_a"] if ("Xie Lang", nome, rk) in cel else r["win_b"]
            den = r["win_a"] + r["win_b"]
            linha.append(f"{(v / den * 100) if den else 50.0:11.1f}%")
        print(f"  {nome:22s} " + " ".join(linha))
    print(f"  {'MÉDIA (dominância)':22s} " + " ".join(f"{pl[('Xie Lang', rk)]:11.1f}%" for rk in RANKS_SOLO))
    print("*" * 122)
    return saida


# ---------------------------------------------------------------------------
# BATERIA N2 — os candidatos de nerf, todos com o Xie no 80:20
# ---------------------------------------------------------------------------
def bateria_n2(incluir_diagnosticos=True):
    print("\n" + "=" * 122)
    print("BATERIA N2 — OS CANDIDATOS DE NERF (Xie Lang sempre no 80:20 correto)")
    print("O nerf vale para OS DOIS LADOS da mesa: o especial de Alma do molde Mestre de Gu")
    print("(1d6 = 6, decisão 206) recebe exatamente o mesmo tratamento.")
    print("=" * 122)
    lista = list(ALMA_CANDIDATOS) + (list(ALMA_DIAGNOSTICOS) if incluir_diagnosticos else [])
    saida = {}
    for modo, label in lista:
        set_alma(modo)
        usa_perfil_xie("80:20 Lua:Alma")
        print(f"\n{'#' * 118}\n### {label}\n{'#' * 118}")
        print("\n  -- matriz PJ × PJ --")
        cel, placar = matriz_pvp()
        print("\n  -- solo: cada PJ × 1 Mestre de Gu --")
        solo = bateria_solo_mestre()
        print("\n  -- grupo: as 5 composições publicadas --")
        grupo, quinhao = bateria_grupo()
        saida[modo] = dict(cel=cel, placar=placar, solo=solo, grupo=grupo, quinhao=quinhao)
    set_alma("atual")
    reset_pcs()
    return saida


# ---------------------------------------------------------------------------
# BATERIA N3 — os guarda-corpos
# ---------------------------------------------------------------------------
def hits_to_kill_alma(rank, VON=0, rd_base=1, n_iter=20000):
    """Acertos pra ZERAR A BARRA DE ALMA de um alvo de rank igual.

    O paralelo exato de `hits_to_kill` (decisão 78), mas contra o trilho que o
    Caminho da Alma realmente ataca. Nenhuma das dezesseis rodadas tinha
    calculado este número — e é ele que explica a dominância em duelo.
    """
    M = M_TABLE[rank]
    grau = STAGE_B[rank]
    alma_max = alma_bar_pc(VON, grau, M)
    d, extra_b = apply_niveis(alma_dado(), 0)
    alvo = {"rd": rd_base * M}
    soma = 0
    for _ in range(n_iter):
        dmg = roll_pool(M, d) + M * (grau + extra_b)
        soma += aplica_rd_alma(dmg, alvo, M)
    return alma_max / (soma / n_iter)


# ---------------------------------------------------------------------------
# BATERIA N2b — O ESPECIALISTA DE ALMA (o teste de esforço do nerf)
# ---------------------------------------------------------------------------
# A correção do 80:20 tira o Xie Lang do topo sozinha, mas ela NÃO conserta o
# Caminho da Alma: quem de fato se especializar nele (um PJ futuro, um NPC,
# o próprio Xie num arco em que ele vire cultivador de Alma) continua com o
# pacote de 88/98/99,5%. É contra ESTE perfil que a força de cada candidato
# fica legível — o nerf é do Caminho, não do personagem.
def bateria_n2b():
    print("\n" + "=" * 122)
    print("BATERIA N2b — O ESPECIALISTA DE ALMA: quanto cada candidato REALMENTE corta o Caminho")
    print("Perfil de esforço: 100% dos ataques em Alma (é o perfil que a 15ª mediu, 88,1/97,8/99,5%).")
    print("Não é o Xie Lang de hoje — é qualquer construção que se especialize no Caminho.")
    print("=" * 122)
    saida = {}
    for modo, label in list(ALMA_CANDIDATOS) + list(ALMA_DIAGNOSTICOS):
        set_alma(modo)
        usa_perfil_xie("puro Alma (1ª-15ª)")
        print(f"\n### {label} ###")
        cel, placar = matriz_pvp()
        saida[modo] = dict(cel=cel, placar=placar)
    set_alma("atual")
    reset_pcs()
    print("\n" + "-" * 122)
    print("DOMINÂNCIA DO ESPECIALISTA DE ALMA POR CANDIDATO")
    print("-" * 122)
    print(f"  {'candidato':12s} " + " ".join(f"{'rank ' + str(rk):>10s}" for rk in RANKS_SOLO)
          + f" {'Δ vs sem nerf':>32s}")
    base = saida["atual"]["placar"]
    for modo, _l in list(ALMA_CANDIDATOS) + list(ALMA_DIAGNOSTICOS):
        pl = saida[modo]["placar"]
        d = " ".join(f"{pl[('Xie Lang', rk)] - base[('Xie Lang', rk)]:+9.1f}pp" for rk in RANKS_SOLO)
        print(f"  {modo:12s} " + " ".join(f"{pl[('Xie Lang', rk)]:9.1f}%" for rk in RANKS_SOLO)
              + f" {d:>32s}")
    return saida


# ---------------------------------------------------------------------------
# SENSIBILIDADE — o atrito do degrau d8 que o motor NUNCA modelou
# ---------------------------------------------------------------------------
# A Tabela de Letalidade paga o d8 com "atrito real: essência congelada,
# lentidão, sangramento acumulado — é o perfil que GANHA lutas longas".
# Nenhuma das dezesseis rodadas modelou efeito de controle vindo de PJ: só os
# especiais de inimigo aplicam Lentidão no motor. Logo, o número do Xie Lang
# no 80:20 é um PISO, não o valor verdadeiro. Este knob põe um teto em volta
# dele: cada acerto de um atacante d8 tem `LUA_ATRITO_P` de chance de custar a
# ação seguinte do alvo. Vale para TODO d8 da mesa (a Lua do Xie Lang E o Lee),
# porque o atrito é do DEGRAU e não do personagem — é por isso que a leitura
# certa desta bateria é a posição relativa, não o número isolado. Não é regra
# publicada: é o intervalo de confiança do modelo, rotulado como tal.
LUA_ATRITO_P = 0.0


def set_lua_atrito(p=0.0):
    global LUA_ATRITO_P
    LUA_ATRITO_P = p


def bateria_sensibilidade():
    print("\n" + "=" * 122)
    print("SENSIBILIDADE — o atrito do degrau d8 (Lua) que o motor nunca modelou")
    print("O motor não dá controle nenhum a PJ; a Tabela de Letalidade paga o d8 exatamente com")
    print("isso. O 80:20 medido é portanto um PISO para o Xie Lang. Aqui, o teto.")
    print("=" * 122)
    set_alma("atual")
    out = {}
    for p in (0.0, 1 / 3, 2 / 3):
        set_lua_atrito(p)
        usa_perfil_xie("80:20 Lua:Alma")
        random.seed(20260830)
        cel, placar = matriz_pvp(verbose=False)
        out[p] = placar
        rot = f"atrito de Lua em {p*100:.0f}% dos acertos"
        print(f"  {rot:40s} Xie Lang: "
              + " ".join(f"r{rk} {placar[('Xie Lang', rk)]:5.1f}%" for rk in RANKS_SOLO))
    set_lua_atrito(0.0)
    reset_pcs()
    return out


def bateria_n3(n1, n2, n2b=None):
    print("\n" + "=" * 122)
    print("BATERIA N3 — GUARDA-CORPOS E DIAGNÓSTICO")
    print("=" * 122)

    # (a) a escada da decisão 78, contra VITALIDADE (o que ela mede)
    print("\n### (a) A escada de letalidade da decisão 78 — d6≈5 · d8≈4 · d10≈3,3 · d12≈2,8 ###")
    print("  Ela mede acertos pra derrubar a VITALIDADE. Nenhum candidato a toca, com UMA")
    print("  exceção: a B muda o DEGRAU do Caminho da Alma dentro dela (d12 → d10).")
    print(f"  {'rank':>4s} {'RD':>4s} {'d6':>7s} {'d8':>7s} {'d10':>7s} {'d12':>7s} {'d6/d12':>8s}")
    ladder = {}
    for rank in RANKS_SOLO:
        rd = M_TABLE[rank]
        random.seed(20260830)
        rz = [hits_to_kill(d, rank, rd, n_iter=12000) for d in (6, 8, 10, 12)]
        ladder[rank] = rz
        print(f"  {rank:4d} {rd:4.0f} {rz[0]:7.2f} {rz[1]:7.2f} {rz[2]:7.2f} {rz[3]:7.2f} "
              f"{rz[0]/rz[3]:8.2f}")
    print("\n  Impacto explícito da candidata B na escada: o Caminho da Alma sai da coluna d12")
    print("  e passa para a coluna d10 — de ~2,8 para ~3,3 acertos contra Vitalidade equivalente.")
    print("  Espada e Relâmpago continuam sozinhos no topo d12, o que é coerente com a tabela")
    print("  publicada (eles pagam 'nenhum efeito colateral' pelo mesmo dado).")

    # (b) a MESMA escada, mas contra a BARRA DE ALMA — o número que faltava
    print("\n### (b) A MESMA escada medida contra a BARRA DE ALMA (nunca calculada antes) ###")
    print("  A barra de Alma é MUITO menor que a Vitalidade: `(12+2VON+3B)×M` contra")
    print("  `(18+3CON+4B)×M`. Alvo padrão VON 0 / CON 0, RD 1×M, mesmo rank.")
    print(f"  {'candidato':10s} {'rank':>4s} {'dado':>5s} {'barra':>7s} {'dano/acerto':>12s} "
          f"{'acertos p/ zerar':>17s} {'vs 2,8 (d12 físico)':>21s}")
    alma_ladder = {}
    for modo, _label in list(ALMA_CANDIDATOS) + list(ALMA_DIAGNOSTICOS):
        set_alma(modo)
        for rank in RANKS_SOLO:
            M = M_TABLE[rank]
            grau = STAGE_B[rank]
            random.seed(20260830)
            h = hits_to_kill_alma(rank, VON=0, rd_base=1, n_iter=12000)
            barra = alma_bar_pc(0, grau, M)
            alma_ladder[(modo, rank)] = h
            fis = ladder[rank][3]
            print(f"  {modo:10s} {rank:4d} {'d'+str(alma_dado()):>5s} {barra:7.0f} "
                  f"{barra/h:12.1f} {h:17.2f} {h - fis:+20.2f}")
    set_alma("atual")

    # (c) a outra metade da dominância: a Defesa de Alma é mais fácil de acertar
    print("\n### (c) A outra metade: acertar a barra de Alma é mais fácil que acertar a Defesa ###")
    print("  Acerto do Xie = d20 + VON(3) + 2×rank + 2. Chance de acertar cada trilho:")
    print(f"  {'alvo':10s} {'rank':>4s} {'Defesa':>7s} {'Def.Alma atual':>15s} {'Def.Alma C':>11s} "
          f"{'% vs Def':>9s} {'% vs Alma':>10s} {'% vs Alma C':>12s}")
    for rank in RANKS_SOLO:
        for nome in PCS_BASE:
            if nome == "Xie Lang":
                continue
            b = _PCS_ORIG[nome]
            atk = 3 + 2 * rank + 2
            dfs = 10 + b["DES"] + 2 * rank
            set_alma("atual")
            da = alma_def_pc(b["VON"], rank)
            set_alma("C")
            dc = alma_def_pc(b["VON"], rank)
            set_alma("atual")
            p = lambda dv: min(100.0, max(5.0, (21 - (dv - atk)) / 20 * 100))
            print(f"  {nome:10s} {rank:4d} {dfs:7d} {da:15d} {dc:11d} "
                  f"{p(dfs):8.0f}% {p(da):9.0f}% {p(dc):11.0f}%")

    # (d) o resumo executivo
    print("\n" + "=" * 122)
    print("### (d) RESUMO — a dominância de PvP do Xie Lang por candidato ###")
    print("=" * 122)
    base_errado = n1["puro Alma (1ª-15ª)"]["placar"]
    base_certo = n1["80:20 Lua:Alma"]["placar"]
    print(f"  {'configuração':52s} " + " ".join(f"{'rank ' + str(rk):>9s}" for rk in RANKS_SOLO)
          + f" {'posição na mesa':>18s}")

    def _posicao(placar, rank):
        ordem = sorted(PCS_BASE, key=lambda n: -placar[(n, rank)])
        return ordem.index("Xie Lang") + 1, ordem

    print(f"  {'perfil ERRADO (Alma pura), sem nerf — a 15ª rodada':52s} "
          + " ".join(f"{base_errado[('Xie Lang', rk)]:8.1f}%" for rk in RANKS_SOLO)
          + f" {'/'.join(str(_posicao(base_errado, rk)[0]) + 'º' for rk in RANKS_SOLO):>18s}")
    print(f"  {'perfil CERTO 80:20, sem nerf':52s} "
          + " ".join(f"{base_certo[('Xie Lang', rk)]:8.1f}%" for rk in RANKS_SOLO)
          + f" {'/'.join(str(_posicao(base_certo, rk)[0]) + 'º' for rk in RANKS_SOLO):>18s}")
    for modo, label in list(ALMA_CANDIDATOS) + list(ALMA_DIAGNOSTICOS):
        if modo == "atual":
            continue
        pl = n2[modo]["placar"]
        print(f"  {'80:20 + ' + label[:44]:52s} "
              + " ".join(f"{pl[('Xie Lang', rk)]:8.1f}%" for rk in RANKS_SOLO)
              + f" {'/'.join(str(_posicao(pl, rk)[0]) + 'º' for rk in RANKS_SOLO):>18s}")

    if n2b is not None:
        print("\n  E o MESMO quadro para um ESPECIALISTA de Alma (100% dos ataques em Alma) —")
        print("  o perfil contra o qual o nerf do CAMINHO se lê, independente da ficha do Xie:")
        b2 = n2b["atual"]["placar"]
        for modo, label in list(ALMA_CANDIDATOS) + list(ALMA_DIAGNOSTICOS):
            pl = n2b[modo]["placar"]
            d = " ".join(f"({pl[('Xie Lang', rk)] - b2[('Xie Lang', rk)]:+5.1f})" for rk in RANKS_SOLO)
            print(f"    {modo:10s} " + " ".join(f"{pl[('Xie Lang', rk)]:8.1f}%" for rk in RANKS_SOLO)
                  + f"   Δ {d}")

    print("\n  A MESA INTEIRA por candidato (placar médio de cada PJ):")
    for modo, label in [("atual", "80:20 sem nerf")] + [(m, l) for m, l in
                                                        list(ALMA_CANDIDATOS)[1:] + list(ALMA_DIAGNOSTICOS)]:
        pl = n2[modo]["placar"]
        print(f"\n  --- {modo} ---")
        print(f"    {'PJ':12s} " + " ".join(f"{'rank ' + str(rk):>9s}" for rk in RANKS_SOLO))
        for nome in sorted(PCS_BASE, key=lambda n: -pl[(n, 3)]):
            print(f"    {nome:12s} " + " ".join(f"{pl[(nome, rk)]:8.1f}%" for rk in RANKS_SOLO))

    print("\n" + "-" * 122)
    print("### (e) O GRUPO NÃO PODE PIORAR — deriva contra o 80:20 sem nerf ###")
    print("  Faixas publicadas: Fácil ≈ 100% · Padrão 75-99% · Difícil ~40-52% · Clímax 56-87%")
    print("-" * 122)
    ref = n2["atual"]["grupo"]
    print(f"  {'candidato':10s} {'Δ vitória média':>16s} {'Δ máx':>8s} {'Δ rodadas':>11s} "
          f"{'quinhão do Xie r1/r3/r5':>26s} {'dele em Alma':>13s}")
    for modo, _label in [("atual", "")] + list(ALMA_CANDIDATOS)[1:] + list(ALMA_DIAGNOSTICOS):
        g = n2[modo]["grupo"]
        dw = [g[(rk, c)]["win"] * 100 - ref[(rk, c)]["win"] * 100
              for rk in RANKS_SOLO for c in COMPS]
        dr = [g[(rk, c)]["rounds"] - ref[(rk, c)]["rounds"] for rk in RANKS_SOLO for c in COMPS]
        q = n2[modo]["quinhao"]
        qs = "/".join(f"{q[rk][0]:.0f}%" for rk in RANKS_SOLO)
        fa = "/".join(f"{q[rk][1]:.0f}%" for rk in RANKS_SOLO)
        print(f"  {modo:10s} {sum(dw)/len(dw):+15.2f}pp {max(dw, key=abs):+7.1f} "
              f"{sum(dr)/len(dr):+10.2f}r {qs:>26s} {fa:>13s}")

    print("\n  Tabela de composição completa por candidato (vitória do grupo):")
    for modo, _label in [("atual", "")] + list(ALMA_CANDIDATOS)[1:] + list(ALMA_DIAGNOSTICOS):
        g = n2[modo]["grupo"]
        print(f"\n  --- {modo} ---")
        print(f"    {'rank':>4s} " + " ".join(f"{c:>16s}" for c in COMPS))
        for rank in RANKS_SOLO:
            print(f"    {rank:4d} " + " ".join(f"{g[(rank, c)]['win']*100:15.1f}%" for c in COMPS))

    print("\n" + "-" * 122)
    print("### (f) A BATERIA SOLO por candidato (cada PJ × 1 Mestre de Gu) ###")
    print("-" * 122)
    for modo, _label in [("atual", "")] + list(ALMA_CANDIDATOS)[1:] + list(ALMA_DIAGNOSTICOS):
        s = n2[modo]["solo"]
        print(f"\n  --- {modo} ---")
        print(f"    {'rank':>4s} " + " ".join(f"{n:>14s}" for n in PCS_BASE))
        for rank in RANKS_SOLO:
            print(f"    {rank:4d} " + " ".join(f"{s[(n, rank)]['win']*100:13.1f}%" for n in PCS_BASE))
    return ladder, alma_ladder


# ===========================================================================
# ███████████  DÉCIMA SÉTIMA RODADA  ███████████
# ===========================================================================
# Os números publicados da décima sexta, para a checagem de reprodução.
REF16_SEM_NERF = {("Xie Lang", 1): 33.4, ("Xie Lang", 3): 39.9, ("Xie Lang", 5): 43.6,
                  ("Jiaotang", 1): 93.5, ("Jiaotang", 3): 78.3, ("Jiaotang", 5): 70.3,
                  ("Lee", 1): 51.2, ("Lee", 3): 27.4, ("Lee", 5): 28.7,
                  ("Demvi", 1): 22.0, ("Demvi", 3): 54.4, ("Demvi", 5): 57.5}
# Décima sexta, tabela "Para a ficha da mesa": Xie Lang contra cada um, sem nerf
REF16_XIE_PARES = {1: dict(Jiaotang=9.8, Lee=25.0, Demvi=65.3),
                   3: dict(Jiaotang=26.1, Lee=55.5, Demvi=38.1),
                   5: dict(Jiaotang=33.6, Lee=57.7, Demvi=39.5)}
# Décima sexta, bateria solo sob a candidata C (a regra aplicada pela dec. 231)
REF16_SOLO_C = {"Xie Lang": (8.9, 9.8, 24.4), "Jiaotang": (59.5, 37.4, 47.7),
                "Lee": (5.3, 5.4, 17.4), "Demvi": (15.3, 24.9, 47.2)}


def configura(lee="melee — foice + Wu Xing", isencao=False, dial=None,
              golpe_duelo=False, teste_publicado=False, niveis="17ª — só a Lee",
              gatilho="chefe", quem=("Xie Lang",), atrito=0.0,
              regra="18a", heuristica="essencia", **kw_teste):
    """Monta a mesa inteira num estado declarado.

    A ordem importa: `set_niveis_ficha` primeiro (ele zera a escada de todo
    mundo), `usa_perfil_lee` depois (o perfil da Lee traz a escada dela)."""
    reset_pcs()
    set_niveis_ficha(niveis)
    usa_perfil_lee(lee)
    if dial is not None:
        set_xie_buff(hibrido_mult=dial, retaliacao_agravada=True)
    elif isencao:
        set_xie_buff(hibrido_mult=1.0, retaliacao_agravada=False)
    else:
        set_xie_buff(hibrido_mult=2.0, retaliacao_agravada=True)
    set_golpe_em_duelo(golpe_duelo)
    set_golpe_regra(regra)
    set_golpe_teste(publicado=teste_publicado, **kw_teste)
    set_golpe_gatilho(gatilho, quem)
    set_golpe_heuristica(heuristica)
    set_lua_atrito(atrito)
    set_alma("C")


def _ranking(placar, rank):
    linha = [(n, placar[(n, rank)]) for n in PCS_BASE]
    return sorted(linha, key=lambda t: -t[1])


def _veredito_criterio(placar, rank):
    """(a) Demvi fecha a fila · (b) Jiāotáng na frente na fase mortal baixa."""
    ordem = _ranking(placar, rank)
    return (("D✔" if ordem[-1][0] == "Demvi" else "D✘")
            + ("J✔" if ordem[0][0] == "Jiaotang" else "J✘"))


def _print_ranking(placar, indent="    "):
    for rank in RANKS_SOLO:
        txt = "  >  ".join(f"{n} {v:.1f}%" for n, v in _ranking(placar, rank))
        print(f"{indent}rank {rank}: {txt}")
    print(f"{indent}{'critério do autor':22s} " + " ".join(
        f"r{rk}: {_veredito_criterio(placar, rk)}" for rk in RANKS_SOLO))


def _curva_xie(placar):
    """A pergunta do autor virou 'a curva dele sobe?'. Aqui está a resposta."""
    v = [placar[("Xie Lang", rk)] for rk in RANKS_SOLO]
    lider = [max(placar[(n, rk)] for n in PCS_BASE) for rk in RANKS_SOLO]
    gap = [l - x for l, x in zip(lider, v)]
    return v, gap


# ===========================================================================
# DÉCIMA OITAVA — AS BATERIAS
# ===========================================================================
REF17_PVP = {   # a matriz de PvP publicada pela décima sétima (braço A, teto da Lee)
    ("Jiaotang", 1): 85.9, ("Jiaotang", 3): 68.7, ("Jiaotang", 5): 57.7,
    ("Lee", 1): 71.0, ("Lee", 3): 67.4, ("Lee", 5): 75.5,
    ("Demvi", 1): 18.4, ("Demvi", 3): 43.9, ("Demvi", 5): 45.1,
    ("Xie Lang", 1): 24.7, ("Xie Lang", 3): 20.0, ("Xie Lang", 5): 21.7,
}
REF17_GRUPO = {  # a bateria de grupo da 17ª, braço "Lee melee — TETO"
    "facil": (100.0, 100.0, 100.0), "padrao": (98.1, 95.6, 99.8),
    "padrao_pesado": (82.7, 77.9, 94.0), "dificil": (59.5, 71.8, 71.3),
    "climax": (16.0, 96.5, 97.5),
}
FAIXAS_PUBLICADAS = {"facil": "≈100%", "padrao": "75-99%",
                     "padrao_pesado": "53-77%", "dificil": "~40-52%",
                     "climax": "56-87%"}


def bateria_q0():
    print("\n" + "=" * 122)
    print("BATERIA Q0 — REPRODUÇÃO: com os três knobs no default, a 18ª é a 17ª?")
    print("Alvo: a matriz de PvP do braço A da décima sétima (Lee melee TETO, sem golpe em duelo).")
    print("=" * 122)
    configura(lee="melee — foice + Wu Xing", isencao=True, golpe_duelo=False,
              teste_publicado=False, niveis="17ª — só a Lee", gatilho="chefe")
    cel, placar = matriz_pvp(verbose=False)
    print(f"\n  {'PJ':12s} {'17ª publicado':>18s} {'agora':>18s} {'Δpp':>22s}")
    pior = 0.0
    for n in PCS_BASE:
        pub = " / ".join(f"{REF17_PVP[(n, rk)]:5.1f}" for rk in RANKS_SOLO)
        ago = " / ".join(f"{placar[(n, rk)]:5.1f}" for rk in RANKS_SOLO)
        dlt = " / ".join(f"{placar[(n, rk)] - REF17_PVP[(n, rk)]:+5.1f}" for rk in RANKS_SOLO)
        pior = max(pior, max(abs(placar[(n, rk)] - REF17_PVP[(n, rk)]) for rk in RANKS_SOLO))
        print(f"  {n:12s} {pub:>18s} {ago:>18s} {dlt:>22s}")
    print(f"\n  ➜ maior desvio nas 12 células: {pior:.2f}pp "
          f"({'REPRODUZ' if pior < 0.05 else 'NÃO REPRODUZ — investigar'})")
    return placar


def bateria_q1():
    print("\n" + "=" * 122)
    print("BATERIA Q1 — BUG 1: a taxa de sucesso da conjuração, antes e depois")
    print("Regra publicada ([[⚡ Golpes Matadores]]): `d20 + AST + nível de domínio`, CD 12+2×nGu,")
    print("−4 se o golpe é registrado e treinado. A nota promete que um golpe registrado em")
    print("condições decentes 'passa quase sempre'; a tabela de CD dá 40% no rank 5.")
    print("=" * 122)
    print(f"\n  {'rank':>4s} {'B':>2s} {'nGu':>4s} {'CD crua':>8s} "
          f"{'MOTOR (d20+AST)':>17s} {'CD publ.':>9s} {'PUBLICADO':>11s} {'prometido':>10s}")
    PROMETIDO = {1: 0.55, 3: 0.45, 5: 0.40}
    linhas = {}
    for rank in RANKS_MORTAIS:
        pc = make_pc("Xie Lang", rank)
        apoios, n_gu = _n_gu_golpe(pc)
        cd = 12 + 2 * n_gu
        set_golpe_teste(publicado=False)
        p_motor = _p_conjuracao(pc, n_gu)
        set_golpe_teste(publicado=True)
        p_pub = _p_conjuracao(pc, n_gu)
        cd_pub = _cd_conjuracao(pc, cd)
        linhas[rank] = (p_motor, p_pub)
        prom = f"{PROMETIDO[rank]:.0%}" if rank in PROMETIDO else "—"
        print(f"  {rank:4d} {pc['B']:2d} {n_gu:4d} {cd:8d} {p_motor:16.0%} "
              f"{cd_pub:9d} {p_pub:10.0%} {prom:>10s}")
    print("\n  Com o `+2 de dano recente` ATIVO (o PJ apanhou desde a última rodada):")
    set_golpe_teste(publicado=True)
    for rank in RANKS_MORTAIS:
        pc = make_pc("Xie Lang", rank)
        pc["dano_recente"] = True
        apoios, n_gu = _n_gu_golpe(pc)
        print(f"    rank {rank}: {_p_conjuracao(pc, n_gu):.0%}")
    print("\n  Com o `+4 de improviso` (combo que não está na ficha):")
    set_golpe_teste(publicado=True, registrado=False, improviso=True)
    for rank in RANKS_MORTAIS:
        pc = make_pc("Xie Lang", rank)
        apoios, n_gu = _n_gu_golpe(pc)
        print(f"    rank {rank}: {_p_conjuracao(pc, n_gu):.0%}")
    print("\n  E o mesmo para os outros três PJs (AST diferente muda a conta):")
    set_golpe_teste(publicado=True)
    print(f"    {'PJ':12s} {'AST':>4s} " + " ".join(f"{'r'+str(rk):>16s}" for rk in RANKS_SOLO))
    for n in PCS_BASE:
        cels = []
        for rk in RANKS_SOLO:
            pc = make_pc(n, rk)
            _a, n_gu = _n_gu_golpe(pc)
            set_golpe_teste(publicado=False)
            m = _p_conjuracao(pc, n_gu)
            set_golpe_teste(publicado=True)
            u = _p_conjuracao(pc, n_gu)
            cels.append(f"{m:6.0%} → {u:5.0%}")
        print(f"    {n:12s} {PCS_BASE[n]['AST']:4d} " + " ".join(f"{c:>16s}" for c in cels))
    set_golpe_teste(publicado=False)
    return linhas


def bateria_q2():
    print("\n" + "=" * 122)
    print("BATERIA Q2 — BUG 1 NA MESA: a coluna CLÍMAX, antes e depois do conserto")
    print("O Golpe Matador é a ferramenta do grupo contra um Chefe, e o Clímax é a ÚNICA")
    print("composição publicada em que ele dispara no gatilho histórico. Faixa publicada: 56-87%.")
    print("Gatilho 'chefe' nos dois braços — aqui só o TESTE muda, para isolar o bug 1.")
    print("=" * 122)
    res = {}
    for rot, kw in (("motor (d20 + AST)", dict(teste_publicado=False)),
                    ("PUBLICADO (d20+AST+B, CD −4)", dict(teste_publicado=True))):
        configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False,
                  niveis="17ª — só a Lee", gatilho="chefe", **kw)
        print(f"\n### {rot} ###")
        grupo, _q = bateria_grupo()
        res[rot] = grupo
    print("\n" + "-" * 122)
    print("Δ DO CONSERTO DO TESTE — todas as 15 células (🚩 > 3pp)")
    print("-" * 122)
    base = res["motor (d20 + AST)"]
    fix = res["PUBLICADO (d20+AST+B, CD −4)"]
    print(f"  {'rank':>4s} " + " ".join(f"{c:>17s}" for c in COMPS))
    movidas = 0
    for rank in RANKS_SOLO:
        cels = []
        for comp in COMPS:
            d = (fix[(rank, comp)]["win"] - base[(rank, comp)]["win"]) * 100
            if abs(d) > 3:
                movidas += 1
            cels.append(f"{d:+8.1f}pp {'🚩' if abs(d) > 3 else '  '}")
        print(f"  {rank:4d} " + " ".join(f"{c:>17s}" for c in cels))
    print(f"\n  ➜ {movidas} de 15 células movem mais de 3pp")
    print("\n  A COLUNA CLÍMAX, em número absoluto:")
    for rank in RANKS_SOLO:
        print(f"    rank {rank}: {base[(rank,'climax')]['win']*100:5.1f}% → "
              f"{fix[(rank,'climax')]['win']*100:5.1f}%  "
              f"({(fix[(rank,'climax')]['win']-base[(rank,'climax')]['win'])*100:+.1f}pp)"
              f"   [17ª publicou {REF17_GRUPO['climax'][RANKS_SOLO.index(rank)]:.1f}%]")
    return res


def bateria_q3():
    print("\n" + "=" * 122)
    print("BATERIA Q3 — BUG 2: a escada de Níveis de ficha, PJ a PJ")
    print("Derivação completa no cabeçalho do script. As escadas medidas:")
    for rot, tab in NIVEIS_FICHA.items():
        desc = " · ".join(f"{n}: " + "/".join(str(tab[n][r]) for r in RANKS_MORTAIS)
                          for n in PCS_BASE if n in tab) or "(ninguém)"
        print(f"    {rot:38s} {desc}")
    print("=" * 122)
    out = {}
    for modo in ("piso — ninguém", "17ª — só a Lee", "paridade — ordinária",
                 "paridade — Jiāotáng só amplificador", "paridade — dials zerados",
                 "paridade — teto"):
        configura(lee="melee — foice + Wu Xing", isencao=True, golpe_duelo=False,
                  niveis=modo, gatilho="chefe")
        random.seed(20260830)
        cel, placar = matriz_pvp(verbose=False)
        out[modo] = placar
        print(f"\n### {modo} ###")
        _print_ranking(placar)
        v, gap = _curva_xie(placar)
        print(f"    curva do Xie Lang: {v[0]:.1f}% → {v[1]:.1f}% → {v[2]:.1f}%   "
              f"(distância para o líder: {gap[0]:+.1f} → {gap[1]:+.1f} → {gap[2]:+.1f}pp)")
    print("\n" + "-" * 122)
    print("A AFIRMAÇÃO DA 17ª, CONFERIDA: 'com paridade, a ultrapassagem da Lee no rank 5")
    print("some, o critério fecha nos três ranks, Jiāotáng 83,5/65,7/64,3% e Demvi último'.")
    print("-" * 122)
    par = out["paridade — Jiāotáng só amplificador"]
    print("  A tabela de paridade da 17ª (Lee+Jiāotáng só, sem atrito de Lua) publicou:")
    print("    r1 Jiāotáng 85,9 > Lee 71,0 > Xie 24,7 > Demvi 18,4")
    print("    r3 Jiāotáng 75,9 > Lee 64,1 > Demvi 41,6 > Xie 18,3")
    print("    r5 Jiāotáng 74,6 > Lee 67,4 > Demvi 39,8 > Xie 18,2")
    print("  Os 83,5/65,7/64,3% do resumo NÃO são a célula de paridade — são a célula")
    print("  'paridade + atrito de Lua em ⅔', que é knob de modelagem, não conserto.")
    return out


def bateria_q4():
    print("\n" + "=" * 122)
    print("BATERIA Q4 — BUG 3: o gatilho econômico, e o que ele decide")
    print("A conta da heurística, alvo a alvo, no rank 3 (nada rolado — é aritmética):")
    print("=" * 122)
    configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False,
              niveis="paridade — ordinária", teste_publicado=True,
              gatilho="economico", quem=tuple(PCS_BASE))
    for rank in RANKS_SOLO:
        print(f"\n  ── rank {rank} " + "─" * 100)
        print(f"  {'PJ':11s} {'alvo':16s} {'barra':>8s} {'e_norm':>8s} {'e_golpe':>9s} "
              f"{'p':>5s} {'custo':>7s} {'nAtq':>5s} {'r':>4s} {'A':>9s} {'B':>9s} {'dispara':>8s}")
        for nome in PCS_BASE:
            pc = make_pc(nome, rank)
            alvos = [("outro PJ (duelo)", make_pc("Jiaotang" if nome != "Jiaotang" else "Lee", rank)),
                     ("Mestre de Gu", _mestres(rank, 1, 0, mix="C")[0]),
                     ("Chefe", make_chefe(rank))]
            for rot, alvo in alvos:
                apoios, n_gu = _n_gu_golpe(pc)
                p = _p_conjuracao(pc, n_gu)
                usa_alma = pc["alma_dmg"] and alvo.get("alma") is not None
                barra = alvo["alma"] if usa_alma else alvo["vit"]
                e_norm = max(1e-9, _e_dano_normal(pc, alvo))
                e_golpe = _e_dano_pool(pc, apoios, usa_alma)
                e_cru = max(0.0, (pc["raw_die"] + 1) / 2.0 + pc["FOR"])
                custo = _custo_golpe(pc)
                custo_atq = ACT_COST_BASE * pc["ess_mod"]
                r = min(MAX_ROUNDS, math.ceil(barra / e_norm))
                dano_a = min(barra, min(r, pc["essence"] / custo_atq) * e_norm)
                resto = max(0, r - 1)
                atq_b = min(resto, max(0.0, pc["essence"] - custo) / custo_atq)
                dano_b = (p * min(barra, e_golpe + atq_b * e_norm)
                          + (1 - p) * min(barra, resto * e_cru))
                print(f"  {nome:11s} {rot:16s} {barra:8.0f} {e_norm:8.1f} {e_golpe:9.1f} "
                      f"{p:5.0%} {custo:7.0f} {custo/custo_atq:5.1f} {r:4d} "
                      f"{dano_a:9.1f} {dano_b:9.1f} {'SIM' if dano_b > dano_a else 'não':>8s}")
    return None


def _matriz_com_disparos(rotulo, **kw):
    configura(**kw)
    reset_golpe_disparos(True)
    random.seed(20260830)
    cel, placar = matriz_pvp(verbose=False)
    disp = {n: (GOLPE_DISPAROS[n][1] / GOLPE_DISPAROS[n][0]) if GOLPE_DISPAROS[n][0] else 0.0
            for n in PCS_BASE}
    reset_golpe_disparos(False)
    print(f"\n### {rotulo} ###")
    _print_ranking(placar)
    print("    golpes por cena: " + " · ".join(f"{n} {disp[n]:.2f}" for n in PCS_BASE))
    return cel, placar, disp


def bateria_q5():
    print("\n" + "=" * 122)
    print("BATERIA Q5 — A MATRIZ DE PvP COM OS TRÊS CONSERTOS (6 pares × ranks 1/3/5)")
    print("Paridade 'ordinária' + teste publicado. Cinco braços de gatilho, para separar")
    print("o efeito do gatilho do efeito da isenção da decisão 233.")
    print("Legenda: D✔ = o Demvi fecha a fila · J✔ = o Jiāotáng lidera.")
    print("=" * 122)
    base = dict(lee="melee — foice + Wu Xing", niveis="paridade — ordinária",
                teste_publicado=True, golpe_duelo=False)
    out = {}
    out["A — gatilho 'chefe' (sem golpe em duelo)"] = _matriz_com_disparos(
        "BRAÇO A — gatilho histórico: nenhum golpe dispara em duelo", isencao=False,
        gatilho="chefe", **base)
    out["B — econômico, só Xie, SEM isenção"] = _matriz_com_disparos(
        "BRAÇO B — gatilho econômico, só o Xie Lang tem golpe, SEM isenção",
        isencao=False, gatilho="economico", quem=("Xie Lang",), **base)
    out["C — econômico, só Xie, COM isenção"] = _matriz_com_disparos(
        "BRAÇO C — gatilho econômico, só o Xie Lang tem golpe, COM a isenção (dec. 233)",
        isencao=True, gatilho="economico", quem=("Xie Lang",), **base)
    out["D — econômico, os QUATRO, SEM isenção"] = _matriz_com_disparos(
        "BRAÇO D — gatilho econômico, os QUATRO com golpe (simétrico), SEM isenção",
        isencao=False, gatilho="economico", quem=tuple(PCS_BASE), **base)
    out["E — econômico, os QUATRO, COM isenção"] = _matriz_com_disparos(
        "BRAÇO E — gatilho econômico, os QUATRO com golpe, COM a isenção (dec. 233)",
        isencao=True, gatilho="economico", quem=tuple(PCS_BASE), **base)

    print("\n" + "-" * 122)
    print("O EFEITO PURO DA ISENÇÃO COM O GATILHO CONSERTADO (C − B e E − D)")
    print("-" * 122)
    for a, b in (("B — econômico, só Xie, SEM isenção", "C — econômico, só Xie, COM isenção"),
                 ("D — econômico, os QUATRO, SEM isenção", "E — econômico, os QUATRO, COM isenção")):
        print(f"\n  {b.split('—')[1].strip()} menos {a.split('—')[1].strip()}")
        for n in PCS_BASE:
            d = [out[b][1][(n, rk)] - out[a][1][(n, rk)] for rk in RANKS_SOLO]
            print(f"    {n:12s} " + " ".join(f"r{rk} {x:+6.2f}pp" for rk, x in zip(RANKS_SOLO, d)))

    print("\n  O par que motivou a decisão 233 — Xie Lang × Demvi (vitória do Xie, normalizada):")
    for rot in out:
        vals = []
        for rk in RANKS_SOLO:
            r = out[rot][0][("Xie Lang", "Demvi", rk)]
            den = r["win_a"] + r["win_b"]
            vals.append(f"{(r['win_a']/den if den else .5)*100:9.1f}%")
        print(f"    {rot:42s} " + " ".join(vals))

    print("\n  A CURVA DO XIE LANG — o critério do autor ('ele atrás no r1 é aprovado;")
    print("  o alvo no r5 é PARIDADE com Jiāotáng e Lee, não vitória'):")
    for rot in out:
        v, gap = _curva_xie(out[rot][1])
        sobe = "SOBE" if v[2] > v[0] else "NÃO SOBE"
        print(f"    {rot:42s} {v[0]:5.1f} → {v[1]:5.1f} → {v[2]:5.1f}%   "
              f"gap p/ líder {gap[0]:+5.1f} → {gap[1]:+5.1f} → {gap[2]:+5.1f}pp   [{sobe}]")
    return out


def bateria_q6():
    print("\n" + "=" * 122)
    print("BATERIA Q6 — A BATERIA DE GRUPO COM OS TRÊS CONSERTOS")
    print("As 5 composições publicadas × ranks 1/3/5. Faixas publicadas:")
    print("  Fácil ≈100% · Padrão 75-99% · Padrão pesado 53-77% · Difícil ~40-52% · Clímax 56-87%")
    print("Baseline = o estado que a décima sétima publicou (Lee TETO, só ela com escada,")
    print("teste do motor, gatilho 'chefe'). 🚩 marca movimento > 3pp.")
    print("=" * 122)
    res, disp = {}, {}
    braços = (
        ("17ª (baseline publicado)", dict(niveis="17ª — só a Lee", teste_publicado=False,
                                          gatilho="chefe")),
        ("+ bug 1 (teste publicado)", dict(niveis="17ª — só a Lee", teste_publicado=True,
                                           gatilho="chefe")),
        ("+ bug 2 (paridade)", dict(niveis="paridade — ordinária", teste_publicado=True,
                                    gatilho="chefe")),
        ("+ bug 3 (gatilho econômico, só Xie)", dict(niveis="paridade — ordinária",
                                                     teste_publicado=True,
                                                     gatilho="economico", quem=("Xie Lang",))),
        ("OS TRÊS + golpe para os quatro", dict(niveis="paridade — ordinária",
                                                teste_publicado=True, gatilho="economico",
                                                quem=tuple(PCS_BASE))),
    )
    for rot, kw in braços:
        configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False, **kw)
        reset_golpe_disparos(True)
        print(f"\n### {rot} ###")
        grupo, _q = bateria_grupo()
        res[rot] = grupo
        disp[rot] = {n: (GOLPE_DISPAROS[n][1] / GOLPE_DISPAROS[n][0])
                     if GOLPE_DISPAROS[n][0] else 0.0 for n in PCS_BASE}
        print("  golpes por cena: " + " · ".join(f"{n} {disp[rot][n]:.2f}" for n in PCS_BASE))
        reset_golpe_disparos(False)

    print("\n" + "-" * 122)
    print("Δ CONTRA O BASELINE DA 17ª — 🚩 > 3pp")
    print("-" * 122)
    base = res["17ª (baseline publicado)"]
    for rot, _kw in braços[1:]:
        print(f"\n  {rot}")
        print(f"  {'rank':>4s} " + " ".join(f"{c:>17s}" for c in COMPS))
        movidas, maior = 0, 0.0
        for rank in RANKS_SOLO:
            cels = []
            for comp in COMPS:
                d = (res[rot][(rank, comp)]["win"] - base[(rank, comp)]["win"]) * 100
                if abs(d) > 3:
                    movidas += 1
                maior = max(maior, abs(d))
                cels.append(f"{d:+8.1f}pp {'🚩' if abs(d) > 3 else '  '}")
            print(f"  {rank:4d} " + " ".join(f"{c:>17s}" for c in cels))
        print(f"       {movidas} de 15 células > 3pp · maior movimento {maior:.1f}pp")

    print("\n" + "-" * 122)
    print("A TABELA DE COMPOSIÇÃO COMO FICA (estado final = os três consertos, só Xie com golpe)")
    print("-" * 122)
    fim = res["+ bug 3 (gatilho econômico, só Xie)"]
    print(f"  {'composição':16s} {'faixa publicada':>17s} " +
          " ".join(f"{'rank '+str(rk):>10s}" for rk in RANKS_SOLO) + "   fora da faixa?")
    for comp in COMPS:
        vals = [fim[(rk, comp)]["win"] * 100 for rk in RANKS_SOLO]
        print(f"  {comp:16s} {FAIXAS_PUBLICADAS[comp]:>17s} "
              + " ".join(f"{v:9.1f}%" for v in vals))
    return res, disp


def bateria_q7():
    print("\n" + "=" * 122)
    print("BATERIA Q7 — SENSIBILIDADE: os dials condicionais e o atrito de Lua")
    print("Três das quatro escadas de ficha são CONDICIONAIS (fase da lua, posição, terreno).")
    print("A faixa honesta vai do piso ao teto. O atrito de Lua entra como controle — é")
    print("knob de MODELAGEM (o motor não dá controle a PJ), não conserto de bug.")
    print("=" * 122)
    out = {}
    base = dict(lee="melee — foice + Wu Xing", isencao=False, teste_publicado=True,
                golpe_duelo=False, gatilho="economico", quem=("Xie Lang",))
    for modo in ("paridade — dials zerados", "paridade — ordinária", "paridade — teto"):
        configura(niveis=modo, **base)
        random.seed(20260830)
        cel, placar = matriz_pvp(verbose=False)
        out[modo] = placar
        print(f"\n### {modo} ###")
        _print_ranking(placar)
        v, gap = _curva_xie(placar)
        print(f"    curva do Xie Lang: {v[0]:.1f} → {v[1]:.1f} → {v[2]:.1f}%")
    print("\n" + "-" * 122)
    print("CONTROLE — o atrito do degrau d8 (a alavanca que a 17ª apontou), sobre a paridade")
    print("-" * 122)
    for atr in (1 / 3, 2 / 3):
        configura(niveis="paridade — ordinária", atrito=atr, **base)
        random.seed(20260830)
        cel, placar = matriz_pvp(verbose=False)
        out[("atrito", atr)] = placar
        print(f"\n### paridade ordinária + atrito de Lua em {atr*100:.0f}% ###")
        _print_ranking(placar)
    set_lua_atrito(0.0)
    return out


def bateria_q8():
    print("\n" + "=" * 122)
    print("BATERIA Q8 — SOLO: cada PJ × 1 Mestre de Gu, com os três consertos")
    print("=" * 122)
    out = {}
    for rot, kw in (("17ª (baseline)", dict(niveis="17ª — só a Lee", teste_publicado=False,
                                            gatilho="chefe")),
                    ("os três consertos", dict(niveis="paridade — ordinária",
                                               teste_publicado=True, gatilho="economico",
                                               quem=tuple(PCS_BASE)))):
        configura(lee="melee — foice + Wu Xing", isencao=True, golpe_duelo=False, **kw)
        reset_golpe_disparos(True)
        print(f"\n### {rot} ###")
        out[rot] = bateria_solo_mestre()
        print("  golpes por cena: " + " · ".join(
            f"{n} {(GOLPE_DISPAROS[n][1]/GOLPE_DISPAROS[n][0] if GOLPE_DISPAROS[n][0] else 0):.2f}"
            for n in PCS_BASE))
        reset_golpe_disparos(False)
    return out



def bateria_q9():
    """A pergunta que o gatilho econômico devolve: EXISTE alvo contra o qual o
    Golpe Matador paga? A regra diz *"Chefe, ou qualquer inimigo de rank acima
    do seu: Sim"* — aqui a conta é feita contra os dois."""
    print("\n" + "=" * 122)
    print("BATERIA Q9 — CONTRA QUEM O GOLPE PAGA, PELA CONTA DA PRÓPRIA REGRA")
    print("[[⚡ Golpes Matadores]]: 'Chefe, ou qualquer inimigo de rank acima do seu — Sim.'")
    print("A heurística é a conta que a nota descreve. Aqui ela é aplicada a alvos cada vez")
    print("maiores, até achar o ponto em que o golpe passa a valer.")
    print("=" * 122)
    configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False,
              niveis="paridade — ordinária", teste_publicado=True,
              gatilho="economico", quem=tuple(PCS_BASE))
    for rank in RANKS_SOLO:
        print(f"\n  ── rank {rank} " + "─" * 100)
        print(f"  {'PJ':11s} {'alvo':34s} {'barra':>8s} {'nAtq×e_norm':>12s} "
              f"{'p':>5s} {'A':>9s} {'B':>9s} {'dispara':>8s}")
        for nome in PCS_BASE:
            pc = make_pc(nome, rank)
            alvos = [
                ("Chefe publicado (63×M)", make_chefe(rank)),
                ("Chefe reforçado (94×M)", make_chefe(rank, vit_mult=94)),
                ("Chefe de rank +1", make_chefe(min(rank + 1, 6))),
                ("Chefe de rank +2", make_chefe(min(rank + 2, 6))),
            ]
            for rot, alvo in alvos:
                apoios, n_gu = _n_gu_golpe(pc)
                p = _p_conjuracao(pc, n_gu)
                usa_alma = pc["alma_dmg"] and alvo.get("alma") is not None
                barra = alvo["alma"] if usa_alma else alvo["vit"]
                e_norm = max(1e-9, _e_dano_normal(pc, alvo))
                e_golpe = _e_dano_pool(pc, apoios, usa_alma)
                e_cru = max(0.0, (pc["raw_die"] + 1) / 2.0 + pc["FOR"])
                custo = _custo_golpe(pc)
                custo_atq = ACT_COST_BASE * pc["ess_mod"]
                n_atq = custo / custo_atq
                r = min(MAX_ROUNDS, math.ceil(barra / e_norm))
                dano_a = min(barra, min(r, pc["essence"] / custo_atq) * e_norm)
                resto = max(0, r - 1)
                atq_b = min(resto, max(0.0, pc["essence"] - custo) / custo_atq)
                dano_b = (p * min(barra, e_golpe + atq_b * e_norm)
                          + (1 - p) * min(barra, resto * e_cru))
                print(f"  {nome:11s} {rot:34s} {barra:8.0f} {n_atq*e_norm:12.0f} "
                      f"{p:5.0%} {dano_a:9.1f} {dano_b:9.1f} "
                      f"{'SIM' if dano_b > dano_a else 'não':>8s}")
    print("\n  Leitura: `nAtq × e_norm` é literalmente a frase da nota — 'os nove a dezoito")
    print("  ataques normais que você está trocando'. Enquanto esse número for MAIOR que a")
    print("  barra do alvo, a regra manda NÃO disparar; é a própria nota que diz isso.")


def bateria_q10():
    """A tabela de composição republicável: a faixa entre os dois dials, e a
    tabela de ações do Chefe nos cinco ranks mortais."""
    print("\n" + "=" * 122)
    print("BATERIA Q10 — A TABELA DE COMPOSIÇÃO NOS TRÊS DIALS (o que republicar)")
    print("=" * 122)
    res = {}
    for modo in ("paridade — dials zerados", "paridade — ordinária", "paridade — teto"):
        configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False,
                  niveis=modo, teste_publicado=True, gatilho="economico",
                  quem=tuple(PCS_BASE))
        print(f"\n### {modo} ###")
        grupo, _q = bateria_grupo()
        res[modo] = grupo
    print("\n" + "-" * 122)
    print("A FAIXA POR CÉLULA (mínimo–máximo entre os três dials) contra a faixa publicada")
    print("-" * 122)
    print(f"  {'composição':16s} {'publicado':>12s} " +
          " ".join(f"{'rank ' + str(rk):>18s}" for rk in RANKS_SOLO))
    for comp in COMPS:
        cels = []
        for rk in RANKS_SOLO:
            vs = [res[m][(rk, comp)]["win"] * 100 for m in res]
            cels.append(f"{min(vs):5.1f}-{max(vs):5.1f}%")
        print(f"  {comp:16s} {FAIXAS_PUBLICADAS[comp]:>12s} " +
              " ".join(f"{c:>18s}" for c in cels))

    print("\n" + "=" * 122)
    print("A TABELA DE AÇÕES DO CHEFE — Chefe + Guerreiro nos cinco ranks mortais")
    print("Publicado hoje: r1 3% · r2 54% · r3 87% · r4 75% · r5 90%")
    print("=" * 122)
    for modo in ("paridade — dials zerados", "paridade — ordinária", "paridade — teto"):
        configura(lee="melee — foice + Wu Xing", isencao=False, golpe_duelo=False,
                  niveis=modo, teste_publicado=True, gatilho="economico",
                  quem=tuple(PCS_BASE))
        linha = []
        for rank in RANKS_MORTAIS:
            random.seed(20260830)
            r = simulate(rank, "climax", n_iter=N_ITER)
            linha.append(f"{r['win']*100:5.1f}% {r['rounds']:5.2f}r")
        print(f"  {modo:28s} " + " ".join(f"r{rk} {c}" for rk, c in zip(RANKS_MORTAIS, linha)))
    return res


def main18b():
    print("=" * 122)
    print("DÉCIMA OITAVA — ADENDO: Q9 (contra quem o golpe paga) e Q10 (o que republicar)")
    print("=" * 122)
    bateria_q9()
    return bateria_q10()


def main():
    print("=" * 122)
    print("DÉCIMA OITAVA RODADA — OS DOIS (TRÊS) CONSERTOS DE MOTOR E A REVALIDAÇÃO")
    print(f"{N_ITER} iterações/célula · semente 20260830 · mix de Alma C")
    print("Baseline: decisões 231 (candidata C) · 227 (ess_mod 1,25) · 236 (Lee de foice) · 215 (treino 0)")
    print("=" * 122)
    q0 = bateria_q0()
    q1 = bateria_q1()
    q2 = bateria_q2()
    q3 = bateria_q3()
    q4 = bateria_q4()
    q5 = bateria_q5()
    q6 = bateria_q6()
    q7 = bateria_q7()
    q8 = bateria_q8()
    return q0, q1, q2, q3, q4, q5, q6, q7, q8


if __name__ == "__main__":
    main()
