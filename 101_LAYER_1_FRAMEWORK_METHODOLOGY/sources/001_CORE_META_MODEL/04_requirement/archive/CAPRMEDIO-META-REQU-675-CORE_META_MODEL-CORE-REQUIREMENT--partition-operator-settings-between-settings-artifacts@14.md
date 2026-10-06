---
atom_id: CAPRMEDIO-META-REQU-675
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings authority
  depends_on:
    continuant:
      - Operator
      - Project Settings
      - Framework Instance Settings
      - Project Name
      - Atom/Identifier/Project Prefix
      - Atom
      - CORE_META_MODEL
version: 14
updated_at: "2026-09-11 15:22:56 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-627-CORE_META_MODEL-REQUIREMENT--bind-every-project-scope-unit-graph-value-to-exact-sources
---
# Partition Operator Settings Between Settings Artifacts

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Name **and** Project Atom prefix, **or** Framework Instance Settings for CAPRMEDIO behavior **and** configuration choices; Atoms define the permitted settings **without** duplicating current selected values; the definitions **and** storage rules for Project Name **and** Project Atom prefix **must** belong **to** CORE_META_MODEL.
