---
atom_id: CA-D-369
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-D-361"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize the semantic-resolution confidence default

an explicit semantic-resolution confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
