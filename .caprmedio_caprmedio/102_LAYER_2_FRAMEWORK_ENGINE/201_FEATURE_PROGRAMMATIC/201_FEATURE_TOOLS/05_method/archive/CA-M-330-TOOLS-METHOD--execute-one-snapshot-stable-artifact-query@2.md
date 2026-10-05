---
atom_id: CA-M-330
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: FIND_AND_FETCH_ARTIFACTS
  depends_on: [Tool, Artifact, Markdown, Journal]
relations:
  relates_to: [CA-R-1849, CA-R-1850, CA-O-159, CA-D-527, CA-D-528, CA-D-529]
---
# Summary

Execute one snapshot-stable Artifact query

## Scope

The query evaluation method for FIND_AND_FETCH_ARTIFACTS, not a new parser,
Workflow, or Journal.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** have CA-O-159 enumerate and retain one
allowlisted Markdown snapshot before parsing the closed filter grammar, then
evaluate and paginate only that retained snapshot in canonical identity order.

## Details

Reuse the existing safe Markdown/frontmatter parser and shared RUN_SUPPORT/Work
Journal library. Validate the full snapshot before accepting a result; preserve
per-carrier diagnostics and reject ambiguity or incomplete reads. Apply
CA-R-1850 without delegation to SQL, code, or eval; retain distinct
frontmatter/section namespaces and generic identity policy. Fetch bodies only
after matching identity and explicit selected request. Bind cursors to retained
digest and exact retained members; continuation cannot enumerate again. Enforce
resolved budgets and return measured coverage. No helper writes carriers,
Projections, Runs, or Journal Events on its own.
