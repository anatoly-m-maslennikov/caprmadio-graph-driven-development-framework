---
atom_id: "CA-E-588"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Atom/Content Role: Analysis/Type: FPF Analysis Report"
  depends_on:
    - "Artifact/Revision"
    - "Carrier"
version: 1
updated_at: "2026-10-05 23:46:22 +0400"
relations:
  evaluation_for: ["CA-R-1889"]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/06_evaluation/CA-E-588-PROJECT_CONFIGURATION-QA_CASE--check-fpf-analysis-report-imports.md
  source_atom_id: CA-E-588
  source_atom_revision: 1
  source_sha256: 992de8cbc5bd753cd46e693b4223ab91d04c74f46d48be97d77f7258de0195ed
  original_relations_sha256: 959b6b66b714bafc7e0737a40201ef12644e0e8c6f29681b7f4d735ec3bc48c9
---
# Summary

Check FPF Analysis Report Imports

## Scope

content-preserving migration of existing reports into FPF Analysis Report Carriers.

## Claim

an FPF Analysis Report import **must** pass all of the following checks before the original Carrier is retired:

- the exact Type and filename token are admitted, the carried Atom ID is unique, and the declared Content Role, owning Scope Unit, tier, Author, Status and Revision metadata match the selected authority;
- exactly one Summary and the ordered Question, Scope, Approach, Results and TLDR sections occur outside the quoted source content, with nonempty values;
- removing only the quotation wrapper recovers every original source byte, including Unicode, line endings, nested headings, code fences and terminal-newline state; its SHA-256 and byte length match the frozen source;
- every selected source has exactly one destination, no existing destination is overwritten, stale inputs and destination collisions stop the batch, and a failed batch does not retire an unverified source;
- rewritten current navigation/source links resolve to the intended new Carriers; historical Journals, archived Revisions, frozen receipts and the quoted report's own historical text remain unchanged.

## Details

These checks verify the import and Carrier structure, not the truth of external findings, FPF execution success, acceptance of recommendations or full framework/runtime conformance. Report unsupported validation coverage explicitly rather than treating an incomplete checker result as a pass.
