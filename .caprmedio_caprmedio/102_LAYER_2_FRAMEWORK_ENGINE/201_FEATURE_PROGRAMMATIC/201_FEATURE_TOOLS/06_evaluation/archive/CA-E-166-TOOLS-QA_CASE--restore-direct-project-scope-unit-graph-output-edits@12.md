---
subjects:
  governs: "project-settings"
  depends_on: []
version: 12
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1070
---
# Restore direct Project Scope Unit Graph output edits

## Test case

**Fixture:** Change one value directly **in** either generated Project Scope Unit Graph output
**without** changing the Configuration Atom **or** an admitted source.

**Expected result:** A read-only generator run reports the outputs stale **and** an
authorized rebuild restores both canonical outputs from Configuration authority,
current graph structure, admitted contributions, **and** Journal inputs.
