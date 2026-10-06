---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Content Role: Plan/Type: Task"
  depends_on:
    - "Autonomous Confidence Threshold"
    - "Confidence Threshold/source"
    - "Epic"
    - "Framework Instance Settings"
    - "Operator"
    - "Atom/Claim"
    - "Atom/Claim/Structural Entity"
    - "Scope Unit"
    - "Scope Expression"
    - "Atom/Content Role: Plan/Type: Task/Definition of Done"
    - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 18
updated_at: "2026-09-15 21:31:49 +0000"
relations:
  evaluation_for:
    - CA-M-124
    - CA-M-271
    - CA-R-1007
    - CA-R-990
    - CA-R-992
    - CA-R-919
    - CA-R-1271
    - CA-R-1445
    - CA-D-271
    - CA-D-367
---
# Validate Task Atoms

## Claim checked

**every** Task Atom has one effective Author, one effective Assignee, one Claim assigned to that Assignee, one Claim Structural Entity, one Definition of Done, one effective Autonomous Confidence Threshold, an optional explicit threshold override, optional bounded Task Details, **and** explicit Task dependencies.

## Test case

create valid Tasks with default **and** explicit Authors **and** Assignees, atomic **and** composite Scope Expressions restricting the work within the selected Claim Structural Entity, atomic **and** composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, standalone Tasks, contained Tasks, **and** permitted integer thresholds from 0 through 100, including 0, 87, 99, **and** 100, supplied explicitly **or** inherited according **to** CA-M-271; include omitted Task values, nested Epics, **and** scoped Operator input. **then** declare multiple Authors **or** Assignees, assign the Claim to another Actor, remove **or** duplicate a required effective component, leave a Task **without** **any** applicable threshold source, use a threshold outside its permitted domain **or** a non-integer, add ambiguous selection **or** falsification grouping, let Details expand the Claim's restrictions **or** intended result, imply dependency **only** through Work Sequence, **or** require Epic membership.

include a Task **without** an explicit Claim Structural Entity, a Task with an explicit permitted Scope Unit target, **and** Tasks with narrower **or** grouped composite selections **in** their Claims; retain the `Scope` section under CA-D-271 as a Carrier section, **not** an independent Scope Entity. place otherwise identical Tasks directly under **`=1`** Scope Unit, **in** an Epic, **and** **in** nested Epics beneath that same Scope Unit. **then** incorrectly resolve an omitted target **to** an Epic, replace an explicit target with the containing Scope Unit, target an ancestor Scope Unit, **or** leave an explicit target unresolved.

## Acceptance criteria

**every** valid fixture resolves to **`=1`** effective Author, **`=1`** effective Assignee, one unambiguous Claim Structural Entity, **and** one falsifiable completion interpretation **and** passes. an omitted Task threshold passes **when** **`=1`** effective value resolves according **to** CA-M-271 **without** copying inherited values into the Task. confidence below the effective Autonomous Confidence Threshold blocks autonomous continuation **and** requests Operator disposition. confidence equal **to** **or** above the effective threshold permits autonomous continuation **only** within existing authority. **every** invalid fixture fails **before** Task execution **or** completion.

an omitted Claim Structural Entity resolves **to** the nearest containing Scope Unit under CA-R-1445, identically for standalone Tasks **and** Tasks **in** single **or** nested Epics. an explicit permitted target remains unchanged; narrower **or** composite Claim restrictions retain their grouping **without** becoming additional structural targets. an Epic substituted as the default target, an overwritten explicit target, an ancestor Scope Unit target, **or** an unresolved explicit target fails. the `Scope` section remains present **without** requiring a duplicated default reference under CA-D-367.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Claim Structural Entity, selection, **or** dependency.
