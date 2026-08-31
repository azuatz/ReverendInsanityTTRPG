---
tags:
  - regra
  - combate
  - fechado
aliases:
  - Combate (v1 — multiplicador 1dX × M)
escopo: sistema
---

# ⚔️ Combate

Resolução em d20 (ataque, defesa, testes). **Dano é rolado em dado — sempre.** Gu de ataque, golpe corpo a corpo, Golpe Matador: tudo sai da mesma Escada de Dano abaixo. O que o rank faz é **multiplicar** o resultado do dado, não substituí-lo por um número fixo.

---

## 🪜 A Escada de Dano

Uma escada só, usada pelo jogo inteiro. Todo Gu de ataque e toda arma tem um **passo inicial** nela; efeitos que mexem no dano movem o personagem pra cima ou pra baixo na escada **antes** de rolar.

| Passo | Dado | Passo | Dado |
|---|---|---|---|
| −4 | 1 *(sem rolagem)* | +4 | 1d12 + 1d4 |
| −3 | 1d2 | +5 | 1d12 + 1d6 |
| −2 | 1d3 | +6 | 1d12 + 1d8 |
| −1 | 1d4 | +7 | 1d12 + 1d10 |
| **0** | **1d6** | +8 | 2d12 |
| +1 | 1d8 | +9 | 2d12 + 1d4 |
| +2 | 1d10 | +10 | 2d12 + 1d6 |
| +3 | 1d12 | … | *segue o mesmo padrão* |

**Como a escada continua.** Sempre a mesma lógica: `1d4 → 1d6 → 1d8 → 1d10 → 1d12`. Quando já há um dado adicional, é ele que sobe (`1d12+1d6` → `1d12+1d8`); quando o adicional chega ao d12, ele se soma ao dado fixo e um dado novo começa no d4 (`1d12+1d12` = `2d12`, e o passo seguinte é `2d12+1d4`).

Abaixo de −4 o dano é **0** — nada de dano negativo.

**Nível de Dano** é o nome do deslocamento: "+2 Níveis de Dano" significa subir dois passos. Um Gu que ataca no passo 0 (1d6), com +2 Níveis, ataca em 1d10.

**Dado fora da escada?** Some o resultado máximo e ache o passo mais próximo. Uma arma de `6d6` (máximo 36) entra perto do passo que tiver máximo semelhante, e sobe a partir dali.

**Efeito que concede "um dado adicional"** (em vez de um Nível) sempre dá o **maior dado do passo atual**. Num Gu em `1d12 + 1d6`, um dado adicional é 1d12, não 1d6.

---

## O Multiplicador de Rank (M)

O rank não muda o dado — multiplica o que ele rolar. É a mesma curva que já rege essência, Vitalidade e Alma.

| Rank do Gu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **M** | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |

```
Dano de um Gu de ataque = (dado do passo dele, já ajustado por Níveis) × M do rank do Gu
```

Um Gu de ataque leve de rank 1 no passo 0 causa `1d6 × 1` = 1 a 6. O mesmo perfil de Gu em rank 5 causa `1d6 × 16` = 16 a 96. Multiplicar por potência de 2 é conta de cabeça — role o dado, dobre o tanto de vezes que o rank pedir.

**Vitalidade e Alma escalam pela mesma tabela de M** (ver [[❤️ Recursos e Dano|Recursos e Dano]]). É isso que mantém o dano de rank alto significativo sem ninguém precisar rolar 256 dados.

---

## Ataque e defesa

**Defesa do alvo** é um número fixo na ficha; ninguém rola pra defender. A conta completa está logo abaixo.

**As duas contas:**

```
Acerto = d20 + atributo + (rank do personagem + 2) + rank do Gu que entrega o golpe + treino
Defesa = 10 + DES + rank do personagem + rank do Gu de movimento/defesa ativo
```

**Qual atributo entra no acerto, conforme o que você usa:**

| Você está atacando com... | Atributo |
|---|---|
| **Arma ou corpo, corpo a corpo** | FOR |
| **Arma à distância** (arco, funda, arremesso) | DES |
| **Um Gu de ataque** | VON |

