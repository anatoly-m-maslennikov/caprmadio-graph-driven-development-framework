---
subjects:
  governs: "Atom selection"
  depends_on:
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Scope Unit"
    - "Atom Collection"
    - "Atom/Claim/Target Scope"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Artifact/Revision"
cce_version: cce_1
cce_form: method
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations: {}
---
# Derive Ownership and Claim-target Atom Sets

**to** derive ownership **and** targeting Atom sets for a selected Scope Unit, the Resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms owned outside the selected subtree whose Claim Target Scope can select a Scope Unit inside it.
2. resolve each candidate Atom's owning Scope Unit from its nearest containing Scope Unit while passing through Atom Collections without treating them as Scope Units.
3. resolve each candidate Atom's Claim Target Scope independently of ownership, including its semantic current-Scope-Unit value when explicit Carrier representation is omitted.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms from their respective definitions **and** the Scope Unit tree.
5. apply requested Content Role, Status, Revision, **and** other filters **after** resolving the selected set.
6. report an incomplete source frontier, unresolved owner, unresolved Claim Target Scope, **or** contradictory ancestry without reporting a complete result.
