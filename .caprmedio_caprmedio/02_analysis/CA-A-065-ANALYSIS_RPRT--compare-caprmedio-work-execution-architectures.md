---
atom_id: CA-A-065
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - work-execution-architecture
      - context-policy
      - project-memory
    occurrent:
      - work-routing
      - workflow-execution
version: 1
updated_at: 2026-08-27 01:18:06 +0400
---
# Compare CAPRMEDIO work-execution architectures

## Conclusion

CAPRMEDIO should classify work by the pair `(content role, operation)`, not by
Content role, lifecycle phase, or tool kind alone. Content role determines the
meaning, authority, and evidence posture of the subject. Operation determines
how much context and judgment the work needs and whether its control path can
be bounded, isolated, recovered, and replayed.

The current evidence supports a plural architecture frontier rather than one
selected design. Codex remains the natural place for project-wide discovery,
interpretation, synthesis, reconciliation, planning, and operator-governed
authority work. A durable workflow is appropriate for contracted operations
with enumerated inputs, fixed or bounded next steps, least-privilege grants,
recoverable state, and governed effects. A workflow may invoke a bounded agent
activity without making that activity deterministic. Its exact inputs,
configuration, grants, result, and evidence still remain bounded and recorded.

This Analysis does not select a workflow engine or final architecture, create
new RMED authority, authorize workflow writes, or claim runtime proof.

## Source and evidence boundary

The detailed option generation and desk-evidence comparison are preserved in
`fpf-reports/20260826T205431Z-fpf-options-explore-caprmedio-work-execution-architecture.md`.
The predecessor harvest is preserved in
`.caprmedio/fpf-reports/20260826T202459Z-fpf-sota-harvest-broad-context-agent-narrow-workflow.md`.

The harvest includes seventeen sources across long-horizon agent harnesses,
durable workflow orchestration, hybrid agent runtimes, prompt and evaluation
lifecycle, least-privilege security, and provenance and observability. The
comparison is architectural desk evidence only. It contains no matched
CAPRMEDIO prototype, measured cost or latency, failure-rate baseline, or
selected engine evidence.

The latest operator correction supersedes the initial phase-labelled split:
the routing unit is `(content role, operation)`. This Analysis preserves that
semantic frontier.

## Two-axis routing interpretation

The same Content role may require both broad and bounded operations:

- CAO discovery, interpretation, and coordination need broad project context;
  mechanical carrier validation and evidence registration may be bounded.
- RMED authoring and authority reconciliation need broad context and governed
  operator judgment; schema, identity, H1, and relation checks may be
  deterministic.
- Implementation design or resolution of an ambiguous change may use broad
  Codex work or a bounded agent activity; applying a complete transformation
  contract may be a workflow activity.
- Evaluation criteria design and conflicting-evidence interpretation need
  broad judgment; fixed tests and versioned graders should run in isolated,
  bounded contexts.
- Ops consequence interpretation and corrective direction need broad context;
  timestamped measurements, receipts, and declared observations may be
  bounded.

The valid memory boundary is not “no memory.” Durable execution requires
explicit run-local state, event history, checkpoints, or recorded activity
results. Bounded work should instead have no ambient cross-run semantic memory.
Broad session history, authoritative project artifacts, workflow replay
history, derived summaries, and user preferences remain distinct sources with
explicit admission and provenance.

## Protected project-integrity constraints

Every admissible architecture must:

1. route by `(content role, operation)`;
2. prevent evidence, Implementation, Evaluation, or Ops results from silently
   becoming RMED authority;
3. keep broad semantic session history distinct from workflow replay history;
4. admit exact inputs, versions, context, and least-privilege capabilities to
   bounded work;
5. correlate tasks, activities, agents, artifacts, evaluations, and writes
   through stable campaign, run, trace, and digest identities;
6. make effects idempotent, previewable, or mediated by an already governed
   writer; and
7. stop for the operator when context, authority, or acceptance criteria are
   missing.

These constraints are eligibility conditions. Cost, latency, convenience, or
implementation simplicity cannot compensate for violating them.

## Compared architecture families

### O1 — Hard-contract two-plane split

Codex performs every adaptive or authority-bearing operation. The workflow
accepts only fully contracted deterministic operations and never invokes an
agent. This has the clearest replay and security boundary and a moderate
implementation burden, but locally ambiguous work must return to Codex.

### O2 — Durable hybrid with bounded agent activities

Codex owns broad authoring and governance. A durable workflow owns recovery,
retry, approval, and causal identity and may invoke deterministic Tools,
sandboxes, or bounded coding and evaluation agents. This has the strongest
direct cross-tradition evidence and broad semantic coverage, but requires
substantial workflow, sandbox, versioning, and observability infrastructure.

### O3 — Policy-compiled execution kernel

A central policy compiler takes Content role, operation, target frontier, risk,
authority, success criteria, and side-effect class and emits an execution
contract. It may route to Codex, a Tool, a workflow, a bounded agent, an
evaluator, or a human gate. This is the most flexible and reversible option,
but the policy language, compiler, conformance suite, and adapters become
critical infrastructure and may create an unnecessary meta-system.

### O4 — Content-role-owned execution mesh

