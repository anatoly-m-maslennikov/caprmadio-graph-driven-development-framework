---
atom_id: CA-R-1480
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "FPF"
  depends_on:
    - "Hook"
    - "Tool"
    - "MCP"
    - "Background Service"
version: 1
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
---
# Keep triggered FPF work off the command-host path

**every** Hook-triggered or deferred FPF action **must** synchronously perform only bounded validation and durable idempotent intake before returning to the command host, after which the existing project-local asynchronous manager and Scheduler **must** dispatch isolated workers; the manager **must not** perform domain work or create one worker per Hook event, and the service **must** expose responsive manual `status`, `stop`, `start`, and `reload` controls plus bounded automatic timeout, heartbeat, retry, quarantine, restart, and circuit-breaker behavior while preserving accepted work and effect gates.
