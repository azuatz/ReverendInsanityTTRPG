#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIGÉSIMA SEXTA RODADA — as quatro pendências de MOTOR do Log de Decisões
=======================================================================

Quatro itens estão abertos no `🧭 Log de Decisões` há tempo, todos de motor,
todos "medidos mas nunca aplicados" ou "nunca modelados". Esta rodada mede os
quatro num script só, cada um como um BRAÇO rotulado, sempre no formato
**com × sem**.

  BRAÇO 1 — o empilhamento C + A (decisão 231, pendência do Log)
            `set_alma("CA")`: a barra endurecida da candidata C MAIS o furo
            de metade da RD da candidata A. Já existe no motor como modo;
            nunca foi rodado nos quatro cenários da casa.

  BRAÇO 2 — CONTROLE VINDO DE PJ (decisão 231f, pendência do Log)
            O motor nunca deu controle a PJ. `LUA_ATRITO_P` existia, mas é
            um CARONA no dano (o acerto já aconteceu e ainda tira a ação do
            alvo) — não é o que a Tabela de Letalidade paga no degrau d8.
            Este braço modela a coisa certa: **o PJ gasta a AÇÃO em controle
            em vez de dano**, e paga por isso em dano não entregue.

  BRAÇO 3 — a Retaliação do Golpe Matador Coletivo (decisão 246g, pendência)
            piso (`só o núcleo`) × teto (`os quatro`) × um MEIO novo
            (os apoios ficam sem Gu por 2 rodadas, não pela cena inteira).

  BRAÇO 4 — o `B` ilimitado acima da faixa (decisão 226, pendência)
            Além do d12 cada Nível extra vira +1 por dado, somando em `B`.
            A pergunta é se isso estoura em rank alto ou se é seguro.

PADRÃO DA CASA
--------------
3.000 iterações por célula · semente 20260830 · os quatro perfis de
[[🎲 A Mesa — Personagens dos Jogadores]] · os quatro cenários estabelecidos
(duelo PJ×PJ, PJ×inimigo solo, grupo×horda, grupo×Chefe).

ESTADO DO MOTOR
---------------
Motor da vigésima (`2026-09-01-vigesima-escolha-ou-obrigacao.py`), com:
  · `niveis="paridade — ordinária"` — o default `"17ª — só a Lee"` é o BUG que
    a vigésima quinta expôs; NÃO se usa o default.
  · o molde Chefe recalibrado da decisão 250 (rank 1 com 2 ações; Vitalidade
    63/72/78/72/80 × M), aplicado igual à vigésima terceira.
  · Lee de foice, teste publicado, heurística "cauda", portão 3, dobra, abertura.

USO
---
    python 2026-09-06-pendencias-do-motor.py [1|2|2f|3|4|all]
