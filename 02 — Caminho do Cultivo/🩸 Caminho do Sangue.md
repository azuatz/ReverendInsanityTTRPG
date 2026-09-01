---
tags:
  - regra
  - cultivo
  - caminho
aliases:
  - Caminho do Sangue
escopo: sistema
---

# 🩸 Caminho do Sangue

> Caminho pleno, e o mais barato do jogo em essência. Ver [[🛤️ Os Caminhos|Os Caminhos]]. Osso e Carne são subcaminhos dele.

O Caminho do Sangue não é um Caminho elemental disfarçado. Ele parte de uma premissa que nenhum outro aceita: **o combustível não está no mundo, está dentro de você**. Por isso um Gu de Sangue custa metade da essência de um Gu de Fogo equivalente ([[🏛️ Arquitetura do Sistema|Arquitetura do Sistema]], modificador de Caminho **×0,5**) — e por isso o cultivador de Sangue é o único da mesa que pode ficar sem recurso **com o tanque de essência cheio**.

O que ele compra com isso é velocidade bruta. Dano alto cedo, cura que nenhum Caminho da Água alcança no mesmo rank, e a capacidade de converter vida — sua, de um refém, de um irmão — diretamente em Níveis de Dano. É o Caminho que faz um rank 3 matar um rank 4 numa terça-feira qualquer, sem lua cheia, sem terreno certo, sem esperar nada.

E é crime capital em toda facção ortodoxa do mundo conhecido. Isso não é sabor: está escrito em número mais abaixo, e é a metade da ficha que o jogador vai passar mais tempo administrando. Combina com Alma, Escravidão, Transformação e Força; briga com qualquer coisa que exija reputação limpa.

---

## 🩸 A Dívida de Sangue — o trilho que rege o Caminho inteiro

**Um trilho novo na ficha, ao lado de Vitalidade e Alma.** Um número que começa em 0, sobe toda vez que você usa o Caminho, e **não desce sozinho**.

```
Sangria    = Vitalidade que um Gu de Sangue cobra pra ativar,
             além da essência. Está na ficha de cada Gu.
             Sangria padrão de um Gu de Sangue = 1 × M do rank dele.

Toda Sangria faz DUAS coisas ao mesmo tempo:
  1. tira aquela Vitalidade agora;
  2. soma o mesmo valor à sua Dívida de Sangue.

Vitalidade máxima EFETIVA = (18 + 3 × CON + 4 × B) × M − Dívida de Sangue
```

**A consequência é o ponto todo:** cura devolve Vitalidade **até o máximo efetivo, nunca acima**. Um cultivador de Sangue com 40 de Dívida e um curandeiro do Caminho da Água ao lado continua com 40 a menos de teto. O corpo não está ferido — está **vazio**, e cura não fabrica sangue.

### Como se quita

| Método | Quita de Dívida |
|---|---|
| **Descanso longo** ([[❤️ Recursos e Dano\|Recursos e Dano]]) | `2 × M` |
| **Descanso curto** | nada. Sangue não volta em uma hora |
| Uma dose (~0,5 L) de **sangue fresco de fera ou gado**, bebido ou absorvido | `1 × M` |
| Uma dose de **sangue fresco humano** | `3 × M` |
| Sangue **drenado em combate** por um Gu de Sangue com efeito de dreno | ponto por ponto, até o total drenado |
| Um **arco de reclusão** com dieta, Gu de Sangue de rank 3+ e tempo | tudo |

Sangue coagulado não serve, sangue de cadáver com mais de uma hora não serve, e sangue do próprio usuário obviamente não serve. **A dose humana valer o triplo é a regra de design da nota inteira** — ela transforma o recurso central do Caminho num problema de logística que só tem uma solução conveniente, e essa solução é crime.

### Os limiares

Compare a Dívida com a Vitalidade máxima **cheia** (`(18 + 3 × CON + 4 × B) × M`, sem descontar nada):

