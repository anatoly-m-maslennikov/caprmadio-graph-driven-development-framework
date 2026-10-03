---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Assess Atom Update Identity"
  depends_on:
    - "Atom"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Workflow Run"
    - "Operator"
version: 1
updated_at: "2026-09-18 21:23:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-O-067", "CA-R-1432", "CA-R-1464", "CA-R-1520"]}
---
# Validate update-to-replacement routing

the Evaluation **must** check the update assessment **and** its terminal replacement result under CA-O-067.

- a proposed change preserving identity under CA-R-1432 returns the admitted change class **without** claiming authorization **or** persistence.
- a changed Summary returns replacement required even **when** the Claim is unchanged; no intermediate update is persisted.
- a proposal that initially preserves identity but later needs another Summary is reassessed **and** redirected **before** the incompatible update is committed.
- an incomplete proposal **or** uncertain change class returns unresolved rather than silently choosing update **or** replacement.
- the replacement-required result carries enough information under CA-R-1520 for the executor **to** continue; the update Run ends **without** calling, waiting for, **or** claiming completion of replacement.

check this behavior with a read-only fixture. execution of the governed replacement itself is outside this assessment Action.