"""

import importlib.util
import os
import random
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
_MOTOR = os.path.join(_AQUI, "2026-09-01-vigesima-escolha-ou-obrigacao.py")
_spec = importlib.util.spec_from_file_location("motor20", _MOTOR)
V = importlib.util.module_from_spec(_spec)
sys.modules["motor20"] = V
_spec.loader.exec_module(V)

SEED = 20260830
N_ITER = 3000
PJS = ("Xie Lang", "Jiaotang", "Lee", "Demvi")
RANKS_3 = (1, 3, 5)
RANKS_5 = (1, 2, 3, 4, 5)

# --- o molde Chefe publicado (decisão 250, aplicado pela vigésima terceira) ---
CHEFE_VIT = {1: 63, 2: 72, 3: 78, 4: 72, 5: 80}
CHEFE_ACOES_NOVA = {1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4}


def aplica_chefe_250():
    V.CHEFE_ACOES.clear()
    V.CHEFE_ACOES.update(CHEFE_ACOES_NOVA)
    orig = V.make_chefe

    def novo(rank, vit_mult=None, **kw):
        if vit_mult is None:
            vit_mult = CHEFE_VIT.get(rank, 63)
        return orig(rank, vit_mult=vit_mult, **kw)
    V.make_chefe = novo


BASE = dict(lee="melee — foice + Wu Xing", teste_publicado=True,
            heuristica="cauda", portao=3, dobra="sim", abertura=True,
            col_ret_todos=False, niveis="paridade — ordinária")


def estado(**kw):
    """Monta o estado publicado da mesa. `set_alma` vem DEPOIS de configura(),
    porque configura() termina fixando o modo 'C'."""
    alma = kw.pop("alma", "C")
    d = dict(BASE)
    d.update(kw)
    V.configura(**d)
    V.set_alma(alma)


def semente(rotulo, rank):
    """Semente determinística por célula (hash() de string é aleatorizado entre
    processos — a casa usa soma de ord())."""
    random.seed(SEED + rank * 311 + sum(ord(c) for c in rotulo))


# ---------------------------------------------------------------------------
# As quatro cenas da casa
# ---------------------------------------------------------------------------
def cena_solo(rank):
    """PJ × inimigo solo — 1 Mestre de Gu, a cena da décima sexta (231d)."""
    return [V.make_mestre_de_gu(rank, 0, special="alma" if random.randint(1, 6) == 6
                                else "physical")]


def duelo_todos(rotulo, rank, n_iter=N_ITER):
    """Duelo PJ×PJ — devolve a vitória média de cada PJ contra os outros três."""
    placar = {n: [] for n in PJS}
    for i, a in enumerate(PJS):
        for b in PJS[i + 1:]:
            semente(f"{rotulo}|{a}|{b}", rank)
            r = V.simulate_duel(a, b, rank, n_iter=n_iter)
            placar[a].append(r["win_a"])
            placar[b].append(r["win_b"])
    return {n: 100 * sum(v) / len(v) for n, v in placar.items()}


def solo_todos(rotulo, rank, n_iter=N_ITER):
    out = {}
    for n in PJS:
        semente(f"{rotulo}|solo|{n}", rank)
        out[n] = V.simulate_solo(n, rank, cena_solo, n_iter=n_iter)
    return out


def grupo(rotulo, rank, comp, n_iter=N_ITER, **kw):
    semente(f"{rotulo}|{comp}", rank)
    return V.simulate(rank, comp, n_iter=n_iter, **kw)


# ---------------------------------------------------------------------------
# Impressão
# ---------------------------------------------------------------------------
def titulo(txt, ch="="):
    print("\n" + ch * 92)
    print(txt)
    print(ch * 92)


def linha_cmp(nome, a, b, unid="pp", larg=22):
    d = b - a
    marca = " ←" if abs(d) > 1.0 else ""
    print(f"{nome:<{larg}} {a:>9.1f} {b:>9.1f} {d:>+9.1f}{unid}{marca}")


# ███████████████████████████████████████████████████████████████████████████
# BRAÇO 1 — O EMPILHAMENTO C + A
# ███████████████████████████████████████████████████████████████████████████
def escada_alma(rank, alvo, n_iter=3000):
    """Quantos acertos de um especialista PURO de Alma (d12, 100% Alma) zeram a
    barra de Alma do alvo. É a métrica da decisão 78 (o degrau d12 promete 2,8)."""
    tot = 0
    for _ in range(n_iter):
        atk = V.make_pc("Xie Lang", rank)
        tgt = V.make_pc(alvo, rank)
        h = 0
        while tgt["alma"] > 0 and h < 200:
            n = atk["M"]
            dado, extra_b = V.apply_niveis(V.alma_dado(),
                                           V.NIVEL_DELTA + atk.get("nivel_bonus", 0))
            dmg = V.roll_pool(n, dado) + atk["M"] * (atk["B"] + extra_b)
            tgt["alma"] -= V.aplica_rd_alma(dmg, tgt, atk["M"])
            h += 1
        tot += h
    return tot / n_iter


def escada_alma_von(rank, von, n_iter=3000):
    """A MESMA escada, contra um alvo sintético de VON arbitrário. A decisão 250
    publicou 2,53/2,59/2,63 para um alvo de VON 0; os PJs reais têm VON 1 a 3, e
    é contra eles que a mesa joga. Esta função permite ler as duas colunas."""
    M = V.M_TABLE[rank]
    B = V.STAGE_B[rank]
    tot = 0
    for _ in range(n_iter):
        atk = V.make_pc("Xie Lang", rank)
        barra = V.alma_bar_pc(von, B, M)
        rd = V.RD_MULT * M
        h = 0
        while barra > 0 and h < 200:
            n = atk["M"]
            dado, extra_b = V.apply_niveis(V.alma_dado(),
                                           V.NIVEL_DELTA + atk.get("nivel_bonus", 0))
            dmg = V.roll_pool(n, dado) + atk["M"] * (atk["B"] + extra_b)
            frac = V.alma_rd_frac()
            if frac > 0:
                dmg = V.apply_rd(dmg, rd * frac, atk["M"])
            barra -= dmg
            h += 1
        tot += h
    return tot / n_iter


def braco_1():
    titulo("BRAÇO 1 — EMPILHAMENTO C + A  (decisão 231, pendência do Log)")
    print("""
A candidata C (aplicada) endureceu a BARRA de Alma e a DEFESA contra Alma.
A candidata A (recusada sozinha) faz o golpe de Alma furar só METADE da RD,
em vez de furar tudo. O empilhamento C+A é as duas juntas: uma linha de regra.

O que o Log promete: escada da Alma vai a 2,66/2,75/2,78 acertos (os 2,8 da
decisão 78) e o especialista de Alma perde mais ~6pp (87,1% -> 85,0% no rank 5).

