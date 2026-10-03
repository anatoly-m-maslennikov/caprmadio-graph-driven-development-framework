---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Commit Automation/Autonomy Envelope"
  depends_on: []
version: 8
updated_at: "2026-09-17 03:18:06 +0000"
relations: {"evaluation_for":["CA-R-1385","CA-O-037"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Control pause, resume, narrowing, and escalation independently

## Test case

pause **and** narrow an active envelope while work is queued, **then** attempt resume, replacement, **and** expansion from the executor, the original authorizer, **and** the registered independent override authority. repeat **after** an integrity-sensitive failure.

## Acceptance criteria

pause **and** narrowing take effect **before** the next dispatch **or** commit. the executor cannot resume, replace, expand, **or** self-authorize. **only** the registered independent authority **may** resume under the same bounds **or** issue a replacement; expansion **and** integrity recovery require a new explicitly authorized envelope.
