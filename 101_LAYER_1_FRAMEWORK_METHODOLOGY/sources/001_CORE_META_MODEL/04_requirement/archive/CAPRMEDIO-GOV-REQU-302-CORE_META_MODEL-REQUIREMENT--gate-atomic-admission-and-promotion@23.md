---
subjects:
  governs: "lifecycle"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
version: 23
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  relates_to:
    - "CA-R-1439"
    - "CAPRMEDIO-GOV-REQU-385"
    - "CA-M-279"
---
# Gate atomic admission and promotion

the effective atomic admission strictness setting **must** be **in** (`medium`, `high`).

**at** medium strictness, CAPRMEDIO requires accepted authority, one primary Claim, one enabled Artifact Type, owning Scope, creation provenance, material relations, priority for Concern Atoms **only**, **and** sufficient precision **to** establish a stable Artifact identity **and** initial accepted Revision. optional non-authoritative context **may** remain explicitly unknown.

**at** high strictness, CAPRMEDIO stops **before** emission while **any** material authority, definition, boundary, classification, Scope, lineage, Conflict, **or** Evaluation question remains ambiguous. it asks focused questions **until** the Atom meets the same one-primary-Claim identity standard.

the two levels assess one-step promotion eligibility. promotion is proposed **only** **when** the Claim applies unchanged at the broader enabled Scope **and** always requires explicit Operator acceptance.

admission does **not** prohibit later same-ID Revisions. **every** later change passes the atomic change-class gate; changing the primary Claim identity requires a replacement.
