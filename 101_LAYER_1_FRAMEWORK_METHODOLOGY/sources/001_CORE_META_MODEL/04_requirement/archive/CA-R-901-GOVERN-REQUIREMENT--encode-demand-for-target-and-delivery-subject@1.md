---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-22 05:30:00
relations:
  child_of:
    - CA-R-900
    - CAPRMEDIO-GOV-REQU-731--place-immutable-atom-id-before-mutable-scope-path
    - CA-R-859
  replacement_of:
    - CA-R-883
---
# Encode Demand For target and Delivery subject

Every accepted Demand For Atom uses this filename structure:

```text
<ATOM_ID>-<CURRENT_SCOPE>-[<LOCAL_TIER>-]DEMAND_FOR-<TARGET_SCOPE>--<SUMMARY_SLUG>.<EXT>
```

The Project root omits `<CURRENT_SCOPE>` under the general filename rule.

`<TARGET_SCOPE>` occurs exactly once. It identifies one registered Scope Unit that differs from the current Scope Unit.

The canonical CCE Claim identifies exactly one Delivery Atom in the target Scope Unit. The identified Delivery Atom is the sole subject endpoint of the Demand For Atom.

A Demand For Atom does not declare `semantic_shape: relational`, `relational_endpoints`, `controller`, or `followers`.
