---
atom_id: CA-D-011
subject_scopes:
  - feature-boundary
version: 9
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-R-856
    - CA-M-103
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CA-R-1064
    - CA-R-1065
---
# Deliver the Tool installer

Realize `INSTALL_TOOLS` through `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/install_tools.py` and the shared non-executable installation library `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/framework_installation.py`. The Tool exposes machine-readable `describe`, read-only `status`, dry-run `run`, and explicit `run --apply` interfaces.

The installed layout is `.caprmedio_install/releases/<release>/TOOLS`, selected by `.caprmedio_install/current.toml`. Stable launchers live under `.caprmedio_install/bin`, including `close-atom`, `commit-trigger`, and `replace-atom`; the lifecycle-intent launchers remain dry-run capable and their apply path stays blocked until the commit pipeline admits lifecycle-intent serialization. The installation retains its canonical Codex Hook fragment under `.caprmedio_install/hooks/codex`, while the active generic dispatcher groups are merged into the current user's Codex Hook carrier. Those groups contain no executable dependency outside the selected project's `.caprmedio_install`, resolve the repository from invocation context, require repository-local Git activation `caprmedio.codex-hooks = v1`, and invoke the stable launcher only when both activation and launcher are present. Git Hook launchers live under `.caprmedio_install/hooks/git`, and Git registers that directory through repository-local `core.hooksPath`. Status reports the user carrier, canonical fragment, project-local migration, local activation marker, and Codex-controlled trust separately.

Apply reports `host-hook-carrier-unavailable` when the Codex user Hook carrier cannot be written. That failure leaves the previously selected release and install-owned Hook fragment selected, rather than exposing the partially installed release through stable launchers.
