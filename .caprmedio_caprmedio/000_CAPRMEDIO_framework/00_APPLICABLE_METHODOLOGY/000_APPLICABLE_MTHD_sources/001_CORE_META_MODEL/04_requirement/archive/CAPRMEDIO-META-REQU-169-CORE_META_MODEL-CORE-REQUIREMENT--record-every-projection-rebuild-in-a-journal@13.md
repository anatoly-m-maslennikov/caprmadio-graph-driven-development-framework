---
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 13
updated_at: "2026-09-10 07:24:21 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
---
# Record every Projection rebuild in a Journal

**every** Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.
