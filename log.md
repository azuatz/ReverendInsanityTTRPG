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

## [2026-09-01] simulação | Décima oitava rodada — os três consertos de motor e a revalidação (decisão 238)
Rodada de correção pura (`_Processo/simulacoes/2026-09-01-decima-oitava-consertos-e-revalidacao.py`, 3.000 iterações/célula, semente 20260830; reproduz a décima sétima com desvio máximo de 0,04pp nas doze células de PvP). Três defeitos da mesma classe — o motor implementando uma leitura estreita da regra escrita. **(1)** O teste de conjuração virou o publicado (`d20 + AST + nível de domínio`, CD com os quatro modificadores, o nível de domínio mortal sendo o `B` por equivalência escrita em O Que Muda ao Subir): de 35/15/5% para 55/45/40% nos ranks 1/3/5, batendo a promessa da nota — e movendo **0 de 15 células publicadas**, o que refuta a suspeita de contaminação registrada na decisão 237. **(2)** A escada de Níveis de ficha só existia para a Lee; derivei as quatro das notas publicadas (Wu Xing rank a rank pelo Catálogo · Força pelo `floor(R/2)` que a nota escreve + Mão de Pedra permanente · Fase da Lua · Corrente+Altitude do Vento), três delas dials de cena que não escalam com rank. É este conserto que move a mesa: 8 de 15 células de grupo, até +15,9pp, e +9 a +25pp na cena solo dos três PJs esquecidos. **(3)** O gatilho do Golpe Matador deixou de ser `boss is not None` e virou a conta de custo-benefício que a própria nota descreve, declarada por extenso como premissa publicada — e ela manda não disparar contra alvo nenhum dos ranks 3 e 5, nem contra um Chefe de rank +2, porque a essência do combo compra 16 a 40 ataques comuns. A isenção da decisão 233 segue em +0,00pp, agora por derivação e não por gatilho congelado. Refutada a afirmação da 17ª de que a paridade fecharia o critério: a ultrapassagem da Lee é confirmada como artefato, mas o Demvi não fecha a fila em rank nenhum e o Xie Lang não converge (23,9 → 22,3 → 19,6%). Corrigidas em ⚔️ Ameaças Genéricas por Rank a tabela de composição (8 células), a de ações do Chefe (5) e as faixas de duração; as composições NÃO foram redesenhadas — isso é decisão do autor. Nada editado em 01-05 nem em 07.


## [2026-09-01] crítica | Três achados estruturais da décima oitava rodada entram em Em aberto (decisão 238, da sessão paralela)
Duas refutações e dois problemas de desenho maiores que os de ficha. O bug do teste de conjuração era grave como taxa (5% contra os 40% prometidos no rank 5) e inerte como número: zero de quinze células se moveram, porque o golpe dispara 0,19 vez por cena. E a afirmação da rodada anterior de que a paridade de Níveis fechava o critério da mesa era outra célula — com paridade limpa, o Xie Lang fecha a fila nos três ranks e a curva dele desce (23,9 → 22,3 → 19,6%), contra um critério que pede paridade no rank 5; nenhuma das cinco leituras testadas faz a curva subir. Os dois achados estruturais: não existe alvo publicado contra o qual o Golpe Matador pague nos ranks 3 e 5, o que mata economicamente o subsistema que a própria nota chama de "como se mata alguém de rank acima"; e o Chefe passou a ser derrubado em mais de 99% das cenas de Clímax depois que três dos quatro PJs receberam a escada de Níveis das fichas deles. Os dois provavelmente têm a mesma solução: a cena de Clímax foi desenhada em torno de um combo que a economia do jogo desaconselha montar.

## [2026-09-01] crítica | Diagnóstico do Golpe Matador corrigido — o eixo estava errado
Minha hipótese de que o custo quadrático contra ganho linear invertia o sinal do subsistema foi refutada pela sessão paralela. A aritmética confere, mas a métrica não se aplica: por essência o combo é 3× a 17× pior, mas por AÇÃO é 1,15× a 1,62× melhor, e melhora com o tamanho. A conta por essência só valeria se essência fosse escassa, e a medição mostra que não é (27 ações de tanque no rank 3, 55 no rank 5, contra cenas de 7-9 rodadas). O recurso escasso é ação. Logo o "não existe alvo contra o qual o combo pague" é artefato do gatilho da simulação, não propriedade do sistema. O culpado real é o teste de conjuração: com os 40% que a regra promete, o combo cai de 1,3-1,6× para 0,8-1,0× por ação — de claramente melhor para empate caro, com Retaliação e Sobrecarga por cima. Isso reabilita o bug de conjuração que a rodada anterior julgou inerte (ele era inerte porque o combo quase nunca disparava) e reordena as saídas: custo linear e ganho escalonado atacam o eixo errado; dar ao combo algo que o ataque normal não faz continua de pé, e agora por um motivo mais forte.

## [2026-09-01] ingest | Espólio de inimigos e feras ganha número (decisão 239)
Pedido do autor. Mestre de Gu inimigo passa a ter duas linhas de ficha: Pedras Primordiais no corpo (20-60 no rank 1 a 8.000-50.000 no rank 5) e materiais de receita. A proporção é deliberada — o bolso é um décimo de um Gu do mesmo rank, então assaltar rende dinheiro de viagem e a fortuna exige achar onde ele guarda. Feras rendem material em vez de bolso (30-80 no rank 1 a 20.000-200.000 no rank 5, repartido entre 2 a 4 partes), valendo um quinto de um Gu do mesmo rank. E a regra que transforma caça em decisão: como você mata decide quanto vale — morte limpa rende cheio, combate normal −25%, fogo e esmagamento −50% ou mais, carcaça largada −50% e sem órgãos. Tudo ancorado na tabela de preço do Mercado e na escala de vida das Pedras. As linhas por molde ficam com a sessão paralela, dona de 06.

## [2026-09-01] crítica | Etapa 1 do conserto do Golpe Matador: confiabilidade (decisão 240)
O autor escolheu "os dois, em etapas" — consertar a confiabilidade agora e decidir o efeito exclusivo depois de medir. A CD passou de `12 + 2 × nº de Gu` para `10 + nº de Gu`, e o Teste de Conjuração passou a somar o rank. Um combo registrado de 5 Gu no rank 5 sai de 5% para 85%; improvisar um de 4 sob pressão fica em 40%. A causa estrutural era a mesma das tribulações: nada na rolagem crescia com o personagem na fase mortal, então um rank 5 rolava igual a um rank 1 contra uma CD que só subia. A seção "Contra quem vale disparar" foi reescrita no eixo certo — a pergunta deixou de ser "tenho essência?" e virou "este alvo merece a minha ação?" —, com a faixa de perigo dos ranks 2 e 3 removida e a medição dos 97% para 76% preservada e reatribuída. Folha de Referência e ficha do Xie Lang sincronizadas. Vai à bateria. O molde do Chefe fica intocado por decisão do autor, porque o número dele foi medido com o combo não disparando.

## [2026-09-01] ingest | Etapa 2 do Golpe Matador: Prerrogativa e Abertura do disparo (decisão 241)
Pedido do autor, fechando o par aberto pela 240. Desenhado a partir da fonte primária: a checagem de canonicidade confirmou seis conceitos do subsistema e achou uma divergência — no romance o golpe matador É usado, inclusive em duelo, e o gatilho canônico nunca é dano ("será difícil contê-la com golpes comuns... vou usar meu golpe matador contra o golpe matador dela"). Duas peças em [[⚡ Golpes Matadores]]: a **Prerrogativa** (Romper/Selar/Prender/Alcançar — o que só o combo faz, tirando-o da disputa de dano por ação que ele perde por construção) e a **Abertura do disparo** (Defesa −4 enquanto executa, canônico literal: "sua defesa cai quando você usa seu golpe matador"). Junto com a 240, o subsistema fica caro, decisivo, confiável e perigoso por ter sido usado — a forma do romance, onde o custo cobra na exposição depois, nunca impede antes. Ainda não medido: a 19ª estava rodando a etapa 1 isolada e vira a linha de base; a próxima mede as duas juntas.

## [2026-09-01] crítica | Conferência independente da etapa 2 do Golpe Matador, e duas ressalvas escritas
Conferi por aritmética o efeito combinado das etapas 1 e 2, com a chance de conjuração dentro da conta, contra um Chefe de RD base 2. Antes do conserto o golpe valia 0,67× / 0,61× / 0,49× de um ataque comum nos ranks 1, 3 e 5; com a etapa 1 sobe para 0,98× / 1,16× / 1,26%; com a etapa 2 chega a 1,33× / 1,47× / 1,50%. O achado que fecha o caso: **a etapa 1 sozinha deixa o rank 1 em 0,98×, ainda sem valer a ação** — a bateria ia concluir isso e ir para a etapa 2 de qualquer jeito. E a etapa 2 não estoura: fica na faixa em que a jogada vale e a escolha continua sendo escolha, longe do 2,0× que a tornaria obrigatória. Duas ressalvas foram escritas: em `👻 Caminho da Alma`, por que a Prerrogativa Romper não come o nicho do Caminho (Alma é propriedade de Caminho, Romper é declaração de um golpe — sempre contra uma vez, e Romper só fura RD, sem trocar a Defesa mirada nem a barra); e em `⚡ Golpes Matadores`, que Romper escala com a RD do alvo e vale zero contra Horda, além de não responder a quem foge, quem se esconde e quem precisa ser capturado vivo.

## [2026-09-01] simulação | Décima nona rodada — o Golpe Matador medido por ação, e o gargalo é a Retaliação (decisão 242)
Medição da etapa 1 da decisão 240 (`_Processo/simulacoes/2026-09-01-decima-nona-golpe-matador-por-acao.py`, 3.000 iterações/célula, semente 20260830; reproduz a 18ª em 0,04pp no PvP e 0,03pp no grupo). **Retratação:** o "não existe alvo contra o qual o combo pague" da décima oitava está retirado — o gatilho daquela rodada usava horizonte solo (`r = ⌈barra / e_norm⌉`), com o qual o ataque comum sempre alcança a barra inteira e disparar só pode perder. Era tautologia, não achado. **O teste da decisão 240 entrega o prometido** — 80/80/80/80/85% contra 55/50/45/40/40% —, e a implementação força uma premissa publicada: `nível de domínio` = 0 na fase mortal, a única leitura que reproduz os 85% e os 40% que a nota publica. **A minha aritmética por ação confere na direção e erra na faixa:** por essência 0,23× a 0,04×, por ação 0,68× a 1,63× — não os 1,15-1,62× que publiquei, porque generalizei os números do Xie Lang; para Jiāotáng e Lee no rank 1 o combo é pior que um ataque comum mesmo com p=1. O Monte Carlo com crítico, RD e falha de conjuração confirma o papel em 11 de 12 células. **O combo passa a disparar, e só com os dois consertos juntos:** de 0,00 (qualquer um isolado) para 3,21 golpes por cena no Clímax de rank 5, contra os 0,19 do gatilho antigo forçado. **Mas o Clímax não recupera o clímax:** 99,7% → 95,4%, contra a faixa de 56-87% — os dois problemas são independentes, e o Chefe fácil é da paridade de Níveis. **O gargalo virou a Retaliação:** perda esperada > ganho em 12 de 12 células, p de equilíbrio de 88% a 146% contra os 75-85% da regra nova — evidência a favor da etapa 2 (decisão 241), que esta rodada não mede. Nenhuma célula de `⚔️ Ameaças Genéricas por Rank` anda mais de 3pp; só a prosa que repetia a conclusão retirada foi corrigida. Nada editado em 02/03/04/07.

