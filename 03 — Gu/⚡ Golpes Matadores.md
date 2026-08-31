---
tags:
  - regra
  - gu
aliases:
  - Golpes Matadores
escopo: sistema
---

# ⚡ Golpes Matadores

Um Golpe Matador não é um Gu — é a combinação de vários Gu, orquestrada como uma única jogada que decide o combate. É a resposta deste sistema ao que a obra chama de *killer move*: o motivo pelo qual um cultivador de rank baixo consegue matar alguém acima dele, uma vez, com tudo preparado.

## Estrutura: núcleo + apoio

Todo Golpe Matador tem duas partes:

- **O Gu núcleo** — o que realmente causa o efeito decisivo (o dano, a captura, a negação). Normalmente o Gu mais forte ou mais específico que o personagem possui.
- **Os Gu de apoio** — Gu mais fracos, baratos, cuja única função é garantir que o núcleo acerte: imobilizar o alvo, cegar, atrasar a reação, esconder a preparação. Sozinhos, quase inúteis; juntos, viabilizam o golpe.

Montar um Golpe Matador exige que os Gu envolvidos sejam ativados em sequência, geralmente ao longo de mais de um turno de preparação — o que o torna arriscado fora de uma emboscada ou de um momento em que o alvo está momentaneamente vulnerável. Um Golpe Matador interrompido no meio (o alvo foge, percebe, ou os Gu de apoio falham) raramente pode ser refeito na mesma cena — os Gu de apoio gastam sustento, e o elemento surpresa já era.

## O que o combo faz, em número

Um Golpe Matador **empurra o Gu núcleo pra cima na [[⚔️ Combate|Escada de Dano]]**. É assim que ele vira dano de matar alguém acima do seu rank sem inventar uma regra nova:

| Gu de apoio no combo | Efeito no núcleo | Exige estágio |
|---|---|---|
| 1 | +1 Nível de Dano | Inicial |
| 2 | +2 Níveis | Médio |
| 3 | +3 Níveis, e o alvo tem desvantagem pra resistir | Alto |
| 4 | +4 Níveis, e o alvo tem desvantagem pra resistir | **Pico** |

**O teto de apoios é o [[🪜 Ranks e Estágios|Teto de Combo]] do seu estágio menos um** — o núcleo também ocupa uma vaga. É uma regra só, não duas: o estágio diz quantos Gu cabem no golpe, e cada apoio vale +1 Nível. Um Golpe Matador **coletivo de 4 personagens** continua chegando a +6 (decisão 32).

> [!note] Por que +4 não desequilibra
> O freio é o custo, que cresce com o quadrado do tamanho do combo: um golpe de 5 Gu num Caminho só custa `(40×5) × 5 = 1.000` de essência, contra 640 do de 4 Gu. O quarto apoio se paga sozinho — e só existe no Pico, que é o topo da progressão de estágio.

Um Gu de apoio só conta se **fizer alguma coisa de verdade** pelo golpe — imobilizar, cegar, atrasar, esconder a preparação, furar defesa. Empilhar três Gu de ataque não é Golpe Matador, é gastar essência.

Golpes de apoio que não somam dano somam **outra coisa**: +2 no teste de acerto, ignorar a RD do alvo, ou impedir uma reação. A mesa escolhe junto com o jogador na hora de montar o golpe, e aquilo fica registrado na ficha — Golpe Matador não se improvisa toda cena, se **desenvolve** e se repete.

## O que um Golpe Matador custa

Um combo não custa a soma dos Gu — custa **muito mais**, porque forçar vários Gu a agir como uma coisa só é a parte cara:

```
Custo = (soma dos custos de ativação dos Gu do combo) × (número de Gu no combo)
Golpe Matador HÍBRIDO (Gu de dois ou mais Caminhos) → × 2 além disso
```

| Exemplo | Conta | Custo |
|---|---|---|
| Combo de 3 Gu, um Caminho só, rank próprio | (40×3) × 3 | **360** |
| Combo de 4 Gu, um Caminho só | (40×4) × 4 | **640** |
| Combo de 4 Gu, **híbrido Lua + Alma** *(2 Gu de Lua a 40, 2 de Alma a 50)* | (80+100) × 4 × 2 | **1.440** |

**O multiplicador híbrido é o freio da build mais forte do sistema.** Combinar dois Caminhos num golpe só é a coisa mais poderosa que um personagem consegue fazer — o alvo enfrenta duas defesas diferentes no mesmo turno, e quase ninguém tem as duas. O dobro de custo é o que impede isso de ser a resposta pra tudo: mesmo com o maior tanque da mesa, um golpe híbrido é **uma vez por combate importante**, não uma rotina.

