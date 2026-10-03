---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Artifact/Carrier"
  depends_on:
    - "Project"
version: 1
updated_at: "2026-09-17 21:23:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Ignore Finder metadata during project validation

## Test case

**Fixture:** compare **otherwise** identical, conforming Project fixtures with **and** **without** a `.DS_Store` entry under the control root.

**Expected result:** exclude `.DS_Store` from governed-Artifact validation **and** return the same governance diagnostics **and** exit status for both fixtures. do **not** emit non-governed-control-root-file solely for that entry, treat it as authority, **or** modify **or** delete it. other selected files remain subject **to** their applicable checks.
