---
atom_id: CA-R-1482
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
# Keep recovery controls independent from the active Tool path

The FPF Extension **must** provide one bounded manual recovery entrypoint for `status`, `stop`, `start`, and `reload` that remains operable without invoking an active Hook, Skill, MCP request, decision manager, or domain worker, and one independent automatic supervisor that may stop dispatch, restart a failed service within a declared budget, or open its circuit but **must not** perform or authorize domain effects; both control paths **must** preserve durable accepted work and report the exact selected release and process state.