Contra o [[🏛️ Arquitetura do Sistema|teto de regeneração]] de **100/rodada** (decisão 28 — os 200 são o cenário *ideal*, não o normal), um híbrido de 1.440 são **quinze rodadas de regeneração**. É um recurso de arco disfarçado de ação.

## Quantos golpes cabem na ficha

```
Golpes Matadores registrados = AST + 1
```

Um Golpe Matador não se improvisa: é uma sequência treinada, ensaiada e memorizada, e a cabeça de um cultivador só guarda um número limitado delas prontas pra sair sob pressão. Com AST +0 você tem **um** golpe a campanha inteira; com AST +4, cinco.

**Trocar um golpe registrado por outro** leva um arco de reclusão e treino — não se faz entre cenas.

É por isso que Astúcia importa pra quem nunca vai deduzir nada: ela é o teto do seu repertório tático.

## 🎲 O teste de conjuração — e a Retaliação

Montar um combo sob pressão pode dar errado. **Na rodada em que o golpe dispara**, faça:

```
Teste de Conjuração = d20 + AST + nível de domínio no Caminho do núcleo
CD = 12 + (2 × número de Gu no combo)
```

| Combo | CD |
|---|---|
| 2 Gu | 16 |
| 3 Gu | 18 |
| 4 Gu | 20 |
| 5 Gu *(coletivo)* | 22 |

**Modificadores:** −4 se você **já usou este golpe registrado antes com sucesso** (a sequência é treinada) · +4 se está improvisando um combo que não está na ficha · +2 se sofreu dano desde a última rodada · −2 se teve uma rodada inteira de preparação sem ser incomodado.

Um golpe registrado, treinado e usado em condições decentes passa quase sempre. **O teste existe pra punir improviso e pressão**, não pra tornar o recurso principal do personagem uma loteria.

### A Retaliação de Essência

Falhar no teste de conjuração não é só "não acontece nada". Os Gu foram forçados a agir juntos e a coisa colapsou por dentro:

| Falha | O que acontece |
|---|---|
| **Falha normal** | O golpe não sai · você **perde a essência inteira** que ele custaria · todos os Gu do combo ficam **inutilizáveis pelo resto da cena** |
| **Falha por 5 ou mais** | O acima · **Retrocesso** completo (ver [[❤️ Recursos e Dano\|Recursos e Dano]]): `(soma dos ranks dos Gu) × 2` em Vitalidade e `× 1` em Alma |
| **1 natural** | O acima · **um Gu de apoio escolhido ao acaso morre** (nunca o Gu Vital, que só fica ferido) · **1 Ferimento permanente** · a Abertura fica instável: todo Gu custa o dobro até um descanso longo |

**Num golpe híbrido** (dois ou mais Caminhos), toda linha acima piora: a Retaliação usa `× 3` em Vitalidade, e o 1 natural mata **dois** Gu de apoio. Forçar Caminhos diferentes a cooperar é a coisa mais instável que se faz com Gu, e quando falha, falha feio.

**Num Golpe Matador Coletivo**, quem rola o teste é o dono do núcleo — mas **todos os participantes sofrem a Retaliação**. É por isso que ninguém entra num combo coletivo com alguém em quem não confia.

## 🎯 Contra quem vale disparar

**Abaixo de um alvo de Chefe, o Golpe Matador custa mais do que devolve.** Isso não é opinião de mesa — está medido em [[🎯 Simulação de Combate — Resultados]]: um grupo que dispara o combo contra um inimigo mediano cai de **97% para 76% de vitória** na mesma cena. Gastar o golpe errado perde a luta com mais frequência que apanhar.

A conta é direta. Um combo de 3 Gu do próprio rank custa **360** de essência, e **720** se for híbrido — contra um custo de **40** por ativação comum. Você está trocando **nove a dezoito ataques normais** por um só. Só compensa quando o alvo não cairia com dezoito ataques normais.

| Alvo | Vale? |
|---|---|
| **Chefe**, ou qualquer inimigo de rank acima do seu | **Sim.** É exatamente para isto que o combo existe |
| **Elite** que já está no meio da luta | Só se ele for o último de pé, ou se a cena vai acabar naquela rodada |
| **Guerreiro, Mestre de Gu, Recruta, horda** | **Não.** Ataque normal duas vezes rende mais e deixa o tanque cheio |
| **Alvo que você não vai conseguir acertar** | Nunca. O custo é pago no disparo, e errar não devolve nada |

**A faixa perigosa é o rank 2 e o rank 3.** É onde a Essência já dá para pagar um combo, mas pagar um **esvazia o tanque** — no rank 1 ninguém consegue pagar, e no rank 5 o custo é troco. Um personagem de rank 2 ou 3 que abre a cena com um Golpe Matador passa o resto dela batendo com a arma.

