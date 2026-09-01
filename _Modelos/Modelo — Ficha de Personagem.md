---
tags: [personagem, ficha]
rank: 1
estágio: inicial
aptidão: 
origem: 
escopo: sistema
---

# 🧑 {{Nome do Personagem}}

> *(uma frase: quem é, e o que quer que ninguém sabe)*

---

## 📊 Atributos

**12 pontos** pra distribuir, todos começam em 0. Custo: 1 ponto até +3, 2 pontos pra ir de +3 a +4. Descer pra −1 devolve 1 ponto. Ver [[💪 Atributos|Atributos]].

| Atributo | Valor | Pra que serve |
|---|---|---|
| **Força** (FOR) | | **Acerto e dano corpo a corpo**, erguer, quebrar, segurar |
| **Constituição** (CON) | | **Vitalidade**, limite de Gu ativos, **portão dos Gu de Corpo**, veneno e fadiga |
| **Destreza** (DES) | | **Defesa**, deslocamento, ordem de turno, **acerto à distância**, furtividade, fuga |
| **Astúcia** (AST) | | Percepção, investigação, **perceber mentira**, refino, criar Golpe Matador |
| **Vontade** (VON) | | **Acerto e CD dos seus Gu**, Alma, resistir a controle mental, medo e loucura |
| **Carisma** (CAR) | | Persuadir, **enganar**, intimidar, liderar, negociar, política de clã |

## 🌟 Cultivo

| Campo | Valor | Como calcular |
|---|---|---|
| **Rank** | 1 | Começa sempre em 1, estágio inicial |
| **Estágio** | Inicial | Inicial → Intermediário → Avançado → Pico |
| **M (multiplicador)** | 1 | 1, 2, 4, 8, 16, 32, 64, 128, 256 por rank |
| **Aptidão** | ___% | `1d80+20`, ou grau sugerido + 1d20. Ver [[🌟 Aptidão e Abertura\|Aptidão e Abertura]] |
| **Grau** | | D (20–39) · C (40–59) · B (60–79) · A (80–99) |

```
Essência máxima   = % de abertura × 4 × 2^(estágio − 1)
Vitalidade máxima = (18 + 3 × CON + 4 × B) × M
Alma máxima       = (12 + 2 × VON + 3 × B) × M
```

| Recurso | Atual / Máximo |
|---|---|
| **Essência** | ___ / ___ |
| **Vitalidade** | ___ / ___ |
| **Alma** | ___ / ___ |
| **Ferimentos** | ___ *(cada um: −5% permanente em Vitalidade e Alma máximas)* |
| **Anos de vida restantes** | ___ / 100 *(ver [[⏳ Longevidade\|Longevidade]])* |

## ⚔️ Combate

| Campo | Valor |
|---|---|
| **Defesa** | `10 + DES + rank + rank do Gu de movimento ativo` |
| **Acerto melee** | `d20 + FOR + (rank + 2) + treino` |
| **Acerto à distância** | `d20 + DES + (rank + 2) + treino` |
| **Acerto de Gu** | `d20 + VON + (rank + 2) + rank do Gu + treino` |
| **CD dos meus Gu** | `10 + VON + rank do Gu` |
| **Arma** | *(passo na Escada: desarmado −2 · leve −1 · média 0 · pesada +1)* |
| **Dano melee** | *(dado do passo)* + FOR **× M do Gu de Força/Transformação ativo** *(sem Gu ativo, sem multiplicador)* |
| **RD** | *(de Gu de defesa: `RD base × M`. Duas fontes: maior + metade da segunda)* |

### 🦴 Gu de Corpo assentados

*(permanentes, não ocupam vaga, não comem. Exigem CON mínima — ver [[⚔️ Combate|Combate]])*

| Gu de Corpo | CON exigida | O que deu | Incompatível com |
|---|---|---|---|
| | | | |

