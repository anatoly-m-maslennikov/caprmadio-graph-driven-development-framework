---
subjects:
  governs: "feature-boundary"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
cce_version: cce_1
cce_form: obligation
version: 19
updated_at: "2026-09-16 21:24:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1491
---
# Gather provisional programmatic action context concurrently

COMMIT_CONTEXT **must** be independently invocable **and** strictly read-only. from **=1** durable trigger, it **must** gather provisional action context containing the sealed Initiative **and** action identity, observed repository frontier, affected subject identity, expected **and** observed Revisions **or** digests, candidate change, Git state, Journal state, **and** available provenance bindings.

- multiple context gatherers **may** work concurrently because their output is provisional **and** mutation-free. identical input **and** an unchanged observed frontier **must** produce the same context identity.
- context capture **must not** require the observed Project state **to** conform **to** Applicable Methodology. retain observable Carrier identity **and** evidence **when** Atom classification, names, properties, **or** relations are unresolved **or** invalid; do **not** invent a conforming identity **or** successful classification.
- no gathered context grants authority **to** mutate.
- a consumer changing governed Project state **or** Git state **must** revalidate its mutation preconditions against the current repository frontier, expected subject Revision **or** digest, **and** durable action state immediately **before** that effect.
- Journal admission follows CA-R-1491 instead: preserve intact sealed observations about the recorded event. subsequent Project changes alone **must not** prevent historical recording; altered **or** incomplete event envelopes remain storage-integrity failures.
