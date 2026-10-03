---
tier: core
version: 3
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-827
  evaluation_for:
    - CA-R-827
subjects:
  governs:
    occurrent:
      - "Project/control"
  depends_on:
    continuant:
      - "Operator"
      - "Project"
      - "CAPRMEDIO Framework Instance"
      - "Atom/Content Role: Evaluation"
cce_version: cce_1
cce_form: evaluation
atom_id: CA-E-229
---
# Evaluate Operator control outside the framework instance

## Claim checked

the Operator controls **every** governed Project part outside the CAPRMEDIO Framework Instance, **and** **every** material change **to** those parts is observable, steerable, interruptible, **and** recoverable under the Operator's current authority.

## Applicable conditions

apply **to** **every** admitted material change class affecting those outside-instance Project parts **and** **after** a material change **to** their authority **or** control mechanisms.

## Check

enumerate **every** governed Project part outside the CAPRMEDIO Framework Instance **and** **every** admitted material change class affecting those parts. for **every** part, demonstrate Operator inspection **and** direction. for **every** change class, demonstrate an Operator-visible state, an admissible steering action, an interruption boundary, **and** a recovery path. evaluate control of the CAPRMEDIO Framework Instance under CA-E-228 rather than including instance-only failures **in** this Evaluation.

## Acceptance

pass **only** **when** **every** governed outside-instance Project part is inspectable **and** directable by the Operator **and** **every** admitted material change class affecting those parts has demonstrated observability, steerability, interruptibility, **and** recoverability under current Operator authority.

## Failure

fail **and** report **every** uncontrolled outside-instance Project part **or** change class missing **any** required control property.