O que se PERDE não é numérico: a frase "a resposta estrutural à RD alta é o
dano de Alma" deixa de ser verdadeira pela metade.
""")

    # --- (a) a escada da decisão 78 --------------------------------------
    titulo("(1a) A ESCADA — acertos de Alma para zerar a barra do alvo (alvo: 2,8)", "-")
    print(f"{'alvo':<22} {'rank':>4} {'C (hoje)':>9} {'C + A':>9} {'Δ':>10}")
    print("-" * 92)
    for alvo in PJS:
        for rank in RANKS_3:
            estado(alma="C")
            V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
            semente(f"escada|{alvo}", rank)
            a = escada_alma(rank, alvo)
            estado(alma="CA")
            V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
            semente(f"escada|{alvo}", rank)
            b = escada_alma(rank, alvo)
            print(f"{alvo:<22} {rank:>4} {a:>9.2f} {b:>9.2f} {b - a:>+10.2f}")
    print("-" * 92)

    print("\n  A MESMA escada contra alvo SINTÉTICO por VON — a decisão 250 publicou")
    print("  2,53/2,59/2,63 para VON 0; a mesa real joga com VON 1 a 3.")
    print(f"\n{'VON do alvo':<22} {'rank':>4} {'C (hoje)':>9} {'C + A':>9} {'Δ':>10}")
    print("-" * 92)
    for von in (0, 1, 2, 3):
        for rank in RANKS_3:
            estado(alma="C")
            V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
            semente(f"escada-von{von}", rank)
            a = escada_alma_von(rank, von)
            estado(alma="CA")
            V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
            semente(f"escada-von{von}", rank)
            b = escada_alma_von(rank, von)
            print(f"VON {von:<18} {rank:>4} {a:>9.2f} {b:>9.2f} {b - a:>+10.2f}")
    print("-" * 92)

    # --- (b) duelo PJ×PJ, ficha real (80:20) -----------------------------
    titulo("(1b) DUELO PJ×PJ — fichas reais (Xie Lang 80:20 Lua:Alma)", "-")
    for rank in RANKS_3:
        estado(alma="C")
        a = duelo_todos("b1-duelo-C", rank)
        estado(alma="CA")
        b = duelo_todos("b1-duelo-CA", rank)
        print(f"\nrank {rank}   {'C (hoje)':>9} {'C + A':>9} {'Δ':>11}")
        print("-" * 92)
        for n in PJS:
            linha_cmp(n, a[n], b[n])

    # --- (c) duelo com o ESPECIALISTA de Alma (o número do Log) ----------
    titulo("(1c) DUELO — o ESPECIALISTA de Alma (Xie Lang 100% Alma, d12)", "-")
    print("É contra este perfil que a decisão 231 calibrou: quem hoje vence ~99% dos duelos.")
    for rank in RANKS_3:
        estado(alma="C")
        V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
        a = duelo_todos("b1-esp-C", rank)
        estado(alma="CA")
        V.set_pc_variant("Xie Lang", dado=12, alma_frac=1.0)
        b = duelo_todos("b1-esp-CA", rank)
        print(f"\nrank {rank}   {'C (hoje)':>9} {'C + A':>9} {'Δ':>11}")
        print("-" * 92)
        for n in PJS:
            linha_cmp(n, a[n], b[n])

    # --- (d) PJ × inimigo solo -------------------------------------------
    titulo("(1d) PJ × INIMIGO SOLO — 1 Mestre de Gu", "-")
    for rank in RANKS_3:
        estado(alma="C")
        a = solo_todos("b1-solo-C", rank)
        estado(alma="CA")
        b = solo_todos("b1-solo-CA", rank)
        print(f"\nrank {rank}   {'C (hoje)':>9} {'C + A':>9} {'Δ':>11}   (vitória do PJ)")
        print("-" * 92)
        for n in PJS:
            linha_cmp(n, 100 * a[n]["win"], 100 * b[n]["win"])

    # --- (e) grupo × horda e grupo × Chefe --------------------------------
    for comp, rot in (("facil", "GRUPO × HORDA (Fácil — Horda de 8)"),
                      ("climax", "GRUPO × CHEFE (Clímax — Chefe + Guerreiro)")):
        titulo(f"(1e) {rot}", "-")
        print(f"{'rank':<22} {'C (hoje)':>9} {'C + A':>9} {'Δ':>11}   {'rodadas C':>10} {'rodadas CA':>11}")
        print("-" * 92)
        for rank in RANKS_5:
            estado(alma="C")
            a = grupo("b1-C", rank, comp)
            estado(alma="CA")
            b = grupo("b1-CA", rank, comp)
            d = 100 * (b["win"] - a["win"])
            print(f"rank {rank:<17} {100*a['win']:>9.1f} {100*b['win']:>9.1f} "
                  f"{d:>+9.1f}pp   {a['rounds_won']:>10.2f} {b['rounds_won']:>11.2f}")
    print()


# ███████████████████████████████████████████████████████████████████████████
# BRAÇO 2 — CONTROLE VINDO DE PJ  (decisão 231f, pendência do Log)
# ███████████████████████████████████████████████████████████████████████████
# O motor nunca deu controle a PJ. O que existia (`LUA_ATRITO_P`) é um CARONA:
# o acerto de dano já aconteceu E o alvo ainda perde a ação. Isso não é o que a
# Tabela de Letalidade paga no degrau d8 — o degrau paga "atrito real", e atrito
# real CUSTA A AÇÃO de quem controla. Sem esse custo, o bracketing da décima
# sexta era um teto, não uma medição.
#
# O que este braço modela:
#   · o PJ controlador gasta a AÇÃO em controle: rola acerto normal
#     (`d20 + atributo + 2×rank + 2`) contra a Defesa do alvo; no acerto o alvo
#     perde 1 turno; NÃO causa dano nenhum.
#   · paga o mesmo custo de essência de um ataque (`40 × ess_mod`).
#   · sem Gu (`fallback_raw` ou essência abaixo do custo) o controle não sai —
#     a ação vira nada. É o PISO conservador: força humana não prende ninguém.
#   · o Chefe ignora o PRIMEIRO controle da cena (guarda-corpo já publicado,
#     `apply_controle`); esta rodada não mexe nele.
#   · alvo do controle = o inimigo vivo AINDA NÃO controlado com mais ações
#     (o Chefe/Mestre, não o mais fraco) — controlar é tirar volume de ação.
#   · contra HORDA, controlar não desliga a horda: tira 1 ataque dela naquela
#     rodada. É o piso honesto de "você prendeu parte da matilha".
#
# Com `CTRL_P = 0` NENHUMA rolagem nova é consumida: o baseline é bit-a-bit o
# motor da vigésima (mesma disciplina do `alma_frac` da décima sexta).

CTRL_P = 0.0            # fração dos turnos que o controlador gasta em controle
CTRL_QUEM = ()          # nomes dos PJs controladores
CTRL_DUR = 1            # turnos perdidos pelo alvo


def set_controle_pj(p=0.0, quem=(), dur=1):
    global CTRL_P, CTRL_QUEM, CTRL_DUR
    CTRL_P, CTRL_QUEM, CTRL_DUR = p, tuple(quem), dur


def _alvo_de_controle(enemies):
    cands = [e for e in enemies if V.enemy_alive(e)
             and not e.get("is_horda") and e.get("skip_turns", 0) <= 0]
    if cands:
        return max(cands, key=lambda e: (e.get("actions", 1), e["vit"]))
    hordas = [e for e in enemies if V.enemy_alive(e) and e.get("is_horda")]
    return hordas[0] if hordas else None


def _acao_de_controle(pc, alvo):
    """Devolve True se a ação foi consumida em controle."""
    sem_gu = (pc["fallback_raw"] or (pc["essence"] is not None
              and pc["essence"] < V.ACT_COST_BASE * pc["ess_mod"]))
    if sem_gu:
        return False        # cai no ataque normal (o piso: sem Gu, sem controle)
    pc["essence"] -= V.ACT_COST_BASE * pc["ess_mod"]
    roll = random.randint(1, 20)
    crit = roll == 20
    acerto = (roll + pc[pc["atk_attr"]] + 2 * pc["rank"] + 2
              + V.treino_pj(pc["rank"]))
    if crit or acerto >= alvo["defense"]:
        if alvo.get("is_horda"):
            alvo["ctrl_ataques"] = alvo.get("ctrl_ataques", 0) + 1
        else:
            V.apply_controle(alvo, turns=CTRL_DUR)
    return True


# --- os dois ganchos no motor (instalados uma vez, inertes com os knobs off) ---
_pc_turn_orig = V.pc_turn
_enemy_turn_orig = V.enemy_turn
_coletivo_orig = V.golpe_matador_coletivo


def _pc_turn_hook(pc, pcs, enemies, boss, rodada=0):
    # BRAÇO 3: a Retaliação coletiva TEMPORÁRIA devolve os Gu dos apoios.
    if pc.get("_ret_ate") is not None and rodada >= pc["_ret_ate"]:
        pc["fallback_raw"] = False
        pc["_ret_ate"] = None
    # BRAÇO 2: a ação de controle.
    if (CTRL_P > 0 and pc["name"] in CTRL_QUEM and V.pc_alive(pc)
            and pc["skip_turns"] <= 0 and random.random() < CTRL_P):
        alvo = _alvo_de_controle(enemies)
        if alvo is not None:
            pc["abertura"] = False
            if pc["vazamento"] and pc["essence"] is not None:
                pc["essence"] = max(0, pc["essence"] - pc["M"])
            if _acao_de_controle(pc, alvo):
                pc["dano_recente"] = False
                return
    return _pc_turn_orig(pc, pcs, enemies, boss, rodada)


def _enemy_turn_hook(e, pcs, enemies):
    if e.get("is_horda") and e.get("ctrl_ataques", 0) > 0:
        desconto = e.pop("ctrl_ataques")
        if e["vit"] <= 0:
            return
        V.update_horda_members(e)
        vivos = [p for p in pcs if V.pc_alive(p)]
        n_atk = max(0, V.horda_n_ataques(len(vivos)) - desconto)
        for _ in range(n_atk):
            vivos = [p for p in pcs if V.pc_alive(p)]
            if not vivos:
                return
            tgt = random.choice(vivos)
            V.resolve_enemy_hit(e, tgt, dado_override=V.horda_dado(e["n_members"]))
        return
    return _enemy_turn_orig(e, pcs, enemies)


V.pc_turn = _pc_turn_hook
V.enemy_turn = _enemy_turn_hook


# --- O CHASSI NEUTRO -------------------------------------------------------
# Para ler "o degrau d8 é competitivo?" é preciso comparar MESMA ficha com dado
# diferente — senão a resposta é a ficha, não o degrau. O chassi é o Demvi (o
# atacante por VON, sem cura, sem Alma), com o `dado` como único dial.
CHASSI = "Demvi"

VARIANTES = (
    ("d8  · sem controle",  8, 0.0),
    ("d8  · controle 1/3",  8, 1 / 3),
    ("d8  · controle 2/3",  8, 2 / 3),
    ("d10 · sem controle", 10, 0.0),
    ("d12 · sem controle", 12, 0.0),
)


def monta_chassi(dado, p):
    estado()
    V.set_pc_variant(CHASSI, dado=dado)
    set_controle_pj(p=p, quem=(CHASSI,))


def braco_2():
    titulo("BRAÇO 2 — CONTROLE VINDO DE PJ  (decisão 231f, pendência do Log)")
    print("""
