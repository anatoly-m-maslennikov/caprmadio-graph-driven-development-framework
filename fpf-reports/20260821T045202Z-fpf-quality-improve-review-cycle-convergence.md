## Task, scope, and boundaries

### Loop contract

Task: improve the CAPRMEDIO FPF review workflow so that design challenge, repair, alignment, and verification converge instead of alternating indefinitely.

Receiving use: govern the next step for the current Intent-and-Principle review and provide a reusable termination protocol for later review campaigns.

Target: `CAPRMEDIO FPF review workflow v1`, evidenced by these two reports:

- [20260821T034644Z-fpf-alignment-audit-intent-and-principles.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260821T034644Z-fpf-alignment-audit-intent-and-principles.md)
- [20260821T043145Z-fpf-design-challenge-intent-principles-with-alignment-findings.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260821T043145Z-fpf-design-challenge-intent-principles-with-alignment-findings.md)

Current state: observed workflow defect. Two full reviews were run against the same unchanged semantic frontier. The second report repeated both blockers from the first report and found no third independent semantic concern.

Allowed change surface: the review method and its proposed campaign controls. This report does not alter CAPRMEDIO authority, either reviewed report, or the Intent-and-Principle proposal.

Saved report: [20260821T045202Z-fpf-quality-improve-review-cycle-convergence.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260821T045202Z-fpf-quality-improve-review-cycle-convergence.md)

Authority: the Operator decides whether to adopt and materialize the proposed workflow. This Analysis report is not normative authority.

### Evaluation frame

Evaluation name: `review-cycle-convergence-v1`.

| Coordinate | Passing condition |
| --- | --- |
| Phase correctness | Design challenge occurs before semantic acceptance or implementation; alignment occurs after an accepted change is applied. |
| Target-version discipline | No full evaluation reruns against an unchanged relevant target unless it uses an explicitly new evaluation profile. |
| Finding novelty | A known defect retains one fingerprint and one lifecycle instead of being recreated under a new report or skill. |
| Monotonic closure | A finding can move toward closure or explicit deferral without silently returning to an earlier state. |
| Defect-detection preservation | Mechanical, structural, and semantic failures remain detectable; convergence must not mean suppressing new evidence. |
| Review cost | Full reviews are run only when their distinct decision use justifies them. |

Protected trade-offs:

- do not hide real blockers merely to stop;
- preserve Operator authority over semantic decisions;
- preserve replayable evidence and target identity;
- permit a genuinely changed design to receive a new challenge;
- permit a genuinely implemented change to receive an alignment audit.

Refusal conditions:

- do not call the workflow improved merely because this proposal exists;
- do not close either current blocker without repair evidence;
- do not turn an out-of-scope observation into a silent expansion of the active campaign.

### Resolved FPF source

The resolved source is the split FPF Knowledge Graph in `/Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph`.

E.23 requires an exact target version, one rerunnable evaluation, a changed target between improvement claims, protected trade-offs, and explicit stop or switch conditions. E.11.PUA requires one useful result or one honest stop instead of accumulating review apparatus.

### Stop condition

This analysis stops when it identifies the observed cycle's cause, defines a bounded replacement workflow with enforceable transition guards, evaluates that workflow against the baseline coordinates, and gives the current campaign one unambiguous next action.

## High-confidence results (>=95%)

### Baseline evaluation

| Coordinate | Baseline result | Evidence |
| --- | --- | --- |
| Phase correctness | fail | The alignment report says its receiving use is to proceed to a design challenge. That reverses the intended order: challenge a proposal first, align accepted applied work afterward. |
| Target-version discipline | fail | The design challenge imported the alignment frontier unchanged, including the same hashes for CA-D-001 and both CA-R-860 carriers. |
| Finding novelty | fail | The second report repeated the two alignment blockers and found zero new independent semantic concerns. |
| Monotonic closure | partial | The alignment report has stable fingerprints, but no campaign gate prevented another full review from reopening them as challenge findings. |
| Defect-detection preservation | pass | Both reports retain the two real blockers and do not claim implementation. |
| Review cost | fail | The reports total 536 lines. The 241-line second report validated the repair direction but produced no new blocker. |

