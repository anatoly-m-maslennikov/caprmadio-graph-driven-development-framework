---
subjects:
  governs: "Workflow"
  depends_on:
    - "Author"
    - "Action"
    - "Step"
    - "Workflow Run"
    - "Atom"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Assess Atom Update Identity"
version: 2
updated_at: "2026-09-18 21:51:53 +0000"
relations: {"relates_to": ["CA-M-301", "CA-O-067", "CA-R-1432", "CA-R-1464", "CA-R-1520"]}
---
# Declare update routing in the calling Workflow

**to** author an Atom update Workflow, declare its response **to** identity assessment **in** the Workflow graph rather than **in** the assessment Action **or** executor code.

- reference CA-O-067 for the assessment; bind the target Revision, proposed result, applicable authority, **and** evidence **to** that Step. the Action returns its assessment **without** selecting the caller's next Step **or** continuation Workflow.
- map identity-preserving results **to** the caller's declared update path **and** remaining authorization **and** checks; the assessment alone does **not** perform the update.
- map replacement-required results **to** a terminal handoff under CA-R-1520. keep the admitted replacement-continuation binding **in** the Workflow definition, **not** as an assessment Action input. the ending Run does **not** call **or** wait for replacement **or** persist an intermediate update merely **to** replace it.
- map unresolved results **to** the caller's declared evidence-gathering **or** escalation path; an unresolved result **must not** be treated as approval.
- include reassessment **when** the proposal changes **or** its evidence becomes stale **before** persistence. a changed Summary remains a replacement under CA-R-1464 even **when** the request began as an update.

this Method constrains how an Author expresses the caller's graph. it is **not** another Workflow, executable routing service, **or** requirement **to** build the executor through a particular Workflow.
