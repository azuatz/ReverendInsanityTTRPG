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

## [2026-08-30] crítica | Progressão de pedras entre ranks corrigida de ×2 para ×4 (decisão 136 revisada)
O autor apontou que a progressão ×2 entre ranks (recém-corrigida) não batia com
a Densidade da Essência do próprio vault, que já dobra a cada pequeno estágio.
[[🧘 Ritmo de Cultivo e Cultivo Fechado]] recalibrada de novo: 3/12/48/192/768
(era 3/6/12/24/48), mantendo um número por rank em vez de granular por estágio
(que explodiria a >25 milhões/dia no Pico do rank 5). Coordenado com a sessão
paralela.

## [2026-08-31] query | Frente 2 da síntese da leitura integral — fidelidade do sistema ao romance
Lidas as seções C) e D) dos 18 digests inteiros contra as notas de cultivo/economia
mais comparáveis numericamente (Ranks e Estágios, Marcas de Dao, Terra Abençoada,
Ecologia, Ascensão Imortal, Aptidão, Longevidade, O Mercado, Metrópoles, Economia
das Pedras Primordiais). Checado contra o Log de Decisões até a 135 pra não
retrabalhar o que a outra sessão já corrigiu. 5 achados novos gravados em
[[🔍 Síntese — Fidelidade ao Romance]], ordenados por importância: (1) a tabela de
Marcas por Calamidade/Provação erra por 6-8× nas faixas altas (o romance dá números
exatos no cap. 1389, algo que não existia antes desta leitura); (2) o teto de vida
de Veneráveis (decisão 89, ~2.000 anos) fica bem abaixo dos 3.000-25.000 anos
documentados no cânone, e o cap. 563 chama a premissa de "engano comum" — tensão
que precisa ir pro Log, não ser resolvida em silêncio; (3) divergências estruturais
concretas da Cidade Shang real contra [[🏙️ Metrópoles — Centros, Tokens e Arena]]
(faltam dois pedágios de entrada, o 1º/2º distrito são fechados a clã no cânone
mas compráveis na nota, limiares de vitória da arena 5-6× abaixo do real); (4)
tamanho de Terra Abençoada pode estar subdimensionado; (5) distribuição de Aptidão,
baixa prioridade. Nada foi editado — só análise, achados apontados pro autor decidir.

## [2026-08-30] simulação | "Difícil" resolvido de vez — composição escala por rank (decisão 137)
A correção de Alma (decisão anterior) resolveu "Padrão" mas só melhorou
"Difícil" — testando zero Mestres com Alma, o resultado continuou catastrófico,
provando que a causa real era volume de ações (penhasco entre 6 e 8
ações/rodada: 90%→13%, não uma rampa). Autor escolheu, entre 3 opções: composição
escalada por rank, igual o Chefe já faz. Ranks 1-4: 3 Mestres (1 Alma) + 1
Guerreiro; rank 5+: 4 Mestres (2 Alma). Aplicado em [[⚔️ Ameaças Genéricas por Rank]] e [[🎯 Simulação de Combate — Resultados]].

## [2026-08-31] otimização | Metrópoles conferida contra a fonte primária (decisão 138)
Fidelidade (Frente 2/3 da síntese): pedágios de base (10+100 antes dos 5 centros), 2º/1º
centro fechados a dinheiro (sangue de clã, não preço), limiares de arena 30/80 (não
5/15), regra matar-vs-vencer no saque, desafio forçado mensal, teto mundial do token
Cristal Roxo (~200). [[🏙️ Metrópoles — Centros, Tokens e Arena]] atualizada.

## [2026-08-31] ingest | Frente 3 da síntese — Aposta por Procuração e refino territorial (decisões 139–140)
Duas prioridades máximas da síntese de atividades jogáveis (leitura integral,
Fase 4 e 5) implementadas como regra de mesa. (1) Nova nota [[🎰 Aposta por Procuração]] em `05 — Arsenal`: guerra por procuração entre Imortais com peões
mortais infundidos em segredo, Vontade de Batalha por combate e reivindicação
do prêmio acima de 50% — adaptado do "Yi Tian Mountain" do romance, sem nomes
de personagens. (2) [[☯️ Marcas de Dao]] ganhou a seção "Refino territorial —
a guerra fria entre Veneráveis": refino de dao marks em região aberta (não em
Abertura de terceiro), sensação passiva do Caminho na área, amplificar/sabotar
cultivo alheio, e reivindicação territorial exclusiva de rank 9 (a lacuna mais
séria que o topo do jogo tinha). Notas tocadas: `🎰 Aposta por Procuração`
(nova), `☯️ Marcas de Dao`, `🗡️ Arsenal`, `🗺️ Mapa do Vault`, `📔 Dicionário
do Sistema`, `🧭 Log de Decisões` (decisões 139–140 + changelog).

## [2026-08-31] ingest | Frente 1 da síntese — 3 Gu novos no Catálogo (decisão 141)
Os 3 candidatos fortes da síntese de lacunas do Catálogo (leitura integral do
romance) viraram ficha completa, curadoria deliberadamente curta a pedido do
autor. (1) **Gu Imortal do Deus de Sangue** (r6, Sangue): preenchia uma
referência pendurada — o Livro de Receitas e a seção A do próprio Catálogo já
citavam o nome sem ficha; agora tem invocação `32d8+32` com dreno vampírico e
cláusula de contragolpe por sacrifício rancoroso. (2) **Rede Celestial** (r8 →
evolução r9, Celestial): primeiro Gu de combate/defesa do Caminho Celestial —
as 6 entradas anteriores eram todas dedução ou presságio; núcleo do "Véu de
Proteção da Rede Celestial", e a versão r9 potencializa o "Segredo Celestial
Obscurecido" já fichado. (3) **Gu do Voto Envenenado** (r3, Leis): o Caminho
das Leis tinha uma única entrada no catálogo inteiro; este detecta má-fé por
teste de VON antes de selar o pacto, e quebrar o voto selado mata o infrator.
Catálogo de 457 para **460**. Notas tocadas: `📖 Catálogo de Gu` (3 entradas +
4 subtotais de rank), `📜 Livro de Receitas de Gu` (linha 49 corrigida),
`🗂️ Índice de Gu por Caminho` (3 linhas novas + contagens de Sangue, Celestial
e Leis), `🪱 Gu.md` e `🧬 Receitas de Combo-Refino` (contagem 457→460),
`🧭 Log de Decisões` (decisão 141 + changelog). Candidato borderline "Homem
que Triunfa sobre o Céu" (r5) descartado por decisão deliberada, ver a
síntese.

## [2026-08-30] canon | Rendimento de Calamidade e teto de Longevidade corrigidos (decisões 142-143)
Achados da síntese de fidelidade da leitura integral. Grande Calamidade e
Calamidade das Dez Mil estavam 2× e 6-8× abaixo do cânone (Cap. 1389) —
corrigidas em [[☯️ Marcas de Dao]]; a aceleração de frequência por rank fica
como pendência explícita, não resolvida. Teto de Longevidade Imortal subiu de
2.000 para 7.000 anos, mirando a média canônica dos Veneráveis documentados
(Cap. 598-601) — [[⏳ Longevidade]] agora registra abertamente a contradição
com o Cap. 563 (o romance chama a premissa de "engano comum"), mantendo o
mecanismo por necessidade estrutural (decisão 89), não por fidelidade.

## [2026-08-31] ingest | Três Quadros — versão imortal do Salão de Missões em 🏛️ Clãs e Seitas (decisão 144)
Item nº 8 das Recomendações prioritárias da 🔍 Síntese — Atividades Jogáveis por Rank
(Fase 4, digest 17, Vol 6 parte 2, cap. 2241–2251). Nova seção logo após "📜 O
Salão de Missões": Quadro de Contribuição (ranking público), Quadro de
Missões (mesmas graduações ☆–☆☆☆☆☆, escala imortal) e Quadro de Troca (Gu
Imortais, receitas, heranças, e um Venerável ajudando numa tribulação).
Decisão de continuidade: a Contribuição do Clã (CC, decisão 118) não vira
terceira moeda — é o mesmo trilho de mérito emitido por um patrono maior.
Adaptados também o kit de ingresso vigiado e a tribulação assistida (troca
Marcas de Dao por CC, reposição cara depois via Quadro de Troca). Tocados:
`04 — Trilhas de Personagem/🏛️ Clãs e Seitas.md`, `_Processo/🧭 Log de
Decisões.md` (decisão 144 + changelog), `00 — Portal/🗺️ Mapa do Vault.md` e
`00 — Portal/📔 Dicionário do Sistema.md`.

## [2026-08-31] ingest | Três padrões de masmorra do romance consolidados numa nota só (decisão 145)
Itens 3 e 5 da Fase 3 e item 2 da Fase 5 da 🔍 Síntese — Atividades Jogáveis
por Rank. Nova nota 🏯 Torres e Estradas de Prova em `05 — Arsenal`, por
pedido explícito do autor de não inflar o vault com três notas quase
idênticas. Parte 1: gerador de masmorra de andares/blocos com CD crescente
(mesma fórmula do 🎲 Gerador de Heranças), recompensa em 3 faixas, sala de
tesouros por troca de valor equivalente, pilares temáticos com supressão de
Caminho, trilha oculta de "arestas" e entrada paga ao controlador — inclui a
exceção local (opcional, sorteada) de PvP sem autodetonação, suspendendo
⚰️ Espólio só dentro da masmorra, nunca como regra geral. Parte 2: Estrada de
Prova, variante de dificuldade auto-escalada (CD pelo rank de quem anda, não
da masmorra) com Predicaments isolando o desafiante e perseguição coletiva
por quebra de acordo de loot — recomendada pra rank 7–9. Rodapé cita a
Convenção do Caminho de Refino do romance como exemplo worked-out, ligando ao
🚀 Gu de Avanço de Rank (Gu das Cem Batalhas Invicto) já fichado no vault.
Tocados: `05 — Arsenal/🏯 Torres e Estradas de Prova.md` (nova), `05 —
Arsenal/🗡️ Arsenal.md`, `_Processo/🧭 Log de Decisões.md` (decisão 145 +
changelog), `00 — Portal/🗺️ Mapa do Vault.md` e `00 — Portal/📔 Dicionário do
Sistema.md`.

## [2026-08-31] schema | Arco da leitura integral encerrado
[[🔖 Retomada — Leitura integral do romance]] reescrita de nota de "como retomar
após falha" para registro histórico do arco completo: 18 digests, 3 frentes de
síntese, 8/8 recomendações da Frente 3 implementadas (decisões 138-141, 144-145),
mais o sistema de morte dos Gu pedido à parte (129) e as correções de fidelidade
da outra sessão (142-143). Pendências abertas deliberadamente (Terra Abençoada,
Aptidão populacional, candidato borderline do catálogo, aceleração de frequência
de Calamidade) documentadas explicitamente na nota, não escondidas.

## [2026-08-30] ingest | Convenção do Caminho de Refino — última recomendação da Frente 3 (decisão 146)
Nota nova [[🏆 Convenção do Caminho de Refino]] em 03 — Gu: torneio de
attainment coletivo a cada 100 anos, reaproveitando o teste estendido de
[[🧩 Refino e Precificação]] sem número novo — só estrutura de fases (Postos →
Território de Fera) e o prêmio (Marca de Sucesso). Fecha as 8 recomendações da
Frente 3 (atividades jogáveis) da síntese da leitura integral.

## [2026-08-31] canon | Gu do Crânio de Sangue fixado em rank 5 (decisão 147)
Três de quatro notas já diziam rank 5 (Catálogo mestre, Índice, Gu de Avanço);
só [[🩸 Caminho do Sangue]] destoava com rank 6, corrigido agora. Cânone
confirma rank 4 como base (variante rank 5) — 5 é a opção interna mais
próxima. Pendência de "Em aberto" resolvida.

## [2026-08-31] lint | Dicionário conferido contra as 8 notas do arco de leitura integral
Achado real: [[📔 Dicionário do Sistema]] ainda tinha "Vitórias líquidas" em
5+/15+, desatualizado desde a decisão 138 (30+/80+) — corrigido. Adicionadas 3
linhas que faltavam: Sobrecarga (dos apoios), Vontade de Batalha (VB), Kit de
ingresso. Procedimento formalizado em [[🩺 Lint do Vault]] pra repetir depois
de toda rodada grande de notas novas. [[🎓 Guia do Mestre Iniciante]] ganhou uma
linha na trilha de leitura apontando pro cardápio opcional (Torres e Estradas
de Prova, Aposta por Procuração, Três Quadros, Convenção do Caminho de
Refino), que ele não citava.

## [2026-08-31] canon | Economia imortal reauditada sob Dilatação Temporal (decisão 148)
[[⚗️ Materialização e Alquimia Interna]]: tabela de produção (camadas 1-4)
multiplicada ×10, corrigindo a defasagem entre o fluxo antigo (0,5×-3×) usado
no cálculo original e o fluxo atual (5×-40×, decisão 110). Proporções entre
camadas preservadas. Preços do Céu Amarelo e Ração Imortal conferidos e
mantidos — são referência de mercado, não produção. Pendência de "Em aberto"
resolvida.

