---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "CAPRMEDIO Graph/Connectivity"
  depends_on:
    - "General Artifact Graph"
    - "Artifact"
    - "Structural Entity"
version: 4
updated_at: "2026-09-14 21:49:27 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Connect Every CAPRMEDIO Graph through the General Artifact Graph

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
