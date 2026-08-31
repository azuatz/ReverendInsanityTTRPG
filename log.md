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
corrigida, regra arquivada em [[Regras removidas 2026-08-30]] com o motivo do autor.
Cumpre a decisão 103.

## [2026-08-30] ingest | Clipping do repositório GitHub do romance
Segunda fonte recebida: listagem do repositório `azuatz/Reverend-Insanity`. É
ponteiro, não conteúdo — informa que o romance completo em EPUB está sob controle
do autor, o que permitiria checar canonicidade contra a **fonte primária** em vez
da paráfrase da pasta 10. Não ingerido: depende de decisão do autor sobre clonar.

## [2026-08-30] ingest | Grande rodada do autor integrada (decisões 103–118)
A fonte `2026-08-30 — Feedback do autor` + adendos (heranças, missões, dilatação
temporal) foi integrada de ponta a ponta: iniciativa rolada e crítico no 20;
removidos rolagem por média, arcos, desbloqueios de estágio, regen em combate e
aptidão negociável; salto imortal reescrito com a Provação de Avanço (resolve o
9.999/10.000); teto de Marcas total + fonte define o Caminho; via de avanço
explicada em duas regras; Dilatação Temporal 5×–120× com controle de datas;
economia canônica com lojas e Relíquias; ~20 notas tocadas. Antigo em `_Arquivo`.

## [2026-08-30] ingest | Notas novas: Metrópoles, Cultivo Fechado, Gu de Avanço, Gerador de Heranças, Missões
Criadas [[🏙️ Metrópoles — Centros, Tokens e Arena]] (centros 200/600/1.800/5.400,
Token de Sangue em 5 cores canônicas, arena com vitórias líquidas), [[🧘 Ritmo de Cultivo e Cultivo Fechado]] (dias por estágio, pedras 1–16/dia, reclusão), [[🚀 Gu de Avanço de Rank]] (todos os Gu de progressão + tabela de planejamento da mesa) e
[[🎲 Gerador de Heranças]] (rank 4–9, rolado). Salão de Missões e Contribuição do
Clã em [[🏛️ Clãs e Seitas]]. Mapa, Dicionário e notas-mãe atualizados.

## [2026-08-30] canon | Vereditos da rodada: Shang, marcas, tempo, preços
Consultada a pasta 10 em duas varreduras. Confirmado 📕: arena da Cidade Shang,
Relíquias em 5 cores (2 mais altas monopolizadas), leilão como via de Gu raro,
avanço 6→7 por 300 anos + 3 Provações Celestiais, 300 mil Marcas só como gate de
rank 9. Não verificável na base: centros/taxas/tokens, preços por rank,
multiplicadores de tempo de fenda e "milhões de marcas" — entraram como
✍️ autoral/🔧 adaptado por diretiva do autor, com a marcação devida nas notas.

## [2026-08-30] crítica | Nível de Dano deixou de ser moeda única (decisão 112)
Inventário de 118 fontes; 41 convertidas em acerto/RD/CD/atributo em 11 arquivos
(pior caso corrigido: pilha de Força r5 somava +14 Níveis). Combos-exemplo
recalculados. Duplicação de bloco 103–112 no Log de Decisões (escrita simultânea)
fundida num bloco único 103–118; marcador da decisão 16 corrigido para 106.
Pendências novas no Log: simular o motor pós-103–112 e reauditar a economia
imortal sob a Dilatação Temporal.

## [2026-08-30] ingest | Sistema de morte dos Gu (decisão 129)
Pedido do autor: morte de Gu também dentro de Golpes Matadores. Criada [[💀 A Morte dos Gu]] — escada Saudável→Esgotado→Ferido→Morto, mirar Gu manifestado (−4),
escudos que estouram contra 2/3+ ranks, Sobrecarga dos apoios mesmo no sucesso, e a
Queima deliberada (matar 1 apoio por +2 Níveis / vantagem / anular a Brecha).
Ligada em Combate, Golpes Matadores, Gu (nota-mãe), Mapa e Dicionário. Numeração
coordenada com a sessão paralela (peer registrou 119–128; esta entrou como 129).

## [2026-08-30] lint | Correções das 28 contradições (pastas 00–06)
Cinco agentes em paralelo, particionados por pasta. Guia do Mestre tinha **8**
regras revogadas sendo ensinadas (não 2); statblocks do Grimório estavam todos
1,5× abaixo da própria tabela; notas de Caminho, Catálogo de Heranças, Refino e
Formações convertidos do motor v1 para v2 com média conferida; 16 Brechas
escritas (8 no Catálogo de Gu, 8 no Catálogo de Heranças); Dicionário ganhou 12
verbetes; Débito ganhou a seção do Vínculo quebrado. Achados de design pendentes
listados em [[🩺 Lint do Vault]].