| Dívida | Estado | Efeito |
|---|---|---|
| até **25%** | — | Nada. É a faixa de operação normal |
| **25–50%** | **Pálido** | −1 em testes de FOR e CON |
| **50–75%** | **Lívido** | −2 em FOR e CON · deslocamento pela metade · **−4 em Furtividade** contra qualquer coisa com faro (você cheira a ferro) |
| **75–99%** | **Seco** | −4 em FOR e CON · sua regeneração de essência cai pro **teto hostil, 50/rodada** ([[🏛️ Arquitetura do Sistema\|Arquitetura do Sistema]]) · **toda Sangria custa o dobro** |
| **100%** | **Colapso** | Você cai na hora, inconsciente, e rola **Teste de Morte** todo turno. Vitalidade atual vai a 0 |

### Sangria a Descoberto

Você pode pagar uma Sangria que não tem — **uma vez por cena**. Fica com 1 de Vitalidade em vez de cair, o excedente entra na Dívida do mesmo jeito, e você leva **1 Ferimento permanente** (−2 nos dois máximos, cumulativo). É a jogada de quem decidiu que a cena vale um pedaço do corpo, e a mesa deve deixar acontecer sem discutir — mas anotar.

> **Por que esta regra existe.** Sem ela, o modificador ×0,5 de essência tornaria o Caminho do Sangue estritamente superior a todos os outros: mesmo dano, metade do preço, zero condição ambiental. A Dívida é o preço real, e ela é pior que essência de três formas — não regenera por rodada, não volta com descanso curto, e **encolhe o teto em vez do saldo**. Um cultivador de Fogo em apuros espera duas rodadas e ataca de novo. Um de Sangue em apuros precisa de alguém pra sangrar.

---

## O que o Caminho faz

**1. Sangue como matéria.** Agulhas, lâminas, correntes, mãos, cortinas. O sangue sai do corpo e vira coisa sólida no ar — ataque à distância decente, controle bom, e uma defesa que ninguém espera. É o pilar que faz o Caminho funcionar em combate aberto sem depender de nada externo.

**2. Coagulação e roubo.** Fechar ferida, estancar *Sangramento*, transferir vida de um corpo pra outro, e drenar o inimigo pra pagar a própria Dívida. **É a cura mais rápida da fase mortal** — e a única que fica melhor quanto pior está a situação, porque só há sangue disponível quando alguém já está sangrando.

**3. Sacrifício.** Converter Vitalidade em Níveis de Dano, na hora, em quantidade que você escolhe. Nenhum outro Caminho deixa o jogador comprar poder com um recurso da ficha em tempo real. No topo dessa escada está o **sangue de parente** — o multiplicador mais alto do jogo mortal, e o crime que não tem perdão em lugar nenhum.

---

## Gu do Caminho do Sangue

Custo de ativação: Sangue é **×0,5** — **20** (rank próprio) · 5 · 2 · 1. Manutenção por rodada também entra na metade. Todos abaixo entram no [[📖 Catálogo de Gu|Catálogo]] e convivem com os Gu de Sangue que já estão lá.

