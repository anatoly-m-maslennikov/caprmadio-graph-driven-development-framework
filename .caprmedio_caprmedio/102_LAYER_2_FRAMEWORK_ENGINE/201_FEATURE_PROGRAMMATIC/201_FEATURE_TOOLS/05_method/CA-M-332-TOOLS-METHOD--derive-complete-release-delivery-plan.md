---
atom_id: CA-M-332
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-07 23:37:51 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Delivery-plan construction"
  depends_on: [Tool, Manifest, Methodology, Projection, Skill, Image]
relations:
  method_for: [CA-R-1877, CA-R-1878, CA-R-1879]
---
# Summary

Derive one complete release delivery plan

## Scope

Pure derivation of the candidate's source, compilation, runtime, Skill, test, image, and rollback bindings.

## Claim

The Tool derives one ordered delivery plan from the sealed manifest: derived source copy and compilation, package preparation, full-suite gate, separately retained N+1 installation, actual candidate-image build/execution, then promotion and delayed exact retirement. It preserves N as active rollback selection and reports any absent reviewed path or unsupported existing interface as a blocker rather than synthesizing a destination or fallback.

## Details

The plan binds existing compiler and installer interfaces only where their actual declared surface fits and keeps active runtime/Skill exposure at N until every promotion gate passes. It does not execute a compiler, installer, Docker command, Skill copy, test suite, or image operation.

For source-copy replacement, derive a retention plan that preserves the privately reserved parent and uses an absent child for the exact owned predecessor. The plan **must** retain predecessor bytes, modes and empty directories; require safe, unchanged reservation identity and an absent child **before** moving the predecessor; and preserve the existing atomic rename, currentness and publication checks. Removing an empty reservation is not a publication prerequisite. If candidate publication fails, restoration **may** move **only** the actual predecessor child back **when** the fixed target is absent. Retain and report the reservation, staged candidate and actual predecessor carriers after a failure; an empty reservation is not a predecessor tree. Existing recorded Runs and source-copy proofs remain unchanged.

For any later failed, blocked, or unpromoted candidate after completed source delivery, derive a predecessor-only recovery prerequisite from the recorded old source-copy proof. Reopen and authenticate its old frozen manifest, expected/actual old copy digest, same executing N, fixed source-copy target `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`, complete old-tree bytes and modes, canonical Journal, Action/Run identity, and sealed CA-D-574 checkpoint/proof before treating the old tree as retained ownership evidence. Do not compare old source, settings, or frontier digests to the new candidate, reuse old output or authorization, or replay an old effect. The new candidate still independently seals and revalidates its current sources, settings, frontier, and authority, then performs the normal fresh copy whose new actual digest equals its new expected digest; any unknown or mismatched predecessor proof remains blocked.

For a prospective current admission of historical source-delivery evidence, derive the bounded source-authoritative registration in CA-D-567 before deriving any retention or replacement step. Treat the registration as a current lookup, not retroactive sealing or proof that mutable bytes were unchanged at the historical run time: re-read every pinned Journal, Action/Run, checkpoint, candidate manifest, executing-N identity, fixed source-copy root, expected/actual copy digest, and persistent inventory, and require exactly one applicable authoritative match. Use CA-D-567's complete mode-aware persistent-inventory definition for the comparison; do not derive a second codec or loosen its path, mode, exclusion, or serialization rules. The closed schema has `schema_version: 1`, exactly one record with `basis = "current admission of historical delivery evidence"`, and no unknown or duplicate fields; malformed, ambiguous, tampered, wrong-N, unsafe, or inventory-mismatched evidence blocks the plan. The registration may only retain or replace the exact occupied predecessor copy while the new candidate independently seals current inputs and performs a normal fresh delivery; it never reuses, replays, or promotes old output or authorization.
