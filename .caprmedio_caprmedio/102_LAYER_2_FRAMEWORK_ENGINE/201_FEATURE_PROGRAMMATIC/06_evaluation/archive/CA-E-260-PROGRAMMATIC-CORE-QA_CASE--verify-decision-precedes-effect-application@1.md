---
atom_id: CA-E-260
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - effect-boundary
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-160
  derived_from:
    - CA-A-053
---
# Verify decision precedes effect application

## Claim checked

One PROGRAMMATIC effect is applied only after a deterministic decision supplies
its target, ordering, and expected outcome.

## Applicable conditions

Apply when a component combines a decision with an external effect,
asynchronous work, or lifecycle transition.

## Test case

Evaluate one effect request by observing its decision result before allowing
the declared effect owner to apply it.

## Acceptance criteria

Pass only when the decision result contains the target, ordering, and expected
outcome, and the effect owner reports completion facts without adding,
reordering, or suppressing a decision.

## Failure disposition

Stop the operation and return the missing decision boundary to its owner.
