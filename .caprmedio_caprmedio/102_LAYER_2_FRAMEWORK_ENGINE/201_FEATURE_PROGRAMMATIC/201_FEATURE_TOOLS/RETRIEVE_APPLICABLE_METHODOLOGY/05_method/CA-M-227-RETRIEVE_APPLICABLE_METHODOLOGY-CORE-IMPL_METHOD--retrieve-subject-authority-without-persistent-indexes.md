---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Retrieval Tool/Execution"
  depends_on:
    - "Applicable Methodology Retrieval Tool"
    - "Applicable Methodology Retrieval"
version: 4
updated_at: "2026-09-15 19:28:04 +0400"
relations:
  method_for:
    - CA-R-1241
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Retrieve Subject Authority Without Persistent Indexes

**to** retrieve applicable authority, the Tool **must** perform **all** of the following:

1. resolve **every** projected Atom's authoritative source from the selected source frontier using its retained Atom ID **and** Revision; fail closed **if** that binding is missing **or** ambiguous, the source is no longer current, **or** the projected Carrier bytes differ from the source. do **not** require **or** insert embedded Projection metadata.
2. derive GOVERNS **and** DEPENDS_ON indexes **in** memory.
3. seed exact matching governed Subject Paths **and** close **every** prerequisite transitively; fail closed on an unresolved prerequisite.
4. emit ordered source-backed Carrier records with their resolved source bindings.
5. write no persistent Subject Index Carrier **or** cache.


## Sources

- [CA-R-1241 — Require Source-Backed Subject Retrieval](../04_requirement/CA-R-1241-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-REQUIREMENT--require-source-backed-subject-retrieval.md)