| Gu | Rank | Tipo | Efeito mecânico | Forte / Fraco | Peculiaridades | Alimentação |
|---|---|---|---|---|---|---|
| **Gu da Agulha Vermelha\*** | 2 | Ataque, à distância | `Ataque: M d10 = 2d10` (passo +1), alcance 15 m. **Sangria 1 × M = 2**. Contra alvo que já esteja sob *Sangramento* ou abaixo de metade da Vitalidade, **+1 Nível** — a agulha puxa o sangue que já está solto. Ativação 20 de essência | ⬆️ Ataque à distância barato num Caminho que a maioria supõe ser só corpo a corpo · ⬇️ Cada disparo é 10% da sua barra num rank 2. Sem alvo sangrando, é um Gu de rank 2 comum e caro em corpo | ⚡Recuo ⚡Marca | Sangue fresco, uma dose por semana. Aceita sangue de gado |
| **Gu do Torniquete Vivo\*** | 3 | Cura, toque | Toca um alvo a 2 m e recupera `M d6 = 4d6` de Vitalidade nele, removendo *Sangramento*. **O valor curado entra inteiro na SUA Dívida de Sangue** — você não gasta Vitalidade agora, você empresta teto. Não cura ninguém acima do máximo efetivo dele. Ativação 20 | ⬆️ O melhor curandeiro de campo do rank 3, sem depender de Caminho da Água. Numa expedição longa, mantém o grupo inteiro de pé · ⬇️ Curar quatro aliados numa luta te coloca em **Lívido** e você luta o resto da campanha assim. O Caminho cura os outros com o seu corpo | ⚡Recuo | Sangue fresco, duas doses por semana |
| **Gu das Correntes Vermelhas\*** | 3 | Controle + dreno | Três correntes de sangue coagulado, alcance 10 m. Cada alvo faz **FOR contra a CD dos seus Gu** ou fica *Preso* por 2 rodadas. Enquanto preso, cada alvo perde `1 × M = 4` de Vitalidade por rodada e **você quita a mesma quantia da sua Dívida, ponto por ponto**. **Sangria 2 × M = 8** pra ativar. Sustentado: 5 de essência/rodada | ⬆️ O único Gu do Caminho que **paga a conta em vez de abri-la**. Três alvos presos por 2 rodadas devolvem até 24 de Dívida · ⬇️ Enquanto as correntes estão fora do seu corpo, **sua Defesa cai 2** — o sangue que deveria estar em você está no ar | ⚡Recuo ⚡Ruidoso ⚡Marca | Sangue coagulado, meio litro por uso |
| **Gu da Crosta Coagulada\*** | 2 | Defesa, sustentado | O sangue aflora e coagula em placas sobre a pele. **`RD 1 × M`**. Enquanto ativo, ser atingido faz você **perder 1 de Vitalidade por rodada** até passar um turno sem levar golpe. **Isso é perda de Vitalidade comum, NÃO é Sangria** — não entra na Dívida de Sangue nem encolhe o teto. Um Gu defensivo que acumulasse Dívida em silêncio seria armadilha |
| **Gu do Sangue Espesso\*** | 4 | Defesa + recuperação, sustentado | O sangue engrossa e circula devagar. **`RD 2 × M`** e você **recupera `M` de Vitalidade no início de cada turno, até o total de `4 × M` por cena** — depois disso o Gu só defende. Em troca, **todo deslocamento seu cai pela metade** enquanto ativo. **O teto é a identidade do Caminho:** o preço temático do Sangue é não recuperar Vitalidade sem sangue alheio, e cura indefinida a partir do próprio corpo inverteria isso |
| **Gu do Manto Fervente\*** | 4 | Amplificação, sacrifício | Ao ativar, você declara **N de 1 a 3**. Sangria imediata de `N × M = N×8`, e por **3 rodadas** todos os seus Gu de Sangue e todo golpe corpo a corpo seu ganham **+N Níveis de Dano**. Enquanto ativo você **não pode ser curado por fonte nenhuma** — o sangue está fervendo, não fecha ferida. Ativação 20, manutenção 3/rodada | ⬆️ Compra Níveis com um recurso da ficha, na hora, sem preparação e sem condição ambiental. É o botão que decide duelos · ⬇️ 24 de Dívida por 3 Níveis e uma janela de 3 rodadas em que curandeiro nenhum te alcança. Se o combo não fechar nessas 3 rodadas, você perdeu a luta e a semana | ⚡Recuo ⚡Preso ⚡Viciante | Sangue quente, colhido de corpo vivo — uma dose por ativação |
| **Gu da Lâmina de Parentesco\*** | 5 | Ataque, execução | Exige **uma dose de sangue de um parente consanguíneo do alvo**, colhida antes. `Ataque: 16d12 + 32` (passo +5, 2 Níveis acima de d12), alcance 30 m. Contra o alvo cujo parente doou o sangue: **ignora RD por completo** e o alvo tem **desvantagem** em qualquer teste pra resistir. **Sangria 5 × M = 80**. Ativação 20. **Crime capital — converse com a mesa antes** | ⬆️ Passo +5 ignorando RD contra um alvo nomeado. É o Gu que mata alguém acima do seu rank sem Golpe Matador nenhum · ⬇️ **Sem a dose do parente, o Gu simplesmente não dispara.** E 80 de Sangria é metade da barra de um rank 5 típico: um uso te joga em **Lívido** na hora | ⚡Condicional ⚡Marca 🍖Proibida 🔨Sacrifício | Sangue de parente consanguíneo do alvo pretendido. Não come outra coisa |
| **Gu Imortal do Rio Retornante\*** | 6 | Área, dreno pesado | `32d12` (32–384) em todos os inimigos num raio de 30 m. **Metade do dano total causado quita Dívida**; o que sobrar depois de zerar a Dívida vira cura de Vitalidade, respeitando o teto normal. **Se a sua Dívida for 0 no momento da ativação, o Gu cobra `10 × M = 320` de Vitalidade sua** — ele é um rio, e um rio precisa de leito. Ativação 20 | ⬆️ Num campo com seis inimigos, ele limpa a Dívida de um arco inteiro numa rodada · ⬇️ É um Gu que **exige que você esteja em dívida pra ser seguro**. Quem entra na luta inteiro e ativa isso primeiro se mata sozinho | ⚡Ruidoso ⚡Cego ⚡Recuo 🍖Proibida | 20 UV por ativação. Alimenta-se de sangue de campo de batalha — cem litros por trimestre, e alguém precisa ter morrido pra isso existir |

