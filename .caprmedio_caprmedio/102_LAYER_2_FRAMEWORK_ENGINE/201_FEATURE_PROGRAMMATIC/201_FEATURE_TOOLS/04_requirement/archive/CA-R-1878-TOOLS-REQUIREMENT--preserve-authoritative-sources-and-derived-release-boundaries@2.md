---
atom_id: CA-R-1878
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 14:47:41 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Authority preservation"
  depends_on: [Tool, Methodology, Projection, Journal, Project Settings, Framework Settings]
relations:
  relates_to: [CA-R-1876, CA-R-1877]
---
# Summary

Preserve authoritative sources across release delivery

## Scope

The boundary between canonical release inputs and derived source, runtime, Skill, and image deliveries.

## Claim

Release Version **must** copy, compile, package, install, and verify only derived deliveries while preserving canonical authoring sources, Project Structure, Project and Framework Settings, existing Journal evidence, and unrelated Skills byte-for-byte.

## Details

Neither a compiled Methodology projection nor an installed package establishes source authority. A source/frontier change after sealing invalidates promotion and requires a fresh candidate; it does not permit repair through the release Tool.

When the normal source-copy phase has completed and a later phase fails, blocks, or becomes recording-uncertain, Release Version **must** retain the completed source-copy predecessor proof even when the candidate is never promoted. The proof authenticates the old frozen candidate manifest, expected and actual old source-copy SHA-256 values, the same executing N, the fixed target `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`, the complete old-tree file bytes and modes, and the canonical Journal plus Action/Run and sealed CA-D-574 checkpoint/proof references. Unknown, tampered, unrecorded, unsafe, mode-drifted, identity-drifted, or wrong-N predecessor evidence is blocked; file presence or arbitrary old JSON is not proof. The old proof is predecessor ownership evidence only: it neither authorizes a new candidate nor requires old source, settings, or frontier digests to equal a new candidate's independently sealed values.
