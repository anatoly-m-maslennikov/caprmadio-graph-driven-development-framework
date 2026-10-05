---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "AI Agent"
version: 4
updated_at: "2026-10-03 00:34:47 +0400"
relations: {"relates_to": ["CA-R-1584"]}
atom_id: "CA-R-1585"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1585-CORE_META_MODEL-GENERAL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent.md
  source_atom_id: CA-R-1585
  source_atom_revision: 4
  source_sha256: 5998a90d15aedb5aa923b5ec90394a387ee5ece7489340e2dc9e1785699640ae
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Default Plan work assignment to an AI Agent

## Scope

a Plan Atom with its own work and no explicit Assignee.

## Claim

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.

## Details
