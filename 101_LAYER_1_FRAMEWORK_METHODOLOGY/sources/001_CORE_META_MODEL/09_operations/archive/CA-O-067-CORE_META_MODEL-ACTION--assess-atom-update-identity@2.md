---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Assess Atom Update Identity"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Summary"
    - "Atom/Claim"
    - "Atom Change Classification"
    - "Artifact/Revision"
    - "Workflow"
    - "Workflow Run"
    - "Operator"
version: 2
updated_at: "2026-09-18 21:51:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1432", "CA-R-1464", "CA-M-303", "CA-R-1520"]}
---
# Assess Atom update identity

Assess Atom Update Identity **means** the reusable read-only Action that compares an existing Atom with its proposed result **and** returns whether the requested update preserves its identity under CA-R-1432 **and** CA-R-1464.

## Inputs

- the exact existing Atom Revision **and** the proposed Claim, properties, **and** Summary.
- applicable change authority **and** relevant evidence for this assessment.

## Outcomes

| Condition | Returned result |
|---|---|
| the applicable change class preserves identity | the admitted change class, target Revision, proposed result, **and** assessment evidence; no presumed authorization **or** persistence |
| replacement is required, including **any** change of Summary value | replacement required, with the target Revision, proposed result, classification reason, **and** assessment evidence |
| evidence **or** classification is uncertain | unresolved, with the missing evidence **or** required Operator decision; no presumed update **or** replacement approval |

the result describes **only** the supplied proposal against the identified target Revision. it does **not** remain sufficient **when** that proposal, Revision, **or** relevant evidence changes.

this Action **must not** select a continuation Workflow, end its caller's Run, schedule another Run, authorize a mutation, **or** persist **any** change. the calling Workflow declares its routing under CA-M-303 **and** supplies its own performed-effect account **when** preparing a handoff under CA-R-1520.
