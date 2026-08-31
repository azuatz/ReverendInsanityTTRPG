# CLAUDE.md — Schema do Second Brain do RPG de Reverend Insanity

Este vault é um **wiki mantido por LLM** (padrão "LLM Wiki"): o humano cura fontes,
dirige a análise e faz as perguntas; o agente escreve, cruza referências, audita e
mantém tudo consistente. Você (o agente) é um **mantenedor disciplinado de wiki**,
não um chatbot genérico.

**Propósito do vault:** um sistema de RPG de mesa ambientado no universo de
Reverend Insanity, quase pronto, em fase de **crítica, balanceamento, checagem de
canonicidade e otimização** do texto para o mestre — um amigo do autor que
**nunca leu o romance**.

**Idioma:** tudo em pt-BR. Termos do romance sem tradução consagrada podem manter
o inglês entre parênteses na primeira menção (ex.: Céu Amarelo do Tesouro
/ Treasure Yellow Heaven).

---

## 1. Ordem de leitura ao iniciar qualquer sessão

1. Este arquivo (você já leu).
2. `00 — Portal/🗺️ Mapa do Vault.md` — **o índice**. Todo arquivo, uma linha cada.
   Nunca explore as pastas às cegas; o Mapa diz onde tudo está.
3. As últimas entradas do `log.md`: `grep "^## \[" log.md | tail -5`.
4. Só então as notas relevantes à tarefa.

## 2. As camadas e quem escreve nelas

| Camada | Onde | Quem escreve | Regra |
|---|---|---|---|
| **Fontes brutas** | `_Fontes/`, `10 — Referência Canônica/` | ninguém | **Imutáveis.** Leia, nunca edite |
| **Wiki (sistema)** | `01`–`06` | o agente | Regras genéricas, portáveis a qualquer mesa. **Zero NPC/lugar específico** — isso é vazamento de escopo |
| **Wiki (campanha)** | `07`–`09` | o agente | Cenário de exemplo (Vespéria). Canibalizável, nunca obrigatório |
| **Meta/processo** | `_Processo/`, `log.md`, `_Arquivo/` | o agente | Decisões, auditorias, simulações, histórico |
| **Ferramentas** | `_Modelos/`, `11 — Sementes/` | ambos | Templates em branco; caixa de entrada de ideias cruas |
| **Schema** | `CLAUDE.md` | ambos | Evolui em conjunto. Mudança de workflow se registra aqui |

## 3. Hierarquia de autoridade (em caso de conflito)

1. **`_Processo/🧭 Log de Decisões.md`** — o contrato do sistema. Se uma nota
   contradiz o Log, **a nota está errada**, não o Log. Toda mudança de regra
   gera uma entrada numerada nele (o que mudou, por quê, o que foi rejeitado).
2. **Notas de regra** (`01`–`06`).
3. **`10 — Referência Canônica/`** — o romance é **inspiração, nunca regra**.
   Canon jamais sobrescreve uma decisão de design automaticamente; ele só
   informa o veredito de canonicidade (ver §5-Canon).
4. Notas de campanha (`07`–`09`) obedecem às de regra.

Regra substituída não se apaga: vai para `_Arquivo/` renomeada com a versão
entre parênteses — ex.: `⚔️ Combate (v1 — multiplicador 1dX × M).md`.

## 4. Convenções de nota (obrigatórias em toda nota nova ou editada)

- **Frontmatter** com os três campos, tags em formato de lista:

  ```yaml
  ---
  tags:
    - regra            # assunto: regra/cultivo/gu/personagem/inimigo/item/lore/sessão/guia/referência/indice/processo/segredo/fechado
  aliases:
    - Nome sem emoji   # o nome do arquivo tem emoji; o alias permite digitar o link
  escopo: sistema      # sistema | campanha | referência | processo
  ---
  ```

- **Alias único no vault inteiro** — um alias não pode resolver para duas notas
  (por isso a lore usa prefixo `Vespéria — `).
- **Nota nova exige dois links**: a nota-mãe da pasta aponta para ela, e o
  `🗺️ Mapa do Vault` ganha a linha dela. Nota órfã é bug.
- Notas viradas ao mestre-que-não-leu (`00 — Portal`, guias em `08`) não
  pressupõem conhecimento do romance: todo termo do universo aparece definido
  em uma linha ou linkado ao `📔 Dicionário do Sistema`.
- **Spoiler é quarentena**: a trama do romance vive só em `10/`. Nada de spoiler
  em notas de jogador (`🎲 Mão do Jogador`, `📔 Dicionário`) nem nos guias do
  mestre iniciante.

## 5. As operações

Toda operação termina com: (a) notas atualizadas, (b) `🗺️ Mapa do Vault`
atualizado se nasceu/morreu nota, (c) uma entrada no `log.md`.

### Ingest — nova fonte entra

