## Task, scope, and boundaries

**LangWatch offers six useful ideas for CAPRMEDIO Tools, Apps, and MCP. The strongest discussion shortlist is: executable discovery, compact results with drill-down, and reviewed failures becoming regression cases.** These extend the earlier trace-engineering assessment with concrete interface and feedback patterns.

This is a bounded harvest from one repository, not a claim to cover the whole field. The receiving use is Anatoly’s consideration of good ideas; no implementation, adoption decision, Requirement change, or software installation is included.

- **LangWatch snapshot:** [b3fb7ae516bec12171ad420f7e487c177100e13e](https://github.com/langwatch/langwatch/commit/b3fb7ae516bec12171ad420f7e487c177100e13e), committed 2026-09-23 12:47:34 UTC; inspected 2026-09-23. Git acquisition failed/stalled and was stopped. The complete tree and selected actual source files were fetched through GitHub at that commit. This was not a completed local checkout.
- **CAPRMEDIO snapshot:** live dirty worktree over `f57194953055ee35647bf5b6dcbb71d1389352b1`, with inspected-file hashes below. HEAD alone does not identify these current files. The worktree was left unchanged.
- **Evidence:** source, documentation, specifications, and test-file inspection. No LangWatch software or tests were run; test assertions describe intended checks, not observed passes. No performance benefit was measured.
- **Existing baseline:** [CA-A-903][C1] already proposes execution evidence, artifact dependencies, and evaluated lessons. Current code contains [sealed Work Journal events][C2] and [proof-currentness checking][C3]. Their presence prevents treating those ideas as novel gaps; operational coverage was not audited. Current [Apps boundaries][C4] and [MCP contracts][C5] constrain all transfers below.
- **State:** `COMPLETE`. The approved harvest is finished; the six ideas remain proposals for consideration.

Saved report: [fpf-reports/20260923T152008Z-fpf-sota-harvest-langwatch-tools-apps-mcp.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260923T152008Z-fpf-sota-harvest-langwatch-tools-apps-mcp.md).

### Composition receipt

Original invocation:

> in the context of our tools/apps/mcp
>
> [$fpf](/Users/am/.codex/skills/fpf/SKILL.md)  i need to do sota harvest from this repo
> not implementation, just good ideas
>
> https://github.com/langwatch/langwatch

Approved Plan: `FPF-LANGWATCH-20260923-2e6409b4` (`do`). Requested and executed: one `$fpf sota harvest`; no suffix or inter-command edge. This final report consolidates the passed step without new findings. Profile: none. Methodology: 1 page read/used, 0 deferred. Issues: LW-I01–LW-I06; ideas: LW-F01–LW-F06. Stop: `COMPLETE`.

## Issues, weak points, and improvements

### Native result

#### Harvest contract

**Frame H1:** Which practices evidenced in LangWatch could improve discoverability, evidence usability, evaluation learning, and execution visibility across CAPRMEDIO’s deterministic Tools, optional Apps, and provider-neutral MCP?

Admit primary repository sources with an exact commit and identifiable claim. Preserve differences between implemented code, test expectations, product documentation, and proposed architecture. English-language sources at the pinned snapshot are included; historical notes are used only with their amendments and stated status. Other vendors, field-wide comparisons, enterprise governance, cloud operations, gateway routing, and pricing are excluded. Jurisdiction is immaterial to this technical idea harvest.

The search followed the MCP source/test tree, dataset and annotation material, run-plan and experiment material, and matching local contracts. It stopped after each admitted idea had a source anchor and explicit transfer limit. Missing runtime evidence remains a gap. Competing semantics remain visible rather than being silently merged.

#### Corpus ledger and screening trail

All LangWatch links below resolve to the pinned commit. The tree inventory contained 26,583 entries; this is a retrieval fact, not an audited coverage count.

| Source group | Admitted evidence and inspected region | Role and limits |
|---|---|---|
| L1 — discovery | [Schema renderer][L1], [renderer tests][L2], [tool-name drift test][L3], [discovery specification][L4] | Code plus test/specification evidence. Platform-derived filter/SQL schema is distinct from still-static metrics/groups. Tests were not run. |
| L2 — result presentation | [Trace search][L5], [single-trace retrieval][L6], [experiment results][L7] | Code: digest/raw modes, pagination, row limits, target-scoped row keys, partial-result disclosure. Experiment handler inspected through relevant regions, not its whole call graph. |
| L3 — feedback into cases | [Dataset guide][L8], [review-queue guide][L9], [annotation mapping specification][L10], [suggestion resolver][L11], [resolver tests][L12] | Documentation describes review-to-dataset flow; code/test anchors substantiate the distinction between a suggested input and expected output. End-to-end persistence was not exercised. |
| L4 — repeatable comparisons | [Run-plan guide][L13], [MCP run handler][L14], [run-handler tests][L15], [scenario-version read][L16], [version-stamp test][L17], [dynamic-scope specification][L18] | Docs describe retained past-run configuration; implementation reads scenario versions with run inputs; a database test asserts old queued stamps survive edits. Service inspection is bounded to reference resolution. |
| L5 — incomplete runs | [Status derivation][L19], [status tests][L20], [result handler][L7], [run receipt formatter][L21] | Code distinguishes started jobs, partial results, interrupted state, and terminal markers. A five-minute heuristic is LangWatch-specific. |
| L6 — observation versus enforcement | [Online-evaluation guide][L22], [CI experiment guide][L23] | Documentation-level evidence: asynchronous monitors versus inline guardrails, and row-level CI evaluation results. Runtime enforcement was not verified. |
| P1 — parked architecture | [Payload-cost ADR][L24], [event-log ADR][L25] | Screened selected context/decision/amendment sections. Useful background, but distributed-worker architecture and partially proposed work are not justified imports for this local framework. |
| P2 — supporting source | [Run-plan API][L26], [identity-by-name specification][L27], [monitor service][L28] | Bounded screening confirms adjacent interfaces. Name-based grouping is not imported as CAPRMEDIO identity; the small monitor service alone does not prove asynchronous execution. |
| C1 — local receiving context | [README][C0], [prior analysis][C1], [Work Journal][C2], [proof currentness][C3], [Apps topology][C4], [MCP scope][C5], [invocation contract][C6], [currentness contract][C7], [App service method][C8], [Tool receipt method][C9] | Current bytes inspected; source declarations and code presence are distinguished from runtime completeness. |

Screening record `FLOW-H1`: operator repository → pinned commit/tree → MCP, feedback, run, and evaluation source families → six admitted ideas; two architecture documents parked and three adjacent sources screened. No claim of exhaustive repository review. The shortlist below is an explicitly requested discussion view of all six admitted ideas, selected for direct relevance and concrete evidence; it is not an adoption ranking or a measured optimum.

#### Claim sheets: useful ideas and their transfer

| ID | LangWatch source claim | CAPRMEDIO idea, overlap, and limit |
|---|---|---|
| H1-01 | Discovery reads filter/SQL definitions from the platform’s reference endpoint; a test compares feature-map tool names with registrations. [Code][L1], [test][L3]. | **Make discovery an executable view of the real capability catalog.** A Tool’s actual contract should supply MCP help, examples, and App actions, with a check that advertised names resolve. This concretizes existing complete-contract/current-registry rules [C6][C6], [C7][C7]; it is not a new authority layer. Do not copy the static lists or regex extraction as a universal generator. |
| H1-02 | Trace tools default to readable digests and offer raw JSON; search exposes its next-page token; experiment results disclose partial data and truncation. [Search][L5], [results][L7]. | **Offer a small answer first, with reliable expansion.** MCP and Graph UI can show affected IDs, failures, counts, currentness, and the next read operation before full evidence. This adds a usable presentation to existing evidence, reducing likely context load. CAPRMEDIO must retain its structured result envelope; Markdown is a presentation, not a replacement for it. Benefit is unmeasured. |
| H1-03 | Reviewed traces become dataset rows; corrections remain beside the original. The resolver accepts whole-trace/output suggestions as expected output and rejects input/span suggestions for that field. [Guide][L9], [code][L11], [tests][L12]. | **Turn a reviewed failure into an anchored regression case.** Preserve the original run, exact input/output field, reviewer correction, expected outcome, and applicability. This gives CA-A-903’s lesson idea a concrete intermediate artifact before any governed rule change. A correction is still a proposed expectation, not verified truth. LangWatch’s permissive fallback for unknown anchors should not be copied into governed evidence. |
| H1-04 | Runs vary scope, targets, repeats, and simulator/judge settings; past runs retain settings. Scenario versions are read with run inputs and stamped on queued runs. [Guide][L13], [code][L16], [test][L17]. | **Compare versions with an explicit case × target × evaluator matrix.** A future Evaluation interface could show precisely which Tool/Prompt/Workflow release ran each case, under which evaluator and input versions. Existing proof currentness provides part of the provenance foundation. Dynamic selectors must also record their resolved cases, or changed denominators can masquerade as improvement. This does not imply deterministic replay. |
| H1-05 | Status code preserves running/interrupted/completed/stopped distinctions; results remain available before completion. The scheduling receipt names batch and job count and points to a separate results call. [Status][L19], [receipt][L21], [results][L7]. | **Treat execution status as evidence the interfaces must expose.** Tools/MCP/Workflow Orchestrator/Graph UI should distinguish accepted, running, waiting, interrupted, failed, cancelled, and completed according to their declared contracts. This makes the existing App-state and operation-receipt requirements tangible [C8][C8], [C9][C9]. Import the distinction, not LangWatch’s five-minute timeout or its exact state vocabulary. |
| H1-06 | Online monitors score after the response; inline guardrails may block it. CI experiments can return per-row outcomes. [Monitor guide][L22], [CI guide][L23]. | **Keep observation and a blocking Evaluation visibly separate.** An Ops signal may suggest investigation; a declared Evaluation can govern a specific release/change gate. Shared checks may reduce duplicated logic, but timing, completeness, and authority differ. This reinforces CAPRMEDIO’s existing role separation; evidence here supports an idea, not a verified implementation recipe. |

**Discussion shortlist:** H1-01, H1-02, and H1-03. They add concrete interfaces and a feedback path to the existing trace/currentness direction. Keep H1-04–H1-06 in the same evidence map; their value depends more on the eventual evaluation and workflow scope.

#### Method families, bridges, and examples

Palette `PALETTE-H1` and harvested set `SET-H1` contain H1-01–H1-06 exactly. They preserve three distinct approaches:

| Approach | Objects and actions | Useful characteristics | Bridge to CAPRMEDIO; loss to avoid |
|---|---|---|---|
| Contract-driven interfaces | Catalog, schema, query, structured result; discover and inspect | Contract coverage, stale references, result size, retrieval completeness | MCP registry and App projections. A help description is not execution authority. |
| Experimental evaluation | Case, target, evaluator, version, run; execute and compare | Per-case outcome, failure/error/skip counts, cost, duration, coverage | Evaluation definition plus Operations evidence. An LLM score is not a deterministic invariant, and a changed case set is not a like-for-like comparison. |
| Operational observation and review | Trace, span, annotation, interruption; observe, correct, curate | Failure context, evidence currentness, completion status, review provenance | Work Journal and candidate regression corpus. Observed traffic differs from controlled tests; edited examples differ from original evidence. |

Bridge records `B-H1-1`–`B-H1-3` are conceptual mappings for these rows only. They assert neither equivalence nor replacement. In particular, LangWatch’s **run plan** is test configuration/history grouping, not CAPRMEDIO’s **Plan Atom** with accepted change authority. LangWatch’s mutable product state cannot become CAPRMEDIO authority.

Micro-examples are proposed receiving uses, not executed demonstrations:

- **ME-1:** An agent asks which read operation returns dependants. Discovery provides the current schema and registry revision; the response gives ten IDs and a continuation token. A later full read resolves the same snapshot.
- **ME-2:** A review finds that an Atom search omitted an eligible result. The original input/output stays intact; a reviewed case records the missed ID and expected set. A suggested query correction occupies an input field, never the expected-output field. This is the distinction checked by [L12][L12].
- **ME-3:** Two Tool releases run the same versioned cases. The App shows each failure and evaluator error separately. If one run ends early, its available rows remain inspectable and its total is explicitly incomplete, following [L7][L7].

Pack-local object map `OBJECTS-H1`: discovery/result → MCP interface over a declared Tool contract; review/case → candidate Evaluation input derived from Operations; run/version/outcome → observed execution evidence; App row → non-authoritative projection. No public terminology or governed names are minted (`UTS-H1`: none). Indicator families `IND-H1` are proposals only: complete versus partial coverage; pass/fail/error/skip; current/stale/unknown evidence; bytes/tokens/latency. No threshold or gate authority is established here. Case generation is limited to reviewed observed failures; synthetic scenario generation remains outside the admitted transfer.

#### Disagreements, exclusions, and return condition

- Source-derived discovery is promising, but LangWatch still keeps some categories static. Its drift test checks name inclusion, not whole-contract semantic equality.
- Summaries trade context size against detail. A digest must retain omitted-count/status/provenance cues and an expansion path; it cannot support a completeness claim on its own.
- [L12][L12] explicitly tests treating an unknown annotation anchor as a whole-trace suggestion. CAPRMEDIO should keep such unknown provenance unresolved if this idea is pursued.
- Dynamic run scopes and mutable plan configuration are convenient for repeat usage but insufficient by themselves for stable comparison. Preserve resolved input identities alongside the friendly name.
- The payload-cost ADR has amendments distinguishing shipped mechanisms from deferred phases. No distributed storage, queue, grant-pool, or event-sourcing adoption is recommended from that document.

Return to this pack if LangWatch changes an admitted path, CAPRMEDIO’s relevant contract hashes change, or the Operator selects an idea for deeper evaluation. A selected idea would need a bounded design/evaluation task and current evidence before implementation. No automatic follow-up or monitoring is started.

### Issue registry

These are **transfer risks**, not claims that six bugs exist in CAPRMEDIO. Percentages express reviewer confidence in the stated risk and evidence interpretation, not measured frequencies.

| ID | Issue, target, and consequence | Evidence; confidence; coverage limit | State; mapping |
|---|---|---|---|
| LW-I01 | Interface documentation can drift from callable capabilities, causing invalid MCP calls. | L1/L3 explicitly describe and check this failure; 99%. Current CAPRMEDIO drift prevalence is unknown. | OPEN; LW-F01 |
| LW-I02 | Large or silently partial results can exhaust context or support false completeness claims in MCP/App use. | L5/L7 contain paging, caps, and partial markers; 98%. No local token/latency baseline. | OPEN; LW-F02 |
| LW-I03 | Review conversion can put the wrong correction into an expected result, corrupting regression cases. | L11/L12 distinguish input/output anchors and reveal the permissive fallback; 99%. Full review-to-dataset runtime was not tested. | OPEN; LW-F03 |
| LW-I04 | Mutable cases or scopes can make historical evaluation comparisons misleading. | L13/L16/L17 retain run/scenario version context; 98%. Full evaluator/environment provenance not audited. | OPEN; LW-F04 |
| LW-I05 | Started or silent work can be mistaken for completed work, hiding missing results. | L19/L20/L21 and L7 explicitly distinguish these conditions; 99%. Timeout values are workload-specific. | OPEN; LW-F05 |
| LW-I06 | An asynchronous monitoring score can be mistaken for a blocking or complete Evaluation. | L22 explicitly separates monitor timing from guardrails; 97%. Documentation-level evidence, no runtime timing check. | OPEN; LW-F06 |

### Fix and improvement register

All entries are **PROPOSED ideas for later consideration**. Owner: Anatoly for selection, the relevant CAPRMEDIO component owner for any later change. Implementation authority is absent. Verification below is a future acceptance criterion, not a performed test. The order is a discussion order, not an implementation schedule.

| ID / issue | Exact idea and relationship | Confidence, expected result, trade-offs | Dependencies/order, verification, recommendation |
|---|---|---|---|
| LW-F01 / I01 | Derive discovery/help/App capability references from one admitted contract and check advertised identities. Complementary to current MCP rules. | 95% fit: L1/L3 align with C5–C7. Fewer invalid invocations; generation and revision handling add maintenance. | No other idea required; resolve the actual registry first. Check every advertised call against name/schema/revision and explicit stale rejection. **Preferred** for discussion; PROPOSED. |
| LW-F02 / I02 | Add compact result views with counts, status, provenance, explicit truncation, and a stable route to full structured evidence. Complementary. | 95% fit: direct L5/L7 mechanism plus C6. More usable evidence; extra reads and snapshot retention cost. | Define contract/result identity before a digest; F01 is compatible, not mandatory. Verify digest/raw agreement and complete retrieval across pages. **Preferred**; PROPOSED. |
| LW-F03 / I03 | Curate original run + anchored correction + expected outcome + applicability into a candidate regression case. Complementary to CA-A-903. | 92% fit: L8–L12 show the path, but local schema/workflow is unresolved. Reusable failure learning; review labor and sampling bias. | Resolve original evidence identity first; reject unknown anchors. Verify a suggested input cannot become expected output and originals remain unchanged. **Preferred**; PROPOSED. |
| LW-F04 / I04 | Retain resolved versioned case sets and target/evaluator configuration on each Evaluation run, then compare outcomes by case and target. Complementary. | 92% fit: L13/L16/L17 plus currentness code. Interpretable comparisons; more provenance and experiment complexity. | Requires a selected evaluation use; F03 may supply cases. Verify later edits leave old run settings/stamps unchanged and differing denominators are visible. **Acceptable**; PROPOSED. |
| LW-F05 / I05 | Expose declared run states and partial results consistently across backend, MCP, and App views. Complementary to operation receipts. | 95% fit: L19/L20 with C8/C9. Fewer unsupported completion claims; heartbeat/recovery ambiguity remains. | Resolve each operation’s lifecycle; no other idea required. Verify start receipts never imply completion and interruption retains labeled partial evidence. **Acceptable**; PROPOSED. |
| LW-F06 / I06 | Label observation, advisory score, and blocking check by timing and authority; reuse evaluator logic only where its inputs and meaning match. Complementary. | 90% fit: L22 and existing role separation; implementation unverified. Clearer reliance; asynchronous lag and judge uncertainty persist. | Requires an Operator-owned gate if enforcement is desired; F04 may record results. Verify an advisory/partial result cannot close a blocking gate. **Acceptable**; PROPOSED. |

#### Local evidence pins

The following SHA-256 values identify the inspected dirty-worktree bytes. Links C0–C9 resolve to their current paths, not immutable Git versions.

| Local source | SHA-256 |
|---|---|
| C0 README | `bbe228cd9c7ddd97a9b586d608e639aeebbbae81c5e7f8ff4d1b5c2416723cb2` |
| C1 CA-A-903 | `a0f2dc6cdd296afff3609764d665e853c0401bcf179744084d07c8b1c5e66034` |
| C2 Work Journal | `1dcbaf834e0818cb0f3158dfa31d917559af257256be113aa5c1d9d97dcaaea8` |
| C3 proof currentness | `80120a14d82eed3763ceea7d20848c4544f220cd78560ec1a56f4ea1afa37cff` |
| C4 CA-R-1100 | `1da267f1676aed64015aaf4bfd83764b0c591bbd20aa0dba4c8aaa150d554497` |
| C5 CA-R-1113 | `d73081839df851d4af282383222335745516027e349a2fe04fa45a95240df242` |
| C6 CA-R-1107 | `0ffeed71691af63a1b75aa6cf33c7ac4164729e44bc162a34b3819021fb2bef4` |
| C7 CA-R-1115 | `d8d64e465be7ef32f18bcb4ee3179363a4533afb4f677198ea1668181edef64b` |
| C8 CA-M-222 | `973bba46ab38aa7ec21bd27231fb5bcace34d67810e2fffaaa8f99989953c9b8` |
| C9 CA-M-223 | `1bcc3b53e738dbad582122fa9137e78738214c068be67fb93adb6500f6bb6251` |

## Unresolved evidence gaps

| ID / links | Best current answer and missing evidence | Consequence and exact next evidence |
|---|---|---|
| LW-G01 / I01–I06, F01–F06 | Existing requirements and partial code overlap substantially; full current implementation coverage is unknown. | Novelty is bounded. If an idea is selected, inspect that component’s active registry, code, and tests against the recorded hashes. |
| LW-G02 / F02–F06 | Benefits are plausible, unmeasured; no local benchmark, operator study, or LangWatch runtime test was performed. | No savings/reliability promise. Later evaluate one representative local task with baseline and candidate, recording complete results. |
| LW-G03 / I03, F03 | Anchored correction logic is evidenced; end-to-end dataset integrity and adjudication quality are unverified. | A curated row cannot automatically become trusted expected truth. Inspect the mapping/persistence path and test reviewed input/output cases before adoption. |
| LW-G04 / I04, F04 | Scenario version stamping is evidenced, but complete evaluator, model, environment, and resolved-data snapshots were not audited. | No exact replay or universal comparability claim. Trace one run end-to-end before relying on it as a reference design. |
| LW-G05 / I06, F06 | Monitor/guardrail timing is documented; full asynchronous runtime was not verified. | Retain this as a conceptual boundary. Inspect dispatch and enforcement paths if selected. |
| LW-G06 / all | This is one repository and selected file regions. The native Git checkout did not complete; pinned source retrieval succeeded. | Insufficient basis for field-wide SoTA or whole-system correctness. A broader comparison or full local checkout is separate follow-up evidence if needed. |

## Skills used

1. `$fpf sota harvest` — completed the approved, read-only idea harvest.

### FPF sources consulted (1 read; 1 used)

- **Used:** `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_SoTA Harvester & Synthesis/00_G.02 - SoTA Harvester & Synthesis.md`, verified `fpf_id: G.2`; edition source revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`, generated 2026-08-26. Inspected Problem frame, Problem, Forces, Solution §§4.2–4.4 and 4.6–4.7, and Consequences. This grounds the ledger, distinct claims, mappings, and bounded receiving use. The entire Solution and linked neighboring patterns were not inspected.

[L1]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/discover-schema.ts#L14-L76
[L2]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/__tests__/discover-schema.unit.test.ts#L1-L119
[L3]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/__tests__/feature-map-tool-drift.unit.test.ts
[L4]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/specs/mcp-server/schema-discovery.feature
[L5]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/search-traces.ts
[L6]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/get-trace.ts
[L7]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/get-experiment-results.ts
[L8]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/docs/datasets/overview.mdx
[L9]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/docs/annotations/queues.mdx
[L10]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/specs/datasets/dataset-annotations-mapping.feature
[L11]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/server/annotations/annotationSuggestedOutput.ts
[L12]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/server/annotations/__tests__/annotationSuggestedOutput.unit.test.ts
[L13]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/docs/agent-testing/run-plans.mdx
[L14]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/run-plan.ts
[L15]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/__tests__/run-plan-tools.unit.test.ts#L1-L143
[L16]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/server/suites/suite.service.ts#L2487-L2514
[L17]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/server/suites/__tests__/suite-run-version-stamp.integration.test.ts#L111-L190
[L18]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/specs/suites/run-plan-dynamic-scopes.feature
[L19]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/experiment-run-status.ts
[L20]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/__tests__/experiment-status.unit.test.ts
[L21]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/mcp/typescript/src/tools/format-run-plan.ts#L6-L44
[L22]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/docs/evaluations/online-evaluation/overview.mdx
[L23]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/docs/evaluations/experiments/ci-cd.mdx#L102-L134
[L24]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/dev/docs/adr/069-payload-cost-doctrine.md
[L25]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/dev/docs/adr/022-event-log-source-of-truth.md
[L26]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/app/api/run-plans/%5B%5B...route%5D%5D/app.ts#L1-L100
[L27]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/specs/suites/run-plan-identity-by-name.feature#L1-L170
[L28]: https://github.com/langwatch/langwatch/blob/b3fb7ae516bec12171ad420f7e487c177100e13e/platform/app/src/server/app-layer/monitors/monitor.service.ts
[C0]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/README.md
[C1]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-903-FRAMEWORK_ENGINE-ANALYSIS_RPRT--assess-trace-engineering-ideas-for-caprmedio.md
[C2]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py
[C3]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/generate_proof_currentness_catalog.py
[C4]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/04_requirement/CA-R-1100-APPS-CORE-REQUIREMENT--define-the-application-scope-unit-topology.md
[C5]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1113-MCP-REQUIREMENT--provide-one-project-local-provider-neutral-mcp-service.md
[C6]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1107-MCP-REQUIREMENT--require-complete-tool-invocation-contracts.md
[C7]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1115-MCP-REQUIREMENT--bind-mcp-operation-to-the-current-project-frontier.md
[C8]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-222-APPS-CORE-METHOD--bind-an-app-interface-to-declared-backend-services.md
[C9]: /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-223-TOOLS-CORE-METHOD--bind-tool-effect-results-to-the-canonical-operation.md
