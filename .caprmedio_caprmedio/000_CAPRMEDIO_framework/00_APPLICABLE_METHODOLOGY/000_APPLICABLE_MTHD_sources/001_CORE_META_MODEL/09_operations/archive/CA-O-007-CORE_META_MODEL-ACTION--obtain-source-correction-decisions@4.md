---
subjects:
  governs: "Obtain Source Correction Decision"
  depends_on:
    - "Action"
    - "Operator"
    - "AI Agent"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Journal"
    - "Journal/Record"
version: 4
updated_at: "2026-09-16 22:01:42 +0000"
relations: {}
---
# Obtain source correction decisions

Obtain Source Correction Decision **means** the reusable Action that obtains the Operator's explicit decision about an exact conflict-resolution proposal.

1. present the proposal, the conflict it addresses, **and** the selected source frontier **to** the Operator.
2. request an explicit decision. distinguish approval, rejection, requested revision, **and** absence of a decision; confidence, inferred intent, **or** an LLM judgment is **not** approval.
3. record the actual decision **in** the Journal with its proposal, conflict, exact source-frontier binding, **and** provenance. record a missing decision as missing, **not** as an approval **or** rejection.
4. return the recorded decision for the applicable authorization checks. a changed proposal **or** source frontier requires the decision's applicability **to** be checked again **before** reliance.

this Action **must not** apply the correction, record approval the Operator did **not** give, **or** create a duplicate approval Atom **in** Project Configuration. the Journal records the decision; it does **not** independently redefine the governing source Claims.
