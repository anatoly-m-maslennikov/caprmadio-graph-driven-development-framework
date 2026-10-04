---
atom_id: CA-C-297
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Session-harvest Analysis/Main Content"
  depends_on:
    - "Markdown Atom Carrier/Main Content"
version: 1
updated_at: "2026-10-04 07:41:00 +0400"
relations:
  concern_about:
    - CA-A-906
    - CA-A-907
    - CA-A-908
    - CA-P-1118
---
# Summary

Harvest reports omit the registered TLDR heading

## Concern

Root's full-parser/heading verification found that the three completed harvest Analysis carriers omitted the literal required `## TLDR` heading. Their substantive evidence was retained, but their body Properties did not fully follow current Delivery authority. Resolved: root added truthful local-result summaries to CA-A-906/907 and renamed CA-A-908's existing Conclusions heading to TLDR, without changing harvested decisions or claiming monthly completion. New packets must use the exact required Analysis headings.

## Evidences

- CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties v6 requires Question, Scope, Approach, Results and TLDR in this order, exactly once.
- The first comprehensive root verification failed on the missing CA-A-906 TLDR; direct saved-carrier inspection confirmed the same omission in CA-A-907 and CA-A-908's synonymous Conclusions heading.
- Repaired saved carriers retain complete packet coverage, unfinished frontiers and provisional candidate status. The later strict YAML/heading check records actual verification; subagent source-integrity checks are not represented as the earlier comprehensive heading check.
- Root's temporary scoped diagnostic submitted actual saved carrier bytes to the existing Docker worker's duplicate-rejecting safe YAML parser. It passed68 Plans and five supporting carriers, exact headings/order, unique IDs, Done placement and the completion/BLOCKS DAG. No container mount or local environment repair was needed.

## Blast radius

Only CA-A-906/907/908 carrier summaries/headings and subsequent packet authoring templates. No source content, methodology model, implementation or acceptance of Operations changed. This resolved formatting defect does not block independent harvest work.
