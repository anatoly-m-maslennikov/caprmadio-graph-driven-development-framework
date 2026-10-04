---
atom_id: CA-O-029
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Archive Selected Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_ARCHIVE"
    - "Atom"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 4
updated_at: "2026-10-04 17:40:59 +0000"
relations: {}
---
# Summary

Archive selected active Atoms

## Operation

Archive Selected Active Atoms **means** the reusable Action that withdraws the selected active Atom authority as **`=1`** all-or-nothing archive transaction while preserving its governed meaning **and** recoverable historical Carriers. its modeled boundary is that withdrawal transaction: a partially archived selected set is **not** a useful independently successful outcome.

### Applicable conditions

- select **`=1`** active Atom **or** a frozen bulk set of **`>=2`** active Atoms.
- actual archival requires an authorized Project-local MCP delegation with a sealed Initiative action envelope. a preview grants no apply authority.
- preserve the Atom ID, Version, content, Summary, prior history, **and** resolvable historical dependents. derive the archive location **and** basename from the applicable Delivery authority under CA-D-289 **and** CA-D-303; preserved meaning **and** history do **not** require unchanged lifecycle metadata **or** active basename.

### Action

1. resolve **every** selected Atom uniquely, establish its active classification **and** owning Content Role/Type, **and** retain its exact path, ID, Version, Status, Updated At, digest, **and** historical references as preconditions. resolve the applicable Atom status model **and** authorization/transition conditions under CA-R-1521; require its admitted Archived transition. missing **or** unsupported models block **or** report the unsupported capability, **not** an invented universal lifecycle. this Tool is the archive shortcut used by Change Status, **not** another generic Status Workflow.
2. derive **`=1`** role-local archive destination per target using the required `@<version>` suffix. reject Drafts, already archived Carriers, non-Atoms, invalid destinations, collisions, repeated targets, **and** stale targets.
3. freeze the complete source-to-destination map **and** return its mutation-free dry run.
4. on explicit authorized `--apply`, recheck **every** source **and** destination precondition. archive each whole Carrier with its admitted lifecycle `status: Archived` **and** actual archive-time `updated_at` under CA-R-1788/CA-R-1371, preserving body, Summary, ID, Version, **and** **all** other frontmatter values. publish the complete selected set as **`=1`** rollbackable transaction **and** exclude it from current-authority discovery.
5. verify unchanged body, Summary, ID, Version, **and** other preserved metadata/history; independently verify **only** the admitted lifecycle Status/actual Updated At differences, correct @<version> archive basename, absence from active locations, **and** retained historical resolution. do **not** demand an unchanged full-file digest after an admitted Status/time edit. failed preflight still leaves **all** bytes unchanged.
6. **if** an effect **or** postcondition fails, restore **every** selected mutable source **and** destination **to** its before-state; preserve unrelated Carriers **and** immutable accepted Journal evidence. report the failed attempt **and** recovery result rather than archive success.

### Outcome

successful apply requires the complete selected set archived under its applicable model, historically resolvable **and** absent from current authority. mutation-free preview is prepared; deferred/not-applied, rejected **or** a genuine no-op is **not** an invented archive effect. remain **in** dry-run mode **without** delegated apply authority. stop **or** attempt restoration of the full mutable set on a failed lifecycle, source, destination, collision, **or** postcondition check; report failed/partial/unknown actual effects **and** recovery evidence. incomplete **or** unverified restoration is **not** successful recovery. missing shared Run persistence retains actual archive effects **and** the recording blocker, without a blind repeated archive.

## Details

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
