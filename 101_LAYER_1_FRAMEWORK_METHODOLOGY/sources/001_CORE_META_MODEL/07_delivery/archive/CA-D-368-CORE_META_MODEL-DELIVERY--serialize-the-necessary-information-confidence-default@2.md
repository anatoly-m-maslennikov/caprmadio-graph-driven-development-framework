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
version: 2
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize the necessary-information confidence default

the Framework Instance Settings TOML Carrier **must** encode the necessary-information confidence default as the integer-percentage field `confidence.necessary_information_threshold_percent`.