---

## ⚖️ O peso social — isto é regra, não sabor

**Usar um Gu do Caminho do Sangue à vista de qualquer cultivador ortodoxo é crime capital.** Não é impopular; é executável. A mesa rastreia isso num trilho:

### O trilho de Suspeita (0 a 5)

| Gatilho | Suspeita |
|---|---|
| Um Gu de Sangue ativado à vista de uma testemunha que sobreviveu | **+1** |
| Um corpo drenado deixado onde alguém vai encontrar | **+2** |
| Um Gu de investigação encontra o rastro da tag ⚡`Marca` (todo Gu de Sangue ofensivo tem) | **+1** |
| Uso de Gu que exija sangue humano ou de parente, com qualquer indício | **+2** |
| Um arco inteiro sem nenhum uso público e sem corpo | **−1** |

| Suspeita | O que acontece |
|---|---|
| **0–2** | Boatos. Nada mecânico |
| **3** | A facção abre **investigação formal**. Todo teste social seu dentro dela sofre **−2**, e você recebe uma escolta que não sai do seu lado |
| **4** | **Falta de grau 4** ([[🏛️ Clãs e Seitas\|Clãs e Seitas]]): suspensão de acesso a Gu, receitas e Pontos de Contribuição. Custa **60 PC ou um Débito selado** pra segurar |
| **5** | **Falta de grau 5: Exílio.** A Origem vira Errante, o clã **sela uma caçada**, e as heranças de sangue param de funcionar. Numa seita: expulsão, 100 PC ou caçada |

### O que não funciona

- **O Gu Devorador de Cadáveres não resolve.** Ele dissolve o corpo em uma hora e **não apaga o sangue já derramado no chão** ([[📖 Catálogo de Gu|Catálogo de Gu]]) — que é exatamente o que um Gu de investigação procura. Some com o corpo e você tirou +2; a poça continua valendo +1.
- **Testemunha viva é o problema, não a prova.** Matar a testemunha resolve a Suspeita e cria um segundo crime, que é como praticamente todo cultivador de Sangue do cânone acaba onde acaba.
- **Comprar silêncio funciona, e é a saída cara.** Um **[[🤝 O Débito|Débito]] selado** com quem viu apaga **1 de Suspeita** por testemunha. Você trocou a caçada por uma coleira, e a mesa agora tem um NPC com alavanca permanente sobre o personagem. Esta é a saída que o jogo *quer* que o jogador use.

