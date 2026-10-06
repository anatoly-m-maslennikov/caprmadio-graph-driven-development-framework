---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Atom selection"
  depends_on:
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Scope Unit"
    - "Atom Collection"
    - "Atom/Claim/Structural Entity"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Artifact/Revision"
    - "Directory Carrier"
version: 5
updated_at: "2026-09-12 04:10:58 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Ownership and Claim-target Atom Sets

**to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
2. resolve **every** candidate Atom's current Scope Unit from its nearest containing Scope Unit, passing through Atom Collections **without** treating their nesting as additional Scope Unit ownership. preserve the existing Operator ownership **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
3. resolve **every** candidate's Claim Structural Entity independently of ownership. use the explicit target **when** present **and** the current Scope Unit **when** the reference is omitted for a Current-scope Atom; apply CA-R-1445 for Tasks inside Epics. an unresolved required target remains unresolved. a reference **to** another Structural Entity **must not** transfer ownership, **and** an Epic target **must not** be silently replaced by its enclosing Scope Unit.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447, CA-R-1448, CA-R-942, **and** CA-R-1449 respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288, independently of Local Tier.
6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.
