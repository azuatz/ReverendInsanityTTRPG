---
tags:
  - processo
  - fechado
aliases:
  - Revisão Final — Estado do Sistema
  - Revisão Final
escopo: processo
---

# 🏁 Revisão Final — Estado do Sistema

*Fechada em 2026-09-01, em duas frentes paralelas: uma varredura de **números** (coerência entre notas e as 26 rodadas de simulação) e uma varredura de **texto** (contradição, claim desatualizado, termo sem definição, e a leitura do mestre que nunca leu o romance). 106 notas auditadas, ~170 achados, peneirados para 58 que fariam alguém aplicar regra errada na mesa.*

**Esta nota existe porque o resultado estava espalhado** por dezenas de decisões numeradas, quatro relatórios e uma conversa longa entre duas sessões. Aqui ele está inteiro, numa leitura só.

---

## 1. A manchete

> [!success] Não há pendência de balanceamento. O sistema estava certo; a documentação dele não.
> Vinte e seis rodadas de simulação, e **o achado que fechou a ordem de poder da mesa não foi uma simulação — foi uma varredura de prosa.**

O critério que o autor fixou — **paridade entre Xie Lang, Jiāotáng e Lee, com Demvi por último** — parecia violado por uma margem absurda: uma medição pôs o Jiāotáng fazendo **3,4 vezes** o dano do Xie Lang no rank 3. A conclusão natural era desequilíbrio de desenho.

Não era. **Eram dois defeitos de texto empilhados:**

1. **Três dos quatro Caminhos da mesa tinham os pools de ataque calculados a partir de `d6`** em vez do dado real do Caminho. Lua e Sangue são `d8`, Vento é `d10`. O Vento perdia quase metade do dano. Era o mesmo defeito já corrigido no Caminho da Alma tempos atrás — e ninguém tinha ido olhar as outras colunas.
2. **O pico do Fantasma de Fera estava publicado como se fosse a linha de base** do lutador, quando ele é uma exceção lendária.

Corrigidos os dois, a ordem de poder mede **Lee 100 · Xie Lang 97 · Jiāotáng 79 · Demvi 71** — o critério, cumprido, sem tocar num único número de balanceamento.

**O resto do motor também está fechado:** a escada de dificuldade entrega **25 de 25 células** dentro da faixa prometida, os moldes de inimigo estão calibrados, a economia tem guia de mesa, o refino tem tempo em calendário, e a fase imortal tem tribulação, espólio e calamidade.

---

## 2. O que a revisão achou, em uma frase

**O vault errava na baixa, não na decisão.** Regra nova entrava, regra velha não saía, e a propagação parava na nota onde a decisão nasceu. **~70% dos 58 achados são resíduo de revogação** — quatorze decisões diferentes que foram tomadas, aplicadas na nota-dona, e nunca chegaram ao resto.

E o resíduo não estava onde se esperaria:

> As pastas de **regra profunda** estavam limpas. As pastas que **a mesa efetivamente lê** — o Portal, os guias, as fichas modelo — eram as mais quebradas.

Alguns exemplos do que isso significava na prática, todos corrigidos:

| Onde | O que estava publicado | Por que importava |
|---|---|---|
| **Folha de Referência**, a página que fica aberta durante o jogo | O acerto somava bônus de treino | Regra revogada com efeito medido de **até +30,9 pontos percentuais** de vitória do grupo |
| **As duas fichas modelo**, em três linhas cada | O mesmo bônus de treino no ataque | Pior que na Folha: ficha é gabarito, e o jogador copia linha por linha |
| **Ficha de exemplo do guia do mestre** | Regeneração de essência **24× rápida demais** | Sozinho, apagava a escassez de essência da campanha inteira |
| **Guia de criação** | 60% de Aptidão classificado como Grau C | Rebaixava o gabarito **duas faixas de teto de rank** |
| **Grimório de Ameaças** | **Duas tabelas de vitória contraditórias para a mesma cena** | O mestre montava o clímax com o número errado |
| **Conversão Medieval**, o que um mestre de D&D lê primeiro | Cinco regras revogadas, incluindo um estágio que não existe | É a porta de entrada do sistema para quem vem de fora |
| **A nota de Caminhos**, para onde o vault inteiro aponta | "+50% por Caminho extra" | Escondia que **Sangue + Força — a build de um PJ — é um par incompatível**, que se anula e fere a Terra Abençoada |

