---
atom_id: CA-C-459
content_role: Concern
type: Question
current_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 04:53:09 +0000"
subjects:
  governs: "Draft origin provenance"
  depends_on: [Atom, Carrier, History, Tool, Evaluation]
relations:
  concern_about: [CA-P-1662, CA-P-1675, CA-D-568, CA-D-570]
---
# Summary

Which evidence binds Draft origin to its own history

## Concern

Mutable Draft provenance can describe an admitted origin but cannot prove that an arbitrary valid archive belongs to that Draft. Options considered: trust the mutable map; add a self-hash/signature without a trust authority; or bind admitted Draft outputs to immutable retained Atom history. Choose the third, at 88% design confidence, because it uses existing history rather than a second identity registry and closes the actual counterexamples. Each current Draft carries a pre-addressable history-entry reference; that entry binds its exact output locator and digest, direct parent lineage and origin. Lifecycle effects are the admitted writers of retained history. Out-of-band Draft bytes without a matching entry fail closed; an Operator able to reauthor both authority and history is outside the untrusted-request boundary. P1675/P1676 define and review the minimum source contract before code. A self-hash alone is not claimed to authenticate origin.

### Publication choice

The next narrow review found that a pre-write consuming entry could claim nonexistent output. Choose a non-consuming private pending transition over a multi-file atomic-publication claim: reserve the exact planned output and request, observe the actual output, then append finalized retained history. Pending repair binds the same identity on retry; it is ephemeral runtime context, not a new identity registry or another Journal. Only finalized history consumes the Draft head. P1681 binds this necessary repair before P1676 accepts source and P1677 implements it.

## Evidences

P1638's saved rejected review and independent origin adjudication identify the exact branches and source claims. Prior partial passing evidence is retained, not converted into a clean pass.

## Blast radius

The bounded Draft identity promotion path and its source history contract. No mandatory image/permission gate is bypassed and no broad identity registry or new Journal is introduced.
