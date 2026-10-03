---
atom_id: CA-I-001
cce_version: cce_1
cce_form: implementation
subjects:
  governs:
    continuant:
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES/Implementation
  depends_on:
    continuant:
      - Claim Value Set Consolidation Candidate Detection
      - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES
version: 1
updated_at: 2026-09-01 22:40:10 +0400
relations:
  implementation_for:
    - CA-M-238
---
# Implement Report-Only Candidate Detection

the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool Implementation **must** deterministically emit a report from the caller-supplied Source frontier **and must not** rewrite, merge, archive, replace, compile, **or** otherwise mutate Source Atoms.