## [2026-09-01] otimização | Quatro correções em Golpes Matadores depois da décima nona rodada
A regra de bolso da decisão 240 se contradizia: mandava disparar contra quem não cairia com um ataque normal, o que ao pé da letra apontava para Guerreiro, Elite e Horda — os alvos que a tabela logo acima desaconselha. Reescrita em torno da Prerrogativa: dispare quando ela resolve um problema que você tem, não quando o alvo tem muita vida. Explicitado que na fase mortal o nível de domínio do Teste de Conjuração é ZERO, porque domínio é contagem de Marcas de Dao e não se confunde com o Grau de Densidade do estágio — foi a premissa que a simulação teve de fixar para reproduzir os 85% e 40% publicados. Resolvida a ambiguidade do `+ FOR`: um combo com núcleo de corpo a corpo mantém o bônus, porque o combo empurra o núcleo na Escada e não troca a fórmula — a ausência dele foi o que fez o combo parecer pior que um ataque comum no rank 1 para os melees. E escrita a Retaliação como o custo real do subsistema: medida, a perda esperada supera o ganho de dano em todas as células, e a conjuração precisaria de 88% a 98% nos ranks 3-5 (contra os 80-85% entregues) e de mais de 100% no rank 1. A conclusão registrada é que o Golpe Matador não se justifica por dano e nunca vai — o que o paga é a Prerrogativa.

## [2026-09-01] ingest | Golpe Matador exige rank 3 (decisão 243)
Diretiva direta do autor. A regra nunca esteve escrita: a nota tratava o assunto como economia ("no rank 1 ninguém consegue pagar"), não como acesso, e o Teto de Combo é por estágio, que existe desde o rank 1. Agora é portão: rank 1 e 2 não montam. 🔧 Adaptado — o volume que cobre toda a fase de rank 1-2 do romance não menciona um único golpe matador, mas a obra cita "golpe matador de rank dois" bem depois, então é simplificação de mesa e não proibição da fonte. Consequência limpa: três achados da 19ª eram sobre rank 1 e deixaram de existir (o principal: p de equilíbrio de 115%/146% para melee no rank 1, impossível). Sobrevive intacto o achado central — nos ranks 3-5 a Retaliação ainda supera o ganho de dano, e quem conserta isso é a Prerrogativa, não o portão.

## [2026-09-01] otimização | Portão de rank 3 do Golpe Matador propagado para quatro notas (decisão 243)
A regra nova invalidava um exemplo trabalhado inteiro: a ficha do Xie Lang montava o Corte do Minguante no Pico do rank 2. Refeito para o Pico do rank 3, onde ele pode montá-lo de verdade — `4d12 + 28` (média 54) em vez de `2d12 + 14`, mesmo custo de 640 e conjuração em 80% com o golpe registrado —, com um aviso explicando que a montagem antiga deixou de ser legal. Aproveitada a passagem para escolher a Prerrogativa dele: Selar combina com a ficção do frio que prende antes do corte, e Romper seria desperdício porque a metade de Alma do arsenal já ignora RD de graça. Portão também propagado para o Dicionário (entrada do Teto de Combo), a Folha de Referência e o checklist de O Que Muda ao Subir, que sugeriam combo desde o rank 1 por serem por estágio.

## [2026-09-01] ingest | O pool do Golpe Matador dobra no sucesso (decisão 244)
Diretiva do autor, revertendo a recomendação que eu tinha feito. Diante da medição de que a Retaliação superava o ganho de dano em todas as células, eu havia recomendado abrandar a falha; ele recusou pela razão certa — Golpe Matador é alto risco e alta recompensa, e abrandar a punição apagaria metade da identidade da jogada. O problema nunca foi a punição ser dura, foi a recompensa ser modesta: alto risco com retorno de 30% é EV negativo por aritmética. Agora um combo bem-sucedido rola `2 × M` dados, a mesma mecânica do crítico. Nada foi abrandado — Retaliação, Abertura do disparo e portão de rank 3 continuam de pé. O dano esperado por ação sobe de 1,23-1,32× para 2,22-2,46×. Ressalva registrada: eu mesmo escrevi que acima de 2,0× a jogada vira obrigatória em vez de escolha, e os números novos passam disso — vai à bateria, e se estourar o dial é a forma do bônus, não o princípio.

## [2026-09-01] lint | O rótulo do Golpe Matador Coletivo perdeu o lastro; gatilho do item do Chefe corrigido
A decisão 161(a) classificava o Coletivo como "jogada de desespero tardio" com base na CD 22 do teste de conjuração de quatro participantes. Essa CD foi revogada pela decisão 240 (`10 + nº de Gu`), e sob a regra nova um coletivo de 5 Gu tem CD 15 — muito mais fácil. Além disso, nenhuma bateria jamais mediu o Coletivo: todas rodaram o combo em modo solo. O rótulo ficou marcado como não verificado na nota, sem ser apagado, com o registro de que a Retaliação caindo sobre todos os participantes pode continuar justificando o "desespero" sozinho. Separado o que não depende de medição: a Brecha compartilhada derruba o golpe inteiro se um participante for neutralizado, e é isso que torna o Coletivo frágil por construção. E o item armado do Chefe teve o gatilho corrigido — ele espera a bateria que mede o Clímax com o pool dobrado, não a que mediu só a confiabilidade, porque dimensionar o reforço contra o número antigo seria calibrar contra um combo que não existe mais.

## [2026-09-01] crítica | A heurística do jogador vira premissa; a classificação do Coletivo perde o lastro (decisão 245)
Duas decisões do autor sobre o que a 19ª deixou aberto. (a) O "jogador" das simulações passa a ser oficialmente o da **cauda precificada** — a heurística que desconta a perda de arsenal, porque modela quem enxerga o custo real da falha; a alternativa ("por ação" pura) ignora esse custo e produz números otimistas. Mesmo estatuto do desenho da tribulação e do `domínio = 0`: premissa publicada que nenhuma rodada futura precisa adivinhar. (b) O rótulo "jogada de desespero tardio" do Golpe Matador Coletivo (decisão 161a) está **marcado como não verificado**: apoiava-se na CD 22, revogada pela decisão 240, e o coletivo nunca foi medido em rodada nenhuma. Não revogado — pode continuar certo pela Retaliação dos quatro —, mas mandado para medição na 20ª. Registrado também que Sobrecarga dos apoios, Queima deliberada e o coletivo seguem fora do motor, então todo número de Retaliação já publicado é otimista.

## [2026-09-01] lint | Registrado que os números de Retaliação publicados são o piso do custo, não o teto
Sobrecarga dos apoios e Queima deliberada ficaram fora do motor em todas as vinte rodadas. As duas só encarecem o lado de quem dispara o combo, então nenhum achado muda de sinal — mas o custo real de falhar um Golpe Matador é maior que o medido. A ressalva entrou no callout da Retaliação em `⚡ Golpes Matadores`, para que quem recalibrar isso depois saiba que está lendo o piso do custo. A outra sessão registrou em paralelo as duas decisões do autor: o "jogador" das simulações passa a ser oficialmente a heurística que precifica a perda de arsenal, e a decisão 161(a) fica marcada como não verificada em vez de revogada, com o coletivo emendado na próxima bateria.

## [2026-09-01] crítica | Coletivo medido: o rótulo sobrevive com justificativa nova; números do Clímax corrigidos
O Golpe Matador Coletivo foi medido pela primeira vez. A justificativa antiga do rótulo "desespero tardio" morreu: a CD caiu de 22 para 9 pela decisão 240 e o sucesso subiu de ~15% para 80-95%. A nova é melhor — ele acerta e entrega metade. Custa quatro ações e produz de 0,52× a 0,58× do que esses quatro fariam atacando normalmente; descontada a Retaliação de todos, o líquido vai de −0,11× no rank 3 a +0,32× no rank 5, e ele perde para o combo solo do mesmo núcleo. Continua sendo jogada de última rodada não por falhar, mas por custar caro demais para o que devolve — exceto quando aquelas quatro ações não fariam diferença. Callout reescrito. E os números do Clímax que eu tinha em mãos estavam inválidos: vinham de uma heurística com defeito de horizonte que subprecificava a cauda de Retaliação pela metade. Os corretos são 99,3 / 98,5 / 96,8% nos ranks 3/4/5 — o Clímax continua trivial e no rank 5 ficou 1,4pp mais difícil, não mais fácil. O item armado do Chefe foi atualizado com eles, porque dimensionar contra os números errados sub-reforçaria muito.

## [2026-09-01] ingest | Prerrogativa ampliada no Golpe Matador Coletivo (decisão 247)
O autor desconfiou do custo de quatro ações e perguntou se era canônico. Duas respostas: (a) o custo está certo, mas a nota deixava ler errado — são quatro ações na MESMA rodada, não quatro rodadas; explicitado também que o Coletivo escala (dois participantes = duas ações), e que um coletivo de dois é provavelmente a versão que a mesa vai usar. (b) O buraco real: a Prerrogativa da decisão 241 tinha sido escrita só para o golpe solo, então o Coletivo continuava sendo máquina de dano — a única coisa que ele faz mal (medido: 0,52-0,58× do que quatro ataques comuns entregam). O cânone resolve: o golpe coletivo mais famoso do romance ("busca e travamento ilimitados", dos quatro anciãos do clã Tie) NÃO causa dano — é "o método de captura número um", e a vítima famosa é alguém que podia voar para qualquer lugar. Prender e Alcançar são descrição literal daquele golpe. Adicionada a tabela ampliada; o dano permanece por pedido do autor, mas deixa de ser a razão de montar.

## [2026-09-01] simulação | O preço da captura — vigésima primeira rodada (decisão 248)
Bateria montada sobre uma crítica de método da sessão paralela, aceita integralmente: medir "o Coletivo impede a fuga?" seria tautologia, porque a regra diz que Prender impede fuga por construção. O eixo certo é o custo. Cena: Chefe que foge a 30% de Vitalidade; braços deixar-fugir / Coletivo ×2 / ×3 / ×4; saídas de captura E sobrevivência. Achado principal: o ×4 monta em só 10-22% das cenas, e não é por essência (refutado por controle com essência infinita — as taxas não se movem). O gargalo é exigir quatro pessoas de pé numa cena em que alguém já caiu: a taxa de montagem do ×4 é a taxa de "ninguém caiu ainda", casa por casa (22,4/21,7 · 10,5/10,1 · 19,9/19,3). O ×2 compra +26 a +30pp de captura por ~0,5pp de sobrevivência cada; o ×3 é o mais letal para o grupo (+18-21pp de TPK); contra Elites o ×3/×4 têm captura negativa. Nenhum número mudou — o ×4 se pune sozinho por um mecanismo que nerf nenhum conserta. Mudou o texto da nota.

