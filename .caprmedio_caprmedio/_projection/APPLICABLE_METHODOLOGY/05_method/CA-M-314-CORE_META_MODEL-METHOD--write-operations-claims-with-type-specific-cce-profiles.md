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
version: 4
updated_at: "2026-10-01 21:41:08 +0400"
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
atom_id: "CA-M-314"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-314-CORE_META_MODEL-METHOD--write-operations-claims-with-type-specific-cce-profiles.md
  source_atom_id: CA-M-314
  source_atom_revision: 4
  source_sha256: a3f8c559979f66d1130dc199f1a842fff3e77e1e589fca77ff32e3276d61bbbc
  original_relations_sha256: 3433384006fce9f2b11a1b99e5e37de2b9ede1c7d33967e50399bef16b0a52de
---
# Summary

Write Operations Claims with Type-specific CCE Profiles

## Scope

Operations Claims written with their admitted Operations Type-specific CCE Profiles.

## Claim

**to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** **then** apply **`=1`** primary Type profile:

1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305-CORE_META_MODEL-METHOD--write-workflow-schemes-using-step-references.
3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.
4. for Actor, define participation, responsibility, capability, authorization, **or** prohibition using **must**, **may**, **must not**, **only**, conditions, **and** explicit boundaries as applicable. do **not** encode one particular execution as reusable Actor authority.

## Details

an Operations Claim **must not** combine more than one primary type profile. subordinate inputs, conditions, results, failures, transitions, **and** effects remain part of the selected type's single operational contribution.