## [2026-08-31] canon | Escala da Terra Abençoada reconferida (decisão 149)
Achado 4 da `🔍 Síntese — Fidelidade ao Romance` (tamanho de Terra Abençoada,
confiança moderada, só 2 exemplos) reaberto com os 18 digests já salvos.
Achado o grau formal de blessed land por área, citado em 4 capítulos
(609, 690, 939, 1027): Baixo/Médio/Alto/Super por km². Convertido pra mu
(1 km² = 1.500 mu), bate quase em cima das qualidades Comum/Boa/Excelente/
Especial que [[🗝️ Terra Abençoada]] já usava — nenhum número da tabela
"Faixas de resultado" mudou. Nota ganhou 3ª coluna com o grau canônico e
citação, definição inline de "mu", e citação sobre como o tamanho cresce
(Marcas de Dao espaciais e anexação, Cap. 1027/1291/2243). Fecha o achado 4.

## [2026-08-31] canon | Auditoria de fidelidade das notas de Caminho (Alma, Força, Lua, Vento, Wu Xing, Os Caminhos)
Primeira passada nota-a-nota contra os 18 digests da leitura integral (nunca auditadas individualmente antes — a síntese anterior só cobriu Metrópoles/Marcas/Longevidade/Terra Abençoada/Aptidão). Achado real único: subcaminho Encantamento estava mapeado pra Humano em [[🛤️ Os Caminhos]]; os digests confirmam consistentemente que é derivado de Sabedoria (cadeia canônica Pensamento→Vontade→Emoção→Encantamento). Corrigido, decisão 150 — não mexe em dado de combate (Sabedoria e Humano são os dois d6). Achado sinalizado sem aplicar: o dado de Sangue (d8) pode estar subdimensionado frente ao status canônico de "um dos 5 Caminhos de maior poder de combate" — é número de letalidade, registrado em "Em aberto" pra decisão futura com simulação. As outras cinco notas (Alma, Força, Lua, Vento, Wu Xing) fecharam a auditoria sem achado que passasse do filtro de curadoria — várias confirmações fortes de canonicidade sem necessidade de edição (Força de Alma medida "em homens" bate com a unidade canônica "man soul"; teto de poder baixo da Força bate com o romance descrevendo o Caminho como historicamente mais fraco e só com Gu de ataque; o dial de Fase Lunar bate com golpe canônico que cresce de crescente a lua cheia; "fraco em dano direto" do Vento bate com o golpe-assinatura canônico do Caminho, que precisa imitar outros Caminhos em vez de bater forte sozinho).

## [2026-08-31] canon | Segunda passada de fidelidade em [[☯️ Marcas de Dao]] inteira (decisões 151–153)
Auditoria ponta a ponta da nota completa, além do que as decisões 140 e 142 já haviam corrigido. Três achados reais, todos contra os 18 digests da leitura integral e checados contra a fonte primária em inglês onde a citação exigia número exato. **(151)** A pendência de frequência de calamidade/tribulação deixada em aberto pela decisão 142 foi resolvida: a cadência acelera por rank num padrão regular e bem corroborado (Cap. 740/826/1097/1161/1185/1217/1703/1007/2136/2300) — a cada salto de rank, o evento mais frequente do patamar anterior some, o resto acelera um degrau (100→50→10 anos) e um evento novo aparece no topo a 100 anos. Nova tabela de cadência por rank (6 a Venerável) substitui o aviso de pendência; como consequência, os "300 anos por rank" já calculados pro rank 6 generalizam pra ranks 7 e 8 (mesmo padrão "3× o evento de 100 anos"), fechando também o cálculo de calendário externo que ficara pendente. **(152)** Duas correções na mecânica de Anexação: o rendimento de "metade das Marcas" da vítima era otimista demais — o cânone documenta um caso concreto de ~30% (Cap. 1185), com 100% tratado como anomalia exclusiva do protagonista; e o requisito de domínio pra anexar Terra Abençoada não é Grão-Mestre fixo — escala com o rank da terra-alvo (Mestre pra rank 6, Grão-Mestre pra rank 7+, Cap. 735). Sinalizado que [[🗝️ Terra Abençoada]] ainda descreve o requisito antigo — não tocada por estar em uso de outro agente agora. **(153)** A escada de domínio de 6 nomes não tem equivalente pro patamar canônico "Grão-grão-mestre"/"Grande Grão-Mestre" (o que a maioria dos rank 8 atinge, Cap. 1326/1501-1502) — "Quase-Supremo" ocupa o lugar numérico dele mas não é o nome certo. Anotado como 🔧 adaptado com citação, sem renomear (o nome está consolidado em 10+ notas, inclusive um enigma em [[📜 Catálogo de Heranças]] — renomear é decisão do autor). Achado sinalizado sem aplicar, registrado em "Em aberto": a amplificação de poder por Marca pode ser não-linear no topo (Cap. 852: ~+20%/200 Marcas na faixa baixa, mas saltos de centenas a milhares de vezes em rank 8) contra a progressão em degraus fixos (+1 Nível por patamar) da nota — é número de combate/letalidade, não mexido sem simulação.

## [2026-08-31] simulação | Sexta rodada — validação completa pós-decisão 133, Padrão pesado corrigido (decisão 154)
Bateria completa (3.000 iterações/cenário) com `2026-08-31-validacao-completa.py`: ranks 1–5 × 5 tipos de cena, rank 4 medido pela primeira vez, rank 6 duplo-gênio com motor completo, e Golpe Matador Coletivo/cura/controle/terreno simulados pela primeira vez — fechava a pendência mais antiga do Log. "Padrão pesado" corrigido com o mesmo limite de Alma de "Padrão"/"Difícil" (1 dos 2 Mestres, não os 2) e remedido: 77%/68%/71%/88% (ranks 1,2,3,5), substituindo o número obsoleto da terceira rodada. [[⚔️ Ameaças Genéricas por Rank]] atualizada. Três achados viraram pendência nomeada em "Em aberto" (decisão do autor, não correção mecânica): CD do Golpe Matador Coletivo inacessível na fase mortal (~15% de sucesso), terreno reabrindo a decisão 75 (~20pp de variação medida vs. ~4pp na época), e nenhum PJ com Gu de cura na ficha oficial apesar da simulação assumir cura ativa.

## [2026-08-31] crítica | Gu de cura registrado na ficha do Lee (decisão 155)
Fecha a pendência "nenhum PJ tem Gu de cura registrado": Gu do Broto Restaurador (Madeira, arsenal de Cinco Elementos) adicionado à ficha do Lee em [[🎲 A Mesa — Personagens dos Jogadores]] — `M d6`, uma vez por cena, só a toque. Mais fraco que a heurística de simulação usada até aqui (`M d8` sem limite). Simulações futuras devem usar o valor real; fica sinalizado que os números de vitória já medidos carregam margem de cura levemente otimista.

## [2026-08-31] crítica | Repaginada completa da pasta 04 — Trilhas de Personagem
Leitura crítica das 6 notas (🧑‍🎤 mãe, ⚖️ Pontos de Criação, 🌱 Origens, 📋 Guia de Criação de Ficha, 🤝 Vínculos e Acordo de Mesa, 🏛️ Clãs e Seitas) contra o Log de Decisões e o Dicionário. Achados aplicados direto: (1) vazamento de escopo confirmado pendente desde a rodada de lint de 2026-08-30 — os 3 exemplos de Vínculo em [[🤝 Vínculos e Acordo de Mesa]] citavam nomes de PC/jogador (Demvi/Jiāotáng/Lee), genericizados para papéis; (2) os dois "ponteiros hardwired em 'A Mesa'" apontados como limítrofes na mesma rodada (em ⚖️ Pontos de Criação e 🤝 Vínculos) rotulados "(exemplo de campanha)"; (3) [[📋 Guia de Criação de Ficha]] tinha a Aptidão descrita como "piso 20%, teto 99%" — `1d80+20` dá 21–100%, corrigido; (4) [[🏛️ Clãs e Seitas]] tinha uma mesada obsoleta ("2/6/20 Pedras") na tabela comparativa §4, sobrevivente de antes da decisão 90 (40/120/400), corrigida; (5) [[📔 Dicionário do Sistema]] afirmava que Pontos de Contribuição "não converte em Pedra", contradizendo a própria tabela de preços de [[🏛️ Clãs e Seitas]] (4 PC = 10 Pedras, via oficial); corrigido para refletir a via única. Termo "Cerimônia do Despertar", usado sem link em duas notas, agora aponta pro Dicionário/[[🌟 Aptidão e Abertura]]. [[🩺 Lint do Vault]] atualizado marcando os dois achados resolvidos. Nada sinalizado sem aplicar — todos os achados desta rodada eram mecânicos ou vazamento de escopo, sem número de combate envolvido.

## [2026-08-31] crítica | Repaginada completa da pasta 02 — Caminho do Cultivo
Leitura crítica das 9 notas do escopo (♾️ A Ascensão Imortal, 🌟 Aptidão e Abertura, ⛈️ A Vontade do Céu, 🌩️ Calamidades e Provações, 🌠 Os Dez Físicos Extremos, 🧘 Ritmo de Cultivo e Cultivo Fechado, 💠 Economia das Pedras Primordiais, 🧿 Espíritos da Terra, ⏳ Longevidade) contra o Log de Decisões e o Dicionário; [[🪜 Ranks e Estágios]] só lida como referência, não editada (território da recalibração de combate em paralelo). Achados aplicados direto, todos fora de combate/letalidade: (1) [[🌟 Aptidão e Abertura]] tinha dois erros aritméticos — a alegação de que Grau D leva "mais que o dobro" pra encher o tanque contradizia a própria fórmula (Essência e velocidade de recuperação escalam pela mesma %, então o tempo de recarga é **idêntico em qualquer grau** dentro do mesmo estágio; o que varia é o estágio, não a Aptidão — corrigido pra `40 × 2^(estágio−1)` minutos, citando o Pico como o caso extremo real); e a proporção do Grau A ("um a cada duzentos que abrem, ou um a cada seiscentas pessoas") estava com os denominadores trocados e errados — o correto é 1 em 60 dos que abrem, 1 em 200 da população total. (2) [[💠 Economia das Pedras Primordiais]] ainda citava "1–16 pedras/dia" de cultivo acelerado, número pré-decisão 136 que já tinha recalibrado [[🧘 Ritmo de Cultivo e Cultivo Fechado]] pra 3/12/48/192/768; sincronizado. (3) [[🌩️ Calamidades e Provações]] tinha a tabela de frequência congelada em "a cada 100 anos" pra Provação Celestial, Grande Calamidade, Calamidade das Dez Mil e Calamidade do Caos — a decisão 151 já tinha estabelecido que a cadência acelera por rank (100→50→10) e que a Calamidade Terrestre para no rank 8 e a Provação Celestial some no Venerável; tabela corrigida e trocada por um link pra [[☯️ Marcas de Dao]] em vez de duplicar a tabela completa (reduz redundância). (4) [[🧿 Espíritos da Terra]] ainda exigia "nível Grão-Mestre" fixo pra anexar a Terra Abençoada de outro Imortal — a decisão 152(b) já tinha corrigido isso pra escalar com o rank da terra-alvo (Mestre basta contra rank 6, Grão-Mestre só a partir do 7); sincronizado (a própria decisão 152 já sinalizava que [[🗝️ Terra Abençoada]] também precisa desse ajuste, mas aquela nota é território de outra sessão agora, não tocada). (5) [[📔 Dicionário do Sistema]] ganhou as entradas que faltavam pra **Ativação Forçada** e **Pressão da Abertura**, termos usados nas notas do escopo sem âncora no Dicionário. Notas conferidas sem achado: [[♾️ A Ascensão Imortal]], [[⛈️ A Vontade do Céu]], [[🌠 Os Dez Físicos Extremos]], [[🧘 Ritmo de Cultivo e Cultivo Fechado]], [[⏳ Longevidade]]. Nenhum vazamento de escopo encontrado (nenhuma nota cita NPC/lugar de 07–09). Nada precisou ir pro "Em aberto" do Log — todos os achados eram sincronia mecânica com decisões já tomadas, não mudança de número de combate/letalidade nem julgamento de design novo.

## [2026-08-31] crítica | Repaginada completa da pasta 05 — Arsenal (exceto Céu Amarelo do Tesouro)
Leitura crítica das 9 notas do escopo (🗡️ mãe, 🎰 Aposta por Procuração, 📜 Catálogo de Heranças, ⚰️ Espólio, 🎲 Gerador de Heranças, 📜 Manuais e Heranças, 🏙️ Metrópoles, 🤝 O Débito, 🏪 O Mercado, 🏯 Torres e Estradas de Prova) contra o Log de Decisões (155 decisões) e o Dicionário do Sistema. Estado geral: alto — as duas notas mais novas (Aposta por Procuração, decisão 139; Torres e Estradas de Prova, decisão 145) já citam a decisão certa, não duplicam mecânica uma da outra nem de O Mercado, e a escala de preços bate em ordem de grandeza entre si (apostas de Aposta por Procuração e entrada de masmorra calibradas contra as faixas de O Mercado). Nenhum vazamento de escopo — os NPCs autorais das heranças (Xu o Manco, Madame Ye, Gorde Wan, Zhao Ping etc.) são o padrão já autorizado do catálogo, nenhum nome de PC/jogador ou de Vespéria encontrado. Três achados aplicados direto: (1) [[📜 Catálogo de Heranças]], herança "O Jardim que Come" — Terra Abençoada listada como "qualidade Boa (1,5×)", resíduo do fluxo antigo pré-decisão 110 (que fixou Boa = 20×); todas as outras 4 heranças imortais do catálogo já usavam o multiplicador certo (Mesquinha 5×, Comum 10×, Excelente 30×) — corrigido para 20×. (2) [[🏯 Torres e Estradas de Prova]], passo 8 (Entrada) não distinguia moeda: "Pedras fixas na porta" não dizia se, numa masmorra imortal (rank 6+), o valor é em Pedras Primordiais ou em Pedras de Essência Imortal — inconsistente com o resto da nota (que já usa Céu Amarelo para conteúdo imortal) e com o próprio Gerador de Heranças, que faz essa distinção explicitamente ("em Pedras, ou Pedras Imortais, se r6+"); clarificado. (3) [[📔 Dicionário do Sistema]], verbete "Metrópole / Centros" ainda dizia "5 anéis pagos — do 5º (rank 1) ao 1º (rank 5)", desatualizado desde a decisão 138 (2º e 1º centro fechados por sangue de clã, não compráveis por preço nenhum) — corrigido. Nada sinalizado sem aplicar — nenhum achado desta rodada dependia de recalcular número de combate ou de julgamento de design do autor.

