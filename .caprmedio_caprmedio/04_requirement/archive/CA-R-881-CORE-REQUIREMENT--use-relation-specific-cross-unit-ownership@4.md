---
tier: "core"
version: 4
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  child_of:
    - "CA-R-1407"
    - "CA-M-001"
cce_version: "cce_1"
cce_form: "obligation"
subjects:
  governs:
    continuant:
      - "Project/cross-unit relation ownership"
  depends_on:
    continuant:
      - "Project"
      - "Scope Unit"
      - "Relational Atom"
      - "Atom/Scope"
      - "Atom/Claim/Scope"
      - "Consumer"
      - "Producer"
atom_id: "CA-R-881"
---
# Use relation-specific cross-unit ownership

cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
