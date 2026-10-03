---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Analysis/Type: External Analysis Report"
  depends_on:
    - "Atom/Content Role: Analysis"
    - "Atom/Claim"
    - "Carrier"
    - "Action"
    - "Process"
priority: medium
version: 1
updated_at: "2026-09-17 13:54:37 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should external-review adoption authority be separated?

which Claims **and** reusable Operations preserve the external-review adoption boundary while separating its Carrier envelope, internal interpretation, **and** accepted-result creation?

## Evidence

GOV-REQU-355 requires an External Analysis Report envelope with source, provenance, reviewed scope, original body, **and** native attachments **without** a provider-specific finding schema. it also requires an internal Analysis **and** materialization of accepted dispositions, while rejected **or** non-actionable findings remain **in** that Analysis. META-REQU-164 repeats the internal-review authority boundary. both enumerate derived roles **without** Operations; GOV-REQU-355's final `CPRMAD` list also differs from its preceding list containing Evaluation. neither list can silently determine a new complete domain.

## Principle check

CA-M-002 requires one adoption-authority owner; CA-M-001 requires a complete, non-overlapping separation at the chosen level; CA-M-006 requires the role lists **and** boundaries **to** agree; CA-R-1490 protects the external report **and** rejected findings. CA-R-1342 assigns Carrier specifications **to** D, **and** CA-R-1344 assigns execution behavior **to** O. these establish the separation, but **not** the missing admitted result-role domain **or** exact reusable Action boundaries.

## Disposition

preserve both sources until their unique obligations are mapped **and** the resulting role domain is settled. keep source reports non-authoritative over Project decisions, reuse existing Analysis authority, **and** do **not** add an approval gate, discard Evaluation, assume Operations exclusion, **or** run an external review during this repair.
