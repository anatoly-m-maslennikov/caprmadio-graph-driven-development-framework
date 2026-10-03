---
atom_id: CA-P-966
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - "Applicable Methodology Compilation"
  depends_on:
    continuant:
      - "Core Meta-Model"
      - "Applicable Methodology/Sources"
      - "Atom/Content Role"
      - "Atom/Claim"
      - "Atom/Claim/Scope"
      - "Atom/Revision"
      - "Carrier/Canonical Address"
      - "Confidence Threshold"
version: 1
updated_at: "2026-09-11 02:58:19 +0400"
relations: {}
---
# Inventory existing compilation RMED authority

the Assignee **must** produce a current coverage **and** gap inventory of the RMED authority for Applicable Methodology compilation **in** CORE_META_MODEL.

## Scope

(active RMED authority for Applicable Methodology compilation **in** CORE_META_MODEL)

## Definition of Done

the Task is **not** Done **if** ((an in-scope Atom lacks its exact identity, Version, Carrier path, **or** content digest) **or** (an in-scope Claim lacks a reuse, update, replacement, retirement, **or** justified retention disposition) **or** (a required compilation responsibility lacks an existing authority owner **or** an explicit gap) **or** (a proposed addition duplicates an existing Claim) **or** (this inventory Task changes a source Atom)).

## Details

cover source admission **and** inclusion, source identity **and** Claim preservation, generic compilation, conflict detection, Operator approval, source-level correction, Evaluation coverage, **and** Projection placement **and** representation. keep the role boundary explicit: required outcomes (R), reusable work procedures (M), falsifiable checks (E), **and** Carriers (D).

start from the current CORE_META_MODEL Carriers for CA-R-1434, CA-R-1228, CA-R-1314 through CA-R-1317, CA-R-1375, CA-M-224, CA-E-379, CA-D-253, CA-D-305, CA-D-306, **and** CA-D-313. these are discovery seeds, **not** a complete inventory **or** frozen revision list. resolve identities within CORE_META_MODEL by exact Carrier path **and** Revision; report ambiguity rather than choosing a global ID match. CA-R-1224 **and** CA-R-1225 are preserved historical restrictions, **not** active input authority.

record which remaining work belongs to the R, M, D, **and** E Tasks. this Task does **not** install Extensions, change current Settings, rewrite Local Configuration contents, migrate source folders, implement Tools, rebuild APPLICABLE_METHODOLOGY, normalize unrelated Atoms, **or** repair the Project-wide ID collisions. read governing Project Principles as prerequisites, **not** as edit targets.
