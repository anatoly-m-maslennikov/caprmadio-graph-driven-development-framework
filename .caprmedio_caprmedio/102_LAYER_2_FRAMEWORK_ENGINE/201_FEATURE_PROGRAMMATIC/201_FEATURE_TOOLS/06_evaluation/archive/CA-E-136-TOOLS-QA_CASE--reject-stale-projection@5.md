---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject stale Projection

## Test case

**Fixture:** Change a Projection source after its recorded `source_frontier` without rebuilding the Projection.

**Expected result:** Fail with the stable stale-Projection diagnostic and a non-zero exit.
