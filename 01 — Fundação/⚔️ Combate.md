---
tags:
  - regra
  - combate
  - fechado
aliases:
  - Combate
escopo: sistema
---

# ⚔️ Combate

Resolução em d20 (ataque, defesa, testes). **Dano é um pool de dados acumulados.** O rank não multiplica um dado — ele diz **quantos dados você rola**. O Caminho diz **qual dado**. O estágio e os Níveis dizem **quanto cada dado soma**.

> O porquê deste desenho está nas decisões 77–82 do [[🧭 Log de Decisões]]; a versão anterior do motor, em [[_Arquivo/⚔️ Combate (v1 — multiplicador 1dX × M)|_Arquivo]].

---

## 🎲 A fórmula única

```
DANO = M d(dado do Caminho)  +  (M × B)

M  = quantos dados      → o rank DO GU        (1·2·4·8·16·32·64·128·256)
d? = qual dado          → o Caminho do Gu     (d6 · d8 · d10 · d12)
B  = bônus POR DADO     → Densidade da Essência + Níveis de Dano excedentes
```

Na mesa isso é uma frase só: **"role seus dados, e some o número de dados vezes o seu bônus por dado."**

Um Gu de Alma de rank 3 (M = 4, Caminho d12) de um cultivador no estágio Alto (B = 2) causa `4d12 + 8` — de 12 a 56, média 34.

---

## 🗡️ A Tabela de Letalidade dos Caminhos

**O dado é uma propriedade do Caminho, não do Gu.** Todo Gu de Alma rola d12; todo Gu de Terra rola d6. É isto que dá a cada Caminho um perfil que se sente antes de qualquer texto de sabor.

A regra que equilibra a tabela: **quanto maior o dado, menos o Caminho faz além de dano.**

| Perfil | Dado | Caminhos | O que ganha | O que paga |
|---|---|---|---|---|
| **⚡ Letalidade direta** | **d12** | **Alma** · **Espada/Lâmina** · **Relâmpago/Trovão** | O maior dano do jogo. Alma ignora RD e armadura por completo; Espada e Relâmpago **ignoram metade da RD** | **Nenhum efeito colateral, nunca.** Estes Gu causam dano e mais nada. Sem debuff, sem controle, sem utilidade fora de combate |
| **🔥 Dano alto** | **d10** | **Fogo** · **Vento/Ar** · **Osso** · **Metal** | Dano forte, e **um efeito de 1 rodada** no acerto (queimadura, deslocamento forçado, sangramento) | Efeito curto e sem escolha — vem junto com o dano ou não vem. Sem sustentação, sem controle de terreno |
| **🌙 Moderado + controle** | **d8** | **Lua** · **Luz** · **Gelo** · **Sangue** · **Escravidão** · **Veneno** · **Água** · **Sombras** | Dano constante **mais atrito real**: essência congelada, lentidão, sangramento acumulado, cativeiro, veneno que dura. É o perfil que **ganha lutas longas** | Nunca mata numa ação. Precisa de tempo, e o tempo é o que uma emboscada não dá |
| **🧠 Utilitário / suporte** | **d6** | **Sabedoria** · **Terra** · **Madeira** · **Sonhos** · **Formações** · **Espaço** · **Cosmos/Tempo** · **Informação** · **Sorte** · **Humano** · **Alimentação** · **Refino** | Dano ruim de propósito. Em troca: **+2 na CD de todos os seus Gu**, alcance sem teto prático, e o direito de **ignorar regras convencionais de combate** — tirar alguém da cena sem dano, negar uma ação inteira, agir fora da ordem de turno, atravessar distância | Se a luta virar troca de golpes, você perde. Este Caminho não disputa dano — ele decide que a disputa de dano não vai acontecer |

**Duas exceções que valem anotar:**

- **Sombras** rola d8 normalmente, mas **d12 contra um alvo que não sabe onde você está.** É a assinatura do Caminho, e é o que faz a preparação pagar.
- **Força** não tem dado próprio: ele **empresta o dado da arma** e sobe o tipo dela (ver *Dano melee*, abaixo).

> ### ⚖️ A leitura de mesa
>
> Contra um alvo com Vitalidade de rank igual, o número de acertos pra derrubar é: **d6 ≈ 5 · d8 ≈ 4 · d10 ≈ 3,3 · d12 ≈ 2,8.** Essa é a escala inteira de letalidade do jogo, e ela é estável em todos os nove ranks.
>
> Um Caminho d6 leva quase o dobro de acertos que um d12. Se o seu Gu de Terra parecer fraco em combate, **ele está correto** — o poder dele está na coluna da direita da tabela, e usá-lo como Gu de ataque é jogar errado.

---

## ⚡ Níveis de Dano — como tudo que "aumenta dano" entra