## [2026-08-30] canon | Fonte primária instalada
Repositório do romance clonado e convertido: 2.341 capítulos em texto pesquisável
(`~/Documentos/Reverend-Insanity-fonte/texto/`, 28 MB, fora do vault). Nota
[[Fonte Primária — O Romance]] criada na pasta 10 com glossário de tradução.
Schema atualizado: "não verificável na base" deixa de ser veredito aceitável.

## [2026-08-30] schema | Decisões 119–128 e renumeração
Colisão de numeração com a sessão paralela (`reverend-insanity-8a`) resolvida: as
minhas 113–123 viraram **119–128**, e a minha antiga 117 (lojas de Gu) foi
removida por ser duplicata da 113 dela. Registradas: teto do Golpe Matador (119),
Domínio de Formações via gênio pobre (120), Lua é Caminho (121), fonte primária
(122), sistema de receitas — portão + Dedução + receitas imortais + falha canônica
(123–125), Dedução (126), Exposição (127) e insígnia/aura (128).

## [2026-08-30] ingest | Notas novas: 🧠 Dedução e 👁️ Exposição
Criadas em `01 — Fundação` implementando as decisões 126–128. A Dedução conserta
o "+4 em toda Dedução" do Físico da Sabedoria Despreocupada, que apontava para uma
rolagem inexistente. A Exposição universaliza a Assinatura do mercado imortal e
responde "matamos o cara, e agora?". Ligadas à nota-mãe, ao Mapa e às âncoras.

## [2026-08-30] ingest | Duas fontes de outros sistemas
`Homebrew 3DeT — Lamúrias do Reverendo` (adaptação de RI para 3DeT, banco de
ideias) e `Feiticeiros e Maldições v2.5` (o RPG de Jujutsu Kaisen de onde saiu a
Escada de Dano da decisão 9 — 368 págs., para conferir balanceamento e escrita).
Ambas registradas em [[📥 Fontes]]; avaliação pendente.

## [2026-08-30] ingest | Leitura integral do romance — tentativa 1, interrompida
Fonte primária clonada (~/Documentos/Reverend-Insanity-fonte/texto/, 6 volumes,
~435 mil palavras). 18 agentes leram os trechos inteiros com sucesso (cobertura
confirmada: caps. 1–2334), mas TODOS morreram no limite de sessão no passo de
gravar o digest — zero arquivos no disco. Plano de relançamento, fatiamento e a
lição principal (gravar incrementalmente, não só no fim) em
[[🔖 Retomada — Leitura integral do romance]]. Retomar por aí.

## [2026-08-30] crítica | Homebrew 3DeT — 10 candidatos avaliados, 2 adotados
Comparação sistemática contra [[Homebrew 3DeT — Lamúrias do Reverendo]]. 7 de 10
mecânicas já existiam iguais ou melhores no vault (Quebra de Paredes, Pressão da
Abertura, Jogo das Pedras Seladas, backlash de refino, Estrutura do Clã — e o
"Elo da Morte" do Gu Vital foi rejeitado por contradizer as decisões 1 e 18).
Adotados como decisão 130: **Destruição da Abertura** em [[❤️ Recursos e Dano]]
(estado terminal entre sobreviver e morrer) e **Ganhos por criatividade** em
[[⚔️ Combate]] (uso esperto de Gu dá Vantagem, sem custo). Três ganchos de
textura em [[🏛️ Estrutura do Clã]] (diplomacia e fronteiras). Uma terceira
mecânica (Fratura da Abertura em crítico) ficou pendente de simulação, anotada
em "Em aberto" no Log — soma dano incidental ao crítico e não deve entrar sem
medir o impacto na letalidade.

## [2026-08-30] crítica | Auditoria do Feiticeiros & Maldições (fidelidade e estilo)
Achado principal: "Níveis de Dano" em F&M é modificador situacional, não motor de
progressão — o motor real de F&M é um pool de dados por nível de Feitiço,
estruturalmente igual ao `M dX` do vault. A decisão 77–83 converge com F&M melhor
do que uma leitura literal da Escada sugeriria; adendo registrado na decisão 9
para blindar contra reversão futura por engano. CDs, ataque/defesa e crítico
conferem fiéis; Teste de Morte é simplificação deliberada, coerente com a
filosofia "menos coisa pra lembrar" (decisões 97–100). Aplicada 1 de 3 técnicas
de escrita recomendadas: seção "As três regras que valem em toda parte"
(arredondamento, ordem de resolução, não-empilhamento por fonte) na
[[📄 Folha de Referência]] — as outras duas (exemplo resolvido inline, tabelas
rank→CD) ficam como orientação de estilo para notas futuras, não retrofit.

