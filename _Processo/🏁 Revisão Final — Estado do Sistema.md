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

Corrigidos os dois, o critério passou a ser cumprido **sem tocar num único número de balanceamento**. Uma terceira passada fechou o que faltava — a mesma escada de dado tinha parado nos ranks 2 a 4, porque nos Gu de rank 5 o passo já não sobe o tipo do dado e vira `+1 por dado`, então eles **não pareciam errados e estavam** — e junto com ela as somas de apoio dos Golpes Matadores, que davam +3 onde a regra dá +2 e contavam um Gu duas vezes. **Estado final medido: Lee 100 · Jiāotáng 90 · Xie Lang 87 · Demvi 67.** Paridade entre os três da frente, Demvi por último — o critério do autor, inteiro.

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

## 3. As seis lições de método

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

> [!tip] 6. Uma garantia **escrita** não é uma garantia **verificada**
> O vault publicava uma semente fixa como prova de que as simulações eram reprodutíveis — e as sementes saíam de uma função que o Python aleatoriza a cada processo. **A garantia estava no texto e não existia no código**, e as células eram irreprodutíveis dentro do próprio ruído. Ninguém acharia isso lendo: só tentando reproduzir. É a versão numérica de *execute, não avalie*.

**As seis dizem a mesma coisa por ângulos diferentes:** o erro raramente está no julgamento de desenho. Está no que se aceita como prova, e no caminho entre a decisão e o lugar onde alguém vai lê-la.

---

## 3b. E uma sétima, que é de outra natureza

As seis acima dizem **como auditar**. Esta diz **como escrever para não gerar auditoria** — é a única do conjunto que previne em vez de detectar, e por isso fecha a seção.

> [!important] Um vazio deliberado precisa estar escrito como deliberado
> Campo em branco, exceção sem justificativa e regra que "obviamente não se aplica aqui" são todos convites para alguém reinterpretar. **Metade do que esta revisão corrigiu era silêncio que um leitor posterior preencheu do jeito errado, de boa-fé.**
>
> **A ressalva que torna a regra aplicável, e sem ela ela vira "comente tudo":** anote o vazio **só quando um leitor competente ficaria tentado a preenchê-lo**. Um Gu que genuinamente não tem desvantagem não precisa de nota; um **golpe defensivo sem Prerrogativa precisa**, porque doze irmãos dele têm uma e o vazio parece esquecimento. **O critério é a expectativa que o próprio documento cria, não a ausência em si.**
>
> **E o inverso também vale.** A fórmula de *acerto à distância* continua publicada e válida, num mundo onde **arco e besta não existem** — porque ela serve ao arremesso de objeto improvisado. Alguém vai querer "consertar" isso apagando a fórmula. Ali, o **não-vazio** é que precisava de nota.

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
| ~~**B1 — Gu de Corpo só começam no rank 2**~~ | — | ✅ **Fechado pelo autor, que derrubou o julgamento de "fronteira deliberada".** Criados quatro Gu de Corpo permanentes de rank 1 — um para Lua, Alma, Vento e Wu Xing —, todos com portão `CON +0` |

**As três pendências que travavam o autor foram fechadas nesta rodada:** o Acordo de Mesa foi unificado em seis perguntas, o Gu do Empenho Total ficou no arsenal declarado como exceção, e as peças que a lore de Vespéria inventa foram **marcadas como variantes de campanha** e listadas numa tabela única na nota-mãe — com âncora mecânica onde a falta dela travaria a mesa.

---

## 5. O que ainda não foi testado

**A revisão mediu coerência interna. Ela não mediu o objetivo real.**

O leitor final é um mestre que **nunca leu o romance e nunca rodou este sistema**. Nada até aqui verificou se ele consegue pegar o vault, montar uma ficha e rodar um combate sem travar. O instrumento existe e já foi usado uma vez — [[🔍 Playtest de Leitura — Mestre Novo (2026-08-31)]] —, e na época achou coisas reais.

**Rodá-lo de novo agora mede a coisa certa**, porque os 58 achados que ele reencontraria já foram corrigidos. É a validação natural desta revisão, e é a única que responde a pergunta que o vault inteiro existe para responder.
