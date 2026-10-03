---
atom_id: CA-A-903
cce_version: cce_1
cce_form: rationale
subjects:
  governs:
    continuant:
      - trace-engineering-adoption
      - execution-evidence-currentness
  depends_on:
    continuant:
      - FRAMEWORK_ENGINE
relations:
  analysis_of:
    - CA-R-1426
version: 1
updated_at: 2026-09-15 05:09:46
---
# Assess Trace Engineering ideas for CAPRMEDIO

## Task, scope, and boundaries

Assess the practical value of the article **Trace Engineering for AI agents: full explanation and architectural guide**, published by **Не шути, да не шутим будешь (@uncleshampoO)** on 2026-09-14, for CAPRMEDIO. The article and the primary references below were inspected on 2026-09-15. The Operator then requested that the assessment be saved as an Analysis.

**Finding:** three ideas merit further evaluation: evidence-backed completion claims, explicit artifact dependencies between operations, and scoped lessons distilled from verified failures. The strongest first candidate is an Evaluation execution record whose evidence is checked against the current inputs.

This Analysis concerns Framework Engine observability across programmatic execution and agentic reporting. It relates to `CA-R-1426`, which requires engine execution to be observable and transparent. Framework Engine is the narrowest common scope for those concerns.

The result preserves an assessment and proposed next step. It does not authorize implementation or establish new normative requirements. The repository review was bounded to the README and the identified observability goal, not an exhaustive inventory of existing tracing, evidence-currentness, or memory implementations. Accordingly, the proposals are not claims that those capabilities are absent.

## Issues, weak points, and improvements

### 1. Require execution evidence for completion claims

The article's strongest idea is to connect important agent claims to recorded execution. An agent saying that tests passed should reference an execution containing:

- The command, working directory, and tested code revision or input digest.
- Exit status and actual test results.
- References to the artifacts produced by the run.

**Application to CAPRMEDIO:** connect an Evaluation result to the execution that supports it. The current README distinguishes Evaluation, which checks claims, from Ops, which preserves evidence from running and using the system. This proposal makes that relationship operational.

**Additional recommendation from this assessment:** evidence must become stale when relevant inputs change. Passing tests before the final edit cannot establish that the final state passes. A zero exit code alone also cannot establish that the intended tests ran against the intended inputs; the recorded test selection and results matter.

The execution record establishes what was observed. Whether that evidence is sufficient for a completion claim remains a question for the applicable Evaluation.

### 2. Record which artifact versions each operation consumed

A call hierarchy answers who called whom. Debugging also needs to show which output an operation relied on. Record input and output artifact identities and hashes alongside operation links, allowing an investigation to follow:

> Failed validation → generated configuration → source artifact version → operation that introduced the problem.