Existe uma moeda só, e ela funciona em dois tempos:

```
1º  Enquanto o dado for menor que d12, +1 Nível SOBE o tipo:
        d4 → d6 → d8 → d10 → d12
2º  Uma vez em d12, cada Nível excedente vira  +1 POR DADO  (soma em B)
```

Uma regra só cobre a escada inteira, do chão ao teto. Um Gu de Terra (d6) que ganha +4 Níveis vira d12 e mais +1 por dado. Um Gu de Alma (d12) que ganha +4 Níveis vira `M d12 + 4M`.

### De onde vêm os Níveis

| Fonte                               | Quanto                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Densidade da Essência** (estágio) | **+1 por dado por estágio** acima do Inicial — entra direto em B, nunca sobe o tipo do dado. Ver [[🪜 Ranks e Estágios]] |
| **Passo próprio do Gu**             | O que a ficha dele disser. Um Gu "passo +1" começa um tipo acima do dado do Caminho dele                                 |
| **Gu do Caminho da Força ativo**    | +1 Nível a cada 2 ranks do próprio Gu (rank 1–2 = +1, 3–4 = +2, 5–6 = +3)                                                |
| **Golpe Matador**                   | +1 por Gu de apoio, até o **Teto de Combo do estágio menos um** (Inicial +1 · Médio +2 · Alto +3 · Pico +4); +6 num coletivo de 4. Ver [[⚡ Golpes Matadores]] |
| **Marcas de Dao**                   | +1 por nível de domínio. Ver abaixo                                                                                      |
| **Físico Extremo**                  | +2 nos Gu do Caminho correspondente (+1 se a Abertura estiver Latente)                                                   |
| **Fase Lunar**                      | 0 a +2, ver [[🌙 Caminho da Lua]]                                                                                        |
| **Material da arma**                | Não dá mais Nível: material especial dá **+1 no acerto** (definido no item)                                              |
| **Pra baixo**                       | Nada tira Nível: Gu de enfraquecimento e ambiente hostil dão **−2 no acerto** do atacante; armadura pesada protege via **RD**, nunca via Nível |

**Abaixo de d4 o dano é 0.** Não existe dado negativo.

---

## ⏱️ Rolar é obrigatório — o dano nunca é fixo

**Dano é sempre rolado, em qualquer rank.** A graça do pool é a incerteza — trocar os dados pela média transforma o clímax da campanha em aritmética, e foi decidido que isso não acontece nesta mesa (decisão 103).

Pra rolar 32+ dados sem travar a mesa: rolem em punhados (8 de cada vez, somando), ou usem um rolador digital (`/roll 64d12` em qualquer bot de Discord). O que não se faz é substituir a rolagem por um número pronto.

---

## Ataque e defesa

A Defesa é um número fixo na ficha; ninguém rola pra defender.

```
Acerto = d20 + atributo + (rank do personagem + 2) + rank do Gu que entrega o golpe
Defesa = 10 + DES + rank do personagem + rank do Gu de movimento/defesa ativo
```

*(Ataque **não** soma bônus de treino — o treino vale só em teste de perícia, ver [[💪 Atributos]], decisão 215.)*

| Você está atacando com... | Atributo |
|---|---|
| **Arma ou corpo, corpo a corpo** | FOR |
| **Um Gu de ataque** | VON |

**Não existem armas à distância mundanas.** Arco, besta e funda não fazem parte do arsenal deste mundo — ataque à distância é trabalho de Gu, sempre (decisão 104). Quem quer alcance carrega um Gu de ataque à distância.

E quando um Gu **força um teste no alvo** em vez de rolar acerto:

```
CD dos seus Gu = 10 + VON + rank do Gu          (+2 se o Caminho for do perfil d6)
```

### As taxas que a fórmula produz

| Situação (mesmo rank, atributos iguais) | Chance de acertar |
|---|---|
| Atacante com Gu do rank dele **vs.** defensor com Gu de movimento do rank dele | **65%** — o padrão do jogo |
| Atacante com Gu **vs.** defensor **sem** Gu de movimento | 80% |
| Corpo a corpo sem Gu **vs.** defensor com Gu de movimento | 50% |

1. **Acertou, role o pool.** Não existe dano extra por "quanto passou" no teste.
2. **20 natural é crítico:** acerta automaticamente, mesmo contra Defesa maior, e **dobra os dados de dano** — role `2 × M` dados em vez de `M`. O bônus por dado não dobra: o crítico fica `2M d(dado) + (M × B)`. **Sem falha automática em 1** — errar por número é só errar.

