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
| **Dez Físicos Extremos** *(só NPC)* | 100%, transbordando | Sem teto natural — mas a provação de Ascensão é ao menos 10× mais perigosa, e a maioria não sobrevive pra contar história | Lenda ou tragédia, quase nunca os dois |

> **A última linha não é uma opção de ficha.** Os Dez Físicos Extremos são anomalia de mundo — rival, vilão ou gancho de sessão, nunca personagem jogador (decisão 217). Ela está na tabela porque o mestre precisa saber onde eles caem na régua.

Aptidão não é só o teto — também afeta a **velocidade de recuperação de essência** e quanto custa refinar um Gu (ver [[🧩 Refino e Precificação|Refino e Precificação]]).

### A regeneração — só fora de combate

**Durante um combate, a Essência não regenera** (decisão 107). O tanque com que você entrou na luta é o tanque da luta inteira — cada ativação é uma decisão, e ficar seco no meio da cena é um dos jeitos clássicos de morrer neste mundo. Pedra Primordial também não repõe essência em combate ([[💠 Economia das Pedras Primordiais]]).

**A única exceção do sistema inteiro é o [[🌠 Os Dez Físicos Extremos|Físico Extremo]] — e ele é ficha de NPC:** um portador recupera **10% da Essência máxima por rodada** (sujeito ao teto de regeneração). Nenhum personagem jogador tem isso, em hipótese alguma; a torneira aberta existe justamente pra fazer o rival do grupo parecer outra categoria de criatura quando a luta se arrasta.

**Fora de combate**, a recuperação é **uma porcentagem da sua Essência máxima por hora**, ditada pelo Grau de Aptidão:

```
Recuperação em descanso = % da Essência MÁXIMA por hora, pelo Grau:
Grau D: 2%/h  ·  Grau C: 4%/h  ·  Grau B: 6%/h  ·  Grau A: 8%/h
```

**O tempo de recarga se mede em dias, não em minutos** — encher o tanque do zero leva ~50 h (D), ~25 h (C), ~17 h (B) ou ~12,5 h (A), em qualquer estágio (a recuperação é proporcional ao total: tanque maior recupera mais por hora, o tempo cheio é o mesmo). *(📕 Canônico: Cap. 10 — Grau C recupera 4%/h, "24% em 6 horas"; Grau A, 8%/h. Os valores de D e B são interpolação 🔧 entre os dois pontos que a obra dá.)*

**Na mesa, isso significa o ritmo da obra:** quem lutou de manhã chega à luta da tarde com o tanque pela metade. Emendar duas cenas de combate no mesmo dia é uma decisão cara — e é assim de propósito. A válvula de escape é a mesma do romance: **consumir Pedras Primordiais fora de combate** repõe essência na hora ([[💠 Economia das Pedras Primordiais]]) — gastar dinheiro e gastar tempo são a troca central do cultivo.

## 🌍 A distribuição do mundo — e por que ela NÃO é a rolagem de criação

> **Furo corrigido:** `1d80+20` distribui os quatro graus em 25% cada. Aplicada à população, essa curva faria **um quarto de todo mundo** capaz de chegar ao rank 5 — e o cenário inteiro pressupõe que rank 5 é lendário. A rolagem está certa; o escopo dela é que precisa ser dito.

**A rolagem de criação descreve personagens jogadores, que são excepcionais por definição** — gente que a Cerimônia do Despertar já separou do resto. A população real segue outra curva:

| Da população total | Resultado na Cerimônia |
|---|---|
| **~70%** | **A Abertura não abre.** Ficam mortais comuns a vida inteira. Não é falha de esforço — é o corpo |
| ~21% | **Grau D** (20–39%) — teto rank 1–2. A base de qualquer clã |
| ~6% | **Grau C** (40–59%) — teto rank 2 |
| ~2,5% | **Grau B** (60–79%) — teto rank 3–4. Um por geração numa vila grande |
| **~0,5%** | **Grau A** (80–99%) — teto rank 5. **Um a cada sessenta que abrem**, ou um a cada duzentas pessoas |
| **~1 em muitos milhões** | Um dos Dez Físicos Extremos. Uma vez por era, por região |

**Como usar:** role `1d80+20` para PJs e para qualquer NPC que a história declare excepcional. Para preencher população, use a coluna da esquerda — a maioria absoluta de quem o grupo encontra **nunca abriu Abertura nenhuma**, e é exatamente isso que faz um Mestre de Gu de rank 1 ser uma autoridade numa aldeia.

## Como determinar na criação

Duas opções — a mesa escolhe uma pro grupo inteiro, não mistura:

**Opção A — Aleatório puro (recomendado).** Role **1d80 e some 20**. O resultado (21–100) é a **% de Abertura direto** — não existe grau abaixo de 20%, por isso o dado já começa deslocado. O grau do personagem sai sozinho de onde o número cai na tabela acima (por exemplo, tirar 63 é Grau B). Simples, uma rolagem só, cobre toda a faixa jogável de forma equilibrada. **Físico Extremo não sai de dado:** tirar 100 no `1d80+20` é Aptidão 100% e mais nada — sem físico, sem teto de rank removido, sem contagem regressiva.

**Opção B — Grau sugerido + rolagem dentro da faixa.** O mestre sugere o grau que melhor serve o conceito de cada personagem (um prodígio talvez peça Grau A; um coadjuvante do clã talvez sirva melhor em Grau C) — o jogador topa ou negocia. Depois, role **1d20** e some ao mínimo do grau escolhido pra achar a % exata: Grau D = 19 + 1d20, Grau C = 39 + 1d20, Grau B = 59 + 1d20, Grau A = 79 + 1d20. Essa opção dá controle narrativo sobre o teto de cada personagem sem tirar de todo a variação de um dado.

**Nenhuma das duas opções produz um Físico Extremo.** Aptidão 100% não é resultado de criação de personagem — é anomalia de mundo, e mora do lado do mestre.

## Os Dez Físicos Extremos — material de mestre, não de ficha

Existe uma categoria acima do Grau A: um punhado de pessoas nasce com Aptidão **100%**, sem gargalo entre grandes reinos, um corpo que gera mais poder do que consegue conter, e uma contagem regressiva que quase sempre as mata antes da hora.

**Isso não é opção de personagem jogador** (decisão 217). Não se compra com pontos de criação, não se concede como Buff de Lore, e ninguém desperta um durante a campanha. É a peça que o mestre usa quando precisa de um rival que o grupo não alcança cultivando igual — e a ficha completa dele, com a regeneração violenta, a Pressão da Abertura e as tribulações, está em **[[🌠 Os Dez Físicos Extremos|Os Dez Físicos Extremos]]**.

## Aptidão não é 100% fixa

Existem formas de elevar o próprio grau depois da criação — nenhuma delas barata ou limpa:

- **Gu de aptidão**, extremamente raros, que sobem a % diretamente.
- **Métodos do Caminho do Sangue**, como Gu que convertem vida de parentes em Abertura — poderosos, irreversíveis, e crime capital se descobertos (ver o Gu do Crânio de Sangue no [[📖 Catálogo de Gu|Catálogo de Gu]]).
- **Acúmulo de virtude ou de feitos**, num ritmo lento, através de certos Caminhos ortodoxos.

Nenhum desses é um recurso de rotina — cada um é, no mínimo, o gancho de um arco.
