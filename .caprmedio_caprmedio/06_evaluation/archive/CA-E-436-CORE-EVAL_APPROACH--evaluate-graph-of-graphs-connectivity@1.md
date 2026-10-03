---
atom_id: "CA-E-436"
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    occurrent:
      - "Project/Graph of Graphs/connectivity"
  depends_on:
    continuant:
      - "Project"
      - "Graph of Graphs"
      - "Artifact"
      - "Atom/Content Role: Implementation"
      - "Scope Unit"
      - "CAPRMEDIO Framework Instance"
version: 1
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-R-1407"
    - "CAPRMEDIO-REQU-007--full-minimal-traceability"
---
# Evaluate graph-of-graphs connectivity

the Graph of Graphs connectivity Evaluation **must** return `fail` **if** a governed Artifact **or** delivered Implementation element has no recoverable location **or** no valid connection **to** the shared connected whole; a connection **may** cross graph boundaries, **and** specialized Methodology, Engine, **or** other Scope Unit checks **may** supply evidence **to** this Evaluation. apply cycle restrictions **only** **to** graph families whose authority requires them; connectivity **must not** impose universal acyclicity.