## [2026-09-01] otimização | O rótulo do Coletivo é separado em dois casos que não se parecem (decisão 248)
A vigésima primeira rodada, medida pelo eixo de custo em vez do de eficácia, mostrou que "golpe de desespero" descrevia bem as versões grandes e mal a de dois. Reconciliada a seção: o Coletivo de dois é ferramenta tática de verdade (+26 a +30 pontos percentuais de captura por cerca de meio ponto de sobrevivência cada), enquanto o de três é o mais letal para o próprio grupo de todas as configurações medidas (+18 a +21pp de aniquilação total) e o de quatro quase não acontece — monta em 10-22% das cenas, porque exige quatro pessoas de pé numa cena em que alguém quase sempre já caiu. A refutação por controle é o achado: com essência infinita as taxas de montagem não se movem uma casa decimal, então o gargalo é estrutural e nenhum número o conserta. A abertura da seção foi reescrita para liderar com dois em vez de quatro, que era o que a nota vinha vendendo.

## [2026-09-01] otimização | O Coletivo estava lendo como requisito do golpe comum
O autor perguntou se um Golpe Matador precisa de outra pessoa. Não precisa — o golpe é solo por padrão, e é o que as sete etapas de montagem descrevem ("apoio" ali são Gu, não pessoas). Mas duas rodadas seguidas mexendo só no Coletivo deixaram três frases falando em "quatro pessoas" e nenhuma dizendo que a seção é opcional. Adicionado um callout no topo do Coletivo dizendo que o golpe normal é sozinho e que nada daquela seção é requisito do comum; título e frases residuais de "quatro pessoas" corrigidos para o número medido (dois).

## [2026-09-01] crítica | Recomendação fechada para o reforço do Chefe: Vitalidade 63×M → 94×M
A pedido do autor. As outras três alavancas caem por motivo medido: mais ações bate no contador da decisão 137, que já rejeitou uma peça desenhada em torno disso; Chefe de rank acima do grupo é TPK medido e proibido pela nota; e a defesa que só a Prerrogativa fura — que eu mesmo tinha recomendado antes de ter o número — foi retirada, porque a vigésima mostrou que o grupo que dispara o Golpe Matador perde cerca de 14 pontos de vitória, e forçá-lo para dentro do combo transformaria o clímax numa punição a quem segue a regra. A Vitalidade voltou a ser viável porque a premissa que eu usei para descartá-la caiu: o Clímax mede 4,7-6,7 rodadas, não os 6,8-10,7 que se publicava, e o autor já fixou 6-8 como o ritmo desejado — mais barra empurra a cena de volta para dentro da faixa em vez de estourá-la, e derruba a vitória pelo eixo que a medição aponta como decisivo. Não inventa mecânica e não toca guarda-corpo. Vai à bateria antes de publicar; implementação é de 06.

## [2026-09-01] simulação | O Chefe mais duro — 22ª rodada (decisão 249)
Implementada e medida a alavanca que o autor escolheu para o reforço do molde Chefe (Vitalidade 63×M → 94×M), com duas saídas obrigatórias: vitória em 56-87% E cena em 6-8 rodadas. O 94×M uniforme erra as duas — a vitória cai abaixo do piso nos ranks 1, 2 e 4 (0,9% · 45,0% · 43,4%) e o ritmo estoura o teto em todos os cinco (8,3 a 10,1 rodadas). O número certo é por rank e quase metade do proposto: 72×M (r2, r4), 78×M (r3), 80×M (r5); o rank 3 é o único que não fecha limpo em nenhuma célula. Achado maior: o rank 1 não tem problema de barra, tem de ações — é o único molde com quatro ações por rodada, e com duas (Vitalidade intacta) mede 69,8% em 7,23 rodadas, o centro dos dois alvos. Nada foi alterado na tabela publicada: trocar a alavanca do rank 1 é decisão do autor. A nota de moldes ganhou um aviso para ninguém aplicar o 94×M às cegas.

## [2026-09-01] lint | Resolvido o bloqueio da linha de Alma: os Gu mortais rolam d12 (decisão 250)
Era o item que travava a simulação do Xie Lang com arsenal real. A ficha publicava o Verme da Lembrança como `2d12+2` e a nota do Caminho publicava o mesmo Gu como `2d6` "passo 0". Investigado, o erro era sistemático: os três Gu mortais de Alma vinham numa escada de d6, com rótulos de passo que só fariam sentido se o Caminho fosse d6. Alma é d12 pela Tabela de Letalidade, e o resto do vault já dependia disso — o Gu Imortal da mesma tabela sempre foi 32d12, a ficha sempre publicou 2d12+2, e o nerf da decisão 231 foi calibrado com Alma em d12. Corrigido para 2d12, 4d12 e 8d12+8. Não é buff: é o mesmo movimento da decisão 223, alinhar o texto ao que já estava medido, porque todas as simulações rodaram d12 e só estas três linhas diziam outra coisa. Corrigida junto a leitura da Agulha Espectral, que passa de ~14 por acerto (22% da barra) para ~26 (41%, ~2,5 acertos) — exatamente o que o degrau d12 promete. E registrado que "passo +1" em d12 vira +1 por dado, não um dado maior.

## [2026-09-01] simulação | Chefe recalibrado, aplicado e revalidado — 23ª rodada (decisão 251)
O autor aprovou a recomendação da 22ª. Aplicado: Vitalidade 63/72/78/72/80 × M nos ranks 1-5 (o 94×M uniforme fica rejeitado por medição), e o Chefe de rank 1 volta de quatro para duas ações com a Vitalidade intacta. Clímax passa a medir 70,3/78,3/84,3/77,5/86,8% — as cinco células dentro da faixa de 56-87% pela primeira vez desde a 18ª —, em 7,2-8,8 rodadas contra o alvo de 6-8. O controle passou limpo: Fácil, Padrão, Padrão pesado e Difícil não se moveram uma casa decimal, o que era a checagem, já que nenhuma usa o molde. Consequência de leitura: a escada de ações, não a Vitalidade, é o botão da dificuldade do Chefe (o rank 1 andou +53pp só com isso); a Vitalidade governa o ritmo. Notas tocadas: Ameaças Genéricas (tabela de Vitalidade e ações, callouts, tabela de composição, faixas, durações, Ancião Renegado), Log de Decisões, Resultados.

## [2026-09-01] lint | Renumeração 250→251 completada, e a correção de Alma verificada contra o motor
Colisão de numeração resolvida pela sessão paralela (a decisão do Chefe virou 251). A correção lá cobriu uma das cinco referências em `⚔️ Ameaças Genéricas por Rank`; as outras quatro (tabela de Vitalidade e ações, callout do rank 1, nota da tabela de faixas, linha de durações) foram corrigidas aqui. Nenhum "250" órfão restou na nota.
Verificada de forma independente a correção da linha de Alma para d12 (decisão 250, da sessão paralela), e ela se sustenta: `alma_dado()` é a ÚNICA fonte do dado de Alma no motor — dez pontos de chamada, nenhum dado fixo alternativo — e devolve 12 no modo publicado. O `dado=8` do perfil "80:20" do Xie Lang é o dado da Lua, não o da Alma. **Consequência que importa: nenhum número publicado por este lado se move.** Todas as vinte e três rodadas já rodavam Alma em d12; a escada de d6 vivia só no texto e nunca alcançou uma simulação. Acertos para derrubar a barra de Alma, remedidos: 2,53 (r2) · 2,59 (r3) · 2,63 (r4-5) com VON 0, contra os ~2,8 que o degrau d12 promete pela decisão 78 — coerente, e coerente com o alvo do nerf da decisão 231.

## [2026-09-01] lint | Verificação independente confirma a correção de Alma, e com argumento mais forte (anexo à decisão 250)
A outra sessão conferiu a correção contra o motor em vez de aceitá-la direto. A função que devolve o dado de Alma é a única fonte dele no código — dez pontos de chamada, nenhum valor fixo alternativo — e devolve 12 no modo publicado; o `dado = 8` do perfil 80:20 do Xie Lang é o dado da Lua, e a fração de Alma roteia pela função. Logo nenhum número publicado se move e nenhuma bateria está contaminada: as vinte e três rodadas já rodavam d12, e a escada de d6 nunca existiu fora daquelas três linhas de texto. Isso vai além de "alinhar o texto ao medido" — o texto era a única cópia do erro. Remedidos os acertos para zerar a barra de Alma de um alvo de VON 0: 2,53 no rank 2, 2,59 no 3 e 2,63 nos ranks 4 e 5, contra os ~2,8 que o degrau d12 promete, batendo com o ~2,5 calculado na ficha da Agulha Espectral. A outra sessão também completou a renumeração, corrigindo mais quatro referências à decisão do Chefe que eu não tinha pego.

## [2026-09-01] ingest | Os sete Gu novos entram no Catálogo e fecham os buracos de arsenal (decisão 252)
Inseridos os sete Gu que o levantamento de arsenais propôs, fechando três dos quatro buracos (o quarto já tinha sido fechado sem ação, por ser desenho e não lacuna). O Gu da Voz Sem Dono dá ao Caminho da Alma o ataque de alvo único que faltava no rank 5 — a tabela de cobertura declarava esse ✅ e ele era falso. Corrigido antes de inserir: a proposta vinha calibrada na escada antiga de d6 da Alma e virou `16d12`, em passo 0 e não +1, porque em passo +1 ela seria estritamente melhor que o Gu da Lua Afogada do mesmo rank, que bate mais mas não ignora RD — o desequilíbrio que a decisão 231 acabou de corrigir. Wu Xing ganhou melee de Madeira e Água no rank 5 e de Terra nos ranks 2 e 4, completando os cinco elementos nos cinco ranks. E dois Gu de Corpo de rank 2 abriram portas fechadas: o Peito de Fole é o primeiro reforço estrutural de grau Leve compatível com os Ossos Ocos do Falcão, o que tira o Caminho do Vento de uma parede lógica, e a Pele de Luar é a primeira defesa própria do Caminho da Lua. Três inconsistências pré-existentes corrigidas no caminho: a seção Alma do Índice não listava nenhum dos oito Gu que moram na nota do Caminho, uma contagem de Gu no Catálogo já tinha drifado e foi substituída por texto que não drifa, e a cláusula de passo do mesmo parágrafo ignorava que o melee de rank alto chega a +3 e +4.

