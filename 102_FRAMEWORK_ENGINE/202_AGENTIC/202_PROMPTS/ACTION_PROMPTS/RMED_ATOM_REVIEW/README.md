# RMED Atom Review

**gather scope → check selected Atoms → fix confirmed local issues**

Methodology O Atoms own the Workflow, Actions, and Steps. Their prompt
Implementation is governed by PROMPTS RMED in the existing
`202_FEATURE_PROMPTS` authority folder:

- R: CA-R-1801 (complete local review capability), CA-R-1802 (truthful completion).
- M: CA-M-317 (semantic assessment separate from heading recognition).
- E: CA-E-524 (golden implementation scenarios, distinct from methodology checks).
- D: CA-D-509 (prompt package), CA-D-510 (coverage/correction report encoding).
- Run evidence: CA-R-1803 and CA-D-511 (shared Journal and full Markdown report).

`source_bindings.json` records their exact source paths, Versions, and digests.
These are implementation specifications, not additional workflow stages.

1. [Gather scope](CA-O-108.prompt.md): save the selected Atom list and collect
   shared checking rules once. No reviewer dispatch in this step.
2. [Check](CA-O-109.prompt.md): give each Atom and relevant rules to one fresh
   Terra/high reviewer. Save one report per Atom.
3. [Fix](CA-O-110.prompt.md): give each fixer its Atom, its own findings, and
   applicable editing rules. Record the changes in the same report.

Complete all six checks for an Atom before its normal fix phase. Independent
Atoms may progress in parallel. Safe partial fixes for a genuinely blocked Atom
do not complete it.
The caller coordinates dispatch and keeps one short progress list in
`progress.json`. Workers return their own result; they do not load or rewrite
other workers' reports.

## Checks and results

The six checks are properties, local CCE, one Scope, one Claim, Details
expansion, and faithful Summary. Reports contain those outcomes and actual
defect quotes or observed absences, rule references, confidence, and proposed
fixes. Exclude graphs, Entity completeness, classification, and cross-Atom
comparisons.

Missing or misplaced headings are Properties defects, not an automatic reason
to skip content checks. Read the whole text and quote actual passages; explain
their semantic function without inventing Property sections. Genuine ambiguity
or missing evidence blocks only affected checks. Resume unfinished checks within
the check step; do not introduce a saved-output recheck.

Within the Claim check, apply CA-R-1799: capability requirements do not authorize
execution. Direct Operator instruction or explicit prior authorization can
cover Workflows and automations. Keep their mandatory behavior and safeguards;
`must` or missing repeated approval alone is not a violation. Unknown intent
or an unspecified target stays unresolved. The fixer changes meaning only
when authorized and retires an Atom only with explicit authority. This adds
no seventh check or review stage.

- `checked_clean`: all six checks passed.
- `issues`: all six checks concluded; confirmed findings need fixes.
- `fixed_not_rechecked`: all six initial checks concluded and findings were
  corrected or explicitly rejected with reasons; output was not reviewed again.
- `blocked`: state the missing input, authority, capacity, or decision.

Preserve initial check outcomes, blockers, and actual corrections separately.
Applying an edit does not resolve skipped checks. `workflow_progress.py` counts
reports received, checks completed, and Atoms completed separately. Any unfinished
check or unresolved finding keeps the Atom and the selected run incomplete.
This is report bookkeeping, not another evaluation gate or a semantic verdict.
Old frozen criteria/reports remain historical; new dispatches use current rules.

There is no recheck loop or additional review gate.

## Implemented Run recording

`workflow_evidence.py` implements durable Run recording around those same three
steps. `workflow_progress.py` requires a disposition for every finding; missing,
unknown, or conflicting references cannot produce completion. Fix blockers do
not erase initial check coverage. The fixer retains all initial evidence.

- Full reports: `tmp/RMED Atoms Base Revise/<workflow_run_id>.md`.
- Internal recovery state: `.caprmedio_tmp/rmed-base-revise/<workflow_run_id>/progress.json`.
- Per-Atom reports: `reports/0001.json`, etc., below that recovery directory.
- Execution events: the existing configured Project Journal, with the same Run
  ID and report path. No separate Workflow Journal. Schema-v4 execution records
  coexist with the existing v2/v3 Artifact-change records.

The caller supplies identity/session/scope, current criteria paths, selection,
and actual check/fix results. Fix context checks both source and criteria
bindings before work. Report assembly does not re-evaluate Atoms. `sync` only
retries evidence writes; sealed Event IDs make Journal retries idempotent.
`recording_blockers` remains distinct from the saved work outcome. A failure to
write the recovery state is a Tool error, not a success acknowledgement.

The initial local adapter is in `201_PROGRAMMATIC/204_MCP/server.py` relative to
FRAMEWORK_ENGINE; it delegates to the `RMED_ATOMS_BASE_REVISE` Tool. It returns
prompts and accepts results. The calling session performs scope gathering,
launches reviewers/fixers, and grants permission for any Atom edits. MCP does not
launch Agents, execute arbitrary commands, or edit source Atoms. It is not
installed in any host by this implementation change.

## Context and continuation

The caller resolves `rmed_review.context_headroom_fraction` from actual
settings; do not hard-code a fallback in prompts. Hand off at the configured
threshold, preserving completed work and remaining work. A short same-stage
handoff resumes in a fresh agent without replaying edits. Distinguish measured
context usage from estimates; an input that cannot fit is blocked, not truncated.

## Existing tools

The existing evaluator prompts provide optional reference material for checking
criteria. Their report contracts, repair helpers, and historical gates are not
part of this default workflow. Historical records are not erased, relabeled,
or implicitly invoked.