E quando um Gu seu **força um teste no alvo** em vez de rolar acerto (veneno, medo, controle, área):

```
CD dos seus Gu = 10 + VON + rank do Gu
```

Isso é o que faz Força e Vontade serem as duas formas de fazer dano — ver [[💪 Atributos|Atributos]].

### Por que acerto e Defesa sobem juntos com o rank

Os dois crescem com o rank do personagem, mas **o ataque anda 2 à frente da defesa**. O resultado é uma taxa de acerto estável a vida inteira, em vez de um dos lados desandar:

| Situação (mesmo rank, atributos iguais) | Chance de acertar |
|---|---|
| Atacante com Gu do rank dele **vs.** defensor com Gu de movimento do rank dele | **65%** — o padrão do jogo |
| Atacante com Gu **vs.** defensor **sem** Gu de movimento | 80% |
| Corpo a corpo sem Gu **vs.** defensor com Gu de movimento | 50% |

**A leitura de mesa:** um Gu de ataque do seu rank cancela um Gu de movimento do mesmo rank, e sobra o +2 do atacante. Quem não corre atrás de um **Gu de movimento** apanha 80% das vezes — é a razão mecânica pra esses Gu existirem e serem disputados, e é por isso que eles aparecem em todos os ranks do [[📖 Catálogo de Gu|Catálogo]].

**Contra rank diferente**, a conta se resolve sozinha: cada rank de diferença vale 1 ponto no acerto e 1 na Defesa, além de todo o resto (o dano multiplica por M, a RD multiplica por M). Ninguém precisa de tabela extra.

**Só o Gu que entrega o golpe soma o rank dele.** Um Gu do Caminho da Força que amplifica a sua espada não entrega o golpe — a espada entrega, e não há bônus de rank de Gu. Mas um Gu de Transformação que vira **o seu corpo em arma** (garras, forma zumbi) entrega, sim, e soma o rank dele normalmente. É assim que um lutador consegue precisão sem abrir mão do corpo a corpo.

*(Arma à distância sem Gu é raríssima neste cenário — quem ataca de longe usa Gu. A linha existe pra quando alguém quiser um arqueiro, não porque a mesa vá encontrar arqueiros toda sessão.)*

1. **Acertou, role o dano.** Não existe dano extra por "quanto passou" no teste — passar por 1 ou por 15 acerta igual.
2. **Sem crítico automático em 20, sem falha automática em 1** — ver [[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]] ("O que este sistema deliberadamente não tem"). Um 20 natural garante o acerto mesmo contra Defesa alta; nada além disso.
3. **Diferença de rank entre atacante e Gu do alvo:** um Gu de defesa de rank inferior ao do Gu de ataque que o atinge simplesmente não segura o golpe — a defesa cai automaticamente se a diferença for de 2 ranks ou mais, sem teste. É o "esmagamento total" que a diferença de rank promete.

### Redução de Dano (RD)

Gu de defesa e armadura dão **RD**: um número subtraído do dano **depois** de rolado e multiplicado. RD de um Gu de defesa também escala por M — um Gu de defesa de rank 3 com RD base 2 reduz `2 × 4` = 8 de dano.

**RD nunca reduz o dano abaixo de `1 × M`.** Um golpe de um Gu do seu rank sempre machuca alguma coisa, por mais blindado que o alvo esteja — sem esse piso, RD alta zerava ataques inteiros e o combate travava.

Duas fontes de RD **não** somam integralmente: vale a maior, mais metade da segunda (arredonda pra baixo). Isso evita que empilhar três Gu de defesa deixe alguém imune.

### Armadura mortal — o mesmo teto do corpo

**Armadura não multiplica por M.** Ela dá RD fixa, pelo mesmo motivo que um soco não escala: aço é aço, e o mundo não fabrica aço melhor porque você subiu de rank.

| Armadura | RD fixa | Estorvo |
|---|---|---|
| Roupa comum ou reforçada | **0** | — |
| Couro | **1** | — |
| Couro batido, escamas | **2** | — |
| Malha | **3** | −1 em testes de DES |
| Placas | **4** | −2 em testes de DES e furtividade; impossível se esconder |

