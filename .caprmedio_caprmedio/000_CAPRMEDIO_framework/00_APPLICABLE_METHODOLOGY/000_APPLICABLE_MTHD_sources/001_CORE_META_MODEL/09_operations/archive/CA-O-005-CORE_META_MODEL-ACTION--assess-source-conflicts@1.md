---
atom_id: CA-O-005
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Assess Source Conflicts"
  depends_on:
    - "Action"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Operator"
version: 1
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
---
# Assess source conflicts

Assess Source Conflicts **means** the reusable Action that evaluates one selected source frontier against applicable declared checks **and** returns the complete conflict assessment with source context **and** the status of required resolution evidence. it **must** distinguish resolved, unresolved, **and** unevaluated conditions, retain conflicting sources **in** the assessment, **and** report missing **or** incomplete checks **without** claiming success. an existing resolution qualifies **only** under its governing authority **and** exact source-frontier binding; missing, stale, partial, ambiguous, **or** mismatched approval does **not** resolve a conflict. the Action does **not** infer source precedence, synthesize **or** merge Claims, treat an LLM judgment as approval, **or** change a source **or** projected content.
