---
atom_id: CA-D-368
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Confidence/Necessary Information Threshold/Carrier"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Confidence Threshold"
      - "Carrier"
version: 3
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize the necessary-information confidence default

an explicit necessary-information confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
