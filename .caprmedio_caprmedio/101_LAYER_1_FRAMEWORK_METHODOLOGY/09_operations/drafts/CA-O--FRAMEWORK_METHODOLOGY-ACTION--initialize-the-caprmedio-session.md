---
content_role: Operations
type: Action
current_scope_unit: FRAMEWORK_METHODOLOGY
claim_target_scope_unit: FRAMEWORK_METHODOLOGY
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: definition
subjects:
  governs: "CAPRMEDIO Session Initialization"
  depends_on:
    - "Action"
    - "CAPRMEDIO Main Skill"
    - "Operator"
    - "Project"
    - "Scope Unit"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Project Structure"
    - "CAPRMEDIO Routing Tree"
    - "Session-State Envelope"
    - "Exploration Mode"
    - "AI Agent Delegation"
    - "Atom"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Methodology"
    - "Atom/Content Role: Implementation"
version: 4
updated_at: "2026-09-23 17:20:35 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1530", "CA-R-1565", "CA-M-314", "CA-R-1552", "CA-R-1558", "CA-R-852", "CA-O-052", "CAPRMEDIO-GOV-REQU-371", "CAPRMEDIO-METHODOLOGY-REQU-507", "CAPRMEDIO-METHODOLOGY-REQU-509", "CA-E-483"]}
---
# Summary

Initialize the CAPRMEDIO session

## Claim

CAPRMEDIO Session Initialization **means** the Action that prepares the bounded context needed for a session using the CAPRMEDIO Main Skill, at session start **or** **after** context compaction, **without** treating restored context as new authority **to** execute work.

### Inputs and preconditions

- the session entry **or** compaction event, the current Operator request, **and** available Project identity evidence.
- the registered Project Settings, effective Framework Instance Settings, Project Structure, canonical CAPRMEDIO Routing Tree, **and** **any** existing bounded Session-State Envelope.
- references **to** current active authority **and** existing authorization; missing inputs remain explicit rather than being inferred from another Project.

### Behavior

1. identify the owning Project **and** current Scope Unit. reuse CA-O-052 for initialization inputs **before** interpreting Project Structure; resolve declared ownership from Project Structure rather than inventing it from folder names.
2. prepare a new session's bounded context from the resolved sources, **or** restore existing context **after** compaction **and** check its freshness. include **only** the context admitted by CAPRMEDIO-GOV-REQU-371 **and** CAPRMEDIO-METHODOLOGY-REQU-509. retain references for on-demand authority loading, **not** another authoritative copy of the Methodology **or** session history.
3. check the registered CAPRMEDIO Routing Tree under its existing validation authority CA-E-483. an absent, invalid, **or** stale required input blocks affected routing; do **not** silently substitute a cached tree **or** fabricate a successful check.
4. classify the current request using CA-R-1558. preserve Exploration Mode for exploratory input; retain an explicit executable request as a pending request subject **to** current authorization **and** applicable checks. revalidate restored delegation under CA-R-852 **and** CA-R-1552 **before** relying on it.
5. return the prepared context **and** references **to** the calling session. restoration does **not** itself replay an effect, resume unfinished work, persist a Plan, **or** authorize an additional change.

### Results and effects

- ready: the identified Project **and** Scope Unit, effective settings references, checked routing reference, compact context, request classification, **and** **any** pending request.
- blocked: missing, stale, conflicting, **or** invalid inputs with the evidence **and** decision needed **to** resolve them.
- failed: the failed initialization operation **and** recoverable partial session state; do **not** report the session ready.

the Action changes **only** the admitted session context. it does **not** modify governing Atoms, Settings, Project Structure, **or** Implementation. host hooks, provider integration, **and** storage mechanics remain outside this Action definition.
