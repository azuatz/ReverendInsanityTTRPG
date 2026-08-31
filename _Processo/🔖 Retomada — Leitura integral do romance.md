---
tags:
  - processo
aliases:
  - Retomada — Leitura integral do romance
escopo: processo
---

# 🔖 Retomada — Leitura integral do romance

**Ponto de parada de 2026-08-30, fim de sessão.** Esta nota existe pra que a próxima sessão retome sem reconstruir contexto. Leia-a junto com as últimas entradas do `log.md`.

---

## Estado: a leitura NÃO foi concluída

Foram lançados 18 agentes de leitura integral sobre a fonte primária. **Nenhum chegou a gravar o digest antes do fim da sessão** — os agentes morrem com a sessão, então **a leitura precisa ser relançada do zero**. Nada foi perdido além do tempo de processamento: a fonte está intacta e o plano está aqui.

**A pasta `_Fontes/2026-08-30 — Leitura integral do romance/` está vazia** e é o destino dos digests.

## A fonte primária

```
/home/azuatz/Documentos/Reverend-Insanity-fonte/texto/*.txt   (6 arquivos, ~435 mil palavras)
```

Também existe `Volumes/` com 2.344 capítulos em `.xhtml` — **prefira os `.txt`**, que já vêm limpos e com os capítulos marcados como `Chapter N`.

| Volume | Arquivo | Linhas |
|---|---|---|
| 1 — A Demon's Nature Doesn't Change | `Volume_1_-_A_Demons_Nature_Doesnt_Change.txt` | 32.385 |
| 2 — The Demon Leaves the Mountain | `Volume_2_-_The_Demon_Leaves_the_Mountain.txt` | 40.019 |
| 3 — The Demon Wreaks Chaos in the World | `Volume_3_-_The_Demon_Wreaks_Chaos_in_the_World.txt` | 45.165 |
| 4 — The Demon Lord Rampages Unhindered | `Volume_4_-_The_Demon_Lord_Rampages_Unhindered.txt` | 66.074 |
| 5 — Demon King's Domination | `Volume_5_-_Demon_Kings_Domination.txt` | 177.481 |
| 6 — Demon Venerable's Eternal Life | `Volume_6_-_Demon_Venerables_Eternal_Life.txt` | 73.957 |

## Como relançar (fatiamento usado)

18 agentes, cada um lendo seu trecho **inteiro** com Read em fatias de 2.000 linhas e gravando **um** arquivo em `_Fontes/2026-08-30 — Leitura integral do romance/`:

| Arquivo do digest | Volume | Linhas |
|---|---|---|
| `01 — Vol 1 (parte 1).md` | 1 | 1 – 16.200 |
| `02 — Vol 1 (parte 2).md` | 1 | 16.201 – 32.385 |
| `03 — Vol 2 (parte 1).md` | 2 | 1 – 20.000 |
| `04 — Vol 2 (parte 2).md` | 2 | 20.001 – 40.019 |
| `05 — Vol 3 (parte 1).md` | 3 | 1 – 22.600 |
| `06 — Vol 3 (parte 2).md` | 3 | 22.601 – 45.165 |
| `07 — Vol 4 (parte 1).md` | 4 | 1 – 22.000 |
| `08 — Vol 4 (parte 2).md` | 4 | 22.001 – 44.000 |
| `09 — Vol 4 (parte 3).md` | 4 | 44.001 – 66.074 |
| `10 — Vol 5 (parte 1).md` | 5 | 1 – 29.600 |
| `11 — Vol 5 (parte 2).md` | 5 | 29.601 – 59.200 |
| `12 — Vol 5 (parte 3).md` | 5 | 59.201 – 88.800 |
| `13 — Vol 5 (parte 4).md` | 5 | 88.801 – 118.400 |
| `14 — Vol 5 (parte 5).md` | 5 | 118.401 – 148.000 |
| `15 — Vol 5 (parte 6).md` | 5 | 148.001 – 177.481 |
| `16 — Vol 6 (parte 1).md` | 6 | 1 – 24.700 |
| `17 — Vol 6 (parte 2).md` | 6 | 24.701 – 49.400 |
| `18 — Vol 6 (parte 3).md` | 6 | 49.401 – 73.957 |

**Lições da tentativa de hoje — o que deu errado, e é o que importa:**

Os 18 agentes **leram os trechos inteiros com sucesso** (as respostas finais de cada um confirmam a cobertura: Vol. 1 caps. 1–199, Vol. 2 caps. 200–405, Vol. 3 caps. 406–649, Vol. 4 caps. 650–1021, Vol. 5 caps. 1022–1966, Vol. 6 caps. 1967–2334). **Todos morreram no limite de sessão exatamente no passo seguinte — o de gravar o arquivo.** Zero digests no disco. A leitura toda foi refeita do zero por causa de um único ponto de falha no fim do processo.

