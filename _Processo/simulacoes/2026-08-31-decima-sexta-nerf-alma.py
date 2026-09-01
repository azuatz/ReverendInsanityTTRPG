#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Décima sexta rodada — O NERF DO CAMINHO DA ALMA e O XIE LANG 80:20
==================================================================

Cópia de [[simulacoes/2026-08-31-decima-quinta-tribulacao-e-potencia.py]] (o
motor mais atual: módulo de tribulação, mix de Alma "C", treino da decisão 215,
teto de dados da decisão 225). O módulo de tribulação vem junto mas **não é
chamado** nesta rodada — nada nele mudou.

AS DUAS DIRETIVAS DO AUTOR
--------------------------
(1) **O Xie Lang é 80:20 Lua:Alma.** As quinze rodadas anteriores modelaram
    ele como atacante de Alma PURO (`dado=12, alma_dmg=True`), o que está
    errado: **Lua é o Caminho principal (~80% dos ataques) e Alma é o
    secundário (~20%)**. Lua é d8 e o dano dela vai na Vitalidade através da
    RD normalmente; só a fração de Alma fura RD e mira a barra de Alma.
    Todo número de PvP e solo dele foi medido no perfil errado.

    MODELAGEM ADOTADA (declarada aqui, é escolha e não dedução): a cada ataque
    do Xie Lang rola-se uma moeda — **80% de chance de um golpe de Lua
    (`M d8` contra a Defesa física, RD normal) e 20% de um golpe de Alma
    (`M d12` contra `10 + VON + rank`, sem RD)**. A moeda vale para TODO
    ataque dele, Golpe Matador incluído. É a leitura literal de "80% dos
    ataques dele"; a alternativa (misturar os dois dados no mesmo golpe) foi
    rejeitada por não existir em regra nenhuma do vault.

(2) **Nerfar o Caminho da Alma.** Verbatim: *"nerfe o caminho da alma bastante
    pois ele não atinge o RD, sendo ruim para batalhas em grupo e bom para
    batalhas solo"*. O diagnóstico já está medido: Alma é o ÚNICO dano que
    ignora RD por completo (dominante em duelo — décima quinta rodada), e uma
    especial de Alma solitária é FRACA em cena de grupo porque gasta dano numa
    barra que mais nada na cena ataca (décima rodada). Hoje Alma é d12, ignora
    RD e armadura, mira `10 + VON + rank` e, pela Tabela de Letalidade, "não
    tem efeito colateral nenhum" — ou seja, um pacote estritamente melhor que
    o dos colegas de degrau (Espada e Relâmpago, também d12, furam só METADE
    da RD).

OS TRÊS CANDIDATOS (+ dois diagnósticos)
----------------------------------------
  A — ALINHAMENTO DE DEGRAU: Alma continua d12 mas passa a furar só **metade**
      da RD, como Espada e Relâmpago. (A RD física do alvo entra pela metade
      no golpe de Alma; a Defesa continua sendo `10 + VON + rank` e o dano
      continua indo na barra de Alma.)
  B — QUEDA DE DADO: Alma mantém o furo total de RD, mas cai para **d10**.
  C — ENDURECIMENTO DA BARRA: Alma continua d12 e furando tudo, mas a barra
      cresce — `(12 + 2×VON + 3×B) × M` → `(16 + 3×VON + 3×B) × M` — e a
      Defesa de Alma passa a escalar **+2/rank** (como a Defesa física) em vez
      de +1/rank: `10 + VON + 2×rank`.
  C_bar / C_def — as duas metades da C isoladas, para saber qual delas paga.

O nerf é do CAMINHO, não do personagem: ele vale para os dois lados da mesa.
Os moldes de inimigo com especial de Alma (o `1d6 = 6` do mix C, decisão 206)
recebem exatamente o mesmo tratamento, e a barra de Alma dos moldes (que é
`razão × Vitalidade`, não a fórmula de PJ) é inflada pelo mesmo fator médio
que a fórmula de PJ ganha sob a C (**×1,35**), com a Defesa de Alma deles indo
de `10 + rank + 3` para `10 + 2×rank + 3`.

