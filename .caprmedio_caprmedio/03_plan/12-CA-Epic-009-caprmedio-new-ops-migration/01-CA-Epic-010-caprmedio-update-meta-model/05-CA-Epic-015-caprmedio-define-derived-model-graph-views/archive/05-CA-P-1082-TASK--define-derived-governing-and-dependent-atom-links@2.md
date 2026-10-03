---
atom_id: CA-P-1082
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Scope Unit"
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Term"
    - "Entity"
    - "Relation"
    - "Operator"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Task"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-13 02:59:43 +0400"
relations:
  depends_on:
    - CA-P-1081
---
# Define derived governing and dependent Atom links

the Assignee **must** establish source-derived navigation from a Subject target **to** its governing **and** dependent Atoms.

## Scope

(selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` limited **to** direct Subjects links **and** their derived reverse navigation); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (the view omits an admitted governing **or** dependent Atom **or** requires maintained reverse-link fields **or** duplicates a target identity **or** lacks source traceability **or** Subject DEPENDS_ON is interpreted as Task prerequisite, Process control flow, **or** a dependency between Scope Units).

## Details

derive links from scalar `subjects.governs` **and** unique values **in** `subjects.depends_on`. retain **all** selected governing **and** dependent Atoms for **every** target; **`=1`** governed target per Atom does **not** imply **`=1`** governing Atom per target. preserve qualified target identities **and** apply this navigation mechanism **to** admitted Entity, Action, **and** Process targets. reuse the approved direct-link model **without** temporal nesting, wrappers, **or** repeated source target-kind fields. resolve relation graph ownership under CA-R-1246 **and** CA-R-806 **without** treating a composite view as a new owner; ask **if** required ownership remains unresolved. reserve Operation-specific composition **and** flow relation definitions for CA-P-980. specify sufficient authority under the accepted Content Role boundary; D belongs **to** CA-P-1084.

assign **every** Claim by the accepted Content Role boundary: R for model **and** selection invariants, M **only** for Implementation choices **or** conventions, E for checks, **and** O for **any** reusable Action **or** Process definition. reuse existing authority; do **not** require an Atom **in** **every** Content Role. D remains with CA-P-1084; Operation-specific composition **and** control-flow schema remain with CA-P-980.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.
