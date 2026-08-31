---
tags:
  - processo
aliases:
  - Crítica — Correção e Clareza 2026-08-31
escopo: processo
---

# 🔍 Crítica — Correção e Clareza (2026-08-31)

Pedido direto do autor: revisar o trabalho recente (correção/balanceamento) e ler o sistema inteiro (01–06) contra a régua de clareza do [[🔍 Síntese — Feiticeiros e Maldições (Bestiário, Mestre, Técnicas)|F&M]] — "quem nunca leu Reverend Insanity entende isso?" Cinco auditorias em paralelo: uma de correção sobre o conteúdo novo da sessão, quatro de clareza cobrindo 01–06. Formato **achado → evidência → impacto → sugestão**, por CLAUDE.md.

**01 e 06 já foram corrigidos direto** (território do agente que escreveu esta nota) — ver `git log` recente. **02, 03, 04, 05 ficam como achado registrado**, para o autor ou o outro agente aplicar.

---

## A. Correção — conteúdo novo (Gu Lendários, Auditoria de Cobertura, Metrópoles, Achados de Baixo Rank)

1. **Vazamento de escopo em [[👑 Gu Lendários]]** — "o exemplar único é mantido pelo **Templo da Maré Silenciosa**, com um ancião cego..." é o único dos 28 ganchos com topônimo próprio; os outros 27 usam descritor genérico ("um clã em decadência", "um general aposentado"). Contradiz o próprio padrão da nota e a regra de zero-NPC/lugar em `01`–`06`. **Sugestão:** trocar por descritor genérico, nos moldes das outras 27 entradas.
2. **Lacuna na cadeia Sombras** — "Nome Apagado" (rank 5) não declara valor de dado de ataque; rank 4 é `8d12`, rank 6 salta pra `32d12`, pulando o `16d12` que a tabela de dobro-por-rank da própria nota exige pro rank 5. **Sugestão:** declarar `16d12` explicitamente, ou justificar por que o rank 5 não escala em dano.
3. **`Gu Imortal do Peso Que Nunca Cai`** (rank 5, Força) declara RD `4×M` contra "qualquer dano de impacto, inclusive Golpe Matador", sem discutir a exceção "ignora RD" que o próprio sistema de Golpe Matador permite construir. **Sugestão:** restringir a cláusula a golpes sem essa opção, ou registrar a interação como exceção deliberada com justificativa.
4. Sem achados de canonicidade (4 alegações verificadas contra a fonte primária, todas corretas) nem na Auditoria de Cobertura (metodologia sólida, duas afirmações checadas batem). A nota da auditoria estava órfã — **já corrigido**, link adicionado no Mapa.
5. Sem achados nas seções novas de Metrópoles (177-179) nem em Achados de Baixo Rank.

## B. Clareza — o padrão que se repete em toda pasta

**A mesma coisa aparece em quase toda nota auditada: justificativa de design ("por que fizemos assim") misturada no texto de como jogar.** CLAUDE.md já manda: a nota diz *como*, o Log diz *por quê*. Isto não é nitpick disperso — é o achado de maior alavancagem da auditoria inteira, porque é uma correção mecânica (mover texto, não reescrever regra) que se repete em quase toda nota de 02-05.

### 02 — Caminho do Cultivo (pior pasta da auditoria)

**Piores três notas:**
1. **[[⚗️ Materialização e Alquimia Interna]]** — 9+ blocos "Por quê" (linhas 41, 97, 123, 137-143, 202, 270, 309, 330, 352). Provavelmente perde um terço do tamanho de graça só cortando isso.
2. **[[☯️ Marcas de Dao]]** — mesmo padrão, mais uma passagem genuinely confusa (linha 89: "não vem mais de..." implica uma regra anterior nunca declarada) e o "Retrocesso de Marca" definido duas vezes (linhas 89 e 197).
3. **[[🌪️ Caminho do Vento]]** — nota limpa, mas com **violação de regra real**, não só clareza: nomeia PJs específicos ("Demvi", "Pepo") numa nota de sistema (linhas 125-145). CLAUDE.md proíbe isso explicitamente em 01-06.

**Quatro contradições/bugs reais entre ou dentro de notas** (não são clareza, são conflito de regra ou erro de fato — decisão do autor ou correção mecânica direta):
- **Requisito de domínio pra anexar terra**: [[🧿 Espíritos da Terra]] diz Grão-Mestre fixo; [[🗝️ Terra Abençoada]] diz que escala pelo rank da terra-alvo (a correção da decisão 152b). As duas notas discordam entre si — confirmado por leitura direta dos dois arquivos.
- **Custo de Desequilíbrio em Grau 3+** em [[🌾 Ecologia e Economia da Terra Abençoada]]: a regra de rejeição (linha 104) e a seção "Sobrecarga por incompatibilidade" (linha 293) implicam custos-base diferentes pro mesmo caso.
- **Referência quebrada dentro da própria nota** em [[⛈️ A Vontade do Céu]]: a tabela (linha 26) usa "+5 a cada 10.000 Marcas totais"; 50 linhas depois (linha 78) a nota diz que isso substitui "o '+1 a cada 25.000 Marcas' de Marcas de Dao" — mas essa regra **não existe** em [[☯️ Marcas de Dao]] (confirmado, zero ocorrências de "25.000" na nota). É uma citação órfã dentro do próprio arquivo. **Mecânico, seguro de corrigir direto**: apagar a frase ou achar a regra real que ela tentava citar.
- **Contagem errada** em [[🌩️ Calamidades e Provações]] linha 112: "Falhar uma Calamidade cobra **três** coisas ao mesmo tempo", mas a lista logo depois tem **quatro** itens. **Mecânico, seguro de corrigir direto**: trocar "três" por "quatro", ou marcar o 4º item como condicional se for esse o caso.

