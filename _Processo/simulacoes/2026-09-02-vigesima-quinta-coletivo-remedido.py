"""Vigésima quinta rodada — REMEDIÇÃO do preço da captura do Golpe Matador Coletivo.

Por que esta rodada existe
--------------------------
A vigésima primeira rodada mediu o preço de captura do Coletivo chamando
`configura()` SEM passar `niveis=`. O default dessa função é "17ª — só a Lee",
que o próprio motor comenta como sendo o bug: três dos quatro PJs rodam sem os
Níveis de Potência que as fichas deles concedem. Os números publicados em
[[⚡ Golpes Matadores]] ficaram marcados como PROVISÓRIOS desde então.

Esta rodada repete a bateria idêntica, trocando uma coisa só:
    niveis="paridade — ordinária"
que é o estado declarado como "condições ordinárias de cena, cada PJ com o que a
nota publicada dele concede".

Mesma seed, mesmo N, mesmas cenas. A diferença entre as duas tabelas é o efeito
do bug, e mais nada.
"""

import importlib.util, os, random, sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
_R21 = os.path.join(_AQUI, "2026-09-01-vigesima-primeira-o-preco-da-captura.py")
_spec = importlib.util.spec_from_file_location("r21", _R21)
R = importlib.util.module_from_spec(_spec)
sys.modules["r21"] = R
_spec.loader.exec_module(R)

V = R.V

def roda(rotulo, niveis):
    random.seed(R.SEED)
    V.configura(lee="melee — foice + Wu Xing", teste_publicado=True,
                heuristica="cauda", portao=3, dobra="sim", abertura=True,
                col_ret_todos=True, niveis=niveis)
    print("\n" + "=" * 78)
    print(f"### {rotulo}  (niveis={niveis!r})")
    print("=" * 78)
    t1 = R.bateria("CENA A — Chefe + Guerreiro, o Chefe foge a 30%", R.cena_chefe)
    t2 = R.bateria("CENA B — dois Elites, o primeiro foge a 30%", R.cena_elite)
    print("\n---- CENA A — CHEFE ----")
    R.veredito(t1)
    print("\n---- CENA B — ELITE ----")
    R.veredito(t2)
    return t1, t2

if __name__ == "__main__":
    print(__doc__)
    roda("A) COMO FOI PUBLICADO — com o bug de Níveis", "17ª — só a Lee")
    roda("B) REMEDIDO — paridade ordinária, o estado correto", "paridade — ordinária")
