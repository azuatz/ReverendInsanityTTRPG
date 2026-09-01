---
tags:
  - processo
  - balanceamento
  - simulação
aliases:
  - Simulação de Combate — Resultados
escopo: processo
---

# 🎯 Simulação de Combate — Resultados

> [!important] Rodada mais recente
> A **décima sexta rodada** ([[#🌑 Décima sexta rodada — o nerf do Caminho da Alma e o Xie Lang 80:20 (2026-08-31)|2026-08-31]]) corrige o erro de modelagem mais caro do vault e usa a correção para nerfar o Caminho da Alma com número. **(1) O Xie Lang nunca foi atacante de Alma puro:** ele é **80:20 Lua:Alma**, e Lua é d8 que atravessa RD normalmente. Medido no perfil certo, a dominância de PvP dele cai de **83,9 / 97,8 / 99,5%** para **33,4 / 39,9 / 43,6%** — ele sai do 1º lugar e vira **3º de 4** nos três ranks, e o novo topo da mesa é o **Jiāotáng** (93,5 / 78,3 / 70,3%, decrescente com o rank). *(Os 88,1% publicados eram duplamente obsoletos: perfil errado **e** o `ess_mod = 1,0` que a decisão 227 reverteu.)* **(2) A diretiva do autor culpava o furo de RD, e a medição mostra que a culpa é de outro lugar:** o número que dezesseis rodadas nunca calcularam é **quantos acertos zeram a barra de Alma** — **1,85 / 2,12 / 2,21**, contra os **2,8** que a decisão 78 promete ao degrau mais letal do jogo. A barra é um terço menor que a Vitalidade e a Defesa que a protege cresce **+1/rank** contra um acerto que cresce **+2/rank** (no rank 5 ela **não erra nunca**). **(3) Dos três candidatos, só um funciona:** meia-RD e d10 deixam o especialista de Alma em **96-99%** (nerfs no papel, não no número); a **barra endurecida** (`(16+3×VON+3×B)×M` e Defesa `+2/rank`) leva o especialista de **99,5% para 87,1%**, a escada da barra de 2,21 para **2,63**, não toca dado nenhum — e custa **+0,24pp** na bateria de grupo, com o quinhão de dano do Caminho em cena de grupo **inalterado**, que era a promessa a cumprir. Aplicada em [[⚔️ Combate]] (decisão 231), com um ripple de oito notas listado.
>
> A **décima quinta rodada** ([[#⛈️ Décima quinta rodada — tribulação, face RD e a mesa sem o Físico (2026-08-31)|2026-08-31]]) constrói o **motor de tribulação** — o subsistema que catorze rodadas de combate nunca tinham modelado — e o usa para três vereditos pedidos pelo autor. **(1) O fork da CD de Calamidade está resolvido:** o vault publicava duas fórmulas incompatíveis, e a de [[🌩️ Calamidades e Provações]] (`14 + 2 × (rank − 6) + faixa`) é a correta — a de [[⛈️ A Vontade do Céu]] conta a faixa duas vezes, é indefinida abaixo de Marcado, não escala com rank e torna Perseguido e Alvo do Céu **insobrevivíveis em todo rank** (97,9-100% de mortalidade por Provação). O motor novo **reproduz a curva da quarta rodada** (2,2/48,3/70,2% → 0,2/49,9/76,2%) escrito do zero. **(2) A escala de escalonamento por excesso de Marcas é brutal e NÃO-MONOTÔNICA:** a banda de +10-25% (que importa a regra de morte da Provação) deixa **2,9%** de sobrevivência em cem anos internos, contra **25,7%** da banda de >+50% que deveria ser a pior. **(3) A face RD do Nível de Potência não entra** — a variante simétrica é um no-op aritmético exato, e a assimétrica estoura o alvo de 7-9 rodadas **sem melhorar a vitória**, quebra a escada da decisão 78 por +0,54 a +0,66 (quatro a cinco vezes o ajuste que a 11ª tinha na direção certa) e infla a vitória do grupo em +14,85pp de média. **(4) O Xie Lang sem o Físico da Lua Antiga NÃO cai para o mais fraco:** ele perde 1,0pp de dominância em PvP e continua vencendo 97,8-99,5% de qualquer duelo — a dominância sempre veio do Caminho da Alma, não do Físico. Três achados 🔴 novos, o maior deles estrutural: **a escada de CD por rank ultrapassa a ficha, e nada na ficha a alcança**.
>
> A **décima quarta rodada** ([[#🧭 Décima quarta rodada — a bateria estendida (2026-08-31)|2026-08-31]]) é a **bateria estendida** pedida pelo autor: as cenas solo remedidas com o piso da Horda, o primeiro PJ × PJ do motor atual, e a quarta saída do fork do treino. Quatro achados: **(1)** a Horda de 8 contra um PJ isolado deixou de ser guerra de atrito e virou **execução** (vitória 0-37%, ~5 rodadas — 10 de 12 células ≤ 1%), e o alvo de 7-9 rodadas solo é **inatingível** com qualquer variante medida (proporcional 2-3, `VIT × n/4`): solo, duração e piso pedem coisas opostas; **(2)** o Rei de Cem solo caiu de "melhor caso 8,4%" pra **0,0-0,1%** — a sentença que o design promete, agora absoluta; **(3)** no PvP a degeneração de 1-2 rodadas que o F&M teme não é a norma, mas **Xie Lang vence 84-99,5% de qualquer duelo** (80-100% das vitórias por queda de Alma) e o Lee segue no fundo, como na era Perl; **(4)** o **híbrido do treino** (mortal sem treino + escada só nos moldes de rank 6+) recupera os ranks 7-9 como a saída (c) **com 0,00pp de custo na fase mortal** — mas superaquece o rank 6 (ΔB 0: 51,8% → 4,4%). Nenhuma regra mudou; tudo devolvido ao autor com número.
>
> A **décima terceira rodada** ([[#✅ Décima terceira rodada — validação final conjunta (2026-08-31)|2026-08-31]]) é a **validação final conjunta** do lote de decisões 146-210 — o mesmo papel que a sexta rodada teve para as 103-133. Primeiro corrige o motor, que ainda modelava **Alma zerada como morte permanente** enquanto a decisão 205 já mandava tratá-la como inconsciência (Colapso Espiritual): medido com a mesma semente nos dois modelos, o efeito é **0,00pp na vitória em 25 de 25 células** e **+0,003 sobrevivente de 4** — a decisão 206 (Alma rara) tornou o Colapso raro, e ele é relógio de campanha, não alavanca de combate. Depois confere cada número publicado: **19 das 20 células da tabela de composição batem dentro de 3pp**, o **"~99%" do Rei de Cem Feras e o "0%" do Rei de Mil sobrevivem** ao piso da Horda, e a coluna de Vitalidade da Varredura não drifou. **Oito números foram corrigidos**, dois deles graves: a **tabela de ações do Chefe** contradizia a tabela de composição da própria nota (57% contra 3% para a mesma cena de rank 1), e a **régua ΔB imortal** só é dial de verdade no **rank 6** — nos ranks 7-9 nem um inimigo três níveis acima ameaça (98% de vitória do grupo no rank 9). E ao medir a decisão 211 (bônus de treino escalado, aplicada às regras durante esta rodada) apareceu o achado que ninguém procurava: **o motor nunca modelou o bônus de treino que [[💪 Atributos]] põe na fórmula de acerto de Gu** — ligar isso move a tabela +12,6pp em média, dos quais só +2,7 são da decisão 211 e +9,9 são uma lacuna antiga. **Nada foi republicado por causa disso**: é fork de design, devolvido ao autor com três saídas medidas, e a nota ganhou um aviso 🔴.
>
> A **décima segunda rodada** ([[#🗡️ Décima segunda rodada — a peça de muitas ações (2026-08-31)|2026-08-31]]) mede a **opção 4** da pendência da decisão 208 — a peça de **muitas ações e pouca Vitalidade** (molde "Enxame": `7 × M` de Vitalidade, 2 ações, `M d4`, sem RD e sem especial), desenhada pelo autor para *desacoplar* duração de dificuldade. **Veredito: a hipótese não se sustenta, e nada foi aplicado.** Encurta só 5,8% (pior que a alavanca mais fraca da rodada anterior), põe Difícil em 5,8-23,8% e Clímax em 1,2-40,0% (muito fora das faixas), e deixa o penhasco de ações mais íngreme em 4 de 6 células. O achado que fecha o caso é um guarda-corpo novo: a peça é **ameaça de primeira linha ou decorativa dependendo de o grupo focá-la ou não** — 10 a 16 ações executadas se ignorada, 0,56 a 2,40 (abaixo do Recruta solto) se focada — o que faz a dificuldade da cena oscilar **16,2pp em média e até 59,3pp**, contra 3,1pp das cenas publicadas. Nenhuma Vitalidade de `7 × M` a `14 × M` satisfaz as duas metades: **a solda entre duração e dificuldade se repete dentro da própria peça.**
>
> A **décima primeira rodada** ([[#⏱️ Décima primeira rodada — encurtando a cena (2026-08-31)|2026-08-31]]) mede as três alavancas de encurtamento da decisão 160 **isoladas** (RD menor · mais dano por Nível · menos inimigos), contra o alvo do autor de ~4-6 rodadas e com dois guarda-corpos: a curva de letalidade da decisão 78 e o penhasco de ações da decisão 137. **Veredito: nenhuma passa limpa, e nada de motor foi aplicado.** RD menor encurta só 6-13% (mas é a única que *melhora* a fidelidade à decisão 78); mais dano por Nível encurta 13-23% reescrevendo a escada de letalidade inteira; menos inimigos encurta 25% e apaga a escada de dificuldade (Padrão vira 99-100%). O achado estrutural: **duração e dificuldade são o mesmo botão** — a cena é governada pelo número de corpos, não pela dureza deles. Menu de quatro saídas devolvido ao autor em "Em aberto".
>
> A **décima rodada** ([[#🔇 Décima rodada — Alma rara entre inimigos (2026-08-31)|2026-08-31]]) aplica a diretiva do autor "inimigos muito raramente terão poder de Alma": o molde Mestre de Gu troca o default da especial de Alma pela física, com o cultivador de Alma virando exceção rolada (1d6 = 6). Achado principal, **contraintuitivo e medido**: Alma rara torna as cenas 2-10pp MAIS difíceis, não mais fáceis — uma especial de Alma isolada desperdiça o golpe numa barra que nada mais ataca; os limites das decisões 135/137 já tinham removido a pilha que fazia Alma matar. Tabela de composição atualizada pros números do mix rolado; três células fora da faixa histórica (Padrão r1, Difícil r1-2) escaladas ao autor.
>
> A **oitava rodada** ([[#🏰 Oitava rodada — bateria de grupo nos ranks imortais (2026-08-31)|2026-08-31]]) fecha a última lacuna de cobertura: a primeira bateria de **grupo × cena nos ranks imortais (6-9)**, com dois perfis de densidade de Marca por rank. Achado principal: **a escada de dificuldade das composições mortais colapsa acima do rank 5** — quase toda cena vira ≥93% de vitória do grupo, e a dificuldade *cai* conforme o rank sobe. O dial de dificuldade imortal é o **diferencial de nível de domínio** (ΔB), não a composição — registrado como pendência nomeada pro autor, sem mexer nas tabelas.
>
> A **sétima rodada** ([[#🔁 Sétima rodada — cura real remedida (2026-08-31)|2026-08-31]]) remede a bateria completa da sexta rodada trocando a heurística de cura (`M d8`, sem limite) pelo Gu real da ficha do Lee (**Gu do Broto Restaurador**, decisão 155: `M d6`, uma vez por cena) — fechando a pendência de "Em aberto" que a decisão 155 tinha deixado. **Nenhum número da sexta rodada precisou mudar de leitura**: as diferenças ficam dentro do ruído de Monte Carlo já aceito no vault (a maior é de ~6pp, a maioria 1-4pp), sem nenhuma composição cruzando de "ganhável" para "perda na maioria das vezes" ou vice-versa. A sexta rodada permanece como registro de referência do motor completo (Golpe Matador Coletivo, controle, terreno); a sétima só substitui a peça de cura.
>
> A **sexta rodada** ([[#🏁 Sexta rodada — validação completa pós-decisão 133 (2026-08-31)|2026-08-31]]) é a validação final do motor **completo** — decisões 103 a 145, com as composições de cena JÁ corrigidas (Padrão/Difícil por limite de Alma e por rank, decisões 135-137) e as quatro peças que nenhuma rodada anterior tinha modelado: **Golpe Matador Coletivo**, **cura** (com taxa de acionamento medida), **condições de controle** (Lentidão, implementada pela primeira vez) e **terreno** (com a composição atual de "Difícil"). Cobre ranks 1-5 (rank 4 pela primeira vez) e revalida o cenário duplo-gênio de rank 6. A quinta rodada logo abaixo continua valendo como o registro de quando o motor v2 pós-decisão 133 foi medido pela primeira vez, e como referência de comparação. As rodadas 1-4 mais abaixo são auditoria histórica do motor v1/v2 inicial — os números delas **não** descrevem o sistema como ele é hoje.

Auditoria quantitativa do sistema em Monte Carlo, **3.000 combates por cenário**, com os quatro personagens da mesa, rodada nos **ranks 1, 2, 3 e 5**.

> [!info] O que o modelo implementa
> Ordem de turno por Destreza sem rolagem · `Acerto = d20 + atributo + (rank + 2) + rank do Gu + treino` contra Defesa · Escada de Dano completa com `× M` · RD com piso de `1 × M` e não-empilhamento · dano de Alma ignorando RD · Essência com **escala por estágio** (`% × 4 × 2^(estágio−1)`), regeneração base (`% ÷ 10`) e teto · Manutenção de Sustentação quadrática, com o personagem **desligando um Gu sustentado** quando a Essência cai abaixo de 25% · dano melee pela decisão 64 (`(dado × M) + FOR`) · **Golpe Matador** com custo, teste de conjuração, multiplicador híbrido e Retaliação · **cura** (`1d8 × M` quando um aliado cai abaixo de 40%) · **condições de controle** (Lentidão custando ação, e o Chefe ignorando a primeira) · **terreno** Wu Xing (±2 Níveis) · **hordas** e **ações especiais** de inimigo.
>
> **Premissa de catálogo:** todo personagem tem o Gu de ataque do próprio rank, em todo rank. O catálogo do vault é para ser completo — onde o tipo de Gu faz sentido para o Caminho, ele existe. Uma lacuna é item a escrever, nunca um dado de balanceamento.

---

## As quatro fichas simuladas

| | **Xie Lang** | **Jiāotáng** | **Lee** | **Demvi** |
|---|---|---|---|---|
| Caminho | Lua + Alma | Sangue + Força | Cinco Elementos | Vento |
| Aptidão | 86% | 76% | 63% | 56% |
| FOR/CON/DES | −1 / +3 / +3 | +4 / +3 / +2 | +3 / +2 / +2 | −1 / +1 / +4 |
| AST/VON/CAR | +2 / +3 / +2 | +1 / +1 / 0 | +1 / +3 / +1 | +2 / +3 / +2 |
| Papel no modelo | Controle + Golpe híbrido | Melee, paga em Vitalidade | Melee versátil + cura | Defesa alta, controle |

Estágio acompanha o rank (rank 1 → Inicial, rank 4+ → Pico), que é o que a progressão do vault espera.

---

## 🆕 Quinta rodada — motor v2 pós-decisão 133 *(2026-08-30)*

Reimplementação completa do motor em Python (as rodadas 1-4 eram um script em Perl, arquivado; este vive em [[simulacoes/2026-08-30-motor-v2-pos-decisao-133.py|_Processo/simulacoes/2026-08-30-motor-v2-pos-decisao-133.py]]). **3.000 iterações por cenário**, limite de 20 rodadas, semente fixa `20260830`. Mesmas composições de cena da terceira rodada (Fácil = Horda de 8 · Padrão = 3 Mestres de Gu · Difícil = 4 Mestres de Gu · Clímax = 1 Chefe + 1 Guerreiro especial, ações do Chefe pela tabela por rank), pra manter a comparação limpa.

### O que mudou desde a última rodada

- **Crítico no 20** dobra os dados (decisão 105), sem falha automática em 1.
- **Iniciativa rolada** uma vez por combate (`d20+DES`), não mais por Destreza fixa (decisão 106).
- **Essência não regenera em combate** (decisão 107) — nos quatro PJs da mesa (nenhum é Físico Extremo com a regra ligada), o tanque é o que a Densidade permitiu no início da cena e nada mais.
- **41 fontes de Nível de Dano viraram acerto/RD/atributo** (decisão 112) — não muda a simulação diretamente (nenhuma das quatro fichas usava essas fontes), mas fecha a contabilidade.
- **Fratura da Abertura** (decisão 132): crítico que deixa o alvo a ≤25% da barra rola 1d6 (Vazamento de Essência · Gu Atordoados · nada · Esmagamento de um Gu) — implementada e medida pela primeira vez.
- **Gênio pobre duplo** (decisão 133): um NPC rank 6 real-Pequeno-Feito pode empilhar dois feitos de compreensão e operar como Grão-Mestre — cenário novo, medido pela primeira vez.
- **Refinamento de modelagem** (não é mudança de regra, é correção de fidelidade): as rodadas 1-4 tratavam "dano de Alma ignora RD" como um bônus contra a Vitalidade. A leitura literal de [[⚔️ Combate]] e da ficha do Xie Lang é que o dano de Alma **drena a barra de Alma**, com Defesa própria (`10+VON+rank`) — uma barra bem menor que a Vitalidade e sem RD nenhuma a proteger. Esta rodada modela isso corretamente, e é a maior causa isolada da queda de número que segue.
- **Correção de um bug de script** encontrado nesta própria rodada: a primeira versão do script esqueceu a decisão 82 ("todo inimigo usa o mesmo Grau de Densidade do grupo") — sem ela, o rank 5 saía 100% de vitória em toda cena, porque só os PJs ganhavam o bônus de Densidade. Corrigido antes de fechar os números abaixo.

### Ranks 1, 2, 3 e 5 — comparando com a terceira rodada

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** — Horda de 8 | 100% · 4,00 *(igual)* | 100% · 4,00 *(igual)* | 100% · 3,99 *(igual)* | 100% · 3,99 *(igual)* |
| **Padrão** — 3 Mestres de Gu | **68,3% · 2,04** ↓ de 99% | **77,1% · 2,05** ↓ de 98% | **84,7% · 2,15** ↓ de 98% | **95,7% · 2,62** ↓ de 98% |
| **Difícil** — 4 Mestres de Gu | **12,0% · 0,31** ↓↓ de 75% | **9,6% · 0,21** ↓↓ de 63% | **11,3% · 0,20** ↓↓ de 56% | **30,0% · 0,55** ↓↓ de 59% |
| **Clímax** — Chefe + Guerreiro especial | **3,5% · 0,09** ↓↓ de 56% | **56,6% · 1,51** ↓ de 62% | **85,9% · 2,11** ↑ de 80% | **87,4% · 2,06** ↑ de 73% |

*(vitória do grupo · sobreviventes de 4; comparação contra a terceira rodada, [[#🔁 Terceira rodada — com o arsenal completo]], linha "Chefe + Guerreiro especial" no Clímax)*

**Fácil não mudou** — a Horda não tem dano de Alma nem pressão de essência relevante (os PJs matam Recrutas rápido demais pra gastar o tanque), então nenhuma das mudanças de regra a toca.

**Padrão e Difícil caíram em todos os ranks, e a queda do Difícil é desproporcional.** A causa raiz é a mesma nos dois: cada Mestre de Gu dispara a especial de Alma **na primeira ação que tem** — e como o motor agora acerta a barra de Alma como recurso separado e pequeno (60-70% do tamanho da Vitalidade, sem RD nenhuma), 3 ou 4 especiais de Alma disparando essencialmente todas na primeira rodada da cena é um alfa-strike quase simultâneo contra uma barra que qualquer um dos quatro PJs tem em quantidade pequena. Com 3 Mestres (Padrão), geralmente sobra 1 PJ que não foi alvo do estouro inicial e consegue estabilizar a cena — daí a queda ser dolorosa mas não fatal (68-96%). **Com 4 Mestres (Difícil), os quatro PJs recebem um estouro de Alma cada, e a queda vira de 56-75% para 10-30% em TODO rank** — é um efeito estrutural do "4 especiais vs. 4 barras pequenas", não um efeito que melhora ou piora com o rank do grupo (por isso a queda é praticamente uniforme: -63, -53, -45 e -29 pontos percentuais).

**O Clímax teve o comportamento mais interessante: piorou no rank 1, e melhorou nos ranks 3 e 5.** No rank 1, a essência sem regeneração (decisão 107) é o fator dominante: o tanque de um PJ rank 1 (`aptidão% × 4`, sem multiplicar por M) dá de 5 a 8 ativações de Gu antes de cair pro corpo a corpo cru — e numa luta de Chefe que se estende por 7+ rodadas, os PJs ficam sem essência bem antes do fim e passam a bater com `1d4-1d10 + FOR`, incluindo dois personagens com FOR negativo (Xie Lang e Demvi). Nos ranks 3 e 5, o Grau de Densidade (Alto/Pico) multiplica o tanque de essência por 4-8×, e essa pressão desaparece — o que sobra é só o crítico (mais dano ocasional pros dois lados) e a Fratura, que não é grande o bastante pra derrubar o grupo, então o Chefe fica **relativamente mais fácil** que na rodada anterior.

### Rank 6 — o NPC "Imortal Denso Duplo-Gênio" (decisão 133)

Cenário novo: rank 6, real **Pequeno Feito** (~9.000 Marcas no Caminho principal, dado d12), mas com os **dois** feitos de compreensão da decisão 133 empilhados — opera como **Grão-Mestre** (+3 Níveis de Dano) apesar da contagem real. Chefe de uma cena Clímax (+ 1 Guerreiro especial de apoio) contra os 4 PJs adaptados pro rank 6 (recém-ascendidos, domínio Vislumbre — B efetivo 0, essência tratada como equivalente ao Grau Pico mortal por analogia, já que a regra de essência de Imortal não está escrita).

| Cenário | Vitória do grupo | Sobreviventes |
|---|---|---|
| **Duplo-gênio** (Grão-Mestre por empilhamento, B=+3) | **5,2%** | 0,09 / 4 |
| Controle — mesmo NPC **sem** empilhar (Pequeno Feito real, B=+1) | **20,0%** | 0,36 / 4 |

**O empilhamento da decisão 133 tem impacto medível e grande: quase 4× a diferença na taxa de vitória do grupo** (20,0% → 5,2%, uma queda de 14,8 pontos percentuais só por causa de +2 Níveis de Dano extras no Chefe). Isso confirma que a regra faz o que o autor queria — um rank 6 duplo-gênio é **muito** mais perigoso que um rank 6 denso comum — mas também confirma que **mesmo sem o empilhamento, um Chefe rank 6 contra um grupo recém-ascendido já é extremamente duro** (20% de vitória, praticamente nenhum sobrevivente médio).

> [!warning] Achado a sinalizar — não corrigido nesta rodada
> **5,2% de vitória é do tamanho de "não é um encontro, é uma sentença"**, no mesmo espírito da regra já existente "nunca um Chefe de rank acima do grupo" ([[⚔️ Ameaças Genéricas por Rank]]) — aqui o rank é igual, mas o domínio não é, e o efeito prático é parecido. Isto é coerente com a leitura canônica que motivou a decisão 133 (um Fang Yuan ou uma You Lan de Grão-Mestre no rank 6 **deveria** ser aterrorizante para outro rank 6 comum), então **não é necessariamente um bug de balanceamento** — mas o autor deve decidir se quer que a nota de [[⚔️ Ameaças Genéricas por Rank]] diga isso em voz alta (algo como "nunca um duplo-gênio contra um grupo recém-ascendido, pelo mesmo motivo que nunca um Chefe acima do rank") em vez de deixar o mestre descobrir na mesa.

### Fratura da Abertura — o impacto medido, contra a estimativa da auditoria de 3DeT

A decisão 132 entrou como regra viva sem simulação prévia, com a auditoria de 3DeT estimando **+5 a 10% de letalidade**. Medição: liga/desliga a regra nos mesmos 9 cenários (ranks 1, 3 e 5 × Padrão/Difícil/Clímax), mesma composição, 3.000 iterações cada lado.

| rank · cena | Com Fratura | Sem Fratura | Δ na vitória do grupo |
|---|---|---|---|
| 1 · Padrão | 66,7% | 68,0% | +1,2 pp |
| 1 · Difícil | 11,7% | 12,7% | +1,0 pp |
| 1 · Clímax | 3,9% | 3,7% | −0,2 pp |
| 3 · Padrão | 84,9% | 85,0% | +0,1 pp |
| 3 · Difícil | 11,9% | 11,2% | −0,6 pp |
| 3 · Clímax | 87,0% | 86,6% | −0,4 pp |
| 5 · Padrão | 96,0% | 96,5% | +0,4 pp |
| 5 · Difícil | 29,8% | 29,9% | +0,1 pp |
| 5 · Clímax | 87,7% | 87,6% | −0,1 pp |

*(Δ = vitória sem Fratura menos vitória com Fratura; positivo = a Fratura reduz a vitória do grupo)*

**A estimativa de 5-10% de letalidade extra NÃO se confirma — o efeito medido é da ordem de ruído estatístico (média de 0,2 ponto percentual, nunca mais que 1,2 em qualquer cena testada).** Duas razões, ambas visíveis no próprio desenho da regra: **crítico é raro** (5% por ataque, dos dois lados), e o **gatilho de ≤25% de Vitalidade** exige que o alvo já esteja perto de cair — na maioria dos casos em que a Fratura dispara, o combate já estava decidido pelo dano do próprio crítico, e o 1d6 extra raramente muda o resultado final da cena. **Recomendação para o autor:** a estimativa da auditoria de 3DeT pode ficar como estava registrada no Log (é uma estimativa, não uma medição), mas esta simulação mostra que **não há necessidade de ajustar o gatilho de 25% para 15%** como a decisão 132 cogitava — o problema que motivaria esse ajuste (letalidade excessiva) não aparece nos números.

### Metodologia e simplificações desta rodada

Documentadas no cabeçalho do script — resumo: cada PJ ataca com um único Gu "de assinatura" (Xie Lang = Alma d12 ignorando RD/na barra de Alma; Jiãotáng = melee com Gu de Força, arma pesada d10; Lee = Gu elemental genérico d8; Demvi = Vento d10); Lentidão e outras Condições de controle não são modeladas (como nas rodadas 2-4); Golpe Matador só é tentado pelo Xie Lang, só nos cenários Clímax de rank mortal, contra o Chefe; a essência de Imortal (rank 6) usa por analogia o fator do Grau Pico mortal, na ausência de fórmula própria no Log. Nenhuma dessas escolhas está registrada como regra — são decisões de modelagem, revisáveis numa rodada futura.

### 🩹 Correção do achado — limitar Mestres com especial de Alma *(2026-08-30, mesmo dia)*

Rodada de verificação da correção adotada para o item "Em aberto" do [[🧭 Log de Decisões|Log]] (o alfa-strike de dano de Alma acima): **limitar quantos Mestres de Gu com especial de Alma aparecem juntos fora de uma cena Clímax**, trocando os demais pela especial física de rank equivalente que a nota de [[⚔️ Ameaças Genéricas por Rank#🧑‍🦱 Mestre de Gu — o inimigo humano|Mestre de Gu]] já ensinava ("Como variar sem refazer a ficha"). A regra de Alma em si (ignora RD, [[👻 Caminho da Alma]]) não muda — ela continua absoluta contra um só atacante de Alma ou numa cena Clímax. Script: [[simulacoes/2026-08-30-correcao-composicao-alma.py|_Processo/simulacoes/2026-08-30-correcao-composicao-alma.py]], mesma metodologia (3.000 iterações/cenário, ranks 1/2/3/5, mesma semente `20260830`), partindo do motor desta quinta rodada sem alterar nenhuma regra de dano.

**Composições testadas:**
- **Padrão corrigido** — 3 Mestres de Gu, só **1** com especial de Alma (`M d12`, ignora RD); os outros 2 com especial física (`M d10` melee, RD normal, mesmas 2 ações e mesma ficha do molde).
- **Difícil corrigido** — 4 Mestres de Gu, só **2** com especial de Alma; os outros 2 com a mesma especial física.

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Padrão** (3 Mestres, 100% Alma) — antes | 68,5% | 77,1% | 84,7% | 95,9% |
| **Padrão corrigido** (1 de 3 com Alma) — depois | **74,6%** | **80,8%** | **88,9%** | **99,0%** |
| **Difícil** (4 Mestres, 100% Alma) — antes | 13,0% | 9,8% | 10,6% | 29,9% |
| **Difícil corrigido** (2 de 4 com Alma) — depois | **14,2%** | **10,6%** | **15,5%** | **45,6%** |

**Padrão: resolvido.** A vitória do grupo volta pra uma faixa alta e segura (75–99%) em todo rank — não precisa cravar de volta nos ~98% de antes do achado, e fica coerente com a faixa-alvo (85–98%) na maior parte dos ranks; só os ranks 1–2 ficam ligeiramente abaixo de 85% (74,6% e 80,8%), o que ainda é uma melhora clara sobre os 68,3–77,1% quebrados.

**Difícil: melhora, mas NÃO resolve.** A vitória sobe em todo rank, mas fica muito abaixo da faixa-alvo (50–75%) e continua **bem mais letal que a maioria dos Chefes** (56–80%, ver [[⚔️ Ameaças Genéricas por Rank#O Chefe — a regra especial pra combate solo|a tabela de Chefes]]) nos ranks 1–3 — só o rank 5 chega perto (45,6%, ainda abaixo de 50%).

#### Por que a correção não basta pra "Difícil" — achado novo

Antes de aceitar 2-de-4 como número final, testei a proporção Alma/física inteira (0, 1, 2, 3 e 4 de 4 Mestres com a especial de Alma) e uma composição alternativa que reduz o total de ações (3 Mestres + 1 Guerreiro, 7 ações/rodada em vez de 8):

| Difícil, rank 1 / 2 / 3 / 5 | 0-de-4 | 1-de-4 | **2-de-4** | 4-de-4 (original) |
|---|---|---|---|---|
| Vitória do grupo | 8,0% · 5,3% · 5,9% · 28,8% | 11,3% · 8,0% · 9,3% · 36,7% | **14,2% · 10,6% · 15,5% · 45,6%** | 13,0% · 9,8% · 10,6% · 29,9% |

**Zero Mestres usando dano de Alma (100% especial física) ainda é catastrófico** — 8,0–28,8% conforme o rank, quase idêntico ao "Difícil" original 100% Alma. Isso prova que o dano de Alma **não é mais a causa dominante** da letalidade de "Difícil": é o **volume de 8 ações/rodada** (4 Mestres × 2 ações cada), que ficou pesado demais depois das decisões 103–133 (crítico dobra dano, essência sem regeneração em combate, Grau de Densidade corrigido) — um efeito que existe **independente** de qual Caminho a especial usa. A variante "3 Mestres (1 Alma) + 1 Guerreiro" (7 ações/rodada) melhora — 41,7% · 40,4% · 52,4% · 85,0% — mas ainda fica abaixo de Chefe nos ranks 1–2 e só empata/ultrapassa no rank 3 e no rank 5 (onde passa a faixa-alvo pro lado difícil demais).

**2-de-4 foi a melhor composição testada dentro do escopo original** (limitar a proporção de Alma, mantendo 4 Mestres) — mas o achado acima era novo e distinto do diagnóstico da decisão 135, e o autor decidiu resolvê-lo numa segunda rodada de calibração, abaixo.

#### 🩹 Segunda correção — o penhasco de volume de ações, e a composição final *(mesmo dia)*

Com o dano de Alma descartado como causa dominante, testei o eixo real — **número de ações inimigas por rodada**, de 5 a 8, script `_Processo/simulacoes/2026-08-30-dificil-rank-escalado.py`:

| Ações/rodada (composição) | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| 5 (2 Mestres + 1 Guerreiro) | 95,2% | 98,1% | não testado | não testado |
| 6 (3 Mestres — Padrão) | 74,6% | 80,8% | 88,9% | 99,0% |
| 7 (3 Mestres, 1 Alma + 1 Guerreiro) | 41,7% | 40,4% | 52,4% | 85,0% |
| 8 (4 Mestres, 2-de-4 Alma) | 14,2% | 10,6% | 15,5% | 45,6% |

**Não é uma rampa, é um penhasco.** Entre 6 e 8 ações a vitória do grupo despenca de ~90% pra ~13% — cada ação a mais custa 30-40 pontos percentuais, não uma fração proporcional. Nenhuma composição fixa cobre os 4 ranks dentro da faixa-alvo (50-75%, "mais difícil que Padrão, não pior que a maioria dos Chefes"): 7 ações funciona no rank 3 (52%) mas fica abaixo da faixa nos ranks 1-2 (~41%) e acima dela no rank 5 (85%); 8 ações só funciona (aproximadamente) no rank 5 (46%).

**Resolução escolhida pelo autor:** "Difícil" escala por faixa de rank, pelo mesmo princípio que já rege o Chefe (nenhum número de ação é constante entre ranks) — **ranks 1-4: 3 Mestres (1 com Alma) + 1 Guerreiro** (42% · 40% · 52% nos ranks 1/2/3); **rank 5+: 4 Mestres (2 com Alma)** (46%). Aplicado em [[⚔️ Ameaças Genéricas por Rank]]. Alternativas descartadas: uma composição sem tabela fixa (o mestre mira o contador de ações ponderadas ao vivo) e aceitar "Difícil" como quase-Clímax nos ranks 1-3 — ambas cogitadas, o autor preferiu manter a tabela com números fixos por serem mais rápidas de usar na mesa.

---

## 🏁 Sexta rodada — validação completa pós-decisão 133 *(2026-08-31)*

Validação final do dia: todas as mudanças de regra desde a quinta rodada (decisões 103 a 145) testadas juntas, nos 4 personagens da mesa, em **todos os ranks jogáveis (1-5)** com as composições de cena **atuais** de [[⚔️ Ameaças Genéricas por Rank]] (pós-correção das decisões 135-137), mais quatro peças que **nenhuma rodada anterior tinha modelado**: **Golpe Matador Coletivo**, **cura** (com taxa de acionamento medida pela primeira vez), **condições de controle** (Lentidão, implementada mecanicamente pela primeira vez) e **terreno** (contra a composição atual, não a antiga). Script: [[simulacoes/2026-08-31-validacao-completa.py|_Processo/simulacoes/2026-08-31-validacao-completa.py]], que estende o motor de [[simulacoes/2026-08-30-motor-v2-pos-decisao-133.py]] e [[simulacoes/2026-08-30-dificil-rank-escalado.py]] sem reescrever o que já estava certo. **3.000 iterações por cenário, limite de 20 rodadas, semente `20260830`** — mesmo padrão das rodadas anteriores.

### Tabela completa — ranks 1 a 5, todos os tipos de cena

| Cena | rank 1 | rank 2 | rank 3 | rank 4 *(inédito)* | rank 5 |
|---|---|---|---|---|---|
| **Fácil** — Horda de 8 | 100% · 4,00 | 100% · 4,00 | 100% · 3,99 | 100% · 3,99 | 100% · 3,99 |
| **Padrão** — 3 Mestres, máx. 1 com Alma | 71,3% · 2,02 | 78,0% · 2,00 | 88,7% · 2,12 | **95,0% · 2,37** | 98,8% · 2,75 |
| **Padrão pesado** — 2 Mestres (Alma) + Horda 8 | 77,4% · 2,25 | 73,5% · 2,09 | 75,1% · 2,05 | **76,6% · 2,05** | 91,7% · 2,76 |
| **Difícil** — ranks 1-4: 3M(1 Alma)+1G · rank 5+: 4M(2 Alma) | 37,0% · 0,96 | 35,6% · 0,84 | 49,1% · 0,96 | **62,9% · 1,22** | 45,5% · 0,80 |
| **Clímax** — Chefe + Guerreiro especial | 3,2% · 0,07 | 56,2% · 1,50 | 85,8% · 2,07 | **69,0% · 1,45** | 87,5% · 2,06 |

*(vitória do grupo · sobreviventes médios de 4)*

**Rank 4, medido pela primeira vez em qualquer rodada, não quebra nenhum padrão.** Padrão e Padrão pesado seguem a curva esperada (sobem suavemente com o rank). Difícil sobe para 62,9% dentro da mesma composição de rank 1-4 (3 Mestres + 1 Guerreiro) — consistente com o padrão já visto entre rank 1 (37%) e rank 3 (49%): a mesma composição fica relativamente mais fácil conforme o rank sobe dentro da faixa em que ela não muda — e cai de novo para 45,5% no rank 5 porque **a composição muda ali** (vira 4 Mestres, 2 com Alma, 8 ações em vez de 7). O salto não é um bug: é o "penhasco de composição" que a decisão 137 já descreveu, agora visível também na borda 4→5, não só na 3→4 antiga.

**Clímax no rank 4 (69,0%) fica abaixo do rank 3 (85,8%) e do rank 5 (87,5%)** — mesmo formato de "vale" que a nota de Ameaças já registra para o Chefe (a dificuldade dele é regida por quantos Golpes Matadores o grupo paga naquele rank, não por ele mesmo: `CHEFE_ACOES` dá 2 ações no rank 3 mas 3 no rank 4-5, e o rank 4 ainda não tem a folga de essência do rank 5). Consistente com o texto já publicado ("nunca é uma escala limpa"); não é achado novo, é o rank que faltava confirmar o padrão.

### Comparação com a quinta rodada, nos cenários que se sobrepõem

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Padrão** — 5ª rodada (corrigida) | 74,6% | 80,8% | 88,9% | 99,0% |
| **Padrão** — 6ª rodada (motor completo) | 71,3% | 78,0% | 88,7% | 98,8% |
| **Difícil** — publicado em [[⚔️ Ameaças Genéricas por Rank]] (decisão 137) | 42% | 40% | 52% | 46% |
| **Difícil** — 6ª rodada (motor completo) | 37,0% | 35,6% | 49,1% | 45,5% |
| **Clímax** — 5ª rodada | 3,5% | 56,6% | 85,9% | 87,4% |
| **Clímax** — 6ª rodada (motor completo) | 3,2% | 56,2% | 85,8% | 87,5% |

**A composição corrigida de "Difícil" continua valendo — a diferença de 3-5 pontos percentuais tem causa identificada, não é ruído nem regressão.** Clímax bate quase exatamente com a quinta rodada (diferenças de 0,1-0,4pp, dentro do ruído de Monte Carlo) porque o Chefe não usa Ação Especial e só há um Guerreiro aplicando Lentidão uma vez. Padrão e Difícil caem de forma pequena, mas **consistente e nova**: esta é a primeira rodada em que a Lentidão das Ações Especiais realmente custa a ação do alvo — as rodadas anteriores (motor v2 e a correção de composição) descreviam a Lentidão na ficha dos moldes, mas nunca a implementavam mecanicamente. Isso está confirmado pela seção de Controle abaixo (mesmo efeito, mesma direção, mesma ordem de grandeza). **Nada aqui indica que a tabela de composição da decisão 137 precisa mudar** — o efeito é pequeno o bastante para caber dentro da margem "não precisa cravar o número exato" que a própria decisão já usava.

### 🤝 Golpe Matador Coletivo vs. Chefe

Cenário dedicado: Clímax (Chefe + Guerreiro especial), comparando três aberturas — **nenhum Golpe Matador**, **solo** (só o Xie Lang, como nas rodadas 5-6 anteriores) e **coletivo** (os 4 PJs, [[⚡ Golpes Matadores#🤝 Golpe Matador Coletivo]], peça nova desta rodada).

| Rank | Nenhum golpe | Solo (Xie Lang) | **Coletivo (4 PJs)** |
|---|---|---|---|
| 1 | 2,9% | 3,2% | 2,8% |
| 2 | 54,5% | 54,4% | **2,5%** |
| 3 | 86,2% | 86,8% | **49,8%** |
| 4 | 73,0% | 70,6% | **30,2%** |
| 5 | 87,5% | 86,7% | **50,0%** |

> [!warning] Achado a sinalizar — Golpe Matador Coletivo é uma jogada de risco altíssimo pra esta mesa, se usado de abertura
> **Disparar o coletivo automaticamente no início de todo Clímax é PIOR do que não usá-lo, em todo rank a partir do 2.** A causa é matemática, não é bug de script: a CD de conjuração de um coletivo de 4 é **22** (a linha "5 Gu, coletivo" da tabela em [[⚡ Golpes Matadores]]), e mesmo aplicando o modificador **−2** de "rodada inteira de preparação sem ser incomodado" (que se aplica aqui, porque o combo é lançado antes de qualquer troca de golpe na cena), a CD efetiva fica em **20** contra um teste de `d20 + AST`. O maior AST da mesa é **+2** (Xie Lang) — ou seja, **só um 18, 19 ou 20 natural passa: 15% de chance.** Nos outros 85%, o grupo perde a rodada inteira de ação de todo mundo, o núcleo (Xie Lang) fica sem o próprio Gu de ataque pelo resto da cena, e os 4 tomam um corte de 15% no teto de Vitalidade (Retaliação de golpe híbrido, distribuída a todos os participantes por regra explícita da nota). Numa cena que já era enforcável (rank 2, 54%), isso derruba a vitória do grupo pra **2,5%**.
>
> **Isto não é um efeito pequeno nem um capricho do motor — é a mesma lição que a decisão 71 já registrou pro Golpe Matador solo ("disparar contra o alvo errado perde a luta"), elevada ao quadrado**: o coletivo tem CD mais alta que qualquer combo solo pagável nesta mesa mortal (nenhum dos 4 PJs tem nível de domínio de Marcas de Dao pra somar ao teste — isso só existe a partir do rank 6), então ele nunca deveria ser a abertura padrão de um Clímax nesta faixa de rank. **Sugestão para o autor, sem aplicar sozinho:** ou (a) documentar explicitamente que o coletivo é jogada de **desespero tardio** (só depois que a cena já está perdida e não há mais nada a proteger), nunca abertura, ou (b) revisar a CD do coletivo pra fase mortal — por exemplo, um desconto quando os 4 participantes já lutaram juntos antes (o equivalente coletivo do −4 "golpe já registrado com sucesso"), já que atualmente nada na regra dá a um grupo mortal um caminho realista pra essa CD ficar alcançável antes da Ascensão.

### ❤️ Cura — taxa de acionamento e a lacuna na ficha

Confirmado: o motor usa `roll_pool(pc["M"], 8)` — **`M d8`, batendo com a decisão 14.** O bug de `M d10` que a Folha de Referência tinha foi corrigido pela decisão 102 e não reapareceu aqui.

| Cenário | Disparos / Oportunidades | Taxa de acionamento |
|---|---|---|
| rank 1, Difícil | 5.880 / 7.294 | **80,6%** |
| rank 3, Difícil | 8.676 / 8.721 | **99,5%** |
| rank 3, Clímax | 9.999 / 10.027 | **99,7%** |
| rank 5, Difícil | 8.276 / 8.313 | **99,6%** |

**A cura dispara quase toda vez que é preciso, exceto no rank 1** (80,6%) — onde a Essência baixa (`aptidão × 4`, sem multiplicar por `M`) faz o Lee ficar sem tanque pra curar antes do fim da cena. Do rank 3 em diante a taxa satura perto de 100%: sempre que alguém cai abaixo de 40%, o Lee cura.

> [!warning] Achado a sinalizar — nenhum PJ tem Gu de cura registrado na ficha oficial
> Conferido em [[🎲 A Mesa — Personagens dos Jogadores]]: **nenhum dos 4 personagens lista um Gu de cura na ficha.** O papel de curandeiro do Lee, usado nesta e em todas as rodadas anteriores, é uma escolha de **modelagem**, justificável (Lee tem acesso ao Gu do Broto Restaurador — Madeira, dentro do arsenal de Cinco Elementos que a ficha dele já reivindica, ver [[☯️ Os Cinco Caminhos Wu Xing]]) mas **mais generosa que o Gu real**: o Broto Restaurador cura `M d6` (não `M d8`), **uma vez por cena** (não toda vez que alguém cai abaixo de 40%), só a distância de toque, e não repara dano de Metal ou fogo. Com a taxa de acionamento medida em ~80-99,7% por combate, o grupo está sobrevivendo em boa parte com uma cura que ainda não existe por escrito. **Recomendação para o autor:** ou registrar oficialmente o Broto Restaurador (ou outro Gu de cura) na ficha do Lee, ou aceitar que os números de vitória acima têm uma folga não lastreada em ficha — não é um bug de implementação, é uma lacuna de registro que a simulação expôs.

### 🌀 Condições de controle (Lentidão) — implementada pela primeira vez

Lentidão modelada como "o alvo perde a ação da rodada seguinte" (simplificação documentada no script — a leitura literal de outros Gu do Catálogo é "metade do deslocamento", mas o modelo não tem posição). Aplicada pela Ação Especial de Guerreiro/Elite e pela especial de Alma do Mestre de Gu, com o Chefe ignorando a primeira condição de controle da cena (regra já escrita em [[⚔️ Ameaças Genéricas por Rank]]).

| Cena | Com controle | Sem controle | Δ na vitória do grupo |
|---|---|---|---|
| rank 1, Difícil | 36,9% | 39,7% | +2,8pp |
| rank 3, Difícil | 47,5% | 52,5% | +5,0pp |
| rank 3, Clímax | 86,6% | 85,3% | −1,3pp |
| rank 5, Difícil | 44,9% | 48,4% | +3,5pp |

**Efeito pequeno mas real e consistente em "Difícil" (2,8 a 5,0 pontos percentuais a favor de desligar o controle), e ruído em "Clímax"** — porque só há um Guerreiro aplicando Lentidão uma vez ali, contra 3-4 Mestres de Gu com especial em "Difícil". É o mesmo efeito que explica a diferença de 3-5pp entre esta rodada e a quinta na tabela de comparação acima: **agora que a Lentidão custa a ação de verdade, ela pesa exatamente onde a nota de Ameaças já dizia que "Ação Especial vale mais que tirar Vitalidade"** — só que até esta rodada isso nunca tinha sido medido, só afirmado.

### 🌍 Terreno — a composição atual muda a leitura da decisão 75

Testado no Lee, rank 3, na composição **atual** de "Difícil" (3 Mestres [1 com Alma] + 1 Guerreiro) — a composição antiga usada no teste de terreno das rodadas 3-4 (1 Elite + 2 Guerreiros + 2 Recrutas) não existe mais na tabela de Ameaças.

| Terreno | Vitória do grupo | Sobreviventes |
|---|---|---|
| **Hostil** (−1 Nível, decisão 98) | 38,7% | 0,73 |
| **Neutro** | 49,3% | 0,95 |
| **Favorável** (+1 Nível) | 58,7% | 1,17 |

> [!warning] Achado a sinalizar — o terreno agora vale ~20 pontos percentuais, não 4
> A decisão 75 fechou o dial de terreno como "não é alavanca de dificuldade do mestre", medindo **4 pontos percentuais** de ponta a ponta (92,2% a 95,9%) contra o "Difícil" antigo (1 Elite + 2 Guerreiros + 2 Recrutas, ±2 Níveis na época). Com o "Difícil" **atual** (3 Mestres + 1 Guerreiro, resultado ~50% em vez de ~95%) e o dial já reduzido pela decisão 98 (±1 Nível, não mais ±2), o mesmo terreno vale **20 pontos percentuais** (38,7% a 58,7%). **A regra do terreno não ficou mais forte — a cena em que ela é testada ficou muito mais equilibrada**, e a mesma alavanca pesa muito mais numa moeda de 50/50 do que numa cena já decidida a 95%. Isto não invalida a decisão 75 (ela dizia respeito a uma dificuldade que não existe mais), mas **reabre a pergunta que ela fechou**: numa cena "Difícil" de verdade, o terreno de fato decide o resultado sozinho pro personagem elemental — o autor deve decidir se isso é o dial funcionando como pretendido (recompensar preparação e leitura de terreno) ou se precisa de outro olhar agora que "Difícil" não é mais um passeio.

### 🌟 Rank 6 — Imortal Denso Duplo-Gênio, revalidado com o motor completo

Mesmo cenário da quinta rodada (decisão 133), rerodado com Lentidão mecanicamente implementada e a cura já presente:

| Cenário | Vitória do grupo | Sobreviventes | *(5ª rodada, referência)* |
|---|---|---|---|
| **Duplo-gênio** (B=+3) | **5,4%** | 0,09/4 | 5,2% |
| Controle — Pequeno Feito real (B=+1) | **18,3%** | 0,33/4 | 20,0% |

**Confirma a quinta rodada, sem mudança de leitura.** A pequena queda no controle (20,0% → 18,3%) é o mesmo efeito da Lentidão agora sendo real, não um novo achado sobre o gênio pobre duplo. O aviso já registrado em [[⚔️ Ameaças Genéricas por Rank]] ("este perfil é sentença, não encontro") continua de pé.

### 🎲 Fratura da Abertura — reconfirmação rápida

| rank · cena | Com Fratura | Sem Fratura | Δ |
|---|---|---|---|
| 3 · Difícil | 47,8% | 49,8% | +2,0pp |
| 3 · Clímax | 85,7% | 86,7% | +1,0pp |

Mesma ordem de grandeza da quinta rodada (0,1 a 1,2pp então; 1,0 a 2,0pp agora, ainda pequeno frente às composições novas). **Nenhuma razão nova para mexer no gatilho de 25%.**

### Achados de desbalanceamento a sinalizar — não corrigidos nesta rodada

1. **"Padrão pesado" nunca recebeu a correção de limite de Alma que "Padrão" e "Difícil" já têm**, e cai bem abaixo do que a nota ainda documenta (97%/94%/93%/96%, marcado ✝ "não retestado"): medido aqui em **77,4% / 73,5% / 75,1% / 76,6% / 91,7%** (ranks 1-5) com o motor completo — os mesmos 2 Mestres, ambos com especial de Alma, sofrendo o mesmo alfa-strike que motivou a correção das decisões 135-137. **Sugestão, sem aplicar sozinho:** aplicar a mesma correção (1 dos 2 Mestres com especial de outro Caminho) e remedir.
2. **Golpe Matador Coletivo é matematicamente inviável como abertura pra esta mesa antes do rank 6** (ver caixa de aviso acima) — CD 22 (20 com o modificador de preparação) contra um teste de no máximo `d20+2`. Sinalizado para decisão do autor: documentar como jogada de desespero, ou revisar a CD pra fase mortal.
3. **O terreno dos Cinco Elementos, medido contra a composição atual de "Difícil", vale ~20pp — não os 4pp que fecharam a decisão 75.** Não é regressão nem bug: é a mesma regra, numa cena que ficou de fato equilibrada. Reabre a pergunta pro autor, não resolve sozinha.
4. **Nenhum PJ tem Gu de cura na ficha oficial**, apesar de a cura modelada disparar em 80-99,7% dos combates simulados. Ver a caixa de aviso da seção de Cura acima.

### 🕐 Duração de cena contra o alvo declarado de F&M *(2026-08-31, `2026-08-31-duracao-de-cena-vs-fm.py`)*

O bestiário/framework de criação de inimigo de *Feiticeiros e Maldições* declara por escrito o próprio alvo de design: **"o cálculo de vida foi feito para uma criatura aguentar 3 rodadas inteiras contra jogadores."** Instrumentando o motor da sexta rodada só para contar rodadas até a resolução (vitória ou derrota do grupo, 2.000 iterações):

| Cena | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Padrão** | 7,59 | 7,98 | 6,72 |
| **Padrão pesado** | 8,28 | 11,61 | 11,49 |
| **Difícil** | 8,56 | 9,65 | 9,65 |
| **Clímax** | 6,99 | 9,92 | 8,68 |

**7 a 12 rodadas, contra o alvo de 3 de F&M — um fator de 2 a 4×.** Isto não muda os acertos-pra-matar de um atacante contra um alvo (2,8-5 golpes, decisão 158, que já confere com F&M) — é um eixo diferente: a duração da cena inteira, com vários combatentes de cada lado. Sem ajuste aplicado; registrado como pendência nomeada no [[🧭 Log de Decisões|Log]] (decisão 160) — é decisão de mesa (ritmo pretendido vs. valer a pena encurtar), não correção mecânica.

### Metodologia e simplificações desta rodada

Documentadas por completo no cabeçalho do script. Resumo do que muda em relação à quinta rodada: **Lentidão** vira "perde a ação seguinte" em vez de descrição sem efeito; **Golpe Matador Coletivo** usa Xie Lang como núcleo e os outros 3 como apoio, com o modificador de conjuração −2 aplicado (a preparação é de fato "sem ser incomodado", já que dispara antes de qualquer troca de golpe); a Retaliação de falha do coletivo desliga o Gu de ataque só do **núcleo** (não dos 4) — uma correção feita **durante** esta própria rodada, documentada abaixo. **Terreno** só afeta o Lee, via o `B` (Grau por dado), sem modelar o desconto/sobretaxa de custo de essência por terreno (mesma simplificação das rodadas 3-4). **Cura** mantém a heurística "Lee cura quem estiver <40%", instrumentada com contadores de disparo/oportunidade.

> [!info] Bug de modelagem encontrado e corrigido nesta própria rodada, antes de fechar os números
> A primeira versão do script aplicava a Retaliação de falha do Golpe Matador Coletivo **desligando o Gu de ataque dos 4 participantes** (não só do núcleo), o que — combinado com cada PJ deste modelo só ter UM Gu de ataque "de assinatura" — deixava o grupo inteiro reduzido a dano cru pelo resto da cena após uma falha (~85-95% das vezes). Isso derrubava a vitória do grupo pra 0,3-3,8% em **todo** rank, um número claramente artificial (o próprio texto da regra fala em desligar "os Gu do combo", e os apoios de um Golpe Matador de verdade são Gu baratos e diferentes do Gu principal de cada um — não o mesmo Gu que o modelo usa pra tudo). Corrigido antes de reportar: só o núcleo perde o próprio ataque; os apoios sofrem só o corte de Vitalidade da Retaliação. Os números acima já são os corrigidos.

---

## 🔁 Sétima rodada — cura real remedida *(2026-08-31)*

Pendência fechada: a decisão 155 tinha registrado oficialmente o **Gu do Broto Restaurador** na ficha do Lee (Cinco Elementos, Madeira) e deixado marcado em "Em aberto" que as simulações precisavam ser **remedidas** com o valor real do Gu (`M d6`, uma vez por cena) em vez da heurística usada nas rodadas 1-6 (`M d8`, sem limite de usos, sempre que alguém caísse abaixo de 40% de Vitalidade). Esta rodada faz exatamente isso: **copia** [[simulacoes/2026-08-31-validacao-completa.py|_Processo/simulacoes/2026-08-31-validacao-completa.py]] em [[simulacoes/2026-08-31-cura-real-remedicao.py|_Processo/simulacoes/2026-08-31-cura-real-remedicao.py]] e troca só a peça de cura: `roll_pool(pc["M"], 8)` → `roll_pool(pc["M"], 6)`, mais um contador `cura_usada` na ficha do Lee (reinicia sozinho a cada combate, porque cada iteração de `simulate()` já cria fichas novas do zero) que bloqueia qualquer segunda cura na mesma cena. Alcance de toque não é modelado — o motor não tem posição, mesma simplificação já usada para Terreno. Todo o resto do motor (dano, Golpe Matador, Fratura, controle, terreno, composições de cena) é idêntico à sexta rodada. Mesma bateria: ranks 1-5, 5 tipos de cena, **3.000 iterações, semente `20260830`**.

### Tabela completa — sétima rodada (cura real)

| Cena | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 3,99 | 100% · 3,98 | 100% · 3,99 |
| **Padrão** | 67,5% · 1,79 | 79,3% · 1,87 | 88,5% · 2,01 | 95,4% · 2,33 | 99,2% · 2,70 |
| **Padrão pesado** | 74,2% · 1,98 | 71,1% · 1,73 | 72,5% · 1,61 | 76,3% · 1,70 | 90,9% · 2,32 |
| **Difícil** | 34,4% · 0,84 | 38,0% · 0,78 | 51,3% · 0,92 | 67,2% · 1,24 | 48,1% · 0,80 |
| **Clímax** | 3,4% · 0,08 | 55,4% · 1,33 | 84,5% · 1,91 | 74,9% · 1,52 | 89,2% · 2,03 |

*(vitória do grupo · sobreviventes médios de 4)*

### Comparação lado a lado — sexta rodada (cura heurística) vs. sétima (cura real)

| Cena · rank | 6ª rodada (M d8, sem limite) | 7ª rodada (M d6, 1×/cena) | Δ (7ª − 6ª) |
|---|---|---|---|
| Padrão · 1 | 71,3% | 67,5% | −3,8pp |
| Padrão · 2 | 78,0% | 79,3% | +1,3pp |
| Padrão · 3 | 88,7% | 88,5% | −0,2pp |
| Padrão · 4 | 95,0% | 95,4% | +0,4pp |
| Padrão · 5 | 98,8% | 99,2% | +0,4pp |
| Padrão pesado · 1 | 77,4% | 74,2% | −3,2pp |
| Padrão pesado · 2 | 73,5% | 71,1% | −2,4pp |
| Padrão pesado · 3 | 75,1% | 72,5% | −2,6pp |
| Padrão pesado · 4 | 76,6% | 76,3% | −0,3pp |
| Padrão pesado · 5 | 91,7% | 90,9% | −0,8pp |
| Difícil · 1 | 37,0% | 34,4% | −2,6pp |
| Difícil · 2 | 35,6% | 38,0% | +2,4pp |
| Difícil · 3 | 49,1% | 51,3% | +2,2pp |
| Difícil · 4 | 62,9% | 67,2% | +4,3pp |
| Difícil · 5 | 45,5% | 48,1% | +2,6pp |
| Clímax · 1 | 3,2% | 3,4% | +0,2pp |
| Clímax · 2 | 56,2% | 55,4% | −0,8pp |
| Clímax · 3 | 85,8% | 84,5% | −1,3pp |
| Clímax · 4 | 69,0% | 74,9% | **+5,9pp** |
| Clímax · 5 | 87,5% | 89,2% | +1,7pp |

**Nenhum delta cruza uma fronteira de leitura.** A maior variação é de +5,9pp (Clímax rank 4) e a maioria fica entre 0,2 e 4,3pp — a mesma ordem de grandeza que a própria decisão 154 já chamou de "pequena" ao aceitar sem correção (2-9pp na comparação "Padrão pesado" antes/depois). Nenhuma cena muda de categoria: nada que já era "ganhável" (>50%) virou "perda na maioria das vezes" (<50%) nem o oposto — Difícil rank 1 (37,0%→34,4%) e rank 5 (45,5%→48,1%) continuam do mesmo lado da linha de 50%, só que agora mais perto dela nos dois sentidos.

**O sinal misto (algumas cenas melhoram, outras pioram, sem padrão direcional) é o resultado esperado, não um artefato.** Uma cura mais fraca deveria, em tese, só piorar a vitória do grupo — mas o motor consome números aleatórios em ordem diferente a cada vez que a lógica de cura muda (a decisão de curar ou não, e quantos d6/d8 rolar, desloca todas as rolagens seguintes na mesma semente). Com a mesma semente `20260830`, isso descorrelaciona os dois fluxos de números aleatórios entre os dois scripts — cada cena efetivamente roda uma amostra de Monte Carlo *diferente*, não a mesma amostra com uma variável trocada. Os deltas aqui são, portanto, uma mistura de "efeito real da cura mais fraca" com "ruído de reamostragem", e não dá pra separar os dois sem uma técnica de números aleatórios pareados (fora do escopo desta remedição). Na prática isso não muda a leitura: mesmo somando os dois efeitos, nenhum delta se aproxima de mudar a categoria de nenhuma cena.

**Taxa de acionamento da cura, sob o Gu real:**

| Cenário | Disparos / Oportunidades | Taxa | *(6ª rodada, heurística)* |
|---|---|---|---|
| rank 1, Difícil | 2.734 / 6.594 | 41,5% | 80,6% |
| rank 3, Difícil | 2.889 / 7.543 | 38,3% | 99,5% |
| rank 3, Clímax | 2.930 / 8.312 | 35,3% | 99,7% |
| rank 5, Difícil | 2.893 / 7.272 | 39,8% | 99,6% |

A taxa cai pela metade ou mais em todo cenário — esperado, já que "disparos" agora satura em no máximo 1 por combate (3.000 no total possível) contra "oportunidades" que continuam contando toda vez que alguém está abaixo de 40%, cena inteira afora. **Isto confirma o achado da sexta rodada por outro ângulo**: o grupo passava a maior parte de cada combate abaixo de 40% de Vitalidade em algum PJ, e a heurística cobria quase toda essa janela; o Gu real cobre uma fatia bem menor dela, mas — como a tabela de vitória acima mostra — isso **não** derruba a taxa de vitória do grupo de forma proporcional. Os PJs sobrevivem majoritariamente com a Vitalidade que já tinham e com o dano que causam, não com a cura — a cura era um colchão de segurança em cenas já limítrofes, não a diferença entre ganhar e perder na maioria delas.

> [!important] Nenhuma tabela de composição precisa mudar — isto é confirmação, não correção
> Diferente do "Padrão pesado" da decisão 154 (onde a correção mudou o resultado por dezenas de pontos percentuais em alguns ranks, exigindo nova tabela publicada), aqui a mudança de cura fica dentro do ruído já tolerado no vault. **Não há fork de design a resolver** — não existe um cenário onde "manter a heurística" e "usar a cura real" levem a leituras de mesa diferentes (nenhuma composição vira "impossível" nem "trivial" sob a cura real). Por isso esta rodada **não** mexe em nenhuma tabela de [[⚔️ Ameaças Genéricas por Rank]]: é tratada como o mesmo tipo de correção mecânica de baixo impacto que a decisão 154 já aplicou para "Padrão pesado", registrada no Log e fechada.

### 🌟 Rank 6 e demais peças — confirmação rápida

Rodadas junto com a bateria principal (mesmo script), para registro — nenhuma delas depende do healer de forma relevante além do que já está capturado acima:

| Peça | 6ª rodada | 7ª rodada | Leitura |
|---|---|---|---|
| Rank 6 Duplo-gênio (B=+3) | 5,4% | 6,5% | Ruído — cenário não usa o Lee como curandeiro de forma decisiva (poucos turnos, cena curta) |
| Rank 6 Pequeno Feito (B=+1) | 18,3% | 19,8% | Ruído |
| Golpe Coletivo · Clímax rank 3 | 49,8% | 54,4% | Ruído de reamostragem (mesma ressalva acima) |
| Terreno · Difícil rank 3, neutro | 49,3% | 50,7% | Ruído |

Nenhuma leitura qualitativa das seções de Golpe Matador Coletivo, Controle, Terreno ou Fratura da Abertura muda sob a cura real — os achados e recomendações já registrados na sexta rodada continuam valendo como estão.

---

## 🏰 Oitava rodada — bateria de grupo nos ranks imortais *(2026-08-31)*

Fecha a última lacuna de cobertura da simulação: os ranks 1-5 têm bateria completa de grupo (rodadas 5-7), mas nos ranks imortais só existiam o cenário-Chefe do duplo-gênio (rank 6, decisão 133) e um duelo 1v1 (rank 8, decisão 164) — **nunca uma bateria grupo × cena**. Esta rodada roda os 4 PJs contra as 5 composições de [[⚔️ Ameaças Genéricas por Rank]] nos ranks **6, 7, 8 e 9**, em dois perfis de densidade de Marca por rank. Script: [[simulacoes/2026-08-31-oitava-rodada-ranks-imortais.py|_Processo/simulacoes/2026-08-31-oitava-rodada-ranks-imortais.py]] (cópia do motor da sétima rodada com o `make_pc(imortal=True)` generalizado — nada do motor reescrito). 3.000 iterações por célula, semente `20260830`, MAX_ROUNDS 20 (timeout conta como derrota; taxa medida em separado).

### Premissas (resumo — a versão completa está no cabeçalho do script)

- **Nível de domínio por rank × perfil**, tirado da escada e dos tetos de [[☯️ Marcas de Dao]] (decisões 194/195):

| Rank | **Recém-chegado** | **Denso** (veterano do rank) |
|---|---|---|
| 6 | Vislumbre (B+0) — entra com 800-900 Marcas | Pequeno Feito (B+1) — o teto de 9.999 do rank 6 não passa disso (decisão 194; Mestre no rank 6 só via gênio pobre, que é exceção) |
| 7 | Mestre (B+2) — especialista recém-convertido cruza os 10.000 | Grão-Mestre (B+3) — teto 99.999 |
| 8 | Grão-Mestre (B+3) — chega com ~100.000 num Caminho | Quase-Supremo (B+4) — teto 299.999; **nenhum rank 8 é Grande Mestre Supremo** (decisão 195) |
| 9 | Grande Mestre Supremo (B+5, **pool 2×M**) — o GMS nasce no rompimento pra Venerável (decisão 195), então **todo** rank 9 já é GMS | idem — a escada satura; os dois perfis coincidem por regra, e as diferenças medidas entre as duas linhas são ruído de reamostragem |

- **PJs especialistas** no Caminho de assinatura (a norma canônica); dado de ataque com o upgrade imortal da sexta rodada (+2 passos, teto d12). O pool 2×M do GMS segue a Escada de [[⚔️ Combate]] (bônus `M×B` **não** dobra — mesmo modelo da decisão 164).
- **Inimigos com o mesmo B do grupo** (recém enfrenta recém, denso enfrenta denso) — é a instrução da própria nota de Ameaças ("declare rank + nível de domínio"); o molde Elite B+0 bate com o exemplo publicado "Imortal Recém-Ascendido" (VIT 672). No rank 9, inimigos também GMS (B+5, pool 2×M).
- **Essência imortal**: mantida a simplificação documentada da sexta rodada (fator do estágio Pico mortal por analogia) — o Log não tem fórmula de pool de essência imortal, só o grau econômico (Uva Verde → Damasco).
- **Golpe Matador**: `golpe_mode="solo"`, o padrão da bateria (o coletivo é desespero tardio, decisão 161).

### Tabela — perfil Recém-chegado *(vitória do grupo · sobreviventes médios de 4)*

| Cena | rank 6 · Vislumbre (B+0) | rank 7 · Mestre (B+2) | rank 8 · Grão-Mestre (B+3) | rank 9 · GMS (B+5, 2×M) |
|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 4,00 | 100% · 3,98 |
| **Padrão** | 100% · 3,48 | 100% · 3,38 | 100% · 3,47 | 100% · 3,45 |
| **Padrão pesado** | 100% · 3,72 | 99,9% · 3,61 | 100% · 3,66 | 99,2% · 3,27 |
| **Difícil** | 96,3% · 2,57 | 97,9% · 2,52 | 99,2% · 2,70 | 94,0% · 2,43 |
| **Clímax** | 77,1% · 1,64 | 97,1% · 2,52 | 99,9% · 2,96 | 100% · 3,35 |

### Tabela — perfil Denso *(vitória do grupo · sobreviventes médios de 4)*

| Cena | rank 6 · P. Feito (B+1) | rank 7 · Grão-Mestre (B+3) | rank 8 · Quase-Supremo (B+4) | rank 9 · GMS (B+5, 2×M) |
|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 4,00 | 100% · 3,98 |
| **Padrão** | 100% · 3,33 | 100% · 3,34 | 100% · 3,43 | 100% · 3,46 |
| **Padrão pesado** | 99,9% · 3,56 | 99,9% · 3,49 | 99,9% · 3,54 | 99,5% · 3,29 |
| **Difícil** | 94,5% · 2,33 | 97,5% · 2,40 | 98,7% · 2,62 | 93,1% · 2,41 |
| **Clímax** | 85,0% · 1,87 | 98,1% · 2,63 | 99,9% · 3,04 | 100% · 3,33 |

### 🔴 Achado principal — a escada de dificuldade mortal COLAPSA nos ranks imortais

Na fase mortal a escada entrega gradação de verdade (sétima rodada: Difícil 34-67%, Clímax 3-89%). Nos ranks imortais, **toda cena vira ≥93% de vitória, nos dois perfis** — a única exceção é o Clímax de rank 6 (77,1% recém / 85,0% denso), e mesmo ele está acima de qualquer Clímax mortal. "Difícil" e "Clímax" imortais jogam como o "Padrão" mortal; a gradação sobrevive só como **atrito de recursos** (sobreviventes médios ainda ordenam as cenas: 4,0 → ~3,4 → ~2,5) — não como risco real de derrota.

Pior: **a dificuldade INVERTE com o rank** — Clímax vai de 77% (rank 6) pra 97% (7), 99,9% (8) e 100% (9). Quanto mais alto o rank, mais trivial a cena.

**Diagnóstico — são duas assimetrias estruturais entre PJ e molde de inimigo**, medidas em isolamento (perfil recém-chegado; não é proposta de regra, é instrumentação):

| rank · cena | moldes atuais | inimigo com dado imortal (+2 passos) | inimigo com acerto 2/rank | as duas juntas |
|---|---|---|---|---|
| 6 · Difícil | 96,9% | 83,8% | 49,3% | 13,1% |
| 6 · Clímax | 75,2% | 44,1% | 8,9% | 1,1% |
| 8 · Difícil | 99,1% | 95,3% | 11,2% | 3,2% |
| 8 · Clímax | 99,7% | 98,6% | 48,8% | 25,5% |

1. **Acerto do inimigo escala +1/rank; a Defesa de PJ escala +2/rank** (decisão 10). Na fase mortal a diferença acumulada é pequena; no rank 9 o inimigo físico só acerta com ~25-35% enquanto o PJ acerta ~100%. É a assimetria dominante — sozinha, devolve Difícil/Clímax pra faixa mortal (e no rank 8 já passa do ponto, 11-49%).
2. **Os PJs imortais ganham upgrade de dado (+2 passos, teto d12); os moldes ficam no d8/d10 mortal** — um Mestre de Gu inimigo de rank 9 ainda ataca com d8. Efeito secundário (5-31pp), mas real.

O ataque de **Alma é a exceção que confirma**: a Defesa de Alma escala +1/rank (igual ao acerto do inimigo), então a especial de Alma continua acertando a mesma fração em todo rank — é o único dano inimigo que não derrete, e é por isso que "Padrão pesado" (2 especiais de Alma) ainda arranha no rank 9 (99,2-99,5%, as únicas células não-100% fora de Difícil/Clímax).

### O dial que funciona nos ranks imortais é o ΔB, não a composição

Recém-chegado e denso produzem números **quase idênticos** — quando os dois lados sobem de densidade juntos, o B cancela. O que muda tudo é o **diferencial** de nível de domínio, e a âncora desta rodada (o duplo-gênio da decisão 133, rerodado no mesmo binário: **6,2%** com ΔB+3; **19,5%** com ΔB+1; 7ª rodada: 6,5%/19,8%) mostra a escada real: **ΔB 0 → 77-100% · ΔB+1 → ~20% · ΔB+3 → ~6%**. O aviso já publicado em [[⚔️ Ameaças Genéricas por Rank]] ("o duplo-gênio é sentença, não encontro") é o caso particular; o geral é: **nos ranks imortais, dificuldade se dosa por densidade de Marca do inimigo, não por quantidade de inimigo**.

### O que NÃO quebrou

- **Sem estagnação no rank 9**: timeout ≤0,1% em todas as 40 células, mesmo com pools de 512 dados (crítico: 1.024) — o piso de RD cresce com M mas os pools crescem com M × dado, então nenhuma composição congela. A preocupação da premissa 6 (travamento por RD/pool gigante) **não se materializou**.
- **Fácil continua fazendo o serviço de cena de abertura** (100%, 4/4 de pé) — igual à fase mortal.
- **A âncora confere com a sétima rodada** (deltas de 0,3pp) — o motor é o mesmo; os números novos vêm das premissas imortais, não de regressão.

> [!warning] Nenhuma tabela foi corrigida — isto é achado pra decisão do autor, não correção mecânica
> As composições de [[⚔️ Ameaças Genéricas por Rank]] foram escritas e calibradas pra fase mortal, e esta rodada mostra que elas **não transferem** pros ranks 6-9 como estão. Consertar exige escolher entre caminhos com cara de regra nova (escalar o acerto/dado dos moldes imortais? uma tabela de composição própria pra rank 6+? declarar que cena imortal se dosa por ΔB e documentar isso na nota?) — registrado como pendência nomeada em "Em aberto" no [[🧭 Log de Decisões]] (decisão 202), junto com o diagnóstico acima.

---

## 🥷 Nona rodada — batalhas solo *(2026-08-31)*

Pedido direto do autor: toda bateria até aqui mede **a mesa de 4** — as rodadas 1-4 tinham duelos PJ×PJ, mas **nunca um PJ sozinho contra um molde de inimigo**. Esta rodada roda cada um dos quatro, sozinho, contra três cenas: **Mestre de Gu solo** (especial de Alma, o teto da variante), **Horda de 8** (a cena "Fácil" do grupo) e o **Rei de Cem Feras** de [[🐺 Reis Fera e a Maré]] (Elite + escolta de Horda de 8). Script: [[simulacoes/2026-08-31-nona-rodada-batalhas-solo.py|_Processo/simulacoes/2026-08-31-nona-rodada-batalhas-solo.py]] — cópia do motor da sétima rodada, nada reescrito. Ranks 1, 3 e 5 × 4 PJs × 3 cenas = 36 células, 3.000 iterações cada, semente `20260830`, MAX_ROUNDS 20 (timeout conta como derrota; ficou ≤2,1% em toda célula — sem estagnação).

> [!warning] Números históricos — esta rodada é PRÉ-piso, e foi remedida
> As células de Horda de 8 e de Rei de Cem abaixo foram medidas **antes** do piso de ataques da decisão 207 — o piso que o achado 3 desta mesma rodada motivou. Com o piso ativo a leitura muda de natureza: a Horda de 8 solo deixa de ser guerra de atrito de 10-19 rodadas e vira **execução em ~5** (vitória 0-37% conforme o perfil), e o Rei de Cem solo cai de "melhor caso 8,4%" para **0,0-0,1%**. Ver [[#🧭 Décima quarta rodada — a bateria estendida (2026-08-31)|a décima quarta rodada]]. As tabelas abaixo ficam como história.

**Duas regras mudam de comportamento em jogo solo, e foram medidas COMO ESTÃO ESCRITAS:** (a) a Horda ataca **uma vez por personagem de pé** — solo, isso vira 1 ataque/rodada, um quarto do volume que o grupo recebe (ver o achado 3); (b) a cura do Lee ("o aliado mais machucado abaixo de 40%") — solo, o único candidato é ele mesmo: o Lee se cura, 1×/cena, com o Gu real da decisão 155; os outros três não têm cura nenhuma. Golpe Matador não dispara (o gatilho do motor é "há um Chefe na cena", como em todas as baterias — nenhuma das três cenas tem Chefe).

### Tabelas *(vitória · rodadas médias nas vitórias · % de Vitalidade restante nas vitórias)*

**Mestre de Gu solo** (especial de Alma):

| PJ | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang** (caster de Alma) | 73,7% · 4,0r · 51% | 84,0% · 4,1r · 47% | **94,3%** · 3,9r · 54% |
| **Jiaotang** (melee-tank) | 71,5% · 4,2r · 44% | 50,6% · 5,2r · 30% | 58,7% · 5,6r · 30% |
| **Lee** (curandeiro) | **9,9%** · 6,4r · 31% | 10,1% · 6,8r · 26% | 24,9% · 6,9r · 27% |
| **Demvi** (striker frágil) | 19,0% · 4,8r · 39% | 33,6% · 5,8r · 30% | 59,0% · 5,8r · 34% |

**Horda de 8** (a cena "Fácil" do grupo — 100% pra mesa de 4 em todo rank):

| PJ | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang** | 69,6% · 9,7r · 40% | 56,6% · 13,0r · 20% | 57,5% · 14,5r · 21% |
| **Jiaotang** | **99,1%** · 5,8r · 59% | 51,6% · 12,6r · 17% | **34,3%** · 15,7r · 15% |
| **Lee** | 71,6% · 10,2r · 29% | **10,2%** · 17,3r · 10% | 12,3% · 19,0r · 12% |
| **Demvi** | 15,2% · 12,1r · 26% | 30,3% · 14,5r · 17% | 39,2% · 16,1r · 19% |

**Rei de Cem Feras** (Elite + Horda de 8 — o grupo mede ~99% a ~55-60% de custo):

| PJ | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang** | 3,7% | 3,0% | 6,0% |
| **Jiaotang** | **8,4%** | 0,1% | 0,1% |
| **Lee** | 0,0% | 0,0% | 0,0% |
| **Demvi** | 0,0% | 0,0% | 0,1% |

*(Nas células do Rei com <10 vitórias em 3.000, rodadas e Vitalidade restante são ruído — omitidas. Nas vitórias que existem, o PJ termina a 3-33% de Vitalidade e a cena roda 9-19 rodadas.)*

### 1. Rei de Cem solo é sentença — esperado, agora quantificado

O grupo leva o Rei de Cem em ~99% pagando ~55-60% da Vitalidade; **sozinho, o melhor caso da mesa inteira é 8,4%** (Jiaotang no rank 1, antes de os moldes ganharem grau de estágio), e nos ranks 3-5 **nenhum PJ passa de 6%** — três dos quatro ficam em 0,0-0,1%. Não é achado de quebra: é o comportamento que [[🐺 Reis Fera e a Maré]] promete ("cena Difícil de verdade" **pra mesa de 4**) se comportando como deve quando a mesa não está lá. Nenhum ajuste pedido.

### 2. Quem sobrevive sozinho — e a dupla esperada troca de lugar com o rank

- **Xie Lang é o único PJ com perfil solo de verdade**: 74-94% contra o Mestre, 57-70% contra a Horda — nunca abaixo de 56% fora do Rei. São as mesmas duas vantagens já diagnosticadas na oitava rodada, operando dentro da fase mortal: o ataque de **Alma** mira a Defesa de Alma (que escala +1/rank contra o acerto dele a +2/rank) e a maior Aptidão da mesa (86) banca a cena longa sem cair no dado cru.
- **Lee colapsa em tudo** (9,9-24,9% contra o Mestre; 10-12% contra a Horda nos ranks 3-5): o kit dele é suporte — d8 de dano, e a cura real (`M d6`, 1×/cena) devolve ~meio golpe inimigo. Solo, o papel que ele exerce na mesa simplesmente não existe. É o retrato invertido do achado da sexta rodada ("a cura dispara em 80-99% dos combates do grupo"): o valor do Lee é sistêmico, não individual.
- **Jiaotang × Demvi invertem com o rank** — e não é o resultado que a intuição "tank aguenta, vidro quebra" prevê: Jiaotang **domina o rank 1** (99,1% contra a Horda, 71,5% contra o Mestre) e **decai** (34,3% e 58,7% no rank 5); Demvi faz o caminho oposto (15-19% no rank 1 → 39-59% no rank 5). O cruzamento é **economia de essência**, não ficha de combate: a Aptidão 56 do Demvi dá só ~5 ativações de Gu no rank 1 (aí ele cai no d4 cru e afunda), mas o pool de essência dobra por estágio enquanto o custo fica fixo — no rank 5 ele ativa a cena inteira. Já o Jiaotang bate na parede oposta: a Vitalidade da Horda cresce com o grau de estágio dos moldes (`6M+4M×B` por membro) mais rápido do que o dano físico dele, e sem essência sobrando pra compensar.

### 3. A regra da Horda escala PARA BAIXO solo — mas NÃO trivializa a cena, e isso é achado pro autor

A hipótese era: se a Horda ataca "uma vez por personagem de pé", um PJ sozinho leva 1/4 dos ataques e a cena viraria trivial. **Medido: não vira** — só o Jiaotang de rank 1 trivializa (99,1%); o resto da tabela fica entre 10% e 72%. O que segura a cena não é o dano por rodada, é a **parede de Vitalidade** (a Vit da Horda é por membro × 8 — idêntica pra quem chega em 4 ou sozinho) somada à economia de essência: solo contra a Horda, a cena vira **guerra de atrito de 10-19 rodadas** em que perde quem esvazia a Abertura primeiro.

O resultado líquido da regra como escrita, solo: **pressão por rodada baixa e constante, dificuldade errática entre perfis (99% a 10%) e cena comprida** — a Horda ameaça o PJ isolado mais por exaustão do que por perigo. Dois pontos pra decisão do autor (registrados em "Em aberto" no [[🧭 Log de Decisões]]):

1. Se a intenção é que 8 feras **assustem** um PJ isolado, a regra precisa de um piso (ex.: mínimo de 2-3 ataques/rodada contra 1-2 alvos); se a intenção é "horda é perigo de volume, e volume se dilui contra menos alvos", a regra atual entrega exatamente isso — é escolha de design, não bug.
2. As 13-19 rodadas médias das vitórias solo contra a Horda agravam o item já aberto da decisão 160 (cenas 2-4× mais longas que o alvo de F&M) — solo, o pior caso encosta no teto de 20 rodadas.

---

## 🔇 Décima rodada — Alma rara entre inimigos *(2026-08-31)*

Diretiva do autor, verbatim: *"os inimigos muito raramente terão poder de alma, a maior parte dos inimigos são normais ou de outros caminhos — refaça isso, provavelmente precisará refazer as simulações e rebalancear"*. Isso invalida o default do molde Mestre de Gu (especial de Alma de fábrica) e, com ele, toda a calibração das decisões 135/137/154 — os limites "máx. 1 de 3 com Alma" etc. só existiam **porque** Alma era o default. Script: [[simulacoes/2026-08-31-decima-rodada-alma-rara.py|_Processo/simulacoes/2026-08-31-decima-rodada-alma-rara.py]] — cópia do motor da sétima rodada, nada do motor reescrito; só a bateria muda. Ranks 1-5 × 5 cenas × **três mixes de especial**, 3.000 iterações/célula, semente `20260830`:

- **A — mix atual** (baseline): os limites publicados (Padrão 1 de 3 · Padrão pesado 1 de 2 · Difícil 1 de 3 nos ranks 1-4, 2 de 4 no rank 5). *Nota de fidelidade:* o script da sétima rodada ainda modelava Padrão pesado com os **dois** Mestres de Alma (comentário herdado da sexta, anterior à correção da decisão 154); o mix A segue a tabela publicada (1 de 2), então a linha de Padrão pesado difere um pouco da sétima — as demais linhas conferem com ela em ≤0,5pp.
- **B — Alma rara ao pé da letra**: ZERO especiais de Alma fora do Clímax (que, na composição da bateria, é Chefe + Guerreiro — sem Mestre nenhum, idêntico nos três mixes).
- **C — Alma rara com exceção rolada**: cada Mestre de Gu rola **1d6 na montagem da cena — em 6, é um cultivador de Alma de verdade** (o mesmo gesto de rolagem do loadout de bagagem do molde).

### As três tabelas *(vitória do grupo · sobreviventes médios de 4)*

**Mix A — atual (baseline):**

| Cena | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 3,99 | 100% · 3,98 | 100% · 3,99 |
| **Padrão** | 67,5% · 1,79 | 79,3% · 1,87 | 88,4% · 2,01 | 95,2% · 2,32 | 99,1% · 2,69 |
| **Padrão pesado** | 74,6% · 1,97 | 67,8% · 1,59 | 65,6% · 1,33 | 70,7% · 1,46 | 87,9% · 2,09 |
| **Difícil** | 34,7% · 0,85 | 37,4% · 0,77 | 51,2% · 0,92 | 66,8% · 1,24 | 48,6% · 0,80 |
| **Clímax** | 3,4% · 0,08 | 55,2% · 1,33 | 85,1% · 1,93 | 74,9% · 1,52 | 89,3% · 2,04 |

**Mix B — Alma rara (zero fora do Clímax):**

| Cena | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 3,99 | 100% · 3,98 | 100% · 3,99 |
| **Padrão** | 60,6% · 1,58 | 72,6% · 1,60 | 83,9% · 1,77 | 91,6% · 2,08 | 98,2% · 2,49 |
| **Padrão pesado** | 69,5% · 1,69 | 59,3% · 1,28 | 59,0% · 1,11 | 64,1% · 1,21 | 82,1% · 1,80 |
| **Difícil** | 28,4% · 0,69 | 29,1% · 0,57 | 40,8% · 0,68 | 56,5% · 0,97 | 31,9% · 0,48 |
| **Clímax** | 2,7% · 0,06 | 54,5% · 1,31 | 87,4% · 2,00 | 73,2% · 1,47 | 88,8% · 2,02 |

**Mix C — Alma rara com exceção rolada (1d6 = 6 por Mestre):**

| Cena | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| **Fácil** | 100% · 4,00 | 100% · 4,00 | 100% · 3,99 | 100% · 3,98 | 100% · 3,99 |
| **Padrão** | 62,3% · 1,65 | 76,7% · 1,75 | 84,5% · 1,87 | 93,7% · 2,21 | 98,8% · 2,61 |
| **Padrão pesado** | 71,2% · 1,78 | 64,3% · 1,42 | 63,3% · 1,25 | 66,7% · 1,30 | 84,7% · 1,92 |
| **Difícil** | 29,8% · 0,73 | 35,1% · 0,70 | 45,5% · 0,79 | 60,9% · 1,08 | 38,2% · 0,61 |
| **Clímax** | 3,2% · 0,07 | 53,5% · 1,28 | 85,6% · 1,93 | 74,3% · 1,48 | 90,3% · 2,06 |

*(Clímax é a mesma composição nos três mixes — as diferenças da linha são só ruído de reamostragem, a mesma ressalva de semente documentada na sétima rodada.)*

### 🔴 Achado principal — a direção INVERTE: Alma rara torna as cenas mais difíceis, não mais fáceis

A expectativa (a da própria diretiva: "provavelmente precisará rebalancear" *pra baixo*) era que remover o dano que ignora RD deixasse tudo mais fácil. **Medido: o contrário.** Mix B custa de 1 a 17pp de vitória do grupo em relação ao baseline (Padrão −1 a −7 · Padrão pesado −5 a −9 · Difícil −6 a −17); mix C, a metade disso (−0,3 a −10). O mecanismo, visível na estrutura do motor e coerente com todo o histórico:

1. **Uma especial de Alma isolada desperdiça o próprio dano.** O PJ cai quando **uma** das duas barras zera — e todo o resto do dano da cena bate na Vitalidade. O golpe de Alma (`M d12`, sem RD) abre ~35% de uma barra de Alma que **nada mais na cena vai tocar**: quase nunca completa um abate. Já a especial física (+4 no acerto, `M d10`) soma no mesmo foco de fogo que os ataques comuns — cada ponto dela conta.
2. **O +4 da especial física quase garante a Lentidão.** As duas especiais aplicam Lentidão 2, mas a física acerta mais — e "tirar a ação de um personagem vale mais que tirar Vitalidade dele" (a tese da própria nota de Ameaças, confirmada de novo aqui).
3. **Alma só é letal em pilha** — o alfa-strike de várias especiais na mesma barra, medido na quinta rodada (Difícil todo-Alma: 10-30%). Os limites das decisões 135/137 já tinham removido exatamente essa pilha; o que sobrava do default de Alma era a versão fraca. Corroboração interna: no mix A desta rodada, corrigir Padrão pesado de 2-Alma pra 1-Alma (decisão 154, aplicada agora ao script) **derrubou** a linha em 3-6pp em relação à sétima rodada — trocar Alma por física endurece a cena.

A promessa da ficção continua de pé onde ela importa: o dano de Alma segue sendo o único que **não derrete com o rank** (oitava rodada: é a única ameaça inimiga que ainda arranha no rank 9), e a pilha de Alma segue sendo a ferramenta de Clímax. O que muda é a frequência — e o preço medido dela.

### Recalibração — o que foi medido antes de propor

Faixas-alvo históricas: Fácil ≈ 100% · Padrão 75-99% · Difícil ~40-52% · Clímax 56-87%. Sob o mix C: Fácil ✓ em tudo; Padrão ✓ nos ranks 2-5, **rank 1 fora (62,3%)**; Difícil ✓ no rank 3 (45,5%), **ranks 1-2 fora (29,8%/35,1%)** e rank 5 na beirada (38,2%); Clímax inalterado. As compensações candidatas, medidas nas duas direções:

**Pra cima (a hipótese original — mais inimigos):** todas despencam no penhasco de ações da decisão 137, com ou sem Alma:

| Compensação (mix C) | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| Padrão + 1 Guerreiro (7 ações) | 28,7% | 32,0% | 45,7% | 61,4% | 82,8% |
| Difícil + 1 Guerreiro (8-9 ações) | 9,1% | 6,1% | 10,6% | 18,1% | 9,0% |
| Difícil com 4º Mestre no lugar do Guerreiro (8-10 ações) | 7,1% | 6,1% | 8,6% | 15,2% | 0,6% |

*(Consistência interna de graça: "Padrão + 1 Guerreiro" é literalmente a composição Difícil dos ranks 1-4 — 28,7% vs 29,8% na célula Difícil, 1,1pp de ruído de reamostragem.)*

**Pra baixo (aliviar as células que caíram):**

| Compensação (mix C) | Resultado | Veredito |
|---|---|---|
| Difícil ranks 1-4 com o Guerreiro **sem** Ação Especial | 31,4% · 35,3% · 48,5% · 64,5% | **Não move a agulha** (±2pp do baseline — dentro do ruído) |
| Difícil rank 5: 3 Mestres + 2 Guerreiros em vez de 4 Mestres | 40,5% | Cai na beirada da faixa, mas é **empate estatístico** com os 38,2% dos 4 Mestres (+2,3pp ≈ 1,8σ) |
| Padrão rank 1: 2 Mestres + 1 Guerreiro | **92,0%** (mix B) / 91,8% (mix C) | **Cai DENTRO da faixa 75-99** — mas salta por cima do buraco: nada existe entre 62% e 92% |

**A leitura consolidada:** o penhasco de ações governa tudo — cada Mestre a mais ou a menos move a célula em 25-30pp, então **as faixas-alvo de Padrão rank 1 e Difícil ranks 1-2 não têm composição alcançável com as peças existentes** (Difícil rank 1: as opções são 30% ou 62%, nada no meio; Padrão rank 1: 62% ou 92%). Isso não é um efeito novo do Alma rara — é o penhasco da decisão 137 exposto de novo, agora sem a maquiagem de 5-7pp que a especial de Alma "fraca" dava às células baixas.

### Por que o mix C foi o aplicado

O C é a leitura mais fiel da diretiva: "muito raramente" não é "nunca" — e o molde já usa exatamente esse gesto no loadout (`role 1d6 → em 5-6, ele sabe uma receita`), então "role 1d6 por Mestre → em 6, é um cultivador de Alma" adiciona **zero regra nova**, só mais uma linha na rolagem que o mestre já faz. O custo de calibração é nulo: B e C diferem em no máximo 6pp, sempre na mesma direção, e o C ainda preserva a surpresa ocasional do golpe que ignora RD — que é o que mantém a promessa do [[👻 Caminho da Alma]] visível na mesa fora do Clímax.

### O que mudou / o que fica pro autor

**Aplicado** (era ordem direta, não escolha): o molde Mestre de Gu de [[⚔️ Ameaças Genéricas por Rank]] muda o default da Ação Especial de Alma pra especial física do próprio Caminho, com o cultivador de Alma virando exceção rolada (1d6 = 6); a tabela de composição recebe os números do mix C e perde a linguagem de limite de Alma das decisões 135/137/154 (obsoleta — sem Alma como default, não há o que limitar); [[🎓 Guia do Mestre Iniciante]] (Parte 7) e [[🏰 Conversão Medieval]] atualizados na mesma linha. **Pro autor** ("Em aberto" no Log): as três células fora da faixa (Padrão r1 62% · Difícil r1-2 30/35%) e o menu medido acima — aceitar os números novos como a régua real de rank baixo, adotar Padrão escalado por rank (2M+1G no rank 1, 92%), ou reabrir o desenho da cena Difícil de rank baixo, que o penhasco de ações deixou sem alvo alcançável.

---

## ⏱️ Décima primeira rodada — encurtando a cena *(2026-08-31)*

Pendência da decisão 160, agora com veredito do autor: **encurtar de verdade, alvo ~4-6 rodadas** (o vault media 7-12 contra o alvo declarado de ~3 de *Feiticeiros e Maldições*), sabendo que é recalibração de motor. A pendência lista três alavancas — **RD menor · mais dano por Nível · menos inimigos por cena** — e o autor pediu o método que funcionou nos três mixes de Alma da décima rodada: **medir cada alavanca ISOLADA, mesma semente, antes de aplicar qualquer coisa**, com dois guarda-corpos obrigatórios (a curva de letalidade por Caminho da decisão 78 e o penhasco de ações da decisão 137).

Script: [[simulacoes/2026-08-31-decima-primeira-duracao.py|_Processo/simulacoes/2026-08-31-decima-primeira-duracao.py]] — cópia do motor da décima rodada com a contagem de rodadas de `2026-08-31-duracao-de-cena-vs-fm.py` e duas sincronizações com a tabela publicada depois da decisão 207 (Padrão de rank 1 = 2 Mestres + 1 Guerreiro; piso de ataques da Horda). 3.000 iterações/célula, semente `20260830`, mix de Alma C.

### Como cada alavanca foi parametrizada *(e por que)*

| Alavanca | Grau fraco | Grau forte |
|---|---|---|
| **L1 — RD menor** | `RD × 0,5` nos dois lados (o `1 × M` do molde vira `0,5 × M`) | `RD = 0` — nenhuma RD na cena |
| **L2 — mais dano por Nível** | **+1 Nível de Dano** em todo ataque dos dois lados | **+2 Níveis** |
| **L3 — menos inimigos** | uma peça a menos em cada composição *(grau único)* | — |

Duas escolhas de parametrização, declaradas: **(a)** o **piso de dano** (`nunca abaixo de M`) fica intacto nos dois graus de L1 — ele não é RD, é o chão que impede a anulação, e baixar RD só faz o piso deixar de ser atingido. **(b)** Em L2 **não** usei "B conta dobrado", que era a sugestão: no rank 1 o estágio é Inicial e `B = 0`, então dobrar B é rigorosamente nulo em um terço da bateria — justamente onde a cena mais dói. Usei a moeda que a decisão 79 já define e que funciona em todo rank: +1/+2 Níveis sobem o tipo do dado (d6→d8→d10→d12) e, já em d12, viram `+1 por dado`.

### Baseline — o estado atual, já com a decisão 207 dentro

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** | 100% · **2,51 rd** | 100% · **3,44 rd** | 100% · **4,08 rd** | 100% · **4,57 rd** |
| **Padrão** | 92,3% · 6,04 rd | 76,6% · 7,71 rd | 86,1% · 7,47 rd | 98,1% · 6,34 rd |
| **Padrão pesado** | **63,3%** · 7,58 rd | **57,2%** · 8,92 rd | **50,1%** · 9,68 rd | **75,5%** · 10,44 rd |
| **Difícil** | 30,8% · 8,29 rd | 31,9% · 8,83 rd | 45,8% · 8,91 rd | 37,7% · 8,77 rd |
| **Clímax** | 3,1% · 6,75 rd | 54,7% · 10,66 rd | 87,2% · 9,28 rd | 89,3% · 8,06 rd |

Dois achados já no baseline, antes de qualquer alavanca:

1. **A decisão 207 já comprou 1-2 rodadas de graça.** A medição que abriu a pendência (7,59-11,61) virou 6,04-10,66 sem nenhuma mudança de motor — só o Padrão aliviado no rank 1 e o piso de ataques da Horda. **"Fácil" já está dentro do alvo** (2,5-4,6 rodadas) e "Padrão" encosta nele.
2. 🔴 **A linha de "Padrão pesado" publicada ficou desatualizada pela própria decisão 207.** O piso de ataques da Horda endurece a cena que mais depende dela: os **71% · 64% · 63% · 85%** da tabela são medição pré-piso e valem hoje **63,3% · 57,2% · 50,1% · 75,5%** (−8 a −13pp). É correção mecânica de número medido, não escolha de design — corrigida em [[⚔️ Ameaças Genéricas por Rank]]. As outras quatro linhas conferem com o publicado dentro de ≤1,5pp.

### As três alavancas — RODADAS MÉDIAS *(alvo do autor: 4-6)*

| Cena / rank | BASE | L1a `RD×0,5` | L1b `RD=0` | L2a `+1 Nível` | L2b `+2 Níveis` | L3 `−1 peça` |
|---|---|---|---|---|---|---|
| Padrão r1 | 5,94 | 5,79 | 5,39 | 5,53 | **4,97** | **4,35** |
| Padrão r3 | 7,51 | 7,05 | 6,70 | 6,66 | 6,02 | **4,41** |
| Padrão r5 | 6,31 | 6,25 | **5,77** | **5,79** | **5,32** | **4,06** |
| Padrão pesado r1 | 7,56 | 7,21 | 6,79 | 6,36 | **5,55** | **4,81** |
| Padrão pesado r3 | 9,70 | 9,22 | 8,78 | 8,44 | 7,42 | 6,66 |
| Padrão pesado r5 | 10,42 | 10,31 | 9,95 | 9,44 | 8,46 | 6,78 |
| Difícil r1 | 8,29 | 7,55 | 6,84 | 6,71 | **5,69** | 7,67 |
| Difícil r3 | 8,92 | 8,21 | 7,76 | 7,59 | 6,63 | 7,51 |
| Difícil r5 | 8,81 | 8,15 | 7,76 | 7,56 | 6,78 | 6,32 |
| Clímax r1 | 6,75 | 6,35 | **5,90** | **5,80** | **5,10** | 7,59 |
| Clímax r3 | 9,29 | 8,01 | 7,13 | 8,03 | 7,17 | 6,99 |
| Clímax r5 | 8,01 | 7,14 | 6,23 | 7,01 | 6,28 | **5,91** |
| **média das 12 células** | **8,13** | 7,60 | 7,08 | 7,08 | **6,28** | **6,09** |
| **encurtamento** | — | −6,5% | −12,9% | −12,9% | **−22,7%** | **−25,1%** |
| **células dentro de 4-6** | 1 / 12 | 1 / 12 | 3 / 12 | 3 / 12 | **6 / 12** | **5 / 12** |

### As três alavancas — VITÓRIA DO GRUPO *(o que cada uma custa)*

| Cena / rank | BASE | L1a | L1b | L2a | L2b | L3 |
|---|---|---|---|---|---|---|
| Padrão r1 | 92,7% | 91,8% | 89,7% | 86,2% | 84,0% | **99,0%** |
| Padrão r3 | 85,6% | 82,8% | 82,4% | 80,3% | 75,8% | **100,0%** |
| Padrão r5 | 98,7% | 97,5% | 97,9% | 97,7% | 96,3% | **100,0%** |
| Padrão pesado r1 | 64,4% | 58,7% | **51,4%** | 53,0% | **47,3%** | **98,8%** |
| Padrão pesado r3 | 50,0% | 42,9% | **36,7%** | 45,5% | **39,5%** | **99,0%** |
| Padrão pesado r5 | 76,5% | 67,7% | **61,9%** | 68,8% | 65,0% | **99,9%** |
| Difícil r1 | 29,8% | 28,8% | 25,1% | 25,3% | 21,0% | **63,7%** |
| Difícil r3 | 46,0% | 43,3% | 43,1% | 40,2% | 35,6% | **84,3%** |
| Difícil r5 | 35,8% | 31,1% | 34,0% | 32,3% | 31,9% | **98,6%** |
| Clímax r1 | 3,2% | 5,9% | 8,5% | 5,4% | 5,3% | 10,6% |
| Clímax r3 | 86,1% | 91,1% | 94,8% | 85,4% | 86,5% | **99,6%** |
| Clímax r5 | 89,6% | 93,9% | 95,9% | 89,4% | 90,1% | **99,2%** |

**L1 e L2 tiram vitória do grupo, não dão.** É a mesma assimetria de sempre: os inimigos têm mais ações por rodada que os PJs, então qualquer coisa que acelere a troca de golpes acelera mais o lado que bate mais vezes. A exceção é o Clímax, onde o inimigo é **um** corpo — lá L1 devolve 3-9pp ao grupo, porque a `RD 2 × M` do Chefe era metade do problema.

### 🛡️ Guarda-corpo 1 — a curva de letalidade da decisão 78

Acertos pra derrubar um alvo de rank igual com CON padrão, medido direto (Vitalidade ÷ dano médio por acerto, com RD e piso já aplicados — não inferido). No **rank 1 sem RD** a medição reproduz a escada publicada com 3 casas, o que valida o método antes de julgar qualquer alavanca:

| Leitura | d6 | d8 | d10 | d12 | razão d6/d12 |
|---|---|---|---|---|---|
| **publicada (decisão 78)** | **5,14** | **4,00** | **3,27** | **2,77** | **1,86** |
| BASE — sem RD *(a definição)* | 5,16 | 4,01 | 3,27 | 2,76 | 1,87 ✅ |
| BASE — com RD `1 × M` *(a mesa de verdade)* | 6,78 | 4,98 | 3,90 | 3,25 | 2,09 |
| L1a — com RD `0,5 × M` | 5,87 | 4,44 | 3,57 | 2,98 | 1,97 |
| L1b — RD zero | 5,17 | 4,00 | 3,30 | 2,74 | 1,89 |
| **L2a — +1 Nível** *(sem RD)* | **4,02** | **3,26** | **2,78** | **2,41** | 1,67 |
| **L2b — +2 Níveis** *(sem RD)* | **3,29** | **2,77** | **2,40** | **2,12** | 1,55 |
| L3 — idêntico ao BASE | 5,16 | 4,01 | 3,27 | 2,76 | 1,87 ✅ |

Três leituras, e elas decidem a rodada:

- ✅ **L1 não toca a escada — ela a CONSERTA.** A definição da decisão 78 é sem RD, então baixar RD não muda um dígito dela; o que muda é a leitura prática de mesa, que hoje está *distorcida* pela RD (2,09 de razão contra os 1,86 declarados, com o d6 pagando 6,78 acertos em vez de 5,14). Meia RD leva a mesa a 1,97; RD zero, a 1,89. **A alavanca de RD aproxima o jogo real do número publicado.**
- 🔴 **L2 reescreve a escada inteira, nos dois graus.** Com +1 Nível, cada Caminho passa a matar como o Caminho **um degrau acima** matava (d6 vira 4,02 ≈ o d8 de hoje; d8 vira 3,26 ≈ o d10; d10 vira 2,78 ≈ o d12) — os quatro números publicados em [[⚔️ Combate]] e em [[❤️ Recursos e Dano]] ficam todos errados. Com +2 Níveis é pior: **d10 e d12 convergem** (2,40 vs 2,12, porque os dois já rolam d12 e só diferem no `+1 por dado`), e a razão d6/d12 cai de 1,86 pra 1,55 — o "um Caminho d6 leva quase o dobro de acertos que um d12" deixa de ser verdade. **Quatro perfis de letalidade viram uns três e meio.**
- ✅ **L3 não toca a escada** — é composição, não motor.

*(A escada não é perfeitamente estável entre ranks nem hoje: a Densidade da Essência soma `+4 × M × Grau` na Vitalidade e `+1 por dado` no dano, e as duas não crescem na mesma proporção — a razão d6/d12 cai de 1,87 no rank 1 pra 1,54 no rank 3 e 1,46 no rank 5. Isso é efeito da decisão 80, anterior a esta rodada, e não muda o veredito; fica registrado porque a decisão 78 afirma estabilidade "em todos os nove ranks" e a afirmação vale para o Grau 0, não para todos os Graus.)*

### ⛰️ Guarda-corpo 2 — o penhasco de ações da decisão 137

Swing de vitória ao somar **um Guerreiro** à composição publicada, em pontos percentuais. É o degrau sobre o qual a tabela de composição inteira repousa:

| Alavanca | Padrão r1 | Padrão r3 | Padrão r5 | Difícil r1 | Difícil r3 | Difícil r5 |
|---|---|---|---|---|---|---|
| **BASE** | 23,8 | 41,1 | 15,0 | 24,6 | 33,6 | 28,4 |
| L1a `RD×0,5` | 26,6 | 39,6 | 18,9 | 19,5 | 32,2 | 24,7 |
| L1b `RD=0` | **29,3** | 40,7 | 18,3 | 19,1 | 31,5 | 27,0 |
| L2a `+1 Nível` | **28,4** | 40,6 | **20,5** | 18,1 | 32,0 | 24,8 |
| L2b `+2 Níveis` | **31,6** | 39,7 | **21,3** | 16,0 | 27,5 | 23,8 |
| L3 `−1 peça` | 23,8 | 41,1 | 15,0 | 24,6 | 33,6 | 28,4 |

**L1 e L2 inclinam o penhasco de um lado e o achatam do outro** — Padrão fica mais íngreme (23,8 → 31,6 no rank 1, 15,0 → 21,3 no rank 5, sob L2b), Difícil fica mais raso (24,6 → 16,0). Não é uma melhora: é o penhasco **mudando de lugar**, o que obriga a recalibrar a tabela de composição inteira em vez de só encurtar a cena. Sob L2b uma cena Padrão de rank 1 está a 31,6pp de virar uma cena Difícil por causa de um Guerreiro a mais — a tabela fica **menos** perdoável ao erro do mestre, não mais.

**L3 é idêntico ao BASE por construção** (não mexe no motor) — mas isso é a armadilha, não o alívio: L3 **é** o penhasco. Aplicá-lo significa descer todas as cenas um degrau de 15 a 41pp de uma vez, e é exatamente o que a tabela de vitória acima mostra.

### 🔴 O veredito — nenhuma das três alavancas passa limpa

| Alavanca | Encurta? | Guarda-corpo 78 | Guarda-corpo 137 | Veredito |
|---|---|---|---|---|
| **L1a** `RD × 0,5` | −6,5% (8,13 → 7,60 rd). **Não chega perto de 4-6** | ✅ **melhora** a fidelidade (razão 2,09 → 1,97) | ⚠️ Padrão +3pp mais íngreme, Difícil −5pp | ❌ **Efeito pequeno demais.** Custa 6-9pp em Padrão pesado por 0,5 rodada |
| **L1b** `RD = 0` | −12,9% (→ 7,08 rd). 3/12 células no alvo | ✅ razão 1,89, praticamente a publicada | ⚠️ Padrão +5,5pp mais íngreme | ❌ **Deleta um subsistema.** Sem RD, "Alma ignora RD por completo" e "Espada/Relâmpago ignoram metade" viram frases sem efeito — a coluna "o que ganha" do perfil **d12** em [[⚔️ Combate]] deixa de existir, e com ela a resposta estrutural do jogo ao inimigo de rank superior. Armadura mortal (0/1/2/3/4) vira decoração. Custa 13-15pp em Padrão pesado |
| **L2a** `+1 Nível` | −12,9% (→ 7,08 rd). 3/12 no alvo | 🔴 **escada inteira sobe um degrau** — os 4 números publicados ficam errados | 🔴 Padrão +4,6 / +5,5pp mais íngreme | ❌ **Paga a escada de letalidade e não chega ao alvo** |
| **L2b** `+2 Níveis` | **−22,7%** (→ 6,28 rd). 6/12 no alvo — o melhor resultado de motor | 🔴 **d10 e d12 convergem**; razão 1,86 → 1,55; "quatro perfis" vira três e meio | 🔴 **o penhasco mais íngreme de todos** (Padrão r1: 31,6pp) | ❌ **O melhor encurtamento é também o que quebra os dois guarda-corpos ao mesmo tempo.** E ainda custa 4-17pp de vitória, com Padrão pesado despencando pra 39-47% |
| **L3** `−1 peça` | **−25,1%** (→ 6,09 rd), e **Padrão inteiro cai em 4,0-4,4 rd** | ✅ intocada | ✅ inalterado *(mas é literalmente descer o penhasco)* | ❌ **Apaga a escada de dificuldade.** Padrão 99-100%, Padrão pesado 98,8-99,9%, Difícil 63,7-98,6% — o jogo inteiro vira "Fácil". E nem resolve: Difícil r1/r3 continuam em 7,5-7,7 rd, e **Clímax r1 fica MAIS LONGO** (6,75 → 7,59) |

### O que a rodada descobriu além do menu — duração e dificuldade estão soldadas no mesmo botão

O padrão que atravessa as cinco medições: **a duração da cena não é governada pela dureza dos alvos, é governada pelo número de corpos.** Dobrar a letalidade por acerto (L2b move o dano médio em ~40-50%) compra só 22,7% de cena; tirar **um** corpo compra 25,1% sozinho. E corpos são ações — o próprio penhasco da decisão 137. As três alavancas da pendência não são três opções independentes: **duas empurram a dureza (a variável a que a duração é pouco sensível) e a terceira empurra os corpos (a variável que É a dificuldade).**

Duas hipóteses alternativas foram medidas e **rejeitadas** na mesma rodada, pra não deixar o diagnóstico só no argumento:

- **"A cena arrasta porque os PJs ficam sem Essência e caem no dano cru."** Instrumentado: só **0-21%** dos ataques de PJ se resolvem em dano cru, e nos ranks 3 e 5 é **0-6%** — a economia de Essência não é o freio. *(A intuição vinha da nona rodada, mas lá a cena era solo.)*
- **"A barra da Horda é o vilão da duração, e encolhê-la é quase de graça."** É a maior barra do jogo (`(6×M + 4×M×Grau) × membros`: 2.304 no rank 5, mais que o Chefe) e o volume de ataques dela **não** depende do número de membros — só o dado desce. Parecia a alavanca limpa. Medido, não é: Horda de 8 → 6 em Padrão pesado corta 0,5-1,8 rodada e **entrega 18-25pp de vitória ao grupo** (63,8→81,8 · 51,4→76,3 · 76,9→93,4), porque o dado cai de `M d8` pra `M d6` no mesmo passo. Mesmo botão de novo.

| Horda em Padrão pesado | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **8 membros** *(publicado)* | 63,8% · 7,55 rd | 54,6% · 8,79 rd | 51,4% · 9,70 rd | 76,9% · 10,55 rd |
| 6 membros | 81,8% · 7,02 rd | 80,2% · 8,13 rd | 76,3% · 8,89 rd | 93,4% · 8,79 rd |
| 5 membros | 83,8% · 6,63 rd | 81,7% · 7,61 rd | 80,3% · 8,26 rd | 95,2% · 8,07 rd |

### O que foi aplicado / o que volta pro autor

**Aplicado: nada de motor.** Nenhuma das três alavancas passou os dois guarda-corpos, e o autor pediu explicitamente que, nesse caso, a rodada volte com os números em vez de escolher no escuro. Única edição de regra: a linha de **Padrão pesado** da tabela de composição, corrigida para a medição pós-decisão 207 (é sincronização de número medido, não alavanca).

**Pro autor**, o menu medido, em ordem de custo:

1. **Aceitar 6-8 rodadas como o ritmo real** e mover o alvo, não o motor. A decisão 207 já entregou "Fácil" em 2,5-4,6 e "Padrão" em 6,0-7,7 de graça; o que passa de 8 rodadas é Padrão pesado, Difícil e Clímax — as cenas que a mesa joga **uma vez por sessão**, não quatro.
2. **L1a (`RD × 0,5`) por outro motivo que não a duração.** É a única alavanca que *melhora* um guarda-corpo: aproxima a letalidade de mesa dos números que a decisão 78 publica (razão 2,09 → 1,97). Compra 0,5 rodada de brinde. O preço é 6-9pp em Padrão pesado, dentro da ordem de grandeza que as decisões 154/163 já trataram como recalibração aceitável.
3. **L2b + recalibrar a tabela de composição e reescrever a escada de letalidade.** Chega em 6/12 células no alvo, e é o único caminho de motor que entrega encurtamento de verdade — mas exige reabrir a decisão 78 (a escada vira 3,3/2,8/2,4/2,1) e remedir as cinco composições, porque o penhasco fica mais íngreme no Padrão.
4. **Atacar o número de corpos com uma peça NOVA** — a única saída que a rodada não pôde medir porque não existe: um molde de inimigo com **muitas ações e pouca Vitalidade** (o inverso do Chefe). Isso desacopla os dois botões — mantém a pressão por rodada (dificuldade) cortando as rodadas necessárias pra limpar a mesa (duração). É a única hipótese estrutural que sobra depois desta rodada, e ela precisa de desenho do autor antes de simulação.

*(Medida e fechada pela [[#🗡️ Décima segunda rodada — a peça de muitas ações (2026-08-31)|décima segunda rodada]]: a peça existe agora, foi desenhada e medida, e **não desacopla**.)*

---

## 🗡️ Décima segunda rodada — a peça de muitas ações *(2026-08-31)*

Fecha a **opção 4** da pendência da decisão 208 — a única das quatro saídas que a rodada anterior não pôde medir, porque a peça não existia. O desenho veio do autor: um molde de **muitas ações e pouca Vitalidade**, o inverso do Chefe, com a teoria de que ele **desacopla os dois botões** (mantém a pressão por rodada, que é a dificuldade, cortando as rodadas necessárias pra limpar a mesa, que é a duração).

Script: [[simulacoes/2026-08-31-decima-segunda-peca-nova.py|_Processo/simulacoes/2026-08-31-decima-segunda-peca-nova.py]] — cópia do motor da décima primeira rodada com o motor de dano, as fichas dos PJs, os Golpes Matadores e os moldes existentes **intocados**. As únicas adições são o molde novo, um seletor de escolha de alvo (explicado adiante) e a instrumentação do guarda-corpo 3. 3.000 iterações/célula, semente `20260830`, ranks 1/3/5, mix de Alma C.

> [!warning] Enquadramento — encurtar deixou de ser obrigatório
> O autor já aceitou a **saída 1** da pendência (6-8 rodadas é o ritmo real do jogo). O Enxame entrou nesta rodada como *bônus*, não como resgate: o critério de aprovação passou a ser **manter as faixas de vitória publicadas E encurtar, sem piorar o penhasco e sem ser decorativo**. Um resultado neutro (não encurta, mas não quebra nada) seria aceitável.

### O candidato — molde "Enxame"

| Enxame | Valor | De onde veio o número |
|---|---|---|
| **Vitalidade** | `7 × M` *(mais o `4 × M × Grau` de estágio que todo molde leva)* | Um terço do Mestre de Gu, pouco mais da metade do Guerreiro — morre em 1-2 golpes concentrados |
| **Defesa** | `11 + rank` | Interpola Recruta (`10 + rank`) e Guerreiro (`12 + rank`) |
| **Acerto** | `d20 + rank + 6` | Igual ao do Guerreiro — a peça ameaça por volume, não por ficha |
| **RD** | nenhuma | O que compra a fragilidade |
| **Ações** | **2 por rodada** | O ponto do molde |
| **Dano** | `M d4` por ataque | Metade do Guerreiro, fraco por golpe de propósito |
| **Ação Especial** | nenhuma | Idem |
| **Por cena** | 2 a 4 | — |

Além dele, quatro variantes medidas na mesma bateria: **E9** e **E10** (Vitalidade `9 × M` e `10 × M`), **E7d6** (o mesmo corpo com o dado do Recruta, `M d6` — o `d4` não existe em nenhum outro lugar do vault e a escada por Caminho da decisão 78 começa no `d6`) e **E7pr** (bônus de estágio proporcional, explicado no achado colateral mais abaixo).

As três composições, todas por **substituição** nas cenas publicadas pós-decisão 207:

- **Padrão-E** = 2 Mestres + 2 Enxames *(6 ações, a mesma contagem do Padrão de 3 Mestres)*
- **Difícil-E** = 3 Mestres + 2 Enxames *(nos ranks 1-4 isto é exatamente a substituição pura: o Difícil vigente é 3 Mestres + 1 Guerreiro)*
- **Clímax-E** = Chefe + 2 Enxames *(a segunda substituição pura: o Clímax vigente é Chefe + 1 Guerreiro)*

### Fase 1 — vitória e duração *(motor histórico)*

| Cena / rank | BASE | **E7** | E9 | E10 | E7d6 | E7pr |
|---|---|---|---|---|---|---|
| Padrão-E r1 *(faixa 75-99%)* | 92,7% | **80,1%** ✅ | 77,2% ✅ | 77,1% ✅ | 58,7% ❌ | 80,1% ✅ |
| Padrão-E r3 | 85,6% | **84,3%** ✅ | 82,2% ✅ | 81,1% ✅ | 64,8% ❌ | 86,4% ✅ |
| Padrão-E r5 | 98,7% | **97,2%** ✅ | 97,4% ✅ | 97,1% ✅ | 91,7% ✅ | 98,2% ✅ |
| Difícil-E r1 *(faixa 40-52%)* | 29,8% | **12,8%** ❌ | 12,9% ❌ | 11,6% ❌ | 4,8% ❌ | 13,5% ❌ |
| Difícil-E r3 | 46,0% | **5,8%** ❌ | 4,8% ❌ | 4,6% ❌ | 1,8% ❌ | 7,2% ❌ |
| Difícil-E r5 | 35,8% | **23,8%** ❌ | 23,0% ❌ | 24,3% ❌ | 11,9% ❌ | 30,3% ❌ |
| Clímax-E r1 *(faixa 56-87%)* | 3,2% 🔴 | **1,2%** ❌ | 1,1% ❌ | 1,1% ❌ | 0,4% ❌ | 1,1% ❌ |
| Clímax-E r3 | 86,1% | **29,5%** ❌ | 28,6% ❌ | 27,1% ❌ | 13,4% ❌ | 32,9% ❌ |
| Clímax-E r5 | 89,6% | **40,0%** ❌ | 39,2% ❌ | 39,6% ❌ | 24,0% ❌ | 46,1% ❌ |

| Rodadas médias | BASE | E7 | E9 | E10 | E7d6 | E7pr |
|---|---|---|---|---|---|---|
| **média das 9 células** | **7,76** | 7,31 | 7,43 | 7,48 | 6,77 | 7,01 |
| **encurtamento** | — | **−5,8%** | −4,2% | −3,5% | −12,7% | −9,7% |
| **células dentro de 4-6** | 1/9 | 1/9 | 1/9 | 1/9 | 3/9 | 2/9 |

**Duas leituras imediatas.** (1) **Não encurta**: 5,8% é menos que a pior das três alavancas da rodada anterior (L1a, `RD × 0,5`, −6,5%), e nenhuma célula nova entra na faixa de 4-6 rodadas. (2) **Duas Enxames não substituem um Guerreiro** — Difícil desaba de 46,0% para 5,8% e Clímax de 86,1% para 29,5%. A aritmética explica: uma ação de Guerreiro a `M d8` contra a `RD 1 × M` de um PJ entrega ~22 de dano por rodada no rank 3; **uma** Enxame entrega ~28 (duas ações de `M d4` a ~14 líquidos cada) — a paridade de pressão declarada estava certa para **uma** peça, e a composição usou **duas**. Só que a decisão 137 já dizia qual é o contador que importa: **rolagens de ataque**, não dano. Trocar 1 Guerreiro por 2 Enxames troca **uma** rolagem por **quatro**.

Nas mãos das variantes: subir a Vitalidade (7 → 9 → 10) muda menos de 3pp em qualquer célula, e o `M d6` do E7d6 tira 17-25pp e derruba o Padrão da faixa. **A alavanca do molde não é nem a Vitalidade nem o dado — é a contagem de ações**, como sempre.

### 🛡️ Guarda-corpo 1 — a escada de letalidade da decisão 78

Intocada **por construção** (o Enxame é composição, não motor — mesma situação do L3 da rodada anterior). Verificada em vez de afirmada: no rank 1 sem RD a bateria devolve **d6 5,16 · d8 4,01 · d10 3,28 · d12 2,76**, razão d6/d12 **1,87** contra os 1,86 publicados. ✅

### ⚠️ Guarda-corpo 2 — o penhasco de ações da decisão 137

Swing de vitória ao somar **uma** peça, em pontos percentuais. A pergunta: o Enxame é um degrau mais suave que o Guerreiro?

| Composição / rank | swing de **+1 Guerreiro** | swing de **+1 Enxame** |
|---|---|---|
| Padrão r1 | 23,8 | **18,7** ✅ |
| Padrão r3 | 42,0 | **47,6** 🔴 |
| Padrão r5 | 15,4 | **20,6** 🔴 |
| Difícil r1 | 19,8 | **17,8** ✅ |
| Difícil r3 | 36,0 | **38,6** 🔴 |
| Difícil r5 | 30,3 | **34,2** 🔴 |
| **média** | **27,9** | **29,6** |

E o degrau **dentro** das composições novas (somar um terceiro Enxame a Padrão-E): 25,4 · 47,7 · 30,1 — média **34,4**, contra 27,1 do `+1 Guerreiro` sobre o Padrão publicado.

**O penhasco fica um pouco mais íngreme, não mais raso** — em 4 das 6 células, e na média. Não é o desastre que o L2b da rodada anterior foi (23,8 → 31,6 numa célula só), mas é o oposto do que a peça prometia: ela deveria ser o degrau intermediário que o penhasco nunca teve. ⚠️

### 🔴 Guarda-corpo 3 — "Recruta solto 2.0", e a armadilha que ele revelou

O guarda-corpo novo desta rodada. A própria [[⚔️ Ameaças Genéricas por Rank]] chama o Recruta solto de **decorativo** porque morre antes de agir; a peça nova não pode repetir isso. Instrumentado direto: **quantas ações cada Enxame executa antes de morrer**.

Medindo isso, apareceu um problema de método que muda o veredito. O motor de todas as rodadas anteriores faz o PJ atacar **quem tem a menor FRAÇÃO de Vitalidade** — ou seja, termina o ferido. Com a mesa inimiga inteira de pé no começo da cena, todos estão em 100%, o desempate é a ordem da lista, e **a peça frágil é atacada por último**. Mas a hipótese da opção 4 diz literalmente *"o grupo mata rápido, mas dói enquanto vive"* — e essa premissa **só existe se o grupo focar a peça frágil**. Julgar o Enxame só pelo motor histórico seria julgá-lo por um artefato.

Então a bateria roda os **dois modos**: `fração` (o motor histórico) e `absoluto` (o PJ ataca quem tem menos Vitalidade restante em valor absoluto — mata o Enxame primeiro). Piso de referência do "decorativo", medido na mesma bateria: **6 Recrutas soltos executam 1,28 · 2,20 · 2,97 ações** nos ranks 1/3/5, com 24% · 12% · 8% morrendo sem agir nenhuma vez.

| E7 · ações executadas por Enxame | alvo por **fração** | alvo **absoluto** |
|---|---|---|
| Padrão-E r1 | **10,78** *(0% com zero)* | **1,15** *(51,7% com zero)* |
| Padrão-E r3 | **12,23** *(0%)* | **1,99** *(27,8%)* |
| Padrão-E r5 | **10,74** *(0%)* | **2,33** *(22,4%)* |
| Difícil-E r1 | **12,72** *(0%)* | **1,25** *(49,9%)* |
| Difícil-E r3 | **12,37** *(0%)* | **2,10** *(26,2%)* |
| Difícil-E r5 | **14,82** *(0%)* | **2,37** *(21,5%)* |
| *referência: Mestre de Gu, cenas publicadas* | 5,57 a 10,14 | — |
| *referência: Guerreiro, cenas publicadas* | 5,33 a 8,67 | — |
| *piso do decorativo: 6 Recrutas soltos* | 1,28 a 2,97 | — |

**As duas colunas são as duas metades de uma contradição, e é isso que mata a hipótese:**

- **Se o grupo NÃO foca a peça frágil**, ela fica de pé **5,4 a 8,2 rodadas** e executa **10 a 16 ações** — mais que um Mestre de Gu e o dobro de um Guerreiro. Não é uma peça que sai rápido da mesa; é uma ameaça de primeira linha com um terço da Vitalidade. A cena não encurta porque nada é removido dela, e as faixas quebram porque as ações se acumulam.
- **Se o grupo FOCA a peça frágil** — que é exatamente a premissa que a opção 4 assume — ela executa **0,56 a 2,40 ações** e **20% a 73% morrem sem agir uma vez**, ou seja, **abaixo do Recruta solto que a nota já classifica como decorativo**. A cena continua sem encurtar (Difícil-E r1 8,12 rodadas contra 8,20 do baseline; Clímax-E r1 7,61 contra 7,61) porque a peça não estava governando a duração.

Não existe posição intermediária: **a peça é ameaça-de-verdade ou é decorativa, e quem decide qual não é o mestre — é a escolha de alvo do grupo.**

### 🔴 O achado que fecha o caso — a volatilidade tática

O corolário do parágrafo acima, quantificado. Diferença de vitória do grupo entre os dois modos de escolha de alvo, em pontos percentuais — quanto a dificuldade da cena depende de uma decisão tática:

| Família de composição | volatilidade média *(diferença absoluta de vitória entre os dois modos)* | pior célula |
|---|---|---|
| **Cenas publicadas** *(Padrão · Difícil · Clímax)* | **3,1 pp** | Difícil r3: 14,2 |
| Com **1** Enxame no lugar da peça trocada | 6,7 pp | Clímax r3: 17,8 |
| Com **2** Enxames *(as composições da rodada)* | **16,2 pp** | **Clímax-E r3: 59,3** |

Clímax-E de rank 3 mede **30,4%** se o grupo termina o ferido e **89,7%** se o grupo mata o frágil primeiro. É a mesma cena, os mesmos dados, a mesma semente. **Uma peça cuja dificuldade oscila 59 pontos com a tática do grupo não é dosável pelo mestre** — e a tabela de composição inteira do vault é uma promessa de dosagem. Isso é desqualificante por si só, independente de faixas e de duração.

### Fase 3 — a varredura de Vitalidade, onde ela realmente morde

A Fase 1 varreu 7/9/10 no modo `fração`, onde a Vitalidade do Enxame quase não importa (ele é atacado por último de qualquer jeito). Sob alvo `absoluto` ela é o que decide se a peça age ou é decorativa — então a varredura foi refeita ali, com uma quarta parada (`14 × M`, dois terços do Mestre de Gu):

| Vitalidade | ações/Enxame *(r1 · r3 · r5)* | Padrão-E *(faixa 75-99%)* | Difícil-E *(faixa 40-52%)* | rodadas Padrão-E |
|---|---|---|---|---|
| `7 × M` | 1,15 · 1,99 · 2,33 🔴 *decorativo* | 89,5% · 93,9% · 98,7% ✅ | 21,9% · 15,9% · 35,7% ❌ | 6,25 · 6,88 · 6,43 |
| `9 × M` | 1,51 · 2,46 · 2,37 🔴 | 84,6% · 90,2% · 99,2% | 17,6% · 9,1% · 33,8% ❌ | 6,64 · 7,44 · 6,47 |
| `10 × M` | 1,72 · 2,59 · 2,44 🔴 | 81,3% · 88,3% · 98,8% ✅ | 14,1% · 7,1% · 32,8% ❌ | 6,93 · 7,50 · 6,53 |
| `14 × M` | **2,49 · 3,19 · 3,35** ✅ | 68,3% ❌ · 78,0% · 94,9% | 5,9% · 3,4% · 13,9% ❌ | **7,85 · 8,25 · 7,51** |

**É a mesma solda de novo, agora dentro do próprio molde.** A única Vitalidade que tira o Enxame do território decorativo (`14 × M`, o único degrau que passa das ~3 ações do Recruta) é também a que derruba o Padrão da faixa e **alonga a cena em 1,1 a 1,6 rodada**. Vitalidade da peça nova é mais um botão com o mesmo sinal de todos os outros: mais corpo = mais ação = mais tempo = mais dificuldade. A decisão 208 tinha medido a solda entre composições; esta rodada mede a mesma solda **dentro dos parâmetros de uma única peça**.

### 🟡 Achado colateral que vale além desta rodada — o bônus de estágio dilui todo molde frágil

`+4 × M × Grau` de Vitalidade é **igual para todo molde**, do Recruta ao Chefe. Consequência: qualquer peça desenhada como "pouca Vitalidade" perde a identidade conforme o rank sobe.

| | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| Enxame `7 × M` como % da Vitalidade do **Guerreiro** | **58%** | 75% | **79%** |
| Enxame `7 × M` como % da Vitalidade do **Mestre de Gu** | **33%** | 52% | **58%** |

"Um terço do Mestre de Gu" só é verdade no rank 1. A variante **E7pr** (bônus de estágio proporcional, `4 × M × Grau × 7/21`) confirma que a diluição custa: encurta **9,7%** em vez dos 5,8% do E7, e devolve 2-6pp de vitória ao grupo nos ranks 3 e 5. **Não muda o veredito desta rodada** (a E7pr continua fora da faixa em Difícil e Clímax), mas fica registrado: qualquer molde futuro de pouca Vitalidade precisa de um bônus de estágio proporcional, ou vira um Guerreiro caro a partir do rank 3.

### 🔴 O veredito — a hipótese do desacoplamento não se sustenta

| Critério | Resultado |
|---|---|
| **Faixas de vitória** | Padrão-E dentro (80-97%) nas três variantes de Vitalidade; **Difícil-E (5,8-23,8%) e Clímax-E (1,2-40,0%) muito fora** ❌ |
| **Encurtamento** | **−5,8%** (7,76 → 7,31 rodadas), pior que a alavanca mais fraca da rodada anterior; 1/9 células em 4-6, igual ao baseline ❌ |
| **Guarda-corpo 78** | Intocado por construção, verificado (razão 1,87 vs 1,86 publicada) ✅ |
| **Guarda-corpo 137** | Penhasco **mais íngreme** em 4 de 6 células (média 29,6 contra 27,9 do Guerreiro) ⚠️ |
| **Guarda-corpo 3 (decorativo)** | **Falha no único modo em que a hipótese faz sentido**: sob foco de fogo, 0,56-2,40 ações por peça e 20-73% morrendo sem agir — abaixo do Recruta solto ❌ |
| **Volatilidade tática** *(critério novo)* | **16,2pp de média contra 3,1pp das cenas publicadas**, com pico de 59,3pp ❌ |

**A resposta à pergunta da rodada é não.** O Enxame não desacopla duração de dificuldade — ele anda **na mesma curva** das três alavancas da decisão 208, e de um jeito pior: as outras três pelo menos escolhiam um lado da curva de forma previsível. O Enxame escolhe o lado **em tempo de jogo**, pela tática do grupo, e por isso pode ser as duas coisas erradas ao mesmo tempo (decorativo *e* sem encurtar) ou a coisa errada de outro jeito (letal *e* sem encurtar).

A razão estrutural, agora medida por dentro: **a hipótese pede que a peça seja simultaneamente rápida de matar e duradoura o bastante para pressionar**, e isso é uma contradição, não um problema de calibragem. Não existe valor de Vitalidade que satisfaça as duas — a Fase 3 percorreu a faixa inteira de `7 × M` a `14 × M` e o trade-off é monotônico.

### Duas leituras positivas que sobraram, e por que nenhuma vira regra

1. **Padrão-E (2 Mestres + 2 Enxames) é a única composição do vault que fica na faixa nos três ranks sem exceção por rank** — 80,1% · 84,3% · 97,2%, contra o Padrão publicado que precisa da exceção de rank 1 da decisão 207. Mas ela **alonga** a cena (6,84 contra 6,59 de média) e é **17× mais volátil** taticamente (6,8pp contra 0,4pp). Trocar uma exceção documentada por volatilidade não documentada é um mau negócio.
2. **Clímax com UM Enxame no lugar do Guerreiro (Chefe + 1 Enxame)** põe os ranks 3 e 5 dentro da faixa — **80,5% e 83,9%**, contra os 88,1% e 89,4% do Chefe + Guerreiro, que estão *acima* do teto de 87% — e corta 0,4-0,6 rodada. É o resultado mais limpo da rodada inteira. Mas o rank 1 continua em 4,3% (o 🔴 histórico do Clímax de rank 1, que a peça não resolve) e a volatilidade tática da célula é de 10,6 a 17,8pp. **Fica registrado como candidato para uma rodada futura, não aplicado aqui.**

**Aplicado: nada.** O molde não entra em [[⚔️ Ameaças Genéricas por Rank]], nenhuma composição muda, nenhum número publicado é tocado. A opção 4 da pendência da decisão 208 fecha como **medida e rejeitada**, deixando as saídas 1-3 — com a saída 1 (aceitar 6-8 rodadas) já escolhida pelo autor antes desta rodada.

---

## ✅ Décima terceira rodada — validação final conjunta *(2026-08-31)*

O lote de decisões **146-210** entrou hoje em duas sessões paralelas. Várias peças foram medidas **isoladas** e nunca juntas, e uma delas — o **Colapso Espiritual** (decisão 205) — mudou uma regra que o motor continuava modelando do jeito ANTIGO. Esta rodada faz para as decisões 146-210 o que a sexta rodada fez para as 103-133: liga tudo ao mesmo tempo e confere **cada número publicado**, célula a célula.

Script: [[simulacoes/2026-08-31-decima-terceira-validacao-final.py|_Processo/simulacoes/2026-08-31-decima-terceira-validacao-final.py]] — cópia do motor da décima primeira rodada (Alma rara da decisão 206, piso de ataques da Horda e Padrão escalado da decisão 207, contagem de rodadas), com a correção do Colapso, o suporte imortal portado da oitava rodada e a instrumentação de desgaste portada da calibração da Varredura. **3.000 iterações/célula, semente `20260830`, mix de Alma C.**

### 🔧 A correção que abriu a rodada — Colapso Espiritual (decisão 205)

O motor tinha `pc_alive(pc) = vit > 0 and alma > 0` e contava o resultado como **baixa**: Alma zerada matava o personagem na hora, para sempre. A regra desde a decisão 205 é outra — Alma 0 é **inconsciência + Teste de Morte espiritual**, a primeira queda **nunca mata**, três degraus dão coma espiritual (ainda não é morte), e a morte real só vem numa **segunda** queda com a sequela aberta, o que por definição não cabe numa cena só.

**Como foi modelado, explicitamente** — a parte que importa para ler qualquer número abaixo:

| Peça | Antes | Agora |
|---|---|---|
| **Quem age e é alvo** | `vit > 0 and alma > 0` | **igual** — o caído por Alma sai da cena do mesmo jeito |
| **Rolagens no loop** | — | **nenhuma nova.** O Teste de Morte espiritual não muda o combate (passando ou falhando, o personagem segue fora da cena), então o fluxo aleatório é bit-a-bit o mesmo das rodadas anteriores |
| **O que conta como baixa** | `vit ≤ 0` **ou** `alma ≤ 0` | **só `vit ≤ 0`** — o Teste de Morte físico segue exatamente como sempre esteve |
| **Caído por Alma** | morto | **fora da cena, vivo**, com sequela e um relógio de campanha |

**A consequência tinha que ser medida, não assumida**, então a bateria mortal inteira rodou **duas vezes com a mesma semente**, com o Colapso ligado e desligado.

| O que mudou | Medido |
|---|---|
| **Vitória do grupo** | **0,00pp de diferença em todas as 25 células** — e isso é resultado, não descuido: o caído por Alma já não agia no modelo antigo, então a condição de vitória (limpar os inimigos) não podia mudar |
| **Sobreviventes** | **+0,003 personagem de 4, em média** (máximo **+0,013**, em Difícil de rank 1) — gente que o motor antigo matava e a decisão 205 devolve viva |
| **Cenas com pelo menos um Colapso** | **0,0% a 1,3%** — pico em Difícil de rank 1 |
| **Derrotas em que ninguém morreu de verdade** | **0,0%** em todas as células — nenhum "TPK" do vault era, na verdade, quatro Colapsos |

**O efeito é minúsculo e o motivo é a decisão 206.** Com Alma rara (1d6 = 6 por Mestre de Gu), a especial de Alma quase não aparece: só Padrão, Padrão pesado e Difícil produzem Colapso, e Fácil (Horda, sem Alma) e Clímax (Chefe + Guerreiro, sem especial de Alma) medem **zero** em todos os ranks. **O Colapso Espiritual não é uma alavanca de combate — é um relógio de campanha**, exatamente como a decisão 205 o descreveu ao dispensar simulação própria. A correção do motor era necessária mesmo assim: o motor estava matando permanentemente personagens que a regra manda levantar.

### 1️⃣ Bateria mortal completa — ranks 1-5 × 5 composições, contra o publicado

| Cena | rank 1 | rank 2 | rank 3 | rank 4 *(inédito)* | rank 5 |
|---|---|---|---|---|---|
| **Fácil** | 100,0% | 100,0% | 100,0% | 100,0% | 100,0% |
| **Padrão** | 92,7% | 77,0% | 86,4% | 93,4% | 98,9% |
| **Padrão pesado** | 65,8% | 55,8% | 52,2% | 54,1% | 76,1% |
| **Difícil** | 30,9% | **31,4%** ⚠️ | 46,0% | 61,6% | 37,4% |
| **Clímax** *(Chefe + Guerreiro)* | 3,3% | 54,4% | 87,3% | 74,7% | 89,6% |

**Veredito: 19 das 20 células publicadas conferem dentro de 3 pontos percentuais.** A maior diferença entre as que passam é de 2,8pp (Padrão pesado de rank 1), dentro do ruído de Monte Carlo que o vault já aceita.

**A única que se moveu: Difícil de rank 2 — 35% publicado, 31,4% medido (−3,6pp).** Corrigida na nota para **31%**, junto com a menção de "30%/35%" no callout das duas exceções, que agora lê **31%/31%**. Não muda a leitura de design: Difícil de rank 1-2 continua sendo o quase-Clímax que a decisão 207 aceitou por escolha explícita do autor — só ficou marginalmente mais duro e mais uniforme entre os dois ranks.

**Duração**: Fácil 2,5-4,6 · Padrão 6,0-7,7 · Padrão pesado 7,5-10,5 · Difícil 8,3-9,1 · Clímax 6,8-10,7. As faixas publicadas conferem; as duas pontas que se alargaram (10,5 e 9,1) são o **rank 4**, que a tabela nunca tinha medido. Timeouts ≤ 4,6% (pico no Clímax de rank 2), sem nenhum sinal de estagnação.

**Achado colateral, rank 4:** a célula **Difícil de rank 4 mede 61,6%**, bem acima da faixa de 40-52% que "Difícil" promete — é o último rank que ainda usa `3 Mestres + 1 Guerreiro` antes de o rank 5 trocar para `4 Mestres` (37,4%). O degrau entre 4 e 5 é de 24pp. Nenhum número publicado está errado (a tabela nunca publicou o rank 4), então **nada foi corrigido**; fica registrado como pendência de design.

### 🔴 A tabela de ações do Chefe estava contradizendo a própria nota

A mesma nota publica **duas** taxas de vitória para **a mesma cena** (Chefe + 1 Guerreiro de apoio): a tabela de composição dizia `3%` 🔴 no rank 1, e a tabela "Quantas ações o Chefe tem" dizia `57%`. Remedidas as cinco:

| Rank | Ações | Publicado *(tab. do Chefe)* | Medido | Δ |
|---|---|---|---|---|
| **1** | 4 | 57% | **3,3%** | **−53,7pp** 🔴 |
| **2** | 2 | 62% | **54,4%** | −7,6pp |
| **3** | 2 | 79% | **87,3%** | +8,3pp |
| **4** | 3 | 75% | **74,7%** | −0,3pp |
| **5** | 3 | 75% | **89,6%** | **+14,6pp** |

Os números da tabela de ações eram **os mais antigos da nota inteira** — vinham da quinta rodada, antes das decisões 135-137, 206 e 207. Todos corrigidos, a linha "4–5" foi separada em duas (o rank 4 e o rank 5 divergem em 15pp), e o rank 1 ganhou um aviso próprio: **um Chefe de 4 ações no rank 1 não é um clímax, é uma execução** (0,1 personagem de pé em 3.000 cenas). A linha de leitura "7 a 10 rodadas, 56% a 80%, 1,5 a 2,1 de pé" também foi remedida para **6,8-10,7 rodadas, 54% a 90% do rank 2 em diante, 1,3 a 2,1 de pé**.

### 2️⃣ Spot-check imortal — a régua ΔB da decisão 205 sobreviveu?

Duas leituras, porque a régua publicada foi montada emendando duas medições diferentes da oitava rodada.

**(a) A alegação de "passeio" a ΔB 0** — as 5 composições mortais rodadas nos ranks 6-9 com inimigos no mesmo nível de domínio do grupo. Estas **passam** pelas decisões 206 (Mestres de Gu) e 207 (Horda), então eram as que podiam ter mudado.

> **Medido: 75,9% a 100,0%** em 20 células, contra os **77-100%** publicados. **Confirmado** — a única célula abaixo do piso publicado é o Clímax de rank 6 (75,9% contra 77%), diferença de 1,1pp. As decisões 206-207 não moveram a fase imortal.

**(b) A escada ΔB 0 / +1 / +3** — a âncora de Chefe da oitava rodada (Gu Imortal `M d12`, escolta de Guerreiro no domínio do grupo), com o nível de domínio como única variável, agora nos **quatro** ranks em vez de só no rank 6:

| ΔB do inimigo | rank 6 | rank 7 | rank 8 | rank 9 |
|---|---|---|---|---|
| **0** | 51,8% | 91,3% | 99,0% | 99,6% |
| **+1** | **23,3%** | 79,9% | 96,5% | 99,0% |
| **+3** | **3,1%** | 43,4% | 79,4% | 98,0% |

**Veredito partido, e é o achado mais importante da rodada depois do Colapso.**

- **No rank 6 a régua publicada está certa** — 23,3% contra o "~20%" e 3,1% contra o "~6%" reproduzem a medição da oitava rodada dentro da variação esperada (a diferença vem de duas escolhas de modelagem declaradas: a escolta agora fica no domínio do grupo, como a própria regra manda, e o Chefe usa a Vitalidade cheia do molde). **E ela sobreviveu às decisões 206-207 por construção**: a cena é Chefe + Guerreiro, sem nenhum Mestre de Gu e sem nenhuma Horda — nada que aquelas duas decisões tocam.
- **Dos ranks 7 ao 9 a régua não existe.** O ΔB perde força até sumir: no rank 9, um inimigo **três níveis de domínio acima** do grupo ainda perde 98% das vezes. A causa não é nova — é a **assimetria dominante** que a oitava rodada já tinha diagnosticado (decisão 202): o acerto do inimigo escala `+1/rank` e a Defesa dos personagens `+2/rank`, então o inimigo erra tanto que nenhum bônus de dano compensa.

**O que foi corrigido:** a tabela do callout imortal em [[⚔️ Ameaças Genéricas por Rank]] deixou de ser uma escada única e virou uma **matriz por rank**, com o aviso explícito de que **o ΔB só é dial de verdade no rank 6** e de que os ranks 7-9 não têm dial de dificuldade publicado — a cena ali se resolve por objetivo, terreno, Brecha ou pressão narrativa. Consertar a assimetria estrutural continua sendo a pendência aberta da decisão 202, e **nada de regra nova foi inventado aqui**.

### 3️⃣ Rei de Cem Feras — o número mais suspeito do vault, e ele sobreviveu

A nota [[🐺 Reis Fera e a Maré]] publica "~99% de vitória a ~55-60% da Vitalidade" para o grupo, medido **antes** do piso de ataques da Horda (decisão 207) e de Alma rara (206) — e o Rei de Cem é `Elite + Horda de 8`, ou seja, metade da força dele é exatamente a peça que a decisão 207 endureceu. Remedido em 3.000 iterações por rank (a calibração original era de 1.500, só nos ranks 2-4):

| Rank | Vitória | Vitalidade perdida | Essência gasta | Rodadas |
|---|---|---|---|---|
| 1 | 98,5% | 46,5% | 62,3% | 5,2 |
| 2 | 98,6% | 54,7% | 40,1% | 6,3 |
| 3 | 99,3% | 59,3% | 22,4% | 6,9 |
| 4 | 99,3% | 60,3% | 11,9% | 7,3 |
| 5 | 99,8% | 54,2% | 11,8% | 7,1 |

**O "~99% de vitória" está exatamente certo** (98,5-99,8%), e o custo de Vitalidade **também**, para os ranks 2-5 (54-60%). A única correção é a ponta de baixo: o **rank 1 custa 46,5% e dura 5,2 rodadas**, não os 55-60% e ~7 rodadas que a nota generalizava. A linha da tabela passou a ler **"47-60% da Vitalidade e 5 a 7 rodadas (55-60% do rank 2 em diante)"**.

**Por que o piso da Horda quase não moveu o Rei:** o piso só morde quando a Horda tem **menos de dois alvos de pé** (2 ataques contra dois alvos, 3 contra um). Contra o Rei de Cem o grupo raramente chega nesse estado — ele vence com 3,4 a 3,6 personagens de pé. A decisão 207 endureceu as cenas em que a Horda **continua batendo depois que o grupo já caiu**, e essa não é uma delas.

**Rei de Mil:** **0,0% em todos os cinco ranks**, sem exceção. O "um grupo sozinho NUNCA vence" da nota está literalmente certo, e continua batendo com o cânone dos três grupos.

**A regra de ondas, porém, moveu** — e essa era pré-207 de verdade:

| Hordas simultâneas | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
|---|---|---|---|---|---|
| **2× Horda de 8** *(publicado: 83/56/36 nos ranks 2/3/4)* | 97,1% | **78,3%** | **47,1%** | **29,2%** | 46,1% |
| **3× Horda de 8** *(publicado: 0%)* | **16,5%** | 0,1% | 0,0% | 0,0% | 0,0% |

Duas ondas simultâneas caíram **5 a 9 pontos** em relação ao publicado — aqui o piso de ataques morde, porque com duas hordas o grupo perde gente rápido e a horda passa a atacar uma mesa de dois ou de um. Corrigido para **78/47/29/46** (ranks 2/3/4/5). E "três ao mesmo tempo = 0%" vale **do rank 2 em diante**; no rank 1, com a horda mais fraca do jogo, o grupo ainda arranha **16,5%** — a nota agora diz isso.

### 4️⃣ A tabela de custo da Varredura, recalibrada

Uma onda de Horda de 8 limpa, que é a média de onde a tabela inteira deriva:

| Rank | Vitalidade perdida | Essência gasta | Rodadas |
|---|---|---|---|
| 1 | 15,4% | 32,8% | 2,5 |
| 2 | 23,4% | 23,6% | 3,5 |
| 3 | 28,5% | 14,1% | 4,1 |
| 4 | 32,1% | 7,9% | 4,5 |
| 5 | 29,5% | 7,9% | 4,6 |

**Média: 25,8% de Vitalidade, 17,3% de essência, 3,8 rodadas.** A faixa de Vitalidade publicada no rodapé da nota (23-32%) precisa virar **15-32%**: o rank 1 é bem mais barato do que a calibração de 1.500 iterações nos ranks 2-4 conseguia ver.

Aplicando a mesma regra de escala que a nota declara (a linha "2-3 passaram" é a média, as outras escalam dela em 0,6× e 1,6×):

| Resultado | Vitalidade publicada → medida | Essência publicada → medida |
|---|---|---|
| **4 passaram** | 15% → **15%** ✅ | 10% → **12%** |
| **2-3 passaram** | 25% → **26%** ✅ | 15% → **17%** |
| **1 passou** | 40% → **41%** ✅ | 20% → **23%** |

**A coluna que importa — Vitalidade — não drifou** (≤ 1,2pp em três linhas). A de essência subiu 2-3 pontos e foi corrigida para **12/17/23**. O acúmulo entre ondas do limite 3 ("três ondas varridas custam ~45-75% da Vitalidade") continua valendo: 3 × 15,5% a 3 × 25,8% dá 46-77%.

### 5️⃣ A decisão 211 medida — e a lacuna de treino que ela revelou

A decisão **211** (bônus de treino escalado, `+2` subindo `+1` a cada rank par até `+6`) entrou nas regras **hoje, durante esta rodada**, aplicada antes de simulação por pedido do autor e com a obrigação explícita registrada no Log: *"a próxima rodada deve medir"*. Esta é a próxima rodada.

Ao ligar o knob apareceu uma coisa mais antiga que a decisão 211. **O motor de todas as treze rodadas modela `treino = 0`**: o acerto de PJ é `d20 + atributo + 2×rank + 2`, que decompõe exatamente em `(rank + 2) + rank do Gu` — sem treino nenhum. Mas [[💪 Atributos]] traz `+ treino` na fórmula de **acerto de Gu** desde muito antes da decisão 211, quando o bônus era `+2` fixo. **Os números publicados nunca modelaram o bônus de treino.**

Quatro configurações, mesma semente, ranks 1-5 × 5 composições:

| Configuração | Swing médio | Máximo | O que é |
|---|---|---|---|
| **`+2` fixo** *(a regra pré-211)* | **+9,9pp** | +21,4pp | A lacuna antiga do motor |
| **escalado, só PJ** *(a decisão 211 como publicada)* | **+12,6pp** | **+30,9pp** | O total |
| **escalado vs. `+2` fixo** | **+2,7pp** | +10,0pp | A decisão 211 propriamente dita |
| **escalado, simétrico** *(PJ + inimigo)* | **−8,3pp** | −56,2pp | A correção candidata que a própria 211 nomeia |

**A leitura que muda a conversa: a decisão 211 é o menor dos dois problemas.** Ela sozinha vale +2,7pp em média — dentro do ruído que o vault já trata como aceitável. Os outros +9,9pp são uma lacuna de modelagem que estava lá desde a primeira rodada.

As células que mais doem, para dimensionar: **Difícil de rank 2 iria de 31% para 62%** e **Clímax de rank 2 de 54% para 85%** com o treino ligado só no lado dos PJs. Uma tabela de composição em que "Difícil" mede 46-86% não é mais uma tabela de dificuldade.

**E a correção óbvia corrige demais.** Dar aos moldes de inimigo a mesma escada de treino devolve a média para perto do publicado (−8,3pp), mas com uma variância inaceitável: as cenas homogêneas mal se movem (Padrão: +1,4 a −4,9pp) enquanto as cenas com Horda desabam — **Padrão pesado de rank 5 vai de 76% para 19,8% (−56,2pp)** e Difícil de rank 5 para 3,3%. A causa é aritmética simples: a Horda rola um ataque **por personagem de pé** (com o piso da decisão 207), então somar `+4` de acerto a ela multiplica muito mais rolagens do que somar `+4` ao grupo.

**Mas o mesmo botão conserta os imortais.** A correção simétrica é justamente o que a bateria 2 mostrou faltar nos ranks 7-9:

| Cena imortal | sem treino | só PJ | **simétrico** |
|---|---|---|---|
| rank 7, ΔB +3 | 43,4% | 63,2% | **3,8%** |
| rank 8, ΔB +3 | 79,4% | 87,2% | **9,4%** |
| rank 9, ΔB +1 | 99,0% | 99,4% | **84,3%** |
| rank 9, ΔB +3 | 98,0% | 98,0% | **63,3%** |

O treino simétrico é a primeira coisa medida no vault que **devolve dificuldade à fase imortal** — exatamente o conserto que a decisão 202 deixou em aberto e que a decisão 211 previu ao dizer que os moldes precisariam da mesma escada. E o lado "só PJ" confirma o alerta da 211 palavra por palavra: **agrava** o colapso (rank 6, ΔB +1: 23,3% → 51,8%).

> [!danger] 🔴 Nada foi republicado — e isso é deliberado
> Este é um **fork de design, não uma correção mecânica**, pelos critérios que o vault já usa (decisões 154, 202, 206). Republicar a tabela com o treino ligado exigiria decidir, no lugar do autor, **se um ataque de Gu em combate conta como ação treinada** — e [[🎯 Perícias]] diz que perícia não rola em combate, o que empurra para "não". Aplicar a correção simétrica no escuro trocaria um desequilíbrio por outro, que é literalmente o que a decisão 211 se recusou a fazer.
>
> A tabela de [[⚔️ Ameaças Genéricas por Rank]] continua publicando os números **sem treino dos dois lados** — internamente consistentes, e a mesma premissa das treze rodadas — com um aviso 🔴 na própria nota. O menu foi devolvido ao autor.

### 🛡️ Guarda-corpo — a curva de letalidade da decisão 78

Rerodada por segurança, já que a rodada mexeu no motor: `d6 5,16 · d8 4,01 · d10 3,27 · d12 2,76`, **razão d6/d12 = 1,87** contra a 1,86 publicada. Intacta.

### ✅ O veredito da rodada

**O que se manteve:**

1. **19 das 20 células da tabela de composição**, dentro de 3pp, com todas as regras de hoje ligadas ao mesmo tempo.
2. As **faixas de duração** publicadas, e a ausência total de estagnação (timeout ≤ 4,6%).
3. O **"~99%" do Rei de Cem Feras** e o **"0%" do Rei de Mil** — o par de números que a rodada mais esperava ver quebrar.
4. A coluna de **Vitalidade** da tabela de custo da Varredura.
5. A **régua ΔB no rank 6**, e a alegação de "passeio a ΔB 0" nos ranks 6-9.
6. A **curva de letalidade da decisão 78**.

**O que a rodada descobriu que ninguém procurava:** o motor nunca modelou o **bônus de treino** que [[💪 Atributos]] põe na fórmula de acerto de Gu — uma lacuna de +9,9pp em média, mais velha que qualquer decisão deste lote, encontrada só porque a decisão 211 obrigou a olhar para aquela linha. Ver a bateria 5.

**O que se moveu e foi corrigido:**

| Onde | De | Para |
|---|---|---|
| Composição, Difícil rank 2 | 35% | **31%** |
| Tabela de ações do Chefe (5 linhas) | 57/62/79/75/75 | **3/54/87/75/90**, com a linha "4–5" separada e um aviso no rank 1 |
| Leitura do Clímax | "7-10 rodadas, 56-80%, 1,5-2,1 de pé" | **6,8-10,7 rodadas, 54-90% do rank 2 em diante, 1,3-2,1 de pé** |
| Régua ΔB imortal | escada única (0 / +1 / +3) | **matriz por rank**, com o aviso de que só o rank 6 tem dial |
| Rei de Cem Feras | "~55-60% da Vitalidade, ~7 rodadas" | **47-60% e 5-7 rodadas** (55-60% do rank 2 em diante) |
| Ondas simultâneas | 83/56/36 (ranks 2/3/4) | **78/47/29/46** (ranks 2/3/4/5); "3× = 0%" só do rank 2 em diante |
| Varredura, faixa medida | 23-32% de Vitalidade | **15-32%** |
| Varredura, coluna de essência | 10/15/20 | **12/17/23** |

**O efeito do Colapso Espiritual, medido:** **zero** na vitória do grupo (25 de 25 células), **+0,003 sobrevivente de 4** em média, e **0,0-1,3%** de cenas com pelo menos um Colapso. É a interação com a decisão 206 funcionando como previsto — Alma rara torna o Colapso raro. **A correção do motor era necessária mesmo assim**, porque o motor estava contabilizando como morte permanente uma coisa que a regra manda levantar; o que ela não é, é uma mudança de balanceamento.

**Nenhuma regra nova foi criada nesta rodada.** Tudo o que mudou foi número publicado alinhado à medição, e dois avisos: um onde a nota contradizia a si mesma (ações do Chefe), outro onde ela contradiz [[💪 Atributos]] (o bônus de treino, abaixo).

### 📌 Três pendências de design que a rodada deixa (nenhuma resolvida aqui)

1. 🔴 **O bônus de treino, e o que fazer com ele** — a maior das três, e a única que invalida números publicados. Três saídas, todas medidas acima: **(a)** declarar que ataque de Gu em combate **não** é ação treinada (a tabela publicada fica certa como está, e [[💪 Atributos]] ganha essa ressalva na fórmula de acerto); **(b)** ligar o treino **só nos PJs** e republicar a tabela +12,6pp acima, aceitando que "Difícil" passa a medir 46-86%; **(c)** ligar **simétrico**, que salva a média mortal e **conserta a fase imortal**, mas derruba Padrão pesado de rank 5 em 56pp e exige recompor as cenas com Horda. A opção (c) é a única que resolve duas pendências de uma vez.
2. **Difícil de rank 4 mede 61,6%**, contra a faixa de 40-52% — o degrau para o rank 5 (`4 Mestres`, 37,4%) é de 24pp. Precisa de composição própria para o rank 4, ou de aceitar mais uma exceção documentada?
3. **Os ranks 7-9 não têm dial de dificuldade.** É a pendência da decisão 202 revivida com número novo: nem o ΔB resolve lá em cima. Escalar o acerto dos moldes imortais para `+2/rank` (a paridade com a Defesa dos PJs) devolveria a fase mortal, como a oitava rodada mediu — e a opção (c) da pendência 1 é uma forma concreta de fazer isso. Mas é mudança de regra, e é do autor.

---

## 🧭 Décima quarta rodada — a bateria estendida *(2026-08-31)*

Lote pedido pelo autor: quatro medições que a série deixou para trás. As duas primeiras remedem as cenas **solo** da nona rodada, que foram medidas **antes** de o piso de ataques da Horda existir (decisão 207 — que a própria nona motivou); a terceira é o primeiro **PJ × PJ** desde as rodadas 1-4 do motor Perl; a quarta mede o número que faltava no fork do treino (o item 🔴 da decisão 213). Script: [[simulacoes/2026-08-31-decima-quarta-bateria-estendida.py|_Processo/simulacoes/2026-08-31-decima-quarta-bateria-estendida.py]] — cópia do motor da décima terceira, nada do motor reescrito (a única extensão é um knob que restringe o treino do inimigo por rank; ele devolve 0 sem consumir rolagem, e o baseline reproduziu a décima terceira célula a célula dentro da própria bateria 4). **3.000 iterações/célula, semente `20260830`, mix de Alma C, treino = 0 dos dois lados** — a premissa das tabelas publicadas — em tudo, exceto a bateria 4, cujo assunto é o knob do treino.

### 1️⃣ Horda de 8 solo, com o piso — a decisão 207 trocou a guerra de atrito por uma execução, e o alvo de 7-9 rodadas não existe nesta cena

A nona rodada mediu 1 PJ × Horda de 8 **sem** piso: guerra de atrito de 10-19 rodadas, vitória errática de 10% a 99% conforme o perfil. Remedido com o piso publicado (3 ataques/rodada contra alvo único):

| PJ | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang** | 8,2% · 5,0r *(era 69,6%)* | 0,0% · 5,0r *(56,6%)* | 0,1% · 5,5r *(57,5%)* |
| **Jiaotang** | **37,4%** · 4,6r *(99,1%)* | 0,0% · 4,6r *(51,6%)* | 0,0% · 4,9r *(34,3%)* |
| **Lee** | 0,2% · 4,7r *(71,6%)* | 0,0% · 4,4r *(10,2%)* | 0,0% · 4,8r *(12,3%)* |
| **Demvi** | 0,8% · 4,3r *(15,2%)* | 0,0% · 4,6r *(30,3%)* | 0,0% · 5,2r *(39,2%)* |

*(vitória · rodadas médias da cena inteira; entre parênteses, a vitória da nona rodada pré-piso. As rodadas da nona — 9,7 a 19,0 — eram medidas só nas vitórias.)*

**O piso não aproximou a cena do alvo — ele a atravessou.** Três ataques de `M d8` por rodada num único personagem, com a parede de Vitalidade da Horda ainda dimensionada para quatro, derrubam o PJ em ~5 rodadas antes que ele cave a barra: **10 das 12 células medem ≤ 1%**, e o melhor caso da mesa é 37,4% (Jiaotang no rank 1). A cena saiu de "cansa mas não assusta" (o defeito que a nona apontou) para **execução**. E o alvo do autor pra batalha solo — **7-9 rodadas** — não acontece em nenhuma célula (0 de 12; média 4,8).

Medidas então as duas hipóteses de escala à la F&M (a matilha dimensionada pra quem está em cena):

| Variante | Vitória (12 células) | Rodadas (média) | Células em 7-9 |
|---|---|---|---|
| **Horda de 8 + piso** *(a regra de hoje)* | 0,0-37,4% | 4,3-5,5 (4,8) | 0/12 |
| **Horda de 2** *(proporcional à mesa: 8 × 1/4)* | 48,6-99,1% | 1,7-4,4 (3,3) | 0/12 |
| **Horda de 3** *(proporcional, teto da faixa)* | 5,6-96,9% | 2,4-5,1 (4,2) | 0/12 |
| **Horda 8 com `VIT × 1/4`** *(mantém o dado dos 8)* | 26,1-97,3% | 1,9-4,7 (3,6) | 0/12 |

**Nenhuma variante entrega 7-9 rodadas — e a razão é estrutural, não de calibragem.** Solo, uma cena com chance real de vitória é curta (3-5 rodadas: um atacante só de cada lado da conta); a única configuração medida que estica um solo até 7-9+ rodadas é parede de Vitalidade grande com pressão baixa — que é literalmente a guerra de atrito pré-piso que o autor rejeitou ("8 feras devem assustar, não cansar"). **Na cena de Horda, o alvo de duração e o piso pedem coisas opostas.** Das variantes jogáveis, a proporcional de 3 é a que mais preserva perigo sem executar (5,6-96,9% — errática entre perfis, como todo solo é), e a `VIT × 1/4` é a mais estável (26,1-97,3%) mantendo a ficção de matilha cheia. **Nada foi aplicado** — menu no [[🧭 Log de Decisões]].

### 2️⃣ Rei de Cem solo — a sentença virou absoluta

| PJ | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang** | 0,0% *(era 3,7%)* | 0,0% *(3,0%)* | 0,0% *(6,0%)* |
| **Jiaotang** | **0,1%** *(8,4%)* | 0,0% *(0,1%)* | 0,0% *(0,1%)* |
| **Lee** | 0,0% *(0,0%)* | 0,0% *(0,0%)* | 0,0% *(0,0%)* |
| **Demvi** | 0,0% *(0,0%)* | 0,0% *(0,1%)* | 0,0% *(0,1%)* |

**Confirmado — e endurecido.** O melhor caso da mesa caiu de 8,4% pra 0,1%, e a cena dura 2,5-3,6 rodadas: a escolta de Horda com o piso executa quem chega sozinho antes de o Elite precisar trabalhar. É o comportamento que [[🐺 Reis Fera e a Maré]] promete ("cena Difícil de verdade **pra mesa de 4**") levado ao limite. **Nenhum ajuste** — o design publicado prevê exatamente isso; a cena solo contra um Rei é fuga, isca ou negociação, nunca combate.

### 3️⃣ PJ × PJ — o primeiro duelo do motor atual, e o Xie Lang venceu o torneio inteiro

As rodadas 1-4 mediram duelos no motor Perl (pré-pool de dados, pré-barra de Alma como alvo) e nenhuma rodada mediu desde então. Os 6 pares dos 4 PJs, ranks 1/3/5 *(vitória do primeiro nomeado · rodadas médias)*:

| Duelo | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **Xie Lang × Jiaotang** | 80,1% · 3,1r | 98,1% · 3,2r | 99,9% · 2,9r |
| **Xie Lang × Lee** | 84,3% · 4,8r | 98,9% · 4,0r | 99,8% · 3,5r |
| **Xie Lang × Demvi** | 82,6% · 5,6r | 96,5% · 4,0r | 99,0% · 3,5r |
| **Jiaotang × Lee** | 96,7% · 4,7r | 90,3% · 6,6r | 83,7% · 7,0r |
| **Jiaotang × Demvi** | 93,6% · 4,3r | 70,8% · 5,9r | 60,6% · 6,4r |
| **Lee × Demvi** | 75,2% · 8,3r | 28,0% · 7,5r | 27,4% · 7,5r |

**Placar geral** (média de vitória de cada um nos próprios 3 duelos): Xie Lang **83,9% → 97,8% → 99,5%** · Jiaotang 70,1% → 54,3% → 48,2% · Demvi 14,7% → 34,9% → 37,7% · Lee 31,4% → 12,9% → 14,6%.

As duas perguntas da bateria, respondidas:

- **(a) O aviso de PvP do Livro do Mestre de F&M ("dano de jogador contra jogador acaba a luta em 1-2 turnos") não é a norma aqui — mas aparece num eixo só.** Os três duelos físicos (sem Xie Lang) rodam 4,3-8,3 rodadas com 0-12% de resolução em ≤2 rodadas: a RD e a Vitalidade por estágio seguram o dano físico de PJ. A degeneração existe exclusivamente nos duelos do Xie Lang (pico: 34,4% dos Xie × Jiaotang de rank 1 acabam em ≤2 rodadas). O conserto que o F&M usa — metade de dano/cura/RD em PvP + condição Ferido escalonada — segue catalogado como padrão **não aplicado** em [[🔍 Síntese — Feiticeiros e Maldições (Bestiário, Mestre, Técnicas)]]; como regra geral ele continua desnecessário, porque o problema real é o item (b).
- **(b) Xie Lang é dominante em toda a tabela — e 80-100% das vitórias dele são queda de Alma.** É o mesmo eixo já diagnosticado nas rodadas oito e nove, agora com os dois lados da assimetria somados contra um PJ: o ataque de Alma mira a Defesa de Alma (`10 + VON + rank`, escala +1/rank contra o acerto dele a +2/rank) e cai numa barra menor que a Vitalidade, sem RD nenhuma. Nos registros da era Perl o quadro era o oposto (o Xie Lang duelista fraco antes de a decisão 69 preencher os buracos de catálogo de Lua/Alma; "Lee no fundo do PvP é o desenho funcionando" era o veredito que sobrou) — **o Lee no fundo confirma até hoje** (paga pico de dano por versatilidade), e **Jiaotang × Demvi trocam de lugar com o rank** (70→48% contra 15→38%), o mesmo cruzamento de economia de essência da nona rodada. **Nada foi mudado**: o vault nunca prometeu equilíbrio PvP, e duelo entre PJs é cena rara — mas a mesa deve saber que, hoje, duelar com o Xie Lang é aceitar ~1 chance em 20 nos ranks 3+. Registrado em "Em aberto" pra leitura do autor.

### 4️⃣ O híbrido do fork do treino — recupera os ranks 7-9 como a saída (c), custa zero na fase mortal, e superaquece o rank 6

O item 🔴 da decisão 213 listou três saídas medidas; existe uma quarta que o Log não tinha nomeado: **(a) na fase mortal + (c) restrita aos moldes de rank 6+** — o treino fica fora da matemática mortal (as tabelas publicadas continuam certas como estão) e a escada da decisão 211 entra só no acerto fechado dos moldes imortais (`d20 + rank + N` → `+ treino escalado`), atacando exatamente a assimetria que a decisão 202 diagnosticou (acerto de inimigo +1/rank contra Defesa de PJ +2/rank). O PJ não ganha treino em fase nenhuma. Medido na âncora ΔB da décima terceira:

| Célula | sem treino *(publicado)* | **híbrido** | simétrico (c), 13ª |
|---|---|---|---|
| **rank 6** · ΔB 0 / +1 / +3 | 51,8 / 23,3 / 3,1% | **4,4 / 0,6 / 0,0%** 🔴 | — |
| **rank 7** · ΔB 0 / +1 / +3 | 91,3 / 79,9 / 43,4% | 34,2 / 15,7 / **1,4%** | *(+3: 3,8%)* |
| **rank 8** · ΔB 0 / +1 / +3 | 99,0 / 96,5 / 79,4% | 58,9 / 36,1 / **5,4%** | *(+3: 9,4%)* |
| **rank 9** · ΔB 0 / +1 / +3 | 99,6 / 99,0 / 98,0% | 84,5 / 80,4 / **57,3%** | *(+1: 84,3% · +3: 63,3%)* |

Três leituras:

1. **A pergunta da rodada tem resposta: sim.** Nos ranks 7-9 o híbrido recupera a dificuldade como a saída (c) — um pouco mais duro até (rank 7 ΔB+3: 1,4% contra 3,8; rank 8: 5,4 contra 9,4; rank 9: 57,3 contra 63,3) — **sem tocar a fase mortal**: a bateria mortal completa rodada sob o híbrido mediu **0,00pp de diferença nas 25 células** (por construção — o knob devolve 0 pra rank < 6 sem consumir rolagem). O custo de −56pp nas cenas mortais com Horda, que desqualificava a (c), **não existe no híbrido**.
2. **Mas o rank 6 superaquece.** É o único rank onde o dial ΔB já funcionava — e com +5 de treino no molde, ΔB 0 despenca de 51,8% pra 4,4% e toda célula da âncora vira sentença. A causa é aritmética: a escada de treino é quase chapada na faixa imortal (+5/+5/+6/+6) enquanto o déficit de acerto cresce +1 por rank — um knob chapado corrige demais na base da faixa e de menos no topo (o rank 9 segue em 84,5% a ΔB 0).
3. **As composições a ΔB 0 deixam de ser passeio — e reganham uma escada, desordenada.** Sob o híbrido: Fácil segue 100%, Padrão 95,7-99,7%, Padrão pesado 53,2-94,8%, Difícil 22,9-48,9%, Clímax 15,9-94,4% (ranks 6→9). Pela primeira vez desde a oitava rodada uma cena imortal montada por composição tem dificuldade real — mas desordenada entre ranks (o Clímax vai de 15,9% no rank 6 a 94,4% no 9), então isso não substitui o ΔB como régua; é efeito colateral a pesar no fork, não uma tabela nova.

**Nada foi aplicado.** O número entra no item 🔴 do Log como **quarta saída medida (d)**; a escolha — inclusive a dose por rank, se o autor quiser tratar o superaquecimento do rank 6 (ligar a escada só do rank 7 em diante, ou trocar a escada de treino por `+1 × (rank − 6)`) — é dele, e essas doses alternativas **não foram medidas**.

### ✅ O veredito da rodada

- **Horda solo**: o piso da decisão 207 conserta a mesa de 4 (décima terceira) mas pune demais o PJ isolado — execução em ~5 rodadas, vitória 0-37%. O alvo de 7-9 rodadas solo é inatingível com todas as peças medidas: duração e piso pedem coisas opostas nessa cena. Menu devolvido ao autor.
- **Rei de Cem solo**: sentença confirmada e absoluta (0,0-0,1%) — o design publicado ("pra mesa de 4") se comporta como promete. Nenhum ajuste.
- **PJ × PJ**: a degeneração de 1-2 rodadas que o F&M teme não é a norma (só nos duelos do Xie Lang), mas **Xie Lang vence 84-99,5% de qualquer duelo** via Alma. Dominância registrada pra leitura do autor; Lee no fundo confirma o veredito histórico.
- **Híbrido do treino**: a quarta saída do fork, medida — recupera os ranks 7-9 como a (c) com custo zero na fase mortal, mas superaquece o rank 6. No item 🔴.

Anotações feitas: a seção da nona rodada ganhou o aviso de "números pré-piso" apontando pra cá, e [[⚔️ Ameaças Genéricas por Rank]] ganhou o número medido do solo-com-piso no parágrafo do piso da Horda. **Nenhuma regra mudou nesta rodada.**

---

## ⛈️ Décima quinta rodada — tribulação, face RD e a mesa sem o Físico *(2026-08-31)*

Script: [[simulacoes/2026-08-31-decima-quinta-tribulacao-e-potencia.py]] (cópia do motor da décima quarta + o **motor de tribulação**, que nunca tinha existido em código versionado). Semente 20260830, 3.000 iterações por célula, **20.000 carreiras** na bateria de reprodução, mix de Alma "C", `treino = 0` nos dois lados (decisão 215).

---

### 🌩️ O desenho de resolução da tribulação — declarado por extenso

Quatorze rodadas modelaram combate; nenhuma modelou uma Calamidade. Este é o desenho adotado, montado **só com regras já publicadas** — nada foi inventado. A sessão que escreve a regra tem que conseguir reescrever isto idêntico a partir daqui.

**1. O que é uma "rodada" de tribulação.** É **uma etapa**. Não existe iniciativa, alcance, ação nem turno: a Calamidade é uma sequência de testes anunciada, e a unidade de resolução é a etapa. Uma **Calamidade Terrestre são 3 rodadas** (etapas 1 · 3 · 5); uma **Provação Celestial e tudo acima são 5** (1 · 2 · 3 · 4 · 5). **Nunca se para no meio** — todas as etapas são roladas, mesmo depois de duas falhas.

**2. Como se rola uma etapa.**

```
Etapa = d20 + atributo  vs  CD da etapa
   1 — O Aviso      CON
   2 — A Lacuna     VON
   3 — A Fraqueza   o atributo MAIS BAIXO da ficha
   4 — A Brecha     AST
   5 — O Veredito   VON + nível de domínio no Caminho principal
```

**Sem bônus de treino** — a decisão 215 fechou que o treino vale só em teste de perícia, e uma etapa é teste de atributo puro. **Sem bônus de rank**: o vault não põe rank em teste de atributo, só em acerto e Defesa.

**3. Como a CD se compõe.** Ver o veredito do fork logo abaixo; a fórmula medida como correta é a de [[🌩️ Calamidades e Provações]]:

```
CD de cada etapa = 14 + 2 × (rank − 6)
                   + bônus da faixa do Contador (0/+1/+2/+3/+5)
                   + 2 se Provação Celestial ou acima
                   + escalonamento por excesso de Marcas (se houver)
                   − 3 se Gu de Estabilização (sequência inteira)
                   − 2 se terra Inabalável (só Calamidade Terrestre)
                   − 2 por presságio respondido (uma etapa cada)
```

A **vantagem do Imortal aliado** entra como vantagem em uma etapa. O jogo ótimo modelado gasta presságios e vantagem nas **etapas mais difíceis** (maior `CD − modificador`) — declarado, porque a mesa real pode gastar pior.

**4. As Fichas de Azar.** O mestre recebe `faixa` Fichas ([[⛈️ A Vontade do Céu]]) e o motor as gasta contra a sequência, **no máximo uma por etapa**, sempre contra um **sucesso**: se a margem foi ≤ 2, converte em falha (a opção garantida); senão, rerrola o d20 e fica com o pior. Só as duas opções que a nota autoriza.

**5. Um 1 natural conta como duas falhas.** Modelado como `sucessos efetivos = sucessos − (nº de 1 naturais)`, com piso em 0 — a leitura que fecha com a provação da [[♾️ A Ascensão Imortal|Ascensão]]. **Numa Terrestre, um único 1 natural é falha automática**, porque 3 etapas não comportam a correção.

**6. O que uma etapa falhada custa.** `M d6` no trilho que a Calamidade atacou (Vitalidade ou Alma — a mesa anuncia antes), **por etapa falhada**, e **uma rolagem `1d6` na tabela de dano colateral** de [[🌾 Ecologia e Economia da Terra Abençoada]] — esta segunda acontece *mesmo quando o personagem passa a Calamidade inteira*. Terra Inabalável ignora a primeira rolagem; terra Frágil rola uma a mais.

**7. Dano à Fenda Imortal.** `+1 nível de Ferimento da Terra` por **Calamidade falhada** (não por etapa), pela tabela de [[🗝️ Terra Abençoada]]; nível 4 sem reparo em um ano custa a Abertura, o rank e a vida. Em faixa Alvo do Céu, duas Calamidades falhadas seguidas levam direto ao nível 2. Na banda de excesso de +25 a +50% o escalonamento proposto adiciona **um Ferimento da Terra por etapa falhada** — é a única fonte que escala por etapa em vez de por evento.

**8. Gasto de Essência Imortal.** `50 UV + 3 meses internos por nível` de Ferimento da Terra reparado, **sem pular níveis**. O tanque contra o qual isso se lê é o **da terra**, não o da ficha: 200/400/600/800/1.200 UV no rank 6 por qualidade, dobrando a cada rank. O modelo repara **1 nível por década interna** (a correção que a quarta rodada já tinha feito).

**9. As simplificações — todas declaradas.**

| Simplificação | Por quê |
|---|---|
| **Atributos não crescem com o rank** | Porque o sistema não os faz crescer: 12 pontos na criação e ponto final. Isso tem consequência medida — ver o achado 🔴 abaixo |
| A faixa do Contador vem **só do gatilho de Marcas** (`+5 a cada 10.000`) nos cenários do autor | É o único gatilho que a ficha do cenário determina. Os outros dez são história de campanha; o fork completo por faixa está na bateria T3 |
| Presságios/Gu/terra/aliado entram como **dial**, não como sorteio | A nota trata os três presságios como obrigatórios e as reduções como o caso normal — o dial deixa o autor ler qualquer nível de preparação |
| A Calamidade "sob medida" (os 3 passos) não é modelada como conteúdo | Ela muda **a ficção da etapa**, não o número dela. O que ela move — a CD por faixa — está no fork T3 |
| Vitalidade/Alma zeradas pelo dano `M d6` são **contabilizadas mas não resolvidas** | A regra **não diz** o que acontece se a Calamidade zerar o trilho. Fica reportado como lacuna, não preenchido |
| Marcas do evento sorteadas uniformemente na faixa publicada | 200-500 · 1.000-2.000 · 6.000-8.500, dobro para Físico Extremo |
| O dano `M d6` é rolado **sem o teto de 16 dados** da decisão 225 | O teto é troca de média-por-média: a média de `32d6` e a de `16d6 + 56` são a mesma. Só o **desvio** muda, e todo número desta seção é média. As baterias de combate (ranks 1/3/5) são intocadas por construção — `M ≤ 16` na fase mortal inteira |

---

### ✅ T1 — a reprodução da quarta rodada, e um `+5` que não existe em regra nenhuma

20.000 carreiras por célula, método transcrito da [[#🔧 Método desta rodada|quarta rodada]] (Calamidade Terrestre a cada 10 anos internos, Provação a cada 100, do rank 6 até 10.000 Marcas). Ficha genérica de 12 pontos (`FOR+1 · CON+3 · DES+2 · AST+2 · VON+3 · CAR+1`).

| Perfil | Preparação | Vivo no rank 7 | Quarta rodada | Δ | Anos internos | UV de reparo |
|---|---|---|---|---|---|---|
| **Imortal comum** | despreparado | **0,2%** | 2,2% | −2,0pp | 397 | 527 |
| **Imortal comum** | típico | **49,9%** | 48,3% | **+1,6pp** | 340 | 413 |
| **Imortal comum** | bem preparado | **76,2%** | 70,2% | +6,0pp | 260 | 152 |
| Físico *(+5 de CD, como a 4ª)* | despreparado | 0,0% | 0,0% | +0,0 | — | 448 |
| Físico *(+5 de CD, como a 4ª)* | típico | **0,0%** | 4,2% | −4,2pp | — | 455 |
| Físico *(+5 de CD, como a 4ª)* | bem preparado | **1,1%** | 20,2% | **−19,1pp** | 245 | 374 |
| **Físico *(regra escrita: só o piso de CAC 15)*** | despreparado | 0,0% | — | — | 250 | 488 |
| **Físico *(regra escrita)*** | típico | **25,1%** | — | — | 228 | 459 |
| **Físico *(regra escrita)*** | bem preparado | **63,8%** | — | — | **161** | 192 |

**A curva do Imortal comum reproduz.** As três células caem a −2,0 / +1,6 / +6,0pp do publicado em 2026-08-28, com o motor reescrito do zero e sem acesso ao código antigo. O pilar "a preparação **é** o sistema" continua de pé, medido duas vezes por caminhos independentes.

> [!warning] 🔴 Achado — o "+5 se Físico Extremo" do método da quarta rodada não existe em regra nenhuma
> Nenhuma nota do vault dá +5 de CD a um portador de Físico Extremo. O que [[⛈️ A Vontade do Céu]] dá é um **piso de +15 no Contador de Ameaça**, que o coloca em **Notado — +1 de CD**, não +5. Medido pela regra como está escrita, o Físico bem preparado atravessa o rank 6 em **63,8%** (contra os 20,2% publicados) e em **161 anos internos** contra os 260 do Imortal comum. Isso muda a leitura do achado 2 da quarta rodada: o Físico não é "três vezes e meia mais mortal e um quarto mais rápido" — pela regra escrita ele é **ligeiramente mais mortal (−12,4pp) e 38% mais rápido**, que é uma troca muito mais parecida com o que a nota do físico promete. O `+5` é o número que a [[🎲 A Mesa — Personagens dos Jogadores|nota da Mesa]] repete ("uma Calamidade a cada ~3 meses com +5 de CD"), e ele só se justifica se o personagem estiver em **Alvo do Céu** — o que é destino provável de um Físico, mas não é o piso dele. **Não corrigido nesta rodada** (é território da sessão paralela): reportado ao autor.

---

### 🔴 T3 — O FORK DA CD: duas fórmulas incompatíveis, e o veredito

O vault publica duas contas diferentes para a mesma coisa:

| | Fórmula | Rank 6 Perseguido | Rank 8 Ignorado |
|---|---|---|---|
| **A** — [[🌩️ Calamidades e Provações]] l.49 | `14 + 2 × (rank − 6) + faixa (+2 se Provação)` | **17** | **18** |
| **B** — [[⛈️ A Vontade do Céu]] l.109 | base `14/18/22` pela faixa, **"mais os bônus da tabela de faixas"** | **21** | **14** |
| **C** — leitura escopada de B (só a etapa 3, o "Passo 2" da Tribulação sob medida) | mista | 18,3 (média) | 16,7 |

**Mortalidade por Provação Celestial (bem preparado, 3.000 iterações/célula) — 0-1 sucessos é morte sem Teste de Morte:**

| Rank | Faixa | **A** *(rank)* | **B** *(faixa)* | C *(escopada)* |
|---|---|---|---|---|
| 6 | Ignorado | **11,3%** | 11,3% | 11,3% |
| 6 | Marcado | **60,0%** | 60,0% | 60,0% |
| 6 | Perseguido | **82,4%** | **99,2%** | 88,4% |
| 6 | Alvo do Céu | 95,5% | **100,0%** | 97,3% |
| 7 | Ignorado | **18,7%** | 11,6% | 19,8% |
| 8 | Ignorado | **31,1%** | 10,7% | 25,7% |
| 8 | Marcado | 90,8% | **57,0%** | 84,4% |
| 9 | Ignorado | **44,2%** | 9,8% | 33,9% |
| 9 | Notado | 81,8% | **24,9%** | 69,1% |

> [!important] ✅ **Veredito: a fórmula correta é a A — `14 + 2 × (rank − 6) + faixa (+2 se Provação)`.** A linha de [[⛈️ A Vontade do Céu]] deve deixar de enunciar CD própria.
> Cinco razões, todas medidas ou estruturais:
> 1. **B conta a faixa duas vezes.** O próprio texto de B diz "mais os bônus de CD da tabela de faixas" *sobre* uma base que já é a faixa. A [[☯️ Marcas de Dao]] é explícita de que **os bônus de CD vêm só da tabela de faixas** — B viola isso.
> 2. **B é indefinida abaixo de Marcado.** Não existe base para Ignorado nem para Notado, que são as duas faixas onde a maioria da mesa vive. (A medição acima usou 14 como leitura caridosa.)
> 3. **B não escala com rank.** Um Venerável Ignorado enfrenta a mesma CD 14 de um rank 6 Ignorado — 9,8% de mortalidade por Provação no rank 9 contra 44,2% pela A. Isso apaga o eixo de progressão inteiro do sistema.
> 4. **B torna Perseguido e Alvo do Céu matematicamente insobrevivíveis em TODO rank** (97,9-100% de mortalidade por Provação). Isso contradiz frontalmente a regra de mestre da própria nota: *"a saída tem que estar aberta"* e *"um CAC alto é uma conquista, e trate como tal"*.
> 5. **A é a fórmula que reproduz a curva publicada** — a bateria T1 acima bate os 2,2/48,3/70,2% da quarta rodada usando A.
>
> **Recomendação de texto:** a seção "Passo 2" de [[⛈️ A Vontade do Céu]] deve dizer *"CD conforme a fórmula de [[🌩️ Calamidades e Provações]]"* e parar aí. Os números 14/18/22 podem sobreviver como **descrição de sensação** ("no Marcado a etapa central pesa como uma CD 14; no Alvo do Céu, como 22"), nunca como conta.

> [!warning] 🔴 Achado estrutural — a escada de CD ultrapassa a ficha, e nada na ficha a alcança
> Pela fórmula A, cada rank soma **+2 de CD em todas as etapas** (10 pontos de dificuldade numa Provação de 5 etapas). Do lado do personagem, **só uma etapa das cinco cresce** — a 5, que soma o nível de domínio, e ela ganha **+1** por patamar de Marca. Atributos não crescem: [[💪 Atributos]] dá 12 pontos na criação e nenhuma regra do vault os aumenta depois. O resultado, medido: um Imortal **bem preparado e Ignorado** morre em **11,3%** das Provações no rank 6, **31,1%** no rank 8 e **44,2%** no rank 9 — a mesma preparação, a mesma ficha, o triplo do risco. Nos ranks 8-9 a Provação Celestial é a rotina do patamar, não a exceção. **Isto não é um número para corrigir nesta rodada** — é uma pergunta de design para o autor: ou os atributos ganham progressão imortal, ou a escada de CD para de subir com o rank, ou as reduções de preparação escalam. Registrado em "Em aberto".

---

### 📊 T2 — Os três cenários pedidos, com a conta da Fenda e do UV

Preparação **típica** (`−3` de Gu de Estabilização + 2 presságios respondidos), fórmula A, terra Comum, faixa vinda só do gatilho de Marcas. Por evento:

| Cenário | Faixa | Etapas | CD | Sucesso | **Morte** | Marcas | Dano no trilho | Ferimento PJ | **Ferimento da Terra** | **UV** |
|---|---|---|---|---|---|---|---|---|---|---|
| **1 · r6 inicial, 1.000 Marcas** *(Terrestre)* | Ignorado | 3 | **14** | **71,1%** | 0,0% | 206 | 10,2% do pool | 0,29 | **0,29** | **14,4** |
| **2 · r6 estendido, 12.000 Marcas (+20%)** | Ignorado | **5** | **18** | **41,3%** | **30,2%** | 421 | 26,1% | 0,59 | **0,59** | **29,4** |
| **3a · r7 inicial, 10.000 Marcas** *(Terrestre)* | Ignorado | 3 | **16** | **62,0%** | 0,0% | 174 | 11,3% | 0,38 | **0,38** | **19,0** |
| **3b · r7 estendido, 120.000 Marcas (+20%)** | **Perseguido** | **5** | **23** | **0,0%** | **99,4%** | 0 | 43,7% | 1,00 | **1,00** | **50,0** |

*Números da ficha genérica; os quatro PJs da mesa ficam dentro de ±8pp e aparecem célula a célula na saída do script. A dispersão entre eles é governada pelo **atributo mais baixo** (etapa 3): Demvi e Xie Lang têm `FOR −1` e pagam 4-8pp por isso.*

**O ciclo de 100 anos internos** (10 Terrestres + 1 Provação Celestial — a década real do calendário imortal), que é onde "dano à Fenda" e "gasto de UV" viram grandezas legíveis:

| Cenário | Preparação | **Vivo ao fim** | Marcas | Fer. da Terra ao fim / pico | **UV** | **% do tanque da terra** | Meses de reclusão |
|---|---|---|---|---|---|---|---|
| **1 · r6 inicial** | despreparado | 54,5% | 1.400 | 0,89 / 1,44 | **272** | **68,0%** | 16,3 |
| **1 · r6 inicial** | típico | **80,2%** | 2.636 | 0,33 / 1,11 | **149** | **37,3%** | 8,9 |
| **1 · r6 inicial** | bem preparado | **88,8%** | 3.664 | 0,14 / 0,82 | 64 | 15,9% | 3,8 |
| **2 · r6 estendido** | típico | **1,9%** | 1.421 | 0,99 / 1,01 | 48 | 12,0% | 2,9 |
| **3a · r7 inicial** | típico | **70,4%** | 2.125 | 0,52 / 1,22 | 196 | 24,6% | 11,8 |
| **3b · r7 estendido** | bem preparado | **0,0%** | 2 | 1,00 / 1,00 | 1 | 0,1% | 0,0 |

**A leitura de mesa dos três números que o autor pediu:**

- **Dano à Fenda.** No cenário padrão a Fenda oscila entre **Íntegra e Rachada** e volta ao normal — o pico médio é 1,1 nível e o reparo de uma década segura. **Ela nunca chega a Ferida** com preparação típica. É pressão de manutenção, não espiral: a espiral só começa quando o personagem **para de reparar**, e é isso que a nota de Calamidades já promete.
- **Gasto de Essência Imortal.** **149 UV por século interno** com preparação típica no rank 6 — **37% do tanque de uma terra Comum**, e ~1,5 ano de renda de uma camada 3 Comum (200 PEI/ano). Despreparado sobe a **272 UV (68% do tanque)**, que é o ponto em que a manutenção compete com o investimento. **O reparo é caro em atenção e barato em pedra**: os 9 a 16 meses internos de reclusão pesam mais que o UV.
- **Ferimentos no personagem.** 3,3 por século típico, 6,3 despreparado — de um teto de 20 (−100% de Vitalidade). É o relógio que mata o Imortal negligente **antes** de qualquer Provação.

---

### 🔴 T4 — A escala de escalonamento por excesso: **brutal, e fora de ordem**

Rank 6, preparação típica. Excesso medido sobre a banda de 10.000 Marcas.

| Banda proposta | Etapas | CD | Sucesso | **Morte/evento** | **Vivo em 100 anos** | Fer. da Terra/100a | UV/100a |
|---|---|---|---|---|---|---|---|
| **no teto (0%)** | 3 | 14,0 | 72,6% | 0,0% | **100,0%** | 0,00 | 135 |
| **≤ +10% → +1 CD** | 3 | 15,0 | 68,3% | 0,0% | **100,0%** | 0,00 | 163 |
| **+10 a +25% → +2 CD e categoria acima** | **5** | 18,0 | 41,3% | **30,2%** | **2,9%** | 0,97 | 47 |
| **+25 a +50% → +4 CD e Ferimento auto por falha** | 3 | 18,0 | 49,3% | 0,0% | **1,7%** | **4,66** | 117 |
| **> +50% → +6 CD e cadência dobrada** | 3 | 20,0 | 34,4% | 0,0% | **25,7%** | 3,29 | 305 |

> [!important] ✅ **Veredito pedido: a escala é BRUTAL — e, pior que brutal, é NÃO-MONOTÔNICA.**
> **(a) O primeiro degrau é decorativo.** `≤ +10% = +1 CD` custa 4,3pp de sucesso e **zero** de mortalidade e de dano à Fenda. Frouxo, mas inofensivo.
> **(b) O segundo degrau é um precipício, e a culpa não é do `+2 CD` — é do "categoria acima".** Subir de categoria não soma dificuldade: **importa uma regra de morte que a Calamidade Terrestre não tem** (0-1 sucessos numa sequência de 5 = morte sem Teste de Morte). O evento sai de **0% de mortalidade** para **30,2%**, e um século interno sai de 100% de sobrevivência para **2,9%**. Vinte por cento acima do teto compra uma chance em trinta e quatro de estar vivo em cem anos.
> **(c) O terceiro degrau mata por outra porta, com a mesma força.** `+4 CD` sozinho seria caro-mas-jogável; o **Ferimento da Terra automático por etapa falhada** produz **4,66 níveis por século** contra um reparo de 1 nível por década — a Fenda colapsa (nível 4) e leva a Abertura junto. Sobrevivência **1,7%**, sem uma única morte por Provação.
> **(d) O quarto degrau, o que deveria ser o pior, é o mais brando dos três últimos.** `+6 CD` e cadência dobrada deixam **25,7%** de sobrevivência — **nove vezes mais** que a banda de +20% e **quinze vezes mais** que a de +40%. A ordem dos degraus está invertida na prática.
>
> **Três observações que agravam o veredito, e que a sessão paralela precisa pesar:**
> 1. **Esta escala é agora o ÚNICO preço do excesso, e a decisão 218 a colocou nessa posição de propósito.** Com os tetos duros revogados, passar do topo da faixa é o caso **normal** do "Imortal denso" — a decisão registra explicitamente que *"o preço do excesso é a Vontade do Céu escalando as Calamidades"*. Ou seja: toda a punição por densidade está concentrada nesta única escala, e ela precisa aguentar sozinha o peso de ser um **desenho jogável**, não um portão. Medida, ela não aguenta: 20% acima do topo já é 2,9% de sobrevivência por século.
> 2. **A escala é a única coisa que separa o "Imortal denso" da morte.** A decisão 218 quer que ficar denso seja uma **jogada** ("é assim que o Imortal denso deixa de ser exceção de regra e vira o caso normal"). Com os degraus como estão, ficar denso é suicídio: a banda de +10-25% — a primeira que um Imortal denso encosta — é justamente a mais letal das quatro.
> 3. **A escala não tem teto de rank.** Aplicada ao rank 7 com +20% (cenário 3b), a combinação `Perseguido + categoria acima + 5 etapas` dá **CD 23** e **99,4% de mortalidade por evento**. Não é uma penalidade dura; é a ausência de resultado.
>
> **Se o autor quiser mantê-la**, o desenho mínimo que a medição sustenta: mover o **"categoria acima"** para a banda de topo (onde a morte cabe), pôr um **teto de 1 Ferimento da Terra por evento** na banda de +25-50%, e deixar as bandas baixas como estão. Isso restaura a monotonia. **Nada disso foi aplicado — é medição, e a decisão é do autor.**

---

### 🟠 T5 — A extensão retida da decisão 224: `B` ilimitado acima do topo da faixa

A decisão 224 publicou a Densidade Imortal **com teto em B 4** e mandou à bateria a continuação natural: **`+1 de B` a cada 25% do topo da faixa excedido, sem teto** — exatamente a alavanca que o excesso de Marcas da decisão 218 torna corriqueira. Grupo de PJs com o `B` do excesso, inimigo no domínio-base do rank (o Imortal denso contra a cena publicada):

| Rank | Marcas | Excesso | `B` extra | Vitória média | Rodadas médias | **Clímax** | Vitalidade perdida |
|---|---|---|---|---|---|---|---|
| 6 | 10.000 | 0% | 0 | 94,4% | 5,69 | **8,31r** | 41,7% |
| 6 | 12.500 | +25% | **+1** | 99,7% | 4,80 *(−15,7%)* | **6,50r** *(−21,7%)* | 30,0% |
| 6 | 15.000 | +50% | **+2** | 100,0% | 4,03 *(−29,1%)* | **5,41r** *(−34,9%)* | 21,4% |
| 6 | 20.000 | +100% | **+4** | 100,0% | 3,53 *(−37,9%)* | **4,38r** *(−47,3%)* | 14,5% |
| 6 | 30.000 | +200% | **+8** | 100,0% | 2,39 *(−58,0%)* | **3,04r** *(−63,4%)* | **7,0%** |
| 7 | 150.000 | +50% | **+2** | 100,0% | 4,79 *(−20,9%)* | 4,92r *(−23,7%)* | 26,6% |
| 7 | 200.000 | +100% | **+4** | 100,0% | 3,91 *(−35,5%)* | 4,00r *(−38,0%)* | 17,4% |

> [!important] ⚠️ **A vitória não é a métrica aqui — a duração é.** A escada de composição já colapsa acima do rank 5 (achado da oitava rodada), então a vitória satura em 100% no primeiro degrau e não diz mais nada. O que o `B` ilimitado faz é **apagar a cena**: o Clímax de rank 6 cai de **8,31 para 3,04 rodadas** (−63%) e o grupo termina com **93% da Vitalidade intacta** contra 58% no degrau 0. Dois degraus (`+50%` de excesso, perfeitamente alcançável agora que a decisão 218 revogou os tetos) já cortam a cena em um terço.
>
> **Veredito de medição:** o teto em `B 4` da decisão 224 é a escolha certa, e a extensão sem teto **não deve ser publicada como está**. `B` alimenta Vitalidade *e* dano ao mesmo tempo — é a alavanca mais forte do motor, e a própria decisão já suspeitava disso. Se o autor quiser algum reconhecimento mecânico do excesso acima da faixa, a medição sugere um **degrau que toque um eixo só** (Vitalidade *ou* dano, não os dois), ou o caminho que o vault já tem e que não infla nada: **nível de domínio**, que é por Caminho e mede quanto você machuca sem também engordar a barra.

---

### 🛡️ R5 — A face RD do "Nível de Potência": as três variantes falham

> **A decisão 220 já recusou a face RD por derivação, enquanto esta bateria rodava.** Esta seção é a **confirmação empírica** dela: a derivação que a decisão registra está reproduzida abaixo, e o que ela não tinha — o tamanho da inflação assimétrica em cena — está medido. Nenhum número contraria a decisão; todos a apertam.

**Antes de qualquer cena: a variante (ii) sai por aritmética.** Um Nível vale **+1 na média por dado** (d6→d8→d10→d12 sobe a média de 3,5 a 6,5; em d12 o Nível excedente é literalmente +1 por dado). A RD é `base × M`, ou seja **+1 de RD base é −1 por dado atacante**. Com os dois lados escalando igual:

| Níveis | Dano/dado | RD/dado (i) | **Líquido (i)** | RD/dado (ii) | Líquido (ii) |
|---|---|---|---|---|---|
| 0 | 4,5 | 0 | **4,5** | 0 | 4,5 |
| 2 | 6,5 | 2 | **4,5** | 1 | 5,5 |
| 5 | 9,5 | 5 | **4,5** | 2 | 7,5 |

**A (i) simétrica é um no-op exato** — o líquido nunca sai de 4,5/dado, e a regra seria overhead de mesa sem efeito nenhum. **A (ii) é o mesmo no-op em degraus**, sempre atrás do dano e nunca acompanhando-o. Nenhuma das duas precisa de cena para ser descartada.

**O que restou medir é a assimetria.** Como os moldes de inimigo **não** recebem a face (cláusula anti-dupla-contagem: a RD impressa deles já embute o patamar de domínio), a (i) deixa de ser neutra e vira **inflação pura** do lado do PJ. `N` = os Níveis que o motor já calcula (`pc["B"]`, Densidade da Essência): **rank 1 → 0 · rank 3 → 2 · rank 5 → 3**.

**(a) Duração da cena solo — 1 PJ com o Gu de defesa contra a Horda de 8, alvo de 7-9 rodadas:**

| Variante | Rodadas | No alvo (7-9) | **Acima de 9** | Vitória |
|---|---|---|---|---|
| **(iii)** — regra de hoje | 4,3 – 5,5 *(média **4,78**)* | 0/12 | **0/12** | 0,0 – 37,4% |
| **(i)** assimétrica | 4,3 – **10,4** *(média **7,27**)* | 4/12 | **4/12** | 0,0 – 37,4% |

**Resposta a (a): sim, estoura.** A (i) empurra a média de 4,78 para 7,27 rodadas e **passa de 9 em 4 das 12 células** (rank 5 inteiro, com pico de 10,4). E o mais importante: **a faixa de vitória não se move um ponto** — 0,0-37,4% nas duas. A face RD não torna a cena solo ganhável, só a torna longa. É exatamente o pior resultado possível para uma alavanca de duração: o jogador passa mais rodadas perdendo.

**(b) A escada de letalidade da decisão 78 — `d6≈5 · d8≈4 · d10≈3,3 · d12≈2,8`, razão-alvo d6/d12 = 1,79:**

| Alvo | d6 | d8 | d10 | d12 | **d6/d12** | Δ vs 1,79 |
|---|---|---|---|---|---|---|
| rank 1 *(N=0)*, RD 1 — **âncora da 11ª (2,09)** | 6,78 | 4,99 | 3,92 | 3,21 | **2,11** | +0,32 |
| rank 3 *(N=2)* sob **(iii)** — RD 4 | 5,79 | 4,74 | 4,01 | 3,46 | **1,67** | **−0,11** |
| rank 3 *(N=2)* sob **(i)** — RD **12** | 10,39 | 7,44 | 5,79 | 4,71 | **2,21** | **+0,42** |
| rank 5 *(N=3)* sob **(iii)** — RD 16 | 5,46 | 4,62 | 4,00 | 3,53 | **1,55** | −0,24 |
| rank 5 *(N=3)* sob **(i)** — RD **64** | 12,03 | 8,57 | 6,67 | 5,45 | **2,21** | **+0,42** |

**Resposta a (b): a escada NÃO sobrevive, e o tamanho do estrago está quantificado.** O contexto da décima primeira rodada estava certo: `RD × 0,5` melhorava a fidelidade (2,09 → 1,97) porque **menos RD aproxima a razão do alvo**. Subir a RD faz o oposto, e por mais do que a 11ª tinha para descer: a razão vai de **1,67 → 2,21 no rank 3 (+0,54)** e de **1,55 → 2,21 no rank 5 (+0,66)**. Comparando com o eixo da 11ª, `RD × 0,5` movia a razão **−0,12**; a face RD (i) a move **+0,54 a +0,66** — de **quatro a cinco vezes o tamanho do ajuste**, na direção errada. O d6 passa a precisar de **12 acertos** onde a decisão 78 promete 5.

Varredura direta por `N` (rank 3, `M = 4`), para a sessão paralela ler qualquer valor:

| N | RD sob (i) | d6/d12 (i) | RD sob (ii) | d6/d12 (ii) |
|---|---|---|---|---|
| 0 | 4 | 1,67 | 4 | 1,67 |
| 1 | 8 | 1,86 | 4 | 1,67 |
| 2 | 12 | **2,19** | 8 | 1,86 |
| 3 | 16 | **2,74** | 8 | 1,86 |
| 4 | 20 | **3,09** | 12 | 2,19 |
| 5 | 24 | 2,65 *(o piso `M` começa a mascarar)* | 12 | 2,19 |

**(c) A bateria de grupo — ranks 1/3/5, as cinco composições publicadas:**

| Variante | Δ vitória média | Δ máx | Δ rodadas |
|---|---|---|---|
| **(iii)** controle | — | — | — |
| **(i)** assimétrica | **+14,85pp** | **+61,5pp** | −0,44r |

A deriva de composição é total. Sob (i), nos ranks 3 e 5 **todas as cinco composições passam de 96%**, Clímax incluído (rank 3: Difícil 44,7% → **96,5%**, Clímax 87,7% → **99,6%**; rank 5: Padrão pesado 75,9% → **100,0%**). O dial de dificuldade deixa de existir acima do rank 1 — e o rank 1 só sobrevive porque `N = 0` lá.

**Quanto a RD do PJ morde — o número que nenhuma rodada tinha medido:**

| Variante | Rank | RD | Acertos de inimigo na Vitalidade | No piso `M` | **Dano absorvido** |
|---|---|---|---|---|---|
| (iii) | 1 | 1 | 260.595 | 22,9% | 17,7% |
| (iii) | 3 | 4 | 248.569 | 0,0% | 14,6% |
| (iii) | 5 | 16 | 219.507 | 0,0% | **12,6%** |
| **(i)** | 3 | **12** | 236.621 | 2,1% | **43,8%** |
| **(i)** | 5 | **64** | 204.382 | 0,0% | **50,5%** |

> **Cobertura do Gu de defesa: 100% das rodadas, por construção.** A RD do PJ é campo permanente da ficha no motor (`rd = base × M`) e **nunca foi modelada como sustentado que liga e desliga** — nenhuma das quinze rodadas modelou um PJ sem Gu defensivo. Todo número acima é, portanto, o **teto** da inflação. Uma mesa em que o Gu defensivo fica ativo metade do tempo veria metade da deriva — o que ainda é **+7pp de vitória média** e a escada da decisão 78 quebrada nas rodadas em que ele estiver ligado.

> [!important] ⛔ **Veredito: as três variantes falham os guarda-corpos. A face RD não entra — decisão negativa.**
> **(i) simétrica** — no-op aritmético exato: overhead de mesa por zero efeito.
> **(ii)** — o mesmo no-op em degraus, descartada por derivação.
> **(i) assimétrica** *(a que a spec realmente propõe)* — estoura o alvo de 7-9 rodadas em 4 de 12 células **sem melhorar a vitória**, quebra a escada da decisão 78 por +0,54 a +0,66 (quatro a cinco vezes o ajuste que a 11ª tinha na direção certa), e apaga o dial de dificuldade (+14,85pp de média, +61,5pp de máximo).
> **A medição confirma o raciocínio do autor**, que já não queria RD nova por sobrecarga de mesa: a face RD é a única das três faces que **cobra atenção em toda rodada** e, medida, ou não faz nada ou faz demais. **O Nível de Potência entra com duas faces (DANO e o par CD/duração), não com três.**

---

### 🌙 X6 — Xie Lang sem o Físico da Lua Antiga: **ele não cai; ele continua no topo**

**O que muda no motor, item a item.** Das cinco coisas que o Físico dava, **quatro nunca foram efeito de combate**: regeneração violenta, Marcas em dobro na Ascensão, terra Especial garantida e Pressão da Abertura são relógio de campanha, e nenhuma das quinze rodadas as modelou. A quinta — **+1/+2 Níveis de Dano em Lua e Alma** — é efeito de combate real, e **o motor das catorze rodadas anteriores também nunca a modelou** (`nivel_bonus = 0` para todos). Esta rodada corrigiu isso e mediu as três configurações:

| Configuração | Níveis do Físico | `ess_mod` |
|---|---|---|
| **ficha atual** *(o que a [[🎲 A Mesa — Personagens dos Jogadores\|nota da Mesa]] publica)* | +1 *(Abertura Latente)* | 1,25 *(+25% de Caminho duplo)* |
| **motor 1ª–14ª** *(a lacuna histórica)* | 0 | 1,25 |
| **NOVO — sem Físico** | 0 | **1,00** *(Ressonância da Montanha Fria: Lua+Alma como um Caminho só, sem penalidade nenhuma — decisão 216)* |

*A decisão 216 registra que "as taxas de vitória publicadas dele (63% em duelo, 70% contra Elite de rank 3) foram medidas com o físico na ficha e estão desatualizadas — remedição na décima quinta rodada". É esta.*

**A matriz PJ × PJ (placar: média de vitória de cada PJ nos três duelos dele):**

| PJ | rank 1 | rank 3 | rank 5 | | rank 1 | rank 3 | rank 5 |
|---|---|---|---|---|---|---|---|
| | **ficha atual** | | | | **NOVO (sem Físico)** | | |
| **Xie Lang** | **89,1%** | **98,6%** | **99,6%** | | **88,1%** | **97,8%** | **99,5%** |
| Jiāotáng | 68,3% | 54,0% | 48,2% | | 69,9% | 54,3% | 48,2% |
| Demvi | 13,3% | 34,5% | 37,6% | | 13,3% | 34,9% | 37,7% |
| Lee | 29,3% | 12,8% | 14,6% | | 28,7% | 12,9% | 14,6% |

**Bateria de grupo (ranks 1/3/5, as cinco composições): Δ vitória média de −0,28pp, Δ máximo −2,2pp.** Ruído.

> [!important] ✅ **Veredito pedido: NÃO. Ele não cai para o mais fraco dos quatro — ele continua sendo, com folga, o mais forte.**
> A dominância de PvP cai de **89,1 / 98,6 / 99,6%** para **88,1 / 97,8 / 99,5%**: **−1,0 / −0,8 / −0,1 pontos percentuais**. Nos ranks 3 e 5 ele continua vencendo **97,8% e 99,5%** de qualquer duelo, e o segundo colocado (Jiāotáng) continua 44 a 51 pontos atrás. Na bateria de grupo o efeito é **−0,28pp** — indistinguível de ruído de Monte Carlo.
> **A razão é a que a décima quarta já suspeitava, agora confirmada por construção:** a dominância vem do **Caminho da Alma**, não do Físico. O ataque de Alma rola **d12** (o topo da tabela da decisão 78), **ignora RD e armadura por completo**, e mira `10 + VON + rank` em vez da Defesa física — contra os três colegas isso é 3 a 5 pontos de Defesa a menos e uma barra que ninguém mais ataca. Tirar o Físico não toca em nada disso.
> **Consequência direta para a sessão paralela: não é preciso fortalecer o buff do Xie Lang.** O buff substituto proposto (Lua e Alma como um Caminho só) já é, no motor, **um ganho líquido** — apaga o `+25%` de Caminho duplo e devolve ~20% de orçamento de essência por cena, o que compensa sozinho a perda do +1 Nível (o duelo Xie × Lee no rank 1 sobe de 84,3% para 92,6%). **O item aberto da décima quarta continua aberto e não muda de tamanho:** a dominância de PvP do Xie Lang é um problema do Caminho da Alma em duelo, não do Físico da Lua Antiga.

---

### 📌 O que esta rodada devolve ao autor

1. **✅ A CD de Calamidade é a fórmula de [[🌩️ Calamidades e Provações]]** (`14 + 2 × (rank − 6) + faixa + 2 se Provação`). A linha de [[⛈️ A Vontade do Céu]] deve deixar de enunciar CD própria. *(Território da sessão paralela — reportado, não editado.)*
2. **⛔ A face RD do Nível de Potência não entra** — a **decisão 220** já a recusara por derivação; esta rodada confirma com cena e quantifica a inflação assimétrica.
3. **✅ O Xie Lang sem o Físico continua o mais forte da mesa** — não fortalecer a Ressonância da Montanha Fria (decisão 216). As taxas antigas (63% em duelo, 70% contra Elite r3) ficam substituídas pelos números desta seção.
4. **🔴 A escala de escalonamento por excesso é brutal e não-monotônica** — o degrau de +10-25% é mais letal que o de >+50%.
5. **🔴 O `+5 de CD do Físico Extremo` não existe em regra** — só o piso de +15 no Contador, que é +1.
6. **🔴 A escada de CD ultrapassa a ficha** nos ranks 8-9 e nenhuma regra do vault faz a ficha alcançá-la.
7. **🟡 Lacuna de regra:** a nota de Calamidades não diz o que acontece se o dano `M d6` zerar a Vitalidade ou a Alma do personagem no meio da sequência. Medido em 10-52% do pool por evento — chega perto, e vai acontecer na mesa.
8. **⚠️ A extensão retida da decisão 224 (`B` ilimitado, +1 a cada 25% do topo excedido) não deve ser publicada como está** — dois degraus já cortam o Clímax de rank 6 em um terço; oito o cortam em 63%. O teto em `B 4` é a escolha certa.
9. **🟢 Confirmado por construção:** a **Densidade Imortal** da decisão 224 (`B` pelo total de Marcas) e o **nível de domínio** (por Caminho) são de fato eixos separados no motor de tribulação — a etapa 5 soma **domínio**, não Densidade, como as duas notas mandam.

---

## 🌑 Décima sexta rodada — o nerf do Caminho da Alma e o Xie Lang 80:20 *(2026-08-31)*

Duas diretivas do autor, medidas juntas porque são o mesmo eixo visto de dois lados. Script: [[simulacoes/2026-08-31-decima-sexta-nerf-alma.py|_Processo/simulacoes/2026-08-31-decima-sexta-nerf-alma.py]] — cópia do motor da décima quinta, com o módulo de tribulação intacto e não chamado. Semente `20260830`, **3.000 iterações por célula**, mix de Alma "C", treino = 0 dos dois lados (decisão 215).

1. **O Xie Lang é 80:20 Lua:Alma, e as quinze rodadas mediram ele errado.** O motor sempre o modelou como atacante de Alma **puro** (`dado=12, alma_dmg=True`). A ficha de verdade tem **Lua como Caminho principal (~80% dos ataques)** e Alma como secundário (~20%). Lua é **d8**, e o dano dela vai na Vitalidade atravessando a RD normalmente.
2. **Nerfar o Caminho da Alma**, verbatim: *"nerfe o caminho da alma bastante pois ele não atinge o RD, sendo ruim para batalhas em grupo e bom para batalhas solo"*.

> [!warning] ⏳ Duas decisões posteriores mexeram na mesa — o que desta seção continua valendo
> As decisões **232, 233 e 235** foram escritas **depois** desta bateria, e a leitura correta de cada bloco mudou:
>
> | O que | Estado |
> |---|---|
> | **Xie Lang, PvP e solo** | ✅ **Valem** como medição do perfil 80:20. Mas a **decisão 233 deu a ele uma segunda metade de buff** (Golpe Matador misto Lua+Alma sem a dobra de custo de híbrido), *motivada por estes números* e ainda **não medida** — o efeito esperado é na economia de essência, não no dano. |
> | **A inversão Xie × Demvi** *(38,1% e 39,5% nos ranks 3 e 5)* | ✅ Vale, e foi o achado que motivou a decisão 233. A **ordem de força declarada** ali (Demvi fecha a fila) é o alvo de calibragem, não o estado medido. |
> | **Jiāotáng no topo** *(93,5 / 78,3 / 70,3%)* | ✅ Vale, e a decisão 233 **encerrou a questão**: é comportamento pretendido (*"é normal melee ser mais forte antes"*). Sangue+Força não se nerfa. |
> | **Todas as células da Lee** | 🔴 **Obsoletas.** A decisão 232 a tornou **corpo a corpo** e generalizou o multiplicador de melee. Os números de PvP, solo e grupo dela nesta seção são de antes disso. |
> | **O nerf da Alma (a candidata C) e a escada da barra** | ✅ **Intactos.** Nada nas decisões 232-235 toca a barra de Alma, a Defesa contra Alma ou o dado do Caminho — o veredito e os guarda-corpos desta rodada seguem de pé. |
>
> A remedição da Lee e o teste do buff novo do Xie Lang estão **enviados à medição** pela própria decisão 233.

> [!info] A modelagem do 80:20, declarada — é escolha, não dedução
> A cada ataque do Xie Lang o motor rola uma moeda: **80% de chance de um golpe de Lua** (`M d8` contra a Defesa física, RD normal, dano na Vitalidade) e **20% de um golpe de Alma** (`M d12` contra `10 + VON + rank`, sem RD, dano na barra de Alma). A moeda vale para **todo** ataque dele, Golpe Matador incluído. A alternativa (misturar os dois dados no mesmo golpe) foi rejeitada por não existir em regra nenhuma do vault. Com `alma_frac = 1` o motor **não consome rolagem nova**, então o perfil antigo reproduz as rodadas anteriores bit-a-bit — o que a bateria confere.

### 🔴 O achado que reordena tudo: a correção do perfil sozinha desmonta a dominância

| PJ | *perfil errado* r1 / r3 / r5 | **perfil CERTO 80:20** r1 / r3 / r5 | Δ |
|---|---|---|---|
| **Xie Lang** | **83,9% · 97,8% · 99,5%** | **33,4% · 39,9% · 43,6%** | **−50,5 / −57,9 / −56,0pp** |
| Jiāotáng | 70,1% · 54,3% · 48,2% | **93,5% · 78,3% · 70,3%** | +23,4 / +24,0 / +22,1 |
| Lee | 31,4% · 12,9% · 14,6% | 51,2% · 27,4% · 28,7% | +19,8 / +14,4 / +14,0 |
| Demvi | 14,7% · 34,9% · 37,7% | 22,0% · 54,4% · 57,5% | +7,3 / +19,5 / +19,8 |

**O Xie Lang sai do 1º lugar e vira 3º de 4 nos três ranks.** O novo topo da mesa é o **Jiāotáng** (93,5% no rank 1, caindo a 70,3% no rank 5) — alto, mas nunca ~99%, e decrescente com o rank, que é a forma saudável.

> [!note] Por que o baseline aqui é 83,9% e não os 88,1% publicados
> Os 88,1% da décima quinta foram medidos com `ess_mod = 1,0` — a fusão Lua+Alma do buff substituto, que a **decisão 227 reverteu**. Com o `ess_mod = 1,25` do cultivo duplo normal (o estado de hoje), o mesmo perfil errado mede **83,9 / 97,8 / 99,5%**. Ranks 3 e 5 batem em 0,0pp com a décima quinta; só o rank 1 se move, porque é lá que o orçamento de essência aperta. A checagem de reprodução está no script.

> [!important] 📋 Para a ficha da mesa — Xie Lang na configuração nova *(80:20, `ess_mod` 1,25, sem nerf nenhum)*
> Substitui os **88,1 / 97,8 / 99,5%** que a nota da Mesa herdou da décima quinta.
>
> | Xie Lang contra... | rank 1 | rank 3 | rank 5 |
> |---|---|---|---|
> | **Jiāotáng** | 9,8% | 26,1% | 33,6% |
> | **Lee** | 25,0% | 55,5% | 57,7% |
> | **Demvi** | 65,3% | 38,1% | 39,5% |
> | **Média (dominância)** | **33,4%** | **39,9%** | **43,6%** |
>
> Contra o Mestre de Gu solo: **12,7% · 13,8% · 29,2%** (era 63,0 · 71,5 · 86,5% no perfil errado).

### 🎯 O diagnóstico: não é o furo de RD — é a barra

A diretiva do autor culpa o furo de RD. **A medição diz que o furo de RD quase não importa**, e aponta a causa verdadeira. O número que nenhuma das dezesseis rodadas tinha calculado: **quantos acertos zeram a barra de Alma**, o paralelo exato da escada da decisão 78.

| Alvo do golpe | rank 1 | rank 3 | rank 5 | Promessa publicada |
|---|---|---|---|---|
| **Vitalidade**, d12 físico *(escada da decisão 78)* | 3,21 | 3,46 | 3,53 | **≈ 2,8** |
| **Barra de Alma**, d12 de Alma *(regra de hoje)* | **1,85** | **2,12** | **2,21** | — |

A barra de Alma é `(12 + 2×VON + 3×B) × M` contra a Vitalidade `(18 + 3×CON + 4×B) × M` — **um terço menor**, e o golpe que a ataca é o do dado mais alto do jogo. Some a segunda metade da assimetria:

| Alvo | rank | Defesa física | Defesa de Alma | % de acerto vs. Defesa | **% vs. barra de Alma** |
|---|---|---|---|---|---|
| Jiāotáng | 1 | 14 | 12 | 70% | **80%** |
| Jiāotáng | 3 | 18 | 14 | 70% | **90%** |
| Jiāotáng | 5 | 22 | 16 | 70% | **100%** |
| Demvi | 5 | 24 | 18 | 60% | **90%** |

A Defesa de Alma escala **+1/rank** enquanto o acerto do atacante escala **+2/rank**: no rank 5 a barra de Alma do Jiāotáng **não erra nunca**. O furo de RD, por contraste, vale pouco — a RD de um PJ é `1 × M`, que ao lado de um pool `M d12` (média 151,8 no rank 5) é ruído. **É por isso que a candidata A quase não faz nada.**

### 📊 Os três candidatos, medidos contra o especialista de Alma

O nerf é do **Caminho**, não do personagem — vale para os dois lados da mesa (o especial de Alma do molde Mestre de Gu, `1d6 = 6` da decisão 206, recebe o mesmo tratamento). E como o Xie Lang só gasta 20% dos ataques em Alma, a força de cada candidato se lê contra o perfil que a décima quinta mediu: **um especialista, 100% dos ataques em Alma**. É esse perfil que hoje vence 99,5% dos duelos, e é ele que o nerf tem de consertar.

| Candidato | especialista r1 / r3 / r5 | Δ vs. hoje | acertos p/ zerar a barra | Δ na escada |
|---|---|---|---|---|
| **sem nerf** *(hoje)* | 83,9% · 97,8% · **99,5%** | — | 1,85 · 2,12 · 2,21 | — |
| **A** — d12, fura **metade** da RD | 79,7% · 97,2% · **99,3%** | −4,2 / −0,6 / −0,2pp | 1,99 · 2,25 · 2,33 | +0,12 a +0,15 |
| **B** — **d10**, fura tudo | 76,1% · 96,4% · **98,8%** | −7,7 / −1,4 / −0,7pp | 2,19 · 2,40 · 2,47 | +0,26 a +0,34 |
| **C** — barra `(16+3×VON+3×B)×M` e Defesa **+2/rank** | **62,1% · 85,0% · 87,1%** | **−21,8 / −12,8 / −12,4pp** | **2,47 · 2,59 · 2,63** | **+0,42 a +0,62** |
| *C_bar* — só a barra maior | 67,5% · 94,4% · 98,7% | −16,4 / −3,4 / −0,8pp | 2,47 · 2,59 · 2,63 | idem C |
| *C_def* — só a Defesa +2/rank | 80,3% · 92,5% · 93,7% | −3,6 / −5,4 / −5,8pp | 1,85 · 2,12 · 2,21 | 0 |

**A e B falham o teste, e falham pelo mesmo motivo aritmético.** A metade de uma RD `1 × M` continua sendo um número pequeno ao lado de um pool `M d12`; e `d12 → d10` é −16% de dano numa barra que precisa de ~2 acertos, o que muda 2,12 para 2,40 e não muda quem ganha. As duas deixam o especialista em **96-99% nos ranks 3 e 5** — a métrica de sucesso pedida (*nenhum PJ vence ~99% dos duelos*) continua reprovada.

**A C é a única que move a agulha, e as duas metades dela são complementares, não redundantes:** a `C_bar` carrega a escada inteira e o corte de rank 1; a `C_def` carrega o corte dos ranks 3 e 5, porque é ela que conserta a Defesa que ficava 1 ponto por rank atrás do acerto. Nenhuma sozinha basta (`C_bar` deixa 98,7% no rank 5; `C_def` deixa 93,7%); juntas, entregam.

### 🛡️ Os guarda-corpos

**A escada de letalidade da decisão 78 (`d6≈5 · d8≈4 · d10≈3,3 · d12≈2,8`) sai intacta das candidatas A e C** — nenhuma das duas troca um dado, então nenhuma linha da Tabela de Letalidade se move.

**A candidata B move a escada de propósito, e é preciso dizê-lo:** ela tira o Caminho da Alma da coluna d12 e o põe na d10, de **≈2,8 para ≈3,3 acertos** contra Vitalidade equivalente. Espada e Relâmpago ficariam sozinhos no topo d12 — o que é defensável (eles pagam "nenhum efeito colateral" pelo mesmo dado), mas é uma reescrita da tabela publicada em troca de −0,7pp de dominância no rank 5. Preço alto, entrega nula.

**A C aproxima a Alma da própria promessa da escada** em vez de afastá-la: de 2,21 para **2,63** acertos no rank 5, contra os 2,8 que a decisão 78 promete ao degrau d12. A folga que sobra (2,63 contra 2,8) é o preço justo de um Caminho que continua furando RD por completo — e cuja contrapartida medida é ser fraco em grupo.

**As faixas de composição não se movem em candidato nenhum.** Faixas publicadas: Fácil ≈ 100% · Padrão 75-99% · Difícil ~40-52% · Clímax 56-87%.

| Candidato | Δ vitória média do grupo | Δ máx | Δ rodadas | Quinhão de dano do Xie r1/r3/r5 |
|---|---|---|---|---|
| sem nerf | — | — | — | 9% · 10% · 12% |
| **A** | −0,06pp | +1,0 | +0,00r | 9% · 10% · 12% |
| **B** | +0,05pp | −2,1 | −0,00r | 9% · 10% · 12% |
| **C** | **+0,24pp** | +2,5 | −0,01r | 9% · 10% · 12% |

**A promessa "o nerf não pode piorar Alma em grupo" está cumprida por medição**, e com folga: o quinhão de dano do Xie Lang na cena de grupo é idêntico nos três candidatos até a casa inteira. O motivo é o achado da décima rodada visto do outro lado — em cena de grupo o Caminho da Alma **já** contribui pouco (9-12% do dano da mesa, contra os 25% de uma divisão par), e mexer no tamanho da barra alheia não muda isso, porque o gargalo nunca foi o dano por golpe, e sim o fato de o golpe cair num trilho que mais ninguém ataca. Corolário útil: no perfil errado, **38-52% do dano do Xie ia para uma barra que ninguém mais tocava**; no 80:20 correto essa perda cai para **9-15%**.

**A bateria solo** (cada PJ × 1 Mestre de Gu, 2 ações/rodada) — a cena em que Alma deve brilhar:

| Candidato | Xie Lang r1/r3/r5 | Jiāotáng | Lee | Demvi |
|---|---|---|---|---|
| sem nerf | 12,7% · 13,8% · 29,2% | 59,1 · 37,3 · 46,0% | 5,3 · 5,4 · 17,4% | 15,3 · 24,9 · 47,2% |
| **A** | 11,7% · 13,7% · 28,8% | *inalterado* | *inalterado* | *inalterado* |
| **B** | 10,0% · 11,4% · 28,5% | 59,0 · 35,4 · 47,8% | ±0,2pp | ±0,5pp |
| **C** | **8,9% · 9,8% · 24,4%** | 59,5 · 37,4 · 47,7% | ±0,5pp | ±0,5pp |

A C custa ao Xie Lang **−3,8 / −4,0 / −4,8pp** no solo e não toca os outros três (tudo dentro de ±0,5pp, ruído). É o preço real do nerf, e ele cai onde deve: sobre quem usa o Caminho.

### ⚖️ Os empilhamentos, para o autor que quiser mais

Como só a C move a agulha sozinha, só empilhamento **sobre** a C valia medir:

| Config | especialista r1 / r3 / r5 | acertos p/ zerar a barra |
|---|---|---|
| **C** | 62,1% · 85,0% · 87,1% | 2,47 · 2,59 · **2,63** |
| **C + A** *(barra dura **e** meia RD)* | 56,0% · 82,5% · 85,0% | 2,66 · 2,75 · **2,78** |
| **C + B** *(barra dura **e** d10)* | 48,5% · 78,4% · 79,3% | 2,92 · 2,94 · **2,94** |

O **C + A** encosta a Alma **exatamente** nos 2,8 da decisão 78. O custo é textual e pesa: o vault perde a frase *"a resposta estrutural à RD alta é o dano de Alma"* ([[⚔️ Combate]], seção de RD), que é um pilar de desenho — é ela que garante que um inimigo de rank acima não **desligue** metade da mesa sem contrapartida. O **C + B** passa dos 2,8 e cai no degrau d10 sem estar lá. Por isso a recomendação aplicada é a **C pura**, com o C + A registrado como alavanca de uma linha caso o autor queira o ajuste fino.

> [!warning] O 80:20 do Xie Lang é um **piso**, não o valor verdadeiro
> O motor **nunca modelou controle vindo de PJ** — só especiais de inimigo aplicam Lentidão. E a Tabela de Letalidade paga o degrau d8 exatamente com isso: *"dano constante mais atrito real… é o perfil que ganha lutas longas"*. Ou seja, os 80% de Lua do Xie Lang rendem, no motor, só o dado — nenhuma das vantagens pelas quais o d8 é d8. Bracketing medido, ligando o atrito para **todo** atacante d8 da mesa (a Lua dele **e** o Lee):
>
> | Atrito de Lua | Xie Lang r1 / r3 / r5 |
> |---|---|
> | 0% *(o motor de hoje)* | 33,4% · 39,9% · 43,6% |
> | 33% dos acertos | 37,1% · 49,1% · 54,5% |
> | 67% dos acertos | 40,0% · 59,6% · 63,9% |
>
> A faixa real dele está entre o piso e ~54% no rank 5. **Em nenhum ponto do intervalo ele é dominante, e em nenhum ponto ele é o mais fraco** — o que sustenta as duas metades da métrica de sucesso pedida.

> [!important] ✅ Veredito: **candidata C aplicada.** A e B recusadas por medição
> **A** (meia RD) e **B** (d10) são nerfs no papel e não no número: deixam o especialista de Alma em **96-99%** nos ranks 3 e 5, contra os 99,5% de hoje. A **B** ainda cobra a reescrita de uma linha da Tabela de Letalidade por −0,7pp.
> **C** leva o especialista de **99,5% para 87,1%** no rank 5 (−12,4pp) e de 83,9% para 62,1% no rank 1 (−21,8pp); leva a barra de Alma de **2,21 para 2,63 acertos**, quase encostando nos 2,8 da decisão 78; **não toca dado nenhum**, então a Tabela de Letalidade sai intacta; e custa **+0,24pp** de vitória média na bateria de grupo, com o quinhão de dano do Caminho em cena de grupo **inalterado**.
> **A causa foi corrigida onde ela estava.** A diretiva culpava o furo de RD; a medição mostra que o furo vale +0,12 acerto e que a dominância vinha de uma **barra um terço menor que a Vitalidade, defendida por um número que crescia metade do que crescia o acerto que a atacava**. A C ataca exatamente esses dois.

### 📌 O que esta rodada devolve ao autor

1. **✅ O Xie Lang corrigido é 33,4 / 39,9 / 43,6%** em PvP — 3º de 4 nos três ranks. Os **88,1 / 97,8 / 99,5%** da nota da Mesa e do [[🧭 Log de Decisões]] estão obsoletos por dois motivos somados (perfil errado **e** `ess_mod` da decisão 227).
2. **✅ O novo topo da mesa é o Jiāotáng** (93,5 / 78,3 / 70,3%). Alto no rank 1, decrescente com o rank — nunca ~99%. Não pede ação, mas a mesa deve saber.
3. **🔧 Aplicado em [[⚔️ Combate]]:** a Defesa de Alma passa a `10 + VON + 2 × rank` e a Tabela de Letalidade registra a barra endurecida como a contrapartida do d12 que fura tudo.
4. **🔴 Ripple obrigatório — a fórmula da Alma máxima está publicada em oito lugares.** A nova é `(16 + 3 × VON + 3 × B) × M`. Precisam republicar: [[❤️ Recursos e Dano]] *(o dono da fórmula)*, [[📄 Folha de Referência]], [[🎓 Guia do Mestre Iniciante]] *(2 ocorrências)*, [[📋 Guia de Criação de Ficha]] *(2, uma delas exemplo calculado)*, [[🎲 Mão do Jogador — Pacote Discord]], [[🗺️ Mapa do Vault]] e a nota da Mesa. **Nada disso foi editado aqui** — a nota da Mesa e a pasta `02` estavam com a sessão paralela durante esta rodada.
5. **🔴 Território da sessão paralela — [[👻 Caminho da Alma]] precisa de duas correções:** a Defesa citada na regra "**1. Atravessa**" e na ficha do *Gu da Agulha Espectral* vira `10 + VON + 2 × rank`; e o exemplo do próprio Gu da Agulha (*"a barra de Alma de um lutador de VON 0 no rank 3 são 48 pontos"*) passa a **56** sob a fórmula nova. A escada de Força de Alma (multiplicadores ×1 a ×4) **não** muda — ela multiplica a Alma máxima, qualquer que seja a fórmula.
6. **🟡 O C + A é uma alavanca de uma linha, medida e não aplicada** — encosta a escada da Alma nos 2,8 exatos, ao custo de o Caminho deixar de ser "a resposta estrutural à RD alta".
7. **⚠️ Lacuna de modelagem confirmada e quantificada, não fechada:** o motor não dá controle nenhum a PJ, e é exatamente disso que o degrau d8 vive. Todo número de Caminho d8 nas dezesseis rodadas (Lua, Gelo, Sangue, Veneno, Sombras, Água, Luz, Escravidão) é um **piso**. Modelar isso é uma rodada própria.

---

## ⚒️ Décima sétima rodada — a Lee em corpo a corpo e a isenção do Xie Lang *(2026-09-01)*

Duas diretivas de **ficha** (não de regra genérica), medidas juntas. Script: [[simulacoes/2026-09-01-decima-setima-lee-melee-xie-buff.py|_Processo/simulacoes/2026-09-01-decima-setima-lee-melee-xie-buff.py]] — cópia do motor da décima sexta. Semente `20260830`, **3.000 iterações por célula**, mix de Alma "C", treino = 0 dos dois lados (decisão 215). **O baseline já embute a decisão 231** (candidata C do nerf de Alma **aplicada**) e a decisão 227 (`ess_mod` do Xie Lang = 1,25).

1. **A Lee vira corpo a corpo** — *"a Lee tmb vai ser melee, ela usará uma **foice** e complementará com Gu de suporte ou Gu de ataque melee dos elementos wu xing"*.
2. **O Xie Lang ganha a isenção de custo de híbrido** (decisão 233), para ver se ela reverte a inversão contra o Demvi.

**Reprodução conferida:** o baseline desta rodada bate com a décima sexta em **0,0pp nas doze células** de PvP e **célula a célula** na bateria de grupo. O que muda daqui em diante é mudança de verdade.

### 🧭 A modelagem da Lee, declarada — os números saíram do Catálogo

[[⚔️ Combate]] fecha o melee em `Dano melee = (M do Gu) d(dado da arma, ajustado por Níveis) + FOR + (M × B)`. A arma é a **foice** (pesada, `d10`), o atributo de ataque vira **FOR +3** (o valor é o mesmo do VON +3 que ela usava, então **o acerto não muda** — o que muda é o `+ FOR` fixo no dano), e os Níveis vêm da escada de Gu **🔨 amplifica** dos cinco elementos, lida rank a rank no [[📖 Catálogo de Gu]]:

| Rank | Gu 🔨 amplifica do Catálogo | Níveis | Foice `d10` + Níveis | O que o Catálogo escreve |
|---|---|---|---|---|
| 1 | Palma d'Água · Brasa no Punho · Punho de Seixo | **+1** | `1d12 + FOR` | — |
| 2 | **Gu do Manto de Carvão** (Fogo) | **+2** | `2d12 + 2 + FOR` | *"arma média (d8) sobe dois tipos: `2d12 + FOR`"* |
| 3 | **Gu do Punho de Montanha** (Terra) | **+2** | `4d12 + 4 + FOR` | *"arma pesada (d10) sobe um tipo e ganha o resto por dado: **`4d12 + 4 + FOR`**"* |
| 4 | **Gu da Fornalha nas Veias** (Fogo) | **+3** | `8d12 + 16 + FOR` | *"…os dois Níveis restantes viram +2 por dado: **`8d12 + 16 + FOR`**"* |
| 5 | **Gu do Trono de Terra** (Terra) | **+4** | `16d12 + 48 + FOR` | *"…os três Níveis restantes viram +3 por dado: **`16d12 + 48 + FOR`**"* |

Passada pelo `apply_niveis` do motor (decisão 79: sobe o tipo até d12, depois +1 por dado), a foice com esses Níveis **reproduz literalmente as três linhas que o Catálogo publica**. Nada foi inventado. A Densidade da Essência (`M × B`) entra por cima, como manda a fórmula. **`role="healer"` fica intacto** — a cura (`M d6`, uma vez por cena, decisão 155) continua na ficha.

> [!warning] Esta leitura é o **TETO**, e a rodada mede o piso junto
> Todos esses Gu têm condição pesada — Punho de Montanha e Trono de Terra exigem **os dois pés em solo natural** (*"no ar, sobre pedra trabalhada, assoalho, telhado, barco ou metal, o Gu não pega nada"*), a Fornalha cobra `1 × M` de Vitalidade a cada 2 rodadas, o Trono é **deslocamento 0**. O motor não modela posição nem terreno para ninguém. Por isso toda tabela abaixo traz também o **piso**: a *foice crua*, sem Nível nenhum — que é exatamente o tratamento que o Jiāotáng recebe há dezesseis rodadas.

### 🔴 O achado que domina a rodada: o motor só modela os Níveis de ficha DA LEE

Dezesseis rodadas rodaram com `nivel_bonus = 0` para os quatro. Ao dar à Lee a escada do Catálogo, ela ganha uma coisa que **o Jiāotáng também tem na ficha e nunca recebeu** — [[💪 Caminho da Força]] traz o *Gu do Tendão de Búfalo* (rank 2, **+1 Nível**), a *Gu da Mão de Pedra* (rank 3, **+1 permanente**) e o *Gu do Tirano de Mil Jin* (rank 4, **+2 Níveis**, sustentado até o rank 5) — e isso ainda é piso para ele, porque a **Descarga do Ímpeto soma +3 Níveis** a 5 de Ímpeto.

| Configuração | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| **como o motor roda hoje** *(só a Lee com escada)* | Jiāotáng 85,9 > **Lee 71,0** > Xie 24,7 > Demvi 18,4 | Jiāotáng 68,7 > **Lee 67,4** > Demvi 43,9 > Xie 20,0 | **Lee 75,5** > Jiāotáng 57,7 > Demvi 45,1 > Xie 21,7 |
| **paridade** *(os dois com a escada da ficha)* | Jiāotáng 85,9 > Lee 71,0 > Xie 24,7 > Demvi 18,4 | **Jiāotáng 75,9** > Lee 64,1 > Demvi 41,6 > Xie 18,3 | **Jiāotáng 74,6** > Lee 67,4 > Demvi 39,8 > Xie 18,2 |

**A ultrapassagem da Lee sobre o Jiāotáng no rank 5 é artefato de modelagem, não propriedade da ficha.** Com os dois recebendo o que a ficha deles concede, o Jiāotáng **lidera nos três ranks** e a dianteira dele encolhe como o autor pediu: **+14,9 → +11,8 → +7,2pp** sobre o segundo colocado.

### 📊 A matriz de PvP com as duas mudanças ligadas

Braço A = o motor de sempre (sem Golpe Matador no duelo). Legenda do critério: **D✔** = o Demvi fecha a fila · **J✔** = o Jiāotáng lidera.

| PJ | baseline de hoje *(Lee conjuradora)* | **Lee melee — TETO** | **Lee melee — PISO** |
|---|---|---|---|
| **Jiāotáng** | 94,8 · 81,3 · 73,7% | 85,9 · 68,7 · **57,7%** | 88,1 · 75,9 · 69,6% |
| **Lee** | 53,0 · 29,7 · 32,1% | **71,0 · 67,4 · 75,5%** | 68,0 · 49,3 · 44,5% |
| **Demvi** | 22,9 · 57,1 · 60,9% | 18,4 · 43,9 · 45,1% | 18,9 · 50,5 · 57,3% |
| **Xie Lang** | 29,3 · 31,8 · 33,2% | 24,7 · **20,0 · 21,7%** | 24,9 · 24,3 · 28,5% |
| **critério** | r1 D✔J✔ · r3 D✘J✔ · r5 D✘J✔ | r1 D✔J✔ · r3 D✘J✔ · **r5 D✘J✘** | r1 D✔J✔ · r3 D✘J✔ · r5 D✘J✔ |

**A Lee sai do fundo da mesa.** Ela era **última** nos ranks 3 e 5 (29,7% e 32,1%); vira segunda no piso e primeira-ou-segunda no teto. Isso era o buraco maior da tabela e ele fechou.

**Mas o critério do autor continua reprovado nos ranks 3 e 5 — e o culpado é o Xie Lang, não a Lee nem o Demvi.** Em toda configuração medida, quem fecha a fila nos ranks altos é **o Xie Lang**, não o Demvi.

### ⚖️ A isenção do Xie Lang: ela não pode fazer o que se pediu dela

**A conta da isenção está certa e reproduz o número do autor.** [[⚡ Golpes Matadores]] fecha o custo em `(soma das ativações) × (nº de Gu) × 2 se híbrido`, e o motor escreve isso como `40 × n_gu² × 2`:

| rank | `B` | Gu no combo | custo hoje | **com a isenção** | dial ×1,5 | tanque do Xie | % do tanque hoje → com isenção |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 2 | 320 | **160** | 240 | 344 | 93% → **47%** |
| 2 | 1 | 3 | 720 | **360** | 540 | 688 | 105% → **52%** |
| 3 | 2 | 4 | **1.280** | **640** | 960 | 1.376 | 93% → **47%** |
| 4-5 | 3 | 5 | 2.000 | **1.000** | 1.500 | 2.752 | 73% → **36%** |

Os **1.280 → 640** do autor caem exatos na linha do rank 3. **`ess_mod` não foi tocado — segue 1,25.**

> [!important] 🔴 O achado central: **o Golpe Matador nunca dispara num duelo PJ × PJ**
> O gatilho do motor é `boss is not None`, e `run_duel` passa `None` — **dezesseis rodadas de PvP foram medidas sem Golpe Matador nenhum**. Consequência aritmética: com o motor como está, a isenção é um **no-op exato na matriz de PvP**. Não "quase nada": **0,0pp em todas as doze células**, por construção.
>
> E o motor está **certo**, porque a regra está do lado dele. [[⚡ Golpes Matadores]], seção *"Contra quem vale disparar"*: contra **Chefe ou inimigo de rank acima**, sim; contra **"Guerreiro, Mestre de Gu, Recruta, horda"**, ***"Não. Ataque normal duas vezes rende mais e deixa o tanque cheio."*** Um par de rank igual está do lado errado dessa linha.

Medida a isenção nos **três lugares onde ela pode aparecer**:

| Onde | Δ da isenção | Δ do dial ×1,5 |
|---|---|---|
| **Matriz de PvP** *(braço A, o motor de sempre)* | **0,0 / 0,0 / 0,0pp** — no-op por construção | 0,0 / 0,0 / 0,0pp |
| **Cena de Clímax** *(grupo × Chefe — a única composição publicada em que o golpe dispara)* | **+0,83 / −1,03 / +0,23pp** | +0,87 / −0,23 / +0,00pp |
| **Duelo com o golpe forçado a disparar** *(escolha de modelagem, ver abaixo)* | +1,8 / +10,9 / +0,1pp | — |

E o terceiro braço traz a sua própria lição. Forçando o golpe a sair no duelo (com o teste de conjuração corrigido, ver o achado colateral), o Xie Lang **desaba**: de 24,7 · 20,0 · 21,7% para **16,6 · 0,1 · 10,3%** sem a isenção, e **18,4 · 10,9 · 10,4%** com ela. O motivo é a Retaliação: falhar a conjuração deixa todos os Gu do combo inutilizáveis pelo resto da cena, e ele passa o duelo batendo com dano cru. **A isenção conserta parte de uma ferida que só existe porque o golpe foi disparado no lugar errado** — e mesmo consertada, ele fica muito abaixo de onde estava sem disparar nada.

O par que motivou a decisão 233, medido nos três braços *(vitória do Xie Lang, normalizada)*:

| Xie Lang × Demvi | rank 1 | rank 3 | rank 5 |
|---|---|---|---|
| décima sexta *(sem o nerf de Alma)* | 65,3% | 38,1% | 39,5% |
| **hoje** *(com a candidata C aplicada)* | 62,4% | **29,8%** | **29,2%** |
| com a isenção, braço A | 62,4% | **29,8%** | **29,2%** |
| com a isenção, golpe forçado no duelo | 51,0% | 15,3% | 13,0% |

> [!warning] ❌ **A resposta à pergunta do autor é NÃO — e o motivo não é de calibragem, é de eixo**
> A isenção **não reverte** a inversão contra o Demvi. Ela não move a agulha em lugar nenhum do PvP, e move ±1pp na única cena publicada onde ela existe.
>
> **A razão está medida e é simples: a essência nunca foi a restrição do Xie Lang num duelo.** No rank 3 ele tem **27 ações** de tanque e no rank 5, **55** — contra um duelo de no máximo 20 rodadas. Ele nunca seca. O gargalo que a decisão 233 diagnosticou (*"quantas vezes por cena conseguia pagar a jogada boa"*) **é real na cena de Chefe e inexistente no duelo**, que é justamente onde o número que motivou o buff foi lido.
>
> **O dial de ×1,5 não salva:** ele mexe no mesmo eixo inerte, e mede **0,0pp** no PvP. Não é uma questão de a isenção ser forte ou fraca demais — é de estar na dimensão errada do problema.

### 🎯 O que faria o critério fechar — e não é regra nova

A décima sexta deixou registrado (item ⚠️) que o motor **não dá controle nenhum a PJ**, e que é exatamente disso que o degrau d8 vive pela Tabela de Letalidade (*"dano constante mais atrito real… o perfil que ganha lutas longas"*). **80% dos ataques do Xie Lang são d8 de Lua.** Novidade desta rodada: com a Lee em d10/d12, **ele é o único d8 da mesa** — o knob deixou de ser ambíguo e mede só a Lua dele.

| Atrito de Lua | rank 1 | rank 3 | rank 5 | Xie × Demvi (r3 · r5) |
|---|---|---|---|---|
| **0%** *(o motor de hoje)* | Jiāotáng 85,9 > Lee 71,0 > Xie 24,7 > Demvi 18,4 | Jiāotáng 68,7 > Lee 67,4 > Demvi 43,9 > **Xie 20,0** | Lee 75,5 > Jiāotáng 57,7 > Demvi 45,1 > **Xie 21,7** | 29,8% · 29,2% |
| **33%** | Jiāotáng 85,0 > Lee 69,8 > Xie 27,9 > Demvi 17,4 | Jiāotáng 63,6 > Lee 62,4 > Demvi 39,6 > Xie 34,5 | Lee 71,0 > Jiāotáng 51,9 > Demvi 40,3 > Xie 36,8 | 43,0% · 43,7% |
| **67%** | Jiāotáng 83,5 > Lee 68,3 > Xie 32,4 > **Demvi 15,9** | Jiāotáng 57,0 > Lee 55,8 > Xie 52,4 > **Demvi 34,8** | Lee 65,0 > Xie 53,9 > Jiāotáng 45,2 > **Demvi 35,9** | **57,2% · 56,6%** |

E a célula que fecha tudo — **as duas lacunas de modelagem tapadas ao mesmo tempo** (a Lee com a escada Wu Xing, o Jiāotáng com a escada de Força, e o atrito de Lua em ⅔):

| rank | ordem medida | critério |
|---|---|---|
| **1** | **Jiāotáng 83,5%** > Lee 68,3% > Xie Lang 32,4% > **Demvi 15,9%** | ✅ D✔ J✔ |
| **3** | **Jiāotáng 65,7%** > Lee 52,5% > Xie Lang 49,3% > **Demvi 32,5%** | ✅ D✔ J✔ |
| **5** | **Jiāotáng 64,3%** > Lee 56,9% > Xie Lang 48,2% > **Demvi 30,7%** | ✅ D✔ J✔ |

**É a única configuração medida em que o critério do autor fecha nos três ranks** — o Demvi fechando a fila, os outros três acima dele, o Jiāotáng liderando com a dianteira encolhendo (**+15,2 → +13,2 → +7,4pp**). E **nenhuma das duas peças é mudança de regra**: as duas são coisas que as fichas publicadas já concedem e que o motor nunca leu.

### 👥 A bateria de grupo — a Lee melee mexe a tabela de composição, e muito

As 5 composições publicadas × ranks 1/3/5. 🚩 marca movimento > 3pp.

| Composição | baseline *(Lee conjuradora)* | **Lee melee — TETO** | Δ | **Lee melee — PISO** | Δ |
|---|---|---|---|---|---|
| **Fácil** | 100 · 100 · 100% | 100 · 100 · 100% | +0,0 / +0,0 / +0,0 | 100 · 100 · 100% | +0,0 / +0,0 / +0,0 |
| **Padrão** | 93,2 · 87,6 · 99,2% | 98,1 · 95,6 · 99,8% | 🚩+4,9 / 🚩+7,9 / +0,6 | 97,6 · 92,2 · 98,8% | 🚩+4,4 / 🚩+4,6 / −0,4 |
| **Padrão pesado** | 69,1 · 60,2 · 84,9% | 82,7 · 77,9 · 94,0% | 🚩+13,6 / 🚩+17,7 / 🚩+9,1 | 80,8 · 70,4 · 86,8% | 🚩+11,6 / 🚩+10,2 / +2,0 |
| **Difícil** | 32,6 · 51,1 · 45,8% | 59,5 · 71,8 · 71,3% | 🚩+26,8 / 🚩+20,8 / 🚩+25,5 | 55,5 · 61,5 · 46,2% | 🚩+22,9 / 🚩+10,4 / +0,4 |
| **Clímax** | 3,6 · 87,4 · 90,7% | 16,0 · 96,5 · 97,5% | 🚩+12,4 / 🚩+9,1 / 🚩+6,8 | 11,3 · 93,1 · 92,4% | 🚩+7,7 / 🚩+5,6 / +1,7 |
| | | | **média +10,35pp · máx +26,8pp** | | **média +5,41pp · máx +22,9pp** |

**🔴 As faixas publicadas não seguram no teto.** *Padrão pesado* sai da faixa **53-77%** para **78-94%**; *Difícil* sai de **~40-52%** para **60-72%**. **Doze das quinze células andam mais de 3pp**, e a maior anda **+26,8pp**. No piso o quadro é bem mais brando — no **rank 5 o movimento inteiro cabe em ±2pp** — mas os ranks 1 e 3 ainda estouram.

**A leitura honesta é que a tabela de composição precisa ser remedida depois que a paridade de Níveis for resolvida**, e não agora: metade deste salto é a Lee ganhando o que a ficha dela dá, e a outra metade é os outros três continuarem sem o que as fichas deles dão. Republicar a tabela em cima de uma mesa meio-modelada seria assar o artefato dentro da regra.

*(Nota de leitura: o baseline reproduz a décima sexta exatamente, incluindo o Clímax de rank 1 em **3,6%**, que já estava fora da faixa publicada de 56-87% antes desta rodada. A faixa vem de calibragens anteriores ao 80:20 e ao nerf de Alma.)*

### ⚔️ A bateria solo — onde o corpo a corpo põe a Lee

Cada PJ × 1 Mestre de Gu (2 ações/rodada), ranks 1/3/5.

| PJ | baseline | **Lee melee — TETO** | **Lee melee — PISO** |
|---|---|---|---|
| Xie Lang | 8,9 · 9,8 · 24,4% | *inalterado* | *inalterado* |
| Jiāotáng | 59,5 · 37,4 · 47,7% | *inalterado* | *inalterado* |
| **Lee** | **5,3 · 5,8 · 18,2%** | **36,6 · 30,7 · 61,7%** | **29,8 · 16,5 · 26,7%** |
| Demvi | 15,3 · 24,6 · 48,2% | *inalterado* | *inalterado* |

**A Lee sai do último lugar da mesa na cena solo.** Ela tinha o pior número dos quatro em todos os ranks (5,3 · 5,8 · 18,2%); no teto ela vira **a melhor do grupo no rank 5** (61,7% contra os 48,2% do Demvi), e no piso ela fica em pé de igualdade com os outros nos ranks 1 e 5, ainda atrás no 3. É a mesma história do PvP: o corpo a corpo conserta o buraco, e o teto passa do ponto.

### 🔍 Achado colateral — o teste de conjuração do motor não é o publicado

Descoberto ao fazer o Golpe Matador disparar num duelo pela primeira vez em dezessete rodadas. [[⚡ Golpes Matadores]] publica `Teste = d20 + AST + nível de domínio no Caminho do núcleo`, com **−4 se o golpe está registrado na ficha** (*"a sequência é treinada"*), e a nota diz por extenso: ***"um golpe registrado, treinado e usado em condições decentes passa quase sempre. O teste existe pra punir improviso e pressão."***

O motor rola **`d20 + AST` e mais nada** — sem o nível de domínio e sem o −4.

| rank | CD | motor | **regra publicada** |
|---|---|---|---|
| 1 | 16 | 35% | **55%** |
| 3 | 20 | 15% | **45%** |
| 5 | 22 | **5%** | **40%** |

**No rank 5 o motor transforma o Golpe Matador numa loteria de 5%** — o oposto exato do que a regra promete. O achado nunca apareceu porque o gatilho é `boss is not None` e o golpe só é modelado na composição de Clímax, onde o impacto do conserto é pequeno (**+0,9 / +0,0 / +0,3pp**). **Nada foi aplicado** — o conserto é uma linha do motor, e vai para "Em aberto".

### 📌 O que esta rodada devolve ao autor

1. **✅ A Lee em corpo a corpo conserta o buraco dela, e conserta grande.** Em PvP ela sai de **última** nos ranks 3 e 5 (29,7 · 32,1%) para **67,4 · 75,5%** no teto e **49,3 · 44,5%** no piso; na cena solo, de **5,3 · 5,8 · 18,2%** para **36,6 · 30,7 · 61,7%** (teto) ou **29,8 · 16,5 · 26,7%** (piso). A modelagem saiu inteira do [[📖 Catálogo de Gu]] e reproduz as linhas publicadas do Punho de Montanha, da Fornalha nas Veias e do Trono de Terra.
2. **❌ A isenção do Xie Lang NÃO reverte a inversão contra o Demvi, e não pode.** **0,0pp em todas as doze células de PvP**, porque o Golpe Matador não dispara em duelo — e a regra concorda com o motor (*"Guerreiro, Mestre de Gu… Não"*). Onde ela existe de fato, a cena de Clímax, ela vale **+0,83 / −1,03 / +0,23pp**. **O dial de ×1,5 mede exatamente o mesmo nada** — o eixo do custo é inerte no duelo, porque no rank 3 ele tem 27 ações de tanque e no rank 5, 55.
3. **🔴 O critério do autor está reprovado nos ranks 3 e 5 — e quem fecha a fila é o Xie Lang, não o Demvi.** Em toda configuração medida sem atrito de Lua.
4. **🎯 A alavanca que faz o critério fechar está medida, e não é regra nova — são duas lacunas de modelagem.** Com a paridade de Níveis (o Jiāotáng recebendo a escada do [[💪 Caminho da Força]] que a Lee agora recebe do Wu Xing) **e** o atrito do degrau d8 em ⅔, o critério fecha **nos três ranks**: Jiāotáng 83,5 / 65,7 / 64,3% liderando com dianteira encolhendo (+15,2 → +13,2 → +7,4pp), e o **Demvi em último nos três** (15,9 / 32,5 / 30,7%). Modelar as duas é uma rodada própria.
5. **🔴 A tabela de composição de [[⚔️ Ameaças Genéricas por Rank]] não sobrevive à Lee melee como está** — 12 de 15 células andam > 3pp, *Padrão pesado* vai de 53-77% para 78-94% e *Difícil* de ~40-52% para 60-72%. **Não republicar agora:** metade do salto é a Lee ganhando o que a ficha dá e a outra metade é os outros três seguirem sem o que as fichas deles dão. Remedir depois da paridade.
6. **⚠️ Achado colateral, não aplicado:** o teste de conjuração do motor omite o nível de domínio e o −4 de golpe registrado, fazendo do Golpe Matador de rank 5 uma loteria de 5% contra os 40% da regra escrita. Impacto no Clímax: +0,9 / +0,0 / +0,3pp.
7. **🟡 Se o autor quiser o Xie Lang consertado por ficha e não por modelagem**, o eixo tem de ser **o ataque, não o custo** — a isenção continua valendo pela ficção e pela cena de Chefe, mas ela não é a peça que move o PvP.

---

## ☯️ Marcas de Dao no topo — a escada linear já entrega o veredito da ficção? *(2026-08-31)*

Pendência testada: item de "Em aberto" no [[🧭 Log de Decisões]] apontando que a escada de domínio de [[☯️ Marcas de Dao]] (convertida em `01 — Fundação/⚔️ Combate.md#☯️ Marcas de Dao — o dano depois do rank 6`) é uma progressão em degraus (+1 de `B` por patamar, um único dobramento de pool no topo) enquanto o romance descreve a amplificação por Marca, no rank 8, como saltando para multiplicadores de "centenas ou milhares de vezes" — dado como a explicação canônica de por que rank 7 quase nunca vence rank 8.

### Verificação da citação canônica (grep na fonte primária, antes de tratar como dada)

Confirmado em `~/Documentos/Reverend-Insanity-fonte/texto/Volume_4_-_The_Demon_Lord_Rampages_Unhindered.txt`:

> [!quote] Faixa baixa — ~linear, dobra por volta de 1.000 Marcas (perto do Cap. 852)
> "Two hundred dao marks can increase power by twenty percent. Six hundred would mean a sixty percent increase." — confirma exatamente a leitura já registrada no Log: **+20% de poder a cada 200 Marcas**, extrapolação linear simples chegando a **+100% (dobro) por volta de 1.000 Marcas**.

> [!quote] Rank 8 — salto para multiplicadores de centenas/milhares (linha 32839, poucos capítulos antes do 852, mesmo arco da Vol. 4)
> "The dao marks on a Gu Immortal could amplify the power of Immortal Gu and immortal killer moves. This amplification was quite terrifying, rank eights could have an amplification with a multiplier of hundreds or even thousands, that was also why rank seven Gu Immortals could rarely beat rank eight Gu Immortals."

Um terceiro trecho (Vol. 5) reforça o mesmo padrão qualitativo sem dar número: "between rank seven and eight, the difference in dao marks was like heaven and earth... when rank eight fought against rank seven, it was almost always a one-sided fight." **As duas citações do Log se confirmam** — a única imprecisão é o número exato do capítulo (a citação de "+20%/200 Marcas" está de fato no Cap. 852; a frase "hundreds or even thousands" está no Cap. 850, três capítulos antes, no mesmo arco de Star Form blessed land — próximo o bastante para não invalidar a citação registrada).

**Ressalva importante para a leitura deste achado:** a citação de "centenas/milhares de vezes" descreve a diferença entre **ranks adjacentes** (rank 7 vs. rank 8), não entre patamares de domínio **dentro do mesmo rank 8** (que é o que a escada de [[☯️ Marcas de Dao]] modela pós-rank-6). A escada do vault usa essa citação só como *inspiração* de que o topo deveria ser decisivo — não como um número a bater literalmente em cada degrau.

### Simulação — duelo 1v1, rank 8 (M=128), tudo igual exceto o nível de domínio

Script novo: [[simulacoes/2026-08-31-marcas-de-dao-nao-linear.py|_Processo/simulacoes/2026-08-31-marcas-de-dao-nao-linear.py]]. Reaproveita a MESMA fórmula de dano/ataque/defesa/crítico/RD de [[simulacoes/2026-08-31-validacao-completa.py]] (pool `M dX` + `M×B`, `acerto = d20 + atributo + 2×rank + 2` contra Defesa, RD com piso `1×M`, crítico no 20 dobra os dados) — só troca o cenário de "grupo vs. moldes de inimigo" por um duelo 1v1 simétrico em tudo (CON, Destreza, atributo de ataque, dado — Caminho médio d10) exceto o nível de domínio. **5.000 duelos por confronto, semente `20260830`.**

| Confronto | Escada LINEAR (atual) | Escada NÃO-LINEAR (proposta) |
|---|---|---|
| Grão-Mestre vs. Quase-Supremo | Grão-Mestre 30,6% · Quase-Supremo **69,4%** | Grão-Mestre 4,4% · Quase-Supremo **95,6%** |
| Quase-Supremo vs. Grande Mestre Supremo | Quase-Supremo 5,3% · G.M.Supremo **94,7%** | Quase-Supremo 2,8% · G.M.Supremo **97,2%** |
| Grão-Mestre vs. Grande Mestre Supremo | Grão-Mestre 0,5% · G.M.Supremo **99,5%** | Grão-Mestre 0,0% · G.M.Supremo **100,0%** |

A escada NÃO-LINEAR testada mantém Vislumbre–Grão-Mestre intocados (faixa onde o cânone dá o número ~linear) e só acelera os dois últimos degraus: Quase-Supremo ganha o dobro de pool que hoje só aparece no Grande Mestre Supremo (`B+4`, pool ×2 em vez de ×1), e Grande Mestre Supremo sobe para `B+6`, pool ×8 (em vez de `B+5`, ×2).

### Leitura

**A escada LINEAR atual já produz "o patamar mais alto vence de forma esmagadora" em DOIS dos TRÊS confrontos** — qualquer confronto que atravesse o Grande Mestre Supremo (94,7% e 99,5%, ambos batendo a leitura de "quase sempre uma luta de lado só" que o cânone descreve para rank 7 vs. rank 8). Isso não é coincidência: a nota de Combate já registra que o Grande Mestre Supremo foi desenhado para **igualar um Venerável recém-chegado ao rank 9** (`256d12 + 640` médio 2.304 contra `256d12` médio 1.664) — exatamente o tipo de gap que a citação de "centenas/milhares de vezes" descreve para uma fronteira de rank.

**O único confronto que fica longe de "esmagador" é Grão-Mestre vs. Quase-Supremo (69,4% / 30,6%)** — o único par onde nenhum dos dois lados atravessa o degrau que dobra o pool (a diferença entre eles é só `B+3` vs. `B+4`, sem mudança de multiplicador). Poder médio por golpe sobe só ~12% (`128×5,5+128×4=1216` contra `128×5,5+128×3=1088`), o suficiente para um favoritismo real (o lado mais forte ganha mais de 2× mais que perde), mas não para tornar a luta insustentável para o mais fraco.

> [!important] Recomendação: manter a escada linear — a variante não-linear resolve um problema que o degrau do topo já resolve sozinho
> A variante não-linear testada empurra até o confronto "moderado" (Grão-Mestre vs. Quase-Supremo) para 95,6% — mas isso contradiz a PRÓPRIA citação que motivou a pendência: o Cap. 852 descreve a faixa **baixa/intermediária** de Marcas como aproximadamente linear (+20% a cada 200 Marcas), e é só na fronteira de **rank** que o romance registra o salto para "centenas ou milhares de vezes". Nada no texto sugere que o salto deveria acontecer *dentro* do rank 8, entre Grão-Mestre e Quase-Supremo — a citação de "hundreds or thousands" nunca foi sobre essa fronteira. A escada atual já reserva o salto decisivo para o único lugar que a lógica da ficção pede: o topo (Grande Mestre Supremo, calibrado para igualar rank 9). Tornar TODOS os degraus decisivos, como a variante não-linear faz, apagaria a diferença de ritmo entre "ainda tem alguma chance contra o próximo patamar" (Grão-Mestre vs. Quase-Supremo, hoje) e "praticamente sem chance" (qualquer coisa contra Grande Mestre Supremo, hoje) — uma distinção que o próprio romance também faz (rank 6 vs. 7 "podem ser parelhos ocasionalmente", rank 7 vs. 8 "quase sempre um lado só", rank 9 vs. 8 "como pisar numa formiga" — três gradações, não uma escalada uniforme). **Veredito: nenhuma mudança na tabela de [[☯️ Marcas de Dao]] ou em `⚔️ Combate.md`.** Fecha a pendência de "Em aberto" como decisão negativa — a análise fica registrada para não ser reaberta sem simulação nova.

---

## 🔴 O achado principal: os moldes atuais não ameaçam

Linha de base, com as composições que a nota de [[⚔️ Ameaças Genéricas por Rank|Ameaças]] recomenda hoje:

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** — 6 Recrutas | 100% · 4,0 vivos | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Padrão** — 2 Guerreiros + 4 Recrutas | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Difícil** — 1 Elite + 2 Guerr + 2 Recr | 100% · 3,9 | 100% · 3,9 | 100% · 3,8 | 100% · 3,8 |
| **Clímax** — 1 Chefe + 1 Guerreiro | 96% · 3,3 | 92% · 3,0 | 48% · 1,2 | 76% · 2,0 |

*(vitória do grupo · sobreviventes de 4)*

**Fácil, Padrão e Difícil terminam com os quatro personagens de pé, em todos os ranks, sem exceção.** Não é que sejam fáceis — é que três das quatro categorias não existem mecanicamente. Só o Clímax ameaça, e mesmo ele só a partir do rank 3.

A causa é simples e está na própria nota de Ameaças: o que machuca é **ação inimiga por rodada**, e as composições atuais entregam de 2 a 6. Aumentar a Vitalidade ou o dano do molde não resolve — inimigo com mais vida só alonga a cena. O que falta é *volume de ações* e *dano que a RD não coma*.

---

## 🟢 Os três moldes novos

### 1. A Horda — recrutas como uma unidade só

Recrutas individuais morrem antes de agir: um PJ de rank N mata um Recruta por golpe. A economia de ação deles nunca se materializa. A correção é tratá-los como **uma entidade**:

- **Vitalidade somada:** `4 × M × (nº de membros)`.
- **Um ataque por personagem de pé** — cerco, não iniciativa individual.
- **O passo sobe com o tamanho:** `−1, +1 Nível a cada 4 membros vivos`. Uma horda de 12 bate no passo **+2** (`1d10 × M`); conforme morre, o passo desce sozinho.
- **Acerto `d20 + rank + 6`** (o +2 é o cerco).

O passo decrescente é a peça boa: o grupo **sente** a horda enfraquecendo, sem ninguém precisar contar cadáveres.

### 2. Ação Especial — uma por inimigo, uma vez por cena

Todo Guerreiro e Elite ganha **uma** ação especial, usada uma vez por cena: um ataque com **+2 Níveis** que também aplica **Lentidão 2**. Custa nada de estatística e muda a cena, porque tirar ação de um PJ vale mais que tirar Vitalidade.

### 3. Mestre de Gu humano — o molde que faltava

Inimigo humano cultivador, e não uma fera com números. É o molde mais útil do conjunto porque é o que o cenário produz o tempo todo.

| | Mestre de Gu |
|---|---|
| **Vitalidade** | `14 × M` |
| **Defesa** | `13 + rank` |
| **RD** | `1 × M` (Gu de defesa sustentado) |
| **Acerto** | `d20 + rank + 7` |
| **Ações** | **2 por rodada** |
| **Ataque** | Gu do próprio rank, passo 0 (`1d6 × M`) |
| **Ação Especial** | Gu de **Alma**: `1d8 × M`, **ignora RD**, e aplica Lentidão 2 |

**A especial de Alma é o que faz o molde funcionar.** A RD `1 × M` que todo PJ carrega come ~40% de um golpe comum; o dano de Alma passa inteiro e ainda bate num trilho que quase ninguém protege. Um Mestre de Gu com 2 ações e um golpe que ignora armadura é uma ameaça real com metade da Vitalidade de um Chefe.

---

## 📊 A curva: vitória do grupo por ações inimigas/rodada

| Composição | ações/rodada | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|---|
| Horda de 8 | 4 | 100% | 100% | 100% | 100% |
| Horda de 12 + 1 Guerreiro especial | 5 | 100% | 100% | 97% | 99% |
| **3 Mestres de Gu** | **6** | **99%** | **98%** | **97%** | **98%** |
| 2 Mestres + Horda de 8 | 8 | 97% | 94% | 93% | 96% |
| **4 Mestres de Gu** | **8** | **76%** | **63%** | **56%** | **60%** |
| 1 Elite especial + 3 Mestres | 7 | 67% | 53% | 44% | 44% |
| 3 Mestres + Horda de 12 | 10 | 31% | 19% | 6% | 10% |
| 1 Chefe + 1 Guerreiro | 5 | 96% | 92% | **48%** | 76% |
| Chefe + 2 Mestres | 7 | 24% | 12% | 0,7% | 2,4% |

Três leituras que importam:

**1. Fora o Chefe, a curva é estável entre ranks.** Uma vez corrigido o uso do Golpe Matador (ver abaixo), a mesma composição entrega dificuldade parecida do rank 1 ao 5 — a variação restante é de 10 a 20 pontos na ponta difícil, com o rank 1 sendo o mais leve. **A exceção é o Chefe**, que oscila de 96% no rank 1 a 48% no rank 3 e 76% no rank 5: as 3 ações fixas dele não acompanham nada que escala.

**2. Nem toda ação vale o mesmo.** Oito ações de 4 Mestres (56–76%) são muito piores para o grupo que oito ações de 2 Mestres + Horda (93–97%), porque as do Mestre vêm com dano de Alma que ignora RD e com Lentidão, e as da horda não. **Conte ações ponderadas: uma ação com especial vale duas comuns.**

**3. O Golpe Matador contra alvo errado perde a luta.** Na primeira rodada desta auditoria, a IA dos personagens disparava o Golpe Matador contra qualquer alvo de Elite ou acima. Isso sozinho derrubava a vitória do grupo de **97% para 76%** no rank 3, e criava um "vale do rank 3" que parecia propriedade do sistema e não era. Restringindo o disparo a alvos de Chefe, o vale desaparece por completo. **Não é bug do sistema — é o sistema funcionando:** o custo `(soma dos custos) × nº de Gu`, dobrado se híbrido, torna o Golpe Matador um recurso de arco, e gastá-lo com um inimigo mediano custa a cena. Vale documentar isso para os jogadores, porque a punição é severa e não é óbvia na ficha.

---

## 🌍 Terreno

Difícil (1 Elite + 2 Guerreiros + 2 Recrutas), rank 3, variando só o dial de terreno do Lee:

| Terreno | Vitória | Sobreviventes |
|---|---|---|
| **−2** (hostil ao elemento dele) | 92,2% | 2,64 |
| **0** (neutro) | 94,8% | 2,75 |
| **+2** (favorável) | 95,9% | 2,81 |

**O terreno mexe pouco quando só um personagem o sente** — cerca de 4 pontos percentuais de ponta a ponta. É o esperado, e é a favor do desenho: o dial dos Cinco Elementos é uma alavanca tática do Lee, não um botão que decide a cena. Numa mesa com dois ou mais personagens elementais o efeito dobra, e aí vale o mestre declarar o terreno antes da iniciativa.

---

## ✅ O que mudou por causa desta rodada

1. **Três moldes novos** — Horda, Ação Especial e Mestre de Gu — escritos em [[⚔️ Ameaças Genéricas por Rank]].
2. **A tabela de composição passou a ser por rank**, porque a curva acima mostra que uma tabela única erra.
3. **A contagem de ações virou ponderada:** ação com especial conta como duas.

### Correção de uma conclusão anterior

A rodada anterior concluiu que *"o que decide o poder de um personagem é se o Caminho dele tem um Gu de ataque no rank em que ele está"* e recomendava conferir isso antes de subir a mesa de rank. **Isso estava errado como princípio de design.** O catálogo do vault é para ser completo: todo personagem tem o Gu de ataque do próprio rank. Onde falta um, o que falta é escrevê-lo — não é um fato sobre o sistema nem um risco que o mestre precise contornar. Ver a decisão 69 no [[🧭 Log de Decisões]].

---

## 🔁 Terceira rodada — com o arsenal completo

Depois que os **50 Gu novos** fecharam a cobertura de ataque e de utilidade do catálogo, a simulação foi rodada de novo com as ações de Chefe da decisão 72:

| Cena | rank 1 | rank 2 | rank 3 | rank 5 |
|---|---|---|---|---|
| **Fácil** — Horda de 8 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 | 100% · 4,0 |
| **Padrão** — 3 Mestres de Gu | 99% · 3,6 | 98% · 3,5 | 98% · 3,4 | 98% · 3,3 |
| **Padrão pesado** — 2 Mestres + Horda de 8 | 97% · 3,0 | 94% · 2,7 | 94% · 2,5 | 95% · 2,4 |
| **Difícil** — 4 Mestres de Gu | 75% · 2,3 | 63% · 1,8 | 56% · 1,5 | 59% · 1,5 |
| **Clímax** — 1 Elite especial + 3 Mestres | 68% · 2,0 | 53% · 1,4 | 44% · 1,1 | 46% · 1,1 |
| **Clímax** — 1 Chefe + 1 Guerreiro especial | 56% · 1,7 | 62% · 1,5 | 80% · 2,1 | 73% · 2,0 |

**Os números praticamente não se moveram**, e isso é o resultado que importa. A simulação sempre assumiu que todo personagem tinha o Gu de ataque do próprio rank — que é a premissa correta do projeto. **Escrever os 50 Gu não mudou a matemática; fez o catálogo entregar o que a matemática já assumia.** A tabela de encontros continua válida, e agora está apoiada num arsenal que existe de verdade.

A única linha que se mexeu foi a do **Chefe**, por causa das ações medidas por rank: ela saiu de 96%/92%/48%/76% para **56%/62%/80%/73%**, bem mais perto de um clímax de verdade nas três primeiras faixas. O rank 3 com 2 ações ficou o mais leve dos quatro — se a mesa quiser apertar, **3 ações no rank 3 leva a vitória a 45%**, e é o clímax mais duro que o sistema entrega sem sair do jogável.

---

---

## 🌠 Quarta rodada — o Físico Extremo vale o que cobra? *(2026-08-28)*

20.000 carreiras por cenário, do rank 6 até 10.000 Marcas (o piso do rank 7), em tempo interno.

### ⚠️ Dois artefatos do modelo, corrigidos antes de qualquer conclusão

**Nenhum dos dois é problema do sistema.** Ficam registrados porque a primeira rodada de números estava errada por causa deles.

1. **A primeira versão matava todo mundo por Ferimento da Terra.** O modelo acumulava Ferimentos da Terra sem nunca reparar — mas reparo é regra explícita (50 PEI e 3 meses internos por nível), e qualquer Imortal com renda de camada 3 paga isso sem sentir. Corrigido para reparar 1 nível por década.
2. **A segunda versão matava todo mundo na Provação Celestial** — 93% a 100% de morte, para o Imortal comum inclusive. O modelo estava simulando um Imortal **despreparado**: sem Gu de Estabilização, sem presságio respondido, sem terra Inabalável, sem aliado. A nota de [[🌩️ Calamidades e Provações]] trata os três presságios como obrigatórios e as reduções como o caso normal.

### 📊 A preparação **é** o sistema

Chance de atravessar o rank 6 vivo, do mesmo personagem, mudando só a preparação:

| | Despreparado | Típico *(−3 e 2 presságios)* | Bem preparado *(−3, 3 presságios, Inabalável, aliado)* |
|---|---|---|---|
| **Imortal comum** | **2,2%** | 48,3% | **70,2%** |
| **Físico Extremo** | 0,0% | 4,2% | **20,2%** |

**Isto valida o pilar inteiro**, e vale mais que qualquer outro número desta nota: sem preparação, o ato imortal é intransponível para qualquer um. Não há ajuste a fazer.

### 🔴 Achado 1 — a Pressão da Abertura é matematicamente fatal depois da Ascensão

| Cenário *(bem preparado, terra Inabalável)* | Chega ao rank 7 | Anos internos | Perda de Vitalidade |
|---|---|---|---|
| Imortal comum | **70,2%** | 292 | — |
| Físico, +5 de CD, **Pressão desligada** | 20,7% | 233 | — |
| Físico, +5 de CD, **Pressão ligada** | **0,0%** | — | **100%** |
| Físico, com **Selo de Limite Sombrio** | 20,4% | 232 | — |

A Pressão sobe **+1 a cada 6 meses** e só zera ao **subir de rank**. Na fase mortal isso funciona: rank sobe a cada 1–2 anos, a Pressão chega a 2–4 e o teste de CON passa. Na fase imortal o próximo rank leva ~250 anos internos — **500 testes com a CD subindo sem teto**. Por volta do vigésimo teste a CD é 30 e a falha é automática; vinte falhas são −100% de Vitalidade máxima e autoexplosão. **Todo portador de Físico Extremo que ascende morre em cerca de uma década, sempre.**

O Selo de Limite Sombrio resolve, e a nota já o descreve — mas como recurso opcional e caro, não como obrigação. **A regra não diz o que acontece com a Pressão depois da Ascensão, e é essa omissão que produz o zero.** Ver decisão 97.

### 🟡 Achado 2 — o +5 de CD é caro, e compra velocidade

O Físico troca **70,2% → 20,7%** de chance de atravessar o rank, e recebe em troca **61 anos internos a menos** (233 contra 292) por causa das Marcas em dobro. Ele não é melhor nem pior: é **três vezes e meia mais mortal e um quarto mais rápido**. Isso é coerente com o que a nota do físico promete — *quase nenhum chega velho* — e **não é recomendado alterar**.

### 🟢 Achado 3 — a isenção de Caminho duplo compra exatamente 61 anos

| Penalidade sobre o custo de progressão | Chega ao rank 7 | Anos internos | Diferença vs. Imortal comum |
|---|---|---|---|
| **0% — a regra atual do Xie Lang** | 20,2% | **231** | **−61 anos** |
| +15% em ambos | 15,3% | 265 | −27 anos |
| **+25% em ambos** | 12,4% | **288** | **−4 anos** |
| +50% em ambos *(a penalidade cheia)* | 8,2% | 338 | +46 anos |
| *Imortal comum, 1 Caminho* | *70,1%* | *292* | *—* |

**A vantagem que a isenção dá é de calendário, não de combate.** Com +25% ele chega ao rank 7 em 288 anos contra os 292 de um Imortal comum — paridade exata no relógio, mantendo Marcas em dobro, +2 Níveis de Dano e terra Especial. Ver decisão 98.

**A variante "penalidade só acima de um nível de domínio" foi testada e descartada:** com limiar em 10.000 Marcas ela nunca entra em vigor durante o rank 6, porque 10.000 **é** o piso do rank 7 (20,1% e 232 anos — idêntico a não ter penalidade). Com limiar em 1.000 ela rende 287 anos, ou seja, o mesmo que um +25% direto, com uma regra a mais para lembrar.

### 🔴 Achado 4 — o problema de ritmo não é o Xie Lang, é o Lee

Marcas acumuladas em 200 anos internos de rank 6, bem preparados:

| Personagem | Marcas | Nível de domínio |
|---|---|---|
| **Xie Lang** *(Físico, Lua+Alma isento)* | **8.702** | Pequeno Feito |
| Demvi *(Vento, um Caminho só)* | 7.201 | Pequeno Feito |
| Jiāotáng *(Sangue+Força isento)* | 7.069 | Pequeno Feito |
| **Lee** *(Cinco Elementos — Marcas ÷ 5)* | **2.187** | Pequeno Feito |

O Xie Lang está **21% à frente** do segundo colocado — margem que se sente e não desequilibra, e que a penalidade de +25% zera. **O outlier real é o Lee, 3,3× atrás de todo mundo**: a regra de dividir as Marcas por cinco custa muito mais do que o acordo dele aparentava, e ele leva mais de 600 anos internos para alcançar o mesmo domínio que os outros alcançam em 200. Item aberto — ver abaixo.

### 🔧 Método desta rodada

Calamidade Terrestre a cada 10 anos internos (3 etapas) e Provação Celestial a cada 100 (5 etapas) · `CD = 14 + 2×(rank−6) + faixa do Contador + 2 se Provação + 5 se Físico Extremo − reduções` · Marcas proporcionais aos sucessos, em dobro para o Físico · Marcas iniciais 850 (comum) e 1.700 (Físico) · Contador de Ameaça começando em 3 e 15 · falha zera as Marcas do evento e soma 1 Ferimento e 1 Ferimento da Terra · Ferimento da Terra reparado a 1 nível por década · 0–1 sucessos numa Provação é morte · 1 natural conta como duas falhas.

## 📌 O que continua em aberto

- [ ] **O Caminho dos Cinco Elementos leva 3,3× mais tempo para acumular domínio** por causa da divisão de Marcas por cinco (achado 4 da quarta rodada). A decisão 76 fechou o Wu Xing como "desenho funcionando" olhando só para dano em PvP; o eixo de **ritmo de Marca** não tinha sido medido. Reabrir.

- **O Chefe continua sendo o molde menos estável**, mesmo com as ações medidas por rank (decisão 72): 56% · 62% · 80% · 73%. O rank 3 é o mais leve dos quatro. Não é erro — é consequência de a dificuldade de um Chefe ser governada por quantos Golpes Matadores o grupo consegue pagar naquele rank, e não por ele. Se a mesa quiser um clímax duro no rank 3, use **3 ações** em vez de 2.
- **O Golpe Matador Coletivo não foi modelado** — só os individuais. Quatro participantes chegam a +6 Níveis no núcleo, e isso muda a conta do clímax.
- **O Lee no fundo do PvP é o desenho funcionando**, não um problema: ele compra versatilidade e resposta a qualquer elemento, e paga em pico de dano. Fica registrado como esperado, não como pendência.
- **A Retaliação por falha de Golpe Matador é rara demais no modelo** para medir bem — os PJs quase sempre passam no teste de conjuração no rank em que têm essência para gastar.

## 🔧 Método

Motor em Perl, semente fixa (`20260827`), 3.000 iterações por cenário, limite de 20 rodadas. IA dos PJs: cura se um aliado está abaixo de 40%; Golpe Matador uma vez por cena contra alvo de Elite ou acima; senão ataque padrão; sem essência, desliga um sustentado e cai para melee cru (sem `× M`). IA dos inimigos: foco de fogo no PJ mais ferido, especial na primeira ação. Os scripts ficam no scratchpad da sessão, não no vault.
