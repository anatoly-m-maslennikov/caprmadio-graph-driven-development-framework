---
atom_id: CA-O-008
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Apply Approved Source Corrections"
  depends_on:
    - "Action"
    - "Operator"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Framework Instance Settings"
    - "Project Settings"
version: 2
updated_at: "2026-09-16 22:01:42 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Apply approved source corrections

Apply Approved Source Corrections **means** the reusable Action that applies **only** the exact upstream corrections authorized for the current proposal, conflict, **and** source frontier.

1. **before** mutation, revalidate the actual Operator authorization recorded under CA-O-007 **and** the relevant current source state. missing, rejected, stale, partial, ambiguous, **or** mismatched approval blocks mutation.
2. apply the approved correction through the owning source's separately authorized change workflow. resulting Claims remain **in** their owning source Atoms; resulting selections remain **in** their owning settings. compilation **and** the approval record do **not** themselves grant source-change authority.
3. record actual execution, changes, failures, **and** partial effects **in** the Journal; report the resulting source frontier **or** exact failure. a Journal record describes those effects **without** replacing the current source authority.
4. return changed sources for renewed selection **and** Evaluation under the calling Process.

this Action **must not** edit projected Claims as a conflict fix, infer additional corrections, create a duplicate approval Atom, **or** claim completion **after** a failed correction. retries **and** recovery require their applicable accepted authority **and** bounds; this Action does **not** authorize automatic rollback **or** unbounded repetition.
