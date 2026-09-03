---
tags:
  - regra
  - combate
  - fechado
aliases:
  - Recursos e Dano
escopo: sistema
---

# ❤️ Recursos e Dano

> [!info] Dois símbolos aparecem em quase toda fórmula desta nota
> **M** — quantos dados o rank vale (`1 · 2 · 4 · 8 · 16 · 32 · 64 · 128 · 256`, do rank 1 ao 9). · **Grau de Densidade** — o degrau de estágio dentro do rank (`0` Inicial · `1` Médio · `2` Alto · `3` Pico); é o mesmo número que [[⚔️ Combate]] chama de **B**. Os dois vivem em [[🪜 Ranks e Estágios]].
>
> Qualquer outro termo estranho está em [[📔 Dicionário do Sistema]], uma linha cada.

## Os dois trilhos: Vitalidade e Alma

Todo personagem tem **dois medidores de HP separados**:

- **Vitalidade** — o corpo. Dano físico, dano de Gu de ataque comum, veneno, fogo.
- **Alma** — a mente. Dano de Gu do Caminho da Alma, golpes mortais de sonho/ilusão, certas maldições.

Os dois escalam pela tabela de M do rank **e pelo Grau de Densidade do estágio** (ver [[⚔️ Combate|Combate]] e [[🪜 Ranks e Estágios|Ranks e Estágios]]):

```
Vitalidade máxima = (18 + 3 × CON + 4 × Grau) × M do rank
Alma máxima       = (16 + 3 × VON + 3 × Grau) × M do rank

Grau = 0 (Inicial) · 1 (Médio) · 2 (Alto) · 3 (Pico)
```

> As bases foram calibradas por simulação contra o pool de dados — o porquê dos números está nas decisões 77–82 do [[🧭 Log de Decisões]]; a versão anterior, em [[_Arquivo/❤️ Recursos e Dano (v1 — VIT 12+3CON, sem estágio)|_Arquivo]].

| CON | Vitalidade *(Inicial)* | Vitalidade *(Pico)* | Acertos de um Gu **d10** do seu rank |
|---|---|---|---|
| −1 | `15 × M` | `27 × M` | 3,9 |
| 0 | `18 × M` | `30 × M` | 4,5 |
| +2 | `24 × M` | `36 × M` | 5,9 |
| **+3** *(o padrão)* | **`27 × M`** | **`39 × M`** | **6,5** |
| +4 | `30 × M` | `42 × M` | 7,2 |

**A calibragem:** um personagem comum — Constituição **+3**, que é o valor padrão de atributo desta mesa — aguenta **cerca de seis golpes e meio** de um Gu d10 do próprio rank antes de cair, contando a Redução de Dano mínima. E isso vale **em qualquer estágio**, porque o dano e a carne crescem no mesmo compasso.

**A letalidade varia por Caminho**, e é essa a escala inteira do jogo. Duas leituras, porque a diferença entre elas é grande e as duas aparecem na mesa:

| Caminho do atacante | Contra o alvo padrão *(CON +3, com RD)* | Contra um alvo desprotegido *(CON −1, sem RD)* |
|---|---|---|
| d6 — utilitário | **~11** | ~5 |
| d8 — moderado | **~8** | ~4 |
| d10 — dano alto | **~6,5** | ~3,3 |
| d12 — letalidade direta | **~5,5** | ~2,8 |

> [!warning] Use a coluna da esquerda
> **A coluna da direita descreve o personagem mais frágil que as regras permitem** (Constituição −1, sem RD nenhuma) — quase ninguém. Contra alguém real, o número de acertos mais que dobra. Se você vir `5 / 4 / 3,3 / 2,8` citado por aí como se fosse o caso normal, é a leitura antiga. *(Decisão 252 do [[🧭 Log de Decisões]]; nenhum número de balanceamento mudou, só o rótulo.)*

