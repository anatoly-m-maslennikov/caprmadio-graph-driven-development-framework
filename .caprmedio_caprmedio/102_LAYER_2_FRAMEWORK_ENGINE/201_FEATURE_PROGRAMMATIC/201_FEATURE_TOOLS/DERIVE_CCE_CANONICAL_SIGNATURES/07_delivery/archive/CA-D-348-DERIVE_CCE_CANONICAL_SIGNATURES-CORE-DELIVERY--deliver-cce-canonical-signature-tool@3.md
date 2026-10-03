---
atom_id: CA-D-348
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/DERIVE_CCE_CANONICAL_SIGNATURES/Carrier"
  depends_on:
    - "Tool/DERIVE_CCE_CANONICAL_SIGNATURES"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  delivery_for:
    - CA-M-256
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver CCE Canonical Signature Tool

the Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/DERIVE_CCE_CANONICAL_SIGNATURES/derive_cce_canonical_signatures.py` with focused tests **in** its sibling `tests/` directory.
