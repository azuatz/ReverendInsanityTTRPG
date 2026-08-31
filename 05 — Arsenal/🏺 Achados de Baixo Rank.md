---
tags:
  - regra
  - item
  - guia
aliases:
  - Achados de Baixo Rank
escopo: sistema
---

# 🏺 Achados de Baixo Rank

**Três minigames independentes de rank 1–3** — pequenos, autocontidos, prontos pra encher uma sessão de rank baixo sem virar arco de campanha. Nasceram da mesma leva de leitura integral que gerou o [[🎲 Gerador de Heranças]] e [[🏯 Torres e Estradas de Prova]], mas aqueles dois miram rank 4+; esta nota é o oposto — conteúdo pra quando a mesa ainda está nos primeiros ranks e precisa de "coisa pra fazer" que não seja missão nem combate.

Nenhum dos três inventa sistema de teste novo: os três reaproveitam [[🧩 Refino e Precificação]], as faixas de preço de [[🏪 O Mercado]] e os moldes de [[⚔️ Ameaças Genéricas por Rank]] sempre que fizeram sentido.

---

## 🎰 O Antro de Aposta de Rochas

Uma tenda ou balcão de vila, com uma pilha de **pedras de aposta** — pedaços de rocha comuns, indistinguíveis por fora, que às vezes escondem um Gu morto ou (raríssimo) um Gu vivo ainda dormente. **Comprar é sorte pura: não existe teste de identificação, nem pra Mestre de Gu experiente.** É o cassino do mundo mortal, e funciona porque ninguém sabe o que está comprando.

### Comprar uma pedra

Cinco balcões, por faixa de preço — quanto mais cara a pedra, melhor a chance e maior o prêmio possível:

| Grau | Preço | `d20` no conteúdo |
|---|---|---|
| **1 — Sucata** | **5 Pedras** | 1–14 vazia · 15–19 Gu morto · **20** Gu vivo (rank 1) |
| **2** | **10 Pedras** | 1–12 vazia · 13–18 Gu morto · **19–20** Gu vivo (rank 1) |
| **3** | **20 Pedras** | 1–10 vazia · 11–16 Gu morto · 17–19 Gu vivo (rank 1) · **20** Gu vivo (rank 2) |
| **4** | **40 Pedras** | 1–8 vazia · 9–14 Gu morto · 15–18 Gu vivo (rank 1) · **19–20** Gu vivo (rank 2) |
| **5 — Prima** | **80 Pedras** | 1–6 vazia · 7–12 Gu morto · 13–16 Gu vivo (rank 1) · 17–19 Gu vivo (rank 2) · **20** Gu vivo (rank 3) |

**Vazia:** nada. Pedra comum, dinheiro perdido.
**Gu morto:** uma casca — vende a um refinador por **10% do preço de tabela** de um Gu daquele rank ([[🏪 O Mercado]]), como material de refino comum.
**Gu vivo:** o prêmio de verdade — um Gu dormente de verdade, ainda selvagem, precisa ser refinado normalmente ([[🧩 Refino e Precificação]]) depois de aberto.

Role uma vez por pedra comprada, sempre `d20` puro — **sem bônus de atributo, sem teste**. É o único subsistema do vault ligado 100% ao dado, de propósito: é isso que faz uma tenda de aposta ser uma tenda de aposta, não uma loja.

### Abrir a pedra — grátis, mas cega

Abrir é serviço grátis da casa (ou o próprio jogador quebra a pedra ali mesmo) — e é **sempre malfeito**: se o resultado foi "Gu vivo", a abertura crua sempre mata o Gu escondido antes que ele acorde de vez. Na prática, abrir de graça converte automaticamente qualquer resultado de Gu vivo em Gu morto — a casca ainda vale a venda de 10%, mas o prêmio se perdeu. É o gancho pra empurrar o jogador pro serviço pago abaixo.

### Serviço de dissecação — o profissional que salva o prêmio

Uma cidade grande ou metrópole ([[🏙️ Metrópoles — Centros, Tokens e Arena|Metrópoles]]) tem mestres dissecadores especializados: eles identificam o tipo de casca (ácida, magnética, de fogo, de gelo — a técnica muda por textura da pedra) e abrem com a ferramenta certa, sem matar o que está dentro. **Errar a técnica também mata o Gu** — o serviço reduz o risco, não o zera.

```
d20 + treino do dissecador (+5, padrão)   vs   CD da tabela
```

| Grau da pedra | CD | Custo do serviço |
|---|---|---|
| 1 — Sucata | 10 | **5 Pedras** — não compensa: o serviço custa mais que o valor esperado do conteúdo |
| 2 | 12 | **4 Pedras** |
| 3 | 14 | **3 Pedras** |
| 4 | 16 | **1 Pedra** |
| 5 — Prima | 18 | **Grátis** — dissecadores cobram em reputação, não em Pedras: abrir uma pedra prima com sucesso é propaganda |

