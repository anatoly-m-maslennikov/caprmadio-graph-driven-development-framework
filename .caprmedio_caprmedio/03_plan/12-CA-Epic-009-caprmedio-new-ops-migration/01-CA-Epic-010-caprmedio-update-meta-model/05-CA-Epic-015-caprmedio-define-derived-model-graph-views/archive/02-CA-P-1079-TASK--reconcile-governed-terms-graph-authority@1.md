---
atom_id: CA-P-1079
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Terms Graph"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Subjects"
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
version: 1
updated_at: "2026-09-13 02:51:00 +0400"
relations:
  depends_on:
    - CA-P-1078
---
# Reconcile Governed Terms Graph authority

the Assignee **must** reconcile the authority for deriving the Governed Terms Graph from source Atoms.

## Scope

(selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` limited **to** governed vocabulary **and** admitted Term relations); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (the graph requires an independently maintained vocabulary authority **or** a Term is confused with its referent Entity, Action, **or** Process **or** a displayed Term **or** edge lacks source traceability **or** missing **or** conflicting definitions are silently accepted).

## Details

reuse the current Term, Governed Term, **and** Terms Graph definitions. provide sufficient R, M, **and** E authority for selection, faithful derivation, **and** validation; D representation is owned by CA-P-1084. derive **only** admitted Term relations, retain graph-qualified relation identities, **and** report ambiguity instead of inventing definitions **or** edges. no new governed/non-governed identity axis is introduced solely for a view.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.
