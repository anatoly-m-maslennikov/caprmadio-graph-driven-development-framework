# Selected workflow Docker acceptance portfolio

Prepared by CA-P-1492 on 2026-10-04. This is an acceptance specification, not
runtime evidence. It is bound to CA-P-1117 v3, CA-P-1123 v2, accepted
CA-A-1142 v2, and P1443/P1451 J01--J08. No selected route has a pass from this
document.

## Runtime boundary and evidence state

The usable runtime is `caprmedio-runtime:local`, inspected locally as image ID
and manifest digest `sha256:0c5187b772c0b7f975de30a385b05fa8684658eb4712f9e0fa4c66add931afff`
(created `2026-10-04T01:47:40Z`). At inspection, only
`caprmedio-ea535e2c0d4e-worker-1` and `caprmedio-ea535e2c0d4e-agent-1` for this
image were healthy. This is availability, not a selected-route pass.

`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/`
supplies a non-root, immutable-code runtime: worker and stdio MCP mount one
Project at `/project`; the Agent has no Project mount; routing is Docker-only
after explicit start. The existing `test_docker_e2e.py` creates a disposable
mock Project, talks through `workflow_orchestrator` over stdio MCP, and asserts
MCP-disconnect completion/restart persistence plus uncertain-dispatch no-replay.
It exercises CA-O-104 / Base Revise only. It must not be represented as coverage
for W01--W13.

## Common fixture, harness, and oracle

Create a fresh disposable Git Project per case, with a frozen minimal authority
fixture, registered Operator, `project_structure.toml` where applicable, and a
canonical Work Journal. Seed only case-specific Atom/source inputs and record
SHA-256 snapshots of the admitted sources, selection, criteria and expected
authoritative files. Use mock Agent golden cases before any real-Agent case.

Existing runnable controls (do not use a real Project or an old native Run):

```sh
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py build
CAPRMEDIO_DOCKER_E2E=1 uv run --group workflow-orchestrator --group rmed-workflow-mcp python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p test_docker_e2e.py -v
```

The first command proves only image construction. The second is the available
disposable Docker/MCP harness and must remain a separate Base Revise regression.
The selected-route implementation must add its own fixture parameter/route
adapter before this invocation can become selected-route evidence. Its required
command form is deliberately exact and test-first:

```sh
CAPRMEDIO_DOCKER_E2E=1 uv run --group workflow-orchestrator --group rmed-workflow-mcp python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p 'test_selected_workflows_docker_e2e.py' -v
```

For every case, explicitly start a mock runtime through its lifecycle command,
call MCP tool `workflow_orchestrator` with a fresh case Run ID, then read status
after client disconnect/reconnect. Preserve result/report paths and Journal
receipt paths before scoped fixture cleanup. A real Docker/MCP replay is allowed
only after its matching mock golden case passes and uses the same frozen corpus;
it requires an explicit fresh Run ID, supplied runtime credential, and no native
queue migration. Never start services merely to satisfy this specification.

Pass requires all of the following: exact expected authoritative effects (or
unchanged hashes for no-effect paths); exactly the specified current source
revisions; a Workflow Run and each actually invoked Action Run reconstructable
from the Journal; actual parent/Step lineage where present; start plus truthful
terminal/pending facts; safe input/result/effect references; and one canonical
durable receipt per event. Image build, service health, an MCP acknowledgement,
or a host-only test is insufficient.

## Route matrix

`J` means J01--J08 applies to every row. “Action” names the A1142-bound Action;
an implementation may add no fictitious Action Run when the source action did
not execute.