Sucesso: revela o conteúdo exatamente como rolado (se for Gu vivo, continua vivo — pronto pra Refino normal). Falha: o Gu morre do mesmo jeito que na abertura grátis (converte pra Gu morto), mas a Pedra do serviço já foi gasta — o dissecador erra, mas cobra.

**Por que funciona na mesa:** é uma loot box física com um vendedor de segunda chance ao lado — o grupo decide, pedra a pedra, se confia na própria sorte ou paga pra reduzir o risco, e nenhuma das duas opções garante nada. Boa cena de vila pequena entre missões, e escala natural: o grupo que enriqueceu na Arena ([[🏙️ Metrópoles — Centros, Tokens e Arena]]) volta pro balcão de grau 5 só pra ver se ainda dá a mesma emoção comprando com trocado.

---

## 🏚️ Heranças de Força — a masmorra pessoal de 4 salas

**Distinta de [[🎲 Gerador de Heranças]]** (rola herança de rank 4–9, multi-Gu, guardião negociável) **e de [[🏯 Torres e Estradas de Prova]]** (masmorra de grupo, andares e rounds escaláveis). Esta é a herança de baixo rank, feita pra **um herdeiro só**: um cultivador moribundo, sem tempo ou recursos pra deixar um cofre elaborado, monta quatro salas fixas e sequenciais — cada uma testando uma única virtude, sem sobreposição. Não há dado de guardião nem tabela de amarra: a estrutura inteira **é** a provação.

**Sequência fixa, sempre nesta ordem** — sala 2 só abre depois da 1, e assim por diante. Não há como pular.

### Sala 1 — A Tina (testa constância)

Um tanque cheio de restos de refino: carcaças, resíduos, fragmentos de Gu que morreram de velhice. Sem porta, sem guardião, sem limite de tentativas — só `1d4 + 2` **lotes** de material bruto pra quem quiser se sujar até o fundo.

Cada lote é um teste estendido de Refino comum ([[🧩 Refino e Precificação]]), **CD 12** (padrão de rank 1). Lote refinado com sucesso rende `1d6 × 10%` do preço de tabela de um Gu de rank 1 em Pedras ([[🏪 O Mercado]]). Ninguém limita as tentativas — o único custo é tempo de cena. **A virtude testada é literal: quem entra, refina um lote e sai leva uma fração do que quem fica catando até o fundo.**

### Sala 2 — Os Três Pilares (testa autocontrole)

Três pedestais, três Gu vivos e prontos — role ou escolha do Caminho do doador e dois Caminhos sinérgicos, rank 1–2, puxados do [[🗂️ Índice de Gu por Caminho]]. Um deles é claramente o mais valioso dos três (maior preço de tabela).

**Regra:** o herdeiro escolhe um e só um, na hora de tocar — não há teste de dado. **Tocar mais de um ao mesmo tempo, ou pegar um segundo depois de já ter escolhido, faz os três Gu morrerem instantaneamente** ([[💀 A Morte dos Gu]]) e a sala fica vazia pra sempre. A virtude é literal também: querer mais do que a herança oferece destrói a herança inteira.

### Sala 3 — O Esqueleto (testa respeito)

Os restos do doador, com um diário, um epitáfio ou uma última mensagem. **Não há teste de CAR nem de qualquer atributo** — é julgamento do mestre sobre a cena que o jogador de fato jogou: ajoelhar, ler em voz alta, deixar uma oferenda, tratar o corpo como gente. O mesmo padrão do 6º passo "Mérito de caráter" do [[🎲 Gerador de Heranças]] — o guardião (aqui, a própria estrutura) está olhando o que o grupo faz quando acha que ninguém está julgando.

Reverência genuína revela um **caminho oculto**: uma câmara lateral com um bônus fixo e garantido, independente de sorte — Pedras equivalentes a **20% do preço de um Gu de rank 2**, sempre entregues, sem rolagem. Ignorar ou pilhar o corpo não fecha a herança (esta provação nunca mata quem falha), só deixa o caminho oculto trancado — a Sala 4 segue exatamente igual.

### Sala 4 — As Bocas Famintas (testa sorte pura)

A câmara final: `1d4 + 1` aberturas na parede — frestas, vasos, bocas de pedra, o que a mesa achar mais macabro — que se abrem em batidas cronometradas e **totalmente aleatórias**, sem padrão perceptível e sem controle do jogador.

O **prêmio total** é fixo, decidido antes de a sala começar: um Gu de rank 2 ou 3 (a régua da campanha decide) mais Pedras equivalentes a 20% do preço dele, dividido em `1d4 + 2` frações iguais.

**Mecânica:** a cada rodada de cena que o personagem espera dentro da câmara, role `1d6`. **5–6:** uma boca se abre e libera uma fração do prêmio. **1–4:** nada, tenta de novo na próxima rodada. O prêmio se esgota depois de liberadas todas as frações — não há mais nada depois disso, para sempre. **Sem teste, sem atributo, nenhum modificador** — é a única sala do vault (fora do Antro de Aposta acima) inteiramente decidida pelo dado cru.