> **Por que isso é mecânico e não narrativo.** Porque um Caminho barato em essência precisa ser caro em outra moeda, e "as pessoas te olham torto" não é moeda. O trilho de Suspeita é o custo real de operar o Caminho fora de um duelo isolado — e é o que faz o jogador escolher entre ganhar a luta e continuar tendo uma facção. Um cultivador de Sangue competente é, antes de tudo, alguém que **luta onde não há testemunhas**.

### O sangue de parente

O [[📖 Catálogo de Gu|Gu do Crânio de Sangue]] (rank 5, catálogo) eleva a Abertura em **+10%** matando um consanguíneo, com retornos decrescentes (+10%, +5%, +2%…). A Lâmina de Parentesco e o Verme de Sangue de Parentesco operam na mesma lógica.

**Regra fixa:** qualquer uso confirmado de sangue de parente vai a **Suspeita 5 direto**, sem passar pelos degraus, e **não pode ser apagado por Débito** — não existe favor que compre isso. A linhagem inteira do morto vira antagonista permanente da campanha, e a mesa deve criar esse NPC na hora, com nome.

É a única regra desta nota sem válvula de escape, e é de propósito. Ver [[🛤️ Os Caminhos|Os Caminhos]]: a via de avanço do Caminho do Sangue rende Marca em dobro justamente por **sacrificar sangue de parente**. O Caminho recompensa exatamente a coisa que o mundo pune com a morte, e é isso que ele é.

## 🚀 Por que Sangue avança mais rápido — o mapa do atalho

*(📕 O cânone é explícito: o Caminho do Sangue "permite crescimento rápido, com pouquíssima exigência de recursos" — é o Caminho de quem cresce **lutando**, não comprando. Vol. 5; a citação está na decisão 158. Esta seção só junta num lugar só as peças que já existem espalhadas pelo vault — nenhuma regra nova.)*

Um cultivador de Sangue não espera a mesada do clã. O combustível dele anda por aí, dentro dos outros — e cada ferramenta abaixo já está fichada:

| O atalho | O que faz | Onde está | O preço |
|---|---|---|---|
| **A via de avanço** | Toda cena decidida por sacrifício de sangue próprio (ou de parente) rende **Marca em dobro**, e a próxima Calamidade rende +50% | [[🛤️ Os Caminhos]] | O que a via pede é literalmente sangrar |
| **Custo de essência reduzido** | Gu de Sangue custam menos essência que os equivalentes de outros Caminhos — mais ativações por tanque, menos dependência de Pedra | Esta nota (topo) | Pagamento em Vitalidade — a Dívida de Sangue |
| **Pagar ativação em Vitalidade** | Sem essência? O corpo paga. É o único Caminho que continua lutando de tanque vazio | Esta nota, Dívida de Sangue | Teto efetivo de vida encolhendo a cada uso |
| **Lifesteal em combate** | Lua Sangrenta / Lua Cheia Sangrenta devolvem metade do dano como cura — lutar **é** se sustentar | [[📖 Catálogo de Gu]] r3-4 | Só funcionam à noite |
| **Manto Fervente** | Compra +1 a +3 Níveis de Dano na hora, sem preparação, sem condição — o botão de decidir duelo | Esta nota, rank 4 | `N×M` de Dívida e 3 rodadas sem poder ser curado |
| **O sangue de parente** | +10% de Abertura por consanguíneo (Crânio de Sangue), Marca em dobro na via | Seção acima | Suspeita 5 direto, linhagem antagonista pra sempre — o preço que não se paga com dinheiro |

**A leitura de mesa, e o que ela significa pro grupo:** enquanto o resto da mesa precisa de Pedras, receitas e tempo de reclusão, o Jiãotáng — ou qualquer cultivador de Sangue — converte **combate e o próprio corpo** em progressão. Ele vai estar sempre um passo à frente em Marcas e um passo mais fundo na Dívida; a curva dele é mais íngreme nos dois sentidos. O mestre não precisa frear isso: o freio já está embutido (Dívida, Suspeita, e a caçada de toda facção correta) — o cânone descreve o Caminho exatamente assim, rápido e condenado.

