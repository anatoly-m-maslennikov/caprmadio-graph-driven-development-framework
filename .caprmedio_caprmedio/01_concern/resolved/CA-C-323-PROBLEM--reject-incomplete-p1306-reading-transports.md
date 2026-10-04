---
atom_id: CA-C-323
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Native evidence transport completeness"
  depends_on: [Artifact]
version: 3
updated_at: "2026-10-04 10:10:01 +0000"
relations:
  concern_about: [CA-P-1306]
---
# Summary

Reject incomplete P1306 reading transports

## Concern

Three oversized native/binding responses were truncated: combined Principles and compact leaf binding, duplicated original-part/full-text output, and a mistaken tail boundary that repeated the full leaf. The incomplete responses were rejected for source reading and semantic coverage.

## Evidences

The assigned Agent reopened the complete binding and original parts in four smaller whole-source batches. Every selected record and both complete continuing-source antecedents were read without truncation, and frozen prefix/raw/text hashes were checked. Source/saved/Carrier/local-DAG proof passed at 10:03:14 UTC, 13m30s from the actual start. Two rejected diagnostic assumptions (first-native prefix field shape and an arbitrary prose-length threshold) were corrected without changing evidence. A stale-timestamp completion patch was rejected atomically, and a subsequent combined completion read was truncated and rejected; neither became a save or pass. Small exact header/receipt reads recovered persistence.

The original 15-minute estimate was exceeded during closure. The failure remains recorded: start 09:49:44 UTC, recovered persistence 2026-10-04 10:06:39 UTC. Resolution records restored complete access, saved evidence and honest closure; it does not erase the timing failure or establish completion within 15 minutes.

## Blast radius

Final saved recovery proof passed at 2026-10-04 10:08:23 UTC, 18m39s from the original 09:49:44 UTC start, including full literal reading, analysis, persistence and final native/saved/Carrier/local-DAG checks. The estimate was exceeded. CA-C-323 is nonblocking only because complete saved recovery and placement proof now passes; the original timing failure remains visible. The Agent holds after this leaf.

P1306 reading and completion evidence only. The original 09:49:44 UTC clock was not reset. No source snapshot was unavailable, no rejected transport counted as reading, and no framework Tool or runtime change was made.
