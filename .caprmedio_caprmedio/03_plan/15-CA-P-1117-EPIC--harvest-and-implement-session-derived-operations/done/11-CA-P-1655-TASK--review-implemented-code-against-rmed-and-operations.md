---
atom_id: CA-P-1655
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Epic implementation alignment"
  depends_on: [Implementation, Requirement, Method, Evaluation, Delivery, Operations, Workflow, Action, Tool]
version: 10
updated_at: "2026-10-08 15:33:32 +0000"
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1124]
---
# Summary

Review implemented code against RMED and Operations

## Objective

Review the approved first usable capability cut against its current applicable RMED and O Atoms. The required review covers only that cut, not formal N+1 release acceptance or the former all-sixteen-Workflow review.

## Details

The approved review frontier is exactly six Workflows: Create Atom, Update Atom, Replace Atom, Change Atom Status, Implementation, and Build Applicable Methodology. Review their actually used RMED/O, code, stdio MCP, orchestrator and Journal paths, including success, no-op and relevant failure records. The functional boundary also includes Docker HTTP MCP authentication, initialize/list/call/health/lifecycle and invalid credential, Host and Origin refusal.

The retained review records the exact source/code frontier and governing Atom identities for this cut. It does not assert a formal full N+1 release, all-sixteen-Workflow coverage, or closure of Automated Release, Scope mutations, Revert, graphs, standalone query branches or additional recovery hardening. Those remain deferred work, not accepted behavior.

### Historical review checkpoints

- the six retained Workflows passed the disposable Docker stdio native-effect, source-graph, and shared Run Journal test at Engine commit `38b1d7319`, immutable development image `sha256:46ddf9480372160f0d435d6e03e7bcf358c542ce59659ce71ff269103c3dc9a0`. the aggregate test exited 0 after 133.220 seconds. Implementation used the explicit golden mock Agent, not a live LLM. the detailed receipt is `.caprmedio_tmp/epic-first-cut-20261008/stdio-six-workflows-38b1d7319.log`.
- this receipt covers those six happy cases only. it does not establish every Status, lifecycle composition, proposed direct Relation, or HTTP security case.
- the bounded source review found a missing canonical file-change producer for Update/Status composition, valid direct Relation/nested Plan admission gaps, and incomplete HTTP denial/token-rotation assertions. these are required first-cut repairs, not optional Tool expansion.
- current repair commits include `45ea43214` (evidenced carrier-only baseline authority), `97ec979c3` (truthful interrupted public status), `770afde12` (HTTP denial and token-rotation tests), `53487ee4c` (finite Relation authority pins), `7d5370e89` (complete Status fixtures), and `4ab862ec6` (exact proposed-target inventory). implementation and fresh integrated acceptance remain unfinished.
- the current all-role Status diagnostic at `7d5370e89`, image `sha256:a0a5068cf354d431270f39d5df793cb84cecb99c39e72bc474a05b0d443c989e`, passed image isolation and stale compilation-source refusal. its Status matrix stopped at an incorrect test expectation: the actual unchanged-Status Run recorded `no_op`, while the helper expected `completed`. the failed aggregate receipt remains `.caprmedio_tmp/epic-first-cut-20261008/boundaries-7d5370e89.log`; the unexecuted remainder is not passed.
- real localhost HTTP proof remains unavailable because the active host profile denies the direct loopback connection. synthetic HTTP tests are not a substitute. the prepared Terminal proof must target the final exact development image after the remaining repairs; installed N is unchanged.

### Current accepted first-cut evidence

Engine code is frozen at `1bfab3e78`, in unselected development image `sha256:a363a23108aa9c28acbe8e7c5bb9bb5cd2530fb4c6187811c317b362e4520fc2`. this is a disposable test candidate, not installed N+1 or formal release promotion.

| Reviewed boundary | Accepted repair / evidence |
| --- | --- |
| W09 source graph and W13 partial-effect classification | `7ff886387`; current O016 graph/revisits, and stale applied output retains truthful partial effects |
| W02 rollback and mutable before-state | `a142e7eea`; exact restoration or preserved uncertainty/history, not silent loss |
| W09 malformed Agent result | `b000005f1`; actually observed effects retained |
| HTTP empty-token factory | `b1106f2c5`; empty/missing credentials cannot admit handlers |
| Complete Create/Replace carriers and existing direct Relations | `a3b53639c`, `7286176be`, `093174c59`, `1bfab3e78`; full supplied carriers preflighted; current targets and nested Plan placement resolved |
| Canonical lifecycle / replacement records and actual child Runs | `7be2e970e`, `c8ee3c1c2`, `c56c8a6b7`, `d48de086c`, `d8a5ffba0`; observed baselines, changes, replacement provenance and native child lineage |
| Every current Content Role's Status model | `1bfab3e78`; literal lowercase Concern domain preserved; D324 final Operations entry parsed from source, not omitted |
| Final bounded source acceptance | final wrapper, target inventory and lifecycle hashes accepted by the independent read-only reviewer; no invented domain or source-authority bypass |

