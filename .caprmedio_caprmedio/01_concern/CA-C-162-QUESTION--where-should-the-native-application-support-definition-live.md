---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "CAPRMEDIO Framework"
  depends_on:
    - "Project"
    - "Atom/Claim"
    - "Framework Instance Settings"
    - "Tool"
priority: medium
version: 1
updated_at: "2026-09-17 16:22:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Where should the native application support definition live?

should the native-support definition **in** CA-R-826 remain a local qualifier of that Boundary Claim **or** become separately governed reusable authority, **and** which owner preserves its intended applicability?

## Evidence

- CA-R-826 fixes the current native application support set **to** Codex, defines native support as CAPRMEDIO-owned adapter installation, invocation **and** host-session identity handling **without** a compatibility Extension, **and** reserves boundary expansion **to** later active Boundary authority.
- current available product support is **not** the same fact as the selected application **in** Framework Instance Settings. moving the whole Claim into Settings would lose that distinction.
- the adapter definition could be a qualifier needed **to** interpret this single support boundary **or** independently reusable terminology; the active Claim does **not** declare that boundary explicitly.

## Principle check

CA-M-001 requires a genuine decomposition boundary; CA-M-002 rejects duplicated definitions; CA-M-005 prohibits unnecessary Entities; CA-R-1490 preserves the support limits **and** adapter responsibilities. these Principles do **not** establish that an independent definition Atom is necessary **or** identify its intended owner.

## Disposition

retain CA-R-826 **and** the current support set. review the definition's actual reuse **before** splitting; **if** it is independently governed, preserve all adapter conditions **and** replace the predecessor under the Atom identity rules. do **not** expand supported applications, confuse support with selected Settings, **or** silently move a Project capability into the universally applicable Core Meta-Model.
