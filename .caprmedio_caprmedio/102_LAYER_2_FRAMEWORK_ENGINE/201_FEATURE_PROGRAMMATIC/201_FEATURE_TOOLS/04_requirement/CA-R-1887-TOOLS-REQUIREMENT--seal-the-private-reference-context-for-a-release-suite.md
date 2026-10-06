---
atom_id: CA-R-1887
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:54:35 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Sealed suite reference context"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest]
relations:
  relates_to: [CA-R-1879, CA-R-1886]
---
# Summary

Seal the private reference context for a Release suite

## Scope

The read-only Project control references required by the declared Release suite in addition to its sealed package rows.

## Claim

Before a Release suite executes, its Suite Owner **must** derive, byte-verify, copy read-only, and bind one closed canonical reference context. The context contains only the allowlisted selected-workflow bindings, Operator registry, Project settings, source-registry reference, CA-D-572 and every transitive pin it declares, and the selected-manifest source-path closure. It is private Suite-owner state, never a D566 candidate-inventory member, public request field, MCP route, Workflow, Run, Journal carrier, runtime state, secret, or arbitrary caller file.

## Details

Each context row has exactly `source_path`, lowercase SHA-256 `sha256`, and regular-file `mode`. Every path is Project-relative, allowlisted by the closed construction, regular, non-symlinked through every ancestor, and readable before the read-only workspace is mounted. The closure is rejected if a named root, source-registry resolution, D572 pin, transitive pin, selected-manifest path, digest, mode, or cardinality differs from current Project bytes.

The Suite Owner also binds the existing trusted internal candidate manifest SHA-256, compiled-candidate root, frozen selected N identity, and N image-context identity to this context. These are derived from existing trusted handoffs and actual selected-N evidence, not accepted as public envelope fields. A fresh currentness check immediately before execution and a rederivation after execution must match the pre-run closure and context digest. Any absence, mutation, symlink, unreadable byte, changed trusted binding, or post-run mismatch is non-passing and authorizes no candidate staging, runtime installation, Skill publication, selector change, image retirement, or source mutation.