Baseline outcome: **regressed workflow efficiency with preserved defect detection**, confidence 100%.

### Root cause

The cycle is caused by treating design challenge and alignment audit as consecutive mandatory stages rather than different tools for different target states.

The observed invalid transition was:

`alignment of accepted carriers → unchanged target → design challenge`

No target change occurred between the two evaluations. Under the improvement-loop boundary, another full evaluation could not demonstrate target improvement. It could only restate, reinterpret, or widen the first evaluation.

Confidence: 100%.

### Bounded change hypothesis

Replace the open-ended alternation with one versioned Review Campaign and guarded state transitions.

Expected result: the same unchanged semantic frontier can receive at most one full design challenge and one full post-application alignment audit. Repairs discovered by alignment receive targeted closure verification, not another full design challenge, unless the repair changes semantic design.

Confidence that this prevents the observed cycle by construction: 99%.

### Proposed Review Campaign v2

#### Campaign identity

Each campaign records:

- `campaign_id`;
- `semantic_frontier`: the exact Intent, Principle, and other claim revisions whose meaning is under review;
- `carrier_frontier`: exact carrier paths, versions, and hashes;
- `evaluation_profile`: the complete declared checks and exclusions;
- `predecessor_report`;
- one shared finding registry;
- current phase and permitted next transitions.

The semantic frontier distinguishes meaning changes from mechanical carrier changes. The carrier frontier makes both kinds replayable.

#### Finding lifecycle

Every finding has one stable fingerprint and one lifecycle:

`OPEN → DECIDED → APPLIED → VERIFIED`

Alternative terminal dispositions:

- `DEFERRED`;
- `REJECTED`;
- `SUPERSEDED` by an explicitly named successor finding.

A report may add evidence or change status. It must not recreate the same defect under a new label merely because another skill observed it.

#### Phase gates

| Current state | Allowed full review | Allowed next action | Forbidden automatic transition |
| --- | --- | --- | --- |
| New or materially changed semantic proposal | one design challenge | Operator disposition and one consolidated repair batch | alignment before accepted changes are applied |
| Accepted semantic frontier with repairs not yet applied | none | apply the accepted batch | another design challenge |
| Accepted repairs applied | one alignment audit | close, or register exact blockers | design challenge merely because alignment found a defect |
| Mechanical or representation blocker | no full review | apply bounded repair and run its closure checks plus frozen regressions | restart the complete challenge/audit sequence |
| Semantic blocker with one consequence-preserving correction at accepted confidence | delta review of only the changed claim and affected neighborhood, if required by authority | apply once, then targeted closure verification | full-scope design challenge |
| Semantic blocker requiring a new decision | none automatically | return to Operator; a decision creates a new semantic frontier | autonomous review/fix recursion |
| Unchanged frontier and unchanged evaluation profile | none | stop | any full rerun |

#### Late-finding rule

If targeted closure verification encounters another issue:

1. If it is the same failure predicate, reopen the existing fingerprint; do not create a new finding.
2. If it is a different issue inside the frozen evaluation profile, mark the original evaluation `incomplete`, add the late finding to the same campaign, and stop automatic iteration for Operator disposition.
3. If it is outside the frozen evaluation profile, record a separate Concern or future campaign candidate. Do not expand the current closure pass.
4. Only a safety, authority, or data-loss blocker may interrupt these boundaries immediately.

This preserves detection without allowing every neighboring observation to restart the campaign.

#### Full-review budget

For one semantic frontier:

- at most one full design challenge;
- at most one full alignment audit after the accepted repair batch;
- any number of cheap deterministic closure checks when required, but no additional full review without a changed semantic frontier or a separately approved evaluation profile.

The limit is a routing rule, not a claim that two reviews guarantee completeness.

### Current campaign disposition

The current campaign is already past design challenge and alignment discovery. Its next step is not another review.

The only current actions are:

1. Apply `BL-D001-OBLIGATION-ASSERTION`.
2. Apply `BL-R860-DUPLICATE-ATOM-ID`.
3. Run targeted closure checks for those two fingerprints and the frozen regression checks already named by the alignment report.
4. Close the campaign if both pass.

