---
cce_version: cce_1
cce_form: serialization
atom_id: CA-D-008
subjects:
  governs: "feature-boundary"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 17
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  relates_to:
    - CA-R-1491
  delivery_for:
    - CA-R-804
    - CA-R-1124
    - CA-R-1064
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver the commit-context script

COMMIT_CONTEXT **must** be delivered through the canonical source script `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/COMMIT_CONTEXT/commit_context.py` **and** its content-identical Carrier **in** the selected `.caprmedio_runtime/tools` release.

- expose the common read-only Finder CLI contract. the standalone script **and** the logic used by COMMIT_CHANGE_SET **must** call the same release-local non-executable implementation **and** return the same sealed context for identical inputs **and** unchanged observed state.
- accept an ordinary file, an Atom file, **or** a non-empty folder. seal schema-version-3 context with `subject.kind`, the exact before-path **and** after-path boundary, **and** **=1** file digest **or** a complete ordered folder entry set with its aggregate digest.
- retain available declared Atom Revisions as observed values. ordinary files **and** folders use logger-owned operational Revisions **and** an empty source set; an operational Revision **must not** be presented as a missing **or** invalid declared Atom Version.
- treat Atom classification **and** relation decoration as optional enrichment. unresolved classification **must not** remove an otherwise recordable observed Carrier from the Journal path. preserve its native identity **and** digest **without** inventing an Atom ID.
- use exact unambiguous identity lookups for optional enrichment. an identity collision leaves the ambiguous lookup unresolved; do **not** guess its target.
- diagnostics encountered during capture **may** accompany the observation, but capture **must not** require a Project-conformance scan. naming, classification, lifecycle, relation, **and** placement defects do **not** block Journal admission under CA-R-1491.
- preserve event-envelope integrity **and** read-only behavior; separate Git mutation gates retain their own authority.
