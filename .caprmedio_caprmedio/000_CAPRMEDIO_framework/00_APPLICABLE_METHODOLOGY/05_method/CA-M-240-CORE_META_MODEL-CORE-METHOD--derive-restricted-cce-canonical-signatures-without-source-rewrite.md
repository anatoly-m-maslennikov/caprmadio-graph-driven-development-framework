---
atom_id: CA-M-240
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Canonical Signature Derivation
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Canonical Signature
      - CCE Operator
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-M-115
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-240-CORE_META_MODEL-CORE-METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md
---
# Derive Restricted CCE Canonical Signatures Without Source Rewrite

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.
