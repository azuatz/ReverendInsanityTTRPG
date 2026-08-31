---
tags:
  - processo
aliases:
  - Retomada — Leitura integral do romance
escopo: processo
---

# 🔖 Retomada — Leitura integral do romance

**Arco CONCLUÍDO em 2026-08-31.** Esta nota documenta o que foi feito, pra quem chegar depois (humano ou sessão de agente) entender o histórico sem precisar reconstruir — não é mais uma lista de pendências. Se você é uma sessão nova, leia isto, confira as últimas ~20 entradas do `_Processo/🧭 Log de Decisões.md` (decisões 129–145) e as últimas de `log.md`, e está pronto pra continuar.

---

## O que foi pedido

O autor clonou o repositório GitHub do romance completo (`~/Documentos/Reverend-Insanity-fonte/texto/`, 6 volumes, ~435 mil palavras, 2.334 capítulos) e pediu leitura integral pra: (1) melhorar o sistema mantendo fidelidade sem inflar complexidade à toa, (2) completar o Catálogo de Gu, (3) criar sistemas de atividades jogáveis (arena, coisas pra fazer em rank alto) baseados no que Fang Yuan e o elenco fazem no livro. Critério explícito do autor, repetido várias vezes: **completo e fiel, divertido, sem coisa desnecessária, sem spoiler vazando pras notas de sistema.**

## Como foi feito

### 1. Leitura integral (18 digests)

18 agentes, cada um lendo um trecho do romance inteiro em fatias de 2.000 linhas e gravando um digest estruturado em `_Fontes/2026-08-30 — Leitura integral do romance/01 — Vol 1 (parte 1).md` até `18 — Vol 6 (parte 3).md` (frontmatter + seções A–G: Gu nomeados, sistemas/atividades, regras do mundo, números/preços, locais, golpes matadores, achados soltos — todo item com capítulo citado).

**A primeira tentativa falhou por completo** (todos os 18 agentes leram tudo mas morreram no limite de sessão antes de gravar — zero no disco) porque gravavam só no final. **A lição, já registrada na memória durável do agente**: agentes de leitura longa devem **gravar incrementalmente** (criar o arquivo na primeira fatia, editar a cada 2–3 fatias), nunca acumular tudo pra escrever no fim. A segunda tentativa, com essa correção, completou os 18 digests (~13.100 linhas) e sobreviveu inclusive a quedas parciais de agentes individuais, porque o que já estava escrito ficava salvo.

### 2. Síntese em 3 frentes

Cada frente leu os 18 digests + as notas do vault relevantes e produziu um relatório em `_Processo/`:

- **[[🔍 Síntese — Lacunas do Catálogo de Gu]]** — aplicado um filtro de curadoria rigoroso (adicionar só o que preenche célula vazia, é icônico e recorrente, ou já tem referência pendurada no vault; descartar cenário de passagem, reskin e lore sem estatística). Resultado: só 3 Gu novos recomendados, de ~460 possíveis.
- **[[🔍 Síntese — Fidelidade ao Romance]]** — 5 achados de divergência entre as notas de regra e o texto real (Metrópoles, Marcas de Dao por Calamidade, Longevidade de Veneráveis, Terra Abençoada, Aptidão populacional). Todos endereçados ou marcados como vigilância deliberada (ver Log).
- **[[🔍 Síntese — Atividades Jogáveis por Rank]]** — inventário das 5 fases de progressão (mortal cidade pequena → mortal metrópole → véspera da Ascensão → Terra Abençoada → alta política entre Veneráveis), cada atividade com cobertura ✅/🔧/❌ contra o sistema existente, fechando com 8 recomendações prioritárias.

(`🔍 Síntese — Atividades Jogáveis (material bruto)` é o rascunho de trabalho por trás da nota acima — pode ser consultado se precisar dos achados crus por volume, mas a nota "por Rank" é a organizada.)

### 3. Implementação — as 8 recomendações da Frente 3, todas aplicadas

| # | O quê | Decisão | Onde |
|---|---|---|---|
| 1 | Arena da Cidade Shang com números reais do romance | 138 | [[🏙️ Metrópoles — Centros, Tokens e Arena]] |
| 2 | Aposta por Procuração (peões mortais lutando por patronos imortais) | 139 | [[🎰 Aposta por Procuração]] *(nota nova)* |
| 3 | Refino territorial de dao marks — guerra fria entre Veneráveis | 140 | [[☯️ Marcas de Dao]] |
| 4 | 3 Gu novos no Catálogo (Deus de Sangue, Rede Celestial, Voto Envenenado) | 141 | [[📖 Catálogo de Gu]], 457→460 |
| 5 | Salão de Missões — versão imortal (Três Quadros) | 144 | [[🏛️ Clãs e Seitas]] |
| 6 | Masmorra de andares + Estrada de Prova (consolidando 3 templates de dungeon do romance numa nota só) | 145 | [[🏯 Torres e Estradas de Prova]] *(nota nova)* |

(Os achados de Fidelidade — Calamidade/Longevidade — foram corrigidos pela outra sessão nas decisões 142–143, ver Log.)

## Sistema de morte dos Gu (pedido à parte, no meio do arco)

Não fazia parte do plano original, mas o autor pediu no meio do processo: **[[💀 A Morte dos Gu]]** (decisão 129) — escada de condição Saudável→Esgotado→Ferido→Morto, mirar Gu manifestado em combate, escudos que estouram, e a Sobrecarga/Queima de Gu dentro de Golpes Matadores.

## O que ficou deliberadamente em aberto

- **[[🔍 Síntese — Fidelidade ao Romance]], achados 4 e 5** (Terra Abençoada, distribuição populacional de Aptidão) — confiança baixa/moderada, a própria síntese recomendou "vigilância", não ação. Não mexer sem sinal mais forte (outro dado concreto do romance).
- **[[🔍 Síntese — Lacunas do Catálogo de Gu]], candidato borderline** ("Homem que Triunfa sobre o Céu", rank 5 Caminho Humano) — ficou de fora por decisão deliberada (célula já não-vazia, recorrência mais fraca). Registrado pra o autor reconsiderar se quiser.
- **Frequência de Calamidade/Provação acelerando por rank** — a decisão 142 corrigiu os valores mas deixou a aceleração de frequência como pendência explícita (falta o texto do intervalo completo do romance pra calibrar com segurança).

## Coordenação com a outra sessão — o que aprendemos

Há **duas sessões de agente editando este vault em paralelo** (esta, e `azuatz-fb`). Protocolo que funcionou bem depois do primeiro tropeço:

- **Sempre `grep -oE "^[0-9]+\. " "_Processo/🧭 Log de Decisões.md" | sort -n | tail -1` imediatamente antes de escrever uma decisão nova** — não confie em um número que você viu alguns minutos atrás; a outra sessão (ou seus próprios agentes em paralelo) pode ter avançado o contador nesse meio-tempo. Houve pelo menos duas colisões reais nesta sessão (113–118 e depois 137), ambas resolvidas renumerando depois — funcionou, mas checar antes é mais barato que corrigir depois.
- **Avisar a outra sessão por SendMessage antes de tocar território dela**, e esperar confirmação quando a operação for grande. Território muda ao longo do dia (a outra sessão foi de Dedução/Exposição/Refino pra Ameaças/Alma/Simulação) — não presuma que o mapa de território de uma mensagem antiga ainda vale; pergunte ou releia a mensagem mais recente dela.
- **Commits pequenos e frequentes**, um por decisão ou por lote coerente — facilita a outra sessão acompanhar o que mudou sem precisar ler um diff gigante.