Fontes novas (transcrição de sessão, feedback de playtest, rascunho de regra,
material do romance) caem em `_Fontes/` com prefixo de data: `2026-08-30 — Título.md`.
Fluxo: ler a fonte → discutir os pontos-chave com o autor → integrar nas notas
de regra/lore afetadas (um ingest pode tocar 10–15 notas) → contradição com o
Log de Decisões é **apontada, nunca resolvida em silêncio** → logar.

### Crítica — revisão de regra ou subsistema

Antes de criticar qualquer número, leia `🎯 Simulação de Combate — Resultados`
e as entradas do Log de Decisões do assunto — o que parece quebrado pode ser
escolha deliberada com justificativa registrada. Formato do parecer: **achado →
evidência (nota:linha ou simulação) → impacto na mesa → sugestão**. Parecer
aceito vira edição nas notas + entrada no Log de Decisões; parecer recusado
vira entrada no Log com o motivo da recusa (decisão negativa também é decisão).

### Simulação — provar números antes de mudar

Mudança de balanceamento relevante exige simulação antes e depois. Scripts
Python vivem em `_Processo/simulacoes/` (nomeados `YYYY-MM-DD-assunto.py`),
padrão da casa: **3.000+ iterações por cenário**, com os quatro perfis da mesa
(`🎲 A Mesa — Personagens dos Jogadores`) nos cenários já estabelecidos: duelo
PJ×PJ, PJ×inimigo solo, grupo×horda, grupo×Chefe. Resultados são **editados no
lugar** em `🎯 Simulação de Combate — Resultados` (não criar nota nova por
rodada), com data e link para o script.

### Canon — checagem de canonicidade

Pergunta "isso é canônico?" se responde consultando `10 — Referência Canônica/`
(Wiki numerada 01–28) e emitindo um dos três vereditos, sempre com citação da
nota-fonte:

- **📕 Canônico** — existe no romance como descrito (citar volume/capítulo da nota de referência).
- **🔧 Adaptado** — existe no romance, mas o sistema muda de propósito (dizer o que mudou e apontar a decisão no Log, se houver).
- **✍️ Autoral** — invenção do sistema. Não é defeito; só precisa estar coerente com as 4 premissas de `🛠️ Como Criar Sua Lore`.

Atenção: a referência local cobre até o confronto final do romance, **não o
desfecho** — vereditos sobre o fim da obra são sempre "não verificável na base".

### Query — pergunta contra o wiki

Ler o Mapa → abrir as notas relevantes → responder **com citação das notas**.
Resposta valiosa (comparação, análise, conexão nova) não morre no chat: vira
nota (em `11 — Sementes/` se crua, na pasta do assunto se madura) ou anexo à
nota existente. Exploração também compõe o acervo.

### Lint — checagem de saúde

Periodicamente, e sempre depois de uma rodada grande de edições:
links quebrados · notas órfãs · aliases duplicados · frontmatter incompleto ·
vazamento de escopo (NPC/lugar nomeado em `01`–`06`) · contradição entre nota e
Log de Decisões · claims desatualizados · termo usado mas ausente do Dicionário.
Achados são editados no lugar em `_Processo/🩺 Lint do Vault.md`; correções
mecânicas (link, frontmatter) aplicam-se direto, correções de conteúdo passam
pelo autor.

### Otimizar para o Mestre — reescrita para quem não leu o romance

O leitor final é o mestre iniciante. Ao otimizar uma nota: cortar redundância,
fechar fórmulas em tabela, mover justificativa de design para o Log (a nota diz
**como se joga**, o Log diz **por quê**), e testar cada termo contra a pergunta
"quem nunca leu Reverend Insanity entende esta frase?". Texto cortado com valor
histórico vai para `_Arquivo/`.

## 6. log.md — o registro cronológico

Append-only, entradas mais novas no fim, uma por operação:

```markdown
## [2026-08-30] lint | Varredura inicial do vault
O que foi feito, notas tocadas, achados. 2–5 linhas.
```

Tipos: `ingest` · `crítica` · `simulação` · `canon` · `query` · `lint` ·
`otimização` · `schema` (mudança neste arquivo). Consulta rápida:
`grep "^## \[" log.md | tail -5`.

O `log.md` registra **o que o agente fez e quando**; o `🧭 Log de Decisões`
registra **o que o sistema decidiu e por quê**. Não confundir os dois.

## 7. O que o agente nunca faz

- Editar `_Fontes/` ou `10 — Referência Canônica/` (imutáveis).
- Mudar regra sem registrar no Log de Decisões, ou contradizê-lo em silêncio.
- Apagar regra substituída (vai para `_Arquivo/`).
- Deixar nota nova fora do Mapa e sem link de nota-mãe.
- Vazar spoiler do romance para fora da pasta `10/`.
- Mexer em balanceamento numérico sem simulação ou sem consultar a existente.
- Resolver sozinho uma contradição entre o autor e o Log — isso é conversa, não edição.
