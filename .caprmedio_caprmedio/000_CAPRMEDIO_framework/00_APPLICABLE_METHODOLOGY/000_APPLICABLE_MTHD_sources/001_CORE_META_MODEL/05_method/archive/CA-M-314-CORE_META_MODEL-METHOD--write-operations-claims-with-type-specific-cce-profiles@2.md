---
subjects:
  governs: "CCE/Role Profile: Operations"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
    - "Atom/Content Role: Operations/Type: Actor"
    - "CCE Operator"
version: 2
updated_at: "2026-09-22 18:51:52 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1452
    - CA-R-1530
    - CA-R-1563
    - CA-R-1565
    - CA-R-1569
    - CA-M-304
    - CA-M-305
---
# Write Operations Claims with Type-specific CCE Profiles

**to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** then apply exactly one primary type profile:

1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305.
3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.
4. for Actor, define participation, responsibility, capability, authorization, **or** prohibition using **must**, **may**, **must not**, **only**, conditions, **and** explicit boundaries as applicable. do **not** encode one particular execution as reusable Actor authority.

an Operations Claim **must not** combine more than one primary type profile. subordinate inputs, conditions, results, failures, transitions, **and** effects remain part of the selected type's single operational contribution.
