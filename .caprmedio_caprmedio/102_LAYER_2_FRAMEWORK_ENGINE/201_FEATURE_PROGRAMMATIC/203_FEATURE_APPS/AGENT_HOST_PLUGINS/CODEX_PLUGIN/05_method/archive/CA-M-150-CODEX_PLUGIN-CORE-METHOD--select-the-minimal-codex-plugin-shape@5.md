---
subject_scopes:
  - plugin-architecture
version: 5
updated_at: 2026-08-23 11:39:04
relations:
  method_for:
    - CA-R-1073
---
# Select the minimal Codex plugin shape

Select the Codex plugin shape through this procedure:

1. Start from the bounded CAPRMEDIO workflows that the plugin must make available in Codex and identify the provider-neutral authority that each workflow references.
2. Package a workflow as a skill when instructions and capabilities already available to Codex are sufficient; add an MCP server only when the workflow requires controlled tools, an external service, authentication, or independently operated infrastructure.
3. Combine skills with an MCP server only when reusable workflow guidance must govern use of those tools, and add UI only when inspecting, comparing, editing, confirming, or navigating structured information materially improves the workflow.
4. Keep every MCP tool useful without UI so Codex can complete the same supported workflow headlessly.
5. Keep Codex-only host wiring, including optional hooks, inside `CODEX_PLUGIN`; reference rather than duplicate provider-neutral CAPRMEDIO behavior.
6. Record the selected skills, MCP connection or server, optional UI, optional hooks, excluded capabilities, and the evidence that each included component is necessary before packaging begins.