AS BATERIAS
-----------
N1 — O XIE LANG CORRIGIDO, sem nerf nenhum: matriz PvP (6 pares × ranks 1/3/5),
     solo e grupo, no perfil ERRADO (Alma pura) contra o CORRETO (80:20).
     É o (a) do pedido: onde a dominância de 88,1/97,8/99,5% realmente está.
N2 — OS CANDIDATOS: cada um dos cinco × {matriz PvP, bateria solo contra o
     Mestre de Gu, bateria de grupo}, sempre com o Xie no 80:20.
N3 — GUARDA-CORPOS: a escada de letalidade da decisão 78 (d6≈5 · d8≈4 ·
     d10≈3,3 · d12≈2,8) e — o número que nenhuma rodada tinha calculado — a
     MESMA escada medida contra a BARRA DE ALMA, que é o que o Caminho da Alma
     realmente ataca. Mais o quinhão de dano do Xie Lang em cena de grupo,
     para checar a promessa "o nerf não pode piorar Alma em grupo".

Bateria: semente 20260830, 3.000 iterações/célula, mix de Alma "C",
treino = 0 nos dois lados (decisão 215).

Uso: python3 "2026-08-31-decima-sexta-nerf-alma.py"


--- cabeçalho herdado da décima quinta -----------------------------------------
Décima quinta rodada — TRIBULAÇÃO, FACE RD e A MESA SEM O FÍSICO
================================================================

Cópia de [[simulacoes/2026-08-31-decima-quarta-bateria-estendida.py]] (o motor
mais atual). O motor de COMBATE só ganhou dois knobs novos (face RD do PJ e
Nível de Dano por personagem); o resto é módulo novo — o **motor de
tribulação**, que nunca existiu em código versionado.

O QUE MUDOU NO MOTOR DE COMBATE
-------------------------------
1. `RD_FACE_MODE` — a face RD do "Nível de Potência". Só o lado do PJ recebe
   (cláusula anti-dupla-contagem: a RD impressa dos moldes já embute o
   patamar de domínio deles). Três variantes: 'zero' (hoje), 'per1' (+1 de RD
   base por Nível), 'per2' (+1 a cada 2 Níveis, arredonda pra baixo).
   O `N` de Níveis do PJ é o que o motor já calcula: `pc["B"]` — Densidade da
   Essência na fase mortal, nível de domínio na imortal.
2. `nivel_bonus` por personagem em `PCS_BASE` — Níveis de Dano que a FICHA dá
   (o +1/+2 do Físico da Lua Antiga em Lua e Alma). O motor das 14 rodadas
   anteriores modelava isso como 0; aqui vira knob, porque a décima quinta
   precisa medir o Xie Lang COM e SEM o Físico.

O MOTOR DE TRIBULAÇÃO (novo)
----------------------------
Desenho declarado por extenso na nota de Resultados. Resumo:
  · Uma "rodada" de tribulação é UMA ETAPA. Terrestre = 3 etapas (1·3·5),
    Provação Celestial e acima = 5 etapas (1·2·3·4·5).
  · Etapa = `d20 + atributo` vs CD. Sem treino (etapa é teste de atributo, não
    de perícia — decisão 215). Etapa 5 soma o nível de domínio.
  · CD: DUAS fórmulas em disputa no vault, as duas medidas aqui (bateria 3).
  · Reduções: −3 Gu de Estabilização (sequência), −2 por presságio respondido
    (uma etapa cada), −2 terra Inabalável (só Terrestre), vantagem por aliado.
  · Fichas de Azar: `faixa` fichas, no máximo 1 por etapa, jogadas contra
    sucessos (converte margem ≤2 em falha; senão rerrola e fica com o pior).
  · 1 natural conta como duas falhas.
  · Dano `M d6` por etapa falhada no trilho atacado.
  · Colateral `1d6` na tabela de Ecologia por etapa falhada, mesmo passando.
  · Ferimento da Terra +1 por Calamidade falhada; reparo 50 UV + 3 meses.

