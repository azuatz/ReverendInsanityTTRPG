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

### Por que o pool em vez do multiplicador

`1d12 × 16` e `16d12` têm **exatamente a mesma média** (104). O que muda é o desvio: o multiplicador plano dava 16 resultados possíveis, espaçados de 16 em 16, e um combate de rank alto virava cara ou coroa. O pool dá uma curva de sino — o dano de rank alto fica **previsível**, que é o que a ficção pede (num confronto entre patamares, quem é mais forte ganha; a incerteza está em *quanto custa*, não em *quem*).

A troca também é o que torna esta reforma segura: **como as médias não mudaram, nenhuma calibragem antiga quebrou.**

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
| **Golpe Matador**                   | +1 por Gu de apoio, até +4 solo e +6 num coletivo. Ver [[⚡ Golpes Matadores]]                                            |
| **Marcas de Dao**                   | +1 por nível de domínio. Ver abaixo                                                                                      |
| **Físico Extremo**                  | +2 nos Gu do Caminho correspondente (+1 se a Abertura estiver Latente)                                                   |
| **Fase Lunar**                      | 0 a +2, ver [[🌙 Caminho da Lua]]                                                                                        |
| **Material da arma**                | +1, definido no item                                                                                                     |
| **Pra baixo**                       | Armadura pesada do alvo, Gu de enfraquecimento, condição ambiental hostil — tipicamente −1                               |

**Abaixo de d4 o dano é 0.** Não existe dado negativo.

---

## ⏱️ Rolagem rápida — como não rolar 256 dados

Obrigatório a partir do rank 5. A média de um dado é `(faces + 1) ÷ 2`: **d6 = 3,5 · d8 = 4,5 · d10 = 5,5 · d12 = 6,5.**

| Quantos dados | Como resolver |
|---|---|
| **1 a 8** | Role todos. É a faixa dos ranks 1 a 4 |
| **9 a 24** | **Role 8 dados** e some a média dos restantes. Mantém a sensação de rolagem sem virar aritmética |
| **25 ou mais** | **Use a média direto.** Role 8 dados só se a cena for um clímax e a mesa quiser o teatro |

### Tabela de médias (já arredondada)

| M | Rank | **d6** | **d8** | **d10** | **d12** |
|---|---|---|---|---|---|
| 1 | 1 | 4 | 5 | 6 | 7 |
| 2 | 2 | 7 | 9 | 11 | 13 |
| 4 | 3 | 14 | 18 | 22 | 26 |
| 8 | 4 | 28 | 36 | 44 | 52 |
| 16 | 5 | 56 | 72 | 88 | 104 |
| 32 | 6 | 112 | 144 | 176 | 208 |
| 64 | 7 | 224 | 288 | 352 | 416 |
| 128 | 8 | 448 | 576 | 704 | 832 |
| 256 | 9 | 896 | 1.152 | 1.408 | 1.664 |

**Some o bônus por dado depois:** `média da tabela + (M × B)`. Um rank 6 d12 no domínio Mestre (B = 2) causa `208 + 64` = **272** sem rolar nada.

---

## Ataque e defesa

A Defesa é um número fixo na ficha; ninguém rola pra defender.

```
Acerto = d20 + atributo + (rank do personagem + 2) + rank do Gu que entrega o golpe + treino
Defesa = 10 + DES + rank do personagem + rank do Gu de movimento/defesa ativo
```

| Você está atacando com... | Atributo |
|---|---|
| **Arma ou corpo, corpo a corpo** | FOR |
| **Arma à distância** | DES |
| **Um Gu de ataque** | VON |

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
2. **Sem crítico automático em 20, sem falha automática em 1.** Um 20 natural garante o acerto contra Defesa alta; nada além disso.
3. **Diferença de 2 ranks ou mais:** um Gu de defesa de rank muito inferior ao do Gu de ataque que o atinge não segura o golpe — cai automaticamente, sem teste.

### Ordem de turno

Sem rolar iniciativa. **Por Destreza, do maior pro menor**, e o **Grau de Densidade soma na ordem** (um Pico passa na frente de um Inicial com a mesma DES). Em empate, quem embosca ou tem Gu de movimento ativo passa na frente.

---

## 🛡️ Redução de Dano (RD)

RD é um número subtraído do dano **depois** de rolado o pool inteiro. RD de um Gu de defesa escala por M: um Gu de defesa de rank 3 com RD base 2 reduz `2 × 4` = 8.

```
Piso: a RD nunca reduz o dano abaixo de M (1 ponto por dado do pool atacante).
```

Duas fontes de RD **não** somam integralmente: vale a maior, mais metade da segunda (arredonda pra baixo).

### Quem fura RD

| Fonte | Efeito |
|---|---|
| **Caminho da Alma** | Ignora RD, armadura e Defesa física por completo. A Defesa contra ele é `10 + VON + rank` |
| **Espada e Relâmpago** (d12) | Ignoram **metade** da RD do alvo |
| **Estágio Pico** | Ignora **metade** da RD do alvo, com qualquer Gu. É o desbloqueio de capstone do rank |
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

**Material de fera de rank 3+ soma uma vez:** +1 de RD na armadura, ou +1 Nível na arma.

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

## 🔁 Convertendo um Gu da v1 para a v2

Três passos, e leva dez segundos por Gu:

1. **O dado vem do Caminho** — olhe a Tabela de Letalidade acima.
2. **O passo antigo do Gu vira Nível** — `passo 0` = o dado do Caminho; `+1` sobe um tipo; `−1` desce um.
3. **`× M` vira `M dados`.**

| Exemplo (v1) | Vira (v2) |
|---|---|
| Gu do Luar, Luz, `1d6 × M` (passo 0) | Luz é d8 → **`M d8`** |
| Gu da Foice Crescente, Lua, `1d8 × M` (passo +1) | Lua é d8, +1 passo → **`M d10`** |
| Gu da Agulha Espectral, Alma, `1d6 × M` (passo 0) | Alma é d12 → **`M d12`** |
| Gu do Ácido Ralo, Veneno, `1d3 × M` (passo −2) | Veneno é d8, −2 → **`M d4`** |
| Gu Imortal do Luar Imemorial, `1d12 × 32` | Lua é d8, mas é Gu Imortal de ataque → **`32 d10`** *(ver nota)* |

*Gu Imortais de ataque sobem **um tipo** sobre o Caminho deles — é o que a Ascensão compra.*

## 📝 Changelog

- `2026-08-28` — **v2: pool de dados cumulativo.** `1dX × M` virou `M dX`; o tipo do dado passou a ser propriedade do **Caminho** (tabela de letalidade em 4 perfis); Níveis de Dano passaram a subir o tipo do dado e depois virar bônus por dado; criada a **Densidade da Essência** como progressão de estágio (+1 por dado por estágio); armas subiram um tipo (d4/d6/d8/d10) e a Vitalidade subiu junto pra manter a calibragem. Ver decisões 77–82.
- `2026-08-26` — dano de Gu deixou de ser fixo e voltou a ser rolado; criada a Escada de Dano única; RD formalizada com regra de não-empilhamento.