A Tabela de Letalidade paga o degrau d8 com "atrito real... o perfil que ganha
lutas longas". Dezesseis rodadas nunca deram controle nenhum a PJ, então todo
número de Caminho d8 publicado é um PISO.

O chassi é o mesmo em todas as linhas (a ficha do Demvi); muda só o DADO e a
fração de turnos gasta em CONTROLE em vez de dano. Assim a diferença entre as
linhas é o degrau, não o personagem.

A leitura é uma pergunta só: a linha "d8 + controle" alcança as linhas "d10" e
"d12 sem controle"? Se alcançar, o degrau se paga. Se não, o d8 continua atrás
mesmo com o controle contado — e aí o problema não é de modelagem.
""")

    # --- (a) duelo PJ×PJ ---------------------------------------------------
    titulo("(2a) DUELO PJ×PJ — o chassi contra os outros três PJs (vitória média)", "-")
    for rank in RANKS_3:
        print(f"\nrank {rank}")
        print(f"{'variante do chassi':<22} {'vitória':>9}  {'vs d10':>9}  {'vs d12':>9}")
        print("-" * 92)
        res = {}
        for rot, dado, p in VARIANTES:
            monta_chassi(dado, p)
            placar = duelo_todos(f"b2-duelo-{rot}", rank)
            res[rot] = placar[CHASSI]
        base10 = res["d10 · sem controle"]
        base12 = res["d12 · sem controle"]
        for rot, _, _ in VARIANTES:
            print(f"{rot:<22} {res[rot]:>9.1f} {res[rot]-base10:>+9.1f}pp "
                  f"{res[rot]-base12:>+8.1f}pp")

    # --- (b) PJ × inimigo solo --------------------------------------------
    titulo("(2b) PJ × INIMIGO SOLO — o chassi sozinho contra 1 Mestre de Gu", "-")
    for rank in RANKS_3:
        print(f"\nrank {rank}")
        print(f"{'variante do chassi':<22} {'vitória':>9}  {'vs d10':>9}  {'vs d12':>9}  {'rodadas(v)':>11}")
        print("-" * 92)
        res = {}
        for rot, dado, p in VARIANTES:
            monta_chassi(dado, p)
            semente(f"b2-solo-{rot}", rank)
            res[rot] = V.simulate_solo(CHASSI, rank, cena_solo, n_iter=N_ITER)
        b10 = 100 * res["d10 · sem controle"]["win"]
        b12 = 100 * res["d12 · sem controle"]["win"]
        for rot, _, _ in VARIANTES:
            w = 100 * res[rot]["win"]
            print(f"{rot:<22} {w:>9.1f} {w-b10:>+9.1f}pp {w-b12:>+8.1f}pp "
                  f"{res[rot]['rounds_won']:>11.2f}")

    # --- (c) grupo × horda e (d) grupo × Chefe ----------------------------
    for comp, rot_c in (("facil", "(2c) GRUPO × HORDA (Fácil — Horda de 8)"),
                        ("climax", "(2d) GRUPO × CHEFE (Clímax — Chefe + Guerreiro)")):
        titulo(f"{rot_c} — o chassi ocupa a vaga do 4º PJ", "-")
        for rank in RANKS_3:
            print(f"\nrank {rank}")
            print(f"{'variante do chassi':<22} {'vit. grupo':>10} {'vs d10':>9} "
                  f"{'vs d12':>9}  {'rodadas(v)':>11} {'baixas':>8}")
            print("-" * 92)
            res = {}
            for rotv, dado, p in VARIANTES:
                monta_chassi(dado, p)
                res[rotv] = grupo(f"b2-{comp}-{rotv}", rank, comp)
            b10 = 100 * res["d10 · sem controle"]["win"]
            b12 = 100 * res["d12 · sem controle"]["win"]
            for rotv, _, _ in VARIANTES:
                r = res[rotv]
                w = 100 * r["win"]
                print(f"{rotv:<22} {w:>10.1f} {w-b10:>+9.1f}pp {w-b12:>+8.1f}pp "
                      f"{r['rounds_won']:>11.2f} {r['baixas']:>8.2f}")

    # --- (e) o Xie Lang REAL, com a ficha dele ----------------------------
    titulo("(2e) O XIE LANG REAL (80:20 Lua:Alma, d8 de Lua) — duelo PJ×PJ", "-")
    print("A pendência nasceu dele: com o controle desligado ele fecha a fila nos três ranks.")
    for rank in RANKS_3:
        print(f"\nrank {rank}   {'sem ctrl':>9} {'ctrl 1/3':>9} {'ctrl 2/3':>9}")
        print("-" * 92)
        col = {}
        for p, rotp in ((0.0, "sem ctrl"), (1 / 3, "ctrl 1/3"), (2 / 3, "ctrl 2/3")):
            estado()
            set_controle_pj(p=p, quem=("Xie Lang",))
            col[rotp] = duelo_todos(f"b2-xie-{rotp}", rank)
        for n in PJS:
            print(f"{n:<22} {col['sem ctrl'][n]:>9.1f} {col['ctrl 1/3'][n]:>9.1f} "
                  f"{col['ctrl 2/3'][n]:>9.1f}")
    braco_2f()
    set_controle_pj(0.0)
    print()


def braco_2f():
    """(2f) isolado — chamável sozinho (`python ... 2f`)."""
    titulo("(2f) SENSIBILIDADE — quantos turnos o controle precisa TIRAR para se pagar", "-")
    print("""
