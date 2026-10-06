---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Project"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Structural Parent Relation"
version: 3
updated_at: "2026-09-15 00:05:45 +0000"
relations: {}
---
# Establish Scope Units through Project Structure declarations

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.
