---
atom_id: CAPRMEDIO-META-REQU-675
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings authority
version: 11
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-622-CORE-REQUIREMENT--keep-selected-settings-in-their-authoritative-settings-artifact
    - CA-R-1052
  relates_to:
    - CAPRMEDIO-META-REQU-627-CORE_META_MODEL-REQUIREMENT--bind-every-project-scope-unit-graph-value-to-exact-sources
---
# Partition Operator Settings Between Settings Artifacts

operator-selected configuration values **must** be owned by **`=1`** Framework Instance Settings Artifact **or** Project Settings Artifact according to whether they configure the running CAPRMEDIO instance **or** the governed Project. other Atoms own capability definitions, allowed configuration surfaces, constraints, **and** defaults but **must not** duplicate a current selected value as another settings authority.
