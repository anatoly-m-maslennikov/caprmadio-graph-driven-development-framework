---
atom_id: CAPRMEDIO-GOV-REQU-322
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - "Projection/Type: Implementation Record"
  depends_on:
    continuant:
      - artifact-catalog
project_graph_state:
  artifacts:
    enabled_types:
      - implementation_record
version: 12
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-476--register-change-plan-and-implementation-record-projections
  child_of:
    - CAPRMEDIO-META-REQU-115-CORE_META_MODEL-REQUIREMENT--requirement-use-implementation-record-as-a-projection
    - CA-R-888
  relates_to:
    - CAPRMEDIO-GOV-REQU-313-CORE_META_MODEL-REQUIREMENT--register-catalog-map-and-hub-as-type-values-under-projection
    - CAPRMEDIO-GOV-REQU-342-CORE_META_MODEL-REQUIREMENT--register-implementation-journal
---
# Register the Implementation Record Projection

Implementation Record **means** the internal Type value under Projection that presents current realization, coverage, source-to-target bindings, relevant provenance, **and** unresolved gaps derived from its declared source frontier.

The Projection declares the exact normative Atom, native-target, provenance, **and** **any** registered implementation-lineage frontier it represents. Regeneration replaces its rendered content **without** converting it into an Atom **or** granting it authority over the native project, normative specification, Ops evidence, **or** Verification.

Its storage **and** retention policy is configured separately. A generated runtime copy **may** be disposable; a committed current view **may** be reviewable history. the two storage choices do **not** change the Projection's semantic role.

## Rationale

The predecessor incorrectly bundled Change Plan **and** Implementation Record under one Implementation-role Projection rule. The split preserves the record while routing Change Plan to the new Plan Atom family.
