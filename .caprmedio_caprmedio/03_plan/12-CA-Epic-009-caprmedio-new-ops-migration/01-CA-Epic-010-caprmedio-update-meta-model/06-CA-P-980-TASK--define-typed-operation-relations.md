---
atom_id: CA-P-980
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Relation"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Atom/Subjects"
    - "Scope Unit"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Actor"
    - "Operator"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Task"
    - "Autonomous Confidence Threshold"
version: 3
updated_at: "2026-09-13 02:51:00 +0400"
relations:
  depends_on:
    - CA-P-1085
---
# Define typed Operation relations

the Assignee **must** establish graph-owned typed relations for Actions **and** Processes.

## Scope

(selected graph **and** Subject relation authority needed for Operations **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((a required relation lacks an owner graph kind, endpoint domains, direction, cardinality, **or** precise contribution) **or** (the same relation fact has independently maintained authority **in** multiple graphs) **or** (GOVERNS **or** DEPENDS_ON is removed merely with the temporal nesting) **or** (dependency is silently interpreted as execution order) **or** (Entity, Process, Action, Term, **and** execution references cannot be resolved coherently)).

## Details

CA-P-1078 through CA-P-1085 own the generic Terms, Entity, direct Subject-link, **and** composed-view authority. consume their accepted results **without** duplicating that work; this Task retains Action/Process composition **and** control-flow relations. the sealed direct-Subjects stage is already applied, remains valid, **and** **must not** be repeated **or** erased. this Task remains Active **and** paused **until** CA-P-1085 is Done **and** the remaining parent sub-Epic has been reviewed. the new prerequisite gates remaining work, **not** the historical completed stage.

cover the required Action-**to**-Process composition **and** explicit control flow, including conditional selection **and** revisiting under accepted conditions **and** the required Atom-**to**-Operation governance/reference cases. admit **only** relation kinds actually needed; the Operator did **not** specify exactly two relation kinds. make the Entity/Process boundary **and** reference domain explicit **without** duplicating identity across graphs. Terms remain project-specific words **or** phrases, **not** executions. do **not** revive dependencies between Scope Units: structural containment remains its own tree. ask about **any** unresolved exact relation name **or** domain below 99% confidence; do **not** freeze a speculative schema.

the approved direct Subjects model records **`=1`** GOVERNS target **and** **`>=0`** DEPENDS_ON targets **in** the Atom's Subjects Property; targets resolve **to** canonical Entity, Action, **or** Process identities. do **not** introduce intermediate Subject/Entity **or** Subject/Reference Properties **or** repeated target-kind fields. direct target values **may** use qualified Subject Paths under the registered relation constraints.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.
