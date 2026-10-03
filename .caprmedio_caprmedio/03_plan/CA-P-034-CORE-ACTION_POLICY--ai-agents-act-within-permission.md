---
atom_id: CA-P-034
cce_version: cce_1
cce_form: permission
subjects:
  governs:
    continuant:
      - "AI Agent/authority"
  depends_on:
    continuant:
      - "AI Agent"
      - "Operator"
      - "AI Agent Delegation"
version: 6
updated_at: 2026-09-05 01:15:08 +0400
relations:
  child_of:
    - CA-P-033
---
# AI Agents act within permission

an AI Agent has no original authority, **must not** create **or** expand its own authority, **and** **may** perform **or** authorize a governed action **only** **when** a current Operator-established AI Agent Delegation **or** authorization rule identifies that AI Agent **and** permits the complete action, its target, **and** its decision boundary.
