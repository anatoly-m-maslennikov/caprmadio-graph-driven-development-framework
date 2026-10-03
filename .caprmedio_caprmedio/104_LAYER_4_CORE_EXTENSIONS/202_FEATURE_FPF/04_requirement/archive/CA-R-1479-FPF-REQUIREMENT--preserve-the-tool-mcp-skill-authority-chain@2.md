---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "FPF"
  depends_on:
    - "Tool"
    - "MCP"
    - "Skill"
version: 2
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve the Tool-MCP-Skill authority chain

The FPF Extension **must** realize deterministic behavior first in canonical project-local Tools, expose admitted Tool contracts through the project-local provider-neutral MCP service without changing their meaning, and make the `fpf` Skill a thin direct consumer of that MCP surface; the Skill **must not** duplicate Tool mechanics, MCP transport, lifecycle control, or a `ca` routing wrapper, and Consumer-owned Demands **must not** be admitted before they target **`=1`** identified current MCP Implementation result.
