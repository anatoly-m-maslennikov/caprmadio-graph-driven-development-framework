---
atom_id: CA-P-911
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Epic and Task Authority
    occurrent:
      - Plan Structure Authority Update
  depends_on:
    occurrent:
      - CA-P-910
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Epic and Task Authority

**when** CA-P-910 is Done, **then** the Assignee **must** make Epic and Task authority distinguish recursive Relational Artifacts from Plan-role Task Atoms.

## Scope

`((every CA-P-905 frontier entry assigned to EPIC_AND_TASK) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (Epic is classified as an Atom **or** Task is not classified as `Atom/Content Role: Plan/Type: Task` **or** Epic lacks Artifact identity independent from every member Task **or** Epic membership uses any relation other than Delivery-derived CONTAINS and IS_CONTAINED_BY **or** recursive Epic membership is not the transitive closure of direct containment **or** Epic containment permits a direct or transitive cycle **or** local sequence is not scoped to direct members of one Epic **or** a Task is required to belong to an Epic **or** a Task lacks exactly one effective Author and exactly one effective Assignee **or** the default Task Author is not the Operator **or** the default Task Assignee is not an AI Agent **or** a Task lacks exactly one Autonomous Confidence Threshold **or** 99 is not an admitted Autonomous Confidence Threshold **or** Task Job duplicates the intended result already stated by the Task Claim **or** the Epic identifier grammar differs from `CA-Epic-<number>-<scope>-<summary>` **or** CA-P is assigned to an Epic **or** any replaced conflicting authority remains active).

## Details

model Epic as a Relational Artifact whose membership uses only direct or transitive CONTAINS and IS_CONTAINED_BY supplied by Delivery authority. leave Carrier nesting and containment derivation entirely to CA-P-913. permit nested Epics and standalone Tasks. reserve CA-P identities for Plan-role Atoms, including Tasks. keep the Operator interaction convention that an instruction to create an Epic includes creating its Tasks outside the Core Epic identity invariant.
