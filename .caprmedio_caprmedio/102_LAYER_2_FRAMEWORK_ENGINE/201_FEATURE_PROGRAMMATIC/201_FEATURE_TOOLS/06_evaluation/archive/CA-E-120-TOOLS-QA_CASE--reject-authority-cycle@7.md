---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
    - CA-R-833
    - CA-R-838
    - CAPRMEDIO-REQU-030--require-complete-authority-topology-in-strict-mode
---
# Reject authority cycle

## Test case

**Fixture:** Add one `child_of` edge that closes a cycle.

**Expected result:** Fail with the stable authority-cycle diagnostic and a non-zero exit.