Portanto, no relançamento:

1. **GRAVE INCREMENTALMENTE — esta é a lição principal.** Instrua cada agente a criar o arquivo do digest **na primeira fatia lida** e usar Edit pra ir acrescentando a cada 2–3 fatias. Um agente interrompido deixa 70% do trabalho salvo em vez de 0%.
2. **O teto é de 20 agentes simultâneos.** Lance em duas ondas (9 + 9) em vez de 18 de uma vez — e ondas menores também gastam menos limite de sessão de uma vez só.
3. **Diga explicitamente "leia você mesmo, NÃO crie subagentes"** — um dos agentes gastou a vida delegando em vez de ler.
4. **Resposta final curta** (máx. 8 linhas: caminho + contagens) — o conteúdo mora no arquivo, não na resposta.
5. **Considere fazer volume por volume**, em sessões diferentes, em vez do romance inteiro numa tacada. Seis sessões pequenas terminam; uma sessão gigante bate no limite.

### Formato do digest (o mesmo para os 18)

Frontmatter (`tags: [fonte]`, `escopo: referência`) + estas seções em pt-BR, **cada item com o capítulo entre parênteses**:

- **A) Gu nomeados** — tabela: Nome (inglês) · Rank · Caminho · Efeito · Alimentação/refino/aquisição · Cap. **TODOS**, mesmo os menores.
- **B) Sistemas e atividades jogáveis** — instituições, jogos, loops econômicos, atividades organizadas, e **como funcionam** (regras, preços, prêmios).
- **C) Regras do mundo** — fatos mecânicos de cultivo, um por linha.
- **D) Números e preços concretos** — toda quantia dita, linha a linha.
- **E) Locais e o que se faz neles.**
- **F) Golpes matadores e receitas explícitas.**
- **G) Achados soltos para um designer de RPG.**

Exaustivo em A–D; conciso na prosa.

## Depois dos digests — o plano acordado com o autor

1. **Síntese em 3 frentes** (agentes lendo os digests + o vault):
   - **Lacunas do Catálogo** — quais Gu do romance não existem nas 457 entradas.
   - **Fidelidade** — onde o sistema contradiz o texto, e onde uma mecânica canônica está pela metade.
   - **Atividades jogáveis** — inventário do que Fang Yuan e o elenco fazem, cidade por cidade, do rank 1 ao 9 (o pedido explícito: "coisas para os players fazerem", incluindo o que já virou a nota de Metrópoles, e equivalentes para rank alto).
2. **Implementação** — apêndice canônico do catálogo, correções de fidelidade (apontar antes de aplicar quando contrariarem decisão registrada) e notas novas só para as atividades que valerem mesa.

**Critério do autor, que governa tudo:** *completo e fiel ao original, divertido, e sem complexidade à toa.*

## Coordenação com a outra sessão

Há **duas sessões de agente editando este vault**. Combinado em 2026-08-30:

- **Antes de registrar decisão nova:** `grep -oE "^[0-9]+\. " "_Processo/🧭 Log de Decisões.md" | sort -n | tail -1` e use o próximo número. (Já houve colisão em 113–118, resolvida renumerando as da outra sessão para 119–128; esta sessão registrou a **129**.)
- **Território da outra sessão:** `🧠 Dedução`, `👁️ Exposição` e as âncoras delas (`🕵️ Preparação e Informação`, `💪 Atributos`, `🌠 Os Dez Físicos Extremos`, `🏪 Céu Amarelo do Tesouro`); mais `🧩 Refino e Precificação` e `📜 Livro de Receitas de Gu`, onde ela aplicava as decisões 123–125. **Esperar o commit dela antes de editar esses dois.**
- **Território desta sessão:** a pasta de digests, e as notas criadas hoje (`🏙️ Metrópoles`, `🧘 Ritmo de Cultivo e Cultivo Fechado`, `🚀 Gu de Avanço de Rank`, `🎲 Gerador de Heranças`, `💀 A Morte dos Gu`).
- **Decisão 121 da outra sessão (Lua virou Caminho próprio):** já propagada por ela no Catálogo, no Índice e em `🛤️ Os Caminhos`. **A síntese não deve reverter isso.**
- **Estado "Ferido" de Gu** ficou unificado em `💀 A Morte dos Gu`; a regra de refino da decisão 125 é aplicação local dele.
