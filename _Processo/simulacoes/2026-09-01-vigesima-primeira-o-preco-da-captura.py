#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIGÉSIMA PRIMEIRA RODADA — O preço da captura
=============================================

Decisão 247 deu ao Golpe Matador Coletivo a **Prerrogativa ampliada**, e a
justificativa é canônica: o golpe coletivo mais famoso do romance ("busca e
travamento ilimitados", dos quatro anciãos do clã Tie) **não causa dano** — é
"o método de captura número um". A pergunta que sobrou é se essa ferramenta é
**pagável**.

O EIXO, E A ARMADILHA QUE ELE EVITA
-----------------------------------
A tentação era medir "o Coletivo impede a fuga?". Isso é **tautologia**: a
regra *diz* que Prender impede fuga por meio nenhum, então a resposta é sim por
construção — seria medir o enunciado da própria regra, o mesmo erro que a 19ª
cometeu ao medir o horizonte solo contra a própria fórmula. (Crítica da sessão
`reverend-insanity-8a`, aceita integralmente.)

A pergunta não-tautológica é o **custo**. A eficácia está escrita; o que
ninguém sabe é quanto o grupo apanha enquanto paga por ela. Duas saídas, nunca
uma:

  1. **Taxa de captura** — o alvo saiu vivo da cena? (E ela NÃO é 100% nem com
     o Coletivo: capturar exige passar na conjuração **e** acertar o ataque.)
  2. **Sobrevivência do grupo** — quantos ficaram de pé, e em quantas cenas
     ninguém caiu.

A cena é construída para o preço aparecer: um alvo que **foge ao chegar a 30%
de Vitalidade**. Ele foge justamente quando o grupo já gastou a cena inteira
nele. O braço que monta o Coletivo paga 2 a 4 ações E encara o alvo encurralado
até 0%; o braço que não monta encerra a cena mais cedo, mais inteiro, e de mãos
vazias.

Se a captura for alta e a sobrevivência despencar, o veredito é **"funciona e
ninguém deveria usar"** — que é um achado de verdade, do mesmo formato do que
já aconteceu com a isenção de híbrido e com o combo na cena de Chefe.

O QUE FICA DE FORA (e por isso todo custo aqui é PISO)
------------------------------------------------------
Sobrecarga dos apoios e Queima deliberada continuam fora do motor. O preço
medido é o menor preço possível.

3.000 iterações por célula, semente 20260830.
"""

import importlib.util
import os
import random
import statistics
import sys

# ---------------------------------------------------------------------------
# Importa o motor da vigésima rodada (o nome do arquivo tem hífens)
# ---------------------------------------------------------------------------
_AQUI = os.path.dirname(os.path.abspath(__file__))
_MOTOR = os.path.join(_AQUI, "2026-09-01-vigesima-escolha-ou-obrigacao.py")
_spec = importlib.util.spec_from_file_location("motor20", _MOTOR)
V = importlib.util.module_from_spec(_spec)
sys.modules["motor20"] = V
_spec.loader.exec_module(V)

SEED = 20260830
N_ITER = 3000
MAX_ROUNDS = V.MAX_ROUNDS

# ---------------------------------------------------------------------------
# Parâmetros da cena de fuga
# ---------------------------------------------------------------------------
FUGA_LIMIAR = 0.30      # o alvo tenta sumir ao chegar aqui
GATILHO_COLETIVO = 0.45  # o grupo lê a intenção de fuga e monta o golpe aqui


# ---------------------------------------------------------------------------
# O Coletivo, com número de participantes declarado
# ---------------------------------------------------------------------------
def coletivo_com_n(pcs, alvo, n_part):
    """Versão instrumentada de `golpe_matador_coletivo` com o tamanho do grupo
    como parâmetro (decisão 247: o Coletivo escala a partir de dois).

    Devolve (montou, capturou). `capturou` só é True se a conjuração passou E
    o ataque acertou — é aí que a Prerrogativa Prender se planta."""
    vivos = [p for p in pcs if V.pc_alive(p)]
    if len(vivos) < n_part or alvo is None or not V.enemy_alive(alvo):
        return False, False

    nucleo = next((p for p in vivos if p["name"] == "Xie Lang"), vivos[0])
    if not V._pode_montar(nucleo):
        return False, False
    outros = [p for p in vivos if p is not nucleo][: n_part - 1]
    participants = [nucleo] + outros
    if len(participants) < n_part:
        return False, False

    apoios_outros = len(participants) - 1
    bonus_levels = {1: 3, 2: 5, 3: 6}.get(apoios_outros, 3 + apoios_outros)
    n_gu_cd = {2: 2, 3: 3, 4: 5}.get(len(participants), len(participants) + 1)
    cd = V._cd_base(n_gu_cd) - 2

    base_shares = {p["name"]: V.ACT_COST_BASE * p["ess_mod"] for p in participants}
    total_base = sum(base_shares.values())
    custo_total = total_base * len(participants) * 2
    if sum(p["essence"] for p in participants) < custo_total:
        return False, False

    for p in participants:
        share = base_shares[p["name"]] / total_base
        p["essence"] = max(0, p["essence"] - custo_total * share)
        if V.GOLPE_ABERTURA:
            p["abertura"] = True

    capturou = False
    teste, cd = V._conjuracao(nucleo, cd)
    if teste >= cd:
        golpe_alma = (nucleo.get("alma_frac", 1.0) >= 1.0
                      or random.random() < nucleo["alma_frac"])
        acerto_roll = random.randint(1, 20)
        crit = acerto_roll == 20
        acerto = (acerto_roll + nucleo["VON"] + 2 * nucleo["rank"] + 2
                  + V.treino_pj(nucleo["rank"]))
        usa_alma = golpe_alma and alvo.get("alma") is not None
        def_val = alvo["alma_def"] if usa_alma else alvo["defense"]
        if crit or acerto >= def_val:
            # A Prerrogativa se planta no acerto — é isto que prende o alvo.
            capturou = True
            n = nucleo["M"] * nucleo.get("pool_mult", 1) * (2 if crit else 1)
            base_dado = V.alma_dado() if usa_alma else nucleo["dado"]
            dado, extra_b = V.apply_niveis(base_dado,
                                           V.NIVEL_DELTA + nucleo.get("nivel_bonus", 0))
            dmg = (V._rola_pool_golpe(nucleo, n, dado, base_dado,
                                      V._dobra_ativa(nucleo, alvo))
                   + nucleo["M"] * (nucleo["B"] + bonus_levels + extra_b))
            if usa_alma:
                alvo["alma"] -= V.aplica_rd_alma(dmg, alvo, nucleo["M"])
                if alvo["alma"] > 0 and crit and alvo["alma"] <= 0.25 * alvo["alma_max"]:
                    V.apply_fratura(alvo)
            else:
                alvo["vit"] -= V.apply_rd(dmg, alvo.get("rd", 0), nucleo["M"])
    else:
        # Retaliação: cai em todos os participantes (decisão 246).
        for p in (participants if V.COLETIVO_RETALIACAO_TODOS else [nucleo]):
            p["fallback_raw"] = True
        if cd - teste >= 5:
            for p in participants:
                p["vit_max"] = round(p["vit_max"] * 0.85)
                p["vit"] = min(p["vit"], p["vit_max"])

    return True, capturou


# ---------------------------------------------------------------------------
# A cena de fuga
# ---------------------------------------------------------------------------
def combate_com_fuga(pcs, enemies, fujao, n_part, tentativas=1):
    """`n_part = 0` é o braço que deixa fugir. Devolve dict de resultados."""
    order = []
    for p in pcs:
        order.append((random.randint(1, 20) + p["DES"], id(p), p, "pc"))
    for e in enemies:
        order.append((random.randint(1, 20), id(e), e, "enemy"))
    order.sort(key=lambda t: -t[0])

    preso = False
    fugiu = False
    tentadas = 0
    montagens = 0
    rounds_used = MAX_ROUNDS

    for rnd in range(MAX_ROUNDS):
        if (not any(V.pc_alive(p) for p in pcs)
                or not any(V.enemy_alive(e) for e in enemies) or fugiu):
            rounds_used = rnd
            break

        pulam = set()
        if (n_part and not preso and tentadas < tentativas
                and V.enemy_alive(fujao)
                and fujao["vit"] <= GATILHO_COLETIVO * fujao["vit_max"]):
            tentadas += 1
            montou, capturou = coletivo_com_n(pcs, fujao, n_part)
            if montou:
                montagens += 1
                preso = preso or capturou
                vivos = [p for p in pcs if V.pc_alive(p)]
                nucleo = next((p for p in vivos if p["name"] == "Xie Lang"),
                              vivos[0] if vivos else None)
                escolhidos = ([nucleo] + [p for p in vivos if p is not nucleo][: n_part - 1]
                              if nucleo else [])
                pulam = {id(p) for p in escolhidos}
            else:
                tentadas -= 1  # não montou (essência/portão) — não gastou a janela

        for _, _, entity, side in order:
            if (not any(V.pc_alive(p) for p in pcs)
                    or not any(V.enemy_alive(e) for e in enemies)):
                break
            if side == "pc":
                if id(entity) in pulam:
                    continue
                V.pc_turn(entity, pcs, enemies, fujao, rodada=rnd)
            else:
                if (entity is fujao and not preso and V.enemy_alive(entity)
                        and entity["vit"] <= FUGA_LIMIAR * entity["vit_max"]):
                    fugiu = True
                    break
                V.enemy_turn(entity, pcs, enemies)
                V.update_horda_members(entity)

        if V.ABERTURA_TRACK is not None:
            for p in pcs:
                if V.pc_alive(p):
                    V.ABERTURA_TRACK[p["name"]][2] += 1
                    if p.get("abertura"):
                        V.ABERTURA_TRACK[p["name"]][0] += 1
        rounds_used = rnd + 1
        if fugiu:
            break

    baixas = sum(1 for p in pcs if V.pc_baixa_real(p))
    return dict(
        capturou=(not fugiu) and (not V.enemy_alive(fujao)),
        fugiu=fugiu,
        limpou=not any(V.enemy_alive(e) for e in enemies),
        baixas=baixas,
        intacto=(baixas == 0),
        tpk=(baixas >= 4),
        rodadas=rounds_used,
        montagens=montagens,
        vit_lost=(sum(max(0, p["vit_max"] - max(p["vit"], 0)) for p in pcs)
                  / sum(p["vit_max"] for p in pcs)),
    )


def cena_chefe(rank):
    return [V.make_chefe(rank), V.make_guerreiro(rank, especial=True)]


def cena_elite(rank):
    return [V.make_elite(rank), V.make_elite(rank)]


def roda(rank, cenario, n_part, tentativas=1, n_iter=N_ITER):
    acc = dict(cap=0, fuga=0, baixas=0, intacto=0, tpk=0, rodadas=0,
               mont=0, vit=0.0)
    for _ in range(n_iter):
        pcs = V.make_pcs(rank)
        enemies = cenario(rank)
        fujao = enemies[0]
        r = combate_com_fuga(pcs, enemies, fujao, n_part, tentativas)
        acc["cap"] += r["capturou"]
        acc["fuga"] += r["fugiu"]
        acc["baixas"] += r["baixas"]
        acc["intacto"] += r["intacto"]
        acc["tpk"] += r["tpk"]
        acc["rodadas"] += r["rodadas"]
        acc["mont"] += r["montagens"]
        acc["vit"] += r["vit_lost"]
    n = n_iter
    return dict(
        captura=100 * acc["cap"] / n,
        fuga=100 * acc["fuga"] / n,
        sobrev=100 * (4 * n - acc["baixas"]) / (4 * n),
        intacto=100 * acc["intacto"] / n,
        tpk=100 * acc["tpk"] / n,
        rodadas=acc["rodadas"] / n,
        montagens=acc["mont"] / n,
        vit=100 * acc["vit"] / n,
    )


# ---------------------------------------------------------------------------
# Baterias
# ---------------------------------------------------------------------------
BRACOS = [
    ("deixar fugir", 0, 1),
    ("Coletivo ×2", 2, 1),
    ("Coletivo ×3", 3, 1),
    ("Coletivo ×4", 4, 1),
    ("Coletivo ×2 (2 tentativas)", 2, 2),
    ("Coletivo ×4 (2 tentativas)", 4, 2),
]


def bateria(nome, cenario, ranks=(3, 4, 5)):
    print(f"\n{'='*78}\n{nome}\n{'='*78}")
    print(f"{'braço':<28} {'rank':>4} {'captura':>8} {'fuga':>7} "
          f"{'sobrev':>7} {'intacto':>8} {'TPK':>6} {'rodadas':>8} {'VIT%':>6}")
    print("-" * 78)
    tabela = {}
    for rank in ranks:
        for rotulo, n_part, tent in BRACOS:
            random.seed(SEED + rank * 97 + n_part * 13 + tent)
            r = roda(rank, cenario, n_part, tent)
            tabela[(rotulo, rank)] = r
            print(f"{rotulo:<28} {rank:>4} {r['captura']:>7.1f}% {r['fuga']:>6.1f}% "
                  f"{r['sobrev']:>6.1f}% {r['intacto']:>7.1f}% {r['tpk']:>5.1f}% "
                  f"{r['rodadas']:>8.2f} {r['vit']:>5.1f}")
        print("-" * 78)
    return tabela


def veredito(tab, ranks=(3, 4, 5)):
    print(f"\n{'='*78}\nO PREÇO — o que o Coletivo compra e o que ele cobra\n{'='*78}")
    print(f"{'braço':<28} {'rank':>4} {'Δcaptura':>10} {'Δsobrev':>10} "
          f"{'Δintacto':>10} {'ΔTPK':>8} {'preço/pp':>10}")
    print("-" * 78)
    for rank in ranks:
        base = tab[("deixar fugir", rank)]
        for rotulo, n_part, tent in BRACOS[1:]:
            r = tab[(rotulo, rank)]
            dcap = r["captura"] - base["captura"]
            dsob = r["sobrev"] - base["sobrev"]
            dint = r["intacto"] - base["intacto"]
            dtpk = r["tpk"] - base["tpk"]
            preco = (-dsob / dcap) if dcap > 0.5 else float("nan")
            pstr = f"{preco:>9.3f}" if preco == preco else "        —"
            print(f"{rotulo:<28} {rank:>4} {dcap:>+9.1f}pp {dsob:>+9.1f}pp "
                  f"{dint:>+9.1f}pp {dtpk:>+7.1f}pp {pstr}")
        print("-" * 78)
    print("\n`preço/pp` = pontos percentuais de sobrevivência perdidos por ponto")
    print("percentual de captura ganho. Abaixo de ~0,20 a ferramenta é barata;")
    print("acima de ~0,50 ela é uma armadilha bonita.")


if __name__ == "__main__":
    random.seed(SEED)
    V.configura(lee="melee — foice + Wu Xing", teste_publicado=True,
                heuristica="cauda", portao=3, dobra="sim", abertura=True,
                col_ret_todos=True)
    print(__doc__)
    t1 = bateria("CENA A — Chefe + Guerreiro, o Chefe foge a 30%", cena_chefe)
    t2 = bateria("CENA B — dois Elites, o primeiro foge a 30%", cena_elite)
    print("\n\n############ CENA A — CHEFE ############")
    veredito(t1)
    print("\n\n############ CENA B — ELITE ############")
    veredito(t2)
