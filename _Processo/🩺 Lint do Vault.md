---
tags:
  - processo
aliases:
  - Lint do Vault
  - Lint
escopo: processo
---

# 🩺 Lint do Vault

Nota de saúde do vault, **editada no lugar** a cada rodada de lint (não criar
nota nova por rodada). O que se verifica está definido no `CLAUDE.md` §5-Lint.
A parte mecânica roda com:

```
python3 "_Processo/ferramentas/lint_vault.py"
```

Ele checa: wikilinks quebrados (resolvendo nome de arquivo **e** aliases,
inclusive com `\|` de tabela) · colisões de alias · notas órfãs · frontmatter
sem `tags`/`aliases`/`escopo`. O que ele **não** pega — contradição com o Log
de Decisões, vazamento de escopo, claim desatualizado — é trabalho de leitura
do agente.

---

## Rodada [2026-08-30] — varredura inicial (instalação do Second Brain)

**Estado geral: excelente.** 144 notas, zero colisão de alias, zero órfã real,
grafo fechado. Achados e o que foi feito:

| Achado | Veredito | Ação |
|---|---|---|
| 9 notas sem campo `escopo` (⛩️ Portal, 🗺️ Mapa, 💡 Sementes, 6 modelos) | mecânico | ✅ corrigido: `sistema` para Portal e modelos (seguindo 🧰 Modelos), `processo` para Mapa e Sementes |
| link-placeholder "nome da nota nova" em 🗄️ Arquivo | falso-positivo | é placeholder intencional de instrução — deixado como está |
| `_Fontes/📥 Fontes.md` e `log.md` órfãs | recém-criadas | ✅ ligadas ao 🗺️ Mapa do Vault nesta mesma rodada |

**Pendências para rodadas futuras (exigem leitura, não script):**

- [x] Varredura de contradição regra × [[🧭 Log de Decisões]] → rodada 2026-08-30
- [x] Vazamento de escopo: procurar NPC/lugar nomeado nas pastas 01–06 → rodada 2026-08-30
- [x] Conferir se todo termo de sistema usado nos guias do Portal existe no [[📔 Dicionário do Sistema]] → rodada 2026-08-30
- [x] Checagem de canonicidade sistemática das mecânicas centrais contra a pasta 10 → rodada 2026-08-30

---

## Rodada [2026-08-30] — as quatro auditorias profundas

Quatro varreduras de leitura feitas em paralelo por agentes. Achados de conteúdo
**aguardam decisão do autor** (schema §5-Lint: correção de conteúdo passa pelo
autor); nada foi editado nas notas de regra ainda.

### A. Vazamento de escopo (pastas 01–06)

**Veredito: Vespéria (09) está perfeitamente contida — zero NPC/lugar/escola do
cenário nas pastas de sistema.** O vazamento real é o inverso-leve: **a mesa
atual (pasta 07) está entranhada nas notas de regra**, epicentro na pasta 02.
7 vazamentos claros + 6 limítrofes; todos com genericização trivial (manter os
números, trocar os nomes).

**Claros (7):**

1. [[☯️ Os Cinco Caminhos Wu Xing]] ~l.177, 201–258 — seção inteira **"a regra do Lee"**: regra completa (divisão de Marcas por cinco, Elemento Âncora, isenção do ×2 híbrido) formalizada como propriedade do PC Lee e do jogador Gush. O maior vazamento do vault. → renomear a seção para regra genérica de cultivador dos cinco elementos; deixar em 07 só "esta exceção foi concedida ao Lee".
2. [[🩸 Caminho do Sangue]] ~l.192–204 — "A ficha do Jiāotáng (aptidão 76%)" → "Exemplo de ficha — cultivador Sangue + Força, aptidão 76%".
3. [[💪 Caminho da Força]] ~l.189–199 — mesma ficha do Jiāotáng duplicada → idem.
4. [[🌪️ Caminho do Vento]] ~l.107, 125–145 — "o golpe de campanha do Demvi", "por que o Demvi não é descartável", e "os de rank 5 do **Pepo**" (nome de **jogador**) → "um cultivador de Vento de Grau C" / "aptidão 56% não é descartável" / "do especialista mais forte do grupo".
5. [[📖 Catálogo de Gu]] ~l.582–584 — "como o Lee joga… build do jogador" → "build de referência de um lutador dos cinco elementos".
6. [[🤝 Vínculos e Acordo de Mesa]] ~l.22–24 — os 3 exemplos de Vínculo citam Demvi/Jiāotáng/Lee → nomes neutros ou papéis.
7. [[⚔️ Ameaças Genéricas por Rank]] l.13 — "Esta campanha tem 4 jogadores." → apagar (as tabelas já parametrizam 3 e 4).

