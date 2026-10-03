---
atom_id: CA-P-1078
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Scope Unit"
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
    - CA-P-979
---
# Freeze the derived model view authority boundary

the Assignee **must** freeze the existing authority **and** ownership boundary for the derived model views.

## Scope

(a read-only selection of selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (a relevant existing definition, graph Relation Kind, Subject link rule, Projection rule, **or** competing planned change is unaccounted for **or** the selected source identities **and** revisions are unresolved **or** an existing source Atom is assigned for uncoordinated mutation by multiple following Tasks).

## Details

use CA-R-1318, CA-R-1319, CA-R-1320, CA-R-1335, CA-R-1438, CA-R-1281, CA-R-1246, **and** CA-R-806 as starting points, **not** an exhaustive list. read their current Claims. shared read-only authority prerequisites are permitted. distinguish the Terms Graph, Entities Graph, direct Atom relations, **and** Subjects-based navigation. preserve the completed CA-P-980 direct-Subjects stage; its remaining Operation-specific schema is **not** a prerequisite for this inventory. identify reuse, gaps, proposed replacements, deferred work, **and** ownership **for** **every** following Task. record evidence outside authority sources; this Task changes no source Atoms.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.
