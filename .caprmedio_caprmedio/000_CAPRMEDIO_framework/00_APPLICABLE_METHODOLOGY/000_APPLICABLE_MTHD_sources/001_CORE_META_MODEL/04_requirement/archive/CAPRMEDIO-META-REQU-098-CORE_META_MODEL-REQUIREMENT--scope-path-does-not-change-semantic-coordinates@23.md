---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 23
updated_at: "2026-09-14 23:34:13 +0000"
relations:
  child_of:
    - CA-M-001
    - CAPRMEDIO-REQU-045
atom_id: "CAPRMEDIO-META-REQU-098"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Scope path does not change semantic coordinates

Scope path is a project-relative address containing **`>=0`** operator-labeled structural scopes ordered from broader parent **to** narrower child.

the current project is ambient. Scope **may** govern ownership, applicability, **and** inheritance, but it never changes stable Artifact identity, Artifact form, Content role, **or** Governance locus.
