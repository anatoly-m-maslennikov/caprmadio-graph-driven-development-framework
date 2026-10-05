---
atom_id: CA-R-1876
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Request boundary"
  depends_on: [Tool, Operator, Artifact, Revision, Digest, Project Structure, Framework Settings]
relations:
  relates_to: [CA-P-1620, CA-P-1621]
---
# Summary

Seal the Release Version request and candidate boundary

## Scope

One requested release promotion from executing Version N to separately pinned candidate Version N+1 through one candidateSnapshotManifest.

## Claim

The Release Version Tool **must** accept only one sealed Operator-selected `candidateSnapshotManifest` that identifies executing N, candidate N+1, exact source revisions and digests, Project Structure and Framework Settings bindings, expected compiler frontier, complete package rows, declared full-suite environment, Skill target, and candidate image reference.

## Details

The Tool rejects absent, ambiguous, changed, caller-substituted, or unsealed manifest bindings before any effect. The manifest may reference canonical authority through its sealed source snapshot; it does not rewrite or replace that authority. A request does not authorize a source edit, a definition switch during an executing Run, an unbounded image deletion, or a recursive release invocation.
