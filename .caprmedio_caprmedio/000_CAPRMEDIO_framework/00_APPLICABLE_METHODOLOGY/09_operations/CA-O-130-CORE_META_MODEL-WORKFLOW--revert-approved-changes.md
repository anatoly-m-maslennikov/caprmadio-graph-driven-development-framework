---
atom_id: CA-O-130
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Revert Changes Workflow"
  depends_on: [Workflow, Step, Workflow Run, Step Run, Journal, Operator]
version: 1
updated_at: "2026-10-04 16:45:06 +0000"
relations:
  relates_to: [CA-O-132, CA-R-1525, CA-R-1720, CA-R-1643]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-130-CORE_META_MODEL-WORKFLOW--revert-approved-changes.md
  source_atom_id: CA-O-130
  source_atom_revision: 1
  source_sha256: ad98bde116ba178edae132b6fbc91376354b1b2d02c15a4ef58038e54f00bee3
  original_relations_sha256: 7ebbd5345a3d72e0062da4e83a158b371d4e601ba06e88ea54f72f518f566af1
---
# Summary

Revert approved changes

## Operation

Revert Changes **means** the reusable Workflow graph whose entry **and** only node is CA-O-132.

The graph has no next-Step ON_RESULT edges **and** no retry loop. the node's result selects one terminal outcome:

| From Step | Result condition | Terminal outcome |
| --- | --- | --- |
| CA-O-132 | reverted | completed |
| CA-O-132 | no_op | completed_no_op |
| CA-O-132 | blocked | blocked |
| CA-O-132 | failed or partial_failure | failed |
| CA-O-132 | canceled | canceled |
| CA-O-132 | recording_blocked | recording_blocked |

## Details

CA-O-132 owns the invocation binding; its referenced Action owns reversal behavior. admission **and** recovery retain exact Workflow/Step/Action Revisions under CA-R-1525. an unavailable **or** changed definition blocks further dispatch pending recorded revalidation; completed effects **and** original bindings remain historical evidence, **not** permission **to** replay.

Every actual Workflow Run, including admission failure, cancellation, successful no-op **and** partial failure, retains its distinct Run identity, definition Revision, parent lineage **when** applicable, input references, start, terminal outcome, result **and** actual effect/evidence references **in** the one authoritative Project Journal. use CA-D-340's registered Carrier **and** CA-R-1643's admitted Event Types: Started for start, Completed for successful completion/no-op, Failed for failure, Interrupted for a blocked Run **and** Abandoned for cancellation. these terminal outcome names are **not** new Event Type values.

An unconfirmed Workflow start record blocks dispatch of CA-O-132; record the attempted Workflow admission **without** inventing an uninvoked Action Run. completion requires confirmed durable Run evidence, including the invoked Action Run **and** Step lineage. a Journal failure returns recording_blocked with known effects **and** pending recording evidence; an unpersisted event is never claimed journaled **or** complete. recover missing recording **without** replaying reversal effects. no fictitious Artifact change is recorded for no-op, **and** no secret enters the Journal. Artifact Change Log **and** Process Log remain derived views of the same canonical events.
