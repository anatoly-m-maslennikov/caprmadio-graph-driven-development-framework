---
subjects:
  governs: "Apply Approved Source Corrections"
  depends_on:
    - "Action"
    - "Operator"
    - "AI Agent"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Relation"
    - "Atom/Content Role: Evaluation"
    - "Framework Instance Settings"
    - "Project Settings"
version: 11
updated_at: "2026-09-28 06:30:40 +0400"
relations: {}
atom_id: "CA-O-008"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-008-CORE_META_MODEL-ACTION--apply-approved-source-corrections.md
---
# Apply approved source corrections

Apply Approved Source Corrections **means** the reusable Action that applies **only** the exact upstream corrections authorized for the current proposal, conflict, **and** source frontier.

1. **before** mutation, revalidate the actual Operator authorization **and** relevant current source state. authorization **may** be an explicit decision recorded under CA-O-007 **or** an active Operator delegation that covers **every** proposed action, subject **to** CA-R-1551 **and** the calling Workflow's stricter approval requirements. missing, rejected, stale, partial, ambiguous, **or** mismatched authorization blocks mutation.
2. apply the authorized correction through the owning source's governed change workflow. resulting Claims remain **in** their owning source Atoms; resulting selections remain **in** their owning settings. compilation **and** an approval record do **not** themselves grant source-change authority.
3. for archival, verify CA-O-006's coverage conditions against live sources, complete prerequisite repairs, **and** preserve the predecessor under CA-O-051: retain its body, Summary, identity, Version, and all metadata except archived Status and archive-time Updated At. apply replacement **or** absorption recording under CA-R-807 **when** applicable; a withdrawn obsolete Claim does **not** require an invented successor.
4. record actual execution, changes, failures, **and** partial effects **in** the Journal. report the resulting source frontier **or** exact failure; a Journal record describes those effects **without** replacing current source authority.
5. return changed sources for renewed selection, conflict assessment, Principle alignment, **and** affected coverage checks. do **not** report completion **until** required checks confirm no remaining conflict **or** coverage gap **in** the affected authority.

this Action **must not** edit projected Claims as a conflict fix, infer additional corrections, create a duplicate approval Atom, **or** claim completion **after** a failed correction. retries **and** recovery require their applicable accepted authority **and** bounds; this Action does **not** authorize automatic rollback **or** unbounded repetition.
