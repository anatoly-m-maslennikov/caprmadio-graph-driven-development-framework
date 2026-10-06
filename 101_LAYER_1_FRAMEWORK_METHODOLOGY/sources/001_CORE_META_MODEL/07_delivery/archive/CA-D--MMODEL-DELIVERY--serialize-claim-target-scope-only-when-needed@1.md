---
subjects:
  governs: "Atom/Claim/Target Scope/Carrier"
  depends_on:
    - "Current-scope Atom"
    - "Relational Atom"
    - "Atom/Carrier"
cce_version: cce_1
cce_form: serialization
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations: {}
---
# Serialize Claim Target Scope Only When Needed

a Markdown Atom Carrier **must** omit an explicit Claim Target Scope representation **if** its Atom is Current-scope **and** **must** serialize **`=1`** explicit Claim Target Scope **if** its Atom is Relational; omission **must** resolve **to** the Atom's current Scope Unit **and** **must not** mean that the Claim has no Target Scope.
