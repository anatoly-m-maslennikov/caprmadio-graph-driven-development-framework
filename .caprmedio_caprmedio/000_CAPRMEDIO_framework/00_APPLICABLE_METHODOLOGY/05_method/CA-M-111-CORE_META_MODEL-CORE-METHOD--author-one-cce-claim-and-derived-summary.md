---
atom_id: CA-M-111
subjects:
  governs:
    occurrent:
      - Atom Claim Authoring
  depends_on:
    continuant:
      - Claim
      - Atom/Claim/Scope
      - CCE
      - Summary
cce_version: cce_1
cce_form: method
version: 14
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-111-CORE_META_MODEL-CORE-METHOD--author-one-cce-claim-and-derived-summary.md
---
# Author one CCE Claim and derived Summary

**to** author one CAPRMEDIO Atom Claim, the Author **must** perform **all** of:

1. write **`=1`** independently replaceable Claim **in** CAPRMEDIO Controlled English.
2. assign **`=0`** Claim Scope for a Current-scope Atom **or** **`=1`** atomic **or** composite Claim Scope for a Relational Atom.
3. derive one concise Summary from the complete Claim **and** any Claim Scope.
4. derive **every** Translation from the complete Claim **and** any Claim Scope rather than from the Summary.
