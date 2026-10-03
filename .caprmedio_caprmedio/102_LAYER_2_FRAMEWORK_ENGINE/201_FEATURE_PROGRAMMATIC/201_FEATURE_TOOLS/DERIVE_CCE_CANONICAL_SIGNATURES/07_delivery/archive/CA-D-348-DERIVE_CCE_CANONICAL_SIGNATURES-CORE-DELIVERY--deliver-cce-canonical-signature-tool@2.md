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
version: 2
updated_at: 2026-09-12 04:15:08
relations:
  delivery_for:
    - CA-M-256
---
# Deliver CCE Canonical Signature Tool

the Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/DERIVE_CCE_CANONICAL_SIGNATURES/derive_cce_canonical_signatures.py` with focused tests **in** its sibling `tests/` directory.