---

## Golpes Matadores do Caminho do Sangue

### 🩸 Sentença de Linhagem *(rank 4–5)*
- **Núcleo:** Gu da Lâmina de Parentesco (rank 5)
- **Apoio:** Gu das Correntes Vermelhas (rank 3) · Gu do Manto Fervente (rank 4, declarado em N=3) · Gu da Agulha Vermelha (rank 2)
- **Sequência:** Rodada 1 — a Agulha abre o alvo e aplica *Sangramento*. Rodada 2 — as Correntes prendem e drenam (e já começam a pagar a Dívida que vem por aí). Rodada 3 — o Manto ferve a N=3 e a Lâmina sai contra um alvo preso, sangrando e sem RD.
- **Efeito final:** núcleo no passo **+5**, mais **+3 do combo**, mais **+3 do Manto** = passo **+11**, `16d12 + 128` (8 Níveis acima de d12), ignorando RD, contra um alvo com desvantagem pra resistir. Custo de essência: `(20+20+20+20) × 4` = **320** — ridiculamente barato pro que entrega, porque é Caminho único e ×0,5.
- **🕳️ Brecha — *de preparação*:** o combo inteiro depende de **uma dose de sangue de um parente consanguíneo do alvo, colhida antes**. Sem ela a Lâmina não dispara e o golpe vira três Gu de apoio gastos. Qualquer alvo que saiba disso protege a própria família — ou já matou todos eles, que é o que os inimigos sérios deste cenário fazem.
- **Contragolpe:** **Sangria total do golpe: `5×16 + 3×8 + 2×4` = 112 de Dívida** numa rodada. Um rank 5 com CON +2 tem 160 de máximo: ele termina o golpe em **Seco**, com −4 em FOR e CON e regeneração travada em 50/rodada. Mais **+2 de Suspeita** se houve testemunha.

### 🔗 Colheita de Correntes *(rank 3–4, econômico)*
- **Núcleo:** Gu das Correntes Vermelhas
- **Apoio:** Gu da Agulha Vermelha · um Gu de movimento qualquer que feche a distância
- **Sequência:** Rodada 1 — a Agulha marca e sangra o alvo mais próximo. Rodada 2 — você fecha pra 10 m. Rodada 3 — as Correntes pegam até três alvos já feridos e drenam por 2 rodadas.
- **Efeito final:** passo **+2** do combo sobre o dreno das Correntes (`4d10` por alvo por rodada em vez de `1×M`), três alvos, 2 rodadas — e **tudo isso quita Dívida ponto por ponto**. Contra um grupo de três, devolve até ~90 de Dívida.
- **🕳️ Brecha — *de janela*:** durante as 2 rodadas de dreno, sua **Defesa cai 2** e as correntes são visíveis a 100 m. Qualquer aliado do alvo que ataque **você** em vez de tentar soltar o preso interrompe tudo — as correntes arrebentam se você sofrer dano igual ou maior a `2 × M` numa única rodada.
- **Contragolpe:** só a Sangria de ativação (8) e **+1 de Suspeita**. É o golpe que se usa toda semana — e é o motivo pelo qual o cultivador de Sangue prefere lutar contra grupos: grupo é estoque.

---

## 🤝 Sinergia: Sangue + Força

O par existe porque os dois Caminhos gastam a **mesma coisa** — o corpo — e um deles sabe repor. Vale pra qualquer personagem que cultive os dois (ver [[🛤️ Os Caminhos|Os Caminhos]]: Caminho secundário custa **+50%** de progressão em ambos).

### 1. O Ímpeto paga a Sangria

Um cultivador de Força acumula **Ímpeto** ficando no corpo a corpo e apanhando ([[💪 Caminho da Força|Caminho da Força]]). Um cultivador de Sangue precisa de sangue derramado por perto.

