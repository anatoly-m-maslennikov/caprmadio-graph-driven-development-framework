---
atom_id: CA-M-119
subjects:
  governs: "CCE migration"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Projection"
    - "CCE"
    - "Confidence Threshold"
    - "Operator"
    - "AI Agent"
cce_version: cce_1
cce_form: method
version: 12
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-M-115
    - CA-R-380
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Migrate Atoms to a current CCE version

**to** migrate Atoms **to** a current CCE version, the Operator **or** AI Agent **must** convert one Atom at a time, preserve its lifecycle **and** identity, validate its one Claim **and** derived Projections, **and** request Operator disposition **when** semantic confidence is below the effective Confidence Threshold resolved for that migration according **to** CA-M-271.
