---
content_role: Delivery
type: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "PROGRAMMATIC/software Evaluation record Carrier"
  depends_on:
    - "Artifact/Carrier"
    - "Atom/Claim"
    - "Atom/Content Role: Evaluation"
    - "Event"
    - "Evidence"
    - "Journal"
    - "PROGRAMMATIC/software carriers"
    - "Project Temporary State"
    - "Provenance"
    - "Tool"
version: 1
updated_at: "2026-09-23 19:08:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-M-285"], "relates_to": ["CA-D-250", "CA-D-437", "CA-E-455", "CA-R-1490", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-158"]}
---
# Summary

Deliver replayable software Evaluation records

## Claim

a PROGRAMMATIC software Evaluation evidence Carrier **must** represent one replayable result with the following bounded content:

- the evaluated target **and** source frontier, the checked Claim reference, **and** applicability limits.
- references **to** the canonical configuration **and** its digest, the Python **and** Evaluation Tool versions, **and** the technique selected under CA-M-285.
- the seed **or** reproducing case **when** applicable, including the minimized generated case **when** one was produced.
- the observed result, diagnostics, **and** exact replay command; distinct check outcomes remain distinguishable under CA-E-455 rather than being replaced by one undifferentiated pass value.

the Carrier uses the declared Evaluation evidence location under CA-D-250. disposable run output uses Project Temporary State under CA-D-437; valuable evidence under CA-R-1490 **must** remain recoverable from retained Carriers **or** durable source references **before** its temporary source disappears. reuse canonical Journal Event references under CAPRMEDIO-META-REQU-158 **without** creating another authoritative event history. provenance **and** Claim evidence remain distinct under CAPRMEDIO-META-REQU-097.
