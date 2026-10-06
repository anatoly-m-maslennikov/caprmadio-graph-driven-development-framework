---
atom_id: CA-O-078
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Reconcile Navigation Numbers"
  depends_on:
    - "Project Structure"
    - "Scope Unit"
    - "Scope Unit/Navigational Order Number"
    - "Scope Unit/Local Order"
    - "Scope Unit/Structural Level"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Carrier"
    - "Directory Carrier/Numeric Prefix"
    - "Implementation Folder"
    - "Operator"
    - "Atom"
    - "Action"
    - "Project Structure Maintenance"

version: 2
updated_at: "2026-09-23 15:59:19 +0000"
relations: {"relates_to": ["CA-R-1483", "CA-R-1484", "CA-R-976", "CA-R-981", "CA-R-983", "CA-M-291", "CA-D-440", "CA-D-442", "CA-D-444", "CA-D-445", "CA-D-297", "CA-D-299", "CA-D-300", "CA-D-380", "CA-O-012", "CA-O-015"]}
---
# Summary

Reconcile Navigation Numbers During Project Structure Migration

## Claim

Reconcile Navigation Numbers **means** the Action that prepares evidence-backed Navigational Order Number values for a bounded Project Structure migration candidate, **without** activating that candidate **or** changing live Carriers.

### Inputs and preconditions

- an accepted inventory of the selected Scope Units **and** the exact current Project Structure bytes, **or** an explicit record that the selected declarations do **not** yet exist.
- separate observations of existing authority **and** Implementation Folder Carriers; the applicable source-layout encoding rules, including the Structural Level width used by existing names.
- available accepted creation-order evidence **and** explicit Operator selections, with their applicable units **and** authorized effects.
- the applicable Project Structure schema **and** an explicit candidate workspace under CA-D-444. an unresolved required input is reported, **not** invented.

### Behavior

1. read existing declarations from the authoritative `project_structure.toml` under CA-D-440. preserve declared navigation values **unless** an authorized Operator selection changes them; folder observations **must not** override them.
2. decode selected authority **and** Implementation Folder observations **only** **where** their admitted source layout uses the numbered convention, whether checking a declaration **or** recovering a missing one. use the actual source width under CA-D-300 **and** decimal rendering under CA-D-380, **not** a newly selected candidate width. retain the observed paths, encoding rule, decoded values, **and** evidence used.
3. compare decoded observations with one another **and** with **any** selected value. **if** observations disagree, report the mismatch **and** required reconciliation. a known authoritative declaration remains authoritative; disagreement does **not** create another structural source.
4. preserve consistent existing numbers during recovery. for a missing value **without** usable encoded evidence, use accepted creation-order evidence under CA-R-981 **or** an explicit Operator selection under CA-R-983. an admitted unnumbered native layout remains valid **without** a forced rename. do **not** infer a value from a parent's prefix, lexical order, filesystem timestamps, **or** guessed chronology.
5. prepare the selected values **in** the bounded candidate **and** identify **any** required Carrier **or** reference repairs separately. preserve other declarations **and** authorized selections; do **not** change parentage, Type, Label, structural Local Order, bindings, **or** other configuration merely **to** fit a navigation number. do **not** emit Name, Order, path, **or** configuration Atoms **to** duplicate TOML declarations.
6. **before** reporting ready, verify that the selected source state remains current. return a ready candidate **only** **when** **every** selected unit has a supported value **and** **every** observed mismatch has an explicit disposition. **otherwise**, return the incomplete candidate **and** the stale **or** unresolved items; do **not** mark candidate preparation complete. request an Operator decision **only** for a selection **or** disposition that applicable authority **and** available evidence do **not** settle.

### Results and effects

- ready: the candidate values, exact input references, evidence for **every** selected number, **and** **any** proposed Carrier/reference repairs.
- blocked: the affected units, paths, declared/observed/proposed values, conflicting **or** missing evidence, **and** decisions still required. an unresolved value is **not** replaced with a placeholder accepted as a real number.
- failed: the failed operation, exact partial candidate state, **and** recoverable evidence; do **not** report partial preparation as completion.

this Action writes **only** its candidate **and** result evidence **in** the selected workspace. it does **not** rename live folders, create Scope Units, change active TOML, **or** activate a candidate. authorization, freshness checks, reference repairs, **and** recoverable cutover remain governed by CA-D-444 **and** the Project Structure Maintenance Workflow CA-O-015. a ready result is **not** approval **or** proof that broader migration checks passed.
