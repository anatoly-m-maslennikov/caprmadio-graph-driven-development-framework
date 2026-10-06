---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Projection/Type: Terms Graph"
  depends_on:
    - "Term"
    - "Root Term"
    - "NARROWER_THAN"
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Governed Term"
    - "Definition Atom"
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Entity"
    - "Action"
    - "Workflow"
    - "Projection"
version: 16
updated_at: "2026-09-18 14:16:20 +0000"
relations:
  evaluation_for:
    - CA-R-1335
    - CA-R-1246
    - CA-R-1435
    - CA-R-1244
    - CA-R-1345
    - CA-R-1347
    - CA-R-1319
    - CA-R-1454
    - CA-R-1437
    - CA-R-1472
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Terms Graph

## Graph validity

the Evaluation **must** reject a Terms Graph **if** **any** of:

- a native node is **not** a Term under its governing authority.
- a native Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246, **or** an external reference violates its registered endpoint classes **or** graph contexts.
- a NARROWER_THAN Relation lacks an explicit authoritative source declaration **or** its governing Term definitions do **not** establish the implication under CA-R-1435. absence of Entity instances does **not** establish this implication.
- the NARROWER_THAN hierarchy **contains** a directed cycle, including a self-loop.
- a Root Term classification differs from the **`=0`** direct NARROWER_THAN-parent criterion under CA-R-1347.

the Evaluation **must** accept an acyclic hierarchy with multiple direct parents **or** an isolated Root Term **when** the remaining applicable authority is satisfied. Relations from another graph kind **must not** change Root Term classification **when** the Terms Graph hierarchy is unchanged. the checks **must** distinguish an unregistered Relation Kind from a separately admitted graph-specific expansion.

for a governed-only view under CA-R-1454, the Evaluation **must** reject graph validity **if** a displayed native Term node lacks **`=1`** active defining authority under CA-R-1319. missing **or** conflicting definitions **and** uncertain Relation admission **must** be reported with their affected source references **without** inventing a definition **or** an edge.

filtering out a parent **must not** establish **or** change canonical Root Term classification. **if** the available source evidence is insufficient **to** establish the CA-R-1347 criterion, the classification **must** remain unresolved **without** silently importing source nodes **or** edges from outside the requested selection.

the same NARROWER_THAN implication check applies **when** the Terms name Actions **or** Workflows; the Evaluation **must not** require **or** create Entity duplicates **to** admit operational vocabulary. an empty set of observed instances does **not** prove a hierarchy Relation; acceptance requires the governing Term definitions **and** explicit Relation authority.

## Projection fidelity and source traceability

an admitted source-Atom **or** cross-graph reference under CA-R-1472 **must not** fail **only** because its external endpoint is **not** a Term; that endpoint is **not** a native Terms Graph node. reject a view that imports that endpoint as a Term, erases its graph context, uses an unregistered Relation Kind, **or** lets the external reference alter NARROWER_THAN hierarchy **or** Root Term classification.

for a governed-only view under CA-R-1454, the Evaluation **must** reject the view **if** an eligible Term **or** Relation required by CA-R-1454 is omitted, an ineligible node **or** edge is displayed, a displayed native Term node's Definition Atom **or** a displayed internal edge's source declaration is outside the requested source selection, a displayed native Term node **or** internal edge lacks exact source Claim **and** Artifact Revision traceability, **or** an internal Term Relation edge is inferred **only** from spelling, capitalization, shared Subject use, **or** compatible endpoints.

the Evaluation **must** reject a graph **or** governed-only view **if** its rendered content is treated as independent vocabulary authority, an upstream Projection substitutes for exact defining **or** Relation-source authority, a Projection chain loses its upstream identity **or** ultimate source traceability, **or** an arbitrary filter is treated as another admitted Projection Type. a source-faithful view derived through an upstream Terms Graph Projection **must** pass these Projection-specific checks **when** the applicable fidelity, selection **and** source-traceability requirements are satisfied; graph validity is assessed separately.

## Result boundary

the Evaluation **must** distinguish Projection fidelity from graph validity **and** keep the two outcomes visible, including **any** unresolved source conditions **and** checked-coverage limits. a graph that faithfully represents a source conflict **may** pass fidelity while failing an applicable graph-validity condition **or** leaving that condition unresolved. a composite acceptance result **must not** pass **if** an applicable check fails **or** remains unresolved; faithful reproduction alone does **not** establish a valid source model.

connectivity **and** cycle checks apply **only** as required by the governing graph authority; the NARROWER_THAN cycle prohibition **and** the admitted isolated Root Term cases above remain distinct. passing graph-structure checks does **not** establish Project-specific meaning **or** consistency of source use **without** the required governing definitions **and** source context.