**Material de fera soma uma vez.** Couro ou osso de uma fera de rank 3 ou acima vale **+1 de RD** na armadura, ou **+1 passo** na arma — uma vez só, não cumulativo, e é a razão pela qual peles de fera valem o que valem no [[🏪 O Mercado]].

Armadura entra na regra de não-empilhamento junto com os Gu de defesa: **a maior, mais metade da segunda.** Na prática, placas (RD 4) são decisivas no rank 1, boas no rank 2, e decorativas do rank 4 em diante, quando um Gu de defesa comum já entrega `1 × M(8)` = 8. **É de propósito:** o arco em que a armadura importa é exatamente o arco em que o personagem ainda não tem Gu para tudo.

**Escala de referência:** RD base **1** é uma defesa comum, **2** é um bom Gu de defesa, **3+** é excepcional e vem com custo pesado. Contra um ataque médio de `3,5 × M`, uma RD de `2 × M` já corta 57% do dano — RD é forte de propósito, e é por isso que os números dela são pequenos.

> ### ⚠️ O que a RD faz com quem ataca de um rank abaixo — leia antes de montar um encontro
>
> O piso é `1 × M` **do Gu que ataca**, não do alvo. Isso significa que um Gu de rank 2 (`M = 2`) contra um alvo com `RD 2 × M(4)` = 16 entrega **2 pontos de dano**, por mais que role bem. O ataque não é reduzido — é **anulado**, e o piso só evita o zero.
>
> Isso é a promessa de "esmagamento total" da diferença de rank funcionando, e está correto. Mas ela tem duas consequências que o mestre precisa ter na mão:
>
> 1. **Um inimigo de rank acima do grupo desliga metade da mesa**, não a enfraquece. Quem não tiver um Gu de ataque do próprio rank vira espectador. Ver o aviso em [[⚔️ Ameaças Genéricas por Rank|Ameaças Genéricas]].
> 2. **A resposta existe e é o [[👻 Caminho da Alma|dano de Alma]]** — ele ignora RD por completo, e é por isso que o Caminho da Alma é o contra-ataque estrutural contra blindagem, e não um Caminho de sabor.
>
> Se um personagem da mesa está preso num Gu de rank inferior porque o Caminho dele não tem ataque no rank atual, **isso é um buraco de catálogo, não uma escolha de build** — conserte escrevendo o Gu que falta.

---

## Dano melee — o corpo tem teto; o Gu quebra o teto

**Um golpe corpo a corpo sem nenhum Gu ativo é dano físico puro e não é multiplicado por M.** Reflete a arma e a Força do personagem, ponto. O passo inicial de cada arma na Escada:

| Arma | Passo inicial | Dado |
|---|---|---|
| Desarmado / arma improvisada | −2 | 1d3 + FOR |
| Arma leve (adaga, punhal) | −1 | 1d4 + FOR |
| Arma média (espada, lança curta) | 0 | 1d6 + FOR |
| Arma pesada (machado, martelo, lança longa) | +1 | 1d8 + FOR |

Um Mestre de Gu de rank 5 batendo **sem Gu nenhum** bate igual a um de rank 1 — a força bruta de um humano tem teto, e ninguém foge disso só por acumular rank.

### A regra que faz o lutador existir

```
Com um Gu do Caminho da Força ou de Transformação ativo,
o DADO DA ARMA passa a ser multiplicado pelo M do RANK DAQUELE GU.

Dano melee com Gu ativo = (dado da arma, ajustado por Níveis) × M do Gu  +  FOR
                                                                          ↑
                                                        a Força NUNCA multiplica
```

Um personagem de rank 5 com arma pesada e um Gu de Força de rank 5 ativo causa `1d8 × 16 + FOR`. Sem o Gu, causa `1d8 + FOR` e nada mais.

