---
atom_id: CA-P-1094
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  depends_on:
    - CA-P-1093
---
# Define Project Structure consistency Evaluations

the Assignee **must** establish falsifiable Evaluations for Project Structure declarations **and** their consistency with represented Project artifacts.

## Scope

CORE_META_MODEL at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`; active E authority for Project Structure, structural references, path bindings, Settings resolution, **and** migration invariants.

## Definition of Done

the Task is **not** Done **if** (an accepted invalid declaration can pass **or** Goal-less units disappear **or** declaration/observation disagreement is hidden **or** tests lack explicit checked authority **or** a corrected manifest is silently inferred from contradictory inputs).

## Details

cover duplicate Names, unresolved/ambiguous parents, self-parenting, cycles, the reserved `PROJECT` root, incorrect Structural Levels, Ordered units missing Local Order, Unordered units carrying Local Order, invalid ordering under governing policy, independent navigational numbers, Labels independent of Type, invalid/colliding paths, required/optional fields, explicit versus inherited Authority Modes, **and** conflicting legacy authority.

cover child units beneath administrative folders, Project/framework-instance isolation, preserved Goal links, declared-but-unmaterialized units, materialized-but-undeclared candidate units, **and** folders that are **not** Scope Units. allow admitted Carrier exceptions rather than assuming every logical parent is a physical directory parent. failed observations **or** confidence gaps cause a visible finding, **not** guessed authority. register checked R/M/D/O targets through current Evaluation relations. this Task defines E Atoms; executable test implementations belong **to** CA-P-1100.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

completion evidence: CA-E-446 **and** CAPRMEDIO-GOV-EVAL-002 were reconciled with authoritative declarations **and** direct consumer use. CA-E-469–471 define schema/hierarchy consistency, declared-versus-observed findings, **and** guarded structural cutover checks. five source changes **and** exact prior revisions were verified. executable fixtures **and** Tool tests remain scheduled under CA-P-1100.
