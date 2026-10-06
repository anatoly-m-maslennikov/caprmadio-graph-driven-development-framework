---
subjects:
  governs: "artifact-model"
  depends_on: []
version: 17
updated_at: "2026-09-10 06:29:38 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-114-CORE_META_MODEL-CORE-REQUIREMENT--preserve-content-role-boundaries-through-caprmedio-loop
atom_id: "CAPRMEDIO-META-REQU-119"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 10
---
# Requirement — Create Rationale after its subject

a Rationale is an Analysis Atom created **only** **after** **every** specification Atom it explains already exists. the Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

a Rationale follows **and** points **to** its pre-existing specification subjects **without** modifying them.
