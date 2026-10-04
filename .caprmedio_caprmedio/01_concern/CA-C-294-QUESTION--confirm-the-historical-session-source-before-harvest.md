---
atom_id: CA-C-294
content_role: Concern
type: Question
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: active
subjects:
  governs: "Project session metadata corpus/Source identity"
  depends_on:
    - "Project"
    - "Operator"
version: 2
updated_at: "2026-10-04 07:55:00 +0400"
relations:
  concern_about:
    - CA-P-1125
    - CA-P-1126
    - CA-P-1127
    - CA-P-1128
    - CA-P-1129
---
# Summary

Confirm the historical session source before harvest

## Concern

Does session `01a01cb6-4ee4-7553-b68d-0823dda35094` supply evidence for this Project? Its first session_meta record declares the historical cwd suffix `caprmadio-vibe-coding-to-production-framework`, independently verified for this Project by known app-linked sessions, but supplies neither a repository URL nor parent-session reference.

## Evidences

- Exact file: `/Users/am/.codex/sessions/2026/08/20/rollout-2026-08-20T05-08-24-01a01cb6-4ee4-7553-b68d-0823dda35094.jsonl`.
- First record created `2026-08-20T01:08:24.932Z`; observed bytes5865276; modification `2026-09-23T00:04:22.946084+00:00`; source VS Code. These values do not establish in-window body coverage.
- CA-A-905 retains the entire native metadata manifest and this candidate without consuming its body or adopting its statements.
- Safe choice under CA-P-1117's90% policy and information-preservation Principle: keep the source as a candidate rather than exclude it. The first bounded harvest check confirms Project identity before adopting content. Unknown relevance or actual unrelated content gets a truthful disposition, not an inference from its title or timestamps.
- Metadata discovery can close independently of body/window processing. This Question remains active until the recorded source-identity disposition is supported; it is not an authority, runtime or permission bypass.
- Done CA-P-1196 /CA-A-917 now retain a full5865276-byte prefix check:1570 valid timestamped records,0 canonical messages in all four frozen partitions. The sole in-window record is thread_settings_applied metadata. No candidate semantic content was adopted. This Question remains active for broader historical identity but is nonblocking for the current monthly harvest: there is no in-window content requiring adoption. Future different-window use still requires identity confirmation.

## Blast radius

CA-P-1126–1129 must carry this candidate in their source inventory, deduplicate the identity check across their exact packets, and preserve actual retrieval boundaries. No unrelated content may be adopted. Corpus metadata completion does not mean thirty-day decisions have been harvested.
