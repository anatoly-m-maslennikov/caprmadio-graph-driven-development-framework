---
atom_id: CA-O-129
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Step"
  depends_on: ["Action", "Step Run", "Workflow Run", "Step/Agentic Execution Context"]
version: 2
updated_at: "2026-10-04 17:12:08 +0000"
relations:
  relates_to: [CA-O-128, CA-O-145, CA-R-1509, CA-R-1511, CA-R-1527]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-129-CORE_META_MODEL-STEP--apply-an-admitted-atom-lifecycle-change.md
  source_atom_id: CA-O-129
  source_atom_revision: 2
  source_sha256: a3e4aa7c724804122bf39011f766fb47cc0ce50caf71b7d1a9f8f72a23813e61
  original_relations_sha256: 41d9553cc0bc459a76834b9b50abe0aa6d5b316e2164db5c1ab185ff63b9f658
---
# Summary

Apply an admitted Atom lifecycle change

## Operation

This Step invokes exactly CA-O-128, apply authorized Atom lifecycle changes, as one Agentic Action. Its context is Integrated under R1527; missing required capability blocks admission, not silent context substitution.

### Input and parameter binding

Bind request kind, exactly one Create target or one existing current target/predecessor, its complete frozen Carrier/proposal or status/replacement mapping, current models/authority, permissions/effect admission, effect/recovery/Journal capabilities and check expectations from the exact admitted Workflow request and revalidated current evidence. For Replace preserve the complete accepted set of >=1 successors for that one predecessor. An ambiguous or multi-target/predecessor request returns invalid before invoking O128; separate requests require separate admitted Workflow Runs. Archive shortcut normalization remains subject to O128's actual status-model guard.

For Update, bind the exact identity-preserving assessment and target/proposal/evidence from the latest completed O145 Step Run in this Workflow whose O067 binding matches the current proposal; do not accept an arbitrary historical pass. For other kinds no Update assessment is fabricated. Bind prior effect/receipt evidence and actual Run/parent references from retained execution state, not guessed success.

Return O128's result and evidence unchanged to the Workflow. This Step has no second Action reference, alternate classifier, routing decision or implicit retry.

## Details

The Workflow decides whether to dispatch or terminate after this result. Every dispatch is a distinct Step Run with its exact O128 definition/input/context binding; completed effects are not replayed when a receipt is pending. Tool adapter calls are implementation details, not extra graph nodes or authority.
