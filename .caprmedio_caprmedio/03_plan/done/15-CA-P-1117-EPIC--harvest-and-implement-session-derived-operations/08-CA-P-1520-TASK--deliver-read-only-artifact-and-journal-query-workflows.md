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
version: 6
updated_at: "2026-10-08 00:06:48 +0000"
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1124, CA-P-1655]
---
# Summary

deliver read-only artifact and journal query workflows

## Objective

Deliver exactly two additional Workflows: Find and Fetch Artifacts (Markdown carriers) and Find and Fetch Journal Events. Each uses a minimal Workflow and one query Action/Tool. This composite owns the new-query branch only; it does not modify the original thirteen-Workflow implementation packets or authorize more Workflows.

Both routes are read-only. Artifacts expose frontmatter and Markdown heading/section properties; Journal Events expose their Event fields. Use a bounded non-evaluating equality/inequality/NOT/IN filter grammar with unambiguous boolean composition, return Artifact IDs or Event IDs by default, and fetch only selected fields/sections or full Events on request. Identities come from their authoritative carriers, never filenames. Preserve requested statuses/properties and report malformed carriers/Events, missing IDs, duplicate properties/headings or Event fields, incomplete reads, invalid filters and bounded coverage/pagination. Do not fetch credentials/secrets, create mutation authority or invent Runs. Shared execution journaling must not alter or enlarge the captured query-source snapshot.

## Work decomposition

P1521/P1523 authored the respective source packets; P1522/P1524 independently rejected initial gaps. P1530/P1531 repaired them; P1532 accepted Artifact sources, while P1534/P1535 repaired and accepted the final Journal sources after P1533's remaining rejection. P1525/P1526 implement test-first Tools with P1537/P1538 finishing the Artifact/shared-filter contract; P1544 independently verifies combined Tool coverage. P1542/P1543 author and accept the additive fifteen-route MCP source contract, then P1527 integrates the existing discovery/MCP/orchestrator/shared execution. P1528 proves fresh immutable-image E2E and P1529 independently reviews closure. Each child is a <=15-minute packet inheriting P1117's 90% threshold; exact current source IDs/Versions/paths/hashes and true blocking gates must be rebound before dispatch.

## Details

### Centralized Project carriers

Find and Fetch Journal Events reads canonical Event carriers from the selected Project's `_journal/` root. Persisted query-result Projections use that Project's `_projection/` root; ephemeral response/report state remains temporary. The shared Run recorder uses the same canonical `_journal/` root. Existing immutable historical Event references may retain their original sealed locations; relocation must resolve them without rewriting Event bytes.

### Definition of Done

Both source/RMED packets, independent reviews, Tools, route integration, fresh-image evidence, and closure review are Done with exact source/implementation/image/Run/Action/result evidence. Original13 work continues independently; P1171's final image-coverage review and P1124 closure require this branch's accepted proof.

## Source-review repair frontier

The current source gates are ACCEPTED P1532 and P1535. Completed REJECTED P1522/P1524/P1533 are retained history, not admission. Root reran 15 Artifact/shared-parser and 8 Journal tests successfully; P1544 coverage review remains pending, so Tool completion is not yet inferred. Actual shared Run/MCP behavior, source capture before own execution Events, fresh-image proof and closure remain separate required work. Exactly one CA-R-1850 filter authority and one shared parser are reused.

## Approved first-cut disposition

The first cut retains the six Workflow vertical slice for Atom CRUD/status, Implementation and Applicable Methodology, together with stdio/orchestration/journaling and Docker HTTP MCP transport. This standalone read-only query branch is deferred to a later milestone. It remains Active: no query source, Tool, route, image, Run or closure gate is marked Done, waived or inferred from the retained first cut. Existing lifecycle/runtime current-source binding maintenance may remain a supporting first-cut need; it does not reopen this query branch.
