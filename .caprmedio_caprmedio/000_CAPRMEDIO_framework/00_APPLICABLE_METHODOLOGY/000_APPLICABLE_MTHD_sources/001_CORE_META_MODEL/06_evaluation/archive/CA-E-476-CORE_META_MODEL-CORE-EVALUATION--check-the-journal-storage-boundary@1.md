---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Journal"
  depends_on:
    - "Journal/Record"
    - "Artifact/Carrier"
    - "Atom"
    - "Project"
    - "Applicable Methodology"
version: 1
updated_at: "2026-09-16 21:24:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1491
    - CA-D-308
    - CA-D-340
---
# Check the Journal storage boundary

## Claim checked

Journal admission checks event **and** storage integrity **without** becoming a Project-conformance gate.

## Cases

1. submit a correctly encoded event describing a conforming Project change.
2. keep that event envelope valid while recording a legacy Atom ID, broken filename, invalid placement, malformed Atom Properties, unresolved Relation, **or** invalid lifecycle transition.
3. change the live Project **after** capture while leaving the sealed historical observation intact.
4. submit unreadable event data, missing required Event identity **or** fields, a digest mismatch, unauthorized append access, **or** an attempt **to** rewrite accepted history.
5. resubmit the same Event identity **and** payload; **then** supply a conflicting payload under that identity.
6. record an action whose separate conformance Evaluation failed **or** remained unresolved.

## Acceptance

- cases 1, 2, 3, **and** 6 remain recordable **without** inventing identities, repairing observed values, **or** claiming a successful conformance verdict.
- case 4 fails storage admission, preserves pending evidence safely, **and** leaves accepted history unchanged.
- an identical retry creates no duplicate record. an identity collision with different payload fails **without** overwriting history.
- conformance Evaluations remain independently available; their verdicts do **not** become prerequisites for recording the facts they evaluate.
- Journal acceptance grants no Project-mutation permission **and** does **not** bypass a separate action's preconditions.

## Failure disposition

report a failed Evaluation **if** the Journal loses recordable evidence because of Project defects, accepts corrupted **or** unauthorized writes, silently changes observations, **or** rewrites accepted history.
