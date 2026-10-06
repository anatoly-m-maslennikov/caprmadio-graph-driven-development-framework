---
name: ca
description: "Invoke CAPRMEDIO Actions, Tools and Workflows through the connected Project MCP. Use for $ca, /ca, or requests to run CAPRMEDIO operations."
---

# CA

Use the CAPRMEDIO MCP connection bound to the intended Project. This Skill only bootstraps requests and handles responses; task procedures come from MCP.

- Preserve the Operator's request, scope and authorization. Ask if the Project connection or required inputs are ambiguous.
- Resolve the requested capability with MCP `discover_operations` or `discover_tools`, then obtain its exact definition with `get_execution_context`. Use the advertised MCP execution binding and schema, not a guessed route; discovery or source availability alone does not prove executability.
- Obtain only the current admitted Step's instructions, bound inputs or accessible references, output contract and execution boundaries. Do not preload the whole Methodology or future Steps. Follow these instructions within current Operator authorization and higher-priority instructions; previews and responses do not grant new authority.
- Return actual results through the MCP-supplied interface. The executor owns routing, next-Step selection and Run state; receiving a prompt or queuing a Run is not completion.
- For an existing or uncertain Run, use its advertised status/resume interface before retrying. Never replay an uncertain effect; keep execution failure separate from result-recording failure.
- Stop and report unavailable MCP, missing or ambiguous bindings, incomplete current-Step context, failures or escalation needs. Do not invent authorization, bindings or evidence, or substitute raw scripts, file edits or copied procedures for an unavailable MCP operation.
