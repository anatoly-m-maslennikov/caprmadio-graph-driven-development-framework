---
subjects:
  governs: "Atom/Claim/Scope"
  depends_on:
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Scope"
    - "Scope Unit"
    - "Project Structure"
    - "Project"
atom_id: CA-R-947
cce_version: cce_1
cce_form: obligation
version: 15
updated_at: "2026-09-15 00:05:45 +0000"
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
---
# Validate Goal Claim Scope

a Goal Atom **must** identify **`=1`** Claim Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
