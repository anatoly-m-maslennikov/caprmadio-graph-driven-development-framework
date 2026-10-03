---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "CAPRMEDIO Framework Instance/Carrier Root"
  depends_on:
    - "Framework Instance Settings"
    - "Project"
    - "Directory Carrier"
    - "Carrier/Canonical Address"
priority: medium
version: 1
updated_at: "2026-09-17 13:42:35 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Is the Framework root locator a derived Carrier value?

should D-370's mandatory Framework control-root locator be removed as redundant **or** retained as an explicitly derived, non-authoritative Carrier value?

## Evidence

D-317 fixes the Project-specific Framework root. D-370 nevertheless requires its locator **in** Framework Instance Settings **and** disallows choosing another authority root. D-361 stores explicit instance choices **and** forbids derived structural values as independently editable settings. D-267 requires a fully address-derived Artifact Property **to** have one Carrier encoding. the inspected authority does **not** establish a separate editable root choice **or** the exact exception that would make this locator a checked derived value.

## Principle check

CA-M-002 rejects duplicate authority; CA-M-005 rejects an unnecessary parameter; CA-M-006 requires the locator **and** placement rules **to** agree. a derived readability value is **not** automatically competing authority, but labeling it derived does **not** establish its missing Carrier responsibility **or** authorize an arbitrary new field.

## Disposition

preserve D-370 pending the explicit retained-field **or** retirement decision. do **not** add another root selection, infer a configurable authority root, **or** edit current Settings merely **to** satisfy the old locator rule.
