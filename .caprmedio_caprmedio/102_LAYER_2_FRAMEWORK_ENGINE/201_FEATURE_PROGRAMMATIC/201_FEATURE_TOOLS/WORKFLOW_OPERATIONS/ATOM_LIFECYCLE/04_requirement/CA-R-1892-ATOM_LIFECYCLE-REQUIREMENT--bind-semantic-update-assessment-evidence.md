---
atom_id: CA-R-1892
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Semantic Update Assessment Evidence"
  depends_on: ["CA-O-067", "CA-R-1432", "CA-R-1464", "Analysis Report"]
version: 1
updated_at: "2026-10-06 05:33:09 +0000"
relations:
  relates_to: [CA-R-1825, CA-R-1826, CA-R-1827]
---
# Summary

Bind semantic Update assessment evidence

## Scope

Tool realization of one substantive Atom Update through the existing O067/O145/O129 lifecycle boundary.

## Claim

A Tool **must** treat a substantive Update as unresolved unless one current, completed `Analysis` Atom of type `Analysis Report` supplies exact, read-only-verifiable semantic assessment evidence. The evidence **must** establish unchanged Summary and same primary-Claim identity, one admitted R1432 class, a declared delta, and completed lineage-impact review. It is evidence only: it does not grant Operator permission, effect admission, or any other authorization.

## Details

The report is eligible only when its current source-derived Analysis status is `Done`. Its evidence binds the exact target, complete proposal, current CA-R-1432 and CA-R-1464 authority, admitted class, preserved primary Claim identity, declared delta and completed lineage review. CA-D-585 defines the request and report representation.

O145 and O129 independently reopen the report and every declared pin. They compare the report to the current target and complete proposal, source-derived Analysis whitelist, and current R1432/R1464 bytes. Missing, stale, malformed, ambiguous, non-Done, non-Analysis-Report, mismatched, or unverifiable evidence returns `unresolved` before mutation. A report with `replacement` produces the existing Replace handoff; no report may make a same-ID Update eligible when its Summary changes.

The Tool seals only the normalized verified evidence from a completed O145 Step together with its exact request binding. O129 revalidates that seal immediately before effects. Mechanical lossless normalization remains separately provable without this optional report.