> **Regra de sinergia:** enquanto você tiver **3 ou mais de Ímpeto**, toda Sangria que você pagar custa **`1 × M` a menos** (mínimo 1). O corpo em movimento sangra menos.

**Efeito prático:** o cultivador duplo é o único que consegue manter o Manto Fervente aceso numa luta longa. Ele não paga menos essência — paga menos corpo, e corpo é a moeda que o Caminho do Sangue não consegue regenerar.

### 2. O Manto Fervente amplifica melee

O Gu do Manto Fervente dá `+N Níveis` a **Gu de Sangue e a golpes corpo a corpo**. Isso o coloca dentro da regra central de [[⚔️ Combate|Combate]]:

```
Manto Fervente (N=3) + Gu de Força de rank 5 ativo
→ golpe de arma pesada no passo +1, +3 do Manto, +3 do Gu de Força = passo +7
→ 16d12 + 64 + FOR  (4 Níveis acima de d12; 16 dados do Gu de Força)
```

**Os Níveis somam antes do pool; o `M` — quantos dados você rola — vem do Gu de Força ativo, não do Manto.** É a interação mais forte que a fase mortal permite, e o freio é que o Manto **bloqueia toda cura por 3 rodadas** — exatamente o Caminho que mais apanha, com a cura desligada.

### 3. As Correntes seguram o que a Força arremessa

Alvo *Preso* pelas Correntes Vermelhas não resiste a agarrar: **manobras de agarrar, derrubar e arremessar do Caminho da Força têm sucesso automático** contra alvo preso, sem teste oposto. E um alvo arremessado que ainda esteja preso é puxado de volta ao alcance de 10 m no fim do movimento — ele bate no chão *e* continua na sua mão.

### 4. A conta que não fecha: dois Caminhos de curto alcance

Nenhum dos dois resolve **distância**. Sangue tem 15–30 m de alcance e Força tem 2 m; nenhum tem controle de campo, nenhum tem mobilidade, nenhum tem utilidade fora de combate que valha a mochila. Um inimigo com um Gu de voo e um ataque de 40 m **não perde essa luta** — ele fica em cima, e o Ímpeto zera toda rodada que você passa sem contato.

> **Diga isso ao jogador na cara, antes da criação de ficha.** A build Sangue + Força é a mais direta e mais brutal da mesa dentro de 10 m, e é a mais indefesa fora dela. O terceiro item essencial não é um Gu de dano: é um **Gu de movimento**, e ele vale mais que qualquer coisa nesta nota.

### A ficha do Jiāotáng *(aptidão 76%)*

Referência de mesa pro personagem que cultiva os dois:

| | |
|---|---|
| **Essência** | `76 × 4 × 2^(estágio−1)` = **304** no inicial, **2.432** no pico do rank |
| **Gu carregados** | `(76 ÷ 10) + rank` = **7 + rank** |
| **Gu simultaneamente sustentados** | **3** *(fixo; os Gu de Corpo dele não ocupam vaga)* |
| **Custo típico de um Gu do rank dele** | **20** se for de Sangue *(modificador ×0,5)* · **40** se for de Força |
| **O que trava a ficha dele** | Nunca a essência. É a **Dívida** e o trilho de **Suspeita** |

Com 304 de essência no estágio inicial, Jiāotáng ativa **15 Gu de Sangue** antes do tanque acabar. A Dívida chega primeiro, mas não tão rápido quanto parece: com CON +3 no rank 1 a Vitalidade máxima é 21, a Sangria padrão é `1 × M` = 1, e ele cruza o limiar **Pálido** (25%) na sexta ativação, **Lívido** (50%) na décima primeira e **Colapso** na vigésima primeira. O que realmente aperta é o **Manto Fervente** e qualquer Gu de Sangria pesada: uma única ativação com N=3 no rank 4 são 24 de Dívida de uma vez.

Este é o Caminho: **o tanque nunca é o problema.** O problema é que a barra que ele gasta não regenera por rodada, não volta com descanso curto, e cada ponto dela precisa ser recomprado com sangue de outra pessoa.
