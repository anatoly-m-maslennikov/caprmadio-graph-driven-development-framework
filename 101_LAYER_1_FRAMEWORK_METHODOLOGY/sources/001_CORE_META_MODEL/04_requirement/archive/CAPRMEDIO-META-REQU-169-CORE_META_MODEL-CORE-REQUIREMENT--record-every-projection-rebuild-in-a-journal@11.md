---
atom_id: CAPRMEDIO-META-REQU-169
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 11
updated_at: "2026-09-10 07:24:21 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
---
# Record every Projection rebuild in a Journal

**every** Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.
