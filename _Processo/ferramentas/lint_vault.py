#!/usr/bin/env python3
"""Lint mecânico do vault: links quebrados, órfãs, aliases duplicados, frontmatter."""
import re, sys, unicodedata
from pathlib import Path
from collections import defaultdict

VAULT = Path("/home/azuatz/Documentos/REVEREND INSANITY")
SKIP_DIRS = {".obsidian"}

notes = {}  # relpath -> text
for p in VAULT.rglob("*.md"):
    if any(part in SKIP_DIRS for part in p.parts):
        continue
    notes[p.relative_to(VAULT)] = p.read_text(encoding="utf-8")

# --- build resolution table: basename (no .md) and aliases -> note
targets = defaultdict(list)  # name -> [relpath]
fm_issues = []
alias_re = re.compile(r"^aliases:\s*$", re.M)

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end]

for rel, text in notes.items():
    base = rel.name[:-3]
    targets[base].append(rel)
    fm = parse_frontmatter(text)
    aliases = []
    if rel.name == "CLAUDE.md":
        pass
    elif fm is None:
        fm_issues.append((rel, "sem frontmatter"))
    else:
        # aliases: list form or inline
        m = re.search(r"^aliases:\s*\[([^\]]*)\]", fm, re.M)
        if m:
            aliases = [a.strip().strip("\"'") for a in m.group(1).split(",") if a.strip()]
        elif re.search(r"^aliases:", fm, re.M):
            block = re.search(r"^aliases:\s*\n((?:\s+-\s+.*\n?)*)", fm, re.M)
            if block:
                aliases = [re.sub(r"^\s+-\s+", "", l).strip().strip("\"'")
                           for l in block.group(1).splitlines() if l.strip()]
        for field in ("tags", "escopo"):
            if not re.search(rf"^{field}:", fm, re.M):
                fm_issues.append((rel, f"sem `{field}`"))
    for a in aliases:
        if a:
            targets[a].append(rel)

# alias/name collisions (same key -> >1 distinct note)
collisions = {k: v for k, v in targets.items() if len(set(v)) > 1}

# --- wikilinks
link_re = re.compile(r"(!?)\[\[([^\]\|#]+)(#[^\]\|]*)?(\|[^\]]*)?\]\]")
broken = []
inbound = defaultdict(set)  # relpath -> set of linking notes
for rel, text in notes.items():
    # strip code blocks to avoid linting examples
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in link_re.finditer(body):
        target = m.group(2).strip().rstrip("\\").strip()
        if "/" in target:  # path link
            cand = target.split("/")[-1]
        else:
            cand = target
        if cand in targets:
            for t in set(targets[cand]):
                inbound[t].add(rel)
        else:
            # non-md embeds (svg/png) — check file existence anywhere
            if any(p.name == cand or p.stem == cand for p in VAULT.rglob("*") if p.is_file()):
                continue
            broken.append((rel, target))

orphans = [rel for rel in notes if not inbound[rel]
           and rel.name != "CLAUDE.md"]

print("=== LINKS QUEBRADOS ===")
for rel, t in sorted(broken):
    print(f"  {rel}  ->  [[{t}]]")
print(f"total: {len(broken)}")

print("\n=== COLISÕES DE ALIAS/NOME ===")
for k, v in sorted(collisions.items()):
    print(f"  '{k}' -> {sorted(set(str(x) for x in v))}")
print(f"total: {len(collisions)}")

print("\n=== NOTAS ÓRFÃS (sem link de entrada) ===")
for rel in sorted(orphans, key=str):
    print(f"  {rel}")
print(f"total: {len(orphans)}")

print("\n=== FRONTMATTER INCOMPLETO ===")
for rel, issue in sorted(fm_issues, key=lambda x: str(x[0])):
    print(f"  {rel}: {issue}")
print(f"total: {len(fm_issues)}")
