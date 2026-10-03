---
version: 13
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - "CA-M-001"
    - "CA-M-002"
    - "CA-E-001"
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs: "Project/Principle and Core alignment"
  depends_on:
    - "Project"
    - "Atom/Local Tier"
    - "Atom/Content Role"
    - "Operator"
    - "Atom/Claim"
    - "Atom/Local Tier: Principle"
    - "Atom/Local Tier: Core"
    - "Atom/Content Role: Evaluation"
    - "Atom"
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate the current Principle and Core set

the Principle **and** Core set Evaluation **must** return `fail` **if** a known Project-wide invariant has no canonical owner, a Principle is **only** a narrow application rather than a broad commitment, a required supporting Core Claim is absent, Claims conflict **or** independently duplicate authority **in** the same context, **or** an Atom has an incompatible Local Tier **or** Content Role; **otherwise**, it **may** return `pass` for the reviewed frontier **without** claiming that undiscovered gaps are impossible. apply the accepted Actor **and** authority interpretation of Plan Principles. faithful Core specialization **must not** count as duplicate authority; fixed child counts, a universal RMED checklist per Principle, expansion from Intent, **and** formula/text equivalence **must not** be acceptance conditions. report missing support **and** conflicting owners **to** the Operator **without** silently selecting a winner.
