---
subjects:
  declared:
    continuant:
      - artifact-model
    occurrent:
      - development-flow
  prerequisite:
    continuant:
      - cce-language
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: 2026-08-25 00:02:08
relations: {}
---
# Validate Task Atoms

## Claim checked

each Task Atom has one effective Author, one effective Assignee, one Task Goal assigned to that Assignee, one atomic or composite Task Scope, one Definition of Done, one Autonomous Confidence Threshold, optional bounded Task Details, explicit Task dependencies, and one recorded Task Scope Resolution for each execution.

## Test case

create valid Tasks with omitted `author` and `assignee` properties, explicit top-level `author` and `assignee` overrides, one atomic Scope Expression, `(all Atoms where Local Tier = CORE)`, `(Atom ID in (CA-R-921, CA-R-989))`, nested set functions, property comparisons, atomic and composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, and each allowed Autonomous Confidence Threshold. verify that omission resolves Author to the Operator and Assignee to one AI Agent and that every Task Goal assigns execution to its effective Assignee. for each allowed threshold, test confidence immediately below, equal to, and immediately above the threshold. then declare multiple Authors or Assignees, use an unresolved explicit Actor, assign the Task Goal to an Actor other than its effective Assignee, remove or duplicate each other required component, use a threshold other than `80`, `90`, `95`, or `98`, encode a threshold as a non-integer, add ungrouped mixed functions, use an unregistered property or function, add an undecidable falsification condition, let Details expand Scope or Goal, imply a dependency only through Work Sequence, and execute against an unrecorded Scope Resolution.

## Acceptance criteria

every valid fixture resolves to exactly one effective Author, exactly one effective Assignee, one exact governed-entity set, and one falsifiable completion interpretation and passes. confidence below the Autonomous Confidence Threshold blocks autonomous continuation and requests Operator disposition. confidence equal to or above the threshold permits autonomous continuation. every invalid fixture fails before Task execution or completion.

## Failure disposition

record a Concern naming the affected Task Author, Task Assignee, Task component, Autonomous Confidence Threshold, Scope function, dependency, or execution evidence.