**Por que funciona na mesa:** quatro salas, quatro personalidades diferentes de jogador postas à prova em quinze minutos — o metódico que refina até o fim da Tina, o ganancioso tentado a pegar os três Gu, o cético que zomba do diário e perde o bônus, e todo mundo igualmente refém da sorte na câmara final. É herança pessoal de verdade: um arco de uma sessão só, sem exigir que o mestre prepare guardião nem combate.

---

## 🗝️ O Reino do Tesouro — a porta viva

Um cofre ancestral — de clã, de seita, ou simplesmente um vestígio de alguém rico o bastante pra selar um. **A porta é viva** (uma Vontade guardando, no espírito de [[🧿 Espíritos da Terra]] ou da Vontade do morto do [[🎲 Gerador de Heranças]]) e só reconhece uma linguagem: **troca de valor equivalente**. Não furto, não força, não conversa fiada — o que sai de dentro exige que algo de valor igual ou maior entre no lugar, ali, na hora.

### Como a troca funciona

Dentro, `1d4 + 2` itens dispostos em prateleiras — Gu, receitas, material raro. Cada um tem um valor **secreto**, decidido pelo mestre com antecedência usando as faixas de [[🏪 O Mercado]]:

| `1d6` | Faixa do item |
|---|---|
| 1–2 | Rank 1 (~500 Pedras) |
| 3–4 | Rank 2 (500–1.000) |
| 5–6 | Rank 3 (1.000–10.000) |

Pra tirar um item, o jogador **oferece** algo — Gu, material, Pedras Primordiais, qualquer combinação — na própria porta. O mestre compara o preço de tabela do que foi oferecido contra o valor secreto do item desejado:

- **Oferta ≥ valor do item:** a porta aceita. O item sai, a oferta some (absorvida pela estrutura — não há como recuperá-la depois).
- **Oferta < valor do item:** a porta recusa e **devolve a oferta intacta**. Sem punição pela tentativa errada — é um cofre justo, não uma armadilha. O grupo só descobre se acertou ou errou o preço tentando.

Pagar em Pedras puras sempre funciona, se o grupo tiver o suficiente — é a via mais simples, e a mais cara, porque não tem o desconto que negociar com material teria numa loja de verdade.

### A janela de três respirações

**Um item retirado sem ser refinado na hora volta a ficar selvagem em três respirações** — na mesa, isso é **2 rodadas** a partir do momento em que sai da porta. O jogador precisa **iniciar** o Refino único ([[🧩 Refino e Precificação]]) dentro dessa janela — não terminar, só rolar a primeira tentativa do teste estendido já basta pra prender o Gu ao dono.

Se o prazo passar sem isso, o item volta a selvagem na mesma hora: um Gu vira hostil e ataca (moldes de [[⚔️ Ameaças Genéricas por Rank]] no rank do Gu), e precisa ser subjugado como se fosse caçado do zero, sem nenhum resquício da troca feita. Uma receita ou material simplesmente se desintegra — a estrutura não perdoa hesitação.

**Por que funciona na mesa:** é a única peça deste catálogo com um relógio de verdade — duas rodadas reais de decisão, em voz alta, com o grupo dividindo atenção entre negociar a próxima troca e proteger quem acabou de sacar um item que está prestes a virar inimigo. E resolve sozinho o "problema do grupo pobre chegando num cofre rico": ninguém sai de mãos vazias por falta de dinheiro — sai de mãos vazias por não ter trazido nada que valesse a pena oferecer, o que é gancho de missão, não parede de conteúdo.

---

**🔧 adaptado do romance** (decisão 172 — ver Fase 1, itens 8 e 11, e Fase 2, itens 9 e 10, da [[🔍 Síntese — Atividades Jogáveis por Rank]]). O Antro de Aposta de Rochas e o serviço de dissecação vêm dos digests 01 e 03 (tenda de pedras por faixa de preço, técnica de abertura por tipo de casca); Heranças de Força adapta o modelo de 4 salas do digest 03 (tina de recompensa livre, três pilares, esqueleto/livro, câmara de bocas famintas), mantido pessoal e sequencial de propósito pra não duplicar o [[🎲 Gerador de Heranças]] nem o [[🏯 Torres e Estradas de Prova]]; o Reino do Tesouro adapta a Porta do Tesouro Vivo dos digests 03–04 (troca por valor equivalente, item não refinado voltando a selvagem em três respirações). Nomes de personagens e lugares do romance removidos — sistema reutilizável em qualquer vila, clã ou ruína que a mesa quiser colocar em jogo. Números novos, calibrados pela escala de preços de [[🏪 O Mercado]] (decisão 113) e pela CD de Refino já validada de [[🧩 Refino e Precificação]]; sem simulação própria — é conteúdo de baixo risco econômico (rank 1–3, poucas centenas de Pedras por rodada), não um eixo de balanceamento de combate.