> **A Força fica fora do multiplicador, e isso é o pilar virando número.** *O poder não é seu — está emprestado da criatura que você carrega.* O músculo humano é o mesmo no rank 1 e no rank 9; o que cresce é o bicho. Se a Força entrasse dentro do `× M`, um lutador de FOR +4 no rank 5 ganharia **64 pontos de dano de graça** só por ter comprado um atributo na criação, e o corpo dele estaria escalando junto com o Gu — exatamente o que este sistema diz que não acontece.
>
> **O que isso conserta na prática:** sem essa regra, revestir a arma (**amplificar**) batia mais forte que virar a arma (**entregar**) em *toda* faixa de Defesa, e ainda por cima sem gastar essência por golpe — a escolha tática dos [[📖 Catálogo de Gu|Gu dos Cinco Elementos]] não existia, havia só uma resposta certa. Com a Força fora do multiplicador, as duas linhas empatam em dano por rodada e a escolha volta a ser sobre **precisão contra volume**, que é o que ela deveria ser.

Também é o que impede o corpo a corpo de morrer no rank 3. Sem essa regra, um golpe de arma pesada faria ~9 de dano contra uma Vitalidade de 160 no rank 5 — matematicamente zero. Com ela, o mesmo golpe faz `4,5 × 16 + 4` = **76**, e o lutador é uma ameaça de verdade.

**O que muda o dado além disso:** o material da arma, os Gu de Corpo permanentes, e efeitos do inimigo — tudo através de Níveis de Dano na Escada.

### Fontes de Nível de Dano

**Pra cima:**
- **Gu do Caminho da Força ativo:** +1 Nível a cada 2 ranks do próprio Gu (rank 1–2 = +1, rank 3–4 = +2, rank 5–6 = +3, e assim por diante). O rank do Gu importa, não o do personagem. **Vale tanto pro golpe melee quanto pro dado de um Gu de ataque ativo.**
- **Gu de Transformação que aumenta força/resistência física** (vira zumbi, fera, algo maior e mais duro): enquanto ativo, o golpe desarmado passa a contar como uma categoria de arma melhor (garras/presas contam como leve ou média, a critério do Gu) — e pode somar Níveis extras por cima, na mesma lógica do Gu de Força.
- **Arma de material superior** (aço refinado, material raro): normalmente +1 Nível, definido no item.
- **Golpe Matador:** o combo inteiro sobe o núcleo na Escada — ver [[⚡ Golpes Matadores|Golpes Matadores]].

**Pra baixo:** armadura pesada do alvo, um Gu de defesa específico, ou um efeito de enfraquecimento — cada um definido na ficha de quem causa o efeito, tipicamente −1.

**Combinar Gu de Força + Transformação** soma os Níveis dos dois — caro de sustentar (dois Gu ativos ao mesmo tempo), mas é assim que um cultivador vira uma máquina de dano corpo a corpo de verdade.

---

## 🦴 Gu de Corpo — a cadeia permanente do lutador

Uma categoria à parte: Gu que **se instalam na carne e no osso permanentemente**. Depois de assentados, não ocupam vaga de Gu ativo, não comem nada, não podem ser roubados no meio de uma luta e não precisam ser reativados. São a única coisa neste jogo que é de verdade **sua**.

Em troca, o corpo cobra o preço na entrada.

### Constituição é o portão

```
Todo Gu de Corpo exige um mínimo de CON pra ser assentado.
Abaixo do mínimo, o Gu rasga o hospedeiro: o Gu morre e o
personagem leva dano e uma sequela permanente.
```

| Grau do Gu de Corpo | CON exigida | O que costuma dar |
|---|---|---|
| Leve | +1 | +1 Nível de Dano melee, ou +1 de RD natural |
| Médio | +2 | +1 Nível e um efeito secundário (garras contam como arma média, investida, agarrar) |
| Pesado | +3 | +2 Níveis, ou +1 Nível e uma imunidade |
| Extremo | +4 | +2 Níveis e uma transformação corporal visível e irreversível |

### A cadeia: primeiro o esqueleto, depois a força

Isto é o loop de progressão do lutador, e é o que dá à Constituição um papel que nenhum outro atributo tem:

1. **Gu de reforço estrutural** (Ossos de Jade, Ossos de Ferro, Pele de Aço) dão **+1 CON permanente** cada. Eles pedem pouca CON pra entrar — são a porta.
2. Cada +1 de CON **destrava um grau acima** de Gu de Corpo ofensivo.
3. **Gu de Corpo ofensivos** (Força do Crocodilo, Javali Branco e Negro, Tirano da Força) dão **Níveis de Dano melee permanentes** — não dão Força; a Força é o atributo que você comprou, os Níveis são o que o bicho acrescentou.

