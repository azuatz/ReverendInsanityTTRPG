---
tags:
  - indice
  - processo
aliases:
  - Processo
escopo: processo
---

# 🧭 Processo

Nota-mãe. **Os bastidores do sistema** — por que as regras são como são, e o que já foi testado.

> [!success] Você não precisa ler nada disto para mestrar
> Estas três notas não contêm regra nenhuma que você vá usar na mesa. Elas existem para responder *"por que essa regra é assim?"* quando a pergunta aparecer — sua ou de um jogador.

---

## As três notas, e quando abrir cada uma

### 🧭 [[🧭 Log de Decisões]] — **a única que você vai mesmo usar**

**O contrato do sistema.** Toda decisão de design está aqui, numerada e organizada por assunto.

**Abra quando:** duas notas parecerem se contradizer, ou quando você quiser mudar uma regra e precisar saber o que ela sustenta. A regra é simples — **se uma nota contradiz o Log, a nota está errada, não o Log.**

### 🎯 [[🎯 Simulação de Combate — Resultados]]

Auditoria quantitativa: **3.000 combates simulados por cenário**, nos ranks 1, 2, 3 e 5, com quatro personagens.

**Abra quando:** você achar que um combate saiu fácil ou letal demais e quiser saber se é o sistema ou foi a sua cena. Também serve se você for mexer nos números — mostra o que já foi medido, para você não quebrar o equilíbrio às cegas.

### 🔍 [[🔍 Auditoria de Coerência da Lore]]

Varredura feita antes de escrever o mundo de Vespéria, caçando o que impediria o mundo de fechar. Encontrou três contradições reais — **e elas foram corrigidas nas notas de regra, não contornadas.**

**Abra quando:** você for construir a sua própria lore e quiser ver que tipo de furo procurar. É um bom checklist do que costuma quebrar num mundo de cultivo.

### 🩺 [[🩺 Lint do Vault]]

A nota de saúde do vault, mantida pelo agente LLM (ver `CLAUDE.md` na raiz).
Cada rodada de lint é editada no lugar aqui: links quebrados, órfãs, frontmatter,
contradições. O script mecânico fica em `_Processo/ferramentas/lint_vault.py`.

**Abra quando:** quiser saber o que ainda está pendente de revisão no vault.

### 🗺️ [[🗺️ Plano de Ingest — Feedback 2026-08-30]]

Roteiro das 10 frentes de trabalho abertas pelo feedback do autor de 2026-08-30
(remoções de combate, economia canônica, cidades grandes, arenas, tempo de
cultivo, imortalidade, Níveis de Dano, heranças, missões e catálogo).

**Abra quando:** for retomar o trabalho no sistema e quiser saber o que falta.

---

## Se você mudar uma regra

Anote no [[🧭 Log de Decisões]]. Uma linha basta: o que mudou e por quê. É isso que impede o vault de virar um monte de regras contraditórias daqui a seis meses — inclusive para você mesmo.

Se a versão antiga da regra ainda tiver valor histórico, mova-a para [[🗄️ Arquivo\|_Arquivo]] em vez de apagar.
