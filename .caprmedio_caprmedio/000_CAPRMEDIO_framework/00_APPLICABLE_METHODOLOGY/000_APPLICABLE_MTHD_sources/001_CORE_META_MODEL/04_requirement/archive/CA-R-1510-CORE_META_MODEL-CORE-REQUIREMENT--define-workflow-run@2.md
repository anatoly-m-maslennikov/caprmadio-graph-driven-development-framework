---
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Journal/Record"
version: 2
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
---
# Define Workflow Run

a Workflow Run **means** **`=1`** actual execution of **`=1`** Workflow against the inputs **and** parameters supplied for that run.

- the execution follows the Workflow's typed Relations **and** retains its actual Step Runs, outcomes, **and** applicable retry allowance.
- the run is distinct from the reusable Workflow **and** from the Journal Records that describe its execution. a reference **to** the definition does **not** prove that a run occurred.
