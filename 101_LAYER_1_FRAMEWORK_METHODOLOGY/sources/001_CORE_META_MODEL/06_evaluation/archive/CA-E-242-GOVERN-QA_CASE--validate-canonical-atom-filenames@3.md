---
subjects:
  - artifact-model
  - carrier-format
  - evaluation
atom_id: CA-E-242
cce_version: cce_1
cce_form: evaluation
version: 3
updated_at: 2026-08-23 01:44:00
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

Construct a Project Current-scope Atom, non-Project Atom, draft, internal Goal, external Project Goal, Demand, active revision, and archived revision. Parse and re-render each filename. Then omit, duplicate, reorder, or add each structured component separately.

## Acceptance criteria

Every valid filename round-trips unchanged. Every invalid filename fails with the exact component identified.

## Failure disposition

Record a Concern naming the rejected Carrier and filename component.
