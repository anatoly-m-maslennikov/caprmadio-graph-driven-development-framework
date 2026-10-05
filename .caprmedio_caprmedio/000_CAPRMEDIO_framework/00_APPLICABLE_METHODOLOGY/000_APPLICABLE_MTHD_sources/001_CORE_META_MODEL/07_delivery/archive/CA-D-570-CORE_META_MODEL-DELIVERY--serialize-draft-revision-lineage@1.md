---
subjects:
  governs: "Atom/Revision/Status: Draft/Revision Lineage"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Atom/Revision/History"
    - "Atom/Revision/Version"
    - "Atom/Content Role"
version: 1
updated_at: "2026-10-05 07:51:22 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-568
atom_id: "CA-D-570"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Draft Revision Lineage

## Scope

the durable, ID-free provenance property on a Project-owned Draft Atom Carrier.

## Claim

**every** Project-owned Draft Atom Carrier **must** carry **`=1`** top-level `revision_lineage` map and **must not** carry `atom_id`. `revision_lineage` is predecessor provenance only; it is not the Draft's own identity and does not change CA-D-288's ID-free filename.

the map **must** be exactly one of:

- `{kind: never_identified}`: written only by an admitted Create effect for a Draft with no identified direct predecessor.
- `{kind: demoted_identified, direct_predecessor: {atom_id, version, content_role, summary, digest, immutable_locator: {history_revision, path}}}`: written only by an admitted identified-to-Draft effect. `direct_predecessor` **must** describe the immediately preceding identified Revision retained in immutable history. `atom_id`, `version`, `content_role`, `summary`, and `digest` **must** equal that Revision; `immutable_locator.history_revision` and `immutable_locator.path` **must** resolve that exact retained Revision and its bytes whose digest equals `digest`.

an admitted later non-Draft identification **must** validate this actual Draft property under CA-D-568 before an identity effect. It restores the described Identity only for `demoted_identified` whose direct predecessor and Summary still match. It allocates the next unreused Content Role number under CA-D-508 only for validated `never_identified`. A missing, unknown, malformed, stale, or non-direct property is legacy/unknown and fails closed; it **must not** be interpreted as `never_identified`.

## Details

the admitted Create or identified-to-Draft effect serializes the property with the Draft Carrier. The validation resolves retained history internally; a filename, current path alone, arbitrary archive, request value, result seal, or Journal record cannot create or replace it. A Summary change from a `demoted_identified` predecessor requires the separately admitted Replace/fresh-identity path. This Delivery introduces no persistent identity registry, Event writer, Tool, Workflow, or Journal authority.
