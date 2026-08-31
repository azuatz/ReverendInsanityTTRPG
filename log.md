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
