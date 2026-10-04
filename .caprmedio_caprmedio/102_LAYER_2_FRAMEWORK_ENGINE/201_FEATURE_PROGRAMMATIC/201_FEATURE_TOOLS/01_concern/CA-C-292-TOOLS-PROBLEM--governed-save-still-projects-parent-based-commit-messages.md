---
atom_id: CA-C-292
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: active
version: 1
updated_at: "2026-10-04 06:29:05 +0400"
relations:
  concern_about:
    - CA-R-805
---
# Summary

Governed save still projects parent-based commit messages

## Concern

The existing COMMIT_CONTEXT/COMMIT_CHANGE_SET implementation projects commit prefixes from relation sources or the fallback 0 instead of the sealed Initiative required by current authority. This defect remains active. The original Epic save was postponed; the Operator has since explicitly authorized mechanical Git commits without this Tool for CA-P-1117 and its related changes.

## Evidences

CA-R-805 version 25 requires a real-change commit to use the Initiative-based message Projection. COMMIT_CONTEXT/commit_context_logic.py function event_message derives upstream from event sources, assigning 0 when no relation sources exist. The read-only COMMIT_CHANGE_SET preview for the new Epic directory returned: `0 | ADD | 15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations@1`. Its sealed-context/events/live-preflight/prediction checks passed, demonstrating that those checks do not establish this semantic requirement.

### Disposition and execution impact

Do not call the defective Tool's apply path. Use direct Git for this Epic under the Operator's explicit exception; if Git cannot commit, skip that commit and retain a truthful unfinished save disposition. Tool repair is not a prerequisite for this authorized path. Preserve unrelated work and record actual Git evidence without inventing Tool-generated Journal receipts. This exception does not resolve the implementation defect or change the general methodology; a separate repair/functional verification packet is still needed before claiming the Tool conforms. No Tool implementation was changed by this Plan correction.

## Blast radius

The discrepancy spans commit-context generation and commit application under TOOLS, the narrowest currently declared common Scope Unit. Any action with absent or unrelated relation sources can have an incorrect prefix. CA-P-1117's defective Tool-based save remains affected, but its Operator-authorized mechanical Git path is not blocked by this Concern. This is not a Docker build or permission failure.