As tabelas acima usam a leitura mais magra possível: 1 acerto = 1 turno perdido.
Se o resultado for artefato dessa escolha, ele cai quando o controle dura mais.
Aqui o controlador gasta 1/3 dos turnos e a DURAÇÃO varia: 1, 2 ou 3 turnos.
A linha a bater é sempre `d10 sem controle` — o degrau imediatamente acima.
""")
    for rank in RANKS_3:
        print(f"\nrank {rank}")
        print(f"{'cenário':<24} {'d10 puro':>9} {'d8 dur1':>9} {'d8 dur2':>9} "
              f"{'d8 dur3':>9}   {'empata em':>10}")
        print("-" * 92)
        for cen, rot in (("solo", "PJ × Mestre de Gu"),
                         ("climax", "grupo × Chefe"),
                         ("dificil", "grupo × Difícil")):
            monta_chassi(10, 0.0)
            if cen == "solo":
                semente(f"b2f-{cen}-d10", rank)
                base = 100 * V.simulate_solo(CHASSI, rank, cena_solo, n_iter=N_ITER)["win"]
            else:
                base = 100 * grupo(f"b2f-{cen}-d10", rank, cen)["win"]
            vals = []
            for dur in (1, 2, 3):
                monta_chassi(8, 1 / 3)
                set_controle_pj(p=1 / 3, quem=(CHASSI,), dur=dur)
                if cen == "solo":
                    semente(f"b2f-{cen}-dur{dur}", rank)
                    v = 100 * V.simulate_solo(CHASSI, rank, cena_solo, n_iter=N_ITER)["win"]
                else:
                    v = 100 * grupo(f"b2f-{cen}-dur{dur}", rank, cen)["win"]
                vals.append(v)
            emp = next((f"dur {d}" for d, v in zip((1, 2, 3), vals) if v >= base), "nunca")
            print(f"{rot:<24} {base:>9.1f} {vals[0]:>9.1f} {vals[1]:>9.1f} "
                  f"{vals[2]:>9.1f}   {emp:>10}")


    set_controle_pj(0.0)
    print()



# ███████████████████████████████████████████████████████████████████████████
# BRAÇO 3 — A RETALIAÇÃO DO GOLPE MATADOR COLETIVO  (decisão 246g, pendência)
# ███████████████████████████████████████████████████████████████████████████
# A regra escrita diz que TODOS os participantes sofrem a Retaliação. O motor
# da sexta rodada desligou os Gu SÓ DO NÚCLEO, de propósito: cada PJ do modelo
# tem UM Gu de ataque de assinatura, então aplicar a regra ao pé da letra apaga
# o arsenal inteiro do grupo pela cena toda — enquanto os apoios de um coletivo
# real são Gu baratos e diferentes do Gu principal de cada um.
#
#   PISO   `col_ret_todos=False` — só o núcleo perde o Gu (o motor histórico)
#   TETO   `col_ret_todos=True`  — os quatro perdem, pela cena inteira
#   MEIO   (NOVO) os apoios perdem o Gu por 2 RODADAS; o núcleo, pela cena.
#          É a leitura de "a Retaliação tira os Gu que entraram no combo":
#          o apoio volta a lutar com o arsenal dele, mas não de graça.

COL_RET_MODO = "nucleo"     # 'nucleo' | 'todos' | 'temporario'
COL_RET_RODADAS = 2         # duração da Retaliação dos APOIOS no modo 'temporario'


def _coletivo_hook(pcs, boss):
    antes = {id(p): p["fallback_raw"] for p in pcs}
    r = _coletivo_orig(pcs, boss)
    if r and COL_RET_MODO == "temporario":
        nucleo = next((p for p in pcs if p["name"] == "Xie Lang" and V.pc_alive(p)),
                      None)
        for p in pcs:
            if p["fallback_raw"] and not antes[id(p)] and p is not nucleo:
                p["_ret_ate"] = COL_RET_RODADAS
    return r


V.golpe_matador_coletivo = _coletivo_hook

RANKS_COMBO = (3, 4, 5)     # o portão de rank da decisão 243 fecha 1 e 2


def braco_3():
    global COL_RET_MODO
    titulo("BRAÇO 3 — RETALIAÇÃO DO GOLPE MATADOR COLETIVO  (decisão 246g)")
    print("""
