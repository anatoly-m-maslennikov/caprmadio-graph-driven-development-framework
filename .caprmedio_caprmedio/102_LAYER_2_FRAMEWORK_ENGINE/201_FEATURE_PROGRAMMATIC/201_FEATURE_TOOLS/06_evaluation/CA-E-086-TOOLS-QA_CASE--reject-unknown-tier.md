---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Atom/Tier/Local Tier"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-17 20:52:41 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-D-285
    - CA-R-1136
---
# Reject unknown tier

## Test case

**Fixture:** give an ordinary RMED Atom an unregistered Local Tier token at the registered Local Tier position **in** its otherwise valid filename under CA-D-285; do **not** encode the tier **in** frontmatter.

**Expected result:** fail with the stable unknown-tier diagnostic **and** a non-zero exit.