## [2026-09-01] lint | O Índice passa a listar os Gu que moram nas notas de Caminho (decisão 253)
Diretiva do autor sobre Gu permanentes gerou a investigação e ela achou um buraco maior. O Índice de Gu por Caminho listava só o que está no Catálogo — mas seis Caminhos guardam Gu próprios nas notas deles, e a convenção estava aplicada em apenas dois (Lua e Alma, esta corrigida ontem). Sangue, Força e Vento tinham ZERO linhas apontando para as próprias notas: 19 Gu invisíveis no índice que existe justamente para achá-los, e os três são Caminhos de personagens da mesa. Completados, com o cabeçalho de cada seção declarando quantos moram em cada lugar, no mesmo padrão que a Lua já usava. Sangue vai de 23 para 29, Força de 36 para 42, Vento de 6 para 13. Registrada também a regra de escolha que o autor enunciou: um Mestre de Gu assenta o permanente do próprio Caminho, porque um permanente de Caminho alheio vive dentro dele atritando com o resto do arsenal — é de lá que quase toda incompatibilidade da tabela de Gu de Corpo nasce. Aplicada ao Xie Lang: ele troca a Pele de Aço (Metal) pela Pele de Luar (Lua), perdendo o +1 CON permanente e ganhando RD que dobra sob lua visível.

## [2026-09-01] crítica | A linha de base de atributo é 3 — a escada de letalidade descrevia ninguém (decisão 252)
O autor deu a regra: o valor padrão de atributo, para acerto e status em geral, é 3 — só os psíquicos (Astúcia, Vontade) ficam baixos, e o que fica baixo é sempre o oposto do arquétipo (lutador tem Vontade baixa, atirador tem Força baixa). Eu vinha reportando calibragens com atributo 0, inclusive na verificação da linha de Alma minutos antes. Remedido: os degraus publicados (d6≈5 · d8≈4 · d10≈3,3 · d12≈2,8) reproduzem casa por casa um alvo de CON −1 sem RD nenhuma — o personagem mais frágil que as regras permitem. Contra o alvo padrão (CON +3, piso de RD) os mesmos degraus custam 11,25 · 8,22 · 6,52 · 5,43 acertos. Nada de balanceamento se move: as 23 rodadas sempre rodaram com as fichas reais, então as durações medidas já descrevem o jogo verdadeiro — o defeito era de rótulo. A correção também desfaz uma falsa equivalência: a Alma não custa "os mesmos 2,8 do d12", ela custa ≈2,9 contra um lutador e ≈4,0 contra um conjurador, contra os 5,5 do d12 físico. É letalidade seletiva, não equivalente. Notas tocadas: ❤️ Recursos e Dano, ⚔️ Combate, Log de Decisões.

## [2026-09-01] lint | Acertos-para-derrubar da Agulha Espectral corrigidos para a régua nova
A outra sessão descobriu que a linha de base de atributo desta mesa é 3, não 0, e que os degraus da decisão 78 descreviam um alvo de CON −1 sem RD nenhuma — o personagem mais frágil que as regras permitem. Isso invalidou o número que eu tinha publicado na ficha da Agulha Espectral (~2,5 acertos, calculado com VON 0). Substituído pelos valores medidos contra alvos reais: ~2,9 acertos contra um lutador, que é o alvo natural da Alma porque Vontade é o atributo fraco desse arquétipo, e ~4,0 contra um conjurador de Vontade alta. A leitura melhorou junto com o número: a Alma não é letalidade equivalente à do d12 físico, é letalidade seletiva — a via mais curta contra quem não a defende, e o alvo que mais interessa derrubar, o conjurador, é justamente o que mais resiste.

## [2026-09-01] canon | O teto de Gu ativos e a família de Gu de multitarefa entram em medição
Diretiva do autor derrubou `Gu ativos = CON + rank`, que dava oito Gu simultâneos a um rank 5 quando a obra descreve três como já difícil. A checagem na fonte primária refinou a correção em três pontos: três sem erro é o teto de quem é excepcional e não a linha de base, o que põe o Mestre de Gu comum em dois; a quarta tarefa degrada com o tempo em vez de ser proibida, o que valida uma rolagem de erro por turno; e o limite é de atenção, não de combate, valendo também para refino. O achado que muda a rota é uma família de Gu dedicada a levantar o teto, aditiva e escalonada por rank, que a obra nomeia como a ferramenta central do Caminho da Escravidão — a rota de exceder o limite passa a ser comprável em vez de fixa na ficha. Isso também pode salvar a Manutenção de Sustentação: se o teto base cair para dois ou três mas o Gu de multitarefa devolver o topo a cinco ou seis para quem investir, a regra quadrática volta a morder no especialista que empilhou, em vez de virar decoração. Bateria de três braços em execução; nada propagado até fechar.

## [2026-09-01] simulação | Erro meu: a calibragem do Chefe rodou com o bug de Níveis (decisão 253)
Descoberto por acaso ao montar a bateria do teto de Gu sustentados. Os scripts da 22ª e da 23ª chamaram configura() sem passar niveis=, e o default dessa função é "17ª — só a Lee" — o estado em que três dos quatro PJs rodam sem os Níveis de Potência das fichas, que é exatamente o bug que a 18ª consertou. Duas rodadas mediram um grupo mais fraco que o real. Escada correta: 63/80/100/94/115 × M (não 63/72/78/72/80), entregando 77/86/87/84/85% em 6,5-8,3 rodadas. A proposta original do autor (94×M) estava certa e a minha rejeição dela era artefato — o defeito dela era ser uniforme, não grande demais. O conserto do rank 1 sobrevive e fica mais forte: com quatro ações o molde resiste a 150×M com 0% de vitória do grupo; só ações o movem. Registrado o hábito que causou o erro: toda bateria nova parte de BASE20. A 21ª (preço da captura) usou o mesmo default e fica provisória.

## [2026-09-01] crítica | Bug de motor invalida a calibragem do Chefe e os preços do Coletivo (decisão 253)
As rodadas que calibraram o Chefe chamaram a função de configuração sem declarar os Níveis, e o default dela reproduz um estado antigo em que três dos quatro PJs rodam sem os Níveis de Potência das fichas. Duas rodadas mediram um grupo mais fraco que o real. A escada correta é `63 / 80 / 100 / 94 / 115 × M`, não a `63/72/78/72/80` publicada. Minha recomendação original de `94 × M` fica reabilitada: ela tinha sido rejeitada como "quase o dobro do necessário", e era artefato — o defeito dela era ser uniforme, não ser grande demais. O conserto do rank 1 sobrevive e ficou mais forte: com quatro ações o molde resiste a `150 × M` com 0% de vitória do grupo, e com duas ações e a barra intacta mede 76,5%. A leitura de que ações governam a dificuldade e Vitalidade governa o ritmo sobrevive porque se apoiava num contraste que o bug afetava dos dois lados. Do meu lado, marquei como provisórios os preços de captura do Golpe Matador Coletivo, que vieram da mesma rodada contaminada — o achado estrutural do combo de quatro sobrevive, porque não depende de dado.

## [2026-09-01] crítica | Marcas de Dao e Domínio desacoplados em dois eixos (decisão 254)
A nota derivava o nível de domínio direto da contagem de Marcas, e na obra os dois são eixos que se cruzam, não o mesmo eixo: Marcas são o estoque de lei acumulado, Domínio é a habilidade de manipular esse estoque. O cânone dá os dois descasamentos — quem pilha Marcas de Caminhos que não cultiva fica com muito estoque e compreensão nenhuma, e um candidato a Venerável tinha as Marcas e não ascendeu por faltar attainment. Marca se acumula degrau a degrau; Domínio sobe em salto, quando o cultivador entende algo. Separados em duas tabelas: Marcas dão Níveis de Potência, Domínio dá as capacidades. O gênio pobre deixa de ser exceção e vira o mecanismo normal de progressão do Domínio. E as condições 2 e 3 do salto para Venerável, que pareciam redundantes, passam a ser coisas diferentes — com a mais comum das formas de fracassar sendo ter o estoque e não ter a compreensão. Nenhum número de combate muda. O ganho é temático: enquanto os eixos eram um só, o sistema afirmava que basta acumular, o oposto do que o romance sustenta.

## [2026-09-01] canon | Auditoria externa de canonicidade — quatro achados, só um vira regra (decisão 256)
Uma sessão especializada que terminou a leitura integral dos 2.334 capítulos auditou o vault. Conferi os achados contra o texto-fonte antes de recomendar. Resultado: (a) grau D 20-30% — RECUSADO pelo autor, a faixa 20-39 fica e a divergência fica documentada; (b) "aptidão deveria ser dificuldade, não impossibilidade" — JÁ IMPLEMENTADO, a Quebra de Paredes é 1d20 + bônus de Aptidão vs CD desde sempre; o único buraco é a cláusula de vantagem por essência emprestada, que não cobra o custo que o romance descreve (dano à Abertura, talento latente rebaixado); (c) curva de amplificação por Marcas — JÁ IMPLEMENTADO e a divergência já é a decisão 164, que recusou a fórmula linear por simulação; o piso do rank 8 que o revisor quer mudar vem de reconstrução dele, não de citação; (d) Gu Imortal roubado não pode ser refinado à força — CANÔNICO E AUSENTE, único achado que vira regra nova, mas na versão fraca que o texto sustenta (barreira, não proibição: exige suprimir a vontade original e refinar, e até lá o Gu não responde ao saqueador).

## [2026-09-01] ingest | Ruptura com três saídas e refino com tempo de calendário (decisão 255)
Diretiva do autor. A Quebra de Paredes passa a ter três degraus de falha: falhar por menos de 10 dá escolha (esperar e reacumular, ou forçar pagando 1 Ferimento e rolar de novo); falhar por 10+ impõe Retrocesso e espera obrigatória; 1 natural regride um rank. Forçar escala (1, 2, 3... Ferimentos por forçada seguida), então esperar é o normal e forçar é desespero — como na obra. Essência emprestada deixa de ser vantagem grátis: falhar com ela custa um grau de Aptidão permanente (canônico, o romance liga choque de essências a talento latente rebaixado). No refino, acrescentada tabela de tempo por tentativa e o número que explica o Caminho inteiro: rank 5 de mãos vazias = ~2.400 tentativas, dezenove anos; com as quatro condições do Ritual = ~2 tentativas, uma semana. Calculado do teste estendido já publicado, sem alterar número nenhum.

## [2026-09-01] ingest | Espólio de Gu Imortal — nota nova (decisão 256)
Nasceu de uma discordância que os dois lados venceram em etapas diferentes. O revisor externo dizia que refinar à força um Gu Imortal roubado o destrói; conferi no texto-fonte e discordei com citação, porque o volume 3 mostra o Gu sobrevivendo inerte nas mãos de quem o tomou. Ele voltou com o capítulo 1299, que sustenta a destruição — mas do refino, não do saque. As passagens descrevem etapas diferentes. Publicada como três estados: Tomado (não responde, e o dono vivo sente onde está), Suprimido (teste estendido, falhar não destrói) e Refinado (uma falha destrói o Gu, e exige Domínio no Caminho da Sabedoria como requisito — a exclusividade é literal no texto e foi conferida aqui). Números: refinar de mãos vazias dá 6/4/3% nos ranks 6/7/8; com as quatro condições do Ritual, 75/68/59%. Procedência marcada nota a nota: o capítulo 1299 entra por citação de terceiro, não reconferido aqui.

