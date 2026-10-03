---
subject_scopes:
  - feature-boundary
version: 10
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CA-R-1064
---
# Deliver the commit-context script

Realize `COMMIT_CONTEXT` through the canonical source script `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CONTEXT/commit_context.py` and its content-identical carrier in the selected `.caprmedio_install` release. It must expose the common read-only Finder CLI contract. The standalone script and the logic invoked by `COMMIT_CHANGE_SET` must call the same release-local non-executable implementation and return the same sealed context for the same trigger and unchanged source frontier.

The implementation accepts an ordinary file, an Atom file, or a non-empty folder. It seals schema-version-3 context with `subject.kind`, the exact before-path and after-path boundary, and either one file digest or a complete ordered folder entry set plus aggregate digest. Atom files retain their declared versions and can receive typed-relation decoration. Ordinary files and folders receive logger-owned operational revisions and an empty source set. The implementation indexes Atom carrier identities tolerantly for optional relation decoration: an identity collision removes only that ambiguous lookup key, while exact unambiguous filenames remain usable. Relation registry, lifecycle, version, duplicate, missing-target, and ambiguity defects are returned as non-blocking context diagnostics. They never turn this operational logger into a repository-wide graph validator or prevent an otherwise valid project-path action from reaching the Journal and Git commit boundary.
