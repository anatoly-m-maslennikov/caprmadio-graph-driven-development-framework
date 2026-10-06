---
cce_version: cce_1
cce_form: separation
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Structural Level"
    - "Structural Parent Relation"
    - "Scope Unit/Label"
    - "Operator"
    - "Project Structure"
version: 15
updated_at: "2026-09-17 12:58:37 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
    - CAPRMEDIO-REQU-045
---
# Separate structural levels from scope labels

Structural Level **must** follow declared Scope Unit parentage; a retained level number **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's Structural Level, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.
