---
atom_id: CA-M-240
cce_version: cce_1
cce_form: method
subjects:
  governs: "Canonical Signature Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Canonical Signature"
    - "CCE Operator"
version: 5
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-M-115
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Restricted CCE Canonical Signatures Without Source Rewrite

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.
