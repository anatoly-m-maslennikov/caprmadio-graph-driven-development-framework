---
atom_id: CA-D-348
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/DERIVE_CCE_CANONICAL_SIGNATURES/Carrier
  depends_on:
    continuant:
      - Tool/DERIVE_CCE_CANONICAL_SIGNATURES
version: 1
updated_at: 2026-09-02 01:12:00 +0400
relations:
  delivery_for:
    - CA-I-002
---
# Deliver CCE Canonical Signature Tool

the Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/DERIVE_CCE_CANONICAL_SIGNATURES/derive_cce_canonical_signatures.py` with focused tests **in** its sibling `tests/` directory.
