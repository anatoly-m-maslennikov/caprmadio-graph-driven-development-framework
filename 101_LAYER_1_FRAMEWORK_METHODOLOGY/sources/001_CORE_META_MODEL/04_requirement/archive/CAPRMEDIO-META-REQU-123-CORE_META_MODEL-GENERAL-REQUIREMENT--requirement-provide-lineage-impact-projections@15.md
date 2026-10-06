---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 15
updated_at: "2026-09-10 07:24:21 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-107-CORE_META_MODEL-CORE-REQUIREMENT--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-125-CORE_META_MODEL-CORE-REQUIREMENT--classify-artifacts-through-the-extensible-type-registry
---
# Requirement — Provide lineage-impact Projections

CAPRMEDIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, **or** archived. the Projection derives the reachable descendant set **without** modifying **or** retargeting **any** persisted relation.

for **every** affected descendant, the Projection identifies the exact earlier revision **in** its lineage, the upstream event that triggered review, **and** the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, **or** confirmed compatible **without** change. unresolved descendants remain visible **until** disposition is recorded through governed history.

the Projection **may** group **and** prioritize work, but it cannot change an Atom, break a historical link, **or** establish compatibility merely by listing it.

## Primary claim

a changed, replaced, **or** archived ancestor produces a derived review surface for **every** affected descendant while historical lineage remains intact.