**Limítrofes (6):** [[🌠 Os Dez Físicos Extremos]] l.49/198 (regra da Abertura
Incompleta calibrada no rolo de 86% do PC — reescrever como "+2% por Marco até
100%, ex.: quem rolou 86% precisa de sete"); [[🛤️ Os Caminhos]] l.64 (regra de
sistema apontando a Rede de Informação de 07 como "base mecânica" — inverter a
seta); [[⚖️ Pontos de Criação]] l.69 e [[🤝 Vínculos e Acordo de Mesa]] l.78
(ponteiros hardwired em "A Mesa"); [[🤝 O Débito]] l.71 (link aponta para
🏛️ Estrutura do Clã de **campanha** quando existe [[🏛️ Clãs e Seitas]] de
**sistema** — provável alvo errado); [[🧬 Receitas de Combo-Refino]] (escopo
`sistema`, mas é livro-razão de "validadas nesta campanha", ecoado no
[[📜 Livro de Receitas de Gu]] — reescopar ou trocar por "validadas em jogo").

**Falsos alarmes verificados e descartados:** as "placas" navegacionais de
Vespéria em 01/03/05/06; ponteiros rotulados "(exemplo de campanha)" em 04;
os NPCs das heranças (Madame Ye, Gorde Wan, irmãos Tan etc.) que são fictícios
autorais autorizados por ⚙️ Fundação l.51; termos canônicos do romance.

| Pasta | Claros | Limítrofes |
|---|---|---|
| 01 | 0 | 0 |
| 02 | 4 | 2 |
| 03 | 1 | 1 |
| 04 | 1 | 2 |
| 05 | 0 | 1 |
| 06 | 1 | 0 |

### B. Canonicidade das 12 mecânicas centrais (contra a pasta 10)

**Veredito: o sistema é honesto com o cânone.** 2 mecânicas 📕 canônicas em
substância, 9 🔧 adaptadas, nenhuma inteiramente ✍️ autoral — e apenas
**3 desvios não-sinalizados**, ou seja, casos em que a nota *alega*
canonicidade que a referência não sustenta. Autoral declarado como autoral não
é defeito e não entra na lista.

**Os 3 desvios não-sinalizados, por consequência:**

1. **[[☯️ Marcas de Dao]] ↔ Attainment** *(o mais estrutural)* — o sistema
   define nível de domínio como **contagem de Marcas** e escora isso em "a conta
   fecha com o cânone" (l.110) + "as quatro condições". Mas `01-cultivo:61`
   define Attainment como **compreensão, escala separada do grau e quase
   inteiramente de talento inato** ("é possível ter Grau baixo e Attainment
   alto, ou vice-versa"), e a condição canônica 2 do Venerável são as **3
   Provações Miríade**, não 300 mil Marcas. A regra do "gênio pobre" mostra que
   a fresta foi percebida, mas a troca de compreensão por contagem nunca é
   sinalizada. → decidir: assumir a adaptação por escrito, ou reabrir a regra.
2. **[[🗺️ Supressão Regional]]** — o núcleo é 📕 canônico e preciso (Gu fora da
   região conta 1 rank abaixo, `08-glossario:69`, `01-cultivo:32`; Muralhas
   Regionais, `06-geografia:37-38`). Mas sob a declaração "isso é regra do
   mundo, **canônica**" estão embutidas duas extensões sem base: "Gu de rank 1
   simplesmente não funcionam" fora da região e todo o mecanismo de
   **reancoragem** (1 mês + rank×100 pedras). → marcar as duas como 🔧.
3. **[[🪜 Ranks e Estágios]] l.178** — afirma usar "**Jujuba Vermelha** por ser
   o termo canônico", mas a referência do próprio vault registra **"Tâmara
   Vermelha (Red Date)"** (`01-cultivo:47`). Puramente terminológico (é a mesma
   fruta), mas é alegação de canonicidade contrariada pela base. → correção de
   uma palavra.

**Observação adicional:** [[🪜 Ranks e Estágios]] l.211 define Venerável Demônio
por Caminho cultivado (Sangue/Escravidão/proibido), enquanto `08-glossario:61`
diz que reto/demoníaco descreve **posição social**, "não uma escala simples de
bem contra mal". Contradição implícita leve.

**Achados positivos — claims que pareciam autorais e têm confirmação canônica
direta:** o Gu de Longevidade nascendo espontaneamente onde há vida acumulada e
sendo moeda entre Imortais (`19-compendio:30`, verbatim); o Gu de Limite
Sombrio selando o Físico Extremo e atrasando a catástrofe (`13-compendio:98`);
o mortal refinando Gu Imortal apenas com um Espírito da Terra guardião
(`11-compendio:105`, `12-linha:47`); e a Ascensão via Gu Imortal prévio
(Portão A) reproduzindo a trajetória do próprio Fang Yuan (`12-linha:59`) —
embora o cânone não a exija de todos, o que mantém os **dois portões** como
adaptação autoral.

