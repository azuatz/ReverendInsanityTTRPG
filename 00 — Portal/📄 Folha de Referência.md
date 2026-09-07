---
tags:
  - regra
  - referência-rápida
aliases:
  - Folha de Referência
  - Folha
  - Cheat Sheet
escopo: sistema
---

# 📄 Folha de Referência

O motor inteiro numa página só — **é isto que fica aberto na mesa durante o jogo.** Não é para estudar: é para consultar no meio de uma rodada, em segundos.

> [!tip] Primeira vez olhando para isto?
> Não tente entender a folha inteira. Ela só faz sentido depois de você ler [[⚔️ Combate]] uma vez. As quatro linhas que você mais vai procurar em jogo são:
>
> 1. **`DANO = M d(dado do Caminho) + (M × B)`** — no bloco do motor, dentro da moldura dupla
> 2. **`M por rank = 1 · 2 · 4 · 8 · 16 · 32 · 64 · 128 · 256`** — quantos dados se rola
> 3. **[[#💠 O estágio numa linha|A tabela do estágio]]** — o que muda quando alguém sobe de estágio
>
> Cada bloco tem a nota que o explica na tabela **[[#📍 Onde está a explicação de cada bloco|no fim desta folha]]**.

---

## ⚙️ O motor, em uma página

```
ATRIBUTOS (6, 12 pontos)   FOR · CON · DES · AST · VON · CAR
GRAU DE DENSIDADE (B)      Inicial 0 · Médio 1 · Alto 2 · Pico 3

Vitalidade máxima  = (18 + 3 × CON + 4 × B) × M
Alma máxima        = (16 + 3 × VON + 3 × B) × M
Essência máxima    = % de aptidão × 4 × (1 + 0,5 × (estágio − 1))    [não escala com rank]
Ferimento          = −5% permanente em Vitalidade E Alma máximas

Defesa             = 10 + DES + rank + rank do Gu de movimento ativo
Defesa contra Alma = 10 + VON + 2 × rank    [ataques de Alma miram ESTA]
Acerto melee       = d20 + FOR + (rank + 2)
Acerto de Gu       = d20 + VON + (rank + 2) + rank do Gu
                     [ATAQUE NÃO SOMA TREINO — o bônus de treino é só
                      de perícia, fora de combate. Decisão 215]
                     [não existem armas à distância mundanas — alcance é Gu]
CD dos seus Gu     = 10 + VON + rank do Gu   [+2 se o Caminho for d6]
                     → 65% de acerto entre iguais com Gu dos dois lados
O TURNO            = 1 AÇÃO por personagem, mais o deslocamento (de graça).
                     Sem ação bônus. Ligar um Gu é a ação do turno.
                     Inimigos: Recruta/Guerreiro/Horda 1 · Mestre e Elite 2 ·
                     Chefe 2 a 4 pelo rank. A assimetria é o desenho.
Iniciativa         = d20 + DES, rolada no início do combate
Crítico            = 20 natural: acerta sempre e rola 2 × M dados (B não dobra)

╔═══════════════════════════════════════════════════════════════╗
║  DANO = M d(dado do Caminho)  +  (M × B)                      ║
║         ↑ quantos dados        ↑ bônus POR DADO               ║
╚═══════════════════════════════════════════════════════════════╝
M por rank         = 1 · 2 · 4 · 8 · 16 · 32 · 64 · 128 · 256
B                  = Grau de Densidade + Níveis de Dano excedentes
Níveis de Dano     = sobem o tipo (d4→d6→d8→d10→d12); em d12, viram +1/dado
Cura               = M d8   (não soma B)
RD                 = base × M   [piso: nunca reduz abaixo de M]
                                [duas fontes: vale só a MAIOR, nunca soma]
Dano melee         = 1 dado da arma + FOR          [sem Gu ativo]
                   = (M do Gu de Força) d(arma) + FOR + (M × B)   [com Gu]
Armas              = improvisada d4 · leve d6 · média d8 · pesada d10

DADO POR CAMINHO
  d12  Alma · Espada · Relâmpago            → sem efeito colateral nenhum
  d10  Fogo · Vento · Osso · Metal          → 1 efeito de 1 rodada
   d8  Lua · Luz · Gelo · Sangue · Veneno
       Escravidão · Água · Sombras          → atrito e controle de verdade
   d6  Sabedoria · Terra · Madeira · Sonhos · Formações · Espaço
       Tempo · Informação · Sorte · Humano
       Alimentação · Refino                 → +2 na CD; ignora regras de combate
  (Sombras vira d12 contra quem não sabe onde você está)

DANO SEMPRE ROLADO  Sem média, sem dano fixo — pools grandes rolam em punhados
                    ou num rolador digital

Custo de ativação  = 40 (rank próprio) · 10 · 4 · 1
Modificador de Caminho: Sangue/Carne/Osso ×0,5 · elementais ×1
                        · Alma/Sabedoria/Escravidão/Informação/Sorte ×1,25
                        · Tempo/Espaço/Sonho/Leis ×1,5
                        [o ESTÁGIO NÃO MEXE NO CUSTO — o B vem de graça]
Essência em combate       = NÃO regenera (só Físico Extremo, que é NPC: 10% do tanque,
                            teto 100/rodada · 150 favorável · 200 ideal · 50 hostil)

Gu carregados      = (% ÷ 10) + rank        Gu sustentados = 3 (FIXO; inimigo comum 2)
                                            [+1 acima do teto: 1d6 por turno,
                                             em 1-2 um Gu desliga. Passar disso,
                                             só com Gu de multitarefa]
Vagas de Suporte   = B (só Gu passivos de utilidade/movimento/sentidos)
Teto de Combo      = 2 · 3 · 4 · 5 Gu num Golpe Matador, por estágio
                     [Golpe Matador só existe do RANK 3 em diante]
Golpes registrados = AST + 1                Aliados = CAR + 1
Pontos de Plano    = 2 + maior(AST, CAR)
```

### 📐 As três regras que valem em toda parte

Três convenções gerais que aparecem espalhadas em várias notas — a regra é uma
só, esta é a versão que fica em pé sempre que uma nota específica não disser
outra coisa:

1. **Arredonde sempre para baixo.** `12,7 pedras` são `12`; `3,9 dias` são `3`.
2. **Ordem de resolução de uma ação:** teste → efeito (dano/condição/controle) → RD e reduções → o que sobrar acontece. Nunca aplica RD antes do dano estar rolado.
3. **A mesma fonte nunca soma com ela mesma — vale a maior.** Duas fontes de RD seguem exatamente essa regra: **vale só a maior**, nunca se somam (decisão 223). O mesmo princípio vale para qualquer bônus repetido do mesmo tipo (dois Gu de Vantagem no mesmo teste, dois efeitos idênticos de terreno) que uma nota específica não tenha resolvido de outro jeito.

## 💠 O estágio numa linha

| Estágio | B   | Dano    | VIT   | Alma | Suporte | Combo |
| ------- | --- | ------- | ----- | ---- | ------- | ----- |
| Inicial | 0   | —       | base  | base | 0       | 2     |
| Médio   | 1   | +1/dado | +4×M  | +3×M | 1       | 3     |
| Alto    | 2   | +2/dado | +8×M  | +6×M | 2       | 4     |
| Pico    | 3   | +3/dado | +12×M | +9×M | 3       | 5     |

## ☯️ Depois do rank 6, o domínio ocupa o lugar do estágio

| Domínio | Vislumbre | Pequeno Feito | Mestre | Grão-Mestre | Quase-Supremo | **Grande Mestre Supremo** |
|---|---|---|---|---|---|---|
| **B** | +0 | +1 | +2 | +3 | +4 | **+5, e o pool dobra** |

## 🌩️ Ato imortal · mercado · equipamento

```
CALAMIDADE / PROVAÇÃO
  Etapas            = 5 (CON · VON · atributo mais baixo · AST · VON+domínio)
                      Calamidade Terrestre de rotina usa só 1 · 3 · 5
  CD de cada etapa  = 14 + 2 × (rank − 6) + faixa do Contador (+1/+2/+3/+5)
                      +2 se for Provação Celestial ou acima
  Reduções          = −2 por presságio respondido (numa etapa só)
                      −2 terra Inabalável · −3 Gu de Estabilização
                      (no Catálogo: "Gu da Âncora dos Três Ares")
  Marcas            = proporcionais aos sucessos
  Não passar da maioria = 0 Marcas + 1 Ferimento + 1 Ferimento da Terra

SABEDORIA         = 5% da Alma máxima por ativação (não gasta Essência)
SORTE             = desvia ou devolve uma Ficha de Azar; +1 no Contador por uso

MERCADO MORTAL    Disponibilidade = d20 + lugar (−4 vila · 0 clã · +4 capital
                  · +6 metrópole · +2 negro) vs CD 8 · 12 · 16 · 20 · 24 (rank 1–5)
                  Preço ≈ 500 · 500–1k · 1k–10k · 10k–100k · 100k–1M (rank 1–5)
                  Venda = 40% da tabela · Gu raro: só leilão
CÉU AMARELO       Balcão = 60%, sem teste · Leilão = 60% a 300% (1d6)
  (rank 6+)       Encomenda = 100% + 10% · Monopólio = ×2
                  Anonimato = d20 + CAR + treino vs CD 10 + Assinatura

ARMADURA (RD fixa, NÃO multiplica por M)
  couro 1 · batido 2 · malha 3 · placas 4   [material de fera: +1, uma vez]
ARMAS (passo na Escada)
  improvisada −2 · leve −1 · média 0 · pesada +1

VÍNCULO           1 por personagem · vantagem 1×/sessão · quebrar vira Débito
```

---

**Calibragem central:** três golpes de um Gu do próprio rank derrubam alguém com CON 0, antes de RD.

**Golpe Matador** *(rank 3+; ranks 1-2 não montam)*: cada apoio dá +1 Nível ao núcleo, até o **Teto de Combo do estágio menos um** (Inicial +1 · Médio +2 · Alto +3 · Pico +4); +6 num coletivo de 4. **Brecha obrigatória.** Custo `= (soma dos custos) × (nº de Gu)`, **×2 se híbrido**. Teste `d20 + AST + rank + domínio` vs `10 + (nº de Gu)`, com Retaliação em caso de falha.

---

## 📍 Onde está a explicação de cada bloco

As fórmulas acima estão fechadas de propósito — sem exceções, sem casos de borda. **Quando uma situação da mesa não couber numa delas, a explicação completa está aqui:**

| O que você estava olhando | A regra completa está em |
|---|---|
| Atributos, os 12 pontos, o que cada um faz | [[💪 Atributos]] |
| Vitalidade, Alma, Ferimento, cura, Teste de Morte | [[❤️ Recursos e Dano]] |
| Defesa, Acerto, CD, ordem de turno | [[⚔️ Combate]] |
| A caixa do **dano**, M, B, Níveis de Dano, RD | [[⚔️ Combate]] |
| Dano melee, armas | [[⚔️ Combate]] |
| **Dado por Caminho** — por que Alma é d12 e Terra é d6 | [[🛤️ Os Caminhos]] |
| Essência, custo de ativação, manutenção, regeneração | [[🪜 Ranks e Estágios]] |
| A tabela do **estágio**, Gu carregados e ativos, Vagas de Suporte | [[🪜 Ranks e Estágios]] |
| **Domínio** e o que substitui o estágio depois do rank 6 | [[☯️ Marcas de Dao]] |
| Teto de Combo, Golpe Matador, Brecha, Retaliação | [[⚡ Golpes Matadores]] |
| Golpes registrados, Aliados, **Pontos de Plano** | [[🕵️ Preparação e Informação]] |
| Calamidade e Provação: as 5 etapas, CDs, reduções | [[🌩️ Calamidades e Provações]] |
| O **Contador de Ameaça** que entra na CD da Calamidade | [[⛈️ A Vontade do Céu]] |
| Sabedoria (5% da Alma) e Sorte (Ficha de Azar) | [[🛤️ Os Caminhos]] |
| Mercado mortal, Disponibilidade, preço de venda | [[🏪 O Mercado]] |
| Céu Amarelo: balcão, leilão, anonimato *(rank 6+)* | [[🏪 Céu Amarelo do Tesouro]] |
| Armadura e armas | [[🗡️ Arsenal|05 — Arsenal]] |
| **Vínculo** — 1 por personagem, vantagem 1×/sessão | [[🤝 Vínculos e Acordo de Mesa]] |
| **Débito** — o que acontece quando um Vínculo se quebra | [[🤝 O Débito]] |
| Estatísticas de inimigo e composição de cena | [[⚔️ Ameaças Genéricas por Rank]] |

> [!warning] Se duas notas discordarem
> O [[🧭 Log de Decisões]] é o contrato do sistema. Se uma nota contradiz o Log, **a nota está errada**, não o Log. Esta folha é derivada das notas de regra — se você encontrar divergência entre ela e a nota de origem, a nota de origem manda, e vale corrigir a folha.
