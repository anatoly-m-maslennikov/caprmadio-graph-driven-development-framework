---
atom_id: CA-P-1081
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Entities Graph"
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
version: 2
updated_at: "2026-09-13 02:59:43 +0400"
relations:
  depends_on:
    - CA-P-1080
---
# Reconcile Entities Graph authority

the Assignee **must** reconcile the authority for deriving Entity nodes **and** their admitted qualification relations.

## Scope

(selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` limited **to** Entity graph identity, bearer qualification, **and** allowed-value relations); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (an Entity identity is duplicated by its appearance **in** another view **or** a bearer edge is confused with allowed-value membership **or** qualified paths lose their source identity **or** the full graph is forced into a tree **or** a node **or** edge lacks governing source traceability).

## Details

reuse the current Entity, Property, Subject Path, IS_BORNE_BY, **and** IS_ALLOWED_VALUE_OF authority **and** its endpoint constraints. distinguish a hierarchy view from the combined graph; preserve legitimate sharing. do **not** reintroduce a global ordinal-position rule **or** infer new Entity relations from wording. Actions **and** Processes remain separate targets under accepted authority, **not** Entity duplicates. specify sufficient authority under the accepted Content Role boundary; CA-P-1084 owns representation.

assign **every** Claim by the accepted Content Role boundary: R for model **and** selection invariants, M **only** for Implementation choices **or** conventions, E for checks, **and** O for **any** reusable Action **or** Process definition. reuse existing authority; do **not** require an Atom **in** **every** Content Role. D remains with CA-P-1084; Operation-specific composition **and** control-flow schema remain with CA-P-980.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.