> Diga isso aos jogadores **antes** da primeira cena de combate. A punição é severa, é correta, e não está visível em lugar nenhum da ficha.

## 🕳️ A Brecha — todo golpe tem uma, e ela é escrita

**Nenhum Golpe Matador pode ser registrado sem uma Brecha declarada.** Vale pra PJ e pra NPC, sem exceção.

Uma Brecha é uma condição concreta sob a qual o golpe falha ou fica muito pior. As quatro categorias válidas:

| Categoria | Exemplo |
|---|---|
| **Ambiental** | Não funciona no ar, debaixo d'água, à noite, sob teto, em terreno aberto |
| **De preparação** | Exige uma marca plantada no alvo com antecedência; sem ela, o golpe erra sozinho |
| **De janela** | Abre uma vulnerabilidade durante a montagem — a defesa cai, a posição se revela, o corpo fica exposto |
| **De acúmulo** | Piora a cada uso na mesma cena, ou transforma o usuário permanentemente se usado demais |

### Descobrir a Brecha alheia

Quem **viu o golpe ser usado ao menos uma vez** pode tentar deduzi-la: teste de AST, CD 14, contra o Golpe Matador observado — três sucessos antes de duas falhas, ao longo de uma cena de análise fora de combate.

Quem conhece a Brecha e a explora: o golpe **perde todos os Níveis de Dano do combo** (o núcleo dispara sozinho, no passo base) e o executor **sofre o Retrocesso mesmo assim**, porque montou o combo inteiro. É devastador — e é pra ser.

## 🤝 Golpe Matador Coletivo

Vários cultivadores montando um golpe único, cada um contribuindo com os Gu dele. O romance faz isso o tempo todo — combos de três e quatro pessoas são rotina — e **num grupo pequeno isso é a ferramenta mais forte que existe** — com 3 participantes chega a +5 Níveis, com 4 a +6.

- **Some os Gu de apoio de todos os participantes.** Com 3 PJs, é realista chegar a **+5 Níveis de Dano** no núcleo — território que nenhum deles alcança sozinho.
- **Todos gastam a ação do turno**, e todos pagam o custo de essência da própria parte.
- **O núcleo é de um só**, e é ele quem rola o dano. Os outros são apoio.
- **Uma Brecha compartilhada.** Se qualquer participante for neutralizado, atordoado ou movido antes do disparo, **o golpe inteiro falha e todos sofrem o Retrocesso**.

Essa é a peça que faz um grupo pequeno parecer maior que a soma das partes — e a razão mecânica pela qual vale a pena o inimigo separar o grupo antes de lutar. Um mestre que entende isso constrói encontros em torno disso.

## Golpe Matador de rank 5 — o portão da imortalidade

Um Golpe Matador montado com Gu núcleo de rank 5, **usado com sucesso contra um oponente de rank 5 ou superior**, é um dos dois portões que permitem tentar a [[♾️ A Ascensão Imortal|Ascensão Imortal]] — a rota de quem não conseguiu refinar um Gu Imortal.

Isso torna "desenvolver o meu Golpe Matador de rank 5" um objetivo de campanha declarado, não um detalhe tático. Ver [[📖 Catálogo de Gu|Catálogo de Gu]] pra exemplos prontos.

## O contragolpe (backlash)

Forçar um combo assim tem custo pro próprio corpo do cultivador — não é grátis nem sem risco pra quem executa. Depois de um Golpe Matador bem-sucedido, o personagem sofre um Ferimento ou fica com a Vontade reduzida até descansar; a maioria dos cultivadores guarda o golpe pra uma única vez por combate importante, não pra repetir à vontade.

## Golpes Matadores e o Caminho

Depois da [[♾️ A Ascensão Imortal|Ascensão Imortal]], um Golpe Matador tende a refletir o Caminho do cultivador — um Caminho de Veneno monta combos de debilitação progressiva, um de Ilusão monta combos que terminam antes do alvo perceber que o combate começou. Antes da Ascensão, um Golpe Matador é só o que o jogador conseguiu montar com os Gu que tinha — e é justamente esse padrão repetido, sessão após sessão, que sinaliza qual Caminho o personagem está trilhando sem saber.

## Como criar um pra um personagem (jogador ou NPC)

1. Escolha o Gu núcleo — o que ele faz e qual rank.
2. Escolha 1 a 3 Gu de apoio que preparam o terreno pro núcleo acertar.
3. Descreva a sequência: o que precisa acontecer, em que ordem, pra o combo funcionar.
4. Defina o contragolpe: o que o próprio cultivador paga depois.
