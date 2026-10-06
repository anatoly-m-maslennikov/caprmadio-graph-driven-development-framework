---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Retire Legacy Structural Projections"
  depends_on:
    - "Action"
    - "Projection"
    - "Project Structure"
    - "Project Scope Unit Graph Projection"
    - "Artifact/Carrier"
version: 1
updated_at: "2026-09-17 15:15:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to":["CA-D-332","CA-D-343","CA-R-1483"]}
---
# Retire legacy structural Projections after consumer cutover

Retire Legacy Structural Projections **means** the Action that retires the obsolete Project Scope Unit Graph Sources Projection **or** Project Scope Unit Graph Projection **after** validated direct-consumer cutover.

- the selected target is a legacy Projection retained under CA-D-332 **or** CA-D-343, **not** authoritative Project Structure.
- retire that target **only** **after** its direct-consumer cutover is validated; an unresolved cutover does **not** satisfy this condition.
- preserve its recorded migration disposition **and** return the actual retirement result. this Action does **not** require rebuilding **or** refreshing the obsolete Projection **or** reintroducing consumer dependence.

this Action governs the retirement job only; it does **not** grant new mutation authority **or** prescribe the Tool implementation that performs it.
