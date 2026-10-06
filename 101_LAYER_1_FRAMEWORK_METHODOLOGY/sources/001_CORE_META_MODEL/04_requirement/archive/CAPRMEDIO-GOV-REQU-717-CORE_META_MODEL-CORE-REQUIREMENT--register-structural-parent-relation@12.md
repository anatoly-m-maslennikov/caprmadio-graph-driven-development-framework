---
atom_id: CAPRMEDIO-GOV-REQU-717
subjects:
  governs: "Structural Parent Relation"
  depends_on:
    - "Scope Unit"
    - "Project Structure"
    - "Structural Entity"
cce_version: cce_1
cce_form: definition
version: 12
updated_at: "2026-09-15 00:05:45 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations: {}
---
# Register structural parent relation

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.
