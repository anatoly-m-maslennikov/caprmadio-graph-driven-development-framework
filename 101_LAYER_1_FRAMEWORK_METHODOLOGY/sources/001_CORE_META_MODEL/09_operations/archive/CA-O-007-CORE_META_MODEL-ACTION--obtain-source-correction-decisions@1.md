---
atom_id: CA-O-007
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Obtain Source Correction Decision"
  depends_on:
    - "Action"
    - "Operator"
    - "AI Agent"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Journal"
version: 1
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
---
# Obtain source correction decisions

Obtain Source Correction Decision **means** the reusable Action that presents an exact conflict-resolution proposal **and** its selected source frontier **to** the Operator, requests an explicit decision, **and** records the actual decision with its proposal, conflict, source-frontier binding, **and** provenance under applicable source-authority **and** Journal rules. approval, rejection, requested revision, **and** absence of a decision **must** remain distinguishable. absence of an Operator decision, inferred intent, AI Agent confidence, **or** an LLM judgment **must not** be treated as approval. the Action **must not** apply a proposed correction **or** record approval that the Operator did **not** give; a changed proposal **or** source frontier requires the decision's applicability **to** be checked again **before** reliance.
