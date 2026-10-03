---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Directory Carrier"
    - "File Carrier"
    - "Atom/Revision/Authoritative Carrier Bundle"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Scope Unit"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1579", "CA-R-1537", "CA-D-460", "CA-D-461", "CA-D-475"]}
---
# Derive Plan decomposition from Carrier nesting

Plan `DECOMPOSES_INTO` **and** `IS_DECOMPOSITION_OF` Relations **must** derive from Plan Carrier Bundle placement:

- a Plan Directory Carrier connects **to** **every** directly nested Plan Carrier Bundle; skip intervening reserved Status directories.
- collapse same-stem Directory **and** File Carriers into **=1** Atom **before** deriving Relations; the matching file is **not** a decomposed Plan **or** a self-edge.
- stop at the next Plan Bundle boundary for direct decomposition; recursive decomposition follows CA-R-1537.
- `03_plan` **and** `03_plan/001_backlog` are **not** Plan Atoms. a Plan directly placed there has **=0** `IS_DECOMPOSITION_OF` Relations, but **may** still have outgoing decomposition from its own Directory Carrier.
- derive the inverse from the same placement facts; do **not** persist an independent decomposition declaration.
- folder nesting represents the Relation between independent Atoms, **not** Claim containment **or** a new Scope Unit.
