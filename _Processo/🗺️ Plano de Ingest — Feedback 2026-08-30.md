---
tags:
  - processo
  - indice
aliases:
  - Plano de Ingest — Feedback 2026-08-30
  - Plano de Ingest
escopo: processo
---

# 🗺️ Plano de Ingest — Feedback 2026-08-30

Roteiro de execução da fonte [[Feedback do autor — grande rodada 2026-08-30]].
É uma rodada grande demais para uma sessão: **9 frentes**, de remoções de uma
linha a subsistemas inteiros. Esta nota é o mapa — marque as caixas conforme
avança e registre cada mudança de regra no [[🧭 Log de Decisões]].

> [!success] Frente 0 — RESOLVIDA em 2026-08-30
> A auditoria descobriu que as notas citavam as **decisões 103–112**, ausentes do
> [[🧭 Log de Decisões]]: uma sessão anterior aplicou o feedback do autor nas
> regras e **nunca registrou no contrato**. As dez decisões foram reconstruídas a
> partir das notas que as citam, e as seis decisões antigas que elas revogam
> (16, 18, 21, 65, 77, 80) estão marcadas como revogadas no Log.

> [!warning] Consequência: metade deste plano já estava feita
> Este plano foi escrito a partir da fonte bruta, **antes** de descobrir que as
> notas já implementavam boa parte dela. As frentes 1 e 6 estão em grande parte
> concluídas — as caixas abaixo já refletem isso. O que sobra são as frentes de
> **criação** (2 a 5, 7 a 10), que ninguém começou.

> [!note] Como ler as frentes
> **Remover** e **Responder** são baratas e já dão resultado visível.
> **Reescrever** mexe em números que já foram simulados.
> **Criar** são subsistemas novos — cada um vale uma sessão inteira sozinha.

---

## Frente 1 — Remoções de combate e criação `[remover]`

A mais barata do lote e a que mais enxuga o texto para o mestre novo. Sete itens,
todos decisões já tomadas pelo autor — não precisam de nova discussão, só de
execução + registro no Log.

- [x] **Iniciativa é rolada** *(decisão 105)* — confirmar que [[⚔️ Combate]] diz isso; ajustar se divergir.
- [x] **Crítico**: 20 natural *(decisão 105)* **dobra os dados de dano** — garantir que está escrito em [[⚔️ Combate]] e na [[📄 Folha de Referência]].
- [x] **Tirar a média a partir do rank 5** *(decisão 103; a tabela da Folha foi removida em 2026-08-30 e arquivada em [[Médias do pool (v1)]])* (a regra "role 8 dados e some a média do resto: d6 3,5 · d8 4,5 · d10 5,5 · d12 6,5") — em [[⚔️ Combate]] **e** a tabela correspondente na [[📄 Folha de Referência]]. Motivo do autor: *o legal é rolar os dados para o dano não ser fixo*.
- [x] **Tirar a compra/venda de Aptidão** *(decisão 111)* em [[⚖️ Pontos de Criação]] — as aptidões já foram roladas e definidas.
- [x] **Tirar a tabela de Desbloqueio** *(decisão 106)* (`— / +1 resistência e ordem / +2 · 1 ativação/cena pela metade / +3 · 1ª ativação grátis · ignora ½ RD`) — o autor não entendeu o que é. Verificar antes o que ela sustenta em [[🪜 Ranks e Estágios]]: se outras regras dependem dela, avisar antes de remover.
- [x] **Tirar ataques à distância não-Gu** *(decisão 104)* (arcos) de [[⚔️ Combate]] e do [[🗡️ Arsenal]].
- [x] **Tirar a regeneração de essência em combate** *(decisão 107)* para quem não é Físico Extremo ([[⚔️ Combate]], [[🌠 Os Dez Físicos Extremos]]).

> [!success] Frente 1 concluída — e a última pendência foi fechada
> As sete remoções já estavam nas notas; o que faltava era o registro, feito em
> 2026-08-30 (decisões 103–107, 111). O último resíduo da regra da média —
> a tabela ainda viva na [[📄 Folha de Referência]] (que se contradizia
> sozinha) e a frase em [[📖 Catálogo de Gu]]`:35` mandando resolver 25+ dados
> pela média — foi removido e arquivado em [[Médias do pool (v1)]].
> Era o item que **quebrava na mesa**: um Venerável rolando `256d12` com a folha
> dizendo as duas coisas ao mesmo tempo.

