---
atom_id: CA-P-1130
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 6
updated_at: "2026-10-04 14:44:51 +0000"
relations:
  is_decomposition_of:
    - CA-P-1119
  blocks:
    - CA-P-1156
    - CA-P-1131
---
# Summary

Reconcile candidates with current authority

## Objective

The assigned AI Agent must complete one bounded work packet for reconcile candidates with current authority, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Select at most five candidates from completed saved harvest Analysis outputs admitted by CA-P-1117. No additional native-session harvesting is required. CA-A-1043 is partial and excluded from admitted completion. Read the candidates' active Project and methodology sources, including current terminology for Workflows, Actions, and Steps. Latest explicit Operator input wins over older input; higher Principles remain governing. Cross-map older active harvest/migration Plans instead of duplicating their work.

### Required output

A decision-to-existing/new-Operation mapping with source revisions, semantic deduplication, required RMED ownership, accepted disposition, and linked Concerns. Assign reusable, project-independent Operations to CORE_META_MODEL and caprmedio-specific Operations to PROJECT_CONFIGURATION, with exact source carriers and a destination rationale. Split the remainder into additional leaves which block authoring of their corresponding operations.

### Bound first execution packet and retained remainder

CA-P-1155 binds CA-P-1340 at `01-CA-P-1130-TASK--reconcile-candidates-with-current-authority/02-CA-P-1340-TASK--reconcile-the-source-reconciliation-candidate.md`: one Source Reconciliation family from completed CA-A-924 C02 / D03–D04, compared with the full current authoritative CORE_META_MODEL source Workflows CA-O-010 v7 and CA-O-011 v10. Its reserved output is `.caprmedio_caprmedio/02_analysis/CA-A-1058-ANALYSIS_RPRT--reconcile-the-source-reconciliation-candidate.md`. It decides reuse, actual gap and exact destination; it does not author Operations, run a Workflow, collect native sessions or create a duplicate Workflow. Exact carrier paths, ownership, independent verification and the <=15-minute estimate are carried by CA-P-1340.

CA-P-1341–CA-P-1344 are the four separately bound candidate-family remainder children, with outputs CA-A-1059–CA-A-1062. CA-P-1345 under CA-P-1119 consolidates completed saved candidate sections to expose additional unique families without native harvesting. All five initial families are a bounded selection, not proof that the admitted 102-packet / 5,463-record corpus has been reconciled. Additional unique families exposed by that consolidation require explicit bound leaves and disposition before this parent closes.

### Current saved results and remaining families

CA-P-1340–CA-P-1346 are Done. CA-A-1058–CA-A-1064 retain their actual decisions and evidence; the initial source comparisons reuse O010/O011, O051/O058/O067, O052 and O065. CA-C-350, CA-C-353 and CA-C-354 bind four source-Carrier layout repairs, not semantic Operation changes. CA-A-1064 accepts one optional CORE_META_MODEL completed-Plan handoff assessment Action, reusing current completion authority, Workflow handoffs and O079's editing mechanism. Authoring and independent source review remain unperformed.

The completed CA-A-1063 register admits 102 completed harvest reports and three metadata reports. Its 466 entry forms are exact saved references, not 466 unique Operations; 29 repeated forms are represented by retained links, eight initial inputs were bound above and 429 other forms require disposition. Its 21 provisional families are an organizing aid, not source authority. F02 is covered by CA-A-1058. CA-P-1347–CA-P-1366 bind the other twenty families in register order, with CA-A-1065–CA-A-1084 as reserved outputs. Each child must preserve every exact assigned entry reference while coalescing repeated intents, and must create a narrower child/remainder if its actual comparison cannot fit <=15 minutes. Required child Plans must be saved with concrete inputs before execution.

These comparisons use saved candidate/refinement sections and current authoritative Operations. An exact already-saved supporting context excerpt may clarify an already bound candidate intent; for example, the retained FPF report's MM09–12/FX07–09 passages may support the corresponding F20 comparison. This is historical supporting evidence, not current adoption, new candidates or additional harvested coverage. They do not resume native-session harvesting, mine embedded raw session records for additional candidates, redesign the ontology, or mistake historical assistant reports for present implementation proof. Each complete intent receives covered, adopted-gap, rejected or non-operational disposition; non-operational historical RMED material is identified rather than converted into a duplicate Workflow. Only an accepted executable contribution justifies source Operation authoring, with its exact CORE_META_MODEL or PROJECT_CONFIGURATION destination. Parent authoring gates remain blocked until required family reconciliation is complete; root will bind authoring from actual accepted outputs, not from register membership alone.

Readiness remains gated: CA-P-1155 BLOCKS CA-P-1340; CA-P-1340–CA-P-1344 each BLOCK CA-P-1131 and CA-P-1156; this parent retains its own BLOCKS edges to both. The separate CA-P-1345 gate also remains. Closing the preflight or first family must not unlock authoring while any required reconciliation remainder or independent verification is unfinished. CA-P-1131 / CA-P-1156 were reviewed as still Active and blocked; no edits to their Claims or sources are authorized here.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

### Completed reconciliation and downstream handoff

The single completion check found all 58 nested Plan carriers physically Done, including all 37 direct children, twenty family rollups and seven independent whole-family reviews; the initial five comparisons, CA-P-1346 and the separate CA-P-1345 / CA-P-1155 gates are also Done. Their existing accepted results complete the CA-A-1063 register: 466 exact entry forms comprise 29 represented forms, eight initial inputs and 429 remainder dispositions. CA-A-1058–CA-A-1087 and the completed family/review results retain membership, coalesced dispositions, qualifiers and typed Concerns. This closure adds no candidates, harvesting, repeated semantic review or implementation claim.

Five optional new CORE_META_MODEL Actions are accepted for downstream authoring: CA-A-1064's completed-work handoff assessment; CA-A-1085's evaluator calibration and legacy-evidence/provisional-RMED preparation; CA-A-1086's read-only scoped-choice applicability assessment; and CA-A-1087 v2's single coalesced F07/F08/F10 prepared-result conformance assessment. Their independent narrowed verdicts remain binding. None grants approval, adoption, release, mutation, automatic repair/recheck or Workflow-invocation authority.

Retained source-Carrier repairs, including CA-C-350, CA-C-353, CA-C-354 and CA-C-376, remain downstream obligations with their saved dispositions, not silently resolved by reconciliation. CA-P-1131 v3 and CA-P-1156 must bind the actual accepted Action/source-repair packet; the layout-only allowance is at most four existing Operations plus the identified CA-M-301 supporting-heading repair, preserving Summary, meaning and Version, followed by the existing independent source-review gates. Retained Engine/RMED/runtime gaps and their typed Concerns remain attached to the completed family outputs and pass to CA-P-1120 / CA-P-1121 specification and review, then CA-P-1122 implementation, CA-P-1123 complete Docker verification and CA-P-1124 final traceability. Those stages are not completed by this handoff.

CA-P-1131 v3 and CA-P-1156 v1 were reviewed against the completed result; their current frontier, exact-packet binding and remainder duties need no further gate-detail amendment here. The existing BLOCKS relations and literal Definition of Done are retained. Only this completed parent carrier and its matching bundle move together to CA-P-1119's `done/`; descendant bytes, identities and relations remain unchanged. Earlier child path locators are historical and now resolve beneath that relocated bundle.

## Details

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
