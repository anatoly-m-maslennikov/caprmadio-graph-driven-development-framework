---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Status: Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Hub Atom"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1580", "CA-R-1583", "CA-R-1592", "CA-D-471", "CA-D-474"]}
---
# Validate Plan blocking and parallel readiness

the blocking Evaluation **must** reject a start **unless** **all** explicit blockers are Done **and** the applicable execution permissions hold.

- `A BLOCKS B`, `B BLOCKS C`: permit `A`, **then** `B`, **then** `C` **only** **after** the preceding Plan is Done.
- `A BLOCKS C`, `B BLOCKS C`: allow `A` **and** `B` **to** be ready concurrently; `C` waits for both.
- reorder leading navigation numbers **or** give two Plans the same Hub: do **not** invent another blocking edge.
- reject a self-edge, cycle, unresolved **or** non-Plan target, duplicate direct declaration, inverse declaration, **or** Plan scheduling encoded as `depends_on`.
- accept a Done blocker; Backlog, Active, Canceled, **and** Archived **must not** satisfy its completion gate.
- combine decomposition completion dependencies with blocking for deadlock detection: **if** Hub `H` decomposes **into** `A` **and** `H BLOCKS A`, reject the unsatisfiable cycle even though the blocking graph alone is acyclic.
- distinguish readiness from forced execution: a deterministic display order does **not** prohibit concurrent independent work **or** grant execution authority.

report the failing endpoints **and**, for a cycle, its complete prerequisite chain.
