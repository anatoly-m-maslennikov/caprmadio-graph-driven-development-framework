---
atom_id: CA-D-369
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Confidence Threshold"
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize the semantic-resolution confidence default

the Framework Instance Settings TOML Carrier **must** encode the semantic-resolution confidence default as the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
