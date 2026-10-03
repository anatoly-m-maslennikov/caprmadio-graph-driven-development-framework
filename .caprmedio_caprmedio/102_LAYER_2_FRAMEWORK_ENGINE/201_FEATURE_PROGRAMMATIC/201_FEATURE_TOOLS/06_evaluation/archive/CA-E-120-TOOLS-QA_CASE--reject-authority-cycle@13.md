---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 13
updated_at: "2026-09-17 03:53:30 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for":["CA-R-1137","CA-R-833","CA-E-481","CAPRMEDIO-REQU-030-REQUIREMENT--require-complete-authority-topology-in-strict-mode"]}
---
# Reject authority cycle

## Test case

**Fixture:** Add one `child_of` edge that closes a cycle.

**Expected result:** Fail with the stable authority-cycle diagnostic **and** a non-zero exit.
