---
subject_scopes:
  - development-flow
version: 7
updated_at: 2026-08-19 08:08:20
---
# Options discovery — Draft RMED as the product backlog

## Clarified candidate model

The Product Backlog is the complete set of current draft Requirement, Method, Evaluation, and Delivery Atoms. A draft RMED Atom describes possible future product truth whether or not work on it has been scheduled.

The Queue is the subset of draft RMED connected to an active Plan that will finalize and implement it. Plan priority orders queued work; RMED tier continues to describe specification authority rather than scheduling order.

A Concern may explain why draft RMED exists. Concern is not limited to a gap or problem: it may be a risk, opportunity, question, conflict, or any other matter needing attention.

Reasoning may remain in the operator's mind, exist ephemerally in an LLM session, happen in an unrecorded discussion, or be preserved in an Analysis Atom. In the fourth form, the reasoning remains connected to the graph. The `A?` in the candidate flow records that a governed Analysis Atom may or may not be present.

Sufficiently clear operator input may also create draft RMED directly without first creating Concern or Analysis.

## Informal descriptive and prescriptive lens

The Content roles also admit a useful informal grouping. It is an explanatory view, not a formal axis or another stored classification field.

| Group | Mode | Meaning |
|---|---|---|
| CAO | Descriptive | Concern describes a matter needing attention, Analysis preserves reasoning when recorded, and Ops describes observed results |
| RMED | Prescriptive | Requirement, Method, Evaluation, and Delivery describe what the system should provide and how it should be built, checked, and delivered |
| P | Prescriptive and operational | Plan states accepted actions and coordinates their execution |
| I | Realized | Implementation is the code and other system parts that actually exist |

Plan is the bridge: it does not establish durable system truth like RMED, but it prescribes and coordinates operational change. In the candidate backlog model, draft RMED holds a possible future prescription, Plan selects it into the Queue, Implementation realizes it, and Ops describes the result.

## Candidate flow

```text
C → A? → draft RMED
              ├─ without an active P → Product Backlog
              └─ with an active P    → Queue → active RMED → I → O
```

The same draft RMED remains part of the Product Backlog while queued; Queue is a selected view over the backlog, not a second copy. CAP may also describe operational work that changes no RMED.

## Effect on the current model

Current authority classifies the Development Backlog as a Plan of accepted intended action points and creates RMED during Plan execution. The candidate model instead creates draft RMED first and derives the Product Backlog and Queue from those Atoms and their Plan relations.

Adopting the candidate would therefore require explicit replacement of the current Development Backlog authority. This Analysis does not make that change.

## Remaining options and questions

1. Whether the current Development Backlog remains as a separate list for operational CAP work or is replaced entirely by Plans and generated views.
2. Which precise relation means that a Plan selects draft RMED for finalization and Implementation.
3. When queued RMED leaves the Product Backlog and Queue: on specification activation, Implementation completion, Delivery, or confirmed Ops results.
4. How one Plan selects several RMED drafts without merging their independently replaceable claims or copying priority onto them.
5. How Product Backlog and Queue Projections group related RMED lineage while preserving each Atom.
6. How Concern priority and Plan priority appear in those views without automatic inheritance.

The clarified model remains an option until accepted through RMED authority.
