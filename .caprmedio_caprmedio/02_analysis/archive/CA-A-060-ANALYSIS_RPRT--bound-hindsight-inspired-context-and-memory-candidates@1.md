---
subjects:
  declared:
    continuant:
      - project-context
      - project-memory
      - retrieval-integrity
version: 1
updated_at: 2026-08-25 01:45:35 +0400
---
# Bound Hindsight-inspired context and memory candidates

## Scope and precedence

This Analysis reconciles the Hindsight comparison and the operator's later
candidate-by-candidate dispositions from the current Codex task. The later
operator input takes precedence over the earlier option report. Hindsight is
an inspiration source only; CAPRMEDIO retains its own architecture, wording,
implementation, authority model, and project-integrity constraints.

The source exploration is preserved in
`fpf-reports/20260824T002115Z-fpf-options-explore-caprmedio-vs-hindsight.md`.
This Analysis records project interpretation and disposition; it does not
claim Hindsight implementation details beyond the inspected source boundary
and does not turn an unaccepted candidate into a Plan or Requirement.

## Already captured decisions

- C1, evidence-backed correction candidates, is already governed by
  `CAPRMEDIO-PLAN-009` version 5 and commit
  `5cb4234e5542ff5203f469d1409225d68929bcf6`.
- C2, deterministic non-authoritative standing project briefs, is already
  governed by `CA-P-017` version 6 and commit
  `44698da0e96f15c9484792275fc26cbdd1f3e3d0`.
- The Graph App and Codex Plugin hierarchy, Requirements, Methods, and
  Evaluations already exist. This Analysis does not duplicate them.

## Candidate dispositions

### C3 — bounded hybrid retrieval remains an open Concern

Purpose: improve recall when the exact relevant Atom identities are not known
without weakening deterministic authority selection.

The admissible architecture begins with mandatory deterministic graph and
authority closure. Optional lexical, graph-neighborhood, temporal, or semantic
retrievers may add candidates. A merge stage deduplicates and ranks additions,
then emits a provenance-bound context bundle containing canonical identities,
carrier paths, current digests, selection reasons, and the mandatory closure.
No heuristic may remove, replace, or outrank required authority, widen project
scope implicitly, or become a source of project truth.

Benefits are better discovery and potentially smaller useful context bundles.
Costs are indexing and embedding lifecycle work, freshness checks, ranking
tuning, latency, token use, and a larger leakage surface. No implementation
Plan is admitted until the operator resolves `CA-C-103` with evidence from the
C6 evaluation boundary.

### C4 — independent memory banks are rejected

CAPRMEDIO keeps one canonical project graph. Physical project-local isolation,
derived indexes, caches, and bounded views are permissible only when they are
rebuildable from that graph and cannot establish independent beliefs or
authority. Separate memory banks, scoped truth stores, or cross-project
learning stores would threaten project integrity through divergence, hidden
precedence, and contamination, so they are not admitted.

### C5 — lifecycle wiring belongs to existing owners

The useful purpose is host lifecycle integration: initialize and rehydrate the
session engine, pass selected graph context into governed work, and return Tool
results through the Codex host. It is not a second main skill and does not own
project mutation.

The general architecture is `Codex host adapter -> existing session engine and
main CAPRMEDIO skill -> provider-neutral MCP interface -> canonical Tools`.
Existing authority already assigns session initialization and natural-language
routing to the Framework Methodology and Agentic Skills, and assigns selected
graph-context handoff to `CA-R-1104` and `CA-M-199`. A new C5 Plan would
duplicate those owners and is therefore not admitted.

### C6 — a retrieval-integrity evaluation harness remains an open Concern

Purpose: determine whether any C3 retrieval mechanism improves useful recall
without losing mandatory authority, leaking data, or producing irreproducible
context.

The harness should use versioned project-local fixtures with known mandatory
closures and relevance judgments. A runner executes deterministic-only and
candidate retrieval configurations, then produces non-authoritative evidence
for coverage, leakage, provenance completeness, replayability, latency, token
cost, and authority contamination. Hard gates require complete mandatory
closure and zero cross-project, secret, or authority contamination.

Benefits are an evidence gate, safer tuning, and comparable mechanisms. Costs
are fixture curation, expected-result maintenance, evaluator code, benchmark
runtime, and possible model or embedding expense. The result must remain
Evaluation evidence rather than a new truth store. No implementation Plan is
admitted until the operator resolves `CA-C-104`.

### C7 — autonomous learning memory is not a Core Plan

Purpose, if later justified: learn reusable retrieval or correction signals
from observed work rather than merely rebuild deterministic projections.

The only admissible general architecture separates an authority plane
(`.caprmedio`) from a disposable derived-memory plane
(`.caprmedio_runtime`). Observation ingestion, candidate extraction,
evaluation, and operator-governed promotion may propose changes, but learned
state never mutates authority directly. C1, C2, C3, C5, and C6 remain separate
capabilities with their own owners and evidence boundaries.

Potential benefits are improved recall, adaptation, and reduced repeated
corrections. Costs and risks are the highest of the candidates: persistent
state, migrations, retention and deletion policy, poisoning and privacy
defenses, evaluation infrastructure, replayability, explainability, and
operator-review burden. C7 is therefore rejected as a current Core Plan. It
may be reconsidered only as an optional Core Extension after `CA-C-105` is
resolved with measured need and after C1, C2, and C6 evidence is available.

## Atomization result

- `CA-C-103` owns the unresolved C3 design choice.
- `CA-C-104` owns the unresolved C6 admission and evaluation-contract choice.
- `CA-C-105` owns the evidence threshold for ever reconsidering C7 as an
  optional Extension.
- C4 and C5 remain dispositions in this Analysis because the former is
  rejected and the latter is already owned by existing authority.
- No additional Plan, Requirement, Method, Evaluation, or memory authority is
  created by this Analysis.

## Reopening conditions

Reopen this Analysis if the operator changes the one-canonical-project-graph
boundary, admits a retrieval mechanism, accepts an evaluation harness, assigns
host lifecycle behavior to a new owner, or supplies evidence that justifies an
optional autonomous-memory Extension.