Cena de Clímax (Chefe + Guerreiro), o Coletivo montado na rodada 1, ranks 3-5
(o portão da decisão 243 fecha os ranks 1-2). Cinco modos, a mesma cena:

  · nenhum combo                        — a linha de base
  · COLETIVO, Retaliação só no NÚCLEO   — o PISO (o motor de vinte rodadas)
  · COLETIVO, Retaliação nos QUATRO     — o TETO (a regra escrita ao pé da letra)
  · COLETIVO, Retaliação temporária     — o MEIO NOVO (apoios sem Gu por 2 rodadas)
  · COLETIVO + combos individuais       — o teto com a mesa jogando por completo
""")
    modos = (
        ("nenhum combo (linha de base)", dict(heuristica="nunca"), "solo", "nucleo"),
        ("COLETIVO — Retaliação só no NÚCLEO (piso)",
         dict(heuristica="nunca", col_ret_todos=False), "coletivo", "nucleo"),
        ("COLETIVO — Retaliação TEMPORÁRIA nos apoios (2 rodadas)",
         dict(heuristica="nunca", col_ret_todos=True), "coletivo", "temporario"),
        ("COLETIVO — Retaliação nos QUATRO (teto)",
         dict(heuristica="nunca", col_ret_todos=True), "coletivo", "todos"),
        ("COLETIVO + individuais depois, Retaliação nos QUATRO",
         dict(heuristica="acao_ret", col_ret_todos=True), "coletivo", "todos"),
    )
    cena = {}
    print(f"{'modo':<56} " + " ".join(f"{'rank ' + str(rk):>22s}" for rk in RANKS_COMBO))
    print("-" * 130)
    for rot, kw, modo, ret in modos:
        COL_RET_MODO = ret
        estado(**kw)
        set_controle_pj(0.0)
        linha = []
        for rank in RANKS_COMBO:
            V.reset_coletivo_track(True)
            random.seed(SEED)
            r = V.simulate(rank, "climax", n_iter=N_ITER, golpe_mode=modo)
            tent, suc = V.COLETIVO_TRACK
            V.reset_coletivo_track(False)
            taxa = (suc / tent) if tent else float("nan")
            cena[(rot, rank)] = (r["win"] * 100, r["rounds_won"], r["baixas"], taxa)
            linha.append(f"{r['win']*100:5.1f}% {r['rounds_won']:5.2f}r {taxa:4.0%}OK")
        print(f"{rot:<56} " + " ".join(f"{c:>22s}" for c in linha))
    COL_RET_MODO = "nucleo"
    print("\n  (% = vitória do grupo · r = rodadas nas vitórias · OK = taxa de sucesso do teste)")

    base = "nenhum combo (linha de base)"
    print("\n\nΔ SOBRE A LINHA DE BASE — o preço de montar o Coletivo")
    print("-" * 130)
    print(f"{'modo':<56} " + " ".join(f"{'rank ' + str(rk):>14s}" for rk in RANKS_COMBO)
          + f"{'média':>14s}")
    for rot, _kw, _m, _r in modos[1:]:
        ds = [cena[(rot, rk)][0] - cena[(base, rk)][0] for rk in RANKS_COMBO]
        print(f"{rot:<56} " + " ".join(f"{d:>+12.1f}pp" for d in ds)
              + f"{sum(ds)/len(ds):>+12.1f}pp")
    print("\n\nBAIXAS MÉDIAS (de 4 PJs)")
    print("-" * 130)
    print(f"{'modo':<56} " + " ".join(f"{'rank ' + str(rk):>14s}" for rk in RANKS_COMBO))
    for rot, _kw, _m, _r in modos:
        print(f"{rot:<56} " + " ".join(f"{cena[(rot, rk)][2]:>14.2f}" for rk in RANKS_COMBO))
    print()


# ███████████████████████████████████████████████████████████████████████████
# BRAÇO 4 — O `B` ILIMITADO ACIMA DA FAIXA  (decisão 226, pendência)
# ███████████████████████████████████████████████████████████████████████████
# `B` é o Grau de Densidade do estágio (0·1·2·3) e soma POR DADO no dano. A
# decisão 79 manda: enquanto o dado é menor que d12, um Nível de Dano sobe o
# tipo do dado; CHEGANDO em d12, cada Nível extra vira "+1 por dado" — que no
# motor é `M × (B + extra_b)`. A pergunta aberta é se esse crescimento sem teto
# estoura em rank alto.

def niveis_extra_pj(delta, quem=PJS):
    """Soma `delta` Níveis de Dano à ficha de cada PJ. Chamar DEPOIS de estado().

    ATENÇÃO — armadilha do motor, encontrada nesta rodada: `nivel_bonus_rank` só
    tem chaves 1-5, e `make_pc` faz `nb_rank.get(rank, 0)`. Num rank IMORTAL
    (6+) a escada inteira evapora silenciosamente. A escada é estendida aqui
    até o rank 9, repetindo o valor do rank 5, antes de somar o delta."""
    for n in quem:
        nb = V.PCS_BASE[n].get("nivel_bonus_rank")
        if nb:
            topo = nb.get(5, 0)
            V.PCS_BASE[n]["nivel_bonus_rank"] = {
                r: nb.get(r, topo) + delta for r in range(1, 10)}
        else:
            V.PCS_BASE[n]["nivel_bonus"] = V.PCS_BASE[n].get("nivel_bonus", 0) + delta


DELTAS = (0, 1, 2, 4, 8)


def braco_4():
    titulo("BRAÇO 4 — O `B` ILIMITADO ACIMA DA FAIXA  (decisão 226, pendência)")
    print("""