## [2026-08-31] ingest | Fantasma de Fera no Caminho da Força, origem do Gu do Empenho Total (decisão 156)
Pedido direto do autor: fenômeno canônico (cap. 280-281) de manifestação rara do fantasma de fera em [[💪 Caminho da Força]] — rank 3+, Gu de amplificação ativo, 1d6 numa Descarga, em 1 manifesta (+2 Níveis, −2 no acerto). [[📖 Catálogo de Gu|Gu do Empenho Total]] (rank 3, já existente) ganhou citação canônica (cap. 285) e a frase de que é a versão garantida do fenômeno. Achado no caminho: uma segunda entrada rank 6 com o mesmo nome "Empenho Total" não tinha relação nenhuma com a cadeia de fantasmas — renomeada para Gu do Suor de Ferro no Catálogo e no Índice, sem receita para atualizar.

## [2026-08-31] crítica | Repaginada completa da pasta 03 — Gu (decisão 157)
Leitura crítica das 13 notas do escopo (🪱 mãe, 💀 A Morte dos Gu, 📖 Catálogo de Gu, 🏆 Convenção do Caminho de Refino, 🔷 Formações de Gu, ⚡ Golpes Matadores, 🚀 Gu de Avanço de Rank, 🗂️ Índice de Gu por Caminho, 📜 Livro de Receitas de Gu, 🧬 Receitas de Combo-Refino, 🧩 Refino e Precificação, 🗺️ Supressão Regional, 🍖 Sustento e Alimento) contra o Log de Decisões (156 decisões) e o Dicionário do Sistema, sem mexer em nenhum número de pool/dano/M/RD de Gu individual (recalibração paralela em andamento na outra sessão). Estado geral: alto — a rodada de lint anterior (achados de "Lua sumindo da lista d8", seção "Comida" em vez de "Alimentação" no Índice, ~25 Gu sem receita) já estava toda corrigida, confirmado por amostragem. Nenhum vazamento de escopo (os nomes Xie Lang/Jiāotáng/Lee/Demvi em [[🚀 Gu de Avanço de Rank]] são o padrão já estabelecido em outras notas de 01–06 pros quatro personagens de calibração, não NPC de campanha). Achados aplicados direto, todos registrados na **decisão 157**: (1) contagem do Catálogo estava errada em 1 — a decisão 141 somou as 3 adições daquela rodada como +3, mas a Rede Celestial (rank 8 → evolução rank 9) ocupa duas linhas na tabela, não uma; real é **461**, corrigido em [[🗂️ Índice de Gu por Caminho]], [[🪱 Gu]], [[🧬 Receitas de Combo-Refino]] e no [[🗺️ Mapa do Vault]] (que ainda citava 457). (2) Dois resíduos de notação v1→v2 no [[📖 Catálogo de Gu]] — mesmo padrão do Gu Explosão Cerebral já corrigido antes: **Gu Espírito Refinado** (rank 4, crase solta quebrando a célula) e **Gu da Noite Que Corta*** (rank 5, pool de passo +4 ilegível, recalculado pela fórmula da própria nota para `16d12 + 64`). (3) [[📜 Livro de Receitas de Gu]] não tinha entrada pro **Gu do Voto Envenenado** (rank 3, Leis, decisão 141) — única das 3 adições daquela rodada sem origem registrada; preenchida com receita nova ✍️ autoral (Gu do Fio de Palavra + Gu do Olhar Firme). Nada sinalizado sem aplicar nesta rodada — todos os achados eram de contagem, formatação ou lacuna de referência, não de balanceamento.

## [2026-08-31] crítica | Motor de combate auditado contra Feiticeiros e Maldições v2.5 (decisão 158)
Pedido direto do autor: recalibrar Vitalidade/dano de Gu/RD "em cima do F&M". Extração completa do livro (sem bestiário/capítulo de mestre) mostrou que F&M não tem alvo numérico explícito de "golpes pra matar", mas o que existe confirma o motor atual: RD é absorção real (não só esquiva), com magnitude 20-50%+ de um golpe médio — igual em espírito ao piso de RD do vault; hits-pra-matar via o único proxy com números concretos (kit de invocações) cai em ~2-5 golpes, a mesma faixa da Tabela de Letalidade dos Caminhos; dano de Feitiço escala em curva exponencial por nível, parecido com o `M dX` que dobra por rank. **Veredito: nenhuma fórmula muda** — o motor já converge com F&M onde ele opina, e diverge só onde já havia motivo documentado (self-similaridade entre ranks, decisão 77-82). Resolvido de quebra: o dado de Sangue (d8) fica como está — o cânone descreve o poder de Sangue como escala via sacrifício, não dano bruto.

## [2026-08-31] ingest | 28 cadeias de Gu Lendários, um por Caminho (dois nos da mesa) — decisão 159
Pedido direto do autor. Três agentes em paralelo rascunharam 28 cadeias completas (rank 1 até 6+, algumas até 9) em staging antes de qualquer edição no Catálogo real, evitando colisão com a crítica da pasta 03 em andamento na hora. Consolidado em nota nova [[👑 Gu Lendários]]: 10 cadeias nos 5 Caminhos de PJ (Alma, Lua, Sangue, Força, Ar — 2 cada, coordenadas pra não duplicar o Empenho Total/Fantasma de Fera da decisão 156), 9 nos demais Caminhos de combate (Água, Fogo, Cosmos, Espaço, Sombras, Luz, Transformação, Escravidão, Veneno), 9 nos Caminhos de suporte d6 (Sabedoria, Alimentação, Refino, Formações, Sonhos, Leis, Informação, Sorte, Humano — duas reaproveitando o Gu da Poesia e o Gu de Inspeção da Sorte já existentes como topo de linhagem, por instrução do autor). Todas seguem o princípio "começa comum, vira lendária no salto em que a receita quebra a Regra de Linhagem" — raridade na receita, não no ingrediente. Fora do total de 461 do Catálogo (coleção separada, mesmo padrão do Gu de Avanço de Rank). Notas tocadas: `👑 Gu Lendários` (nova), `🪱 Gu`, `📖 Catálogo de Gu`, `🗂️ Índice de Gu por Caminho`, `📔 Dicionário do Sistema`, `🗺️ Mapa do Vault`, `🧭 Log de Decisões`.

## [2026-08-31] simulação | Duração de cena medida contra o alvo declarado de F&M (decisão 160)
Autor forneceu 3 PDFs novos de F&M (Grimório de Maldições, Livro do Mestre, Técnicas). O Grimório de Maldições — na verdade um framework de criação de inimigo por Patamar × Nível de Desafio — declara por escrito o próprio alvo: inimigos calibrados para durar 3 rodadas contra a party. Medido no motor da sexta rodada (script novo, contagem de rodadas instrumentada): Padrão/Padrão pesado/Difícil/Clímax resolvem em 7-12 rodadas, 2-4× mais longo. Eixo diferente do que a decisão 158 auditou (aquela mediu acertos-pra-matar de um atacante, que confere); este é duração de cena inteira, nunca medido contra um alvo antes. Sem ajuste aplicado — registrado como pendência nomeada no Log, decisão de mesa do autor.

## [2026-08-31] crítica | Duas pendências fechadas por decisão direta do autor (decisão 161)
Golpe Matador Coletivo (CD 22, ~15% de sucesso na fase mortal) documentado em [[⚡ Golpes Matadores]] como jogada de desespero tardio, não abertura — CD não muda. Terreno do dial de Wu Xing (variação subiu de ~4pp pra ~20pp desde a decisão 75) aceito como intencional em [[☯️ Os Cinco Caminhos Wu Xing]], com a válvula de escape de declarar terreno antes da iniciativa pra mesa que achar forte demais. Nenhum número de combate mudou — são leituras de design sobre resultados já medidos na sexta rodada.

## [2026-08-31] ingest | Feiticeiros e Maldições — bestiário, mestre e técnicas (decisões 160, 162)
Autor forneceu 3 PDFs de F&M (Grimório de Maldições, Livro do Mestre, Técnicas). Nova nota [[🔍 Síntese — Feiticeiros e Maldições (Bestiário, Mestre, Técnicas)]] reúne o que não virou regra ainda: 13 padrões mecânicos de Técnicas (banco curado, nenhum aplicado além do item 3) e 2 padrões de mesa do Livro do Mestre (validar-depois-contrapor otimizador; PvP com dano/RD pela metade e condição "Ferido" escalonada — não avaliado se vale importar). Aplicado o item 3 (Heranças das Sombras): [[💪 Caminho da Força]] ganhou "Herança do Fantasma" — fantasma de fera do Gu do Empenho Total que desliga soma Nível nos que sobram, decisão 162. Mapa atualizado.

