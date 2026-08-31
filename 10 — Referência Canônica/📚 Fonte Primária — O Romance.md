---
tags:
  - referência
  - indice
aliases:
  - Fonte Primária — O Romance
  - Fonte Primária
escopo: referência
---

# 📚 Fonte Primária — O Romance

**O texto integral de Reverend Insanity, pesquisável, fora do vault.** É a
autoridade máxima em canonicidade: as notas desta pasta 10 são paráfrase, esta
é a obra.

> [!warning] Continua valendo: canon não é regra
> Ter a fonte primária **não muda a hierarquia** do `CLAUDE.md` — o romance
> informa o veredito de canonicidade (📕 / 🔧 / ✍️), nunca sobrescreve uma
> decisão do [[🧭 Log de Decisões]]. O que ela elimina é o veredito
> "não verificável na base".

## Onde está

```
~/Documentos/Reverend-Insanity-fonte/
├── Volumes/     2.341 capítulos em XHTML (o EPUB original)
└── texto/       os mesmos capítulos em texto puro — é aqui que se busca
```

Fica **fora do vault** de propósito: são 81 MB e um repositório git próprio,
que não deve ser aninhado no repositório do vault. Origem:
`github.com/azuatz/Reverend-Insanity`. O conversor (`converter.py`) refaz a
pasta `texto/` a partir dos XHTML.

| Arquivo em `texto/` | Capítulos |
|---|---|
| `Volume_1_-_A_Demons_Nature_Doesnt_Change.txt` | 201 |
| `Volume_2_-_The_Demon_Leaves_the_Mountain.txt` | 207 |
| `Volume_3_-_The_Demon_Wreaks_Chaos_in_the_World.txt` | 245 |
| `Volume_4_-_The_Demon_Lord_Rampages_Unhindered.txt` | 373 |
| `Volume_5_-_Demon_Kings_Domination.txt` | 946 |
| `Volume_6_-_Demon_Venerables_Eternal_Life.txt` | 369 |

Cada arquivo traz `## Chapter N: Título` antes de cada capítulo, então a busca
sempre localiza o capítulo do trecho.

## Como consultar

O texto é **em inglês** — busque pelo termo em inglês, não pela tradução do
vault. Da pasta `texto/`:

```sh
# o termo existe? quantas vezes?
grep -ohi "moon path" *.txt | wc -l

# ver o contexto
grep -hi "grandmaster attainment" *.txt | head -5

# em qual capítulo aparece
grep -n -B200 "trecho procurado" Volume_5*.txt | grep "^.*## Chapter" | tail -1
```

**Glossário de busca** — o vault traduz, a obra não:

| No vault | Na obra |
|---|---|
| Caminho (da Lua, do Sangue…) | `moon path`, `blood path` … |
| Marca de Dao | `dao mark` |
| Nível de domínio / Attainment | `attainment` (`master`, `grandmaster`, `supreme grandmaster`) |
| Terra Abençoada | `blessed land` · Gruta-Céu = `grotto heaven` |
| Abertura | `aperture` · Abertura Imortal = `immortal aperture` |
| Espírito da Terra | `land spirit` |
| Golpe Matador | `killer move` |
| Céu Amarelo do Tesouro | `treasure yellow heaven` |
| Pedra de Essência Imortal | `immortal essence stone` |
| Venerável | `Venerable` · Físico Extremo = `extreme physique` |

## O que ela já resolveu

- **A Lua é Caminho, não subcaminho** — `moon path` aparece como Caminho próprio,
  com Imortais rank 6+ dedicados a ele (Yin Wu Que, Half Moon Brutemaster) e
  `moon path dao marks`, distinto de `light path`. Base da decisão 115.
- **Attainment alto num rank baixo é possível e é exceção notável** — *"though
  her cultivation was only at rank six, she had grandmaster attainment in sword
  path"* (Swordmaster You Lan). Base da decisão 114, que manda o Domínio de
  Campo de Batalha no rank 6 passar pela regra do gênio pobre.

## O que ela ainda pode resolver

Os pontos que as auditorias de 2026-08-30 marcaram como **"não verificável na
base"** ([[🩺 Lint do Vault]]): as faixas de % por grau de Aptidão, a escala real
de Marcas de Dao (o autor esperava milhões), os nomes dos Físicos Extremos que
faltam, as três leis do Céu Amarelo do Tesouro, as cores canônicas dos tokens de
cidade, e o desfecho do romance — que a paráfrase da pasta 10 não cobria.
