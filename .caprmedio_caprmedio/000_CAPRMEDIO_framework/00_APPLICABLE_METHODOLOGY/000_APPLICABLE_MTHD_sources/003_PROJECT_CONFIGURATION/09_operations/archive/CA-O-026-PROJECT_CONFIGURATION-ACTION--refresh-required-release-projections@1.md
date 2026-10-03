---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Refresh Required Release Projections"
  depends_on:
    - "Action"
    - "Projection"
    - "Artifact/Revision"
    - "Operator"
    - "Journal/Record"
    - "Projection/Type: Reconciled Projection"
    - "Applicable Methodology"
    - "Atom/Claim"
    - "Atom/Content Role: Delivery"
version: 1
updated_at: "2026-09-16 17:31:26 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - "CA-O-025"
    - "CA-O-010"
    - "CA-O-011"
    - "CA-R-1460"
---
# Refresh required release Projections

Refresh Required Release Projections **means** the Action that makes the selected release candidate's required Projections current under their existing governing authority.

1. resolve the exact required Projection set **and** its source Revisions from the selected release gates.
2. retain an existing Projection **when** its governing currentness check passes for those sources; **otherwise** execute its registered derivation **and** Delivery procedure.
3. use the applicable reconciliation Process for a Reconciled Projection, including CA-O-011 for Applicable Methodology. do **not** change projected Claims **to** fix source conflicts.
4. check the resulting Projection against its own required Evaluations **and** current source binding.
5. return the exact checked results **or** the blocking failure; preserve actual execution evidence **in** the shared Journal.

an enabled Projection **not** required by the selected gate does **not** require refresh merely because an Atom changed. unresolved source conflicts, changed source bindings, failed publication, **or** missing required checks block success. this Action does **not** select a new Projection contract, authorize source corrections, **or** infer release readiness from successful refresh alone.
