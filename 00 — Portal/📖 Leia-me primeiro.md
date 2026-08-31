---
tags:
  - portal
  - guia
aliases:
  - Leia-me primeiro
  - Convenções do vault
escopo: processo
---

# 📖 Leia-me primeiro

**Como este vault está organizado.** Não é o guia de jogo — é o manual do caderno.

> [!success] Se você vai mestrar e nunca leu o romance
> Não tem problema nenhum, e você não precisa desta nota agora. Vá direto para [[🌏 O Mundo em 10 Minutos]] e depois para o [[🎓 Guia do Mestre Iniciante]] — é tudo o que você precisa para sentar na cadeira do mestre. Se a sua mesa vem de D&D e quer um cenário medieval, siga para [[🏰 Conversão Medieval]].
>
> **Volte aqui quando quiser escrever suas próprias notas** e precisar saber onde cada coisa vai.

---

## 🚀 As quatro notas de navegação

| Nota | Para que serve |
|---|---|
| [[⛩️ Portal]] | **Fixe esta.** Painel principal: por onde começar, os sete pilares, o mapa das pastas |
| [[🗺️ Mapa do Vault]] | Índice de **todo arquivo**, uma linha cada — para achar algo sem reler nada |
| [[📄 Folha de Referência]] | O motor numa página. É esta que fica aberta durante o jogo |
| [[📔 Dicionário do Sistema]] | Todo termo numa linha — o "o que é isso?" universal |

E, quando duas notas discordarem: [[🧭 Log de Decisões]] — **o contrato do sistema. Se uma nota contradiz o Log, a nota está errada.**

---

## ⚖️ A divisão que organiza tudo

| Pastas | O que são | Obrigatório? |
|---|---|---|
| **01 a 06** | **O sistema.** Vale para qualquer campanha, está pronto para usar | ✅ sim |
| **07 a 09** | **Cenário e sessões.** Exemplos e guias — você inventa o seu | ❌ não |
| **10** | **Referência canônica.** Banco de ideias, nunca regra | ❌ não |
| **11** e `_*` | Rascunho, modelos, bastidor e histórico | 🔧 ferramenta |

Se uma nota das pastas 01–06 mencionar um NPC ou lugar específico, **ela vazou escopo** — o exemplo deveria ser genérico. É isso que mantém o sistema reutilizável por outra mesa qualquer.

---

## 🏷️ As propriedades de toda nota

Toda nota traz no topo um bloco de propriedades. Ao criar uma nota nova, preencha os três:

```yaml
---
tags:
  - regra          # assunto
  - indice
aliases:
  - Nome curto     # como você quer poder digitar o link
escopo: sistema    # de onde a nota é portável
---
```

### `tags` — o assunto

`#regra` `#cultivo` `#gu` `#personagem` `#inimigo` `#item` `#lore` `#sessão` `#guia` `#referência` `#indice` `#processo` `#segredo` `#fechado`

> Escreva em formato de lista (um `- item` por linha), que é o que o editor de propriedades do Obsidian usa. O formato antigo `tags: [a, b]` também funciona, mas o vault está padronizado no primeiro.

### `aliases` — os nomes alternativos

Os nomes das notas têm emoji, o que é bonito e péssimo para digitar. Os aliases resolvem isso: [[⚙️ Fundação]] atende também por `[[Fundação]]` e por `[[01 — Fundação]]`.

**Regra ao criar um alias:** ele não pode dar em duas notas diferentes. As notas de lore, por exemplo, usam o prefixo `Vespéria — ` justamente por isso — [[Clãs e Seitas]] é a **regra** (pasta 04) e [[Vespéria — Clãs e Seitas]] é o **mundo** (pasta 09).

### `escopo` — de onde a nota é portável

| `escopo:` | Significa | Vive em |
|---|---|---|
| `sistema` | Regra genérica, vale para qualquer mesa que use este sistema | `01`–`06` |
| `campanha` | Específico de uma campanha: elenco, lugares, eventos | `07`–`09` |
| `referência` | Material do romance — inspiração, **nunca regra da mesa** | `10` |
| `processo` | Meta: decisões de design, auditorias, histórico | `_Processo`, `_Arquivo` |

---

## 🗂️ Como as pastas funcionam

- **Toda pasta tem uma nota-mãe** — inclusive `_Modelos`, `_Processo` e `_Arquivo`. Ela é índice do assunto, não regra detalhada: diz o que ler, em que ordem, e o que dá para pular.
- As regras detalhadas ficam em notas irmãs dentro da mesma pasta.
- [[🧰 Modelos|_Modelos]] guarda os formulários em branco. **Regra nova não tem modelo:** ela nasce na nota do assunto e é registrada no [[🧭 Log de Decisões]].
- [[🧭 Processo|_Processo]] guarda o Log e as auditorias — **edite no lugar**, não crie uma nota nova por rodada de revisão.
- [[🗄️ Arquivo|_Arquivo]] é a válvula de escape: regra **substituída** vai para lá, renomeada com a versão entre parênteses, em vez de ser apagada ou deixada duplicada na pasta ativa.
- [[💡 Sementes|11 — Sementes]] é a caixa de entrada: toda ideia solta cai lá e você segue em frente.

> [!note] Ao criar uma nota, faça uma coisa a mais
> **Ligue-a a partir da nota-mãe da pasta.** Uma nota que ninguém aponta é uma nota que ninguém acha — nem a busca por tag, nem o grafo, nem você daqui a três meses.

---

## ⚠️ Spoiler

A pasta [[📚 Referência Canônica|10 — Referência Canônica]] tem a trama do romance quase inteira parafraseada, do primeiro capítulo até o confronto final. Ela existe como banco de ideias. **Se você pretende ler a obra algum dia, não abra** — você não perde nada como mestre.

---

## ⚙️ Configuração recomendada do Obsidian

1. **Modelos** — `Configurações → Plugins internos → Modelos`, apontando para `_Modelos`.
2. **Propriedades** — já vêm preenchidas e viram filtros de busca automáticos. Buscas úteis: `["escopo":"sistema"]` para só o que é portável, `tag:#segredo` para o que os jogadores não podem ver.
3. **Grafo** — útil para ver o que ficou isolado. Hoje o vault não tem nenhuma nota órfã; se aparecer uma ilha no grafo, é sinal de que faltou ligá-la à nota-mãe.

---

## ⚠️ O lembrete que importa

Sistemas de RPG morrem por **excesso de escopo**. A ordem que funciona:

> Fundação → Cultivo → Gu → **uma mesa de teste** → só então mundo, arsenal e bestiário.