## [2026-09-01] simulação | A escada de dificuldade volta a funcionar — 24ª rodada (decisão 258)
Autor mandou fazer o recomendado nos três itens. (a) Composições: acrescentar peças NÃO serve — um Guerreiro a mais leva o Difícil r3 de 78% para 38% e ainda estoura o ritmo (7,6→9,3 rodadas), porque vitória e duração andam em direções opostas quando se conta peças. É a razão de fundo do penhasco da decisão 137. O que fecha é +1 ação em APENAS ALGUNS Mestres, que move a vitória sem mexer no ritmo (7,6→7,7). Aplicado em Difícil r3/r5, P. pesado r5 e Padrão r5. Regra de bolso publicada: para apertar sem alongar, dê ação extra a um inimigo; para alongar sem apertar, suba Vitalidade. (b) Densidade paga (235) medida e adotada como está: pagando B cheio dá 6,9/15,2/6,3/5,6 ativações IDÊNTICAS em todos os estágios — a pressão constante que a decisão buscava. Rejeitadas as duas variantes de amolecimento. Vigiar: o Jiāotáng tem mais que o dobro de fôlego pelo ×0,5 do Sangue. (c) O pool dobrado (244) já estava medido desde a 20ª — a etiqueta era dívida de registro. Retiradas as duas etiquetas.

## [2026-09-01] ingest | Curadoria dos Gu do romance em três camadas (decisão 259)
Critério adotado: quantos dos quatro campos a OBRA sustenta, descontando dedução e invenção de quem catalogou. Camada A (3-4 campos, 117) ganha ficha completa; camada B (2 campos, 200) vira lista promovível sob demanda; camada C (0-1, 51) entra só como nome e descrição, sem número. Rejeitado fichar os 368 — obrigaria a inventar mecânica para dois terços. Criada a nota 📇 Índice de Gu do Romance — Consulta com B e C completas e A listada para conferência. A importação das 117 fichas aguarda a fonte terminar a rodada de correção. Registradas duas travas de procedência: o `*` da fonte vira ✍️ autoral com crédito e nunca 📕; e as vinte fichas "não se alimenta" SEM asterisco são canônicas e não devem ser rebaixadas.

## [2026-09-01] crítica | Teto de Gu sustentados cai para 3, fixo — propagado em 18 notas (decisão 260)
A bateria de três braços da sessão paralela fechou em teto 3: 11 das 15 células de composição na faixa prometida, contra 8 da regra publicada, e o desempate contra o teto 2 (que empatava em 11) foi o colateral — teto 2 derrubava o Clímax para fora por baixo e desfazia a calibragem do Chefe da decisão 253. Propaguei `Gu ativos = CON + rank` → **3 fixo** (Mestre de Gu comum 2, inimigo nomeado 3) em Arquitetura, Atributos, Folha de Referência, Mão do Jogador, Guia do Mestre, os três Modelos, Guia de Criação, O Que Muda ao Subir, Força, Sangue, Alma, Wu Xing, Ranks e Estágios, Formações, Catálogo, Grimório, Mesa, Arsenais e Dicionário. O quarto Gu ficou possível com rolagem de erro (`1d6`, 1-2 desliga um Gu), e a rota limpa de exceder virou o **Gu de multitarefa**, especificado em [[💡 Sementes]] e mantido FORA do Catálogo até ser medido, a pedido de quem mediu. A escada de Força de Alma parou de dar vaga barata: agora dá estabilidade em Força 10 e vaga cara em Cem Homens/Monstro. Os arsenais dos quatro PJs não precisaram ser refeitos — já rodavam com 3 sustentados. Corrigidas de passagem três contradições internas achadas na varredura: a nota dos Golpes Matadores ainda dizia que Domínio é contagem de Marcas (contradiz a decisão 254) e ainda trazia a CD de conjuração antiga (`12 + 2n` em vez de `10 + n`), e a prosa do Chefe no Grimório citava `80 × M` no rank 5 quando a tabela logo abaixo já dizia `115 × M`. Terceira colisão de numeração com a sessão paralela: a 259 dela estava commitada, então a minha virou 260.

## [2026-09-01] ingest | Guia de tribulações — a Calamidade é uma cicatriz, não um evento (decisão 261)
Pedido antigo do autor, entregue. A nota de regras já cobria CD, etapas e preparações, mas nada dizia ao mestre o que a tribulação É na cena. A ideia central veio do cânone: a Terra Abençoada da Imortal Hu tem uma área leste com chamas que não se extinguiram desde a segunda calamidade, um norte alagado pela quarta, e uma figura de relâmpago azul deixada pela quinta — que matou a dona da terra. Cinco calamidades viraram um mapa de feridas com um monstro morando numa delas. Regra de bolso: antes de rolar, o mestre responde "que parte da Terra Abençoada este personagem vai perder?"; se for nenhuma, é combate e não tribulação. Entregues os quatro tamanhos, tabela 1d12 de formas com a coluna "o que pode ficar", cinco passos de construção, a regra de que a tribulação tem Caminho (decide qual defesa vale e o que a cicatriz produz depois), e a sabotagem — com a data da Calamidade alheia como informação comprável que organiza um arco inteiro.

## [2026-09-01] simulação | Bateria conjunta fecha 25 de 25 (decisão 262)
A sessão paralela apontou que o teto de Gu e o redesenho de composições foram calibrados separados. Na verdade a bateria da 258 já rodava com o teto 3 ligado — mas só media ranks 1, 3 e 5. Rodada a confirmação com tudo ligado e varrendo os cinco ranks, quatro células apareceram fora, todas no rank 4 mais um resíduo no 5, com o Difícil r4 em 91% contra teto de 75%. A mesma alavanca fechou as quatro (+1 ação em 1 ou 2 Mestres), o que confirma a 258. Resultado: 25 de 25 dentro da faixa, contra 8 de 15 antes dos três consertos. Lição de método registrada: medir só ranks ímpares escondeu que o rank 4 era o pior da tabela.

## [2026-09-01] lint | Correção de propagação: rank 4 escrito na coluna do rank 3 (decisão 263)
Erro meu, achado pela sessão paralela auditando meu commit. A tabela de composição não tinha coluna de rank 4, e eu escrevi as três prescrições de rank 4 na coluna do rank 3, apagando os consertos próprios do rank 3. Não era cosmético: um Difícil de rank 3 montado pela tabela daria duas ações extras onde a medição pediu uma, e a 258 já tinha medido que isso derruba a célula para 28%. Além disso os consertos de rank 4 não chegavam ao mestre, porque não existia coluna onde morassem. Corrigido acrescentando a quinta coluna e redistribuindo com os números da bateria conjunta (todos os ranks medidos sob as mesmas regras), em vez de recolar os da 258. A tabela de faixas tinha o mesmo defeito e foi reconstruída junto. Publicado: 25 de 25 na faixa.

## [2026-09-01] lint | Achado da tabela de composição fechado (decisão 263 da sessão paralela)
Conferi a decisão 262 logo depois de commitada e achei que a tabela de composição não tinha coluna de rank 4: os três consertos de rank 4 tinham sido escritos na coluna do rank 3, que perdeu o conserto próprio dela. Impacto real de mesa — um Difícil de rank 3 pediria duas ações extras onde a medição pediu uma, e a 258 já tinha medido que isso derruba a célula para 28% contra piso de 40%. Não corrigi: os ranks 1 e 2 tinham sido remedidos na bateria conjunta, então recolar os valores da 258 no rank 3 trocaria um número errado por outro. Registrei o diagnóstico fechado em [[🩺 Lint do Vault]] antes de devolver, para o achado sobreviver caso qualquer das duas sessões caísse. A sessão que tem a bateria corrigiu (263): quinta coluna acrescentada, rank 4 no lugar, rank 3 com o número da varredura conjunta, e a tabela de faixas abaixo reconstruída junto. Achado marcado como corrigido no lugar, com a lição de formato anotada — a 262 e a 263 erraram no formato que recebeu o número, não no número.

## [2026-09-01] otimização | Guia de ritmo e tesouro para o mestre (decisão 264)
Pedido do autor. Os números estavam espalhados por três notas e nenhuma respondia "quanto dou por sessão e quão rápido deixo subir". Criado o guia, todo derivado do que já existe — nenhuma regra nova. Ideia estruturante: o mestre tem dois botões e um é de graça (tempo de jogo avança o cultivo sozinho; pedra só compra tempo, cada dia acelerado conta como dois). Daí o diagnóstico mais útil: quando o grupo reclama que não evolui, o problema quase nunca é a bolsa, é o calendário parado. Publicadas a matriz de dias de jogo por sessão (10 sessões por rank como padrão) e o orçamento de pedras por jogador por sessão (~20/155/1.200/9.900/79.000, multiplicando por oito a cada rank), explicitamente como TETO com dose recomendada em 60%. Achado do cálculo: a mesada de clã vira irrelevante no rank 3 (308 meses de mesada para um rank de 17), ou seja, a economia empurra o cultivador para fora do clã sozinha.

## [2026-09-01] simulação | As três perguntas da cadeia de multitarefa (decisão 265)
(1) A quarta vaga move a vitória: 5 a 9pp, e é o que separa Padrão pesado r3 dentro e fora da faixa. (2) A Manutenção quadrática NÃO segura sozinha — 4 Gu bancam 2,8-4,3 rodadas no Inicial e 22-34 no Pico, o mesmo padrão de tanque que dobra e despesa que não acompanha. (3) A vaga de risco entrega 3,71 Gu ligados contra 4,00 da comprada — 71% do ganho — e queima a ação em 1/3 das rodadas; a comprada é estritamente melhor e as duas convivem bem. ACHADO REAL: a decisão 258 adotou a Densidade paga medindo UM Gu sustentado. Somando a Manutenção de 3-4 Gu, o tanque seca em 1,9-3,6 rodadas no Inicial e 4,5-6,6 no Pico, abaixo da cena, para três dos quatro PJs. As duas regras foram calibradas isoladamente e se empilham. Não invalida a 258, mas o "~7 rodadas de pressão constante" dela descreve um cultivador com um Gu ligado, não com três. Recomendado medir as duas juntas em bateria de cena antes de a cadeia subir ao Catálogo.

## [2026-09-01] crítica | Manutenção de Sustentação removida — três contenções viram duas (decisão 266)
Diretiva do autor: parar de adicionar e resolver interação. A 265 tinha exposto que a Densidade paga e a Manutenção quadrática foram calibradas isoladamente e se empilham (tanque seca em 1,9-6,6 rodadas contra cena de 7-9). Em vez de uma terceira regra afinando as duas, removi uma. Razão que decide sozinha: auditados os 25+ scripts, ZERO referenciam a Manutenção — todo o balanceamento publicado foi calibrado sem ela, então removê-la não move número medido. Mesmo movimento das decisões 223 e 250. Além disso ela punia demais no Inicial (2,8-4,3 rodadas) e era decoração no Pico (22-34), o defeito exato que a 258 já consertou pelo lado da ativação. Restam duas contenções: teto de 3 Gu (ficção) e Densidade paga (economia). A Manutenção de Formação não foi tocada — é cadência diária fora de combate. Propagação das oito notas entregue à sessão paralela, que detém a frente de texto.

