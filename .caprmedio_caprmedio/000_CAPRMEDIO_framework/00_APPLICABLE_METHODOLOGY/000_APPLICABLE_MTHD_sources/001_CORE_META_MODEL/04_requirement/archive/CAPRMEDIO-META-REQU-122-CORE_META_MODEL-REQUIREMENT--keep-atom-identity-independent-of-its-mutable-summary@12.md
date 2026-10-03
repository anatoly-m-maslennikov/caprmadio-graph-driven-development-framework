---
atom_id: CAPRMEDIO-META-REQU-122
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - artifact-model
version: 12
updated_at: "2026-09-10 20:57:21 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-110-CORE_META_MODEL-CORE-REQUIREMENT--bind-governed-transactions-to-stable-artifact-revisions
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Keep Atom identity independent of its mutable summary

an Atom's filename Summary is mutable Carrier metadata **and** is **not** part of its stable identity. a draft **may** change its Summary while it has no assigned Atom ID. an accepted role-classified Atom **may** change its Summary through a governed Revision while preserving its assigned Atom identity.

**every** committed Revision remains immutable **and** recoverable through governed history. a Summary change that still describes the same role-specific atomic unit does **not** create a successor Atom.

a change **to** the primary atomic meaning, rather than a filename **or** Summary change by itself, requires a successor Atom **and** a new Atom ID.
