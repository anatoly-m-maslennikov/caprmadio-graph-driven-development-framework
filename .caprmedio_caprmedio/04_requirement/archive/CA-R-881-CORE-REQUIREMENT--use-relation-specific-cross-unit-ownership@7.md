---
version: 7
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - "CA-R-1407"
    - "CA-M-001"
cce_version: "cce_1"
cce_form: "obligation"
atom_id: "CA-R-881"
subjects:
  governs: "Project/cross-unit relation ownership"
  depends_on:
    - "Project"
    - "Scope Unit"
    - "Relational Atom"
    - "Atom/Scope"
    - "Atom/Claim/Scope"
    - "Consumer"
    - "Producer"
    - "Atom/Content Role: Requirement/Type: Demand"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use relation-specific cross-unit ownership

cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
