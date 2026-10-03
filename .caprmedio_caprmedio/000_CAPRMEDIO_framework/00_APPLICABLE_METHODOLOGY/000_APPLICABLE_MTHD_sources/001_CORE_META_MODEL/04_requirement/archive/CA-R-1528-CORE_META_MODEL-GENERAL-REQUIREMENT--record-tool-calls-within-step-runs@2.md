---
subjects:
  governs: "Step Run/Tool Call"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Tool"
    - "Journal"
    - "Journal/Record"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"relates_to": ["CA-R-1452", "CA-R-1509", "CA-R-1511", "CAPRMEDIO-META-REQU-158"]}
---
# Record Tool calls within Step Runs

a Tool Call **means** an invocation of a Tool during execution; **when** it occurs within a Step Run, its execution evidence **must** remain associated with that parent Step Run **in** the canonical Project Journal.

- retain the invoked Tool, supplied inputs, actual result **or** error, **and** parent Step Run association. preserve call identity **and** timing sufficient **to** distinguish separate attempts; do **not** report an attempted **or** uncertain effect as confirmed completion.
- use authorized references **or** protected representations for secret **or** sensitive inputs under their governing rules; execution tracing does **not** authorize copying secrets into the Journal.
- the parent Step Run invokes its **`=1`** declared Action. its internal Tool calls are execution details, **not** automatically new Steps, sub-steps, Action definitions, **or** Workflow nodes.
- a view **may** display Workflow Run, Step Run, **and** Tool-call evidence as a nested trace; derive the view from the canonical records rather than creating another independently maintained execution history.
- preserve actual ordering **and** parentage **without** inferring concurrency permission, Workflow routing, **or** a new Step Run for **every** Tool call.
