---
subjects:
  governs: "Claim Target Scope Authoring"
  depends_on:
    - "Atom/Claim/Target Scope"
    - "Atom/Scope"
    - "Scope Expression"
    - "Current-scope Atom"
    - "Relational Atom"
cce_version: cce_1
cce_form: method
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations: {}
---
# Author One Claim Target Scope

**to** author an Atom Claim Target Scope, the Author **must** perform **all** of:

1. resolve the Atom's current Scope Unit **or** its admitted non-Scope-Unit ownership boundary.
2. select **`=1`** atomic **or** composite Scope Expression to which the Claim applies.
3. omit an explicit Carrier representation **only if** the resolved Claim Target Scope **`=`** the current Scope Unit.
4. represent a different Claim Target Scope explicitly **and** classify the Atom as Relational.
5. retain the resolved Claim Target Scope as semantic value when its duplicate Carrier representation is omitted.
6. preserve structural ownership independently of the selected Claim Target Scope.