## Frente 2 — Economia e mercado `[reescrever]`

Alinhar [[🏪 O Mercado]] e [[💠 Economia das Pedras Primordiais]] à economia
canônica:

- [ ] Existem **lojas de Gu**, com rank 5 em cidades maiores.
- [ ] **Gu raros só em leilão**; comuns em loja de cidade grande, raros em vila.
- [ ] Faixas de preço: r1 ≈ 500 · r2 500–1.000 · r3 1.000–10.000 · r4 10.000–100.000 · r5 100.000–1.000.000 · r6 **nunca** em mercado comum (só [[🏪 Céu Amarelo do Tesouro]]).
- [ ] Exceção **Gu Relíquia**: 2.000 / 8.000 / 50.000 / 300.000; e os Gu que aceleram cultivo fogem da tabela.
- [ ] Conferir o impacto em [[🧩 Refino e Precificação]] e no [[📖 Catálogo de Gu]], que já trazem preços.

## Frente 3 — Cidades grandes `[criar]` — modelo Cidade Shang

Subsistema novo, provável nota própria em `07` (é cenário) com a mecânica em
`01`–`05` (é regra). Decidir o escopo antes de escrever.

- [ ] **Centros concêntricos** (5º ao 1º) com pedágio: 5→4 = 200 pedras (maioria r1) · 4→3 = 600 (r2) · 3→2 = 1.800 (r3) · seguir a progressão.
- [ ] A cidade **atravessa a montanha** — estrutura urbana.
- [ ] **Sistema de tokens**: Gu que suga o sangue do portador e se dissolve no token; só o dono usa. Ranks por cor (o topo é roxo — **verificar as cores canônicas** na pasta 10). Token melhor = melhor tratamento, descontos, acesso a Gu restritos. **Apaga com os anos**, exige voltar à cidade de origem. Vale menos em outras cidades. Sobe e desce por contribuição.

## Frente 4 — Arenas de batalha `[criar]`

- [ ] Lutador desembolsa proporcional ao público atraído; **o vencedor escolhe um Gu do inimigo**.
- [ ] Divisão por centros: 0 vitórias começa no 5º (baixo); vitórias líquidas (V−D) sobem para o 4º (médio) e o 3º (alto).
- [ ] Casa bem com [[🎲 Atividades Adicionais]] e com [[⚰️ Espólio]] (a premiação é espólio dirigido).

## Frente 5 — Cultivo mortal: tempo e pedras `[criar]`

O maior buraco mecânico apontado: hoje não há régua de **quanto tempo** leva subir.

- [ ] Tabela de tempo por estágio/rank, **ou** % de progresso por dia conforme Aptidão.
- [ ] Rendimento de **pedras de essência primordial**: ganho extra por dia e consumo por dia. O rendimento **muda com o rank** — decidir qual das duas vias (o autor delega): consumo mais rápido, ou extração mais pura.
- [ ] **Cultivo fechado**: período longo só cultivando; cultiva mais rápido, não ganha dinheiro, e **calcula a comida dos Gu** no período (custo alto) — salvo se possuir Gu que armazena Gu sem alimentar (como nas heranças). Cruza com [[🍖 Sustento e Alimento]].

## Frente 6 — Imortalidade e Marcas de Dao `[responder]` + `[reescrever]`

Seis pontos: alguns são **perguntas ao vault** (respondíveis já), outros são
contradições reais a resolver.