| Case | A1142 source and required Action | Mock golden case / expected result | Required non-happy assertion |
| --- | --- | --- | --- |
| W01 Create Atom | O127v2 → O129v2 → O128v2; native O032v5/R865v14/E303v14 | Admit one sealed new Atom; complete contents/identity and one lifecycle Action effect. | Reject invalid or duplicate identity before effects; Journal failure after an effect follows recovery portfolio. |
| W02 Update Atom | O127v2 → O145v2/O067v6 → O129v2 → O128v2; O030v5/R866v12/E304v11 | Change only authorized non-Summary fields, preserving role-specific Version/time/history. | Summary change returns a Replace handoff with no same-ID mutation; already-conforming input is a successful no-op. |
| W03 Replace Atom | O127v2 → O129v2 → O128v2; O051v6; O031v4/R1041v7/E299v9/E247v12 | Publish every supplied active successor then archive exactly one predecessor with history. | Incomplete successor set or archival failure leaves truthful partial/deferred facts, never an all-success claim. |
| W04 Change Status / Archive | O127v2 → O129v2 → O128v2; R1521v4; Archive O029v4/R868v12/E306v11 | Resolve the target role’s status model; Archive is the shortcut path. | Invalid transition/no-op does not mutate Version/history/references; post-effect failure is distinguished from preflight rejection. |
| W05 Create Scope Unit | O015v8 → O139--144v2 → O004v5/O012v5/O005v8/O013v5/O014v5 | Add declared Structure entry under admitted parent and update exactly admitted references. | Unauthorised parent/Goal/reference frontier rejects without carrier creation. |
| W06 Rename Scope Unit | Same O015/O139--144 bindings | Rename declared identity/name and the admitted dependent Goal/reference set. | A filesystem-only rename is rejected as no structural authority; recovery reports any partial reference work. |
| W07 Move Scope Unit | Same O015/O139--144 bindings | Reparent declared unit/path and preserve/rewrite exact affected references. | Forbidden destination/currentness conflict produces zero effect or truthful partial state, never inferred recovery. |
| W08 Remove Scope Unit | Same O015/O139--144 bindings | Remove only approved declaration with required dependent/history treatment. | Existing carrier deletion is not inferred; blocked dependents retain source and failure evidence. |
| W09 Implementation | O016v11 → O091--096/O099 and O017v6/O018v6/O019v4/O020v5/O089v3/O024v11/O021v9 | Golden tests first, then one frozen required behavior implementation and its selected checks. | Failed check/low confidence/undelegated repair interrupts with retained evidence; no unperformed-check success or automatic retry. |
| W10 Revert Changes | O130v1 → O132v1 → O131v2 | Apply only an approved reversal and retain history/references. | Reversal denial has zero effects; uncertain/partial reversal is terminally truthful and is not internal rollback. |
| W11 Entities Graph | O133v2 → O135v1 → O134v2 | Build source-traceable projection from selected Entity/Property/Relation and declared Structure inputs. | Incomplete/stale/invalid source yields failed/incomplete projection, not source repair or a complete output. |
| W12 Terms Graph | O136v2 → O138v1 → O137v2 | Build source-traceable graph from selected Terms and their Relations. | No-source-change/no-op and invalid/incomplete source remain non-authoritative; do not silently correct Terms. |
| W13 Applicable Methodology | O011v12 → O152--157v2 with O004--009; O010v9 supporting only | Compile selected Core Meta-Model, extensions and configuration into a derived Projection. | Installed-extension conflict/rejection or missing approval emits no source correction and reports incomplete/blocked projection. |

Each row receives: (1) one mock happy case; (2) its listed non-happy case;
(3) no-op where meaningful; and (4) the shared fault/cancel/partial portfolios
below. W11--W13 additionally prove produced-revision/source-selection provenance
on success and no “current complete projection” claim on failure.

## Shared Run and Journal acceptance (J01--J08)

Use one two-Action Workflow fixture, one genuine standalone Action, and the
applicable row Action to prove both Run levels. The Workflow fixture retains
distinct Workflow, Step and Action IDs/definitions and real parent links. The
standalone Action has no fabricated parent. Assert exact admitted revisions and
frozen inputs (J01--J02), Started plus one truthful terminal or explicit pending
fact/result/effects (J03), and only registered event Type/outcome representation
with timezone/provenance/scope and no secrets (J04).

Fault-inject canonical Journal append *after* the selected effect. The status
must expose the effect and recording blocker, retain the original event
identity/payload, and avoid “journaled”/“complete” claims. Retry append with the
identical identity/payload: obtain exactly one durable receipt without another
Action invocation/effect. Retry a conflicting payload: reject it, preserve the
first payload/history, and again make no effect (J05). Reconstruct Artifact
Change and Process views only from canonical Journal event IDs; no-op has no
fictional change event (J06). For W11--W13, retain target/source revisions,
generator/configuration, attempt start/terminal and produced revision only on
success (J07). Finally inject malformed append input and a historical
nonconforming observed value: reject unsafe storage while preserving safe pending
evidence; do not use journal admission to authorize mutation or certify project
conformance (J08).

For cancellation, terminate an *actually started* mock dispatch at a controlled
barrier and assert the admitted cancellation/interruption representation, actual
effects, and no unstarted-success record. For partial work, fail after the first
observable authorized effect and require exact remaining boundary and recovery
state. For an uncertain dispatch, kill/restart the worker after intent but before
accepted result, then assert one agent/action invocation, no replay, and a
truthful interrupted/pending outcome. These are separate expected-failure or
recovery results, never clean passes.

## Current gaps and handoff

No selected Workflow currently has a generic Docker route adapter, selected
fixture corpus, or the required `test_selected_workflows_docker_e2e.py` harness.
Current observed container proof is limited to Base Revise, including its live
MCP pilot; it must remain excluded from W01--W13 coverage. The next bounded
implementation leaf must first obtain independent review of the relevant RMED,
then create mock golden corpus/harness support before any real Docker/MCP case.
Root should retain this as a readiness portfolio and add actual Run IDs, action
IDs, Journal receipt IDs, image ID and result paths only after functional runs.
