---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Assess Source Conflicts"
  depends_on:
    - "Action"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Atom/Global Tier"
    - "Atom/Revision/Updated At"
    - "Atom/Local Tier: Principle"
    - "Operator"
version: 3
updated_at: "2026-09-16 22:42:50 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Assess source conflicts

Assess Source Conflicts **means** the reusable Action that assesses one exact selected source frontier against its applicable authority **and** returns the conflict assessment **without** changing sources.

1. load the current accepted active authority **and** applicable Project Principles **before** relying on an earlier report **or** proposed fix.
2. identify the conflicting Claims **and** their applicability. for RMEDO Atoms, collect Global Tier, exact Revision, **and** Updated At. distinguish an actual conflict from different permitted cases.
3. for RMEDO conflicts, preserve higher-tier authority, whose Global Tier number is lower. within the applicable authority boundaries, prefer the freshest accepted active Claim over a conflicting older Claim; Updated At **must not** permit a lower-tier Claim **or** prohibited source override **to** defeat higher-tier authority.
4. check **every** proposed disposition against the active Principles **and** retain the evidence for its effect on alignment. a conflict between active Principles requires the Operator under CA-R-830.
5. distinguish resolved, unresolved, **and** unevaluated conditions. report missing checks, uncertain applicability, equal **or** ambiguous timestamps, **and** unresolved authority **without** inventing precedence.
6. verify required resolution evidence against the exact proposal **and** current source frontier. missing, stale, partial, ambiguous, **or** mismatched approval **or** delegation does **not** resolve a conflict.

7. check affected authority coverage, including still-required Claims, active references **and** Relations, **and** required Evaluations. report an unresolved gap separately from a resolved conflict; absence of a conflict does **not** prove complete coverage.

this Action **must not** synthesize **or** merge Claims, treat an LLM judgment as Operator authorization, change source **or** projected content, **or** silently exclude a conflicting source from the assessment.
