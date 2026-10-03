---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Atom/Content Role"
    - "Atom/Type"
    - "Atom/Status"
    - "Artifact/Carrier"
version: 10
updated_at: "2026-09-17 21:22:35 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1308
    - CA-R-1137
---
# Reject unknown lifecycle directory

## Test case

**Fixture:** add a lifecycle directory whose Status is **not** admitted by the complete qualified Content Role **and** Type path of its owning Atoms. include a directory admitted by that exact path as a control; do **not** substitute a universal Content Role-**only** Status domain.

**Expected result:** fail the unregistered lifecycle directory with the stable unknown-lifecycle-directory diagnostic **and** a non-zero exit. do **not** reject the admitted control on this domain check; retain its other applicable placement rules.
