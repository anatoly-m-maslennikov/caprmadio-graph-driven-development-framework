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
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Artifact/Revision"
    - "Directory Carrier"
version: 9
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
---
# Summary

Derive Ownership and Claim-target Atom Sets

## Claim

**to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
2. read **every** candidate Atom's carried current Scope Unit **and** check it against its nearest containing Scope Unit, passing through Atom Collections **and** Plan Hub Carriers **without** treating their nesting as additional Scope Unit ownership. preserve the existing Operator ownership **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
3. resolve **every** candidate's Claim Target Scope Unit independently of ownership. read the internally carried target; absence of a required value is invalid, **not** permission **to** infer it from placement; apply CA-R-1588 for Plans within Hub decomposition. an unresolved required target remains unresolved. a reference **to** another Scope Unit **must not** transfer ownership, **and** the target **must** resolve **to** a Scope Unit, **not** a Hub Atom **or** another non-Scope-Unit object. Claim Scope restrictions remain **in** the Claim text **and** do **not** create extra targets.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447, CA-R-1448, CA-R-942, **and** CA-R-1449 respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288, independently of Local Tier.
6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.