Another full design challenge is allowed only if either repair changes the accepted Principle meaning. Another full alignment audit is unnecessary if the targeted closure verification reuses the complete frozen regression matrix; if project policy requires a named alignment artifact, run it explicitly in `closure` mode and forbid new scope.

Confidence: 100%.

### Implementation evidence

No normative review-method carrier or skill was changed. The proposed v2 workflow exists only in this Analysis report.

Therefore, activity is demonstrated, but adoption and operational improvement are not.

### Re-evaluation of the proposed method

| Coordinate | Baseline | Proposed v2 | Demonstrated status |
| --- | --- | --- | --- |
| Phase correctness | fail | guarded design-before-application and alignment-after-application order | improved by design; not operationally demonstrated |
| Target-version discipline | fail | unchanged frontier forbids a full rerun | improved by design; not operationally demonstrated |
| Finding novelty | fail | one shared fingerprint registry across skills | improved by design; not operationally demonstrated |
| Monotonic closure | partial | explicit finding and campaign state machines | improved by design; not operationally demonstrated |
| Defect-detection preservation | pass | preserved through frozen checks and late-finding rule | protected by design |
| Review cost | fail | removes the redundant full review in the observed scenario | expected reduction of one 241-line full report; not operationally demonstrated |

### Trade-offs, costs, risks, and uncertainty

- A strict review budget can miss a real issue if the initial evaluation profile is weak. Mitigation: freeze a complete check matrix before the full review and treat an in-profile late finding as evaluation incompleteness, not permission for silent recursion.
- Delta review is cheaper but can miss distant semantic impact. Mitigation: include the changed claim's active parents, children, same-scope peers, and Principles in its affected neighborhood.
- Semantic-frontier identity requires judgment when prose changes without changing meaning. Mitigation: record both semantic disposition and exact carrier hashes; when uncertain, treat the semantic frontier as changed.
- The workflow adds a small campaign record and status discipline. This cost is materially lower than repeated full reports and repeated Operator decisions.

### Outcome and decision

Outcome: **not demonstrated**, because the workflow proposal has not been adopted or run on a later campaign.

The diagnosis and replacement method are nevertheless supported at 99% within the two-report evidence.

Decision for the current campaign: **stop reviewing, apply the two registered repairs, then verify closure only**.

Continue only to materialize the review-campaign method or apply the two existing repairs.

Rollback is not applicable because no target authority changed.

Switch method if a closure check finds a genuinely new in-profile blocker: stop automatic work, mark the evaluation incomplete, and return the consolidated campaign to the Operator rather than alternating skills again.

## Open questions (confidence <95%)

### Where should Review Campaign v2 be governed?

Best current answer: put the generic campaign and finding-lifecycle semantics in the Bootstrap Seed layers, and put CAPRMEDIO's concrete FPF skill-routing procedure in Project Method authority.

Confidence: 93%.

Missing decision: the exact ownership boundary and carrier identities.

Consequence: the protocol is usable now as an operating rule but is not yet durable project authority.

Next action: decide ownership before creating or updating Atoms; this does not block applying the two current repairs.

### How should semantic-frontier identity be encoded?

Best current answer: use an exact carrier frontier plus an explicit `semantic_change: true|false` disposition, because hashes alone cannot tell whether a wording change altered meaning.

Confidence: 92%.

Missing decision: canonical field names, carrier form, and whether an existing Map can hold the campaign record.

Consequence: an automated guard cannot yet distinguish every mechanical edit from a semantic change.

Next action: define the smallest executable campaign schema when the review method is materialized.

## Skills used

- `fpf-quality-improve` — evaluated the observed two-report review cycle, proposed a bounded replacement workflow, compared it with the baseline, and preserved the distinction between proposal and demonstrated improvement.

#### FPF sources consulted (2 read; 2 used)

- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_Practical-Use Guidance and Pattern Discovery/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md` — **used**: required one useful result and an explicit stop instead of accumulating review state.
- `FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/22_23_Quality Improvement Loop Method/00_E.23 - Quality Improvement Loop Method.md` — **used**: required a versioned target, rerunnable evaluation, target change before improvement claims, protected trade-offs, and stop or switch conditions.
