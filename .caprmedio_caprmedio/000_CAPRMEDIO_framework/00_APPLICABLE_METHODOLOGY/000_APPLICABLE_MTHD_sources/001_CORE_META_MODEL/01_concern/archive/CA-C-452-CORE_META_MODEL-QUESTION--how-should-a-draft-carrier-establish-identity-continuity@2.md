---
subjects:
  governs: "Atom/Revision/Status: Draft/Identity Continuity"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Operator"
priority: high
version: 2
updated_at: "2026-10-05 07:37:07 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-508
    - CA-D-568
    - CA-D-569
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

- a Draft descended directly from an identified Atom uses `prior_identified_revision` evidence only when the lifecycle result's sealed `prior` **and** `prior_revision` descriptors prove that direct retained predecessor lineage. Re-identification restores that same Atom Identity only when the Draft retains the predecessor Summary; it does not allocate a new number.
- a Draft whose Summary changed from its identified predecessor requires a separately admitted Replace and fresh identity; an older carrier with a matching filename, path, or caller-chosen archive cannot restore its historical ID.
- a never-identified Draft uses `fresh_unassigned_draft` evidence only after internal verification that its retained direct predecessor lineage contains no identified Atom. Only when it later becomes non-Draft does CA-D-508 allocate the next unreused number for its Content Role.
- the Draft Carrier itself remains ID-free in complete frontmatter and filename. A filename, path, Summary, temporary locator, or Journal record cannot establish either basis.

## Alternatives considered

- infer continuity from the Draft filename, Summary, path, or an arbitrary historical archive: rejected because those mutable or unrelated Carrier facts do not establish direct Entity continuity.
- allocate a fresh ID for every Draft leaving Draft: rejected because it breaks verifiable continuity for a demoted identified Atom.
- reuse a prior ID without immutable predecessor evidence: rejected because the ID could be assigned to a different Atom.
- keep `atom_id` in Draft frontmatter: rejected by CA-D-446 and CA-D-288.

## Reasons

CA-D-446 preserves same-Atom semantics for an identified-to-Draft change while removing its Draft ID. CA-D-378 fixes the assigned-ID encoding, CA-D-508 requires a next unreused number for a newly identified Project-owned Atom, and CA-D-507 prevents Carrier formatting from changing identity. The chosen evidence reuses the existing lifecycle `prior` and `prior_revision` seals rather than creating a parallel identity or Journal authority.

## Residual uncertainty

The exact runtime request shape and validator implementation remain unimplemented. CA-D-568 fixes the identity rule and CA-D-569 names the optional `request.parameters.draft_identity_evidence` carrier; a Journal may record the decision but cannot establish identity continuity or freshness.
