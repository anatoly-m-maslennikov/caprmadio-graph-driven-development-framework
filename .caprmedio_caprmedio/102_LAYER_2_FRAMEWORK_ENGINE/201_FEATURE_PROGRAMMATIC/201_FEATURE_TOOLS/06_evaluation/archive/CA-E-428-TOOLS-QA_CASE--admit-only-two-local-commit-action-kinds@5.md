---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Commit Automation/Autonomy Envelope"
  depends_on: []
version: 5
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-1385
    - CA-M-258
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Admit only two local commit action kinds

## Test case

Present one valid local real-change commit, one valid local Journal-only commit, and separate requests for branch creation, deletion, rename, or switch; upstream or remote selection or configuration; fetch, pull, merge, or rebase; push or force-push; tag creation; and release creation.

## Acceptance criteria

Only the two commit actions can enter the fenced Git gate. Every other request is rejected as outside CAPRMEDIO Tool authority before staging, ref mutation, network access, or repository-configuration change.
