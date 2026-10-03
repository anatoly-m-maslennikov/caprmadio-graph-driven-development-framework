---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Journal"
    - "Projection"
version: 10
updated_at: "2026-09-17 21:22:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-367
    - CA-R-1137
---
# Reject duplicate terminal event

## Test case

**Fixture:** record two terminal Events for the same Work Journal Action identifying one Projection Rebuild under CAPRMEDIO-GOV-REQU-367. events belonging **to** separately identified rebuild Actions are **not** this duplicate fixture.

**Expected result:** fail the duplicate terminal Events for that Action with the stable duplicate-terminal-event diagnostic **and** a non-zero exit.
