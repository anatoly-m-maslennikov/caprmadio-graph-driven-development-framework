---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "artifact-model"
  depends_on: []
version: 13
updated_at: "2026-09-10 06:29:38 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-114-CORE_META_MODEL-CORE-REQUIREMENT--preserve-content-role-boundaries-through-caprmedio-loop
---
# Requirement — Create Rationale after its subject

A Rationale is an Analysis Atom created **only** **after** **every** specification Atom it explains already exists. The Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

A Rationale follows **and** points **to** its pre-existing specification subjects **without** modifying them.
