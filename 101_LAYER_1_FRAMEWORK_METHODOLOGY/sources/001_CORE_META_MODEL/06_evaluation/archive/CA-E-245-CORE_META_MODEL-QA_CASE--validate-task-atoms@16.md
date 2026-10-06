---
atom_id: CA-E-245
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Task Atom Validation
  depends_on:
    continuant:
      - "Autonomous Confidence Threshold"
      - "Confidence Threshold/source"
      - "Epic"
      - "Framework Instance Settings"
      - "Operator"
      - "Atom/Content Role: Plan/Type: Task"
      - Atom/Claim
      - "Atom/Claim/Scope"
      - "Scope Unit/Scope"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 16
updated_at: "2026-09-11 03:48:46 +0400"
relations:
  evaluation_for:
    - CA-M-124
    - CA-M-271
    - CA-R-1007
    - CA-R-990
    - CA-R-992
    - CA-R-919
    - CA-R-1271
    - CA-M-273
    - CA-D-271
    - CA-D-367
---
# Validate Task Atoms

## Claim checked

**every** Task Atom has one effective Author, one effective Assignee, one Claim assigned to that Assignee, one atomic **or** composite Claim Scope, one Definition of Done, one effective Autonomous Confidence Threshold, an optional explicit threshold override, optional bounded Task Details, **and** explicit Task dependencies.

## Test case

create valid Tasks with default **and** explicit Authors **and** Assignees, atomic **and** composite Scope Expressions, atomic **and** composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, standalone Tasks, contained Tasks, **and** permitted thresholds (80, 90, 95, 98, 99) supplied explicitly **or** inherited according **to** CA-M-271; include omitted Task values, nested Epics, **and** scoped Operator input. **then** declare multiple Authors **or** Assignees, assign the Claim to another Actor, remove **or** duplicate a required effective component, leave a Task **without** **any** applicable threshold source, use a threshold outside its permitted domain **or** a non-integer, add ambiguous Scope **or** falsification grouping, let Details expand Scope **or** Claim, imply dependency **only** through Work Sequence, **or** require Epic membership.

include a Current-scope Task **without** an explicit Claim Scope override, an explicitly narrower target, **and** an explicitly grouped composite target; retain the `Scope` section under CA-D-271. test standalone Tasks **and** Tasks inside nested Epics **without** treating an Epic as a separate Scope Unit. **then** target an ancestor Scope Unit, leave an explicit target unresolved, **or** introduce a second independent Scope Property for the Task.

## Acceptance criteria

**every** valid fixture resolves to **`=1`** effective Author, **`=1`** effective Assignee, one unambiguous Claim Scope, **and** one falsifiable completion interpretation **and** passes. an omitted Task threshold passes **when** **`=1`** effective value resolves according **to** CA-M-271 **without** copying inherited values into the Task. confidence below the effective Autonomous Confidence Threshold blocks autonomous continuation **and** requests Operator disposition. confidence equal **to** **or** above the effective threshold permits autonomous continuation **only** within existing authority. **every** invalid fixture fails **before** Task execution **or** completion.

an omitted Claim Scope override resolves **to** the current Scope Unit's Scope under CA-M-273 **and** CA-D-367; a valid explicit narrower **or** composite target preserves its complete grouping **and** constraints under CA-R-1271. an ancestor target, unresolved explicit target, **or** second independent Scope Property fails. the `Scope` section remains present **without** requiring a duplicated current-scope override.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Scope function, **or** dependency.
