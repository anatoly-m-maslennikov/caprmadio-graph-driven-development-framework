---
atom_id: CA-P-1562
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Extend the canonical selected route manifest"
  depends_on: [Workflow, MCP, Implementation, Evaluation, Projection]
version: 2
updated_at: "2026-10-04 23:11:38 +0000"
relations:
  is_decomposition_of: [CA-P-1527]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Extend the canonical selected route manifest

## Objective

Within <=15 minutes, implement the accepted closed fifteen-route manifest and existing MCP registration boundary.

## Details

Inputs: accepted P1543, P1552, P1532/P1535, D521@5 and current R1847/R1848/D547/D548/E567/E568. Own selected_routes.py, its MCP tests, the single canonical .caprmedio_caprmedio/_projection/selected_workflow_bindings.json, and only manifest validation/source-copy compatibility in selected_workflows_docker_fixture.py. Preserve all native golden helpers. Extend the exact original thirteen inventory with source-bound Artifact and Journal query routes; preserve A1142's original authority. query_source_admissions contains exactly the accepted P1532 and P1535 frontier pins with their current O definitions, never P1543 as a third pin. Validate all fields, current pins, self/binding digests, closed route order and no duplicate/shadow authority. Preserve strict preview/execute, authorization, Base Revise, hot reload and existing helpers. Update necessary current consumer tests without accepting stale thirteen-route canonical input. Do not edit backend, selected_execution.py, Query Tools, source or Journal. Runtime handlers and pre-own-event capture belong to P1563; registration is not execution proof. Retain the historical Engine manifest unchanged until its separate migration disposition.

You are not alone; preserve others and use apply_patch. Inherit 90% and the mechanical Git exception. Root saves Plans/commits. No FPF, harvesting or permission bypass.

## Definition of Done

The sole current manifest and existing adapter validate/register exactly the admitted fifteen routes with source-bound tests; execution remains a separate gate.

## Result

The canonical manifest admits fifteen routes, retains CA-A-1142 for the original thirteen and exactly P1532@2/P1535@2 for the queries. Its self digest is `00d3dd74ef8b200ac472932eb80a8c3574f704375d7cae9bc6fbe564f08cbcdb`; binding digest is `977ae460d3c34e03dbb4c04d96b116652960d29e849e0eab73a17e0a96bf1864`. Docker worker MCP route tests passed 12/12 and stdio registration tests passed 2/2. Both source frontiers and all six current query O definitions are copied by the disposable fixture. Historical Engine manifest is unchanged. Registration/source validation is accepted; native query execution, full image proof and the stale selected-execution route-count assertion remain separate packets.
