---
subjects:
  governs: "CAPRMEDIO Graph/Connectivity"
  depends_on:
    - "General Artifact Graph"
    - "Artifact"
    - "Structural Entity"
version: 5
updated_at: "2026-09-14 21:49:27 +0400"
relations: {}
---
# Connect Every CAPRMEDIO Graph through the General Artifact Graph

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
