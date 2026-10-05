---
atom_id: "CA-M-345"
content_role: "Method"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
global_tier: 10
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Atom/Content Role: Analysis/Type: FPF Analysis Report"
  depends_on:
    - "Atom/Summary"
    - "FPF"
    - "Artifact/Revision"
version: 1
updated_at: "2026-10-05 23:46:22 +0400"
relations:
  method_for: ["CA-R-1889"]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/05_method/CA-M-345-PROJECT_CONFIGURATION-GENERAL--author-fpf-analysis-reports.md
  source_atom_id: CA-M-345
  source_atom_revision: 1
  source_sha256: 4ef3293ad8babbb6521967ceaf29c65d7c546c45b8a6a6c10894e3d980eae112
  original_relations_sha256: 51a3170543cdff5b64dbe79861991666e642972d2a0b271b7bd65b50dc3d1df6
---
# Summary

Author FPF Analysis Reports

## Scope

authoring and content-preserving import of FPF Analysis Report Atoms.

## Claim

**to** author an FPF Analysis Report, use the common Analysis structure under CA-D-479 and retain the report's bounded question, scope, approach, results, provenance and evidence limits without treating its recommendations as accepted specification.

- carry `content_role: Analysis` and `type: FPF Analysis Report`, the actual owning Scope Unit, applicable tier, Author, Status and Revision Properties. Summary describes the Question; TLDR summarizes the retained analytical record without replacing Results.
- **when** importing an existing report, preserve its complete original UTF-8 text as quoted Markdown in Results. Quotation is a carrier wrapper, not an edit to the original text. Record its original path, SHA-256 and byte length in Approach so the original bytes can be recovered and checked.
- identify the original inquiry from its explicit task or question where available; otherwise identify the bounded historical report without inventing a missing execution contract. Preserve all native findings, alternatives, citations, limitations and time-relative statements in the quoted record.
- distinguish import metadata and its current Revision timestamp from the original report's provenance. Do not infer an original execution timestamp or completed FPF Run merely from a filename or physical file existence.
- place the Carrier by the applicable Analysis Delivery rules. Resolve real destination links to the new Carrier while retaining historical Journal, archive and frozen-evidence references unchanged.

## Details

Importing a report does not rerun FPF, adopt a candidate, change project policy or close an issue. Completion of the bounded imported reporting product is distinct from those outcomes.