- [x] **Contradição de piso** *(explicada em 🪜 Ranks e Estágios: o r7 novo tem ~10.000 Marcas **somadas**; um r6 com 9.000 num Caminho só é mais denso naquele confronto. Rank diz o que se ativa; densidade diz o quanto dói)*: dá para chegar ao rank 7 sem 10.000 Marcas? O vault diz que um r6 com 9.000 vence um r7 com poucas, mas fixa 10.000 como piso do r7. Explicar ou corrigir.
- [x] **Fluxo de tempo na fenda** *(decisão 110: r6 10×–30×, r7 30×–60×, r8 60×–100×+, r9 até 120×+ — sua intuição de 10–30× estava certa e o 3× foi substituído)*: o autor esperava 10–30×; [[🗝️ Terra Abençoada]] dá 3× na melhor qualidade. Conferir contra a pasta 10 e decidir.
- [ ] **Escala de Marcas**: o autor esperava milhões. Conferir o canônico. *(A auditoria de canonicidade já achou um desvio aqui: o vault troca o **Attainment** canônico — compreensão, escala separada — por contagem de Marcas. Ver [[🩺 Lint do Vault]].)*
- [x] **Como se sobe de rank depois de imortal?** *(decisão 108: saturar o teto + sobreviver às provações do patamar + declarar a tentativa, que dispara a Provação de Avanço)* Tendo as marcas: é automático? Ritual? Gu? Hoje não está escrito.
- [x] **De qual Caminho vêm as Marcas** *(decisão 109: o teto é do TOTAL, somando Caminhos — não existe 10.000+10.000)* recebidas (terra abençoada, tribulação)? E multi-caminho: divide as marcas? Dá 10.000 de um + 10.000 de outro, ou o teto é 10.000 no total?
- [ ] **Via de avanço por Caminho**: "quando o Caminho faz aquilo, ganha mais marcas" — ganha como, se ações não dão marcas? É dobro na tribulação? [[🛤️ Os Caminhos]].
- [ ] **Balanceamento do Xie Lang**: Físico Extremo (marcas em dobro + terra melhor) tende a abrir vantagem após a imortalidade. Decidir entre dar aos outros uma via de aceleração ou nerfar. **Exige simulação** (`CLAUDE.md` §5-Simulação).

## Frente 7 — Níveis de Dano `[reescrever]`

- [ ] Criar **onde marcar** os Níveis de Dano do personagem ([[Modelo — Ficha de Personagem]] e [[Modelo — Ficha Compacta]]).
- [x] **Varredura** das fontes *menores* — já convertidas em acerto/RD pela **decisão 112**. Resta revisar as fontes grandes: todo lugar que dá bônus de Nível de Dano deve ser reavaliado caso a caso — vira dano fixo (`+3 × M`), `+1 dado × M`, bônus de acerto, ou bônus de atributo (Força/Vontade)? Toca muitas notas; fazer com lista antes de editar.

## Frente 8 — Heranças rank 4–9 `[criar]`

- [ ] Formalizar em [[📜 Manuais e Heranças]]: r4–r5 **mortais** (Gu e receitas mortais; receita imortal só raramente em r5); r6+ **imortais**, contendo fenda com Espírito da Terra ou vontade.
- [ ] **Gerador rolado de herança**: quantidade de Gu · quantas receitas e de quais Caminhos · tem Terra Abençoada? · teste do Espírito ou natureza da vontade · provação e dificuldade · dono justo ou demoníaco (define puzzles e batalhas). Cruza com o [[📜 Catálogo de Heranças]], que já traz 17 prontas.

## Frente 9 — Missões de clã `[criar]`

- [ ] Ao sair das aulas básicas de r1 (primeiro ano como cultivador, quando se costuma chegar ao r2), o personagem entra num grupo e passa a receber missões com **dificuldade e recompensa**, que aumentam a **contribuição** — encaixa direto na tabela de Pontos de Contribuição de [[🏛️ Clãs e Seitas]].

## Frente 10 — Catálogo de Gu `[criar]` — a mais cara de todas

- [ ] Todo Gu tem **3 aptidões: nutrição, uso e refino** — escrever as três para cada Gu do [[📖 Catálogo de Gu]] (449 Gu + 12 Casas).
- [ ] **Todas as receitas canônicas** de Reverend Insanity no [[📜 Livro de Receitas de Gu]], e criar o básico das demais.

> [!tip] Ordem sugerida
> Frente 1 (remoções) → Frente 6 (as perguntas de imortalidade, que são dúvida
> viva do autor) → Frente 2 (economia) → Frente 5 (tempo de cultivo) → o resto.
> As frentes 8, 9 e 10 são projetos próprios; a 10 é trabalho de várias sessões.
