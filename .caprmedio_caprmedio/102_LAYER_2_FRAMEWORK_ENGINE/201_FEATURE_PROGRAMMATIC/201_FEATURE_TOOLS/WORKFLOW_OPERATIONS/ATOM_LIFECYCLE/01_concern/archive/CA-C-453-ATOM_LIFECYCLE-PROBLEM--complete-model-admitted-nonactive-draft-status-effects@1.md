---
atom_id: CA-C-453
content_role: Concern
type: Problem
current_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 14
author: Anatoly Maslennikov
status: active
subjects:
  governs: "Tool/ATOM_LIFECYCLE/Status change coverage"
  depends_on: [Atom, Status, Carrier, Identifier, Revision, Analysis, Draft]
version: 1
updated_at: "2026-10-05 03:28:48 +0000"
relations:
  concern_about: [CA-P-1637, CA-P-1664]
---
# Summary

Complete model-admitted nonactive Draft status effects

## Concern

The source-derived Status model admits Analysis Done→Draft, but the native effect refuses it at the active-only history guard. Universal Status handling is incomplete despite the fourteen passing initial golden tests.

## Evidences

Root invoked the saved native real-source fixture in the existing development worker with Analysis Done→Draft. The request resolved its actual current model, then failed LifecycleError atom-not-active in preserve_atom_revision; the Project snapshot remained unchanged. Saved native hashes were lifecycle_intents.py15d15e7afabf2abc0d46fdb4e68fa5ecf8e78f6ccc765fcd8c60cb5c13c79c99 and atom_operations.py2a5532d89e6a5a8957b10a80814e07117ce6debf8bbc0af2ba8b2bd52b046519. The same code checks only literal Draft, while Concern uses lowercase draft, and its draft-basename expression recognizes only the short fixture form without Scope/Type/Tier components.

## Blast radius

Model-admitted Draft demotion for non-Active and lowercase-role carriers and canonical full filenames. CA-P-1664 owns bounded test-first repair. Existing passing native tests remain evidence for their exact cases, not all Status pairs or shared/MCP/image completion.