AS SEIS BATERIAS
----------------
T1 — Reprodução da QUARTA RODADA (carreira rank 6 → 10.000 Marcas, 3 níveis de
     preparação, comum × Físico Extremo). Alvo: 2,2% / 48,3% / 70,2%.
T2 — Os TRÊS CENÁRIOS pedidos pelo autor (r6 inicial · r6 estendido +20% ·
     r7), com dano à Fenda (Ferimentos da Terra) e gasto de Essência Imortal.
T3 — O FORK DA CD: `14 + 2×(rank−6) + faixa` (🌩️ l.49) contra
     `14/18/22 por faixa + faixa de novo` (⛈️ l.109). Veredito.
T4 — A ESCALA DE ESCALONAMENTO por excesso de Marcas: frouxa, certa ou brutal?
R5 — FACE RD: as 3 variantes × bateria de grupo (1/3/5) × solo × a escada de
     letalidade da decisão 78 (guarda-corpo).
X6 — XIE LANG SEM O FÍSICO: bateria de grupo + matriz PJ×PJ.

Bateria: semente 20260830, 3.000 iterações/célula (20.000 carreiras em T1,
para bater com a quarta rodada), mix de Alma "C", treino = 0 nos dois lados
(decisão 215: ataque não soma treino; moldes de rank 7+ somariam, mas as
baterias de PJ desta rodada são todas mortais ou de tribulação).

Uso: python3 "2026-08-31-decima-quinta-tribulacao-e-potencia.py"


--- cabeçalho herdado da décima quarta (motor de combate) ---------------------
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
ALMA_MODE = "atual"

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
PCS_BASE = {
    "Xie Lang": dict(FOR=-1, CON=3, DES=3, AST=2, VON=3, CAR=2, aptidao=86,
                     dado=12, alma_dmg=True, alma_frac=1.0, atk_attr="VON",
                     ess_mod=1.25, raw_die=6, role="caster", nivel_bonus=0),
    "Jiaotang": dict(FOR=4, CON=3, DES=2, AST=1, VON=1, CAR=0, aptidao=76,
                      dado=10, alma_dmg=False, alma_frac=0.0, atk_attr="FOR",
                      ess_mod=1.0, raw_die=10, role="melee", nivel_bonus=0),
    "Lee": dict(FOR=3, CON=2, DES=2, AST=1, VON=3, CAR=1, aptidao=63,
                dado=8, alma_dmg=False, alma_frac=0.0, atk_attr="VON",
                ess_mod=1.0, raw_die=6, role="healer", nivel_bonus=0),
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
        nivel_bonus=b.get("nivel_bonus", 0),
        alma_frac=b.get("alma_frac", 1.0 if b["alma_dmg"] else 0.0),
        rd=RD_MULT * (1 + rd_face_bonus(dom_bonus)) * M,
        defense=10 + b["DES"] + 2 * rank,
        alma_def=alma_def_pc(b["VON"], rank),
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
        # A MOEDA 80:20 vale também para o Golpe Matador (escolha declarada no
        # cabeçalho): 20% dele é um golpe de Alma, 80% um golpe de Lua.
        if xie.get("alma_frac", 1.0) >= 1.0:
            golpe_alma = True
        else:
            golpe_alma = random.random() < xie["alma_frac"]
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = acerto_roll + xie["VON"] + 2 * xie["rank"] + 2 + treino_pj(xie["rank"])
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


def main():
    print("=" * 122)
    print("DÉCIMA SEXTA RODADA — O NERF DO CAMINHO DA ALMA · O XIE LANG 80:20")
    print(f"{N_ITER} iterações/célula · semente 20260830 · mix de Alma C")
    print("Premissa de combate: treino = 0 dos dois lados (decisão 215)")
    print("=" * 122)
    n1 = bateria_n1()
    n2 = bateria_n2()
    n2b = bateria_n2b()
    sens = bateria_sensibilidade()
    n3 = bateria_n3(n1, n2, n2b)
    bateria_empilhamento()
    return n1, n2, n2b, sens, n3


if __name__ == "__main__":
    main()
