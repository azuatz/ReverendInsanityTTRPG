---
tags:
  - regra
  - cultivo
  - fechado
aliases:
  - Aptidão e Abertura
escopo: sistema
---

# 🌟 Aptidão e Abertura

A Aptidão decide o tamanho da Abertura de um personagem — a % usada na fórmula de essência em [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]] — e, na prática, o teto natural de rank que ele alcança sem ajuda excepcional.

## Os graus

| Grau | % de Abertura | Teto natural | Papel social típico |
|---|---|---|---|
| **Grau D** | 20%–39% | Rank 1–2 | Base da família — a maioria da população cultivada |
| **Grau C** | 40%–59% | Rank 2, raramente início do 3 | Pilar de uma família comum |
| **Grau B** | 60%–79% | Rank 3–4 | Futuro ancião |
| **Grau A** | 80%–99% | Rank 5, com chance real de Ascensão | "Sorte da família" — prioridade de recursos |
| **Dez Físicos Extremos** | 100%, transbordando | Sem teto natural — mas a provação de Ascensão é ao menos 10× mais perigosa, e a maioria não sobrevive pra contar história | Lenda ou tragédia, quase nunca os dois |

Aptidão não é só o teto — também afeta a **velocidade de recuperação de essência** e quanto custa refinar um Gu (ver [[🧩 Refino e Precificação|Refino e Precificação]]).

### A regeneração — só fora de combate (exceto o Físico Extremo)

**Durante um combate, a Essência não regenera** (decisão 107). O tanque com que você entrou na luta é o tanque da luta inteira — cada ativação é uma decisão, e ficar seco no meio da cena é um dos jeitos clássicos de morrer neste mundo. Pedra Primordial também não repõe essência em combate ([[💠 Economia das Pedras Primordiais]]).

**A única exceção é o [[🌠 Os Dez Físicos Extremos|Físico Extremo]]:** ele recupera **10% da Essência máxima por rodada** (sujeito ao teto de regeneração), e essa torneira aberta — que ninguém mais tem — é a diferença que se sente em toda cena de combate. É a identidade mecânica do físico inteiro.

**Fora de combate**, a Aptidão dita a velocidade de recuperação:

```
Recuperação em descanso = (sua % de Abertura ÷ 10) por minuto
```

Um Grau A (90%) enche um tanque de 360 em ~40 minutos de respiração tranquila; um Grau D leva mais que o dobro. Na prática de mesa: **entre uma cena e outra, todo mundo volta cheio; no meio de uma sequência apertada de cenas, quem tem Aptidão alta se recupera e quem não tem entra pela metade.**

## 🌍 A distribuição do mundo — e por que ela NÃO é a rolagem de criação

> **Furo corrigido:** `1d80+20` distribui os quatro graus em 25% cada. Aplicada à população, essa curva faria **um quarto de todo mundo** capaz de chegar ao rank 5 — e o cenário inteiro pressupõe que rank 5 é lendário. A rolagem está certa; o escopo dela é que precisa ser dito.

**A rolagem de criação descreve personagens jogadores, que são excepcionais por definição** — gente que a Cerimônia do Despertar já separou do resto. A população real segue outra curva:

| Da população total | Resultado na Cerimônia |
|---|---|
| **~70%** | **A Abertura não abre.** Ficam mortais comuns a vida inteira. Não é falha de esforço — é o corpo |
| ~21% | **Grau D** (20–39%) — teto rank 1–2. A base de qualquer clã |
| ~6% | **Grau C** (40–59%) — teto rank 2 |
| ~2,5% | **Grau B** (60–79%) — teto rank 3–4. Um por geração numa vila grande |
| **~0,5%** | **Grau A** (80–99%) — teto rank 5. **Um a cada duzentos que abrem**, ou um a cada seiscentas pessoas |
| **~1 em muitos milhões** | Um dos Dez Físicos Extremos. Uma vez por era, por região |

**Como usar:** role `1d80+20` para PJs e para qualquer NPC que a história declare excepcional. Para preencher população, use a coluna da esquerda — a maioria absoluta de quem o grupo encontra **nunca abriu Abertura nenhuma**, e é exatamente isso que faz um Mestre de Gu de rank 1 ser uma autoridade numa aldeia.

## Como determinar na criação

Duas opções — a mesa escolhe uma pro grupo inteiro, não mistura:

**Opção A — Aleatório puro (recomendado).** Role **1d80 e some 20**. O resultado (21–100) é a **% de Abertura direto** — não existe grau abaixo de 20%, por isso o dado já começa deslocado. O grau do personagem sai sozinho de onde o número cai na tabela acima (por exemplo, tirar 63 é Grau B). Simples, uma rolagem só, cobre toda a faixa jogável de forma equilibrada. **Dez Físicos Extremos não entra nessa rolagem** — é sempre escolha consciente da mesa (ver abaixo), nunca puro acaso, porque vem com uma Dívida do Destino pesada demais pra cair de surpresa num dado.

