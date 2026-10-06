---
atom_id: CAPRMEDIO-GOV-REQU-355
cce_version: cce_1
cce_form: classification
subjects:
  governs:
    continuant:
      - external-boundary
version: 13
updated_at: "2026-09-11 22:30:02 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-164
  resolution_of:
    - CAPRMEDIO-GOV-CONC-053--what-external-review-envelope-is-sufficient
---
# Use external Analysis Atoms as review envelopes

an external review **must** be imported as an External Analysis Report Atom whose governed envelope identifies its source, provenance, reviewed scope, original body, **and** native attachments **without** requiring a provider-specific finding schema. one internal Analysis derives from that Atom, records the project's finding-level interpretation **and** dispositions, **and** becomes the **only** Analysis source from which project-owned Concern, Plan, Requirement, Method, Evaluation, **or** Delivery Atoms are derived. **every** accepted disposition that changes project meaning **or** work is materialized **in** its owning CPRMAD Content role; rejected **or** non-actionable findings remain **only** **in** the internal Analysis.