## [2026-08-30] ingest | Sistema de receitas implementado (decisões 123-125)
[[🧩 Refino e Precificação]] ganhou "Deduzir uma Receita" (Fragmentos, aceleradores,
travões) e a falha canônica (1d6 por Gu ingrediente, Explosão ferindo corpo e
alma). [[📜 Livro de Receitas de Gu]] teve o callout de abertura invertido
(receita é portão, não bônus) e corrigiu 4 receitas contra a fonte primária:
Fulgor Lunar (2 Luzinhas, não 1), Quatro Sabores (2 vermes + 4 vinhos, não só
conchas amargas), Viagem Fixa (faltava a base Gu da Viagem Divina), e o Crânio
de Sangue teve a descrição precisada sem mudar o rank de ancoragem — achado uma
contradição de rank entre 3 notas (5 vs 6 vs o cânone que diz 4), registrada em
"Em aberto" no Log, pendente de decisão do autor.

## [2026-08-30] ingest | 4 melhorias + Fratura da Abertura em crítico (decisões 131-132)
Cerco de Terra Abençoada em 3 fases ([[🗝️ Terra Abençoada]]), Âncora do Débito
([[🤝 O Débito]]), traços de fera + Maré de Feras ([[⚔️ Ameaças Genéricas por Rank]])
e Casa-Gu Imortal ([[🔷 Formações de Gu]]) — os itens 4 a 7 do levantamento de
melhorias. Além disso, a Fratura da Abertura em crítico (que estava pendente de
simulação) foi promovida a regra viva em [[⚔️ Combate]] por pedido direto do autor;
fica marcada como não-medida no Log até a próxima rodada de simulação.

## [2026-08-30] crítica | Gênio pobre corrigido: Grão-Mestre no rank 6 era impossível
Achado do autor confirmado e corrigido: com salto de um nível só, nenhum rank 6
alcançava sequer Mestre real (teto 9.999 < piso 10.000), então Grão-Mestre era
duplamente inatingível. Cânone mostra o oposto — Fang Yuan é rank 6 com
Grão-Mestre em dois Caminhos ao mesmo tempo, não é anomalia única. Decisão 133:
gênio pobre agora empilha até 2 feitos de compreensão. Propagado a
[[☯️ Marcas de Dao]] e [[🔷 Formações de Gu]]. Pendente de simulação.

## [2026-08-30] ingest | Ritual do Refino + guia de Golpe Matador reescrito (decisão 134)
Formalizada a escala de condições de refino por rank/raridade em
[[🧩 Refino e Precificação]], reaproveitando as tags 🔨Refino que o Catálogo já
usava sem regra geral por trás. [[⚡ Golpes Matadores]] ganhou guia de montagem
em 6 passos (era 4, sem Brecha); removida seção de contragolpe obsoleta que
duplicava a Retaliação de Essência com números antigos.

## [2026-08-30] simulação | Quinta rodada — Fratura segura, alfa-strike de Alma exposto (decisão 135)
Script novo em Python (`_Processo/simulacoes/2026-08-30-motor-v2-pos-decisao-133.py`),
3.000 iterações/cenário, ranks 1/2/3/5 + cenário novo de rank 6 duplo-gênio.
Fratura da Abertura (132): impacto real de ~0,2pp, bem abaixo da estimativa de
5-10% da auditoria de 3DeT — revisado, sem mudança de regra. Gênio pobre duplo
(133): efeito grande e real, NPC vence 95% das vezes — aviso adicionado a
[[⚔️ Ameaças Genéricas por Rank]], que também teve um exemplo antigo corrigido
(violava o teto de Marcas do rank 6 desde antes de hoje). Achado que precisa de
decisão do autor: dano de Alma sempre ignorou RD, mas nunca foi medido direito
contra vários Mestres de Gu simultâneos — "Padrão" e "Difícil" são hoje muito
mais letais do que a tabela de composição documentava. Números corrigidos com
aviso explícito na mesma nota; a resposta de design fica pendente no Log.

## [2026-08-30] canon | Consumo de pedras do cultivo acelerado corrigido (decisão 136)
Achado do autor confirmado no cânone: citação direta do cap. 34 (Fang Yuan rank 1,
"three primeval stones" por noite de cultivo acelerado) mostra que o vault estava
3× abaixo. [[🧘 Ritmo de Cultivo e Cultivo Fechado]] recalibrada para 3/6/12/24/48
(era 1/2/4/8/16), coluna de custo de estágio recalculada. Coordenado com a sessão
paralela antes e depois da edição (nota é território dela).
