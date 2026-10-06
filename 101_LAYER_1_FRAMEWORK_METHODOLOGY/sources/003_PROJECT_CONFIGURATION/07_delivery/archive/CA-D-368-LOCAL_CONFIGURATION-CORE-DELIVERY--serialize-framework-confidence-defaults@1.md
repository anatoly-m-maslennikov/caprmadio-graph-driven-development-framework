---
atom_id: CA-D-368
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Confidence/Carrier"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Confidence Threshold"
      - "Carrier"
version: 1
updated_at: "2026-09-09 02:24:28 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize framework confidence defaults

the Framework Instance Settings TOML Carrier **must** encode the necessary-information default as `confidence.necessary_information_threshold_percent` **and** the semantic-resolution default as `confidence.semantic_resolution_threshold_percent`, using integer-percentage values.
