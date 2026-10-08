---
atom_id: CA-R-1041
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "artifact-operations"
version: 7
updated_at: "2026-10-04 17:36:48 +0000"
relations: {}
---
# Summary

Coordinate Atom replacement intent

## Scope

REPLACE_ATOM's explicit singular or frozen bulk replacement intent, delegated application boundary and truthful result evidence.

## Claim

REPLACE_ATOM **must** coordinate explicit Atom replacement intent **without** owning generic Carrier creation, relation editing, **or** archival semantics.

- an atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact already-active successor Atom IDs, **and** action context.
- reject missing, duplicate, inactive, **or** self-referential IDs; return a sealed replacement action containing the supplied predecessor, successor set, **and** predecessor archive intent.
- a bulk replacement accepts a frozen set of explicit predecessor-to-successor-set mappings **and** preserves the approved all-or-nothing change-set boundary.
- use the canonical Atom lifecycle capability for the archive effect **and** pass the explicit IDs **to** the provenance pipeline. do **not** infer, create, **or** write replacement relations **in** Atom Carriers.
- default **to** a mutation-free dry run. permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.
- a successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. an intake acknowledgment is necessary for that handoff **but** is **not** proof that replacement was applied **or** that its authoritative Journal event **and** Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.
- distinguish a prepared sealed description, a deferred delegated request, **and** an actually applied replacement. prepared **or** deferred results **must** state that the archive effect is **not** applied; acceptance, sealing, **or** intake alone **must not** be reported as completed replacement.
- at the actual effect boundary, revalidate the exact predecessor **and** **every** supplied successor identity, bound Revision, Active state, complete sealed mapping **and** current delegated authority. each successor **must** be durably Active **before** predecessor archival. use CA-O-051's whole-Carrier transition: preserve the predecessor's body, Summary, identity, Version **and** frontmatter values except actual archive Status **and** Updated At; retain its canonical prior Version suffix.
- report actual replacement completion **only** with observed canonical lifecycle effects **and** durable authoritative archive-event evidence naming the explicit predecessor **and** complete **`>=1`** already-active successor set under CA-R-807. preserve the frozen bulk boundary **and** actual per-mapping result; partial **or** uncertain effects **must not** be described as all-or-nothing success.
- retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start **and** truthful terminal/pending evidence **and** actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. recording failure leaves completion evidence blocked **and** pending evidence intact; retry recording **without** replaying performed replacement **or** resetting authority/retry allowance. an unpersisted acknowledgment is **not** Journal completion.

## Details

CA-O-031 owns the replacement Action; CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description; CA-E-247 covers admission, delegated-effect and receipt distinctions. The Tool neither creates missing successors nor gains lifecycle or Journal authority from intake acceptance.