## [2026-09-01] crítica | A Densidade paga não sobrevive a uma cena — 258 suspensa (decisão 267)
Auditoria do tipo que a diretiva do autor pediu: varridas as 26 rodadas contra a lista de regras publicadas, SEIS nunca entraram no motor (Manutenção — já removida, Densidade paga, teto de Gu por proxy, Espólio, Supressão Regional, Formações). A Densidade paga era a mais grave por ser regra viva em toda ativação. Implementada e rodada em cena: Clímax r5 cai de 72% para 6%, Clímax r3 de 76% para 11%, P.pesado r5 de 89% para 22%. Seis de doze células saem da faixa. Causa do meu erro: adotei em aritmética de tanque (quantas ativações cabem), mas na cena o personagem também paga ataques e golpes, e o ×2^B chega a ×8 no Pico. Ressalva: a simulação força B cheio toda rodada, que é o pior caso; mas pagando B=0 para sobreviver, o bônus some do dano normal, que é um nerf geral que ninguém pediu. Recomendado reverter a 258. O diagnóstico da 235 volta em aberto, com a informação de que a solução não pode multiplicar o custo por ativação. Lição: aritmética responde "cabe?", só a cena responde "funciona?".

## [2026-09-01] lint | Corrigida a evidência da 266: são 3 scripts, não zero
A sessão paralela apontou que meu "ZERO scripts referenciam a Manutenção" era falso. Medido: 3 de 26 mencionam, e os TRÊS trazem na docstring "Manutenção quadrática dos Gu sustentados OMITIDA" — incluindo o motor-v2 de que todos os posteriores descendem. Nenhum a computa. O argumento fica mais forte, não mais fraco: o motor não apenas ignorava a regra, documentava que a ignorava desde a primeira versão. (O número deles, 11 de 27, também estava errado.) Corrigido na decisão 266 e na nota de Arquitetura.

## [2026-09-01] simulação | A ideia do autor sobrevive, a dose não — Densidade paga em ×1/1,5/2/3 (decisão 268)
A sessão paralela pediu cautela antes de eu recomendar reverter a 258, com dois argumentos certos: a Densidade paga é escolha do autor e não nossa, e eu tinha rejeitado a curva suave usando aritmética de tanque — o método que a própria 267 desqualificou. Medidas quatro doses EM CENA contra as 6 células que a ×2^B quebrava: sem regra 6/6, ×2^B 0/6, ×1/1,5/2/3 6/6, só o primeiro disparo 6/6, +50% por ponto 6/6. Só a dose publicada falha. Descartada a dose "só o primeiro disparo" por ser inerte — mede idêntica a não ter regra. Adotada a ×1/1,5/2/3, a mais cara que a cena tolera: cobra 9pp no Clímax r3. Ressalva registrada: essa dose NÃO entrega a pressão constante entre estágios que a 235 buscava (tanque ×8, custo ×3, então o Pico ainda tem 2,7× o fôlego do Inicial), e a medição mostra que fechar isso pelo custo de ativação é impossível — a única dose que iguala é a que apaga a cena.

## [2026-09-01] crítica | Ambiguidades de arsenal e varredura de coerência do texto (decisões 269 e 270)
Autor mandou fazer tudo que faltava, dividido por agentes especializados e em conjunto com a sessão paralela. Triagem primeiro: 12 dos 20 itens de "Em aberto" já estavam mortos sem baixa, fechados com motivo. Decisão do autor sobre Gu de Corpo (não ocupam vaga de Abertura nem de sustentação) escrita na Arquitetura; as outras duas ambiguidades de montagem resolvidas pela decisão 223 aplicada onde faltava, ambas confirmadas na fonte primária (cap. 204-205). Efeito colateral que muda prioridade: com Gu de Corpo fora da conta, o arsenal do lutador ficou maior do que qualquer bateria supôs, e a bateria de arsenais reais virou revalidação de premissa. Varredura de texto achou três regras revogadas ainda publicadas (RD da 223 em cinco notas, Manutenção da 266 em onze) e uma regra viva que o jogador não tinha onde ler (Defesa contra Alma, publicada só em Combate, propagada para onze notas). Perdi uma discussão com a sessão paralela e revertei: converter os 45/rodada de Formações em ocupação de vaga era regra nova onde cabia remoção, e o custo era duplicata da manutenção diária que a própria nota já cobra. Três agentes rodaram em escopos disjuntos; o terceiro, na reescrita para o mestre em 01 — Fundação, ainda não fechou.

## [2026-09-01] simulação | A linhagem do crocodilo inverte valor ao subir (decisão 271)
Sinalizado pela sessão paralela. Com r2 e r3 da mesma linhagem não convivendo, o r2 dá +2 Níveis e o r3 dá +1 — subir é rebaixamento para lutador armado, e a compensação do r3 ("desarmado vira arma média") não vale nada para quem usa foice. Medido: custa 1,2 a 4,6pp de vitória do grupo (3,6pp no Clímax r3, 4,6pp no r5). É a pior espécie de armadilha, porque o jogador segue a progressão natural e fica mais fraco sem aviso. Recomendado: Crocodilo Maior passa de +1 para +2 Níveis — mudança de um número numa ficha existente, não regra nova, e torna a subida lateral em vez de negativa. Alternativa +3 se o autor quiser que subir seja atraente, mas precisa ser medida contra o teto de +4. Não aplicado: a ficha é território da outra sessão.

## [2026-09-01] otimização | Passada para o mestre em Fundação, e a inversão do crocodilo aplicada
Terceiro agente fechou: sete notas de `01 — Fundação` passaram pela reescrita para o mestre que nunca leu o romance. Combate perdeu ~370 palavras sem nenhum número de regra alterado (changelog virou tabela, seis blocos de justificativa de balanceamento encurtados com link para o Log, lista do pós-acerto remontada); Recursos e Dano teve três repetições fundidas numa; Dedução e Exposição perderam duas menções ao romance que eram spoiler fora da pasta 10. Três achados corrigidos no lugar: o exemplo resolvido de ataque em Combate somava bônus de treino, que a decisão 215 proíbe; o verbete de Níveis no Dicionário ainda usava o nome antigo e só cobria a face Dano; e "Abertura Latente" era resquício sem regra do sistema de Físicos removido pela 217. Aplicada a inversão medida pela sessão paralela: Crocodilo Maior de +1 para +2 Níveis, para subir a linhagem deixar de ser perda de dano. Acrescentada uma trava de leitura no resumo para o motor: os pools de dano não permitem derivar "Níveis efetivos", porque o bônus fixo mistura Grau de Densidade e Níveis excedentes — quem medir usa os pools prontos ou declara o estágio como premissa.

## [2026-09-01] simulação | Bateria de arsenais reais — a ordem de poder colapsa no rank 3 (decisão 272)
Última medição estrutural pendente. Rodada sobre os pools publicados na seção 5, sem reconstruir B e Níveis (o bônus depois do `d` mistura os dois). Dano esperado por ativação, em % do topo: rank 1 — 100/90/86/86, paridade cumprida; rank 5 — Lee 100, Jiāotáng 90, Xie Lang 77, Demvi 67, critério cumprido; RANK 3 — Jiāotáng 100, Lee 37, Xie Lang 29, Demvi 17. O lutador faz 3,4× o dano do Xie Lang. A causa é o Fantasma de Fera: o ataque principal dele no r3 é 3×4d10 dos fantasmas mais o próprio melee. Ressalva decisiva: a decisão 219 estabeleceu o Fantasma como raro por desenho, então 93 é o pico e não a média — e a seção 5 publica o pico sem registrar a frequência. O que a medição estabelece é uma pergunta de formato, não um veredito: enquanto a frequência não estiver escrita, ninguém consegue dizer se o r3 está quebrado. Quarta vez hoje que o defeito está no formato. Contrapesos: Jiāotáng tem RD 0 nos ranks 3 e 5 e a menor Defesa da mesa, e sustenta o arsenal só 3,7 rodadas no r3.

## [2026-09-01] ingest | Sete Gu de defesa criados — quatro Caminhos não tinham RD (decisão 273)
Correção do autor, de método antes de conteúdo: buraco de arsenal se preenche, não se reporta. Eu tinha racionalizado o RD 0 do Jiāotáng como "contrapeso de desenho" quando era falta de catálogo — e um cultivador de Força e Sangue sem resistência bruta contradiz o que esses Caminhos são no romance. Auditados os quatro Caminhos dos PJs: Força só tinha defesa no r4, Sangue nenhuma, Lua nenhuma acima do r2 (B6), Vento nenhuma (B8). Criados sete Gu, cinco ancorados em cânone: Pele de Bronze (r1) e Osso de Ferro (r3) da série que a obra chama de escolha padrão do combate corpo a corpo, e Fantasmas de Guarda (r5), que resolve o rank 5 sem inventar mecânica porque no romance os fantasmas da Força formam camadas de proteção — o sistema só usava metade disso. Mais Crosta Coagulada e Sangue Espesso (Sangue), Véu de Luar (Lua) e Camada de Ar (Vento). Corrigida também a linha do Fantasma na seção 5: o autor confirmou que ele é raro no rank 3, e a via de torná-lo confiável é o Gu Lendário do Esforço Total.

## [2026-09-01] crítica | Correção da 272: o colapso do rank 3 é real, e inventei o nome de um Gu (decisão 274)
Achado pela sessão paralela na leitura adversarial. Dois erros meus. (1) Escrevi "Gu Lendário do Esforço Total" num callout publicado — esse Gu não existe; o real é o Gu do Empenho Total (All-out Effort Gu, r3, canônico). Transcrevi de memória uma fala do autor em vez de conferir a nota. (2) O grave: o Empenho Total É o item 4 do arsenal de rank 3 do Jiāotáng, vinte linhas acima do callout que escrevi dizendo que sem ele o ataque seria 4d10+5. A nota passou a se contradizer. Isso inverte a 272: o colapso do rank 3 NÃO é artefato de publicação. O Fantasma é raro como regra geral do Caminho, mas isso não vale para quem carrega o Gu que remove a rolagem — para esta ficha o pico é o valor de todo turno, 3,4× o Xie Lang. Resolução é escolha do autor: ou Gu lendário quebrar a curva é o que o torna lendário, ou ele não é equipamento padrão de rank 3.

## [2026-09-01] crítica | Leitura adversarial dos sete Gu — cinco ajustes (decisão 275)
Pedi leitura adversarial à sessão paralela e ela achou mais do que eu esperava. (1) O maior: "base × M" tinha duas leituras vivas no vault (M do personagem vs M do Gu), e com sete Gu de defesa novos isso quadruplicava valores. Resolvido pelo motor, que usa o M do PORTADOR desde a v1 — fixado em Combate, com a distinção de que o dado do Gu de ataque continua vindo do rank do Gu. (2) Fantasmas de Guarda não tinham teto: anulariam 8 golpes por rodada contra uma Horda. Agora é um por fantasma, e o fantasma que absorve se desfaz. (3) Crosta Coagulada não dizia se o sangramento é Sangria — fixado como Vitalidade comum, porque defesa que acumula Dívida em silêncio é armadilha. (4) Sangue Espesso não tinha teto de cura e invertia a identidade do Caminho; teto de 4×M por cena. (5) Véu de Luar repetia a Pele de Luar — convertido para RD de Alma, virando a única abaixo do rank 5. Registrada a assimetria: só o Osso de Ferro é Gu de Corpo, então a Força ganhou RD grátis e os outros três com preço de vaga.

