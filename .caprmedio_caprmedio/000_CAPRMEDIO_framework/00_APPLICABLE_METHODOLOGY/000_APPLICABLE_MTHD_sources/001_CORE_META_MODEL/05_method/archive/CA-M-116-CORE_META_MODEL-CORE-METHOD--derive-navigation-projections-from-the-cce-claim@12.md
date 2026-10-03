---
subjects:
  governs: "Atom Claim Projection"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
version: 12
updated_at: "2026-09-15 23:08:05 +0400"
relations:
  relates_to:
    - CA-M-294
---
# Derive navigation Projections from the CCE Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294. for an existing Atom identity, retain **and** check the Summary under CA-R-1273 **and** CA-R-1464 rather than regenerating it as an independent Projection.
