---
subjects:
  governs: "Tool/ATOM_UPGRADE"
  depends_on:
    - "Atom"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Artifact/Revision"
version: 10
updated_at: "2026-09-17 03:44:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
---
# Upgrade active Atom authority

the `ATOM_UPGRADE` Tool is the canonical Doer for upgrading active CAPRMEDIO Markdown Atoms **to** an explicit operator-supplied enabled target Tier of `core` **or** `standard` that is higher than the source Tier. Upgrade is neither archive nor promotion: it preserves the stable Atom ID **and** **may** keep the current Scope Unit **or** move the Atom **only** **to** an explicitly named ancestor Scope Unit. The Tool **must** derive the target authority location **and** filename scope segment **when** the Scope Unit changes, advance revision metadata, **and** reject missing, disabled, non-higher, **or** other invalid target Tiers, non-active Atoms, non-ancestor Scope Units, identity **or** destination collisions, **and** partial operations. An atomic action upgrades exactly one Atom; a bulk action freezes two **or** more Atom targets with their expected revisions **or** digests **and** is all-or-nothing. It **must** default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized project-local MCP delegation with a sealed Initiative action envelope.
