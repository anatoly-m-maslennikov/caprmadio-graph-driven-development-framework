---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Assess Atom Update Identity"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Summary"
    - "Atom Change Classification"
    - "Artifact/Revision"
    - "Workflow"
    - "Workflow Run"
    - "Operator"
version: 1
updated_at: "2026-09-18 21:23:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1432", "CA-R-1464", "CA-R-1520", "CA-O-051"]}
---
# Assess Atom update identity

Assess Atom Update Identity **means** the reusable read-only Action that compares an existing Atom with its proposed result **and** returns whether the requested update preserves its identity under CA-R-1432 **and** CA-R-1464.

## Inputs

- the exact existing Atom Revision **and** the proposed Claim, properties, **and** Summary.
- applicable change authority, relevant completed checks, **and** effects already performed by the calling Run, **if** **any**.
- the calling Workflow's admitted replacement-continuation binding, **when** a replacement route is available.

## Outcomes

| Condition | Returned result |
|---|---|
| the applicable change class preserves identity | the admitted class **and** proposed update, subject **to** the remaining authorization **and** checks |
| replacement is required, including **any** change of Summary value | replacement required, with the target Revision, complete proposed result, classification reason, checks, **and** effect account needed under CA-R-1520 |
| evidence **or** classification is uncertain | unresolved, with the missing evidence **or** required Operator decision; no presumed update **or** replacement approval |

an update Workflow **must** use the replacement-required result as a terminal handoff under CA-R-1520. the executor resolves the replacement Workflow from the admitted continuation binding; a missing binding blocks dispatch rather than permitting an invented route. this Action **must not** invoke replacement **or** persist an intermediate updated Revision merely **to** replace it.

the assessment **must** be repeated **when** the proposed result changes **or** its evidence becomes stale. it does **not** authorize replacement; accepted replacement persistence reuses CA-O-051.
