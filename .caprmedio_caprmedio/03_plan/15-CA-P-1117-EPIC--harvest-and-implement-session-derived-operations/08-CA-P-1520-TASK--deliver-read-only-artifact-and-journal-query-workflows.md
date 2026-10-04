---
atom_id: CA-P-1520
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Read-only Artifact and Events Journal query Workflow delivery"
  depends_on: [Operations, Implementation, Workflow, Action, Tool, MCP, Journal]
version: 3
updated_at: "2026-10-05 01:05:27 +0400"
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1124]
---
# Summary

deliver read-only artifact and journal query workflows

## Objective

Deliver exactly two additional Workflows: Find and Fetch Artifacts (Markdown carriers) and Find and Fetch Journal Events. Each uses a minimal Workflow and one query Action/Tool. This composite owns the new-query branch only; it does not modify the original thirteen-Workflow implementation packets or authorize more Workflows.

Both routes are read-only. Artifacts expose frontmatter and Markdown heading/section properties; Journal Events expose their Event fields. Use a bounded non-evaluating equality/inequality/NOT/IN filter grammar with unambiguous boolean composition, return Artifact IDs or Event IDs by default, and fetch only selected fields/sections or full Events on request. Identities come from their authoritative carriers, never filenames. Preserve requested statuses/properties and report malformed carriers/Events, missing IDs, duplicate properties/headings or Event fields, incomplete reads, invalid filters and bounded coverage/pagination. Do not fetch credentials/secrets, create mutation authority or invent Runs. Shared execution journaling must not alter or enlarge the captured query-source snapshot.

## Work decomposition

P1521/P1523 author the respective O Workflow/Action/Step and RMED source packets; P1522/P1524 independently review them. P1525/P1526 implement test-first Tools, P1527 amends the existing source-bound discovery/MCP/orchestrator route contract and shared execution, P1528 proves fresh immutable-image E2E, and P1529 independently reviews closure. Each child is a <=15-minute dispatch packet inheriting P1117's 90% threshold. Before every downstream dispatch, bind the exact current source IDs, Versions, and carrier paths; absent P1521/P1523 outputs are blockers, not planning evidence. P1521/P1523 instead bind their live authority inputs and save those output IDs/Versions/paths for successors.

## Details

### Centralized Project carriers

Find and Fetch Journal Events reads canonical Event carriers from the selected Project's `_journal/` root. Persisted query-result Projections use that Project's `_projection/` root; ephemeral response/report state remains temporary. The shared Run recorder uses the same canonical `_journal/` root. Existing immutable historical Event references may retain their original sealed locations; relocation must resolve them without rewriting Event bytes.

### Definition of Done

Both source/RMED packets, independent reviews, Tools, route integration, fresh-image evidence, and closure review are Done with exact source/implementation/image/Run/Action/result evidence. Original13 work continues independently; P1171's final image-coverage review and P1124 closure require this branch's accepted proof.

## Source-review repair frontier

P1522/P1524 completed their initial reviews with rejected source contracts. P1530/P1531 own bounded repairs; P1532/P1533 independently review the repaired current packets. P1525/P1526 require these fresh acceptances, not the completed initial rejection records. The two repair lanes share exactly one filter authority, CA-R-1850; no second grammar or parser authority is introduced.