**Sem níveis de ferimento pra rastrear em combate.** Nada de tabela de penalidade por faixa de HP — é coisa demais pra lembrar no meio de uma cena. Os dois trilhos são só um número que desce. Fora zerar (ver abaixo), a ficha não aplica penalidade automática por estar "machucado" — é a mesa que decide o quanto isso pesa na narração.

## Vitalidade zerada — Teste de Morte

Zerar Vitalidade **não mata na hora**. O personagem cai, inconsciente, à beira da morte. No início de cada um dos turnos seguintes dele, role um **Teste de Morte**: `d20 sem bônus nenhum`.

| Resultado | Efeito |
|---|---|
| 10 ou mais | Estabiliza — não piora neste turno, continua inconsciente |
| 9 ou menos | Piora um degrau |
| 1 natural | Piora dois degraus de uma vez |
| 20 natural | Acorda com 1 de Vitalidade, ainda em perigo mas de pé |

**Três degraus de piora (por acúmulo de falhas) = morte.** Um aliado pode estabilizar o personagem caído com uma ação dedicada perto dele (socorro, um Gu de cura, qualquer coisa que a cena aceite como cuidado real) — estabilizado, ele para de rolar Teste de Morte, mas continua inconsciente até tratamento de verdade ou descanso longo.

**Falhar o Teste de Morte pelo menos uma vez deixa sequela**, mesmo que o personagem estabilize depois. A escolha final é da mesa; o padrão recomendado é **uma** destas duas, nunca as duas pelo mesmo teste falho:

| Sequela | O que é |
|---|---|
| **−1 permanente num atributo** | À escolha do jogador, entre os atributos afetados pela cena |
| **Perder o estágio mais recente** | Regride um estágio dentro do rank atual |

Quem chegou perto da morte sai da cena mais fraco, mesmo sobrevivendo — é o preço de sobrevivente que o tom do jogo pede.

## Alma zerada — Colapso Espiritual

Zerar a Alma **também não mata na hora** — mas o trilho é outro. O personagem desaba **inconsciente** (o corpo está intacto; a mente apagou), e no início de cada turno dele rola o mesmo **Teste de Morte** (`d20 sem bônus`, mesma tabela acima), agora espiritual. A diferença está nas pontas:

- **Três degraus de piora** não matam: a alma se apaga num **coma espiritual** — o personagem não acorda com descanso nem cura de Vitalidade, só com tratamento de verdade (um Gu de cura de Alma ou Gu Médico de **rank 3+**, numa cena dedicada fora de combate).
- **Sobreviver a um Colapso sempre deixa sequela de Alma**: **+1d6 de Contaminação** (se o personagem tem esse trilho — ver [[👻 Caminho da Alma]]) ou **−1 VON** até ser tratado (mesma via do coma: cena dedicada, Gu de rank 3+). A Alma máxima recalcula junto com a VON.
- **A morte real é a segunda queda.** Zerar a Alma de novo **enquanto a sequela não foi tratada** apaga o personagem — sem teste, sem estabilização. A alma rachada não segura o segundo golpe.

O desenho espelha o corpo: a primeira queda nunca mata, a repetição sem cuidado sim. Na prática, um golpe de Alma que apaga alguém tira essa pessoa da cena **e** cria o relógio da campanha — tratar a sequela antes da próxima luta contra qualquer coisa que bata na Alma.

## 💥 Destruição da Abertura — o estado terminal que não é morte

A **Abertura** é o espaço interno que guarda a essência e abriga os Gu do personagem — destruí-la é perder o cultivo inteiro e continuar vivo. É a saída pior que morrer e melhor que sobreviver ileso. **Raro por desenho** — nunca automático, sempre escolha do jogador. *(Decisão 130, inspirada em [[Homebrew 3DeT — Lamúrias do Reverendo]].)*

**Dois gatilhos, e só estes dois:**