## [2026-09-01] crítica | Apoio à sessão de medição: duas propagações e duas premissas derrubadas (decisão 276)
Autor mandou ajudar a outra sessão. Entregues as duas propagações que ela pediu: a Densidade paga na dose nova em sete notas — e descobri que a regra nunca tinha sido publicada, existindo só uma menção de passagem com a dose reprovada — e seis dos sete Gu de defesa da 273 no Catálogo e no Índice. Na leitura adversarial que ela pediu, duas premissas da decisão 272 caíram: o Jiāotáng carrega o Gu do Empenho Total, que o Catálogo declara ser a versão garantida do Fantasma de Fera, então o colapso do rank 3 é real e não artefato de publicação; e o contrapeso de 3,7 rodadas de fôlego somava a Manutenção removida pela 266. Recalculei as dez contas de fôlego do levantamento: sustentar virou quase de graça, a Lee foi de 3,4 para 9,0 rodadas e o Demvi de 3,3 para 9,7, e a escassez migrou inteira para ativação. Achado estrutural devolvido a ela com a evidência: RD = base × M usa o M do Gu, não o do personagem, e a nota de evolução contradiz isso. Fechada a última dívida da RD revogada pela 223 — zero ocorrências no vault.

## [2026-09-01] lint | O M da RD confirmado, e a Pele de Bronze reatribuída (decisão 277)
Três devoluções da sessão paralela. (1) O desafio à 275 não procede: a linha 374 do Catálogo descreve o caso em que o rank do Gu coincide com o do portador, onde as duas leituras dão o mesmo número — ela não toca o caso ambíguo. O motor toca: make_pc usa o M do PERSONAGEM sem referência ao rank do Gu de defesa, desde a v1. A 275 fica de pé. (2) O errado era a seção 5, que publicava a RD do Xie Lang como constante (4 no r3 e 4 no r5); corrigido para 16 no r5. (3) A Pele de Bronze já existia como Terra/Metal — criei uma duplicata sem conferir. Reatribuída para Força com a citação canônica da série (escolha da maioria dos Mestres de combate corpo a corpo) e a minha entrada apagada. Segunda vez no dia que escrevo no vault sem conferir contra o vault. (4) Registrado que a coluna Alimentação dos seis Gu foi composta por quem transportou, não calibrada contra a escala de Sustento.

## [2026-09-01] simulação | Supressão Regional medida pela primeira vez (decisão 278)
Última das seis regras publicadas que o motor nunca modelou. Medido com o grupo viajando e os inimigos em casa: Fácil segue em 100%, Padrão desaba de 97% para 6%, e Padrão pesado, Difícil e Clímax vão todos a 0% com aniquilação total (4,00 baixas de 4). Não é um degrau de força, é a mesa desarmada. Testei o conserto óbvio — montar a cena um rank abaixo — e ele estoura para o outro lado (100% em tudo), porque a Supressão corta a ofensiva e não toca a defesa: o grupo mantém Vitalidade e Defesa do rank cheio. Nenhum rank de inimigo encaixa. Conclusão: a regra não tem conserto por escala de cena e provavelmente não deve ter — a ficção dela já está certa na nota. O que muda é que a REANCORAGEM deixa de ser opcional e vira pré-requisito de qualquer cena acima de Fácil longe de casa. Nenhum número alterado. Com isso, as seis regras nunca modeladas estão todas resolvidas.

## [2026-09-01] crítica | O bug de escada d6 estava em Lua, Sangue e Vento também (decisão 279)
Achado pela sessão paralela: a decisão 250 corrigiu esse bug só na Alma e ninguém olhou as outras colunas. São nove Gu em três Caminhos — Lua e Sangue são d8 e Vento é d10 pela Tabela de Letalidade, e todos os pools saem de d6. Wu Xing (d6 de verdade) e Alma (já corrigida) servem de controle. Custo medido: Lua 1,18-1,22×, Sangue 1,29×, Vento 1,57-1,80×. A consequência é maior que os nove Gu: contamina a decisão 272, porque os pools da seção 5 saem desses Gu e os três PJs afetados são Xie Lang (Lua), Jiāotáng (Sangue) e Demvi (Vento) — enquanto a Lee, a única limpa, foi quem apareceu no topo. Testado: corrigindo a escada e tratando o Empenho Total como a exceção lendária que é, o rank 3 dá Lee 100 · Xie Lang 97 · Jiāotáng 79 · Demvi 71, que é exatamente o critério do autor. A 272 media dois bugs ao mesmo tempo, e nenhum era desequilíbrio de desenho.

## [2026-09-01] lint | Varredura sistemática de texto nas nove pastas (decisão 280)
Metade de texto da revisão final, com quatro agentes em escopos disjuntos e gravação incremental. ~170 achados em 106 notas, e o diagnóstico é único: o vault errava na baixa, não na decisão — e o resíduo se concentrava justamente nas notas que a mesa lê, não nas de regra profunda. Corrigidos no lugar: o "+ treino" no acerto da Folha de Referência (revogado pela 215, efeito medido de até +30,9pp), a regeneração 24× rápida demais na ficha modelo do guia do mestre, o Grau C onde 60% é Grau B, a ficha modelo que gastava 11 de 13 pontos, duas tabelas de vitória contraditórias para a mesma cena no Grimório, cinco regras revogadas na Conversão Medieval, o conselho de composição das Crônicas com as duas metades revogadas, e quatro contagens de Gu divergentes trocadas por texto que não drifta. Três regras revogadas da pasta 02 foram removidas com o texto arquivado: a fusão de Marcas Lua+Alma que a nota concedia a qualquer um, as duas regras incompatíveis do 1 natural, e o "+50% por Caminho extra" — este o mais grave pelo alcance, porque escondia que Sangue+Força, a build de um PJ, é par incompatível. Retratei minha própria afirmação de "zero ocorrências" da RD revogada: havia uma oitava, e a lição é que declarar zero a partir de busca por string é declarar exaustividade que a busca não tem. Aplicada também a correção da escada de dado que a sessão paralela mediu (decisão 279): Lua, Vento e Sangue tinham os pools computados a partir de d6 em vez da base do Caminho.

## [2026-09-01] lint | Correção do fator do Sangue na 279 e confirmação das linhas de rank 1
A sessão paralela aplicou a escada pela REGRA em vez de pela minha lista, e isso pegou dois erros meus. (1) Eu tinha reportado o fator do Sangue como 1,29× comparando um "2d6" que não existe no Caminho; o Gu real é a Agulha Vermelha, publicada em 2d8 com passo +1 (já contaminada), e o corrigido é 2d10. O fator é 1,22×, não 1,29× — menor, não maior. (2) As linhas de rank 1 que ela deixou intocadas por não baterem com nenhuma leitura já estão certas: o Gu do Luar é catalogado como LUZ (base d8, passo 0 → d8 ✅) e não Lua, e o do Demvi é Vento base d10 com passo −1 → d8 ✅. Nada a mudar ali. A ordem de poder 97/100/79/71 não se move: o ataque de rank 3 do Jiāotáng é Força, não Sangue.

## [2026-09-01] lint | Alimentação recalibrada e contadores do Índice recontados (decisão 280)
Duas frentes de número devolvidas pela varredura de texto da sessão paralela. (a) O Catálogo contradizia a escala de Sustento em massa: o rank 5 tinha 15 fichas comendo mensal ou mais rápido contra uma escala de 1-2 anos, e o rank 4 tinha 11. 28 fichas recalibradas, com a QUANTIDADE escalando junto com o intervalo — mudar só a cadência baratearia a refeição. Um Gu de r5 que comia 30 kg/mês passa a comer 1.560 kg uma vez por ano: mesma economia anual, convertida em expedição em vez de despesa de rotina. (b) Nove dos cinquenta contadores do Índice estavam defasados, o pior sendo o Vento declarando 5 e tendo 14; também Alma 28→36, Força 36→44, Sangue 23→31. Todos os desvios para MENOS, sem exceção. Corrigidos por contagem e o total global fixado em 649 Gu. As duas frentes confirmam o mesmo padrão: o vault erra na baixa, não na decisão.

## [2026-09-01] crítica | "Gu não se compram em loja" era falso; Vespéria fica intocada (decisão 281)
Duas diretivas do autor. (a) A primeira das quatro premissas de "Como Criar Sua Lore" afirmava que Gu não se compram em loja — o que contradiz a própria tabela de preços (Gu de r1 a ~500 Pedras, de r3 entre 1.000 e 10.000). O agravante é o alcance: aquelas premissas são a régua que o CLAUDE.md manda usar para julgar lore autoral, então o schema reprovava cenários por um critério abandonado. Reescrita: Gu se compram, e a escassez é de RANK ALTO e não de mercado — do rank 4 o preço vira expedição, rank 5+ não tem mercado, e Gu Imortal só se troca por outro Gu Imortal. (b) A lore de Vespéria fica intocada por decisão do autor; registrado como decisão negativa, já que Vespéria é cenário de exemplo e divergir do sistema genérico não é defeito ali.

## [2026-09-01] otimização | Acordo de Mesa unificado em seis perguntas (decisão 282)
Duas notas publicavam "as cinco perguntas" com apenas três em comum, somando sete distintas que ninguém fazia todas. Unificadas em seis, escolhidas por natureza: as três compartilhadas, as duas de operação de mesa que só a nota-dona tinha (faltar, regra ambígua), e o rank do personagem novo, que só o guia tinha e era a única a produzir consequência mecânica — além de não estar respondida em lugar nenhum. Padrão fixado: mesmo rank do grupo, estágio Inicial. A sétima ("alguém quer jogar alguém cruel?") foi absorvida por "o que não entra em cena", que faz o mesmo trabalho sem obrigar ninguém a se declarar na frente da mesa. O guia deixou de duplicar e passou a apontar.

## [2026-09-01] crítica | O Empenho Total fica, declarado como exceção lendária (decisão 283)
Recomendação minha aplicada por instrução do autor; fecha a pendência das decisões 272 e 274. A decisão 279 esvaziou o dilema: o 3,4× que assustava media dois bugs empilhados (a escada d6 errada em três dos quatro PJs e o pico do Fantasma como linha de base). Com os dois consertados a ordem de poder mede 100/97/79/71, que é o critério do autor — ou seja, o sistema já está calibrado por baixo do Empenho Total e não por causa dele. Ele fica, e por razão de desenho: um Gu lendário que não distorce nada não é lendário, e o autor o pediu nominalmente. Muda só o rótulo — passa a ser declarado exceção deliberada, e a régua de paridade vale explicitamente para arsenais comuns. Nenhum número alterado.

