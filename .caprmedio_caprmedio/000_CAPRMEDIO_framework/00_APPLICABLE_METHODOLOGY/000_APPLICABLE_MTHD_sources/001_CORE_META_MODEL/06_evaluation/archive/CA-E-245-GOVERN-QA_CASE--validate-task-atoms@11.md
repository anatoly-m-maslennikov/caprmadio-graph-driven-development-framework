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
      - "Atom/Content Role: Plan/Type: Task"
      - Atom/Claim
      - "Atom/Content Role: Plan/Type: Task/Scope"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 11
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Validate Task Atoms

## Claim checked

**every** Task Atom has one effective Author, one effective Assignee, one Claim assigned to that Assignee, one atomic **or** composite Task Scope, one Definition of Done, one Autonomous Confidence Threshold, optional bounded Task Details, explicit Task dependencies, **and** one recorded Task Scope Resolution for **every** execution.

## Test case

create valid Tasks with default **and** explicit Authors **and** Assignees, atomic **and** composite Scope Expressions, atomic **and** composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, standalone Tasks, contained Tasks, **and** thresholds (80, 90, 95, 98, 99). **then** declare multiple Authors **or** Assignees, assign the Claim to another Actor, remove **or** duplicate a required component, use another threshold **or** a non-integer, add ambiguous Scope **or** falsification grouping, let Details expand Scope **or** Claim, imply dependency **only** through Work Sequence, require Epic membership, **and** execute against an unrecorded Scope Resolution.

## Acceptance criteria

**every** valid fixture resolves to **`=1`** effective Author, **`=1`** effective Assignee, one exact governed-entity set, **and** one falsifiable completion interpretation **and** passes. Confidence below the Autonomous Confidence Threshold blocks autonomous continuation **and** requests Operator disposition. Confidence equal to **or** above the threshold permits autonomous continuation. **every** invalid fixture fails **before** Task execution **or** completion.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Scope function, dependency, **or** execution evidence.
