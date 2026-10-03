---
atom_id: CA-P-032
cce_version: cce_1
cce_form: classification
subjects:
  governs:
    continuant:
      - "Actor/Type"
  depends_on:
    continuant:
      - "Actor"
      - "Type"
      - "Operator"
      - "AI Agent"
version: 4
updated_at: 2026-09-05 01:15:08 +0400
relations:
  child_of:
    - CA-INTENT
---
# Distinguish human Operators from AI Agents

**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
