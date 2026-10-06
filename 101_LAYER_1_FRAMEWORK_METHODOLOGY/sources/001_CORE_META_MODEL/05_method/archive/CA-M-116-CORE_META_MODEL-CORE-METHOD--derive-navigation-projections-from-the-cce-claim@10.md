---
subjects:
  governs: "Atom Claim Projection"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
cce_version: cce_1
cce_form: method
version: 10
updated_at: "2026-09-14 02:40:31 +0400"
relations: {}
---
# Derive navigation Projections from the CCE Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273 **and** CA-R-1464 rather than regenerating it as an independent Projection.