OpenTelemetry supplies parent relationships and additional span links. Meaningful artifact and data dependencies still require application instrumentation; a call relationship alone does not prove the cause of an incorrect result. See [OpenTelemetry span links](https://opentelemetry.io/docs/concepts/signals/traces/#span-links).

**Application to CAPRMEDIO:** link project knowledge to runtime evidence and use the dependency information to help identify which Evaluations need to run again after a change. This is a proposed receiving use, not a confirmed current capability or a demonstrated implementation gap.

### 3. Turn verified failures into reusable, scoped lessons

The useful memory pattern is:

> Observed failure → explanation → tested correction → lesson with applicability conditions and evidence.

[ReasoningBank](https://arxiv.org/abs/2509.25140) studies reusable strategies distilled from successful and failed experiences. Its approach uses agent judgments to supply learning signals; it does not make every extracted rule independently verified.

**Additional recommendation from this assessment:** extracted lessons should remain candidates for evaluation. One failed run is insufficient justification for a permanent prohibition. Preserve the conditions under which a lesson applies and the evidence supporting it before considering a governed Method or Requirement change.

### 4. Correct the article's reproducibility guarantee

Fixing a seed and setting temperature to zero does not provide a universal deterministic-generation guarantee. Anthropic explicitly documents that even zero-temperature results need not be fully deterministic. See the [Claude glossary](https://platform.claude.com/docs/en/about-claude/glossary).

For the proposed design, distinguish replaying recorded model/tool responses under controlled state from continuing with fresh external calls. The latter is a new execution and can diverge. Exact offline replay requires sufficiently complete captured inputs, responses, and relevant state; the trace structure by itself is insufficient. Repeated mutations also require explicit handling so replay does not repeat an external side effect.

### 5. Preserve the scope of the research statistics

The article's **90% versus 4%** figures appear in the cited Co-Scientist study, but they refer to severe result hallucinations in **Agent Laboratory versus Co-Scientist**, with **50 manuscripts per condition**. Co-Scientist without its reliability modules scored **46%**. The full system had zero observed complete data fabrications in its 50-manuscript sample.

These are findings from that evaluation, not a universal error rate for agents. Multiple reliability mechanisms were involved, so the comparison does not isolate tracing alone or establish that fabrication is impossible. See [the study's design and results, Section 3.4](https://arxiv.org/html/2608.26701v1#S3.SS4).

### 6. Correct the claimed OpenTelemetry storage rule

The article's instruction to put content only in Events is not a universal OpenTelemetry requirement. Current GenAI semantic conventions explicitly allow input and output message content on spans. Storage design, indexing, redaction, retention, and payload limits determine the appropriate choice. See [the current GenAI span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md).

## Recommended next step

**Candidate for a later implementation decision:** pilot an Evaluation execution record and an input-currentness check on one existing validation command.

The candidate should demonstrate three observable outcomes:

1. A completion claim resolves to the actual command, tested input state, results, and artifacts.
2. A relevant input change makes the previous evidence insufficient to confirm the new state.
3. Missing execution evidence or a failed check prevents the result from being presented as verified success.

This is a small, testable step toward preventing unsupported completion claims. Replay and evaluated learning can build on the same records later. Selecting the command and checking for existing mechanisms should precede implementation.

## Unresolved evidence gaps

- The existing implementation coverage for execution records, input-currentness checks, and artifact dependency capture has not been audited.
- The first validation command and the complete set of inputs that determine its result have not been selected.
- The cost, retention needs, and practical benefit of the candidate have not been measured.
- This was a bounded review of the article's central ideas and selected claims; its other numerical thresholds and performance promises were not comprehensively verified.

## Sources and provenance

1. [Original X article](https://x.com/uncleshampoO/status/2099505399644684655), @uncleshampoO, published 2026-09-14; full article read through the browser on 2026-09-15.
2. [OpenTelemetry: Traces and span links](https://opentelemetry.io/docs/concepts/signals/traces/#span-links), official documentation; inspected 2026-09-15.
3. [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140), arXiv:2509.25140; version 2, revised 2026-03-16; inspected 2026-09-15.
4. [Accelerating Scientific Research with Gemini in the Real-World](https://arxiv.org/html/2608.26701v1#S3.SS4), arXiv:2608.26701v1, submitted 2026-08-27; study design and results inspected 2026-09-15.
5. [Anthropic: Claude glossary](https://platform.claude.com/docs/en/about-claude/glossary), official documentation on temperature and determinism; inspected 2026-09-15.
6. [OpenTelemetry GenAI span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md), official current repository documentation; inspected 2026-09-15. This branch URL is mutable; the finding is dated to the inspection.
7. [CAPRMEDIO README](../../../README.md), live project description used for the Evaluation/Ops distinction and framework context.
8. [CA-R-1426: Make engine execution observable and transparent](../../04_requirement/CA-R-1426-DEFINES_GOAL_FOR-FRAMEWORK_ENGINE--make-engine-execution-observable-and-transparent.md), version 1; read during persistence on 2026-09-15.

The source findings, CAPRMEDIO applications, and additional recommendations are distinguished above. No FPF analysis command was run for this assessment.
