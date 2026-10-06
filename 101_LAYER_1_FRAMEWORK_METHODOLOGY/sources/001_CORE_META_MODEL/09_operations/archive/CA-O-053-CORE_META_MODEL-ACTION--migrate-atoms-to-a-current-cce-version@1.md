---
subjects:
  governs: "Migrate Atom CCE Representation"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Projection"
    - "CCE"
    - "Confidence Threshold"
    - "Operator"
    - "AI Agent"
cce_version: cce_1
cce_form: definition
version: 1
updated_at: "2026-09-17 05:05:28 +0000"
relations:
  child_of:
    - CA-M-115
    - CA-R-380
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Migrate Atoms to a current CCE version

Migrate Atom CCE Representation **means** the reusable Action that converts **=1** Atom's representation **to** the current CCE version while preserving its Claim, identity, **and** lifecycle. repeat this Action one Atom at a time for a selected set.

1. read the Atom's complete current Claim **and** applicable CCE authority.
2. convert its representation **without** changing the Claim **or** lifecycle. preserve its identity under CA-R-1432 **and** keep its Summary fixed under CA-R-1464; a required replacement is **not** an identity-preserving CCE migration.
3. validate its **=1** Claim **and** source-faithful derived Projections. checking the Summary does **not** authorize regenerating it for the same Atom identity.
4. resolve the effective Confidence Threshold for the migration according **to** CA-M-271. **if** semantic confidence is below that value, **then** request Operator disposition **before** continuing.

an Operator **or** AI Agent **may** perform this Action within its existing authority. the conversion **must not** silently split **or** merge Claims, replace an Atom's identity, **or** change its Summary; those effects require the separately governed replacement boundary under CA-R-1432. preserving identity does **not** prohibit a required Revision.
