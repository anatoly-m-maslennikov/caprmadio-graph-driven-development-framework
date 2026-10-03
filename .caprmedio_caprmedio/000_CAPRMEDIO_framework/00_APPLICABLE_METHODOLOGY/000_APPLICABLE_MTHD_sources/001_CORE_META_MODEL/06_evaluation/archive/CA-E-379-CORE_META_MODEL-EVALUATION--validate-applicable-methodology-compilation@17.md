---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Applicable Methodology Compilation"
  depends_on:
    - "Applicable Methodology"
    - "Applicable Methodology/Sources"
    - "Project Configuration"
    - "Extension"
    - "Framework Instance Settings"
    - "Methodology Source/Expansion Boundary"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Operator"
    - "Journal/Record"
version: 17
updated_at: "2026-09-23 23:28:07 +0000"
relations:
  evaluation_for:
    - CA-D-305
    - CA-O-007
    - CA-O-008
    - CA-R-1317
    - CA-O-011
    - CA-R-1228
    - CA-R-1375
    - CA-R-1434
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Applicable Methodology Compilation

the Applicable Methodology Compilation Validation **must not** pass **if** **any** of:

- CORE_META_MODEL, PROJECT_CONFIGURATION, **or** an applicable installed Extension Source under CA-R-1228 is omitted; an unselected **or** inactive Extension revision contributes.
- an eligible current active source Atom under CA-R-1315 is omitted, **or** an ineligible Atom Revision contributes.
- compilation requires a hard-coded Extension name **or** particular Project-specific Project Configuration contents, rejects a conforming source merely because its contents are new, **or** requires an empty INSTALLED_EXTENSIONS Carrier **when** no Extension is applicable.
- a selected Atom ID, exact source Revision, authority owner, **or** Claim changes; Claims are synthesized **or** merged; a projected member loses its required source traceability **or** Carrier form.
- the `projection.source_carrier_path` binding required by CA-D-305 is missing, malformed, ambiguous, **or** resolves anywhere other than the selected original source Atom Carrier; it is resolved from the repository root rather than the projected file's directory.
- removing **only** the generated binding does **not** restore the exact selected source bytes; Atom ID, Version, authored Frontmatter, **or** Main Content disagrees with the selected Revision; a changed source is accepted as current **without** regeneration.
- the binding is copied **to** source authority, treated as another Atom identity, **or** duplicated as an inverse source-to-projection Atom Relation.
- the conflict report omits a Core expansion-boundary violation, duplicate Atom identity, unresolved replacement, incompatible retained Candidate, **or** unresolved priority; source Atoms are silently discarded **to** hide a conflict.
- a conflict is resolved **without** an unambiguous actual Operator approval recorded **in** the Journal under CA-O-007 **and** bound **to** the exact proposal, conflict, **and** source-frontier digest; an approval is stale, partial, missing, ambiguous, **or** mismatched; a prohibited Extension **or** Project Configuration override is accepted as conforming.
- source order **or** LLM inference resolves a conflict, projected Claims are directly corrected, **or** the same resolved source frontier produces different Applicable Methodology membership.

the Evaluation **must** cover an empty Extension contribution, a newly installed conforming Extension with a previously unknown name, changed conforming Project Configuration contents, **and** an expansion that violates Core authority. conforming input changes **must not** require edits **to** generic Core compilation rules merely **to** recognize their names **or** contents.

check the decision **and** correction boundary:

- a valid actual approval recorded **in** the Journal **must not** require a separate approval Atom **in** Project Configuration.
- a copied approval Claim, an inferred decision, **or** a Journal record **without** evidence of the actual applicable Operator decision **must not** qualify as approval.
- approved source corrections **must** run through CA-O-008, preserve current rules **and** selections **in** their owning source Atoms **or** settings, **and** record actual outcomes **in** the Journal.
- rejection, requested revision, missing decisions, failed corrections, **and** partial effects **must** remain distinguishable; **none** **may** be reported as a successfully approved **and** completed correction.

check source-binding fixtures with nested output directories, missing targets, a target for a different Atom, a stale source Revision, tampered body content, **and** a valid current source. **only** the valid source-faithful case **may** pass the source-binding check; historical output **may** remain preserved **without** being reported as current.
