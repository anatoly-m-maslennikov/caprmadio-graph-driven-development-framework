---
subjects:
  declared:
    continuant:
      - artifact-model
    occurrent:
      - evaluation
  prerequisite:
    continuant:
      - carrier-format
atom_id: CA-E-242
cce_version: cce_1
cce_form: evaluation
version: 6
updated_at: 2026-08-26 15:38:45 +0400
relations:
  evaluation_for:
    - CA-R-731
    - CA-R-948
    - CA-R-956
    - CA-R-957
    - CA-R-958
    - CA-R-959
---
# Validate canonical Atom filenames

## Claim checked

Every Atom filename exposes exactly the facts required by its identity, ownership, Type, target, lifecycle, and derived Summary.

## Test case

Construct a Project Current-scope Atom, non-Project Atom, draft, internal Job, external Project Job, Demand, active revision, and archived revision. Parse and re-render each filename. Then omit, duplicate, reorder, or add each structured component separately.

## Acceptance criteria

Every valid filename round-trips unchanged. Every invalid filename fails with the exact component identified.

## Failure disposition

Record a Concern naming the rejected Carrier and filename component.
