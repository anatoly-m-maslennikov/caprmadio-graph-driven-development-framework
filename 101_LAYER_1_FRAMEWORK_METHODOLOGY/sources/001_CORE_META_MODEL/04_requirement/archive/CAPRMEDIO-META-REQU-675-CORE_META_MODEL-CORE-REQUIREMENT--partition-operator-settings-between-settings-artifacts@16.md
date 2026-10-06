---
atom_id: CAPRMEDIO-META-REQU-675
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Operator"
    - "Project Settings"
    - "Project Structure"
    - "Default Settings"
    - "Project Name"
    - "Atom/Identifier/Project Prefix"
    - "Atom"
version: 16
updated_at: "2026-09-15 00:05:45 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-META-REQU-627-CORE_META_MODEL-REQUIREMENT--bind-every-project-scope-unit-graph-value-to-exact-sources
---
# Partition Operator Settings Between Settings Artifacts

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Name **and** Project Atom prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Name **and** Project Atom prefix belong **to** CORE_META_MODEL.
