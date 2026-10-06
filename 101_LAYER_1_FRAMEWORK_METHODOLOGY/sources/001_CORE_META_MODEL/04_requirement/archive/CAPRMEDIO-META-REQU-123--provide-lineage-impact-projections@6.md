---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - lifecycle-traceability
version: 6
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
---
# Requirement — Provide lineage-impact Projections

CAPRMEDIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, **or** archived. The Projection derives the reachable descendant set **without** modifying **or** retargeting **any** persisted relation.

For **every** affected descendant, the Projection identifies the exact earlier revision **in** its lineage, the upstream event that triggered review, **and** the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, **or** confirmed compatible **without** change. Unresolved descendants remain visible **until** disposition is recorded through governed history.

The Projection **may** group **and** prioritize work, but it cannot change an Atom, break a historical link, **or** establish compatibility merely by listing it.

## Primary claim

A changed, replaced, **or** archived ancestor produces a derived review surface for **every** affected descendant while historical lineage remains intact.