**Opção B — Grau sugerido + rolagem dentro da faixa.** O mestre sugere o grau que melhor serve o conceito de cada personagem (um prodígio talvez peça Grau A; um coadjuvante do clã talvez sirva melhor em Grau C) — o jogador topa ou negocia. Depois, role **1d20** e some ao mínimo do grau escolhido pra achar a % exata: Grau D = 19 + 1d20, Grau C = 39 + 1d20, Grau B = 59 + 1d20, Grau A = 79 + 1d20. Essa opção dá controle narrativo sobre o teto de cada personagem sem tirar de todo a variação de um dado.

**Dez Físicos Extremos**, em qualquer das duas opções, só entra em jogo se um jogador pedir e a mesa topar — nunca por sorteio automático. É praticamente uma classe de risco à parte: sem teto, mas a Ascensão vira dez vezes mais perigosa (ver acima), e o personagem começa com uma **Dívida do Destino** — um gancho de enredo pendente que a mesa cobra mais cedo ou mais tarde.

## Os Dez Físicos Extremos

> **Tratamento completo em [[🌠 Os Dez Físicos Extremos|Os Dez Físicos Extremos]]** — os cinco físicos jogáveis, a regeneração violenta, a contagem regressiva e as tribulações. O resumo abaixo é só o suficiente pra decidir na criação.

Um Físico Extremo não é "aptidão A+". É outra categoria de existência — e a mecânica reflete os dois lados disso.

**O que ganha:**

| | |
|---|---|
| **Regeneração violenta** | No início de cada rodada de combate, recupera **10% da Essência máxima**, sem gastar ação — sujeito ao [[🏛️ Arquitetura do Sistema\|teto de regeneração]]. Ver [[🌠 Os Dez Físicos Extremos\|Os Dez Físicos Extremos]] pra variação por físico |
| **Cultivo passivo** | A essência nutre as paredes sozinha: avança de estágio ~60% mais rápido que um Grau A |
| **Sem gargalos** | Vantagem em todo teste de Quebra de Paredes, e em testes de ativar Golpe Matador ou refinar Gu **do Caminho correspondente ao físico** |
| **Amplificação** | Gu do Caminho do físico ganham **+2 Níveis de Dano** na Escada — não um rank a mais, só dano |

**O que custa:**

| | |
|---|---|
| **A contagem regressiva** | A **Pressão da Abertura** sobe a cada 6 meses; teste de CON contra `10 + Pressão` ou **−5% de Vitalidade máxima, permanente**. Ver [[🌠 Os Dez Físicos Extremos\|Os Dez Físicos Extremos]] |
| **Como se para** | O relógio zera de duas formas: **subir de rank**, ou **esvaziar a Essência** — gastar poder de forma imprudente é a válvula de escape do físico. E a contagem **cessa de vez no rank 6**: a Abertura Imortal comporta o que o corpo mortal não comportava, mas **a perda já acumulada permanece**. É por isso que todo portador de Físico Extremo é apressado — e é por isso que quase nenhum chega velho |
| **Autoexplosão** | Se a Vitalidade máxima chegar a zero por esse acúmulo, o físico detona. A escala é regional: um portador do Físico da Alma de Gelo do Norte congela uma montanha inteira ao morrer |
| **Tribulações violentas** | Toda Calamidade e Provação, incluindo a Ascensão, vem em escala muito pior |
| **A trava da Ascensão** | Pra ascender, o Gu Imortal vital precisa **corresponder exatamente ao físico** — Físico da Verdadeira Marcialidade da Grande Força exige um Gu Imortal do Caminho da Força, sem substituto |

Na mesa isso vira um personagem que **queima**: absurdamente forte pro rank dele, com um cronômetro rodando o tempo todo, e um único caminho de fuga que é correr pro rank seguinte antes que o corpo ceda. Ótimo pra quem quer intensidade; péssimo pra quem quer jogar devagar.

## Aptidão não é 100% fixa

Existem formas de elevar o próprio grau depois da criação — nenhuma delas barata ou limpa:

- **Gu de aptidão**, extremamente raros, que sobem a % diretamente.
- **Métodos do Caminho do Sangue**, como Gu que convertem vida de parentes em Abertura — poderosos, irreversíveis, e crime capital se descobertos (ver o Gu do Crânio de Sangue no [[📖 Catálogo de Gu|Catálogo de Gu]]).
- **Acúmulo de virtude ou de feitos**, num ritmo lento, através de certos Caminhos ortodoxos.

Nenhum desses é um recurso de rotina — cada um é, no mínimo, o gancho de um arco.
