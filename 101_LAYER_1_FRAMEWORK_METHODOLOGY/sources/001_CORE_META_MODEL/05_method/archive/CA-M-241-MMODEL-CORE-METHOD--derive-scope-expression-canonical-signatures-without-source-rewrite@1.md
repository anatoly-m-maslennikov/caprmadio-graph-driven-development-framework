---
atom_id: CA-M-241
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Canonical Scope Signature Derivation
  depends_on:
    continuant:
      - Scope Expression
      - Scope Expression/Canonical Scope Signature
      - Atom/Carrier
version: 1
updated_at: 2026-09-01 23:45:22 +0400
relations:
  child_of:
    - CA-M-121
---
# Derive Canonical Scope Signatures Without Source Rewrite

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
