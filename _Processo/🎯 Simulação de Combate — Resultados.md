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