The bounded seven-finding source review is retained at `.caprmedio_tmp/epic-first-cut-20261008/scoped-review.md`. its original findings are historical, and the accepted repair table above records their disposition. the Epic's explicit mechanical-Git exception is retained; it is not an invented save-Tool intake or Journal receipt.

| Functional evidence | Result / retained receipt |
| --- | --- |
| Native carrier/status/reference/Plan and lifecycle composition | 26 tests passed in 93.815 seconds; `native-status-and-composition-final.log`, SHA-256 `7b2c05b9c7e307882b30ca234b88c3fc1eb1df966cb496e3c22a24e4a33af4c8` |
| Six retained Workflows over Docker stdio MCP | passed in 155.939 seconds; `stdio-six-workflows-1bfab3e78.log`, SHA-256 `9f1c9f2f59bac99c64cc8e86b324ea4766368db63381ce0a2aa46d3a7575b469` |
| Requirement / Method / Evaluation / Delivery Status shard | passed in 311.761 seconds; `status-1bfab3e78-a.log`, SHA-256 `c82f685e62f26b77b6194a4a168cfb3dcbfffb94fe38012ad1fcb0b164cbd19d` |
| Plan / Concern / Operations / Analysis Status shard, image isolation and stale-source refusal | passed in 363.745 seconds; `status-1bfab3e78-b.log`, SHA-256 `bfaef09fad75603455bc31af50605eb037e6a21e87210a0f866990c576f9c8cb` |
| Six-route replay with actual fixture evidence retained | passed in 124.608 seconds; `stdio-six-workflows-1bfab3e78-retained.log`, SHA-256 `4320d6da6b1991e2b89cd7f5da8a764cef311c6308f657259b1dd9cab1483e36` |

All receipt filenames above are under `.caprmedio_tmp/epic-first-cut-20261008/`. the two Status shards exactly partition all eight Content Roles: 27 admitted transitions, eight no-ops and eight invalid-Status refusals. invalid requests preserved both authority and recording snapshots. the isolated-image and stale compilation-source checks passed without undeclared host Implementation or mutation effects.

The retained canonical Journal/result/effect files live under `stdio-1bfab3e78-retained/selected-workflows-docker-e2e/`. their observed terminal index is `retained-workflow-receipts.json`, SHA-256 `9a3866d6b440584feac03a06460b2e9f4d4395a0389e47dac528ffae2ed4a244`: six actual Workflow terminals (`golden-w01-happy`, `golden-w02-happy`, `golden-w03-happy`, `golden-w04-happy`, `golden-w09-happy`, `golden-w13-happy`) and 18 actual Action terminals, with definition pins, event digests, parent identities and retained result/effect references. these are disposable test Runs, not production Runs. the Implementation case used the explicit golden mock Agent, not a live LLM.

### HTTP Terminal failure and publication repair

the Operator's Terminal proof against `1bfab3e78` ran 12 tests in 128.071 seconds: 11 synthetic guards passed, but all six live Workflow subcases failed during MCP initialization with `httpx2.ConnectError`. No HTTP Workflow execution is accepted. The original failed receipt is `http-six-workflows-1bfab3e78-terminal.log`, SHA-256 `129c9ea0a59d6bfe7ead874304478f56bb85a5c15097498600f978afe998b905`.

a fresh Docker diagnostic independently found a real publication defect: `mcp-http` was running and healthy, but Docker reported an empty publisher URL and published port `0`, despite a requested loopback mapping. Commit `b1c2bd18a` repairs this by attaching only the HTTP service to a dedicated publication bridge; worker, Agent and stdio network attachments are unchanged. D578@2 explicitly records that this non-internal bridge permits HTTP-service outbound traffic. Startup now refuses readiness unless actual Docker metadata proves the exact selected loopback publisher. Authentication, runtime-secret injection, restricted mounts and no-Docker-socket boundaries remain intact. The independent bounded review accepted the correction; 36 focused runtime, network, diagnostic and HTTP harness guards passed, with the actual HTTP E2E opt-in case unrun.

the rebuilt unselected development image is `sha256:f8bcb97088e62728c6e48fca703e36fb15a4950196e18fafb0d9b9319dca59a6`, labelled with exact Engine commit `b1c2bd18a`. A real Docker diagnostic now observes the running, healthy HTTP service with `tcp`, target `8092`, published port `18092`, and bind `127.0.0.1`. Its retained receipt is `http-connectivity-ECF9ol9a/diagnostic.log`, SHA-256 `2e8d3fc5432e3e03cad67f1d8f76855e9532b9388ae89afefa8925b5cd1c03d6`. The diagnostic still fails its direct TCP assertion with this session's `PermissionError`, errno `1`; it establishes corrected Docker publication, not MCP protocol or Workflow success. All test services were stopped after the diagnostic.

### Current source admission and proof candidate

the current selected binding initially refused admission because two private source-carrier pins in D572 lagged the accepted Engine. Commit `5fab36806` updates only those pins, preserves D572@28, and advances its exact reader pin to D572@29. Fourteen focused admission tests passed. The serialized public binding has no admission drift, so no Manifest rewrite, Journal reconciliation or Release was performed. An actual advertised MCP reload restored current discovery and complete Change Atom Status context. P1615's closure preview was admitted without changing that Plan or dispatching a Run.