## [2026-09-01] crítica | Peneira dos ~170 achados: 58 mudam a mesa (decisão 284)
Peneira pedida pelo autor. Critério: sobrevive só o que faria aplicar regra errada, calcular número errado, ou não achar uma informação em cena. Resultado: 58 achados (31 ALTA, 21 MÉDIA, 6 BAIXA). Padrão dominante: ~70% é resíduo de revogação — decisão tomada, nota-dona corrigida, propagação parou antes das notas que mestre e jogadores leem. Três padrões menores: os exemplos resolvidos e fichas modelo são o ponto mais frágil (quase toda conta errada está num gabarito, não na regra); os erros são sistemáticos e não pontuais; e o vault se contradiz mais consigo mesmo do que com o Log — em oito casos a resposta certa está na mesma nota a poucas linhas. Corrigidos deste lado: Grau D no Dicionário, cura M d6→M d8, anexação metade→~30%, teto de Marcas que "não grudam mais", teto de +4 Níveis lido por Gu em vez de pela cadeia (permitia +12), RD pré-calculada em três lugares, domínio no B da Vitalidade, e dois exemplos rolando 32 dados contra o teto de 16.

## [2026-09-01] lint | Kit de Origem, mesada da Conversão, e um achado refutado (decisão 285)
(a) A ficha modelo do Guia é declarada Ramo Secundário mas estava equipada com o kit do Ramo Principal — machado pesado 1d10 e couro RD 2 em vez de arma leve/média usada e couro RD 1. Corrigido, e junto o exemplo de combate da mesma nota, que usava o machado. É o padrão da peneira acontecendo de novo: a regra está certa, o gabarito é que equipa errado, e um mestre iniciante entrega o dobro do dado de arma na primeira sessão. (b) A mesada da Conversão Medieval que a sessão paralela não achou por grep existe, numa linha longa: "10 pedras por semana", valor fixo que não escala, contra a escada 40/120/400 por mês. No rank 3 pagava um nono do devido. Corrigido. (c) Refutado: o vazamento de escopo em 06 não existe — as duas ocorrências são legítimas, uma histórica sem nomes e uma orientação sobre onde guardar NPCs.

## [2026-09-01] lint | Alimentação dos ranks imortais — a 280 tinha parado no rank 5 (decisão 286)
O relatório final citava nove fichas de rank 6 comendo mensalmente contra uma escala de 5-6 anos, e a minha decisão 280 tinha corrigido só os ranks 4 e 5 — o padrão que a peneira nomeou, cometido por mim: corrigi a nota-dona da minha metade e parei antes do fim. Oito fichas recalibradas nos ranks 6, 7 e 9, com a quantidade multiplicada pelo intervalo (100 noites de sonho por mês viram 6.000 de uma vez). Registrado um erro de método que quase entrou: a primeira tentativa substituiu a cadência em qualquer lugar da célula e trocou o custo de ativação em UV em vez da cadência de comida; revertido por git checkout e refeito com a substituição restrita ao trecho depois de "Alimenta-se de". Automação que não delimita o alvo produz erro novo enquanto conserta o velho. As três frentes da divisão final deste lado estão fechadas.

## [2026-09-01] otimização | Revisão Final escrita, enigma do Zhao Ping reconstruído, lore marcada como variante
Autor mandou fazer tudo que faltava. Escrita a nota [[🏁 Revisão Final — Estado do Sistema]], ligada ao Mapa e à nota-mãe do Processo: o estado do sistema numa leitura só, porque o resultado estava espalhado por dezenas de decisões, quatro relatórios e uma conversa longa entre duas sessões. A manchete é que não há pendência de balanceamento — o achado que fechou a ordem de poder foi uma varredura de prosa, não uma simulação. Registradas as cinco lições de método das duas frentes. Enigma do Zhao Ping reescrito: a aritmética estava certa, o que quebrou era o passo final que convertia contagem de Marcas em patamar de domínio; virou pegadinha que ensina a decisão 254, e o ponto do escritório passou a ser que o dono contava Marcas de todo mundo e não entendia o próprio Caminho. Corrigido de passagem um resíduo da 254 na própria nota de Marcas de Dao, onde o eixo que conta Marcas ainda se chamava "nível de domínio". Lore de Vespéria: por decisão do autor, as peças inventadas ficam como variantes de campanha, listadas em tabela única na nota-mãe, com âncora de dado nos três Caminhos de NPC para o mestre saber o que rolar num duelo.

## [2026-09-01] crítica | A escada d6 tinha parado no rank 4, e o rank 5 errava de forma invisível (decisão 287)
Achado por um agente da sessão paralela. A correção da 279 procurou pelo padrão NdX e converteu os ranks 2 a 4, onde o passo sobe o tipo do dado; no rank 5 os Gu já estão em d12 e o passo vira +1 por dado, escondido no bônus fixo — os pools não pareciam errados e estavam. Corrigidos: Lua Afogada de 16d12+16 para 16d12+32, e Lâmina de Parentesco de 16d12+32 para 16d12+48. Efeito real na ordem de poder: o Xie Lang de rank 5 sobe de 77% para 87% do topo, deixando a mesa em 100/90/87/67 — mais apertada e ainda cumprindo o critério. Na mesma passada, as somas de apoio dos Golpes Matadores: Lua e Alma somavam +3 com dois apoios (a "alma armazenada" era contada como apoio, sendo munição), corrigidos para +2; e a Sentença de Linhagem contava o Manto Fervente duas vezes, publicando +11 e 16d12+128 — corrigida para +8 e 16d12+96.

## [2026-09-01] simulação | Validação final: 25 de 25, e um defeito de método meu (decisão 288)
Contraparte de números do playtest de leitura. A tabela fecha 25 de 25 células dentro da faixa, com 4.000 iterações e todos os consertos do dia vivos. Mas a primeira passada deu 24 de 25 e a repetição da mesma célula deu outro valor — não era deriva: minhas sementes usavam hash(comp) sobre o nome da composição, e hash() de string em Python é ALEATORIZADO POR PROCESSO. Três execuções, três valores. Toda célula semeada assim era irreprodutível, com ~2pp de variação. O vault publica "semente 20260830" como garantia de reprodutibilidade e para essas células a garantia era falsa. Corrigido para sum(ord(c)) no script da 23ª (o único commitado com o defeito) e nas baterias desta rodada. Consequência prática pequena (tudo dentro do ruído, nenhuma decisão muda), de método não: um resultado que não se reproduz não é medição, é anedota. Sexta lição do dia, e a única sobre o instrumento em vez do vault.

## [2026-09-01] ingest | B1 fechado com quatro permanentes de rank 1, e os quinze pendentes executados (decisão 290)
Autor derrubou o julgamento de "fronteira deliberada" apontando que os Gu de javali existem no rank 1 — e ele estava certo: eles são sustentados, não permanentes, e o único permanente de rank 1 era o da Força. Criados quatro Gu de Corpo, um por Caminho descoberto, todos com portão CON +0 pela lição do B5. A sessão paralela criticou e derrubou dois: o Nó no Osso ganhou trava de rank porque uma RD universal contra Alma no rank 1 quebrava a promessa do Caminho sem mover número nenhum, e a Palma pôs a leitura de Gu alheio atrás de ação e teste porque informação que resolve um dial de ~20pp é o dial, não utilidade. Executados também os quinze itens que a auditoria tinha deixado para decisão humana: Escada de Dano virou Escada de Potência, Grau A passou a cobrir 100%, refino e anexação foram alinhados ao Domínio pela decisão 254, o mito do veterano de rank 6 saiu, o ritmo de campanha voltou à régua de dois saltos, e as linhas de tabela truncadas foram completadas. Colisão de numeração pela sexta vez, resolvida pela convenção de sempre. Playtest de leitura disparado com a condição de método da sessão paralela: o agente monta ficha e roda combate de verdade, não avalia se o texto parece claro.

## [2026-09-01] ingest | Os treze Golpes Matadores ganharam Prerrogativa (decisão 289)
Último buraco estrutural da revisão. A Prerrogativa é obrigatória desde a decisão 241 e nenhum dos treze golpes publicados a declarava — e isso não é lacuna de forma: a 246 mediu que um combo que compete por dano perde 14pp, porque quem paga o combo é a Prerrogativa. Os treze exemplos prontos eram a jogada que a medição chama de erro de jogador. Atribuídas doze pelo que cada golpe faz: Romper para os que atravessam matéria, Prender para os que imobilizam, Selar para os que calam um recurso, Alcançar para os que furam posição. O décimo terceiro (Recolher o Que Sobrou) recebeu dispensa declarada por ser golpe defensivo — a Prerrogativa é o que um golpe ofensivo compra com o Retrocesso. E dois golpes violavam o portão de rank 3, rotulados "rank 2–3": corrigidos. São dois lugares além dos nove mapeados — o portão vazava em onze.

## [2026-09-01] schema | Duas lições de processo do fecho da revisão (decisão 292)
(a) `git add` com caminho explícito protege contra invasão e não contra omissão. Duas edições ficaram órfãs por horas; a causa foi um agente com escopo em 01, 02 e 08 cujo commit listou só 02 e 08. A ironia é útil: o hábito de listar caminhos foi adotado para não varrer arquivos da outra sessão, e produziu a falha oposta. A trava certa é conferir git status contra o escopo declarado do agente antes de fechar, não confiar na lista digitada. (b) A sétima lição de método: um vazio deliberado precisa estar escrito como deliberado. É a única das sete que previne em vez de detectar. Acrescentado o teste que a torna aplicável sem inchar o vault: anotar o vazio só quando um leitor competente ficaria tentado a preenchê-lo — o critério é a expectativa que o próprio documento cria, não a ausência em si.

## [2026-09-01] ingest | Os quatro números que faltavam para o combate rodar (decisão 293)
Achados por um playtest que EXECUTOU em vez de ler: montou fichas, montou um Difícil de rank 1 e rodou três rodadas. O motor não travou uma vez; travaram três números que não existem na ficha de inimigo. (1) Nenhum molde tinha DES e iniciativa é d20+DES em cinco notas — travou no primeiro passo da primeira rodada. Publicada a escada 0/+1/+1/+2/+3/+4, com escopo declarado (iniciativa, desempate e Perseguição; não entra na Defesa). Verificado: a Horda age antes de um PJ em 30-38% e o Chefe em 43-52%. (2) Nenhum molde tinha Defesa contra Alma, embora todos tenham barra — publicada como 13+rank, que é o que as 26 rodadas já usavam. O playtest mediu uma barra de 15 zerando em 4 ativações. (3) O deslocamento base nunca foi publicado, então Lentidão cortava metade de um número inexistente: no playtest ela não fez nada três vezes de três. Fixado em 10 m, e Lentidão passa a cortar N×2 metros fixos. (4) A Perseguição não tinha desfecho para ~75% dos casos (só +3 e −3 em três rodadas de ±1) — preenchida com cinco faixas, e as do meio ganharam consequência.
