---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Name"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Scope Unit/Local Order"
    - "Scope Unit/Navigational Order Number"
    - "Goal"
    - "Framework Instance Settings"
    - "Carrier"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1430"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Author Project Structure without competing declarations

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.
