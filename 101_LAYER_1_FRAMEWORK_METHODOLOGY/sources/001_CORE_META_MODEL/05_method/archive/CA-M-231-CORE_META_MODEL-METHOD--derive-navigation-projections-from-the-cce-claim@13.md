---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
version: 13
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Navigation Projections from the CCE Claim

**to** derive an Atom's navigation values, the Generator **must** read the complete Claim, including **any** applicability restrictions within it,, derive **`=1`** concise source-faithful Summary **when** creating the Atom, **and** derive **every** requested Projection directly from the Claim, including **any** applicability restrictions within it, rather than from the Summary. for an existing Atom identity, retain its Summary **and** check it against those sources; a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.