## [2026-08-31] simulação | Cura remedida com o Gu real do Lee — sétima rodada (decisão 163)
Pendência da decisão 155: as rodadas 1-6 mediam cura com heurística `M d8` sem limite de usos, mais forte que o Gu real de fato registrado na ficha (Broto Restaurador: `M d6`, 1×/cena). Cópia do script da sexta rodada com só a peça de cura trocada (`_Processo/simulacoes/2026-08-31-cura-real-remedicao.py`), mesma bateria completa (ranks 1-5, 5 tipos de cena, 3.000 iterações, semente `20260830`). Deltas de 0,2 a 5,9pp frente à sexta rodada — mesma ordem de grandeza já tratada como ruído aceitável na decisão 154 — e nenhuma cena muda de lado da linha de 50% de vitória. Nenhuma tabela de [[⚔️ Ameaças Genéricas por Rank]] mudou. Resultado em [[🎯 Simulação de Combate — Resultados#🔁 Sétima rodada — cura real remedida (2026-08-31)]].

## [2026-08-31] simulação | Marcas de Dao no topo — escada linear testada e mantida (decisão 164)
Pendência de "Em aberto" sobre a escada de domínio de [[☯️ Marcas de Dao]] possivelmente achatar o salto que o romance descreve entre rank 7 e rank 8 ("centenas ou milhares de vezes" de amplificação, Vol. 4). Citação verificada por grep na fonte primária antes de usar (confirmada, capítulo real 850/852, mesmo arco). Nova simulação de duelo 1v1 simétrico (rank 8, mesmo motor de dano/ataque/RD/crítico do resto do vault, `_Processo/simulacoes/2026-08-31-marcas-de-dao-nao-linear.py`, 5.000 duelos/confronto) mostra que a escada LINEAR atual já produz vitória esmagadora (>94%) em qualquer confronto que atravesse o Grande Mestre Supremo, o único degrau que dobra o pool. Uma variante não-linear testada em paralelo foi rejeitada: o salto do romance é entre ranks, não entre patamares dentro do rank 8. Nenhuma mudança na escada de [[☯️ Marcas de Dao]] nem em `⚔️ Combate.md`. Resultado em [[🎯 Simulação de Combate — Resultados#☯️ Marcas de Dao no topo — a escada linear já entrega o veredito da ficção? (2026-08-31)]].

## [2026-08-31] ingest | Achados de Baixo Rank — 3 minigames de rank 1-3 (decisão 172)
Nova nota [[🏺 Achados de Baixo Rank]] em `05 — Arsenal`, adaptando 3 recomendações não-priorizadas da [[🔍 Síntese — Atividades Jogáveis por Rank]] (Fase 1 itens 8 e 11, Fase 2 itens 9 e 10), a pedido do autor, focadas em conteúdo pra fase inicial da campanha. Antro de Aposta de Rochas (compra às cegas em 5 faixas de preço, `d20` puro, serviço pago de dissecação pra preservar o Gu vivo); Herança de Força (masmorra pessoal de 4 salas sequenciais, cada uma testando uma virtude — constância, autocontrole, respeito, sorte pura — distinta do Gerador de Heranças e de Torres e Estradas de Prova); Reino do Tesouro (porta viva que só troca por valor equivalente, relógio de 3 respirações/2 rodadas antes do item sacado virar selvagem e hostil). Reaproveita [[🧩 Refino e Precificação]], [[🏪 O Mercado]] e os moldes de [[⚔️ Ameaças Genéricas por Rank]] — nenhum sistema de teste novo. Notas tocadas: `🏺 Achados de Baixo Rank` (nova), `🗡️ Arsenal`, `🗺️ Mapa do Vault`, `📔 Dicionário do Sistema`, `🧭 Log de Decisões`. **Colisão de numeração encontrada e corrigida três vezes** enquanto escrevia: a sessão irmã estava simultaneamente inserindo e renumerando um bloco de 3 decisões próprias (Ancião Externo, Zonas da cidade, Teste de Sucessão Comercial) em outro ponto do Log; minha entrada foi renumerada de 165 → 168 → 171 → **172**, sempre checando duplicata por `grep` antes de fixar o número final.

## [2026-08-31] ingest | Ancião Externo, Zonas da cidade e Teste de Sucessão Comercial (decisões 177-179)
Segunda leva da [[🔍 Síntese — Atividades Jogáveis por Rank]] (Fase 2, itens 6, 4 e 8), três seções novas em [[🏙️ Metrópoles — Centros, Tokens e Arena]] sem tocar nenhum número já corrigido pela decisão 138. **Ancião Externo**: 18 vitórias consecutivas na Arena, ou 80+ vitórias líquidas sustentadas por 90 dias, promovem o lutador a status de ancião (token Ouro, isenção de taxa nos centros de baixo, audiência facilitada, pedido pequeno grátis por arco) — cruzado com [[🏛️ Clãs e Seitas]] (não mexe em Obrigação; serve como "serviço excepcional" opcional pra quem tem clã, e é o mais perto de "ter anciãos" pra quem não tem). **Zonas da cidade**: mapa de bairro funcional além da Arena — Cuidado de Gu (pensão paga, 80–20.000/mês por rank), Luta de Gu (esporte de espectador, só os Gu lutam, sem morte), Refino por Procuração (contratar refinador de fora, 10–50% do valor do Gu) e Leilão em 3 portes por frequência (diário/quinzenal/mensal), mais Aposta em Pedras/Comida/Luz Vermelha como textura leve. **Teste de Sucessão Comercial**: arco de campanha de 3 meses — fundo inicial igual por candidato, 3 checkpoints mensais (CD 15/18/22, teste de CAR ou AST), trapaça formal proibida e fiscalizada, ajuda de aliados tolerada, vence quem lucrar mais líquido; prêmio é o posto com renda passiva. Decisão de forma registrada no Log: virou seção de Metrópoles, não nota independente. Notas tocadas: `🏙️ Metrópoles — Centros, Tokens e Arena`, `📔 Dicionário do Sistema`, `🗺️ Mapa do Vault`, `🧭 Log de Decisões`. **Colisão de numeração com a sessão irmã** (mesmo episódio do log acima, visto do outro lado): minha entrada foi renumerada de 165 → 166 → 169 → 177–179 antes de fixar; avisei a sessão irmã via SendMessage reivindicando 177–179 pra parar a corrida.

## [2026-08-31] ingest | Torneio de classificação prévio, restrição da Ascensão e duas dicas de mestre (decisões 180-182)
Terceira leva da [[🔍 Síntese — Atividades Jogáveis por Rank]], Fase 3 (rank 4-5, mortal tardia/véspera da Ascensão), itens 2, 4, 5 e 6, adaptando eventos já aprovados pelo autor. **Torneio de classificação prévio** (decisão 180, item 2 — Herança da Fairy Bai Hu): nova seção em [[🎲 Gerador de Heranças]], variante opcional pra herança rank 4-6 onde um torneio classificatório prévio decide a ordem de entrada — quem entra primeiro cultiva mais tempo, porque o interior roda mais rápido que o exterior; Gu selados dentro, provação vira teste de Vontade/alma puro, falha ejeta em vez de matar. **Restrição da Ascensão** (decisão 181, item 4): [[♾️ A Ascensão Imortal]] ganhou um callout de aviso e uma nota inline na etapa 2 da provação deixando explícito que ninguém pode ajudar o candidato a equilibrar os Três Ares — nem um Imortal supervisionando, ao contrário do que o modificador geral da tabela sugeria; ajuda externa só vale fora da Ascensão. **Duas dicas de mestre compactas** (decisão 182, itens 5 e 6, formato pedido pelo autor — sem regra formal nova): callout em Gerador de Heranças sobre coalizão temporária multi-facção quando o Chefe da câmara final é forte demais pra um grupo só (reaproveita os moldes de [[⚔️ Ameaças Genéricas por Rank]]); callout em [[🤝 O Débito]] sobre como rodar um arco de guerra entre clãs sem Sistema de Mérito de Batalha formal (subsistema de guerra já rejeitado no Log) — reaproveitando Contribuição do Clã como painel público temporário e "empréstimo de mérito" como Débito comum. Notas tocadas: `05 — Arsenal/🎲 Gerador de Heranças.md`, `02 — Caminho do Cultivo/♾️ A Ascensão Imortal.md`, `05 — Arsenal/🤝 O Débito.md`, `📔 Dicionário do Sistema` (novo termo "Torneio de Classificação Prévio"), `🧭 Log de Decisões`. `🗺️ Mapa do Vault` não tocado: as três notas mudam de conteúdo, mas a linha de resumo de cada uma continua descrevendo a nota corretamente. Território proibido respeitado: nenhum arquivo de `01 — Fundação`, `06 — Grimório de Ameaças`, `🗝️ Terra Abençoada`, `☯️ Marcas de Dao` ou `🏛️ Clãs e Seitas` foi editado (só linkado).

## [2026-08-31] ingest | Governança de Território, cláusula de reclamar e relocação de Terra Abençoada (decisões 183-185)
Quarta leva da [[🔍 Síntese — Atividades Jogáveis por Rank]], Fase 4 (rank 6-7, imortal/Terra Abençoada), itens 1, 4 e 10, eventos já filtrados e aprovados pelo autor. **Governança de Território** (decisão 183, item 1): nova seção leve em [[🗝️ Terra Abençoada]] — framework narrativo, sem números novos — pra quando o território passa da Camada 3 e vira "pequeno reino": o dono nomeia um **governador** pra presidir o dia a dia a partir da cidade principal, distribui subordinados por raça/facção pra conter instabilidades ambientais (linkado a [[🌾 Ecologia e Economia da Terra Abençoada]], nota não editada), e resolve atrito interno com a mesma missão ☆☆ "de embaixador" que os Três Quadros de [[🏛️ Clãs e Seitas]] (decisão 144) já listam. **Cláusula de reclamar** (decisão 184, item 4, "Exchange List"): parágrafo curto na seção do Quadro de Troca em [[🏛️ Clãs e Seitas]] — o dono registrado de um item trocado pode reclamá-lo de volta a qualquer momento via missão obrigatória com compensação extra (50%-100% do CC gasto). **Relocação de Terra Abençoada** (decisão 185, item 10): callout `[!tip]` compacto de 4 linhas em [[🗝️ Terra Abençoada]], formato de gancho de missão pedido pelo autor — transplantar a Abertura pro corpo de uma fera viva que a carrega até o novo local e morre no fim, sem poder usar outro Gu Imortal durante o transporte. Notas tocadas: `02 — Caminho do Cultivo/🗝️ Terra Abençoada.md`, `04 — Trilhas de Personagem/🏛️ Clãs e Seitas.md`, `📔 Dicionário do Sistema` (novos termos "Governança de Território" e "Relocação de Terra Abençoada"; linha "Três Quadros" atualizada com a cláusula de reclamar), `🧭 Log de Decisões`. `🗺️ Mapa do Vault` não tocado — nenhuma nota nova nasceu. Território proibido respeitado: `🌾 Ecologia e Economia da Terra Abençoada` só foi linkada, nunca editada; `☯️ Marcas de Dao` não tocada. Numeração checada por `grep` antes de cada escrita no Log, sem colisão com as sessões irmãs (rank 3-5 fechou em 180-182 pouco antes).

## [2026-08-31] ingest | Alta política de rank 8-9 — pontos de recurso, confronto multi-venerável, ressurreição, guilda de Refino e Cálculo Estelar (decisões 186-190)
Quinta leva da [[🔍 Síntese — Atividades Jogáveis por Rank]], Fase 5 (rank 8-9, alta política entre Veneráveis), itens 3, 4, 6, 7 e 9, eventos já filtrados e aprovados pelo autor. **Escala de pontos de recurso** (decisão 186, item 3): tabela de referência em [[💠 Economia das Pedras Primordiais]] — minúsculo/pequeno/médio (rank 1-5) → grande (6) → gigante (7) → super (8) → auge (9/único), sem mecânica nova. **Confronto multi-venerável** (decisão 187, item 6): seção de referência de mestre em [[☯️ Marcas de Dao]], ao lado do refino territorial — resolve um "Confronto aberto" entre Veneráveis em 3 camadas (Gu Imortal de rank 9 → Domínios → como os ativos se encaixam, decidido pela Escada de Dano normal), mais duas texturas de cena (negociação em pleno combate, aliados atacando em turnos por Marcas conflitantes). **Ressurreição como mercadoria** (decisão 188, item 7): nova seção também em [[☯️ Marcas de Dao]] — tabela de preço em pontos de recurso (até rank 6 = 1 grande; rank 7 = +2 gigantes; rank 8 = negociável; rank 9 fora da tabela), com o portão da **Chave de Qi Humano** coletada em vida como pré-requisito absoluto e o gancho de "chave guardada em segredo por terceiro". Decisão de encaixe documentada no Log: nem `🏪 Céu Amarelo do Tesouro` (território de outro agente), nem nota nova — `☯️ Marcas de Dao` por já concentrar a mecânica política/econômica de Venerável. **Colmeia Flutuante de Refino** (decisão 189, item 4): pipeline de qualificação de guilda de elite em [[🏆 Convenção do Caminho de Refino]] (escolhida sobre `🧩 Refino e Precificação` por ser onde o vault trata carreira social de Refino) — 3 provas reaproveitando o teste estendido existente, aprovação dá 50 anos de acesso, depois reteste. **Formação de Cálculo Estelar** (decisão 190, item 9): callout `[!tip]` de 4 linhas em [[🔷 Formações de Gu]], formato compacto pedido pelo autor — rede viva de inteligência regional que também vira mercado/matchmaking de trocas entre membros de facção. Notas tocadas: `02 — Caminho do Cultivo/💠 Economia das Pedras Primordiais.md`, `02 — Caminho do Cultivo/☯️ Marcas de Dao.md`, `03 — Gu/🏆 Convenção do Caminho de Refino.md`, `03 — Gu/🔷 Formações de Gu.md`, `00 — Portal/📔 Dicionário do Sistema.md` (novos termos: Ponto de recurso, Chave de Qi Humano, Colmeia Flutuante de Refino, Formação de Cálculo Estelar), `00 — Portal/🗺️ Mapa do Vault.md`, `🧭 Log de Decisões`. Itens 1 (refino territorial, decisão 140), 2 (Myriad Tribes Ceremony) e 5/8 deliberadamente não implementados nesta rodada, por instrução do autor. Território proibido respeitado: nenhum arquivo de `01 — Fundação`, `06 — Grimório de Ameaças`, `_Processo/simulacoes`, `🎯 Simulação de Combate — Resultados`, `🌾 Ecologia e Economia da Terra Abençoada`, `⚗️ Materialização e Alquimia Interna`, `🏪 Céu Amarelo do Tesouro`, `🩸 Caminho do Sangue`, `🗝️ Terra Abençoada` ou `🏛️ Clãs e Seitas` foi tocado. Numeração checada por `grep` antes da escrita no Log, sem colisão com as sessões irmãs (rank 6-7 tinha fechado em 183-185 pouco antes).

## [2026-08-31] crítica | Correção e clareza do sistema inteiro contra o F&M
Pedido direto do autor: revisar o conteúdo novo da sessão (correção/balanceamento) e ler 01-06 inteiro contra a régua de clareza do F&M. 5 auditorias em paralelo. Corrigido direto em 01/06 (território próprio): justificativa de design movida pro Log em Combate/Arquitetura, checklist v1→v2 arquivado, Lentidão definida pela primeira vez, dois vazamentos de romance removidos de Exposição, e Ameaças Genéricas por Rank (pior nota da dupla) comprimida de narrativa de simulação pra tabela vigente. Nova nota [[🔍 Crítica — Correção e Clareza (2026-08-31)]] registra os achados de 02-05 (território de outro agente): o padrão "bleed de justificativa" repetido em quase toda pasta, 4 contradições/bugs reais entre notas (anexação de terra, Desequilíbrio em Ecologia, referência órfã em Vontade do Céu, contagem errada em Calamidades), 1 vazamento de escopo real (PJs nomeados em Vento), e gaps de Dicionário (UV, Grau A-D, Retrocesso, Contaminação).

## [2026-08-31] crítica | Sete correções mecânicas da auditoria de clareza aplicadas (decisão 191)
Das notas 02-03 que são minhas: vazamento de escopo e dois bugs de conteúdo em [[👑 Gu Lendários]] (topônimo único, dado faltando no rank 5 da cadeia Sombras, ambiguidade RD×Brecha no Peso Que Nunca Cai); referência órfã removida em [[⛈️ A Vontade do Céu]] (citava regra inexistente em Marcas de Dao); contagem corrigida em [[🌩️ Calamidades e Provações]] ("três coisas" com lista de quatro); contradição entre [[🗝️ Terra Abençoada]] e [[🧿 Espíritos da Terra]] sobre domínio de anexação resolvida a favor da versão já corrigida pela decisão 152b; vazamento de escopo real em [[🌪️ Caminho do Vento]] (PJs nomeados, achado original do primeiro lint deste vault, nunca corrigido até agora) genericizado. Nenhum número de balanceamento mudou. Pendente: o padrão de justificativa-misturada-com-regra e os termos sem entrada no Dicionário (UV, Grau A-D, Retrocesso, Contaminação) continuam em aberto — próxima rodada.

## [2026-08-31] otimização | Materialização repaginada, contradição de Desequilíbrio em Ecologia fechada (decisão 192)
Continuação da crítica de clareza (achados que ficaram assinados pra mim). Materialização e Alquimia Interna: 9+ blocos "Por quê" cortados/reduzidos, changelog de 13 linhas virou nota de rodapé, "~70%" corrigido pra "68%" (o número exato). Ecologia e Economia da Terra Abençoada: a regra de rejeição por Sintonia (Grau 3+) e "Sobrecarga por incompatibilidade" pareciam discordar sobre Desequilíbrio — reescritas pra declarar os dois casos (uma tentativa = zero; insistir repondo = +2/ano). Nenhum número de balanceamento mudou.

## [2026-08-31] otimização | Achados de clareza de 04/05 aplicados — Guia de Criação de Ficha e Pontos de Criação fundidas, exemplo resolvido, Retrocesso linkado
Aplicando os achados de "04 — Trilhas de Personagem e 05 — Arsenal" da `[[🔍 Crítica — Correção e Clareza (2026-08-31)]]`. **Duplicação [[📋 Guia de Criação de Ficha]] × [[⚖️ Pontos de Criação]]**: fundida. Pontos de Criação vira a regra completa (fonte da verdade — orçamento, Aptidão, Origem, Buffs de Lore); Guia de Criação de Ficha vira checklist puro, linkando em vez de reexplicar os passos 1, 2 e 6 (Origem, Aptidão, Nenhum Gu), mantendo só o que é exclusivo dela (fórmulas derivadas, arma, Vínculo, tabela de preenchimento). Cada nota agora diz explicitamente qual papel exerce. **Exemplo resolvido adicionado** em Guia de Criação de Ficha: personagem genérico (ramo secundário de um clã de veneno, sem ligação com nenhum PJ real), Aptidão rolada 60%, os 13 pontos (12+1 de Origem) gastos atributo a atributo, todos os derivados calculados, arma e armadura, e um epílogo com o primeiro Gu conquistado em sessão 1 — cobre o gap "sem personagem de exemplo" citado no achado (referência de formato: o Nanami do F&M). **Retrocesso linkado** pela primeira vez em [[📜 Manuais e Heranças]] e [[🎲 Gerador de Heranças]] → [[❤️ Recursos e Dano]] (nota não editada, só linkada — território de 01). **Ambiguidade de regra não decidida**: se "matar" (VB×2) empilha com "Golpe Matador decisivo" (VB×1,5) em [[🎰 Aposta por Procuração]] — item novo na lista "Em aberto" do [[🧭 Log de Decisões]], sem aplicar multiplicador nenhum na nota (é decisão do autor, não de prosa). Nenhum número de balanceamento mudou em nenhuma nota. Notas tocadas: `04 — Trilhas de Personagem/📋 Guia de Criação de Ficha.md`, `04 — Trilhas de Personagem/⚖️ Pontos de Criação.md`, `05 — Arsenal/📜 Manuais e Heranças.md`, `05 — Arsenal/🎲 Gerador de Heranças.md`, `🧭 Log de Decisões`.

## [2026-08-31] otimização | Três achados de clareza da pasta 03 — Gu aplicados
Os três achados de "03 — Gu" da [[🔍 Crítica — Correção e Clareza (2026-08-31)]] que ainda estavam pendentes (os mecânicos de Gu Lendários já tinham sido corrigidos na decisão 191). **[[🔷 Formações de Gu]]**: os três subsistemas empilhados (Formações Terrestres, Domínios de Campo de Batalha, Casa-Gu tripulada) ganharam rótulo de escopo/rank logo abaixo de cada título e um exemplo único acompanhando o mesmo Mestre de Gu genérico do início ao fim — monta uma Formação Terrestre grau II ainda mortal, abre um Domínio Mestre ao virar Imortal rank 6, e comanda a Casa-Gu de rank 5 do clã — reaproveitando só números já existentes na própria nota, nenhuma fórmula nova. **[[👑 Gu Lendários]]**: confirmado por `grep` que a notação `MD [Caminho]` não aparece de fato nesta nota (a definição real vive em [[📖 Catálogo de Gu#Como funcionam os Gu Imortais]]) — callout no topo explica UV/JV/LB e Marca de Dao com link pras notas-fonte corretas ([[📖 Catálogo de Gu]] e [[☯️ Marcas de Dao]]), não pras sugeridas de antemão no pedido. **[[⚡ Golpes Matadores]]**: seção "Como montar um, passo a passo" movida do fim (depois de ~160 linhas de caso de borda) pra logo após "Estrutura: núcleo + apoio", antes de custo/Brecha/Coletivo/rank 5; conferido que nenhuma nota externa linkava a âncora antiga. Nenhum número mecânico mudou nas três notas. Território respeitado: só `03 — Gu`, nada em `01`, `06`, simulações ou notas do agente irmão.

## [2026-08-31] otimização | Achados de clareza aplicados em Marcas de Dao, Dicionário e Caminho da Força
Aplicando os achados da `[[🔍 Crítica — Correção e Clareza (2026-08-31)]]` que ficaram pendentes pra 02 fora das notas já cobertas por outras rodadas. **[[☯️ Marcas de Dao]]**: cinco blocos "por quê fizemos assim" (nomenclatura Quase-Supremo, empilhamento do gênio pobre, recalibração de rendimento de Calamidade, cadência por rank, e o achado sinalizado de não-linearidade no topo) cortados pra um resumo de uma linha + link, porque a justificativa completa já estava registrada no Log (decisões 120/133, 142, 151, 153, 164) — o último também estava **desatualizado**: a nota ainda dizia "achado sinalizado, não aplicado" quando a decisão 164 já tinha fechado a pendência com decisão negativa (escada mantida). Corrigido pra refletir o Log. Linha ~89 ("Retrocesso de Marca... não vem mais de 'acumular demais'") reescrita — presupunha uma regra anterior nunca declarada na nota; e a definição duplicada de Retrocesso de Marca (linhas ~89 e ~197) virou uma só, mantida na versão mais completa em "O preço" (item 4), com a de "Rank e Marcas" virando pointer pra ela. **[[📔 Dicionário do Sistema]]**: 4 termos usados sem definição em várias notas de 02-05 ganharam entrada — **UV** (Uva Verde, essência imortal do rank 6), **Grau (A/B/C/D)** (mapeamento pra % de Aptidão), **Contaminação** (preço de devorar almas no Caminho da Alma) e **Retrocesso** (contragolpe de refino/Golpe Matador falho — com nota explícita distinguindo do homônimo Retrocesso de Marca). **[[💪 Caminho da Força]]**: a seção "Sinergia Sangue + Força", quase duplicada com a de [[🩸 Caminho do Sangue]] (não tocada, território de outra sessão), encurtada pra um parágrafo-resumo + link pra versão completa lá; mantida a subseção "A cadeia de Corpo aceita os dois" (Gu de Corpo de Sangue compatíveis com a build), que não existe do lado do Sangue. Nenhum número, fórmula ou efeito mecânico mudou em nenhuma nota. Território proibido respeitado: `01`, `06`, simulações, `🎯 Simulação de Combate — Resultados`, `🌾 Ecologia`, `⚗️ Materialização`, `🏪 Céu Amarelo do Tesouro`, `🗝️ Terra Abençoada`, `🧿 Espíritos da Terra` e `🩸 Caminho do Sangue` não foram tocados; nada em `03`, `04` ou `05` além do Dicionário compartilhado.

## [2026-08-31] crítica | Regra do degrau pra Caminho duplo, mito do veterano corrigido, VB fechada (decisões 193-194)
O autor apontou um furo lógico real em [[☯️ Marcas de Dao]]: a frase "veterano
de rank 6 mata rank 7 recém-ascendido" era falsa pela própria tabela da nota —
rank 6 no teto é Pequeno Feito (+1), rank 7 especialista já entra Mestre (+2)
com o dobro de M. Corrigida pra verdade condicional (só vale contra rank 7
dividido entre Caminhos, ou com gênio pobre empilhado). Nova subseção "regra
do degrau" ensina como a divisão entre dois Caminhos realmente funciona
(atribuição por fonte, tabela de impacto por rank, recomendação 70:30-90:10
pensando em degraus e não porcentagem), com canonicidade 🔧 do conflito de
dao marks (Cap. 1272-1275, 1863-1865). E a ambiguidade de VB em [[🎰 Aposta por Procuração]] foi fechada como decisão 193: multiplicadores nunca
acumulam, usa-se o maior — matar com Golpe Matador decisivo é ×2, não ×3.

## [2026-08-31] crítica | Revisão da rodada de otimização da outra sessão (12 commits)
Pedido do autor: verificar, criticar e melhorar o trabalho paralelo. Veredito: os 12 commits (Dicionário, Golpes Matadores reordenado, legenda de Gu Lendários, Marcas de Dao enxugada, Guia de Criação com exemplo resolvido, exemplo triplo em Formações, links de Retrocesso, VB resolvido como decisão 193) estão disciplinados — inclusive corrigiram uma imprecisão da minha própria crítica (a notação "MD" não morava em Gu Lendários) em vez de aplicar cegamente. Dois achados da revisão: (1) erro de unidade no exemplo novo do [[📋 Guia de Criação de Ficha]] — "6% por minuto" corrigido pra "6 pontos por minuto" (240 de tanque = 40 min), verificado contra a fórmula de [[🌟 Aptidão e Abertura]]; (2) contradição pré-existente de 2× na taxa essência↔pedra (20 em Refino/Materialização vs 40 na tabela de Formações de Gu) — exposta pelo exemplo novo, registrada em "Em aberto" por ser número de balanceamento. Todos os demais números dos dois exemplos novos verificados na mão contra as fórmulas-fonte: corretos.

## [2026-08-31] ingest | Três diretivas do autor: divisão leve, teto rompido no salto, regen canônica, Caminho da fenda (decisões 195-197)
Rodada de diretivas diretas: (a) subseção de divisão de Caminhos em
[[☯️ Marcas de Dao]] reescrita em formato leve — só "como funciona + o que os personagens
da obra fazem", sem tabela prescritiva de otimização; (b) o furo "teto do rank
8 é 299.999 mas Venerável pede 300.000 num Caminho" resolvido como na obra: as
condições se consolidam NO rompimento do bloqueio, com as Marcas da provação
final entrando já sem teto ([[🪜 Ranks e Estágios]]); (c) regeneração de
essência refeita no ritmo canônico — % do tanque por hora pelo Grau (D 2 · C 4
· B 6 · A 8, 📕 Cap. 10), recarga em dias e não minutos, sincronizada em 5
notas; (d) nova seção "De que Caminho nasce a fenda" em
[[♾️ A Ascensão Imortal]] costurando as decisões 39/42/84 que estavam soltas — Gu Vital ancora,
trajetória confirma, primeiras Marcas selam, sem Marca prévia necessária.

## [2026-08-31] crítica | Taxa essência↔Pedra unificada em 20, Formações reprecificada (decisão 198)
Aprovação do autor sobre a recomendação do "Em aberto": a taxa passa a ser uma
só no sistema inteiro (1 pedra ≈ 20, a de Refino/Materialização); a tabela de
manutenção de [[🔷 Formações de Gu]] convertia a 40 e foi reprecificada — custo
em essência intacto, equivalente em pedras dobrou (grau IV: 100/dia, 3.000/mês),
calibragem econômica reescrita junto.

## [2026-08-31] crítica | Playtest de leitura — persona "mestre de D&D que nunca leu o romance"
Simulada a jornada completa da trilha do mestre novo (Mundo em 10 Minutos →
Guia do Mestre Iniciante → Folha de Referência) mais as três tarefas reais:
sessão zero (ficha de teste criada do zero), primeiro combate (Padrão rank 1,
2 rodadas rodadas no papel com dados) e entrega do primeiro Gu (Luar, via
Índice → Catálogo → Receitas). Relatório completo com ~20 tropeços em
[[🔍 Playtest de Leitura — Mestre Novo (2026-08-31)]]. Top 5: tabela de
composições da Parte 7 do Guia contradiz Ameaças (Clímax r1 = 4% medido);
dinheiro inicial inexistente ("orçamento de jogo" órfão); régua da Horda errada
na cena-modelo da Parte 3; "Níveis de Dano" sem definição no ponto de uso;
Alma zerada sem regra. Nenhuma nota de regra editada — correções ficam pro autor.

## [2026-08-31] ingest | Entrega sob ameaça (Espólio) e mercador itinerante (Mercado) — decisão 199
Pedido do autor: NPCs como alvo de negociação/extorsão, não só combate. Em ⚰️ Espólio,
a via "Coagir" virou a entrega sob ameaça (Gu entregue refina sem Detonação nem
desvantagem; receita extorquida conta como cópia até validar; Gu Vital jamais; extorsão
escritura como Vínculo quebrado). Em 🏪 O Mercado, o mercador itinerante (📕 Vol. 1,
caravana de Jia Fu): 1d4+1 Gu + 1d4 receitas, ágio +25%, intocável por Espólio + Débito
de rota. Dois termos novos no 📔 Dicionário; linhas do 🗺️ Mapa atualizadas.

## [2026-08-31] ingest | Reis Fera, regra de ondas, Varredura e loadout de Mestre de Gu (decisão 200)
Pedido direto do autor: sistema de hordas gigantes pros Reis Fera canônicos. Nova nota [[🐺 Reis Fera e a Maré]] (06) — os três Reis reusando moldes existentes, a regra de ondas (hordas simultâneas medidas como sentença: 2× = 36-83%, 3× = 0%) e a Varredura (pular onda num teste de grupo, custo calibrado por 1.500 iterações/cenário no motor da sétima rodada). Régua canônica do Vol. 1 cap. 114-115 confere com o medido: Rei de Cem = 99% de vitória a ~60% da Vitalidade; Rei de Mil = 0% pra um grupo só. Molde de Mestre de Gu ganhou loadout em três rolagens (Gu carregados + receita), fechando a metade 06 do pedido de extorsão da decisão 199. Links: nota-mãe, Mapa, Dicionário (Rei Fera, Varredura).

## [2026-08-31] crítica | Correções do playtest de leitura aplicadas no Guia do Mestre
Dos 5 tropeços do [[🔍 Playtest de Leitura — Mestre Novo (2026-08-31)]], os 3
mecânicos corrigidos direto no [[🎓 Guia do Mestre Iniciante]]: tabela de
composições da Parte 7 sincronizada com os números vigentes de
[[⚔️ Ameaças Genéricas por Rank]] (incluindo o limite de Alma que faz parte dos números e o
aviso "Chefe contra rank 1 = 4%, não faça"); régua da Horda consertada na cena-
modelo da Parte 3 (8 vivos = d8, não d10, com a queda pra d6 narrada); e
"Nível de Dano" ganhou definição inline na Parte 2, no ponto onde travava a
leitura. Os 2 achados restantes são lacuna de regra (dinheiro/equipamento
inicial inexistente; Alma zerada sem regra) — decisão do autor, vão pro menu.

## [2026-08-31] ingest | Blocos de gerenciamento do privado: Caderno de Receitas e Ficha da Fenda (decisão 201)
Pedido do autor: modelos copiáveis pro chat privado de cada jogador no Discord.
Criados [[Modelo — Caderno de Receitas]] e [[Modelo — Fenda Imortal]] (com o
adendo do autor: ecologia viva, geração de essência, local de refino e o bloco
de Cicatrizes das tribulações). Pacote Discord ganhou o canal privado com as
Mensagens 9–11 (Fenda segurada até a 1ª Ascensão); nota-mãe 🧰 Modelos e Mapa
atualizados. Zero regra nova; decisão 201.

## [2026-08-31] simulação | Oitava rodada — bateria de grupo nos ranks imortais (decisão 202)
Primeira bateria grupo × cena nos ranks 6-9 (2 perfis de densidade de Marca ×
5 composições × 3.000 iterações, `2026-08-31-oitava-rodada-ranks-imortais.py`,
motor da sétima rodada com o PJ imortal generalizado). Achado: a escada de
dificuldade mortal colapsa — toda cena imortal ≥93% de vitória (Clímax rank 6:
77-85%) e a dificuldade inverte com o rank; diagnóstico instrumentado aponta o
acerto dos moldes (+1/rank vs Defesa +2/rank) como causa dominante. Sem
estagnação no rank 9 (timeout ≤0,1%). Nada corrigido — pendência nomeada em
"Em aberto" pro autor. Também consertados 3 wikilinks quebrados por quebra de
linha no próprio log.md (entradas das decisões 195-197 e do playtest de
leitura — o bug recorrente do vault).

## [2026-08-31] ingest | Kit inicial por Origem (decisão 204)
Escolha do autor no menu de decisões: o buraco de dinheiro/equipamento inicial
(achado 🔴 do playtest de leitura) fecha com kit pronto por Origem em
[[🌱 Origens]] — arma + armadura + Pedras + gancho de sabor por Origem, zero
compra na sessão zero. Sincronizado no passo 8 do [[🎓 Guia do Mestre Iniciante]]
e no checklist/exemplo do [[📋 Guia de Criação de Ficha]]. As
outras duas escolhas do menu (régua ΔB imortal, Colapso Espiritual) + a
diretiva "poder de Alma é raro entre inimigos" estão com a outra sessão
(01/06/simulação — décima rodada a caminho).

## [2026-08-31] simulação | Nona rodada — batalhas solo, 1 PJ contra a cena (decisão 203)
Pedido do autor: cada um dos 4 PJs sozinho contra Mestre de Gu solo, Horda de 8
e o Rei de Cem Feras (Elite + Horda 8, molde de [[🐺 Reis Fera e a Maré]]),
ranks 1/3/5 — 36 células, 3.000 iterações cada, motor da sétima rodada intacto
([[simulacoes/2026-08-31-nona-rodada-batalhas-solo.py]]). Achados: Rei de Cem
solo é sentença (melhor caso 8,4% vs ~99% do grupo); Xie Lang é o único perfil
solo real; Lee colapsa (10-25%); Jiaotang e Demvi trocam de lugar com o rank
(economia de essência). A regra da Horda (1 ataque por personagem de pé) escala
pra baixo solo sem trivializar — item novo em "Em aberto". Resultados na seção
nova de [[🎯 Simulação de Combate — Resultados]].

## [2026-08-31] ingest | Régua ΔB imortal e Colapso Espiritual (decisão 205)
Duas das três marteladas do autor sobre o menu de decisões. [[⚔️ Ameaças Genéricas por Rank]]: callout declarando que a tabela de composição mortal não vale no rank 6+ — cena imortal se dosa por diferencial de domínio (ΔB 0 = passeio · +1 ≈ 20% · +3 ≈ 6%), números da oitava rodada virando régua oficial; opção (c) da pendência da decisão 202. [[❤️ Recursos e Dano]]: Colapso Espiritual pra Alma zerada — inconsciente + Teste de Morte espiritual, coma tratável em vez de morte no terceiro degrau, sequela obrigatória (Contaminação ou −1 VON), morte real só na segunda queda sem tratar. Termo no Dicionário. A terceira martelada (Alma rara entre inimigos + recalibração) é a décima rodada de simulação.

## [2026-08-31] simulação | Décima rodada — Alma rara entre inimigos (decisão 206)
A terceira martelada do autor ("inimigos muito raramente terão poder de alma").
Bateria de três mixes em [[simulacoes/2026-08-31-decima-rodada-alma-rara.py]]
(ranks 1-5 × 5 cenas × mix atual / zero Alma / exceção rolada 1d6, 3.000 it.,
semente 20260830). Achado invertido: Alma rara deixa as cenas 2-17pp MAIS
difíceis (especial de Alma isolada desperdiça o golpe numa barra que nada mais
ataca; a pilha letal já tinha sido removida pelas decisões 135/137). Aplicado o
mix C: molde do Mestre de Gu com especial física por default e cultivador de
Alma em 1d6=6, tabela de composição de [[⚔️ Ameaças Genéricas por Rank]] com os
números novos e sem a linguagem de limite de Alma (obsoleta); Guia do Mestre
Iniciante e Conversão Medieval alinhados. Padrão r1 (62%) e Difícil r1-2
(30/35%) ficam abaixo das faixas sem composição alcançável — fork em "Em
aberto". Seção nova em [[🎯 Simulação de Combate — Resultados]].

## [2026-08-31] ingest | Padrão escalado por rank e piso de ataques da Horda (decisão 207)
Duas marteladas do autor sobre pendências de simulação, ambas em [[⚔️ Ameaças Genéricas por Rank]]. Padrão vira escalado por rank (2 Mestres + 1 Guerreiro no rank 1 = 92% medido; 3 Mestres do rank 2 em diante), fechando a pendência da décima rodada; Difícil de rank 1-2 aceito como quase-Clímax por decisão explícita, com o aviso de "células fora da faixa" substituído pela explicação das duas exceções. A Horda ganha piso de ataques (mínimo 2/rodada contra dois alvos, 3 contra um só), fechando a pendência da nona rodada — sem o piso, a nona mediu cena solo virando atrito de 10-19 rodadas. Fechados também no "Em aberto" os itens já resolvidos pela decisão 205 (composição imortal → régua ΔB). A terceira martelada (encurtar a duração das cenas pra 4-6 rodadas) virou a décima primeira rodada, em curso.

## [2026-08-31] simulação | Décima primeira rodada — encurtando a cena (decisão 208)
Medição isolada das três alavancas de encurtamento da pendência da decisão 160
(RD menor · mais dano por Nível · menos inimigos), contra o alvo do autor de ~4-6
rodadas, com os dois guarda-corpos obrigatórios (curva de letalidade da decisão 78,
penhasco de ações da decisão 137). Script novo
[[simulacoes/2026-08-31-decima-primeira-duracao.py]], 3.000 iterações/célula,
semente 20260830. **Nenhuma alavanca passa limpa — decisão negativa, nada de motor
aplicado.** Baseline 8,13 rodadas; RD menor encurta 6-13% (mas é a única que melhora
a fidelidade à decisão 78), +Níveis encurta 13-23% reescrevendo a escada de
letalidade, menos inimigos encurta 25% e apaga a escada de dificuldade. Achado
estrutural: duração e dificuldade são o mesmo botão (o número de corpos). Duas
hipóteses alternativas medidas e rejeitadas (economia de Essência, barra da Horda).
Única edição de regra: a linha de Padrão pesado de [[⚔️ Ameaças Genéricas por Rank]]
remedida (71/64/63/85 → 63/57/50/76), desatualizada pelo piso de Horda da decisão 207.
Menu de quatro saídas devolvido ao autor em "Em aberto".

## [2026-08-31] simulação | Décima segunda rodada — a peça de muitas ações (opção 4 da decisão 208)

Desenho e medição da única saída que a décima primeira rodada não pôde testar: um
molde de **muitas ações e pouca Vitalidade** (o inverso do Chefe), que na teoria
desacoplaria duração de dificuldade. Desenho do autor — molde "Enxame": `7 × M` de
Vitalidade, Defesa `11 + rank`, Acerto `d20 + rank + 6`, sem RD, 2 ações por rodada,
dano `M d4`, sem Ação Especial. Script novo
[[simulacoes/2026-08-31-decima-segunda-peca-nova.py]] (motor da rodada anterior
intocado; só o molde novo, um seletor de escolha de alvo e a instrumentação do
guarda-corpo novo), 3 composições por substituição × 5 variantes do molde × ranks
1/3/5, 3.000 iterações/célula, semente 20260830. **A hipótese não se sustenta —
decisão 209, negativa, nada aplicado.** Encurta só 5,8% (7,76 → 7,31 rodadas), põe
Difícil em 5,8-23,8% e Clímax em 1,2-40,0%, e deixa o penhasco da decisão 137 mais
íngreme em 4 de 6 células. O guarda-corpo novo ("não pode virar Recruta solto 2.0",
medido como ações executadas por peça antes de morrer) é o que fecha o caso: ignorada
a peça executa 10-16 ações, focada executa 0,56-2,40 — abaixo do Recruta solto — e a
cena não encurta em nenhum dos dois casos, com a dificuldade oscilando 16,2pp em média
(pico 59,3) só pela escolha de alvo do grupo. A varredura de Vitalidade de `7 × M` a
`14 × M` é monotônica: a solda entre duração e dificuldade se repete dentro da própria
peça. Achado colateral: o `+4 × M × Grau` fixo dilui todo molde frágil com o rank.
Notas tocadas: [[🎯 Simulação de Combate — Resultados]] (seção nova + callout do topo),
[[🧭 Log de Decisões]] (decisão 209 + item "Duração de cena" de "Em aberto" atualizado).
Nenhuma nota de regra editada.

## [2026-08-31] simulação | A heurística de alvo vale ±15pp em cena mista (decisão 210)
Achado colateral da décima segunda rodada, medido à parte. Todas as rodadas desde a quinta miram quem tem menor FRAÇÃO de vida — premissa de modelagem nunca examinada, que faz peça frágil intacta ser atacada por último. Comparada contra "mate o menor pool absoluto primeiro": cenas homogêneas não mudam (Padrão/Padrão pesado, 0,0pp), cenas mistas oscilam muito (Clímax r3 +8,2pp; Difícil r3 −15,4pp — matar o Guerreiro primeiro é errado, os Mestres de 2 ações são a ameaça). Leitura: os números publicados modelam um padrão intermediário e plausível, mas carregam banda tática de ±15pp em cena mista — e isso é desenho funcionando (cena homogênea não tem decisão de alvo; mista tem). Nada aplicado. Script: `_Processo/simulacoes/2026-08-31-heuristica-de-alvo.py`.

## [2026-08-31] ingest | O bônus de treino passa a escalar por rank (decisão 211)
Pedido do autor, calibrado contra o F&M como ele pediu: a fonte usa base +2 subindo +1 nos níveis 5/9/13/17 até +6 (cinco degraus em 20 níveis), e "+1 a cada rank par" reproduz a mesma faixa e o mesmo número de degraus nos 9 ranks daqui (+2 · +3 · +4 · +5 · +6). Aplicado em [[💪 Atributos]] com tabela e citação. É número de combate aplicado antes de simulação, por pedido direto — mesmo padrão da decisão 132, com a mesma obrigação de medir na próxima rodada. Interação séria identificada e registrada em "Em aberto": soma até +4 no acerto dos PJs nos ranks altos, justamente o eixo que a decisão 202 apontou como causa do colapso imortal; o lado do inimigo NÃO foi mexido, porque aplicar simétrico no escuro trocaria um desequilíbrio por outro.

## [2026-08-31] ingest | Perícias com lista fechada e o mapa do atalho do Sangue (decisões 212 + seção nova)
Pedido direto do autor, em duas pontas: (1) nova nota [[🎯 Perícias]] — 17
perícias pelos seis atributos, calibradas contra F&M (lista fechada, treino em
degraus), com Bestiário/Refino/Avaliação/Etiqueta de Clã como as quatro do
cenário; 3 treinadas na criação, bônus vindo da tabela da decisão 211 em
[[💪 Atributos]] (fonte única). Sincronizada em Guia, Pacote Discord,
Dicionário, Mapa e nota-mãe; revisão da outra sessão aplicada (link de CD,
linha de Concentração sem regra fantasma, Furtividade decidindo emboscada).
(2) Seção "Por que Sangue avança mais rápido" em [[🩸 Caminho do Sangue]] —
o mapa do atalho do Jiãotáng num lugar só (via de avanço em dobro, custo
reduzido, pagar em Vitalidade, lifesteal, Manto Fervente, sangue de parente),
📕 ancorado na citação da decisão 158, sem regra nova.

## [2026-08-31] simulação | Décima terceira rodada — validação final conjunta (decisão 213)
Validação conjunta do lote 146-212, o mesmo papel que a sexta rodada teve para
as decisões 103-133. Motor corrigido para o **Colapso Espiritual** (decisão 205):
Alma zerada tira o personagem da cena mas não é mais baixa, com o Teste de Morte
físico intacto e nenhuma rolagem nova no loop — efeito medido de **0,00pp** na
vitória do grupo nas 25 células e **+0,003 sobrevivente de 4**, porque a decisão
206 tornou o Colapso raro. Cinco baterias em
[[simulacoes/2026-08-31-decima-terceira-validacao-final.py]] (3.000 iterações,
semente 20260830): mortal completa 1-5, ΔB imortal 6-9, Reis Fera, custo da
Varredura e a decisão 211. **19 das 20 células publicadas conferem dentro de
3pp**; o "~99%" do Rei de Cem e o "0%" do Rei de Mil sobreviveram ao piso da
Horda. **Oito números corrigidos** em [[⚔️ Ameaças Genéricas por Rank]] e
[[🐺 Reis Fera e a Maré]] — os dois graves são a tabela de ações do Chefe (dizia
57% onde a tabela de composição da mesma nota dizia 3%) e a régua ΔB imortal,
que só é dial de verdade no rank 6. Achado colateral: **o motor nunca modelou o
bônus de treino** de [[💪 Atributos]] (+9,9pp de lacuna, mais +2,7 da decisão
211) — fork devolvido ao autor com três saídas medidas, nada republicado, aviso
🔴 na nota.

## [2026-08-31] simulação | Décima quarta rodada — a bateria estendida (decisão 214)
Solo remedido com o piso da decisão 207 (a nona era pré-piso): Horda de 8 × 1 PJ
virou execução (~5 rodadas, vitória 0-37%) e o alvo de 7-9 rodadas solo é
inatingível em toda variante medida; Rei de Cem solo caiu pra 0,0-0,1% (sentença
confirmada). Primeiro PJ×PJ desde a era Perl: sem degeneração generalizada de
1-2 rodadas, mas **Xie Lang vence 84-99,5% de qualquer duelo** via Alma. O
híbrido do treino (mortal sem treino + escada só nos moldes de rank 6+)
recupera os ranks 7-9 como a saída (c) com 0,00pp de custo mortal, mas
superaquece o rank 6 — quarta saída do item 🔴. Script novo em
`_Processo/simulacoes/2026-08-31-decima-quarta-bateria-estendida.py`; seção
nova nos Resultados; anotações em [[⚔️ Ameaças Genéricas por Rank]] e na seção
da nona rodada; dois itens novos em aberto. Nenhuma regra mudou.

## [2026-08-31] ingest | Fork do treino fechado, ranks 7-9 recuperados, Horda solo documentada (decisão 215)
Autor mandou fazer o recomendado nos três itens. (a) Ataque não é ação treinada — treino vale só em perícia; fórmulas de [[💪 Atributos]] corrigidas com callout, e a tabela de composição fica válida sem republicação (a alternativa moveria +12,6pp). (d′) Medida uma variante nova (`2026-08-31-hibrido-treino-rank7.py`): treino nos moldes só a partir do rank 7 — a (d) da 14ª superaquecia o rank 6 (ΔB 0: 51,8→4,4%), o piso em 7 deixa rank 6 e fase mortal idênticos por construção e recupera os ranks 7-9 (ΔB+3: 43/79/98% → 1/5/57%; composição volta a ter gradação, Difícil 23-36%). Fecha a pendência da decisão 202, aberta desde a oitava rodada. (c) Horda × 1 PJ mantém o piso e vira cena de fuga documentada — alvo de duração e piso pedem coisas opostas, e nenhuma variante medida entrega os dois. Três pendências fechadas; restam 2 no Log.

## [2026-08-31] ingest | Nota nova: 📈 O Que Muda ao Subir (checklist de evolução)
Pedido direto do autor: uma lista única do que o jogador precisa mudar na ficha ao subir. Nova nota em `04 — Trilhas de Personagem`, irmã do Guia de Criação (aquele monta a ficha, esta a faz crescer). Três blocos com caixas de conferência: subir de estágio (o "pequeno reino" — só o Grau de Densidade muda, mas mexe em cinco linhas), subir de rank (o M dobra e quase tudo recalcula, com a armadilha nº 1 destacada: trocar os Gu de combate, porque o dado deles cresce com o rank DELES, não com o do dono) e ascender (o que acaba — estágios, B, Pressão da Abertura, tanque próprio — e o que nasce — Caminho cristalizado, Marcas, Terra Abençoada, UV, Calamidades no calendário). Fecha com 6 itens que quase todo mundo esquece. Zero regra nova: tudo é reunião do que já está em Ranks e Estágios, Combate, Atributos e A Ascensão Imortal.

## [2026-08-31] otimização | RD deixa de empilhar; acerto de Combate alinhado à 215 (decisão 223)
Pedido do autor por sobrecarga de mesa. Medido antes de simplificar: a segunda fonte de RD adiciona no máximo +2 e nunca escala (Gu de defesa é `base × M` e dobra por rank; armadura mortal é fixa em 1-4) — 3-12% da RD total no rank 5. Decisivo: o motor de simulação nunca modelou empilhamento (PJ sempre teve `rd = 1 × M`, sem armadura), então as quinze rodadas já rodaram sob a regra simplificada — adotá-la alinha o texto com a medição em vez de manter divergência silenciosa. De quebra, corrigido o `+ treino` residual na fórmula de acerto de [[⚔️ Combate]], que contradizia a decisão 215 e só tinha sido corrigido em [[💪 Atributos]].

## [2026-08-31] ingest | Xie Lang perde o Físico Extremo, e os Dez Físicos viram material de mestre (decisões 216 e 217)
Duas diretivas do autor, na mesma rodada. O Xie Lang fica com Aptidão 86% fixa e ganha o Buff de Lore *Ressonância da Montanha Fria* (Lua e Alma como um Caminho só) no lugar do físico — lore nova do autor: ele sobreviveu ao massacre dos pais pela ressonância de um Gu residual na montanha fria. Os Dez Físicos Extremos saem por completo da criação de personagem (pacote de 8 pontos, Abertura Incompleta e os sete Marcos deixam de existir) e a nota foi reescrita como ferramenta de mestre, com três papéis de campanha e a mecânica reapresentada como ficha de NPC; versão jogável em `_Arquivo/` com alias versionado. Varredura em 20 notas. Tabelas de dano do Xie Lang recalculadas sem o +1 do físico, e a rota do Gu Imortal do Crânio de Sangue — que concedia um Físico Extremo — fechada e trocada por elevação de Abertura.

## [2026-08-31] ingest | Marcas de Dao viram faixas flutuantes, ganham conflito de Caminhos e substituem os pequenos reinos (decisões 218, 221 e 224)
Os tetos duros de 9.999/99.999/299.999 foram revogados: as faixas viraram descritivas (6 = 1.000–10.000 · 7 = 10.000–100.000 · 8 = 100.000–300.000) e dá pra passar do topo continuando no mesmo rank, pagando em Vontade do Céu escalada em vez de sobrecarga física. O rank 9 vira a única trava rígida — 300.000 no Caminho principal —, o que transforma "Venerável é coisa de especialista" em teorema. Conflito de Caminhos ganha três relações (complementar +25% · neutro +50% · incompatível +50% mais anulação de domínio, −1 Nível de Potência e Ferimento permanente na Fenda). E a contagem de Marcas passa a dar a Densidade Imortal, ocupando o lugar que os pequenos reinos ocupam na fase mortal — a extensão acima do topo da faixa ficou retida para medição.

## [2026-08-31] canon | Varredura da fonte primária sobre manifestações passivas de Marcas de Dao (decisões 219 e 220)
Três agentes varreram os seis volumes. Achados que mudaram premissa: **mortais têm Marcas de Dao**, gravadas no corpo desde o rank 1 (Cap. 764, 950, 1272), sendo a Fenda um segundo reservatório e não o primeiro; o cânone **não conhece Caminhos complementares** (o eixo é binário, e o conflito cresce com o acúmulo — Cap. 1064, 1102), então a gradação em três níveis ficou marcada ✍️ autoral; e o Fantasma de Fera do Caminho da Força é governado por **densidade de Marcas da mesma fera mais sorte**, não por rank — o exemplo canônico que mais dispara é rank 2 no Pico. Regra reescrita. Publicada também a tabela de manifestações passivas dos 30 Caminhos para o mestre usar em NPC, quase toda descritiva, e a tabela de ganho percentual de dano por patamar de domínio.

## [2026-08-31] ingest | Teto de 16 dados e Nível de Potência (decisão 225)
Autor propôs remover o M e escrever cada dado/RD à mão como o F&M. Recomendação contrária, aceita: o F&M tem ~50 feitiços × 6 níveis, aqui são 460 Gu × 9 ranks — e a decisão 158 já mediu que o método do F&M produz drift (acertos-pra-matar sobem com o nível), que é justamente o que o M impede. Mas metade da queixa era real: 256 dados no rank 9 contra os 28 do maior pool do F&M. Adotado teto de 16 dados com o excedente virando bônus fixo — média idêntica em todo rank, fase mortal intocada (M nunca passa de 16 lá), desvio cai no rank alto. Renomeado "Nível de Dano" → "Nível de Potência" com tabela de faces (uma face por Gu) e o callout de que Nível nunca toca RD. Registrada como recusada a proposta de tornar `+ FOR` multiplicativo: o diagnóstico está certo (e o F&M concorda — ele usa "+1 por dado" quando quer que um bônus continue valendo), mas as duas únicas coisas fixas do motor são deliberadas, e `+ FOR` é o pilar do poder emprestado.

## [2026-08-31] simulação | Décima quinta rodada — tribulação, face RD e a mesa sem o Físico (decisão 226)
Construído o **motor de tribulação**, que catorze rodadas de combate nunca modelaram (`_Processo/simulacoes/2026-08-31-decima-quinta-tribulacao-e-potencia.py`; 3.000 iterações/célula, 20.000 carreiras na reprodução, semente 20260830). Reproduz a curva da quarta rodada (2,2/48,3/70,2% → 0,2/49,9/76,2%) num motor escrito do zero. Três vereditos pedidos pelo autor: **a CD de Calamidade é a fórmula de 🌩️ Calamidades** (a de ⛈️ A Vontade do Céu conta a faixa duas vezes e torna Perseguido/Alvo do Céu insobrevivíveis); **a escala de escalonamento por excesso de Marcas é brutal e não-monotônica** (banda de +20% deixa 2,9% de sobrevivência por século, contra 25,7% da banda de >+50%); **a face RD não entra** (confirma a decisão 220 com cena: estoura 7-9 rodadas sem melhorar a vitória, +0,54 a +0,66 na escada da decisão 78, +14,85pp de vitória de grupo); e **o Xie Lang sem o Físico não cai para o mais fraco** — perde 1,0pp e segue vencendo 97,8-99,5% de qualquer duelo, porque a dominância vem do Caminho da Alma. Editados: `🎯 Simulação de Combate — Resultados` (seção nova + callout do topo) e `🧭 Log de Decisões` (decisão 226, cinco itens em "Em aberto", changelog). Nenhuma nota de regra tocada.

## [2026-08-31] canon | Fidelidade das tribulações checada na fonte primária (decisões 229 e 230)
Dois agentes varreram os seis volumes atrás de como os Imortais atravessam tribulações e do que as tribulações são. A escada confirmou inteira (Terrestre → Celestial → Grande → Dez Mil → Caos), junto da atribuição por rank, da perda da Calamidade Terrestre no rank 8, da cadência 10/50/100 com três repetições precedendo o avanço, e do fato de as tribulações caírem dentro da Fenda e não no mundo. Um erro achado e corrigido: o vault dizia que o céu **nunca** usa o Caminho do alvo contra ele, e o cânone diz o contrário — a Calamidade comum vem no Caminho do próprio cultivador, porque é ela que grava as Marcas dele. A regra antiga foi reposicionada como a escalada da Tribulação sob medida, que só existe da faixa Marcado em diante.

## [2026-08-31] ingest | Tribulação ganha subsistema de preparação e economia de falha (decisão 229)
A pedido do autor, para que quem planeja direito quase sempre passe e a falha vire perda recuperável em vez de morte. Três alavancas novas, todas canônicas: Essência Imortal queimada na defesa (−1 por 100 UV, até −3), tempo interno desacelerado (−1 por ciclo, até −3) e Golpe Matador defensivo registrado (−2), somadas às três que já existiam. A sétima preparação é a escolha do local, que decide o feitio da Calamidade e de que Caminho serão as Marcas colhidas. Ativar Gu dentro da sequência passou a custar desvantagem na etapa seguinte, para impedir a resposta improvisada. E a falha passou a poder ser comprada com recurso permanente — queimar o Gu núcleo, raspar uma camada da Fenda, ou aceitar um Ferimento que vira Marca de Dao e nunca cura. Golpes Matadores defensivos ganharam seção própria, com os Níveis indo para duração, cobertura, usos e CD, nunca para RD. Números enviados à bateria.

## [2026-08-31] crítica | O teto de redução fica fixo — teto móvel rejeitado com número (decisão 229, item j)
Medida a interação entre o teto de −4 e a escala por patrimônio: numa Provação de rank 6, a sobrevivência do preparado cai de 91,3% (camada 2) para 86,9% (camada 3) e 81,2% (camada 4). A suspeita de que enriquecer derrubava o preparado abaixo do alvo estava certa, mas a correção proposta — teto subindo junto com a camada — foi recusada por cancelar a escala com exatidão matemática, anulando a regra do patrimônio. O que fecha o buraco é a compra de sucessos, e ela fecha melhor para quem é rico: comprar um sucesso devolve a camada 4 a 96,9%, e as três moedas de compra (Gu Imortal, camada da Fenda, corpo) são patrimônio. A riqueza levanta a barra e paga a passagem no mesmo movimento. A leitura das três peças como mecanismo único foi publicada na própria nota, com a tabela, para impedir conserto futuro sem ver o conjunto.

## [2026-08-31] simulação | Décima sexta rodada — o Xie Lang 80:20 e o nerf do Caminho da Alma (decisão 231)
Duas diretivas do autor medidas juntas (`_Processo/simulacoes/2026-08-31-decima-sexta-nerf-alma.py`, cópia do motor da décima quinta; 3.000 iterações/célula, semente 20260830, mix de Alma C). **Correção de modelagem:** quinze rodadas trataram o Xie Lang como atacante de Alma puro; ele é **80:20 Lua:Alma** (Lua é d8 e atravessa RD). No perfil certo a dominância de PvP dele cai de 83,9/97,8/99,5% para **33,4/39,9/43,6%** — 3º de 4 nos três ranks, com o Jiāotáng virando o novo topo (93,5/78,3/70,3%). Fecha o item de PvP aberto desde a décima quarta. **Nerf:** a diretiva culpava o furo de RD, mas o número novo da rodada (acertos para zerar a **barra de Alma**: 1,85/2,12/2,21 contra os 2,8 da decisão 78) mostra que a dominância vinha da barra um terço menor que a Vitalidade e da Defesa crescendo +1/rank contra um acerto de +2/rank. Medidos três candidatos contra um especialista 100%-Alma: meia-RD (−0,6pp) e d10 (−1,4pp) são nerfs no papel; a **barra endurecida** corta −12,4pp (99,5% → 87,1%), leva a escada a 2,63, não move dado nenhum e custa +0,24pp na bateria de grupo com o quinhão de dano do Caminho inalterado. Editados: `🎯 Simulação de Combate — Resultados` (seção nova + callout do topo), `🧭 Log de Decisões` (decisão 231, item de PvP fechado, quatro itens novos em aberto, changelog) e `01 — Fundação/⚔️ Combate.md` (Alma máxima, Defesa contra Alma, callout na Tabela de Letalidade, changelog). Ripple de oito notas com a fórmula antiga e duas correções em `👻 Caminho da Alma` reportados em aberto — a nota da Mesa e a pasta `02` estavam com a sessão paralela.

## [2026-08-31] lint | Sincroniza a fórmula de Alma máxima da decisão 231 nas notas de 01 e 04
A décima sexta rodada aplicou o nerf em ⚔️ Combate mas deixou a fórmula antiga em 15 outras notas — inclusive em [[❤️ Recursos e Dano]], que é a casa canônica dela. Sincronizadas as minhas: Recursos e Dano, Atributos e O Que Muda ao Subir. As demais (00, 02, 04-Guia, 07, _Modelos) são território da sessão paralela e foram repassadas.

## [2026-08-31] crítica | O multiplicador de melee qualifica por função do Gu, não por Caminho (decisão 232)
Verificando se a build melee nova da Lee (foice + Gu de melee Wu Xing, diretiva do autor) era sustentável, achei que a regra de [[⚔️ Combate]] dizia "Gu do Caminho da Força ou de Transformação" enquanto o [[📖 Catálogo de Gu]] já traz Gu de melee nos cinco elementos concedendo o pool (Punho de Montanha, Terra r3, faz `4d12`; Manto de Carvão, Fogo r2, faz `2d12`). A regra descrevia um sistema mais estreito que o publicado. Corrigida para "Gu que amplifique ou entregue um golpe corpo a corpo" — qualifica a função, não o Caminho. Pilar intacto (Força fora do pool, poder emprestado da criatura); Força e Transformação seguem sendo quem faz melhor e mais barato. Nenhuma simulação invalidada: o motor nunca modelou a restrição por Caminho.

## [2026-08-31] ingest | A Lee vira personagem de corpo a corpo, e é ela — não ele
Diretiva do autor. A Lee passa a lutar de foice (arma pesada, `d10`), atacando por FOR +3, com os Gu de melee elementais dos cinco Wu Xing multiplicando o dano pelo `M` deles e os Gu de suporte completando. O autor também se refere a ela no feminino, o que a nota não marcava — corrigido em toda a seção dela e nas menções cruzadas. A mudança tornou obsoletas todas as células de simulação que a envolvem (o motor a modelava como conjuradora de `d8` por VON), inclusive as de PvP recém-publicadas contra o Xie Lang; marcadas como fora até a remedição. Sincronizada também a linha de [[💪 Caminho da Força]] que ainda exigia "um Gu do Caminho da Força ou de Transformação" para o multiplicador de melee — a regra passou a qualificar a função do Gu, não o Caminho (decisão 232), porque o Catálogo já publicava Gu de melee nos cinco elementos. E registrada a decisão do autor de encerrar a questão do Jiāotáng: "é normal melee ser mais forte antes, está ok" — a vantagem de rank 1 dele é pretendida, não desequilíbrio.

## [2026-08-31] ingest | O buff do Xie Lang ganha uma segunda metade, e a mesa ganha ordem de força declarada (decisão 233)
Diretiva do autor, motivada pelo achado da décima sexta rodada: o Xie Lang estava perdendo do Demvi nos ranks 3 e 5 (38,1% e 39,5%), inversão na ponta de baixo da mesa, já que o Demvi é quem deveria fechar a fila por Aptidão (56%, Grau C) e por Caminho. Entra na Ressonância da Montanha Fria: Golpe Matador que mistura Lua e Alma não paga a dobra de custo de híbrido, e a Retaliação é a normal — o Corte do Minguante misto dele cai de 1.280 para 640 de essência no Pico do rank 2. Deliberadamente não entra: as Marcas continuam se dividindo entre os dois Caminhos, com os +25% de progressão. A ressonância une os dois no instante da técnica, não na carne — é o que separa este buff do Físico removido e mantém a decisão 227 de pé. Publicada junto a ordem de força pretendida da mesa, para calibrar medições futuras. Encerrada a questão do Jiāotáng por decisão do autor: os 93,5% de rank 1 dele são comportamento pretendido.

## [2026-08-31] otimização | Salto para Venerável sem os tetos duros, e o bloqueio do Dao Celestial ganha regra (decisão 234)
Limpeza de resíduo da decisão 218: a nota de Ranks e Estágios ainda explicava as condições do salto pela mecânica do teto duro de 299.999, com a quarta condição "expandindo o teto no próprio evento". Sem os tetos, a explicação ficou mais simples e mais dura — o candidato junta os 300.000 no Caminho principal por acúmulo real, antes de tentar, com o total bem acima disso e pagando escalada da Vontade do Céu no percurso inteiro. E o bloqueio do Dao Celestial, que era citado de passagem e nunca tinha regra, ganhou seção própria: três frentes simultâneas (Destino, Longevidade e a provação de CD 20 com dano dobrado), as duas contramedidas canônicas (Caminho Humano e Caminho da Sorte) e a rota suja de empilhar tribulação sobre tribulação. Desenhado para a mesa inteira jogar, não só o candidato.

## [2026-09-01] simulação | Décima sétima rodada — a Lee em corpo a corpo e a isenção do Xie Lang (decisão 236)
Duas diretivas de ficha medidas juntas (`_Processo/simulacoes/2026-09-01-decima-setima-lee-melee-xie-buff.py`, 3.000 iterações/célula, semente 20260830; baseline reproduz a décima sexta em 0,0pp nas doze células de PvP). A Lee de foice (`d10` pesada, ataque por FOR +3, Níveis vindos da escada Wu Xing 🔨amplifica do Catálogo rank a rank — a foice com esses Níveis reproduz literalmente `4d12+4+FOR`, `8d12+16+FOR` e `16d12+48+FOR`) sai de última da mesa para segunda ou primeira: PvP de 29,7/32,1% nos ranks 3 e 5 para 67,4/75,5%, e solo de 5,3/5,8/18,2% para 36,6/30,7/61,7%. A isenção de híbrido do Xie Lang mede 0,0pp em todas as doze células de PvP porque o Golpe Matador não dispara em duelo — e a regra concorda com o motor ("contra Mestre de Gu: não, ataque normal rende mais"); na cena de Clímax, onde ela existe, vale ±1pp, e o dial de ×1,5 do parecer mede o mesmo nada. O critério do autor segue reprovado nos ranks 3 e 5, com o Xie Lang fechando a fila no lugar do Demvi. A alavanca que faz o critério fechar nos três ranks está medida e não é regra nova: paridade de Níveis (o Jiāotáng tem a mesma escada na ficha e o motor nunca leu) mais o atrito do degrau d8. Retida a republicação da tabela de composição, que anda 12 de 15 células acima de 3pp. Achado colateral: o teste de conjuração do motor omite o nível de domínio e o −4 de golpe registrado, virando loteria de 5% no rank 5 contra os 40% da regra. Nada editado em `01`-`07`.

## [2026-08-31] simulação | Buff do Xie Lang medido inerte; ranking suspenso por buraco de motor (decisão 237)
A isenção de híbrido que eu desenhei rende 0,0pp em duelo — o Golpe Matador nunca dispara num PJ × PJ, e a própria nota de Golpes Matadores diz isso por extenso. Erro meu de diagnóstico: buff de economia de cena para um problema de duelo. O buff fica (vale contra Chefes) mas está marcado como não sendo resposta ao pedido. O ranking que punha o Xie Lang em último foi suspenso: só a Lee recebia os Níveis da escada de Caminho no motor, enquanto o Jiāotáng rodava com zero — com paridade o critério fecha e o Demvi volta a ser o último. Nenhum ajuste de ficha até a remedição. A Lee de foice está confirmada e publicada: de última da mesa (29,7 / 32,1%) para 67,4 / 75,5% em duelo, modelada direto do Catálogo. Registrado também que o nerf da Alma caiu quase todo sobre o Xie Lang, único usuário de Alma da mesa, para conter uma dominância que era artefato.

## [2026-09-01] query | Levantamento dos arsenais reais dos quatro PJs, e quatro buracos de catálogo (nota nova)
Para alimentar a bateria com os Gu que os personagens realmente teriam em vez de fichas abstratas. Trava do autor respeitada: mesma quantidade de Gu para os quatro (6 no rank 1, 8 no 3, 10 no 5 — o teto é a Abertura do Demvi). Nova nota `_Processo/🎒 Arsenais Reais dos PJs por Rank`, ligada ao Mapa. Quatro achados foram para "Em aberto", três atingindo PJs: Alma não tem ataque de alvo único no rank 5 (o Xie Lang ataca com Gu de rank 4 e em área, pegando aliados, e a tabela de cobertura do Catálogo declara ✅ erradamente); Wu Xing melee sem Madeira e Água no rank 5 e sem Terra nos ranks 2 e 4; o Gu de Corpo do Vento é inalcançável para o Demvi por construção (exige CON +2 e o único reforço que daria o +1 é declarado incompatível); e o rank 1 não tem Gu de Corpo para ninguém exceto Força, o que explica parte da dianteira do Jiāotáng no rank em que a campanha começa. Registrado ainda um bloqueio: a linha do Caminho da Alma publica o Verme da Lembrança como 2d6 "passo 0" enquanto a ficha o publica como 2d12+2, o que invalida os rótulos de passo de toda a linha. Sete Gu propostos nos Caminhos liberados, aguardando revisão.
