---
tags:
  - processo
aliases:
  - Log do Agente
escopo: processo
---

# 📜 log.md — Registro cronológico do agente

Append-only. O que o agente fez e quando — uma entrada por operação, as mais
novas no fim. Formato e tipos definidos no `CLAUDE.md` §6.
Consulta rápida: `grep "^## \[" log.md | tail -5`.

> [!info] Este log não é o Log de Decisões
> Aqui fica **o que o agente fez e quando**. O que o *sistema decidiu e por quê*
> vive no [[🧭 Log de Decisões]], que é o contrato das regras. Achados de saúde
> do vault ficam em [[🩺 Lint do Vault]].

---

## [2026-08-30] schema | Instalação do Second Brain
Vault movido de `~/Downloads` para `~/Documentos/REVEREND INSANITY`. Criados
`CLAUDE.md` (schema completo do padrão LLM Wiki adaptado ao RPG), este `log.md`,
`_Fontes/` (fontes brutas imutáveis) e [[🩺 Lint do Vault]].
O `🗺️ Mapa do Vault` assume o papel de index.md do padrão.

## [2026-08-30] lint | Varredura inicial do vault
Script mecânico instalado em `_Processo/ferramentas/lint_vault.py` e rodado nas
144 notas. Estado excelente: 0 colisão de alias, 0 link quebrado real, 0 órfã
real. Corrigido: campo `escopo` adicionado a 9 notas (Portal, Mapa, Sementes e
6 modelos). Achados e pendências de leitura em [[🩺 Lint do Vault]]. Notas
tocadas: as 9 corrigidas + 🗺️ Mapa do Vault + 🧭 Processo.

## [2026-08-30] schema | Repositório git e Second Brain versionado
`git init` no vault com commit inicial das 146 notas; `.gitignore` para o estado
volátil do Obsidian (`workspace.json`). Identidade git definida só neste repo.

## [2026-08-30] lint | Vazamento de escopo (pastas 01–06)
Vespéria (09) está perfeitamente contida — zero NPC/lugar do cenário nas notas de
sistema. O vazamento real é a mesa atual (07) entranhada nas regras: 7 claros
(epicentro na pasta 02, incluindo a "regra do Lee" inteira em [[☯️ Os Cinco Caminhos Wu Xing]]) + 6 limítrofes. Nada editado — aguarda decisão do autor.

## [2026-08-30] canon | Canonicidade das 12 mecânicas centrais
2 mecânicas 📕 canônicas em substância, 9 🔧 adaptadas, 0 inteiramente autorais.
Três desvios não-sinalizados: Marcas de Dao trocando o Attainment canônico
(compreensão) por contagem de Marcas; Supressão Regional vendendo duas extensões
como canônicas; e "Jujuba Vermelha" contra a "Tâmara Vermelha" da própria
referência. Detalhes em [[🩺 Lint do Vault]].

## [2026-08-30] lint | Cobertura do Dicionário para mestre leigo
Prontidão 8/10. 5 divergências (a pior: o [[🎓 Guia do Mestre Iniciante]] ensina cura
`M d10` contra o `M d8` da decisão 14 do [[🧭 Log de Decisões|Log]]), 9 termos órfãos relevantes,
3 jargões sem ponte, 0 verbetes mortos. Nada editado — aguarda decisão do autor.

## [2026-08-30] ingest | Feedback do autor — grande rodada
Fonte recebida em `_Fontes/` (combate, economia, cidades, imortalidade, heranças,
missões, catálogo). Lida e decomposta em **10 frentes de trabalho** registradas em
[[🗺️ Plano de Ingest — Feedback 2026-08-30]]: 7 remoções de combate/criação,
economia canônica, cidades grandes (modelo Cidade Shang), arenas, tempo de cultivo
e pedras, 6 pontos de imortalidade/Marcas de Dao, varredura de Níveis de Dano,
heranças r4–9 com gerador, missões de clã e as 3 aptidões por Gu no catálogo.
Nenhuma nota de regra editada ainda — a auditoria regra × Log de Decisões está
lendo as pastas 01–06 neste momento. Notas tocadas: 📥 Fontes, 🧭 Processo.

## [2026-08-30] ingest | 8 Gu citados pelas regras entram no catálogo
Auditoria apontou Gu citados por função nas regras sem entrada no catálogo. Criados: Casulo de Pedra* (r2), Aríete de Essência* (r3), Arca do Sono Longo* (r4), Âncora dos Três Ares*, Selo do Dantian*, Gu da Reforma (Reform Gu) e Verme do Vinho Centenário* (r5), Gu do Mês (Month Gu, r6 — canônico na família do Tempo, sem asterisco; o Gu do Ano r7 já existia, não foi duplicado). Origens registradas no 📜 Livro de Receitas (📕 Reforma e Mês; demais plausíveis) e entradas indexadas no 🗂️ Índice por Caminho (Comida, Formações, Força, Humano, Sangue, Tempo, Terra). Contagens 449 → 457 em 🪱 Gu, 🧬 Receitas de Combo-Refino e 🗂️ Índice; totais de rank 5 (51/53) e rank 6 (35) atualizados no 📖 Catálogo.

## [2026-08-30] lint | Contradição regra × Log de Decisões (a auditoria pesada)
40 achados: 28 contradições confirmadas, 4 suspeitas, 8 cosméticos. Registrados em
[[🩺 Lint do Vault]]. O **Achado Zero** dominou tudo: as notas citavam as decisões
103–112, ausentes do contrato — uma sessão anterior aplicou o feedback do autor nas
regras e não registrou.

## [2026-08-30] schema | Contrato reconstruído — decisões 103 a 112
Escritas no [[🧭 Log de Decisões]] a partir das notas que as citam: dano sempre
rolado (103), sem armas à distância mundanas (104), iniciativa rolada e crítico no
20 (105), desbloqueios de estágio removidos (106), essência não regenera em combate
(107), procedimento de avanço de rank imortal (108), teto de Marcas é do total
(109), Dilatação Temporal 10×–120× (110), Aptidão rolada é definitiva (111),
fontes menores de Nível de Dano viram acerto/RD (112). As seis decisões antigas
revogadas — 16, 18, 21, 65, 77, 80 — foram marcadas no lugar, com o motivo.

## [2026-08-30] otimização | Removida a rolagem rápida por média
A [[📄 Folha de Referência]] se contradizia sozinha (oferecia a tabela de médias e
declarava "DANO SEMPRE ROLADO") e [[📖 Catálogo de Gu]]`:35` ainda mandava resolver
25+ dados pela média. Tabela removida da Folha e do índice, frase do Catálogo
corrigida, regra arquivada em [[Médias do pool (v1)]] com o motivo do autor.
Cumpre a decisão 103.

## [2026-08-30] ingest | Clipping do repositório GitHub do romance
Segunda fonte recebida: listagem do repositório `azuatz/Reverend-Insanity`. É
ponteiro, não conteúdo — informa que o romance completo em EPUB está sob controle
do autor, o que permitiria checar canonicidade contra a **fonte primária** em vez
da paráfrase da pasta 10. Não ingerido: depende de decisão do autor sobre clonar.
