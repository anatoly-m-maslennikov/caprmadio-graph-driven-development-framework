---
atom_id: CA-M-241
cce_version: cce_1
cce_form: method
subjects:
  governs: "Canonical Scope Signature Derivation"
  depends_on:
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
    - "Atom/Carrier"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-M-121
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Canonical Scope Signatures Without Source Rewrite

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
