---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings authority
version: 10
updated_at: 2026-09-04 04:05:44 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-622--establish-project-configuration-through-rmed
    - CA-R-1052
  relates_to:
    - CAPRMEDIO-META-REQU-627--bind-every-project-scope-unit-graph-value-to-exact-sources
---
# Partition Operator Settings Between Settings Artifacts

operator-selected configuration values **must** be owned by **`=1`** Framework Instance Settings Artifact **or** Project Settings Artifact according to whether they configure the running CAPRMEDIO instance **or** the governed Project. other Atoms own capability definitions, allowed configuration surfaces, constraints, **and** defaults but **must not** duplicate a current selected value as another settings authority.
