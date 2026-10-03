---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "feature-boundary"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 15
updated_at: 2026-09-15 03:15:32 +0400
---
# Separate project-local runtime and temporary state

**all** Tools **in** one CAPRMEDIO Project **must** use one project-local runtime rooted
at `.caprmedio_runtime/` **and** one project-local temporary-state root at
`.caprmedio_tmp/`. The runtime **contains** content-addressed executable releases,
shared non-executable libraries, machine-readable registries, declared
dependencies, stable launchers, Hook Carriers, logs, sessions, databases,
service state, **and** resumable state. The temporary-state root **contains** **only**
disposable scratch, staging, cache, build, Evaluation, atomic-write
intermediate, **and** interrupted-cleanup Carriers.

An installed Tool **must** import executable **and** non-executable implementation
**only** from its selected release under `.caprmedio_runtime/tools/`; it **must not**
import Framework implementation from the canonical source tree, the configured
Project control root, `.caprmedio_tmp/`, **or** another Project path. Host
interpreters **and** Git remain declared substrate dependencies rather than copied
Framework implementation. A host-required discovery Carrier **may** point into
`.caprmedio_runtime/tools/`, but it **must** contain no independent Framework
behavior **and** **must not** become dependency authority.