CAO, RMED, Implementation, Evaluation, and Ops each receive a stewarded service
or adapter with role-specific context and evidence policy. This maximizes
role-local specialization, but distributes policy, credentials, state, and
operations. It remains admissible only if one authority registry and one RMED
admission boundary prevent service-local truth or policy drift.

### O5 — Provenance-log-centred execution backbone

An immutable campaign log and content-addressed artifact store coordinate
Codex sessions, workflows, Tools, agents, evaluators, and governed writers.
Typed views keep semantic session events separate from workflow replay events.
This offers the strongest reconstruction and executor replaceability, but has
the highest event-schema, retention, privacy, projection, and storage burden.

### O6 — Dual-control assurance pipeline

A generator produces a candidate; a separately scoped evaluator receives the
artifact, declared criteria, and controlled environment without the generator's
scratch context; a policy gate checks the evidence before a governed writer may
act. Deterministic checks may fill the evaluator role. This gives the strongest
separation of duties for high-risk work but adds systematic cost and latency.

### A1 — Progressive pair-cell migration

Progressive migration is an adoption policy, not a competing steady-state
architecture. Existing deterministic validation, testing, receipts, and
governed commits should be enveloped first. Other `(content role, operation)`
cells move only after their context contract, authority boundary, and failure
behavior are proven. A1 can be used with any retained architecture.

## Comparative result

No candidate dominates semantic adequacy, project integrity, determinism,
recovery, security, provenance, cost, latency, implementation burden, and
reversibility at once.

- O1 is strongest in boundary clarity but weakest for bounded nondeterministic
  work.
- O2 is the most directly supported general composition but carries high
  infrastructure and policy cost.
- O3 is the most flexible router but depends on a new central policy system.
- O4 is strongest in role-local stewardship but weakest in operating burden
  and cross-role policy coherence.
- O5 is strongest in reconstruction and provenance but requires the heaviest
  data-governance substrate.
- O6 is strongest for independent assurance but is not justified as a
  universal path for low-risk operations.

The retained steady-state option frontier is O1, O2, O3, O5, and O6. O4 remains
conditional on future scale or independent role ownership. A1 remains a
compatible adoption overlay. This is an option frontier, not a ranking or
architecture decision.

## Common architecture kernel

The comparison identifies a shared minimum without selecting a candidate:

- a pair-based work classifier;
- an immutable Task Envelope and Result Envelope;
- separate semantic-session and workflow-replay histories;
- explicit workflow run state;
- versioned prompts, models, harnesses, Tools, environments, and graders;
- least-privilege resource and operation grants;
- content and configuration digests;
- campaign, run, trace, activity, artifact, and receipt identities;
- independent evaluation when selected by risk and authority policy; and
- a separately governed CAPRMEDIO persistence boundary.

The envelopes isolate work without discarding reconstructibility. They are not
new authority and must map to existing CAPRMEDIO Tool, Journal, Plan/work,
Evaluation, Ops, and commit-receipt contracts wherever those owners already
apply.

## Excluded architectures

- One broad Codex session without explicit contracts, least privilege,
  recovery, provenance, and governed persistence is not an admissible target.
- A deterministic workflow cannot own all project-wide interpretation,
  authority reconciliation, or evaluation design.
- A durable workflow cannot operate without explicit run state; only ambient
  cross-run semantic memory is prohibited.
- Workflow, agent, or evaluator output cannot directly become RMED.
- A weighted scalar score cannot select an architecture without admissible
  weights and matched measurements.
- A workflow product cannot be selected before language, deployment,
  persistence, concurrency, human approval, privacy, licensing, cost, and
  in-flight version requirements are declared.

## Ownership reconciliation

`CAPRMEDIO-META-ANRP-010` retains the analysis of persistent agent memory,
shared graph knowledge, and review before authority adoption. `CA-A-060`
retains the Hindsight-inspired retrieval and memory candidate dispositions,
including one canonical project graph and disposable derived state. Current
Tool, MCP, Codex Plugin, commit automation, Journal, and governed-write Atoms
retain their existing scopes. This Analysis neither duplicates nor widens
those owners.

The unresolved work-execution questions remain evidence gaps in this Analysis.
They are not automatically new Concerns, Plans, Requirements, Methods,
Evaluations, Deliveries, or Implementation commitments.

## Evidence gaps

The following questions remain below the operator's 95% decision threshold:

- the complete routing matrix for representative Content-role and operation
  pairs;
- the workflow engine and local or cloud deployment model;
- the boundary between mechanical, bounded-semantic, and project-semantic
  validation;
- the required replay level for nondeterministic model activities;
- retention, correction, privacy, and access rules for memory and provenance;
- the measured cost and latency break-even for isolation and independent
  evaluation;
- the mapping from envelopes and trace identity to existing CAPRMEDIO carriers;
  and
- the exact governed-write authority for each result class.

## Disposition

Save the two-axis routing model, protected constraints, option frontier,
adoption overlay, common kernel, exclusions, and evidence gaps as Analysis.
Create no further Atom or implementation merely from this comparison. A later
operator decision may select an architecture through a separate decision
synthesis after priorities and sufficient parity evidence are supplied.

## Reopening conditions

Reopen this Analysis if the operator changes the `(content role, operation)`
routing rule, admits one of O1 through O6, selects a workflow engine, changes
the one-canonical-project-graph or governed-write boundary, supplies matched
runtime measurements, or changes the authority of workflow, agent, evaluator,
or memory outputs.
