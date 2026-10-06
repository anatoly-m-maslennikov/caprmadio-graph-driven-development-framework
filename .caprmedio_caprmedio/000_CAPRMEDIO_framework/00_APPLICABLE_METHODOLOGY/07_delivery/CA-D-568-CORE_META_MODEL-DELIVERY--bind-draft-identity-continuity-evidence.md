---
subjects:
  governs: "Atom/Revision/Status: Draft/Identity Continuity Evidence"
  depends_on:
    - "Atom/Identity"
    - "Atom/Identifier"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Atom/Revision/Version"
    - "Atom/Revision/History"
    - "Tool/Workflow Operations/Atom Lifecycle/Request Parameters"
version: 5
updated_at: "2026-10-05 08:50:00 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-569
    - CA-D-570
atom_id: "CA-D-568"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-568-CORE_META_MODEL-DELIVERY--bind-draft-identity-continuity-evidence.md
  source_atom_id: CA-D-568
  source_atom_revision: 5
  source_sha256: 64d2e60303d9dceeaee694263ebd888daf4bd217a794830896b1c5837517559d
  original_relations_sha256: 26799383d9e49344687013dfe0bb6c37bed7b4353c0546ea6e7e46de4b50926c
---
# Summary

Bind Draft Identity Continuity Evidence

## Scope

the required identity basis for a Draft Atom when a later Revision becomes non-Draft.

## Claim

an operation that identifies a Draft Atom **must** read and validate **`=1`** `revision_lineage.history_entry_ref` from the actual target Draft Carrier under CA-D-570 before assigning an Atom ID. That pre-addressable reference resolves only through the exclusive admitted lifecycle writer's append-only retained Atom-history entry; the entry must bind this exact current Draft locator and digest, origin, direct parent lineage, and any identified direct predecessor. It must also be the unique live Draft-head leaf for that canonical Draft locator: every declared parent resolves, no later child or branch names it, and no competing entry binds that locator/digest. Caller parameters may report the resulting reference but **must not** provide, select, alter, or override the identity basis.

- `origin.kind: demoted_identified` is valid only when the resolved matching entry's `direct_predecessor` exactly resolves to the target Draft's own immediate retained identified predecessor. It **must** match that predecessor's `atom_id`, `version`, `content_role`, `summary`, digest, and immutable locator; the target Draft's Summary **must** equal the predecessor Summary. Only then the later non-Draft Revision **must** use that same Atom Identity and **must not** allocate another number.
- `origin.kind: never_identified` is valid only when the matching entry was appended by the admitted Create effect and has no identified direct predecessor. Only then, when the Draft becomes non-Draft, it **must** receive the next unreused Content Role number under CA-D-508.
- `origin.kind: draft_update` is valid only when its matching entry binds the new Draft output and directly names the immediately prior matching Draft-history entry. That parent entry supplies the same validated origin and, for a demoted Draft, the same direct predecessor; an update therefore preserves the original identity basis without converting it to `never_identified`.

a Draft Carrier **must not** carry an `atom_id`; `revision_lineage` is retained-history provenance, not the Draft's own assigned identity. A filename, path, Summary, temporary locator, arbitrary historical archive, Journal record, unsigned caller evidence, or a Draft whose current bytes have no matching unique history head **must not** infer, establish, or replace that provenance. Those conditions fail closed without an identity effect. An admitted non-Draft promotion must append the entry's retained-history successor that consumes this Draft head; restored older Draft bytes then have a child and cannot reuse the origin. A changed Summary requires the separately admitted Replace/fresh-identity path. A verified prior Atom Identity **must not** be assigned to a different Atom. Fully authoritative Operator reauthoring of both Draft and retained history is outside this untrusted-request boundary.

## Details

this Delivery binds carried Draft provenance and its validation before implementation. It preserves CA-D-446's same-Atom Draft transition and CA-D-288's ID-free Draft filename. The lifecycle history writer is the sole trust boundary for these entries; Journal records and request evidence may report but are not a second identity authority, Events writer, identity registry, signature scheme, or history basis.
