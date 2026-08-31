---
tags:
  - processo
aliases:
  - Lint do Vault
  - Lint
escopo: processo
---

# 🩺 Lint do Vault

Nota de saúde do vault, **editada no lugar** a cada rodada de lint (não criar
nota nova por rodada). O que se verifica está definido no `CLAUDE.md` §5-Lint.
A parte mecânica roda com:

```
python3 "_Processo/ferramentas/lint_vault.py"
```

Ele checa: wikilinks quebrados (resolvendo nome de arquivo **e** aliases,
inclusive com `\|` de tabela) · colisões de alias · notas órfãs · frontmatter
sem `tags`/`aliases`/`escopo`. O que ele **não** pega — contradição com o Log
de Decisões, vazamento de escopo, claim desatualizado — é trabalho de leitura
do agente.

---

## Rodada [2026-08-30] — varredura inicial (instalação do Second Brain)

**Estado geral: excelente.** 144 notas, zero colisão de alias, zero órfã real,
grafo fechado. Achados e o que foi feito:

| Achado | Veredito | Ação |
|---|---|---|
| 9 notas sem campo `escopo` (⛩️ Portal, 🗺️ Mapa, 💡 Sementes, 6 modelos) | mecânico | ✅ corrigido: `sistema` para Portal e modelos (seguindo 🧰 Modelos), `processo` para Mapa e Sementes |
| link-placeholder "nome da nota nova" em 🗄️ Arquivo | falso-positivo | é placeholder intencional de instrução — deixado como está |
| `_Fontes/📥 Fontes.md` e `log.md` órfãs | recém-criadas | ✅ ligadas ao 🗺️ Mapa do Vault nesta mesma rodada |

**Pendências para rodadas futuras (exigem leitura, não script):**

- [ ] Varredura de contradição regra × [[🧭 Log de Decisões]] (76 decisões × pastas 01–06) — nunca feita pelo agente
- [ ] Vazamento de escopo: procurar NPC/lugar nomeado nas pastas 01–06
- [ ] Conferir se todo termo de sistema usado nos guias do Portal existe no [[📔 Dicionário do Sistema]]
- [ ] Checagem de canonicidade sistemática das mecânicas centrais (ranks, refino, Marcas de Dao, Terra Abençoada) contra a pasta 10
