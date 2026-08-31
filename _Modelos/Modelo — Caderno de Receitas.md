---
tags:
  - gu
  - refino
  - ficha
  - modelo
aliases:
  - Modelo Caderno de Receitas
  - Caderno de Receitas
escopo: sistema
---

# 📜 Modelo — Caderno de Receitas

O registro pessoal das receitas de Gu que **o personagem possui** — pro chat privado do jogador no Discord. Receita é portão (decisão 123): sem ela a fusão não roda, então este caderno é literalmente o mapa do que o personagem consegue refinar. Não confundir com o [[📜 Livro de Receitas de Gu]], que é **do mestre** e lista o que existe no mundo; o caderno só recebe o que foi conquistado em jogo.

Está como Mensagem 9 do [[🎲 Mão do Jogador — Pacote Discord|Pacote Discord]] — entregue quando o primeiro personagem ganhar a primeira receita.

Formato em linhas de texto, não tabela: o Discord não renderiza tabela em bloco de código.

---

## O modelo

```
📜 **CADERNO DE RECEITAS** de ______________
════════════════════════════════
Estados (regra: Refino e Precificação):
 ✅ completa e testada — +15% e vantagem no refino
 📄 completa, não testada — destrava a fusão, sem bônus
    (o 1º refino bem-sucedido promove a ✅)
 🧩 parcial / cópia — só destrava a tentativa,
    e pode estar errada de propósito
Linhagem não se anota: 2 exemplares saudáveis + alimento
em dose tripla → rank seguinte. Todo Mestre Gu sabe de cor.
────────────────────────────────
🧪 ______________________ (r__)
   Fusão: _________ + _________ (+ material: _______)
   Estado: ✅ / 📄 / 🧩
   Origem: ______________________ (de quem, como)
   Já refinei com ela? ___
   Valor de troca: ~___ pedras (faixa do Mercado)
   Notas: ______________________
────────────────────────────────
🧪 ______________________ (r__)
   Fusão: _________ + _________
   Estado: ✅ / 📄 / 🧩
   Origem: ______________________
   Já refinei com ela? ___
   Valor: ~___ · Notas: ______________________
```

---

## De onde vem cada campo

| Campo | Nota de regra |
|---|---|
| Fusão (A + B → Gu) e a Regra de Linhagem | [[📜 Livro de Receitas de Gu]] |
| Os três estados e o que cada um vale no teste | [[🧩 Refino e Precificação]] (modificadores do combo-refino) |
| Valor de troca | [[🏪 O Mercado]] — receita é tesouro; validada e vendível, ainda mais |
| Dedução de receita nova (3 Fragmentos) | [[🧩 Refino e Precificação]], seção "Deduzir uma Receita" |

**Por que o estado importa:** completa e testada dá **+15% e vantagem**; completa mas nunca usada destrava a fusão **sem bônus** até o primeiro sucesso validá-la; parcial ou copiada só destrava — e o mestre pode ter entregado a cópia **errada de propósito**. Anotar a procedência não é capricho: é como o jogador decide em quem confiar.

---

## Exemplo preenchido

```
📜 **CADERNO DE RECEITAS** de Gu Yue Xie Lang
════════════════════════════════
🧪 Gu do Fulgor Lunar (r2)
   Fusão: Gu do Luar + 2× Gu da Luzinha
   Estado: ✅ completa e testada
   Origem: sala de receitas do clã, prêmio da missão
     do desfiladeiro
   Já refinei com ela? sim, 1× (perdi uma Luzinha na
     1ª tentativa — a receita avisa que acontece)
   Valor de troca: ~200 pedras
   Notas: exige noite de lua forte
────────────────────────────────
🧪 Gu de Jade Branco (r2)
   Fusão: Gu do Javali Branco + Gu da Pele de Jade
   Estado: 🧩 cópia — comprada de um mascate em Qing Mao
   Origem: 40 pedras, sem garantia nenhuma
   Já refinei com ela? não
   Valor: ~40 · Notas: o mascate sumiu da cidade uma
     semana depois. Testar com ingredientes baratos antes
```

---

## 📝 Changelog

- `2026-08-31` — Criado a pedido do autor, no formato do Pacote Discord: registro por receita com fusão, os três estados da regra, procedência, validação em jogo e valor de troca.
