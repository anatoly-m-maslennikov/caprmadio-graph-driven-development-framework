---
subjects:
  governs: "projection-pipeline"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: "2026-10-05 00:13:37 +0000"
atom_id: CA-R-1068
content_role: Requirement
status: Active
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
---
# Summary

Generate active Requirement Lineage Map

## Scope

TOOLS contribution represented by this existing legacy Atom.

## Claim

the framework **must** provide one deterministic `project` Tool that writes the active-only Requirement lineage-section Projection as a registered selected-Scope-Unit destination beneath `.caprmedio_caprmedio/_projection/` with basename `stg_requirements_lineage_sections.md`, assigns **every** non-orphan Requirement exactly once **to** the section named by its complete sorted set of reachable Principle Requirement numbers, orders section names as numeric vectors with a prefix **before** its extensions, orders **every** section by ascending applicable Global Tier, including General where applicable, **and** then numeric Requirement ID, places one Orphans section last, **and** renders exactly the linked `TYPE + ID`, exact authored `Summary` value in the governed Atom carrier format, **and** direct authored `Child of` columns while resolving ancestry against the complete active project graph.
