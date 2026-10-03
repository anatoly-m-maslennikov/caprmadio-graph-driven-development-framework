---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on:
    - "Project Structure"
    - "Scope Unit"
    - "Operator"
    - "Artifact/Carrier"
version: 7
updated_at: "2026-09-17 20:36:34 +0000"
relations:
  method_for:
    - CA-R-1163
    - CA-R-1164
    - CA-R-1165
    - CA-R-1166
    - CA-R-1167
    - CA-R-1168
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register executable Tool folders as active Tool units

## Applicable when

apply **when** an immediate native TOOLS folder has a canonical independently executable deterministic Tool candidate **and** its Scope Unit registration needs reconciliation.

## Procedure

1. resolve the owning Project's authoritative Project Structure declarations, the observed immediate native Tool folders, **and** their canonical executable entrypoints. keep accepted declarations separate from observed materialization.
2. exclude shared libraries, caches, tests, migration collections, **and** other folders that do **not** own a canonical independently executable Tool.
3. resolve **=1** accepted immediate TOOLS child declaration for **every** Tool proposed for admission. **if** the declaration is missing **or** requires correction, obtain explicit per-action Operator acceptance **or** valid delegated authority under CA-R-1058 **before** changing Project Structure. preserve the accepted Name, direct parent, Type, Label, applicable order, navigation number, **and** authority/Implementation Folder bindings required by CA-R-1484. a folder observation alone **must not** authorize those values.
4. verify the declaration against the canonical executable **and** matching authority/Implementation Folder bindings under CA-R-1163. resolve the filename token required by applicable Carrier authority **without** independently redefining structural facts **in** an Atom **or** generated graph. a declared but unmaterialized Tool remains declared; do **not** report it as executable **or** available for MCP exposure.
5. treat an admitted Tool as active **unless** current Project authority **or** Configuration explicitly disables it. allow MCP **to** derive exposure **only** from the current valid Tool frontier.

## Outcome

**every** admitted immediate executable Tool folder has **=1** accepted Tool Scope Unit declaration **and** **=1** deterministic MCP-discoverable identity **without** turning infrastructure folders **or** observed files into structural authority.

## Failure or stop

stop admission on unreadable **or** invalid Project Structure, absent required authorization, a missing **or** ambiguous declaration, no unique canonical executable entrypoint, conflicting Tool identity, invalid authority/Implementation Folder binding, **or** ambiguous enablement. report missing materialization separately; do **not** silently invent a declaration **or** publish an incomplete frontier as current.
