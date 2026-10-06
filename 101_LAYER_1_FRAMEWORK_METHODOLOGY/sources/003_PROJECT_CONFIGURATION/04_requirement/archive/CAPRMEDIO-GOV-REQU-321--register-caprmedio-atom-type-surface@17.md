---
atom_id: CAPRMEDIO-GOV-REQU-321
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Type
  depends_on:
    continuant:
      - Atom
      - Content Role
version: 17
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface
  child_of:
    - CAPRMEDIO-META-REQU-112-CORE_META_MODEL-REQUIREMENT--admit-atoms-only-where-a-role-has-an-atomic-unit
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
  resolution_of:
    - CAPRMEDIO-GOV-CONC-037--semantic-route-catalog-remains-incomplete
    - CAPRMEDIO-GOV-CONC-051--which-types-complete-the-semantic-route-catalog
---
# Register the CAPRMEDIO Type Surface for Atoms

GOVERNANCE **must** register **every** typed Atom with **`=1`** Content Role value **and** **`<=1`** Type value. Content Role states the Atom's primary semantic contribution, Type states the governed kind within that role, **and** Atom routing admits no additional subtype coordinate.
