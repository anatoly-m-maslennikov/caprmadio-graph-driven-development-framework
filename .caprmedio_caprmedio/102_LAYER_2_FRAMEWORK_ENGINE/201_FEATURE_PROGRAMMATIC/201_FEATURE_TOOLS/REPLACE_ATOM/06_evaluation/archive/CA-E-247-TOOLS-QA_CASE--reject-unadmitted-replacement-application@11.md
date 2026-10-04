---
atom_id: CA-E-247
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 11
updated_at: "2026-10-04 18:00:17 +0000"
relations:
  evaluation_for:
    - CA-R-1041
    - CA-R-1093
---
# Summary

Reject unadmitted replacement application

## Scope

REPLACE_ATOM dry run, sealed delegated application and actual replacement/recording outcomes under CA-R-1041.

## Claim

**every** realization **must** distinguish prepared **or** deferred replacement intent from actual admitted replacement effects **and** durable history/Run receipts; unauthorized application, missing current admission **or** incomplete evidence **must not** yield a completed replacement result.

## Details

### Dry run and unauthorized application

Given **`=1`** exact active predecessor **and** **`>=1`** distinct already-active successor Atom IDs **and** a sealed Initiative action, `REPLACE_ATOM` dry run returns the explicit complete replacement action **without** mutation. Direct `--apply` **without** authorized project-local MCP delegation returns a stable rejection **and** leaves **every** Carrier, Journal, index, Git history **and** runtime file unchanged. Repeat with **`>=2`** successors **and** a frozen bulk set of explicit mappings; no pair-only normalization drops a successor **or** changes the approved boundary.

### Prepared, deferred and current admission outcomes

A prepared description **or** deferred delegated request remains explicitly not applied even **when** sealing **or** durable intake succeeds. Independently make the predecessor **or** **any** successor missing, inactive, duplicate, self-referential **or** unresolved; change a bound Revision, successor Active state, approved mapping **or** delegated permission **after** preview. The effect-boundary check rejects **or** reports unresolved admission **without** silently using newer bindings, creating a successor **or** reporting archival. Retain exact request, preview, currentness evidence **and** result.

### Actual canonical effect and receipts

Given the unchanged fully admitted sealed action through authorized MCP delegation, the Tool invokes **only** the canonical lifecycle operation **and** MCP receives durable `COMMIT_TRIGGER` intake acknowledgment **before** reporting successful delegated intake. The Tool itself does **not** append the Journal, stage files **or** create a Git Commit. Intake success alone is **not** a completed replacement.

For actual replacement completion, verify that **every** supplied successor is durably Active **before** predecessor archival; CA-O-051 preserves the whole predecessor body, Summary, identity, Version **and** all frontmatter except archived Status **and** actual Updated At, with its canonical **`@<version>`** suffix. Verify the actual authoritative archive event names the explicit predecessor **and** complete already-active successor set under CA-R-807. No replacement history Relation is written **in** current Atom Carriers. Check truthful Workflow **and** Action Run start/terminal results, actual effects, exact definitions/lineage/input references **and** durable canonical receipts under CA-P-1443/CA-P-1451; a Tool call does **not** automatically create another Run.

### Failure and recording recovery

Inject delegated failure before effects, partial **or** uncertain effects, **and** terminal/archive-event recording failure after an actual effect. Preserve actual failed/partial/uncertain result, affected **and** remaining mapping boundaries **and** pending evidence; do **not** report replacement completion **or** fabricate an event/receipt. With the same pending event identity **and** payload, retry storage only; identical retry obtains one canonical receipt, conflicting payload cannot overwrite history, **and** the replacement Action is **not** replayed. Approved atomic bulk intent is **not** evidence of achieved atomic success. A never-started request has no fabricated Run; an actual no-op has truthful Run evidence **without** fictitious mutation.

### Acceptance and failure disposition

Accept **only** a realization preserving all dry-run/admission/complete-successor/sealed-boundary cases, observed canonical effects **and** the actual result/receipt distinctions above. Reject false completion from prepared/deferred/intake-only evidence, lost successor IDs, changed admission, unrecorded completion, blind replay **or** overwritten/deleted history. Preserve supplied/returned mappings, before/after Carrier evidence, delegated result, actual effect observations **and** durable **or** explicitly pending receipt evidence.

### Sources

- [CA-R-1041 — Coordinate Atom replacement intent](../04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md)
- CA-O-051 v6; CA-R-807 v19; independently accepted CA-P-1443/CA-P-1451 J01–J08 contract. These cases bind later functional proof; this carrier records no observed runtime pass.
