---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Assess Lineage Impact"
  depends_on:
    - "Action"
    - "Atom"
    - "Artifact/Revision"
    - "Relation"
    - "Lineage Impact Analysis"
    - "Operator"
    - "AI Agent"
version: 1
updated_at: "2026-09-17 13:16:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CA-E-002"]}
---
# Assess revision impact through lineage

Assess Lineage Impact **means** the reusable Action that assesses **every** reachable descendant lineage branch of **=1** changed Atom **until** **every** branch has an explicit impact disposition.

apply this Action **when** the Atom:

- receives a new accepted Revision;
- is replaced by a successor; **or**
- moves **to** the archive.

an Operator **or** AI Agent performs this Action within its existing authority. the assessment follows the existing lineage recursively; it does **not** create another cross-Scope Unit dependency graph.
