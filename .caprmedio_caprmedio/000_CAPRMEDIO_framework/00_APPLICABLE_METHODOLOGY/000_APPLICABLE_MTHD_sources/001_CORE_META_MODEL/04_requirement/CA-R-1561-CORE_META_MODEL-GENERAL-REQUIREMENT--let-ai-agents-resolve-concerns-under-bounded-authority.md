---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Atom/Content Role: Concern"
    - "Atom"
    - "Operator"
    - "Atom/Content Role"
    - "AI Agent Delegation"
    - "AI Agent/Confidence"
    - "Autonomous Confidence Threshold"
version: 4
updated_at: "2026-10-03 00:22:56 +0400"
relations: {"child_of":["CA-R-846","CA-P-034"],"relates_to":["CA-R-1058","CA-R-815","CA-R-846","CA-R-1552"]}
atom_id: "CA-R-1561"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Let AI Agents resolve Concerns under bounded authority

## Scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.

## Details