Regra atual: além do d12, cada Nível de Dano extra vira +1 POR DADO, somando em
`B`. Sem teto. A decisão 226 mediu isso no grupo imortal e viu a DURAÇÃO desabar
(Clímax de rank 6: 8,31r -> 3,04r do degrau 0 ao degrau +8) e recomendou teto
em `B 4`. O que faltava era ler o degrau pelo lado do PJ e no rank mortal.
""")

    # --- (4a) o valor marginal de um Nível acima do d12, rank a rank -------
    titulo("(4a) QUANTO VALE UM NÍVEL ACIMA DO d12 — conta fechada, sem simulação", "-")
    print("Dano médio de um ataque de PJ = pool `n d12` + `M × (B + extra)`,")
    print("com n = M × pool_mult. O termo de Nível é FLAT em M; o pool cresce com pool_mult.")
    print(f"\n{'rank':>4} {'M':>5} {'pool_mult':>10} {'B':>3} {'dano base':>11} "
          f"{'+1 Nível':>10} {'ganho':>8} {'+8 Níveis':>11} {'ganho':>8}")
    print("-" * 92)
    for rank in (3, 4, 5, 6, 7, 8, 9):
        M = V.M_TABLE[rank]
        if rank <= 5:
            B, pm = V.STAGE_B[rank], 1
        else:
            dom = V.DOMINIO[(rank, "denso")]
            B, pm = dom["B"], dom["pool_mult"]
        n = M * pm
        base = n * 6.5 + M * B
        um = base + M
        oito = base + 8 * M
        print(f"{rank:>4} {M:>5} {pm:>10} {B:>3} {base:>11.1f} {um:>10.1f} "
              f"{100*(um/base-1):>7.1f}% {oito:>11.1f} {100*(oito/base-1):>7.1f}%")
    print("-" * 92)

    # --- (4b) lado do INIMIGO, cena imortal (reproduz a 226) ---------------
    titulo("(4b) LADO DO INIMIGO — Clímax imortal, Chefe a ΔB (reprodução da decisão 226)", "-")
    print(f"{'rank':>4} {'ΔB':>4} {'vitória':>9} {'rodadas(v)':>11} {'rodadas(todas)':>15} "
          f"{'baixas':>8} {'vit. perdida':>13}")
    print("-" * 92)
    for rank in (6, 7):
        dom = V.DOMINIO[(rank, "denso")]
        for delta in DELTAS:
            estado()
            set_controle_pj(0.0)
            semente(f"b4b-{rank}", delta)
            r = V.simulate(rank, "climax", n_iter=N_ITER, golpe_mode="solo",
                           scenario_factory=lambda rk, d=delta: V.cena_delta_b(rk, dom, d),
                           imortal=True, dom_B=dom["B"], pool_mult=dom["pool_mult"],
                           has_boss=True)
            print(f"{rank:>4} {delta:>+4} {100*r['win']:>8.1f}% {r['rounds_won']:>11.2f} "
                  f"{r['rounds']:>15.2f} {r['baixas']:>8.2f} {100*r['vit_lost']:>12.1f}%")
        print("-" * 92)

    # --- (4c) lado do PJ ---------------------------------------------------
    titulo("(4c) LADO DO PJ — os quatro PJs com Níveis EXCEDENTES", "-")
    for comp, rot in (("climax", "Clímax (Chefe + Guerreiro)"),
                      ("dificil", "Difícil")):
        print(f"\n{rot}")
        print(f"{'rank':>4} {'Δníveis':>8} {'vitória':>9} {'rodadas(v)':>11} {'baixas':>8} "
              f"{'ess. gasta':>11}")
        print("-" * 92)
        for rank in (5, 6):
            imort = rank >= 6
            dom = V.DOMINIO[(rank, "denso")] if imort else None
            for delta in DELTAS:
                estado()
                set_controle_pj(0.0)
                niveis_extra_pj(delta)
                semente(f"b4c-{comp}-{rank}", delta)
                kw = dict(imortal=True, dom_B=dom["B"], pool_mult=dom["pool_mult"]) if imort else {}
                r = V.simulate(rank, comp, n_iter=N_ITER, golpe_mode="solo", **kw)
                print(f"{rank:>4} {delta:>+8} {100*r['win']:>8.1f}% {r['rounds_won']:>11.2f} "
                      f"{r['baixas']:>8.2f} {100*r['ess_spent']:>10.1f}%")
            print("-" * 92)

    # --- (4d) duelo: um PJ com excedente contra os que não têm -------------
    titulo("(4d) DUELO PJ×PJ — um PJ com Níveis excedentes, os outros sem", "-")
    print("A leitura de degeneração de PvP: vitória do beneficiado E fração de duelos de <=2 rodadas.")
    for rank in (3, 5):
        print(f"\nrank {rank}")
        print(f"{'quem recebe':<16} {'Δníveis':>8} {'vitória':>9} {'duelos <=2r':>12} {'rodadas':>9}")
        print("-" * 92)
        for quem in ("Jiaotang", "Demvi"):
            for delta in (0, 2, 4, 8):
                estado()
                set_controle_pj(0.0)
                niveis_extra_pj(delta, quem=(quem,))
                wins, rap, rds = [], [], []
                for outro in PJS:
                    if outro == quem:
                        continue
                    semente(f"b4d-{quem}-{outro}", rank * 100 + delta)
                    r = V.simulate_duel(quem, outro, rank, n_iter=N_ITER)
                    wins.append(r["win_a"])
                    rap.append(r["rapidos"])
                    rds.append(r["rounds"])
                print(f"{quem:<16} {delta:>+8} {100*sum(wins)/3:>8.1f}% "
                      f"{100*sum(rap)/3:>11.1f}% {sum(rds)/3:>9.2f}")
            print("-" * 92)
    print()


ARMS = {"1": braco_1, "2": braco_2, "2f": braco_2f, "3": braco_3, "4": braco_4}

if __name__ == "__main__":
    aplica_chefe_250()
    alvo = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(__doc__)
    if alvo == "all":
        for k in sorted(ARMS):
            ARMS[k]()
    else:
        ARMS[alvo]()