Um lutador de campanha longa é, literalmente, alguém que **reconstruiu o próprio corpo em camadas**, cada camada permitindo a próxima. É a progressão mais visível do jogo — e a mais difícil de desfazer.

### As regras que impedem isso de virar empilhamento infinito

- **Assentar dói:** teste de **CON CD 15** ao instalar. Falha = o Gu assenta mesmo assim, mas custa **1 Ferimento permanente**.
- **Incompatibilidade:** todo Gu de Corpo declara com o que ele **não** convive. Músculos de Gelo não convive com Gu que exija pele normal; remodelagem óssea não convive com outra remodelagem óssea. Assentar dois incompatíveis faz o personagem **perder o estágio mais recente** e um dos dois efeitos morre (escolha do jogador).
- **Irreversível:** não dá pra desinstalar pra abrir espaço. O que você escolheu aos 16 anos ainda está no seu corpo aos 90.
- **Teto natural:** ninguém passa de **+4 Níveis de Dano permanentes** por Gu de Corpo. Além disso, só Gu ativos e Marcas de Dao.

---

## Golpe crítico na Abertura (opcional, pra cenas de clímax)

Um 20 natural no teste de acerto, contra um alvo já abaixo de 50% de Vitalidade, pode mirar direto na Abertura em vez de só dobrar dano — a critério de quem ataca, puxando um efeito extra em vez do dano normal. Role **1d6**:

| 1d6 | Efeito na Abertura do alvo |
|---|---|
| 1–3 | **Vazamento** — a parede rachou. O alvo perde 2 de Essência automaticamente no início de cada turno dele, até tratar com um Gu de cura ou até a cena terminar |
| 4–5 | **Gu Atordoados** — o choque interno bagunça o ecossistema. Por `1d3` rodadas, o alvo não consegue montar Golpe Matador nenhum, e todo Gu que ativar custa o dobro |
| 6 | **Esmagamento** — um Gu ativo do alvo é escolhido ao acaso (nunca o Gu Vital, que é sempre o último da lista) e morre na hora |

Use com moderação — é ferramenta de clímax de arco, não algo que se aplica em todo 20 natural de toda cena de rotina.

## Iniciativa e ordem de turno

Sem rolar iniciativa a cada cena — mantém o ritmo rápido. Ordem padrão: **por Destreza, do maior pro menor** (jogadores e NPCs relevantes juntos numa lista só); em empate, quem embosca ou tem um Gu de movimento ativo passa na frente. Recalcule só se algo mudar a cena de verdade (alguém ativa um Gu de velocidade no meio do combate, por exemplo) — não a cada rodada.

---

## 🔁 Convertendo um Gu da v1 para a v2

*(Movido de [[⚔️ Combate]] na repaginação de clareza — conversão já concluída em todo o Catálogo desde a decisão 102; guia mantido aqui só de referência histórica.)*

Três passos, e levava dez segundos por Gu:

1. **O dado vem do Caminho** — ver a Tabela de Letalidade em [[⚔️ Combate]].
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

- `2026-08-26` — **dano de Gu deixou de ser fixo e voltou a ser rolado.** "Base N × M" virou "dado da Escada × M". Criada a Escada de Dano única, que agora serve Gu, armas e combos ao mesmo tempo — antes existiam 4 linhas paralelas por categoria de arma e o dano de Gu ficava fora do sistema de Níveis. Adicionada RD (Redução de Dano) como estatística formal, com regra de não-empilhamento.
- `2026-08-26` — Escada de Dano trocada pela tabela de **Níveis de Dano de *Feiticeiros e Maldições* (Setsugiri)**, que é a referência que a mesa queria. Passos −4 a +3 não mudaram (eram idênticos); do +4 pra cima a progressão passou de `2d8 / 2d10 / 2d12 / 3d10…` para `1d12+1d4 / 1d12+1d6 / 1d12+1d8 / 1d12+1d10 / 2d12…` — mais granular e um pouco menos inflacionária no topo.