**Níveis de Dano melee permanentes acumulados:** ___ / +4 *(teto)*

---

## 🪱 Gu

**Quantos cabem na Abertura:** `(% de aptidão ÷ 10) + rank` = ___
**Quantos ficam ativos ao mesmo tempo:** `CON + rank` = ___ *(só os sustentados ocupam vaga)*

| Gu | Rank | Efeito | Custo | Alimento | Próxima refeição |
|---|---|---|---|---|---|
| ⭐ *(Gu Vital)* | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

> **⭐ Gu Vital** — o Gu central do personagem. Nunca morre num combo-refino falho (só fica ferido), é sempre o **último** escolhido se algo destruir um Gu ao acaso, e pode subir de rank por Elevação Direta. **Na Ascensão Imortal, ele vira um Gu Imortal de rank 6.**

## ⚡ Golpes Matadores

Máximo de golpes registrados: **AST + 1**. Cada Gu de apoio empurra o núcleo +1 Nível de Dano (até +3). Ver [[⚡ Golpes Matadores|Golpes Matadores]].

### {{Nome do golpe}}
- **Núcleo:** 
- **Apoio:** 
- **Sequência:** 
- **Efeito:** *(passo final × M)*
- **🕳️ Brecha:** *(obrigatória — em que condição ele falha?)*
- **Contragolpe:** *(o que você paga depois)*

---

## 🎭 Personagem

| Campo | |
|---|---|
| **Origem** | *(Ramo Principal · Ramo Secundário/Servo · Discípulo de Seita · Caminho Demoníaco · Errante — ver [[🌱 Origens\|Origens]])* |
| **Tendência de Caminho** | *(nos ranks 1–5 é só uma tendência, não trava nada. Só cristaliza na Ascensão)* |
| **Vínculo com o grupo** | *(uma frase ligando a pelo menos outro jogador)* |
| **O que ele quer** | |
| **O que ele esconde** | |

## 💰 Recursos

| | |
|---|---|
| **Pedras Primordiais** | |
| **Pontos de Plano** | ___ / `2 + maior(AST, CAR)` *(ver [[🕵️ Preparação e Informação\|Preparação e Informação]])* |
| **Aliados/escravos comandados** | ___ / `CAR + 1` |
| **Posses** | |
| **Favores devidos / a receber** | |

## 🎚️ Trilhos especiais

*(só preencha os que se aplicam ao seu personagem — a maioria das fichas usa nenhum)*

| Trilho | Valor | Regra |
|---|---|---|
| **Força de Alma** | ___ homens | *(Caminho da Alma)* ⚠️ **teto mortal 100** — passar mata na hora, sem teste |
| **Contaminação** | ___ | *(Caminho da Alma)* Sobe ao devorar · limiares em 10 / 25 / 50 / 75 / **100** · cai sob lua cheia |
| **Vício em Gu das Tripas** | ___ pedras | *(Caminho da Alma)* VON `CD 14 + pedras já consumidas` pra recusar uma |

---

## ♾️ Só depois da Ascensão Imortal

*(deixe em branco até o rank 6 — a partir daí, **isto** é a progressão, não o rank)*

| Campo | |
|---|---|
| **Caminho cristalizado** | |
| **Marcas de Dao** | *(por Caminho — é o número que importa. Ver [[☯️ Marcas de Dao\|Marcas de Dao]])* |
| **Nível de domínio** | Vislumbre · Pequeno Feito · Mestre · Grão-Mestre · Quase-Supremo · Grande Mestre Supremo |
| **Níveis de Dano do domínio** | *(+1 a +5 nos Gu do seu Caminho)* |
| **Traços de deformação** | *(1 a cada 10.000 Marcas — permanentes)* |
| **Terra Abençoada** | *(tamanho, camada, estabilidade — ver [[🗝️ Terra Abençoada\|Terra Abençoada]])* |
| **Espírito da Terra** | *(tem? qual atitude?)* |
