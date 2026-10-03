---
atom_id: CA-E-245
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - Task
  depends_on:
    continuant:
      - Task/Job
      - Task/Scope
      - Task/Definition of Done
      - Task/Autonomous Confidence Threshold
    occurrent:
      - Task Execution
version: 7
updated_at: 2026-08-27 00:50:08 +0400
relations:
  evaluation_for:
    - CA-M-121
    - CA-M-122
    - CA-M-127
    - CA-M-123
    - CA-M-124
    - CA-M-130
    - CA-R-1008
    - CA-R-1009
    - CA-R-1010
    - CA-R-1011
    - CA-R-1043
    - CA-R-1044
    - CA-R-1045
    - CA-R-1046
    - CA-R-1078
    - CA-R-1079
    - CA-R-1080
    - CA-R-1081
    - CA-R-1082
    - CA-R-1083
---
# Validate Task Atoms

## Claim checked

each Task Atom has one effective Author, one effective Assignee, one Task Job assigned to that Assignee, one atomic or composite Task Scope, one Definition of Done, one Autonomous Confidence Threshold, optional bounded Task Details, explicit Task dependencies, and one recorded Task Scope Resolution for each execution.

## Test case

create valid Tasks with omitted `author` and `assignee` properties, explicit top-level `author` and `assignee` overrides, one atomic Scope Expression, `(ALL Atoms WHERE Local Tier = CORE)`, `(Atom ID IN (CA-R-921, CA-R-989))`, nested set functions, property comparisons, atomic and composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, and each allowed Autonomous Confidence Threshold. Verify that omission resolves Author to the Operator and Assignee to one AI Agent and that every Task Job assigns execution to its effective Assignee. For each allowed threshold, test confidence immediately below, equal to, and immediately above the threshold. Then declare multiple Authors or Assignees, use an unresolved explicit Actor, assign the Task Job to an Actor other than its effective Assignee, remove or duplicate each other required component, use a threshold other than `80`, `90`, `95`, or `98`, encode a threshold as a non-integer, add ungrouped mixed functions, use an unregistered property or function, add an undecidable falsification condition, let Details expand Scope or Job, imply a dependency only through Work Sequence, and execute against an unrecorded Scope Resolution.

## Acceptance criteria

every valid fixture resolves to exactly one effective Author, exactly one effective Assignee, one exact governed-entity set, and one falsifiable completion interpretation and passes. Confidence below the Autonomous Confidence Threshold blocks autonomous continuation and requests Operator disposition. Confidence equal to or above the threshold permits autonomous continuation. Every invalid fixture fails before Task execution or completion.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Scope function, dependency, or execution evidence.
