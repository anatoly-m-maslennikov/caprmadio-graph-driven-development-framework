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
version: 3
updated_at: "2026-10-05 08:50:00 +0400"
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

**every** Project-owned Draft Atom Carrier **must** carry **`=1`** top-level `revision_lineage: {history_entry_ref: {history_revision, path}}` map and **must not** carry `atom_id`. `history_entry_ref` is a pre-addressable safe retained-history locator; it is not the Draft's own identity and does not change CA-D-288's ID-free filename.

Only the admitted lifecycle writer may append the referenced retained Atom-history entry. That entry has exactly `draft_output: {path, digest}`, `origin: {kind}`, `parent_history_entry_ref` when the Draft follows a Draft, and `direct_predecessor` when the origin has or inherits an identified predecessor. `draft_output.path` is the safe locator of this resulting Draft Carrier and `draft_output.digest` equals its exact bytes; both must match the current Carrier that names the entry. `origin.kind` is exactly `never_identified`, `demoted_identified`, or `draft_update`. A `demoted_identified` entry's direct predecessor is the immediately preceding identified Revision and has exactly `atom_id`, `version`, `content_role`, `summary`, `digest`, and `immutable_locator: {history_revision, path}`. A `draft_update` entry directly names the immediately prior matching Draft-history entry and repeats its resolved origin/direct predecessor basis; it binds the new Draft output without changing its original identity basis.

An entry is a current Draft head only when it is the unique retained-history leaf for its `draft_output.path`, its `draft_output.digest` matches the current Draft bytes, each `parent_history_entry_ref` resolves directly and without a cycle, and no later child, branch, or competing entry names that entry or binds that canonical Draft locator. An admitted later non-Draft identification **must** resolve that unique current Draft head and validate it under CA-D-568 before an identity effect. It restores the described Identity only for a validated `demoted_identified` basis, including through a validated `draft_update` chain whose original direct predecessor and Summary still match. It allocates the next unreused Content Role number under CA-D-508 only for a validated `never_identified` basis, including its validated update chain. Promotion appends one `origin: {kind: identified_promotion}` retained-history successor with `parent_history_entry_ref` to the consumed Draft head and the resulting non-Draft output locator/digest; that successor has no Draft `revision_lineage` and makes the old head non-current. A missing, unknown, malformed, stale, non-direct, unrelated, unsigned, output-mismatching, non-head, branched, or missing-parent property/entry is legacy/unknown and fails closed; it **must not** be interpreted as `never_identified`.

## Details

The admitted Create, identified-to-Draft, or Draft Update effect reserves the pre-addressable entry reference, writes the resulting Draft, and appends the matching retained-history entry. The validation resolves retained history internally; a filename, current path alone, arbitrary archive, request value, result seal, or Journal record cannot create or replace it. A Summary change from a `demoted_identified` predecessor requires the separately admitted Replace/fresh-identity path. This Delivery introduces no persistent identity registry, Event writer, Tool, Workflow, Journal authority, cryptographic authentication claim, or hidden global history index.
