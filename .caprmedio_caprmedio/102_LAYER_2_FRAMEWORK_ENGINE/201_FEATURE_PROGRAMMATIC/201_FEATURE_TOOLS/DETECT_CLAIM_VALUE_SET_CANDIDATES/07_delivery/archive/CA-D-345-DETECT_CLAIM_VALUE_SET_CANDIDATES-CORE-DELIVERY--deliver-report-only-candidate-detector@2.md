---
atom_id: CA-D-345
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES/Carrier
  depends_on:
    continuant:
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES
version: 2
updated_at: 2026-09-12 04:15:08
relations:
  delivery_for:
    - CA-M-238
---
# Deliver Report-Only Candidate Detector

the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/DETECT_CLAIM_VALUE_SET_CANDIDATES/detect_claim_value_set_candidates.py` with focused tests **in** its sibling `tests/` directory.
