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
    - CA-R-1136
---
# Preserve carrier bytes after validation failure

## Test case

**Fixture:** Run ACV-002 and compare the complete carrier bytes before and after validation.

**Expected result:** Return the malformed-filename failure while preserving byte-identical carrier content.
