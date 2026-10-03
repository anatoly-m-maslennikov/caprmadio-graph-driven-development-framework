---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "runtime"
  depends_on:
    - "Tool"
    - "Carrier"
version: 8
updated_at: "2026-09-17 21:51:40 +0000"
relations:
  evaluation_for:
    - CA-M-143
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Isolate one Tool runtime folder

## Claim checked

**every** Tool that persists runtime files uses its dedicated owned runtime directory under CA-M-143. a shared runtime service owns its own directory; clients use its interface rather than accessing its files.

## Test cases

- run two Tools that persist their private runtime files concurrently.
- include an owned shared runtime service that both Tools access through its admitted interface.
- include a negative case **where** a client reads **or** writes another owner's files directly, **or** relies on an unowned shared directory.

## Acceptance criteria

- **every** Tool writes its private state **only** below its own runtime directory **or** admitted bounded run-specific descendant.
- the shared service alone owns its persistent files. client use of its interface is **not** rejected merely because the service is shared, **and** does **not** grant file access **to** its clients.
- the negative case is reported as an ownership-boundary failure; no shared directory is silently assigned an owner **to** make the check pass.

## Failure disposition

stop the affected Tool execution **and** report the ownership boundary that failed. reject either a private-file access violation **or** an unsupported ban on the admitted shared-service interface.
