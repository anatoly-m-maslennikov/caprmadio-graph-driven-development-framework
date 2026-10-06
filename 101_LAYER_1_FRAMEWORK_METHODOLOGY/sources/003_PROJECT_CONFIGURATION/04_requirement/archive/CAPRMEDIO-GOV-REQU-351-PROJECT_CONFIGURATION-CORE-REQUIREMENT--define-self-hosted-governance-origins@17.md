---
cce_version: cce_1
cce_form: classification
subjects:
  governs: "Governance Origin"
  depends_on:
    - "Project"
    - "Artifact"
    - "CAPRMEDIO Framework"
    - "Project Configuration"
version: 17
updated_at: "2026-09-17 12:44:19 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Define self-hosted Governance origins

Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CAPRMEDIO-META-REQU-127:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.