| Gatilho | Quando dispara | O que o jogador escolhe |
|---|---|---|
| **1 — Overkill catastrófico** | Um único golpe cujo dano, **já com RD aplicada**, seja igual ou maior que a Vitalidade **máxima** do alvo | Rolar o Teste de Morte normal (risco de morrer, chance de ficar de pé) **ou** aceitar a Destruição garantida (sobrevive, sem risco de morte nesta cena) |
| **2 — O Gu Vital ferido de novo** | O **Gu Vital** (o Gu-identidade do personagem) já está **Ferido** e sofreria um efeito que o feriria outra vez — ver [[💀 A Morte dos Gu]] | Nada: a Abertura colapsa em vez de o Gu resistir mais uma vez |

O gatilho 2 é o limite da proteção do Gu Vital: ele nunca morre por refino ou combate, mas essa blindagem acaba aqui.

**O preço, sempre o mesmo:**

- O personagem **sobrevive fisicamente**.
- **Todos os Gu morrem** — os cadáveres valem metade em refino, como qualquer Gu morto.
- A **Aptidão** (o talento nato, em %) cai a **0%**.
- Vitalidade e Alma recalculam como as de um mortal comum sem cultivo: `M = 1`, Grau de Densidade = 0.

**Reverter exige um Gu Imortal de reconstrução de Abertura** — tesouro de rank 6+ que nunca está à venda — ou um milagre equivalente. É gancho de arco de vingança ou redenção, nunca recurso de rotina.

## Descanso curto e longo

Vitalidade e Verdadeira Essência recuperam pelo mesmo padrão simples:

| Descanso | Recupera |
|---|---|
| **Curto** (uma pausa dentro da cena/sessão — minutos a algumas horas) | Metade do máximo de Vitalidade e de Essência |
| **Longo** (descanso de verdade — durante a narrativa entre cenas, geralmente sono de uma noite) | Tudo — Vitalidade e Essência cheias de novo |

Alma segue a mesma regra de descanso curto/longo, exceto quando a mesa decidir que um dano de Alma específico deixou sequela (algo permanente, tratado à parte, não por descanso).

## Cura por Gu

Gu de cura rola pool, igual a dano — mesmo M (ver [[⚔️ Combate|Combate]]):

```
Cura = M d8   (M = rank do Gu de cura)

Ferimento causado por golpe IMORTAL não é curado por Gu MORTAL,
por mais que se role — a marca no ferimento é de outro patamar.
```

O d8 é o padrão (decisão 14 do [[🧭 Log de Decisões]] — cerca de 25% da barra por ativação). Gu de cura excepcionais usam d10 ou d12; está na ficha de cada um no [[📖 Catálogo de Gu|Catálogo de Gu]].

**Nada soma no pool de cura:** nem **B**, nem Níveis de Potência. A única exceção é o Gu de amplificação do Caminho da Água/Vida, que dá **+1 tipo de dado de cura** (d8 → d10), não cumulativo, teto d12.

## 🩹 Ferimento

Várias regras do sistema cobram "1 Ferimento" — Ativação Forçada, a Ascensão, o Retrocesso de Marca, o contragolpe de Golpe Matador, falha grave de refino. Isto é o que a palavra significa:

> **Um Ferimento é −5% permanente na Vitalidade máxima e na Alma máxima.** Cumulativo. Não impõe penalidade em teste nenhum.

Não é uma condição pra rastrear em combate: é só um teto que desce e não volta sozinho.

**Como se cura:** um Gu de cura de **rank 3 ou superior**, numa cena dedicada fora de combate (não vale no meio da luta), remove **1 Ferimento**. Fora isso, um arco inteiro de recuperação de verdade — reclusão, tratamento, um Gu específico caçado pra isso — remove todos.

## Retrocesso (o contragolpe)

Falhar num refino de Gu (o processo de tornar seu um Gu bruto) ou num **Golpe Matador** (vários Gu disparados como uma jogada só) machuca de volta:

```
R = soma dos ranks de TODOS os Gu envolvidos

Retrocesso em Vitalidade = R × 2
Retrocesso em Alma       = R × 1
```

Quanto mais ambicioso o combo, mais caro sai errar.
