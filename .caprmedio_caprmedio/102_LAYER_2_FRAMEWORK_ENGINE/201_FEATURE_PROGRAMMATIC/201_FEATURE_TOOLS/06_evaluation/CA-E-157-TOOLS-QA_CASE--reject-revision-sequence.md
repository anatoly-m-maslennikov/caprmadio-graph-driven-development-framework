---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Atom/Revision"
    - "Atom/Revision/Updated At"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-17 21:23:05 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1415
    - CA-R-1492
    - CA-R-1137
---
# Reject revision sequence

## Test case

**Fixture:** give an Atom a successive Revision whose Version does **not** increase under CA-R-1415. include a formatting-only Revision with an increased Version **and** the exact preceding Updated At value as a control under CA-R-1492.

**Expected result:** fail the non-increasing Version with the stable revision-sequence diagnostic **and** a non-zero exit. do **not** fail the formatting-only control because Updated At is unchanged. preserve other applicable Revision checks **without** treating a semantic change as formatting.
