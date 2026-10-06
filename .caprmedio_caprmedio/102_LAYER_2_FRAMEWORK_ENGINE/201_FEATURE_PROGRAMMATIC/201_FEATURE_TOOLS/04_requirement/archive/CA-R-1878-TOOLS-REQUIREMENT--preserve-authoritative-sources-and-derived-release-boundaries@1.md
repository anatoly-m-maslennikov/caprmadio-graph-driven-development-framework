---
atom_id: CA-R-1878
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
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