**Mais fiel do vault:** [[🍖 Sustento e Alimento]] — os intervalos batem linha a
linha com `02-gu:24` (rank 1–2 dias, 4 meses, 5 a cada 1–2 anos, Imortal 5–6
anos).

### C. Cobertura do Dicionário para o mestre que nunca leu o romance

**Prontidão para mestre leigo: 8/10.** A arquitetura de acolhimento é rara de
tão boa — 47 verbetes de uma linha, rotas de leitura com tempo estimado, e
**zero nome do romance nas portas de entrada**. Os 2 pontos que faltam são todos
consertos pontuais, nenhum estrutural.

**As 5 divergências — o achado mais perigoso, porque o leigo não tem repertório
para desconfiar de qual lado está certo, e duas estão no [[🎓 Guia do Mestre
Iniciante]], que é a rota recomendada:**

1. **Cura de Gu: d10 vs d8.** O [[🎓 Guia do Mestre Iniciante]] diz `M d10` em
   dois lugares (Parte 1 e Parte 2); [[❤️ Recursos e Dano]] l.82, a
   [[📄 Folha de Referência]] e o [[📖 Catálogo de Gu]] dizem `M d8` — e a
   decisão 14 do Log fixa o d8. → **o Guia está errado pela hierarquia do
   vault**; correção de duas linhas.
2. **Nomes dos estágios.** Dicionário, Folha e a tabela de [[🪜 Ranks e Estágios]]
   usam *Inicial, Médio, Alto, Pico*; mas a l.13 da própria [[🪜 Ranks e Estágios]]
   diz *Intermediário, Avançado* e o Guia (Parte 10) atribui ao "Avançado" o
   desbloqueio que a tabela dá ao "Alto". Sobra de renomeação.
3. **Essência escala com rank ou com estágio?** [[🌏 O Mundo em 10 Minutos]]
   l.42–44 diz que o **rank** dobra a essência; a Folha e [[🪜 Ranks e Estágios]]
   l.44 dizem que quem dobra é o **estágio** (`% × 4 × 2^(estágio−1)`, "não
   escala com rank"). A porta de entrada ensina errado.
4. **Moldes do Grimório.** A nota-mãe [[👹 Grimório de Ameaças]] lista quatro
   (Recruta, Guerreiro, Elite, Chefe), mas [[⚔️ Ameaças Genéricas por Rank]] tem
   seis — faltam **Horda** e **Mestre de Gu**, justamente os que as composições
   do Guia usam ("Horda de 8", "3 Mestres de Gu").
5. **"Vínculo" com dois sentidos.** Regra: **um** Vínculo por personagem, com
   vantagem 1×/sessão. Mas a [[🎲 Mão do Jogador — Pacote Discord]] (Mensagem 5)
   e a ficha compacta chamam de "Vínculos" **três** linhas obrigatórias e nunca
   citam a vantagem. Só a primeira linha é o Vínculo mecânico.

*(Cosmético: aptidão descrita como "20%–100%" quando a rolagem `1d80+20` dá
21–100.)*

**9 termos órfãos relevantes** — usados em nota de entrada sem definição
acessível nem verbete: **Primeiro Giro** (no [[⛩️ Portal]], pilar 7 — a
*primeira* nota que o mestre abre), **Escada (de Dano)** (na Folha e em mais 10
notas; o Dicionário só conhece "Níveis de Dano"), **Ficha de Azar** (Folha
l.134), **Ferimento da Terra** (Folha l.131; o Dicionário só tem "Ferimento" do
corpo), **Três Ares**, **Despertar** (na nota **de jogador**), **Ação Especial**,
**Pontos de Contribuição / Obrigação**, **Força de Alma**. Menores (têm link ou
glosa no local): Teto de Combo, Retaliação, Assinatura, Contador de Ameaça,
Disponibilidade, Buff de Lore, Céu Amarelo do Tesouro, Contaminação/Devoração,
e "Densidade da Essência" vs o verbete "B (Grau de Densidade)" — mesma coisa,
dois nomes.

**Jargão sem ponte (3, severidade baixa):** "Linha Cobre Verde → Cristal Roxo"
sem glosa dentro do próprio Dicionário; a **colisão da palavra "Grau"** (grau de
aptidão B vs Grau de Densidade B aparecem na mesma caixa do Guia, e a Folha l.45
diz "o Grau desempata" sem dizer qual); e "frio Yin" sem uma palavra de ponte.

**Verbetes mortos: nenhum.** Os 47 verbetes foram conferidos por grep contra as
pastas 01–06 e todos apontam para regra viva.
