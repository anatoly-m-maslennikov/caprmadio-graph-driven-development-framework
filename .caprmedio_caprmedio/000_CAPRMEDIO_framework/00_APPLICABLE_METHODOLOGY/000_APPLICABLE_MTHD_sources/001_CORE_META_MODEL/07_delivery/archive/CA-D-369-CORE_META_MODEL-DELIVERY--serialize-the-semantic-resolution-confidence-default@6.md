---
subjects:
  governs: "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
version: 6
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize the semantic-resolution confidence default

an explicit semantic-resolution confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