> **Exemplo resolvido, passo a passo:** um rank 3 (M = 4) ataca com um Gu de Fogo (d10) de rank 3, estágio Médio (B = 1). Rola `d20 + VON + (3+2) + 3 + treino` contra a Defesa do alvo — passou. Rola o pool: `4d10 + (4×1)` = `4d10 + 4`, digamos 22 no dado + 4 = **26**. O alvo tem RD 6 de armadura: `26 − 6 = 20` de dano final na Vitalidade dele.

> [!warning] Fratura da Abertura *(decisão 131 — ainda sem simulação)*
> Crítico que deixa o alvo com **25% ou menos** da Vitalidade máxima: role `1d6`.
>
> | 1d6 | Efeito |
> |---|---|
> | 1–2 | **Vazamento** — perde `1 × M` de Essência no início de cada turno seu, até tratado por Gu Médico ou fim de cena |
> | 3–4 | **Gu Atordoados** — todo Gu ativo dele fica Esgotado por 1 rodada ([[💀 A Morte dos Gu]]); próximo Golpe Matador custa o dobro |
> | 5 | **Fratura funda** — desvantagem no próximo Teste de Morte, se precisar de um nesta cena |
> | 6 | **Esmagamento** — um Gu ativo dele, sorteado (nunca o Vital), fica Ferido |
3. **Diferença de 2 ranks ou mais:** um Gu de defesa de rank muito inferior ao do Gu de ataque que o atinge não segura o golpe — cai automaticamente, sem teste, e fica **Esgotado**; com 3+ ranks de diferença, **morre espatifado**. Mirar um Gu manifestado, e o resto do que mata Gu em combate: [[💀 A Morte dos Gu]] (decisão 129).

> [!tip] Uso criativo, sem custo de ponto *(decisão 130)*
> Quando o jogador descreve um uso não-óbvio de um Gu — explorar o dado do
> Caminho, o ambiente, uma combinação inesperada — de um jeito que muda a
> situação tática de verdade (não só descrição bonita), o mestre pode conceder
> **Vantagem** (2d20, fica com o maior) no teste daquela ação, **ou** impor
> **Desvantagem** (2d20, fica com o pior) na defesa do alvo. Nunca os dois ao
> mesmo tempo, e no máximo uma vez por cena por personagem. Não consome Essência
> extra nem Ponto de Plano — é crédito de imaginação, e o incentivo para usar Gu
> com esperteza em vez de só empilhar dano.

### Iniciativa

**Rolada no início do combate**, uma vez, e a ordem vale a cena inteira:

```
Iniciativa = d20 + DES
```

Empate: maior DES fica na frente; persistindo, quem embosca ou tem Gu de movimento ativo passa primeiro. Gu e efeitos que mexem na iniciativa (ex.: Grilo Pílula-de-Dragão) somam nessa rolagem.

---

## 🐌 Lentidão — a condição de controle mais comum

`Lentidão N` aparece em Gu, Ações Especiais e efeitos de terreno por todo o vault. É sempre a mesma coisa:

```
Lentidão N = metade do deslocamento do alvo por N rodadas
```

Sem número, "Lentidão" sozinha vale `N = 1`. Alguns efeitos somam `−2 DES` junto — a ficha do Gu diz quando.

---

## 🛡️ Redução de Dano (RD)

RD é um número subtraído do dano **depois** de rolado o pool inteiro. RD de um Gu de defesa escala por M: um Gu de defesa de rank 3 com RD base 2 reduz `2 × 4` = 8.

```
Piso: a RD nunca reduz o dano abaixo de M (1 ponto por dado do pool atacante).
```

**Duas fontes de RD não somam: vale só a maior.** Armadura e Gu de defesa não se empilham — anote o maior dos dois e pronto.

> [!note] Por que a regra encolheu *(decisão 223)*
> A versão anterior era "a maior **mais metade da segunda**". Medido, isso somava **no máximo +2 de RD**, e nunca escalava — a armadura mortal é fixa (1 a 4) enquanto a RD de Gu é `base × M` e dobra a cada rank, então a segunda fonte já era irrelevante do rank 3 em diante (6-12% da RD total) e valia ±1 nos ranks 1-2. Trocar isso pela conta mais simples do jogo custa quase nada — e **alinha a regra escrita com as quinze rodadas de simulação, que sempre modelaram uma fonte só**.

### Quem fura RD

| Fonte | Efeito |
|---|---|
| **Caminho da Alma** | Ignora RD, armadura e Defesa física por completo. A Defesa contra ele é `10 + VON + rank` |
| **Espada e Relâmpago** (d12) | Ignoram **metade** da RD do alvo |
| **Quase-Supremo** (Marcas) | Ignora RD de qualquer fonte de rank inferior |