**Termos sem definição, repetidos em várias notas** (fáceis de fechar de uma vez): **"UV"** (usado sem legenda em Sangue, Lua, Vento, Terra Abençoada, Materialização), **Grau A/B/C/D → %** de Aptidão (usado em Físicos Extremos e Ritmo de Cultivo sem nunca declarar o mapeamento), **"Contaminação"** (Caminho da Alma e Físicos Extremos, ausente do Dicionário), **"Retrocesso"** (Espíritos da Terra, sem link).

**Redundância entre notas**: a seção "Sinergia Sangue + Força" (incluindo a ficha de exemplo do Jiāotáng) está quase duplicada palavra por palavra em [[🩸 Caminho do Sangue]] e [[💪 Caminho da Força]] — manter a versão completa numa só, virar ponteiro na outra.

Também sinalizado: [[⚗️ Materialização e Alquimia Interna]] reporta o mesmo dado como "~70%" numa linha e "68%" noutra — checar qual é o número correto antes de mexer em qualquer coisa da nota.

Lista completa (uma nota por uma) no relatório do agente — pedir se precisar do detalhe linha a linha de todas as 22 notas.

### 03 — Gu (mais perto do F&M das quatro pastas)

- **[[🔷 Formações de Gu]]** é o pior offender — três subsistemas quase independentes empilhados numa nota só, cada um com fórmulas próprias, sem um exemplo único que atravesse do início ao fim.
- **`MD [Caminho]`** (notação de Marca de Dao) aparece ~10× em [[👑 Gu Lendários]] sem nunca ser explicado ali (a abreviação de UV/JV/LB também só recebe uma linha vaga). Um leitor que abra essa nota direto (é pensada como referência standalone) cai sem contexto.
- **[[⚡ Golpes Matadores]]**: o "passo a passo de como montar um" fica no fim da nota, depois de ~160 linhas de caso de borda — inverter a ordem.
- Times de qualidade acima da régua do F&M: [[🏆 Convenção do Caminho de Refino]], [[💀 A Morte dos Gu]], [[🍖 Sustento e Alimento]].

### 04 — Trilhas de Personagem e 05 — Arsenal (perto do F&M, gaps concentrados)

- **[[📋 Guia de Criação de Ficha]] e [[⚖️ Pontos de Criação]] se duplicam** — as duas re-explicam "12 pontos só", "sem Gu no início", "Aptidão é 1d80+20" quase frase por frase. Fundir: uma vira checklist puro, a outra mantém a regra.
- **Nenhuma das duas tem um personagem de exemplo resolvido** (o Nanami do F&M) — maior gap de exemplo do audit.
- **[[🎰 Aposta por Procuração]] tem ambiguidade real de regra, não só clareza**: não fica claro se "matar" (VB×2) empilha com "Golpe Matador decisivo" (VB×1,5) — o caso mais comum do jogo (a maioria das mortes vem de Golpe Matador). Precisa de decisão do autor, não só reescrita.
- **"Retrocesso"** usado em [[📜 Manuais e Heranças]] e [[🎲 Gerador de Heranças]] sem nunca linkar a definição real (está em [[❤️ Recursos e Dano]]), e ausente do Dicionário apesar de aparecer em 8+ notas do vault inteiro.
- Notas já no nível do F&M ou acima: [[🎲 Gerador de Heranças]], [[📜 Catálogo de Heranças]], [[🏯 Torres e Estradas de Prova]], [[🍖 Sustento e Alimento]].

## O que já foi corrigido nesta rodada (01 e 06)

[[⚔️ Combate]] e [[🏛️ Arquitetura do Sistema]]: justificativa movida pro Log, checklist de conversão v1→v2 arquivado, exemplo de combate resolvido acrescentado, **Lentidão definida pela primeira vez** (Dicionário + Combate — estava em uso em 10+ notas sem nunca ter mecânica declarada). [[👁️ Exposição]]: dois vazamentos de referência ao romance removidos. [[⚔️ Ameaças Genéricas por Rank]] (pior nota da auditoria de 01/06): narrativa de rodadas de simulação comprimida de ~90 linhas pra ~15, mantendo só a tabela vigente e links pro histórico completo.
