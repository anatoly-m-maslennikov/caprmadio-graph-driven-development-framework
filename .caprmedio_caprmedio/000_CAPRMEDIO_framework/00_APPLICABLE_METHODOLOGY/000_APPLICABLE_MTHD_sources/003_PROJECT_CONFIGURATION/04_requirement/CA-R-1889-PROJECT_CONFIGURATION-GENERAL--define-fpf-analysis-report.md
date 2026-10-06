---
atom_id: "CA-R-1889"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
global_tier: 10
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Atom/Content Role: Analysis/Type: FPF Analysis Report"
  depends_on:
    - "Atom/Content Role: Analysis"
    - "Analysis Report"
    - "FPF"
version: 1
updated_at: "2026-10-05 23:46:22 +0400"
relations:
  relates_to: ["CA-R-1888", "CA-R-1727", "CA-R-1875", "CA-D-479"]
---
# Summary

Define FPF Analysis Report

## Scope

the registered FPF Analysis Report Type under Content Role Analysis.

## Claim

an FPF Analysis Report **means** a specialized Analysis Report whose bounded inquiry **or** interpretation product records an FPF analytical command, composition, **or** directly related analytical follow-up, retaining its findings **and** stated evidence limits as reporting content rather than adopting them as normative authority.

## Details

The common Analysis body Properties remain Question, Scope, Approach, Results and TLDR under CA-D-479. The Analysis lifecycle and applicable Status model remain governed by CA-R-1727 and CA-R-1875; this Type does not introduce another Status domain or transition rule. A Done report can retain unresolved questions and rejected candidates. Done does not mean that its proposals were adopted, its issues were closed, or a tested implementation succeeded.

Historical statements remain bound to their original report context. Missing invocation, source revision, author, or execution evidence remains missing; the conversion must not invent it.