the fresh unselected development image is `sha256:75759a40209b4f2ab9adae212d1f3d8f771bb252a986bcdd5d24dead90bb9cb9`, labelled with exact Engine commit `5fab36806`. The Terminal proof script now selects this image and a fresh retained report directory. The preceding accepted stdio and Status receipts remain exact historical evidence; this pin-only correction is not a new functional HTTP receipt. Installed N is unchanged.

### Fresh authenticated HTTP proof and host harness correction

the Operator's fresh Terminal report `http-5fab36806-terminal-DybImct0/full.log`, SHA-256 `5241c9078bea8affc3382c80112126379142c01e7c18fc611fabeeb39136841c`, ran 12 tests in 102.336 seconds. Each of the six cases completed authenticated MCP initialization and Tool listing, then failed before Workflow dispatch because the host harness incorrectly accessed `session_id` on the SDK's async context manager. This supersedes the original connection-level failure as the current observed proof defect; neither receipt establishes six-Workflow HTTP acceptance.

Commit `9dea0a672` corrects only that host harness. It observes the actual server-issued `Mcp-Session-Id` response header through an awaited HTTP response hook and returns typed session metadata; missing or empty identifiers refuse before yielding. The existing cleanup stack, authentication, disabled proxies, denied-continuation and token-rotation checks remain unchanged. The real installed SDK with a mock HTTP transport reproduced the original AttributeError before the repair and passed afterward. Thirteen corpus tests and six security tests passed; the actual Docker opt-in test was skipped, not passed. The independent read-only review accepted host-harness SHA-256 `0c17f2bb27c9692b5bcde6302799de25d3790bfed9bccd1bacafddcaa0d23a15`.

the candidate image remains exactly `sha256:75759a40209b4f2ab9adae212d1f3d8f771bb252a986bcdd5d24dead90bb9cb9`. No runtime implementation, D572 private pin, selected binding or installed N changed. The corrected host harness has separately recorded provenance and differs from the historical test copy baked into that image; no aggregate byte-identity claim is made. The same Terminal script is ready to collect a fresh retained actual HTTP receipt using this repaired host harness.

### Accepted actual HTTP functional evidence

the Operator's corrected Terminal proof `http-5fab36806-terminal-omm68ywL/full.log` passed all 14 tests in 118.565 seconds, with no skips. Its SHA-256 is `4f157a1e8985d837aa91d10f759735d8600e29753ecdc1d95bdc2b9141da2e1b`. The actual six cases completed authenticated initialize/list/call, non-mutating previews, native effects and shared Workflow/Step/Action Journal checks. Invalid credentials, Host, Origin, denied reload calls and invalid-token session continuation were refused without changing recording state. Healthy loopback startup and stop/status cleanup passed; W01 token rotation rejected the former bearer/session and allowed the replacement session. The same candidate's W01 stdio context check passed, alongside the separate accepted six-route stdio receipts above.

the retained actual fixture artifacts are under `http-5fab36806-terminal-omm68ywL/selected-workflows-docker-e2e/`. The deterministic terminal index `http-workflow-receipts.json`, SHA-256 `adb7d7f0b08be0f58ec97afaebb1a4ae8c0d6d9f4350c8d4c49e282df71b7818`, verifies six completed Workflow terminals and 18 completed Action terminals with source pins, event identities/digests, parent lineage and retained result/effect references. The independent read-only reviewer accepts this actual HTTP boundary. W09 used the explicit golden mock Agent, not a live LLM; these are disposable proof Runs, not production Runs. This is not an all-Status-over-HTTP test, formal Release, promotion or installed-N claim.

### Administrative record closure

the required actual Docker HTTP proof is now accepted from the Operator's permitted Terminal, not from a permission bypass or a synthetic substitute. Together with the accepted source review, stdio, all-role Status and composition receipts, this satisfies the retained first-cut functional acceptance frontier. Installed N, historical failed receipts and deferred work remain unchanged. The Operator explicitly authorized attempting MCP first, then mechanical Git closure if it failed. This review record is closed administratively from the accepted evidence; the Epic closes only after its retained required records and explicit deferred dispositions are saved.

the Project's Docker worker is not running. Current MCP discovery/context succeeded, but the actual read-only orchestrator status call returned `Docker queue call failed; inspect runtime logs; no native queue fallback`. No closure Run was frozen or queued. The admitted P1615 preview is not execution or completion. The Operator's explicit MCP-first/Git-fallback instruction authorizes this administrative source closure; no production status Run, Event or Journal receipt is fabricated.


## Definition of Done

This Plan may be Done only after the six-Workflow frontier has explicit RMED/O-to-code coverage, functional stdio MCP/orchestrator/Journal evidence, and Docker HTTP MCP protocol/authentication evidence with truthful success, no-op and failure dispositions. This scope amendment does not establish that evidence; deferred branches and any formal release/Epic closure remain outside it.
