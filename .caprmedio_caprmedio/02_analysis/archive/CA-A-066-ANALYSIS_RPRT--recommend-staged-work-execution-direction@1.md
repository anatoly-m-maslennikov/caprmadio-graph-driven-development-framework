---
atom_id: CA-A-066
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - work-execution-architecture
      - execution-admission-contract
      - context-policy
    occurrent:
      - work-routing
      - workflow-execution
      - progressive-workflow-migration
version: 1
updated_at: 2026-08-27 02:53:17 +0400
---
# Recommend a staged CAPRMEDIO work-execution direction

## Conclusion

CAPRMEDIO should preserve `(content role, operation)` as the semantic work
classifier, but must not use that pair alone as an executable route or
authorization. Every bounded execution must additionally receive a versioned
Execution Admission Contract that binds the exact target frontier, admitted
context and claims, performer and Method, capabilities, side-effect class,
required checks, gate profile, replay policy, permitted writer, and stop or
return conditions.

The recommended staged direction is:

1. keep broad interpretation, synthesis, reconciliation, RMED authoring,
   planning, and operator-governed authority work in Codex;
2. begin with the strict two-plane boundary represented by `O1`, routing only
   fully contracted deterministic operations into durable workflow control;
3. evolve toward the bounded-agent hybrid represented by `O2` only for
   operation classes whose context, capabilities, evidence, failure behavior,
   and recovery semantics have been demonstrated;
4. add `O6`-style independent evaluation only where authority, consequence,
   or escaped-defect cost justifies its extra latency and cost; and
5. preserve the existing CAPRMEDIO Tool, Journal, and fenced commit gate as the
   governed effect boundary rather than creating a workflow-owned writer.

This is a provisional architecture direction and evidence priority. It does
not select a final architecture or workflow engine, authorize implementation,
or admit any workflow, agent, evaluator, provenance record, or envelope as
RMED authority.

## Option disposition

- `O1` is the recommended initial migration posture because its narrow
  deterministic boundary is easiest to inspect, secure, replay, and reverse.
- `O2` is the recommended evidence-dependent evolution path because it can
  contain locally ambiguous Implementation or Evaluation work without giving
  bounded agents ambient project context or write authority.
- `O6` is a selective assurance overlay for high-risk operations, not a
  universal execution path.
- `O3` should be deferred until the number and variability of proven routes
  justify a central policy compiler. Otherwise the compiler risks becoming an
  unnecessary meta-system or hidden authority surface.
- `O5` should contribute provenance, causal identity, and reconstruction
  principles without initially becoming the central execution backbone. Its
  event-schema, projection, privacy, retention, and rebuild burden is not yet
  justified.
- `O4` should remain conditional until independent Content-role service
  ownership or operating scale justifies its distributed authority,
  credential, contract, and recovery burden.
- `A1` remains the migration overlay, but each `(content role, operation)` cell
  must have exactly one active route edition, one effect owner, an explicit
  cutover frontier, fenced in-flight work, and a tested rollback contract.

These dispositions prioritize experiments and sequencing. They do not remove
any retained option from the comparison frontier or constitute an architecture
Decision.

## Required common-kernel repairs

Before any workflow-engine selection or non-trivial migration, the design must:

1. distinguish Pair Classification from the Execution Admission Contract;
2. make Task and Result Envelopes preserve relied-on claims, interpretation
   scheme, intended use, scope, preserved invariants, permitted loss, and
   rejected inferences rather than only identities and digests;
3. keep provenance, evaluation results, gate decisions, authority, and write
   receipts as separate claims and carriers;
4. define complete required check sets, explicit handling of `notRun`,
   `unknown`, and failure, and bounded `pass`, `degrade`, `block`, or `abstain`
   consequences;
5. bind replay and resume to both semantic and authority frontiers and require
   an explicit `freeze`, `refresh-and-recheck`, `invalidate`, or
   `version-migrate` disposition when either frontier changes;
6. name actual performer Systems, assignments where claimed, enacted Methods,
   dated Work occurrences, capabilities, results, and separate authority and
   responsibility relations;
7. protect every consequence-bearing effect with stable action identity,
   canonical bytes, precondition frontier, fencing, effect receipt, uncertain
   effect reconciliation, and a declared compensation or operator stop;
8. govern memory source admission, authority, currentness, access, retention,
   correction, revocation, deletion, conflict handling, and derived-summary
   invalidation; and
9. define safe behavior for unavailable workflow or evaluation infrastructure
   without silently bypassing required isolation or assurance.

## First evidence campaign

The first campaign should sample at least ten recent CAO, RMED,
Implementation, Evaluation, and Ops runs and classify every material step by
Content role and operation. The first workflow candidates should be frequent,
low-ambiguity operations such as schema, ID, H1, and relation validation;
fixed tests; timestamped observations; receipts; and already governed commits.
Authority reconciliation and new RMED meaning must remain in Codex.

Each selected operation should be run under the same frozen task, target
frontier, admitted context, capabilities, acceptance criteria, and writer
boundary through both the current path and the enveloped candidate path. The
campaign should record wall time, model and infrastructure cost, retries,
operator interventions, defects, escaped defects, context or authority
returns, and recovery behavior without collapsing them into one score.

Failure injection should cover stale target digests, changed prompts or Tools,
changed criteria or authority, suspended-run resume, worker replacement,
duplicate delivery, executor crash before and after an effect, missing
evaluator results, evaluator common-mode failure, workflow unavailability, and
concurrent old/new migration routes.

## Evidence boundary

This Analysis synthesizes:

- `CA-A-065`, which preserves the two-axis routing model, protected integrity
  constraints, plural option frontier, and evidence gaps; and
- `fpf-reports/20260826T212537Z-fpf-design-challenge-caprmedio-work-execution-architecture.md`,
  which records eleven challenged failure surfaces, five strengths, six
  insufficient-basis boundaries, and the minimal repairs or experiments.

The live Tool, MCP, Codex Plugin, Journal, and commit-gate Requirements remain
authoritative for their existing scopes. This Analysis treats their contract,
dry-run, receipt, frontier, fencing, and reconciliation mechanisms as
precedents. It neither widens those owners nor creates a parallel provenance,
gate, memory, or writer ontology.

No matched CAPRMEDIO prototype, runtime benchmark, threat model, memory policy,
evaluator-independence policy, engine/deployment constraint set, or complete
result-class write matrix currently exists. Therefore the evidence supports
the staged direction and next experiments, but not a final architecture or
technology choice.

## Disposition

Retain the staged direction as Analysis. Create no Requirement, Method, Plan,
Evaluation, Delivery, Implementation, workflow-engine selection, or authority
change merely from this recommendation. A later operator action may authorize
the bounded evidence campaign. A final selection must remain a separate
Decision after the common-kernel findings are dispositioned and matched
evidence is available.

## Reopening conditions

Reopen this Analysis if the operator changes the `(content role, operation)`
classifier; changes the one-canonical-project-graph or governed-writer
boundary; supplies matched runtime, security, cost, or failure evidence;
accepts another initial migration posture; selects an engine or deployment
model; or changes the authority of Codex, workflow, Tool, agent, evaluator,
memory, provenance, gate, or writer outputs.
