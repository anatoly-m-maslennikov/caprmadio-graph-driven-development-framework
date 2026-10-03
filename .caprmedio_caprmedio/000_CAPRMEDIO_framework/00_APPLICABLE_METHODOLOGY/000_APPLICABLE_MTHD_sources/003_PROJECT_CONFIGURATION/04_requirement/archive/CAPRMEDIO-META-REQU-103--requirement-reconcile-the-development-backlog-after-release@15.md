---
subjects:
  governs: "development-flow"
  depends_on: []
version: 15
updated_at: "2026-09-17 13:16:29 +0000"
relations: {"child_of":["CA-O-058","CAPRMEDIO-META-REQU-114-CORE_META_MODEL-CORE-REQUIREMENT--preserve-content-role-boundaries-through-caprmedio-loop"]}
---
# Requirement — Reconcile the Development Backlog after release

**after** the Release Record is accepted, CAPRMEDIO reconciles the Development Backlog against its exact released manifest.

Candidates whose promoted Atoms were fully delivered **in** that release are removed from the Development Backlog. Unfinished, partially delivered, excluded, **or** newly deferred candidates remain unscheduled **or** move **to** another target version. a candidate cannot be removed as shipped **unless** the released manifest accounts for its promoted Atoms.

Reconciliation appends Journal records **and** regenerates the Projection. Release Records, Plans under `done/`, **and** Git history preserve what shipped, what was executed, **and** how the planning allocation changed.

## Primary claim

Release reconciliation removes fully shipped candidates from the Development Backlog **and** retains **or** reschedules **every** candidate **not** fully accounted for by the released manifest.
