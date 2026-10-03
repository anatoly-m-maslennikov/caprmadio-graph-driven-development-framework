---
atom_id: CA-E-428
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-04 03:10:59 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-1385
    - CA-M-258
---
# Admit only two local commit action kinds

## Test case

Present one valid local real-change commit, one valid local Journal-only commit, and separate requests for branch creation, deletion, rename, or switch; upstream or remote selection or configuration; fetch, pull, merge, or rebase; push or force-push; tag creation; and release creation.

## Acceptance criteria

Only the two commit actions can enter the fenced Git gate. Every other request is rejected as outside CAPRMEDIO Tool authority before staging, ref mutation, network access, or repository-configuration change.
