---
atom_id: CA-D-368
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Framework Instance Settings/Confidence/Necessary Information Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
    - "Carrier"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-D-361"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize the necessary-information confidence default

an explicit necessary-information confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
