---
subjects:
  - development-flow
  - artifact-model
  - evaluation
  - cce-language
atom_id: CA-E-245
cce_version: cce_1
cce_form: evaluation
version: 2
updated_at: 2026-08-23 03:00:00
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
---
# Validate Task Atoms

## Claim checked

Each Task Atom has one Task Goal, one atomic or composite Task Scope, one Definition of Done, one Autonomous Confidence Threshold, optional bounded Task Details, explicit Task dependencies, and one recorded Task Scope Resolution for each execution.

## Test case

Create valid Tasks with one atomic Scope Expression, `(ALL Atoms WHERE Local Tier = CORE)`, `(Atom ID IN (CA-R-921, CA-R-989))`, nested set functions, property comparisons, atomic and composite falsification conditions, optional bounded Details, an explicit dependency on a Done Task, and each allowed Autonomous Confidence Threshold. For each allowed threshold, test confidence immediately below, equal to, and immediately above the threshold. Then remove or duplicate each required component, use a threshold other than `80`, `90`, `95`, or `98`, encode a threshold as a non-integer, add ungrouped mixed functions, use an unregistered property or function, add an undecidable falsification condition, let Details expand Scope or Goal, imply a dependency only through Work Sequence, and execute against an unrecorded Scope Resolution.

## Acceptance criteria

Every valid fixture resolves to one exact governed-entity set, has one falsifiable completion interpretation, and passes. Confidence below the Autonomous Confidence Threshold blocks autonomous continuation and requests Operator disposition. Confidence equal to or above the threshold permits autonomous continuation. Every invalid fixture fails before Task execution or completion.

## Failure disposition

Record a Concern naming the affected Task component, Autonomous Confidence Threshold, Scope function, dependency, or execution evidence.