> ⚠️ **O que a RD faz com quem ataca de um rank abaixo.** O piso é `M` **do pool que ataca**. Um Gu de rank 2 (2 dados) contra um alvo com RD 16 entrega **2 pontos**. O ataque não é reduzido — é **anulado**, e o piso só evita o zero. Um inimigo de rank acima do grupo **desliga** metade da mesa em vez de enfraquecê-la. A resposta estrutural é o [[👻 Caminho da Alma|dano de Alma]], e é por isso que ele rola d12 e não tem efeito colateral nenhum.

### Armadura mortal — o mesmo teto do corpo

**Armadura não escala com M.** Aço é aço.

| Armadura | RD fixa | Estorvo |
|---|---|---|
| Roupa comum | **0** | — |
| Couro | **1** | — |
| Couro batido, escamas | **2** | — |
| Malha | **3** | −1 em testes de DES |
| Placas | **4** | −2 em DES e furtividade; impossível se esconder |

**Material de fera de rank 3+ soma uma vez:** +1 de RD na armadura, ou **+1 de acerto** na arma.

---

## 🤜 Dano melee

Sem Gu ativo, o corpo é o corpo: **um dado só, sem pool**, porque a força humana não escala com rank.

| Arma | Dado |
|---|---|
| Desarmado / improvisada | **d4** + FOR |
| Leve (adaga, punhal) | **d6** + FOR |
| Média (espada, lança curta) | **d8** + FOR |
| Pesada (machado, martelo) | **d10** + FOR |

### A regra que faz o lutador existir

```
Com um Gu do Caminho da Força ou de Transformação ativo:

Dano melee = (M do Gu) d(dado da arma, ajustado por Níveis) + FOR + (M × B)
                                                               ↑
                                                 a Força NUNCA entra no pool
```

Um rank 5 com machado pesado e um Gu de Força de rank 5 ativo, no estágio Alto: `16d10 + FOR + 32` — média **120 + FOR**. Sem o Gu: `1d10 + FOR`, média 5,5 + FOR.

> **A Força fica fora do pool, e isso é o pilar virando número.** *O poder não é seu — está emprestado da criatura que você carrega.* O músculo humano é o mesmo no rank 1 e no rank 9; o que cresce é o bicho. Se a Força entrasse no pool, um lutador de FOR +4 no rank 5 ganharia 64 pontos de graça por ter comprado um atributo na criação.

---

## ☯️ Marcas de Dao — o dano depois do rank 6

A partir do rank 6 não há mais estágios, e portanto não há mais Densidade. **O nível de domínio ocupa o lugar dela em B.**

| Nível de domínio | Marcas no Caminho | **B** | Pool |
|---|---|---|---|
| **Vislumbre** | 1 – 999 | +0 | M |
| **Pequeno Feito** | 1.000 – 9.999 | **+1** | M |
| **Mestre** | 10.000 – 49.999 | **+2** | M |
| **Grão-Mestre** | 50.000 – 149.999 | **+3** | M |
| **Quase-Supremo** | 150.000 – 299.999 | **+4** | M |
| **Grande Mestre Supremo** | 300.000+ | **+5** | **2 × M** — o único lugar do jogo onde o pool dobra |

O pool dobrado no topo é o que torna verdadeira a promessa da ficção: um rank 8 Grande Mestre Supremo causa `256d12 + 640` (média **2.304**) contra os `256d12` (média **1.664**) de um Venerável recém-chegado ao rank 9. **Densidade de Marca vence rank**, mas só no último degrau.

Todas as capacidades não-numéricas de cada nível de domínio seguem inalteradas em [[☯️ Marcas de Dao]].

---

## 📝 Changelog

- `2026-08-30` — **Rodada do autor (decisões 103–106):** dano passa a ser **sempre rolado** (rolagem rápida por média removida); **iniciativa passa a ser rolada** (`d20 + DES`); **crítico no 20 natural** dobra os dados de dano; **armas à distância mundanas removidas** (alcance é trabalho de Gu); desbloqueios de estágio (resistência/ordem, ativação com desconto, Pico ignorar ½ RD) removidos — o estágio agora dá só o que está na tabela mestre. Regra antiga arquivada em `_Arquivo`; fontes menores de Nível de Dano convertidas em acerto/RD (decisão 112).
- `2026-08-28` — **v2: pool de dados cumulativo.** `1dX × M` virou `M dX`; o tipo do dado passou a ser propriedade do **Caminho** (tabela de letalidade em 4 perfis); Níveis de Dano passaram a subir o tipo do dado e depois virar bônus por dado; criada a **Densidade da Essência** como progressão de estágio (+1 por dado por estágio); armas subiram um tipo (d4/d6/d8/d10) e a Vitalidade subiu junto pra manter a calibragem. Ver decisões 77–82.
- `2026-08-26` — dano de Gu deixou de ser fixo e voltou a ser rolado; criada a Escada de Dano única; RD formalizada com regra de não-empilhamento.
