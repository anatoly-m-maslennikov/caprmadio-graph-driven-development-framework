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
    - "Projection"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"evaluation_for": ["CA-R-1528", "CA-R-1511"]}
---
# Validate nested Tool-call evidence

the Evaluation **must** check Tool-call evidence within a Step Run under CA-R-1528.

- an Agentic Action makes several Tool calls: require their actual parent Step Run, Tool identities, inputs **or** admitted protected references, results **or** errors, **and** distinguishing call evidence.
- a repeated attempt uses the same Tool **and** inputs: preserve distinct attempt identities **without** claiming a second effect **when** its outcome is unknown.
- a Tool call fails **or** its effect cannot be confirmed: retain that outcome rather than recording successful completion.
- a nested trace is rebuilt: require derivation from the canonical Journal **without** another source of execution history.
- a Tool call automatically creates a Workflow Step, ON_RESULT edge, **or** new Action definition: reject that inference.
- secret input is encountered: require its governed protected representation rather than plaintext duplication for trace completeness.

missing evidence **or** an unperformed check is **not** a passing result.
