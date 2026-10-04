---
atom_id: CA-O-031
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Validate And Describe Atom Replacement"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Journal/Record"
version: 4
updated_at: "2026-10-04 17:40:59 +0000"
relations: {}
---
# Summary

Validate and describe one Atom replacement

## Operation

Validate And Describe Atom Replacement **means** the reusable Action that validates **and** seals explicit replacement intent for its admitted lifecycle effect under CA-R-1041. its boundary is **`=1`** exact predecessor-to-successor-set intent, **or** the approved frozen bulk set of those intents; it does **not** own generic creation, Relation editing, **or** archival behavior.

### Action

1. resolve **`=1`** exact active predecessor Atom ID **and** **`>=1`** distinct exact already-active successor Atom IDs per mapping. reject missing, unresolved, inactive, duplicate, **or** self-referential IDs. validate the complete frozen mapping set for a bulk request **without** reducing a successor set **to** a single pair.
2. preserve the sealed Initiative action context, exact mappings, **and** approved atomic boundary. return a structured replacement action naming **every** supplied successor **and** the predecessor archive intent. do **not** infer a successor, replacement Relation, **or** generic Carrier behavior.
3. for dry run, return that exact description **without** applying, promoting, **or** archiving a Carrier.
4. accept `--apply` **only** through authorized Project-local MCP delegation carried by the sealed Initiative envelope. revalidate the selected active identities **and** complete admitted boundary **before** requesting the canonical lifecycle effect.
5. delegate the admitted replacement transition **to** CA-O-051 under CA-R-807: establish **all** explicitly supplied successors Active **before** predecessor archival, preserve the predecessor as a whole Carrier with only its admitted lifecycle Status/actual Updated At changes **and** canonical @<version> basename, **and** obtain the authoritative predecessor-archive replacement event naming the predecessor **and** complete **`>=1`** already-active successor set. pass **every** frozen mapping within the approved all-or-nothing boundary; do **not** collapse multi-successor replacement into one pair. preserve body, Summary, identity, Version, other metadata **and** immutable history; keep replacement history out of Atom frontmatter. do **not** independently implement creation, Relation patching, archival, **or** the Journal.
6. obtain durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports successful completion. preserve the delegated lifecycle result/effect evidence, canonical replacement-event receipt, shared Action Run recording state, **and** actual intake receipt as distinct facts. intake acceptance alone proves neither applied replacement, completed Run journaling, **nor** a Git Commit. absent intake **or** Run persistence is a reported blocker with pending evidence retained, **not** successful completion **or** authority for blind repetition of an effect whose outcome needs reconciliation.

REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit. rejected requests retain their evidence **without** creating a replacement Relation **in** current Atom Carriers.

### Outcome

Return prepared for mutation-free description; deferred/not-applied **when** no lifecycle effect has been performed; rejected for failed admission; **and** applied **only** with the complete approved successor/predecessor postconditions **and** their actual evidence. report failed, partial **or** unknown delegated effects **and** verified/unverified recovery separately. no-op has no invented predecessor transition. reconciliation preserves actual effects **and** accepted history, checks current authority/frozen inputs, **and** retries receipt/intake recording without replaying replacement; a new effect attempt needs separately admitted authorization **and** its own Run binding. interrupted ongoing work remains pending rather than an invented terminal. neither a prepared result **nor** an intake/Run acknowledgment upgrades an unperformed effect **to** applied.

## Details

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
