---
atom_id: CA-D-345
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES/Carrier"
  depends_on:
    - "Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  delivery_for:
    - CA-M-238
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver Report-Only Candidate Detector

the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/DETECT_CLAIM_VALUE_SET_CANDIDATES/detect_claim_value_set_candidates.py` with focused tests **in** its sibling `tests/` directory.
