---
subjects:
  governs: "Atom/Revision/Status: Draft/Identity Continuity"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Operator"
priority: high
version: 3
updated_at: "2026-10-05 07:51:22 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-508
    - CA-D-568
    - CA-D-569
    - CA-D-570
atom_id: "CA-C-452"
content_role: "Concern"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "active"
author: "Anatoly Maslennikov"
type: "Question"
global_tier: 11
---
# How should a Draft Carrier establish identity continuity?

How should a Draft Carrier remain an ID-free Revision while a later identification can distinguish a demoted identified Atom from a never-identified Draft without assigning a prior identity to another Atom?

## Chosen policy

- an ID-free Draft Carrier has exactly one serialized `revision_lineage` frontmatter property under CA-D-570. It is the durable identity-continuity authority, not an `atom_id` and not a second identity registry.
- `revision_lineage: {kind: never_identified}` is written only by the admitted Create effect. It permits later next-unreused-number allocation under CA-D-508 only after validation confirms that the Draft has no identified direct predecessor.
- `revision_lineage: {kind: demoted_identified, direct_predecessor: <descriptor>}` is written only by the admitted identified-to-Draft effect. Its descriptor is revalidated against the target Draft's retained immutable direct predecessor, including Atom ID, Version, Content Role, Summary, digest, and immutable locator. Re-identification restores that same Atom Identity only when the Draft retains the predecessor Summary; it does not allocate another number.
- a missing, unknown, or legacy lineage never counts as `never_identified` and fails closed without an identity effect. A changed Summary requires the separately admitted Replace/fresh-identity path. Optional request evidence may corroborate the exact carried property, but cannot supply, alter, or override it.

## Alternatives considered

- infer continuity from the Draft filename, Summary, path, or an arbitrary historical archive: rejected because those mutable or unrelated Carrier facts do not establish direct Entity continuity.
- allocate a fresh ID for every Draft leaving Draft: rejected because it breaks verifiable continuity for a demoted identified Atom.
- reuse a prior ID without immutable predecessor evidence: rejected because the ID could be assigned to a different Atom.
- keep `atom_id` in Draft frontmatter: rejected by CA-D-446 and CA-D-288.
- retain the continuity basis only in a transient lifecycle result, a Journal, or an external continuation registry: rejected because a later ID-free Draft must carry its own durable, verifiable direct predecessor provenance and those mechanisms would become a second authority.

## Reasons

CA-D-446 preserves same-Atom semantics for an identified-to-Draft change while removing its Draft ID. CA-D-378 fixes the assigned-ID encoding, CA-D-508 requires a next unreused number for a newly identified Project-owned Atom, and CA-D-507 prevents Carrier formatting from changing identity. CA-D-570 makes the required direct predecessor provenance self-sufficient on the Draft Carrier without restoring an `atom_id` or creating a parallel identity or Journal authority.

## Residual uncertainty

The exact runtime serializer and validator implementation remain unimplemented. CA-D-568 fixes the validation rule, CA-D-570 fixes the carried Draft property, and CA-D-569 names optional corroborating request evidence; a Journal may record the decision but cannot establish identity continuity or freshness.
