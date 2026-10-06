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
      - "Atom/Content Role: Plan/Type: Task/Claim/Scope"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 15
updated_at: "2026-09-10 04:04:51 +0400"
relations:
  evaluation_for:
    - CA-M-124
    - CA-M-271
    - CA-R-1007
    - CA-R-990
    - CA-R-992
---
# Validate Task Atoms

## Claim checked

**every** Task Atom has one effective Author, one effective Assignee, one Claim assigned to that Assignee, one atomic **or** composite Task Scope, one Definition of Done, one effective Autonomous Confidence Threshold, an optional explicit threshold override, optional bounded Task Details, **and** explicit Task dependencies.

## Test case

create valid Tasks with default **and** explicit Authors **and** Assignees, atomic **and** composite Scope Expressions, atomic **and** composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, standalone Tasks, contained Tasks, **and** permitted thresholds (80, 90, 95, 98, 99) supplied explicitly **or** inherited according **to** CA-M-271; include omitted Task values, nested Epics, **and** scoped Operator input. **then** declare multiple Authors **or** Assignees, assign the Claim to another Actor, remove **or** duplicate a required effective component, leave a Task **without** **any** applicable threshold source, use a threshold outside its permitted domain **or** a non-integer, add ambiguous Scope **or** falsification grouping, let Details expand Scope **or** Claim, imply dependency **only** through Work Sequence, **or** require Epic membership.

## Acceptance criteria

**every** valid fixture resolves to **`=1`** effective Author, **`=1`** effective Assignee, one unambiguous Task Scope, **and** one falsifiable completion interpretation **and** passes. an omitted Task threshold passes **when** **`=1`** effective value resolves according **to** CA-M-271 **without** copying inherited values into the Task. confidence below the effective Autonomous Confidence Threshold blocks autonomous continuation **and** requests Operator disposition. confidence equal **to** **or** above the effective threshold permits autonomous continuation **only** within existing authority. **every** invalid fixture fails **before** Task execution **or** completion.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Scope function, **or** dependency.