---

## 3. As cinco lições de método

**Valem mais que qualquer item da lista**, porque dizem o que uma auditoria futura deve olhar primeiro.

> [!tip] 1. A regra costuma estar certa; **o exemplo é que mente**
> Quase toda conta errada estava num **gabarito que o mestre copia** — ficha de exemplo, rodada resolvida passo a passo, loadout de inimigo, provação de herança — e quase nenhuma na regra em si. **Audite os exemplos antes das regras.**

> [!tip] 2. O vault se contradiz mais **consigo mesmo** do que com o Log
> Em pelo menos oito casos a resposta certa estava **na mesma nota, a poucas linhas do erro**. Isso torna a correção barata e sugere a auditoria mais eficiente que existe aqui: **conferir cada nota contra ela própria**, antes de conferir contra o contrato de decisões.

> [!tip] 3. Aritmética responde *"cabe?"*; só a cena responde *"funciona?"*
> Uma regra de economia foi adotada por cálculo de tanque e passou. Medida numa cena de verdade, ela derrubava o clímax de rank 5 de 72% para **6%** de vitória. **Nenhuma regra de custo deve ser adotada sem passar por uma cena.**

> [!tip] 4. O defeito costuma estar **no formato que recebeu o número**, não no número
> Duas vezes no mesmo dia: medir só ranks ímpares por economia **escondeu o pior valor da tabela**, que estava no rank 4; e publicar um resultado numa tabela que não tinha a coluna do rank medido **escondeu a medição inteira** — três consertos existiam no Log e não chegavam a mestre nenhum.

> [!tip] 5. Declarar *"zero ocorrências"* a partir de uma busca por texto literal é declarar uma exaustividade que a busca não tem
> Aconteceu nesta própria revisão, e foi retratado. A frase procurada existia mais uma vez, com pontuação diferente em volta, e o `grep` que declarou o zero nunca a viu. **Confira por conceito, não por string, antes de afirmar cobertura total.**

**As cinco dizem a mesma coisa por ângulos diferentes:** o erro raramente está no julgamento de desenho. Está no que se aceita como prova, e no caminho entre a decisão e o lugar onde alguém vai lê-la.

---

## 4. O que ficou em aberto

**Nada aqui é sentido na mesa.** São refinamentos de motor e uma frente de execução.

| O quê | Dono | Estado |
|---|---|---|
| **Empilhamento C + A** — alavanca de uma linha, medida e nunca aplicada | Sessão de medição | Em aberto no [[🧭 Log de Decisões]] |
| **Controle vindo de PJ** — o motor nunca modelou, e é disso que o degrau `d8` vive | Sessão de medição | Em aberto |
| **Retaliação do Golpe Matador Coletivo** — falta escolher entre um piso e um teto de modelagem | Sessão de medição | Em aberto |
| **Extensão do `B` ilimitado acima da faixa** | Decisão de desenho retida | Em aberto |
| **Rabo do backlog da varredura** — os achados 🟡 e 🟢 | Ambas as sessões | Em execução |
| **B1 — Gu de Corpo só começam no rank 2**, e três dos quatro PJs não têm efeito permanente no rank 1 | **Autor** | Julgado fronteira de design deliberada; a recusa aguarda confirmação explícita |

**As três pendências que travavam o autor foram fechadas nesta rodada:** o Acordo de Mesa foi unificado em seis perguntas, o Gu do Empenho Total ficou no arsenal declarado como exceção, e as peças que a lore de Vespéria inventa foram **marcadas como variantes de campanha** e listadas numa tabela única na nota-mãe — com âncora mecânica onde a falta dela travaria a mesa.

---

## 5. O que ainda não foi testado

**A revisão mediu coerência interna. Ela não mediu o objetivo real.**

O leitor final é um mestre que **nunca leu o romance e nunca rodou este sistema**. Nada até aqui verificou se ele consegue pegar o vault, montar uma ficha e rodar um combate sem travar. O instrumento existe e já foi usado uma vez — [[🔍 Playtest de Leitura — Mestre Novo (2026-08-31)]] —, e na época achou coisas reais.

**Rodá-lo de novo agora mede a coisa certa**, porque os 58 achados que ele reencontraria já foram corrigidos. É a validação natural desta revisão, e é a única que responde a pergunta que o vault inteiro existe para responder.
