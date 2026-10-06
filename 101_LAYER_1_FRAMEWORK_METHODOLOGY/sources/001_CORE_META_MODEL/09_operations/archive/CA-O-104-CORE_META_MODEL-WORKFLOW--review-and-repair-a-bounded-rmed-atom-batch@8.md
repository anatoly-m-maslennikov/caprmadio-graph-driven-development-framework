---
atom_id: CA-O-104
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: "2026-10-04 02:57:00 +0400"
subjects:
  governs: "RMED Atom Review Workflow"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Workflow/Relation Kind: On Result"
    - "Atom"
    - "Journal"
    - "Journal/Record"
    - "Evaluation/Report"
relations: {"relates_to":["CA-D-340","CA-O-108","CA-O-109","CA-O-110","CA-R-1643","CA-R-1720"]}
---
# Summary

Review and repair a bounded RMED Atom batch

## Operation

RMED Atom Review Workflow **means** the graph with these **`=3`** Steps:

1. gather the requested scope of active RMED Atoms through CA-O-108.
2. check the selected Atoms through CA-O-109.
3. fix confirmed issues through CA-O-110.

each main Step has **`=1`** result-coverage substep invoking CA-O-118: CA-O-119 **after** gather, CA-O-120 **after** check, CA-O-121 **after** fix. these Coverage Gates inspect execution evidence, **not** Atom correctness. **only** coverage **`=100`** percent permits the next main Step **or** completion; incomplete **or** unknown coverage interrupts the Run **and** asks the Operator with the missing work. no automatic repair retry **or** reduced selection follows a failed gate.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-108 | ready | CA-O-109 |
| CA-O-108 | empty | completed |
| CA-O-108 | blocked | blocked |
| CA-O-109 | checked_clean | completed |
| CA-O-109 | issues | CA-O-110 |
| CA-O-109 | blocked | blocked |
| CA-O-110 | fixed_not_rechecked | completed |
| CA-O-110 | blocked | blocked |

the review profile is `atom_local`: **`=1`** Scope, **`=1`** Claim with faithful Summary **and** explanatory Details, intact carried Properties, **and** current CCE alignment. Entity-model correction, Subject completeness, relation-target resolution, duplicate detection, **and** cross-Atom alignment are outside this Run.

## Details

the caller gives **`=1`** Atom **to** a fresh Isolated reviewer. independent assignments **may** run **in** parallel. supply the actual Atom **and** the relevant local checking rules; keep **`=1`** report per Atom **and** **`=1`** progress list for the original selection.

this Workflow has no proposal-review stage, saved-Atom recheck, **or** fix-and-recheck loop. Coverage Gates review the completeness of saved execution evidence **only**. `checked_clean` records a passing check; `fixed_not_rechecked` records applied corrections **without** asserting a post-fix pass. another review requires a separately requested Run.

continue **until** the original selection is handled **or** a genuine blocker requires the Operator:

- at the configured context threshold, save a short handoff naming the current Atom, unfinished Step, completed edits, **and** next work; automatically continue **in** a fresh subagent.
- preserve completed work **and** resume **only** unfinished work. a context handoff consumes no repair retry.
- **when** slots are occupied, wait for a worker **to** finish. retain actual spawn failures **and** unresolved permission **or** confidence questions as blockers.
- a completed subset does **not** complete the original selection.

completion requires **all** **`=6`** initial checks **to** conclude **and** **all** confirmed findings **to** be corrected **or** rejected with recorded reasons. an applied edit does **not** complete an unfinished check. count reports received, check completion, **and** Atom completion separately; unresolved coverage **or** findings keep the Atom **and** Run incomplete. independent Atoms **may** progress from checking **to** fixing **in** parallel.

### Run evidence

- at the start of an Operator-authorized Run, bind its Workflow name, Run ID, full report location, **and** shared Project Journal. retain the same Run ID through **all** Steps **and** context handoffs.
- record the Run's start, Step outcomes, handoffs, **and** terminal outcome **in** the shared Journal using the admitted Event Types under CA-R-1643-CORE_META_MODEL-GENERAL-REQUIREMENT--register-type-values-for-work-journal-events **and** the registered Event Carrier. include the Run ID **and** full report reference **in** the recorded context. this is the existing Project Journal, **not** a new per-Workflow Journal.
- assemble the full report from the original selection **and** saved per-Atom evidence **after** gathering, **after** received check **or** fix results, **and** at handoff **or** termination. include clean, fixed, blocked, **and** pending Atoms; retain initial findings separately from their dispositions. an empty selection **or** early blocker still has a Run report.
- record Completed **only** for a completed selection, Interrupted for a Run awaiting Operator input, **and** Failed for an execution failure. context continuation **in** another subagent retains the current Run rather than inventing a completed Run.
- retain actual report-write **or** Journal-append failures as evidence-recording blockers. distinguish them from the saved Atom outcomes, report the incomplete Run record, **and** preserve applied edits **without** replaying them. an unconfirmed Journal append is **not** a recorded Event.

Run evidence includes Coverage Gate inputs, expected work, covered work, missing work **and** outcome. coverage reviewers add substeps to the existing **`=3`** main Steps, **not** saved-output rechecks **or** another source of event authority.
