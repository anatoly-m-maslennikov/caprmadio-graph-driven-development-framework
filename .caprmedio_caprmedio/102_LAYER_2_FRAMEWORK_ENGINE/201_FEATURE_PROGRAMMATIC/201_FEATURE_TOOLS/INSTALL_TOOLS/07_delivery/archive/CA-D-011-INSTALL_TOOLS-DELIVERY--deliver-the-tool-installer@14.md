---
atom_id: CA-D-011
subjects:
  governs:
    continuant:
      - feature-boundary
version: 14
updated_at: 2026-09-15 03:15:32 +0400
relations:
  delivery_for:
    - CA-R-856
    - CA-M-103
    - CA-R-1124
    - CA-R-1064
    - CA-R-1065
---
# Deliver the Tool installer

Realize `INSTALL_TOOLS` through `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/INSTALL_TOOLS/install_tools.py` and the shared non-executable installation library `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/framework_installation.py`. The Tool exposes machine-readable `describe`, read-only `status`, dry-run `run`, and explicit `run --apply` interfaces.

The selected Tool runtime layout is `.caprmedio_runtime/tools/releases/<release>/TOOLS`, selected by `.caprmedio_runtime/tools/current.toml`. Stable launchers live under `.caprmedio_runtime/tools/bin`, including `close-atom`, `commit-trigger`, and `replace-atom`. The runtime retains its canonical Codex Hook fragment under `.caprmedio_runtime/tools/hooks/codex`, while active generic dispatcher groups are merged into the current user's Codex Hook Carrier. Those groups contain no executable dependency outside the selected Project's `.caprmedio_runtime/tools`, resolve the repository from invocation context, require repository-local Git activation `caprmedio.codex-hooks = v1`, and invoke the stable launcher only when both activation and launcher are present. Git Hook launchers live under `.caprmedio_runtime/tools/hooks/git`, and Git registers that directory through repository-local `core.hooksPath`. Status reports the user Carrier, canonical fragment, project-local migration, local activation marker, and Codex-controlled trust separately. Disposable installation staging and atomic-write intermediates live below `.caprmedio_tmp/install_tools/`.

Apply reports `host-hook-carrier-unavailable` when the Codex user Hook Carrier cannot be written. That failure leaves the previously selected release and runtime-owned Hook fragment selected, rather than exposing the partially installed release through stable launchers. Successful migration removes `.caprmedio_install/` after every active Hook and launcher points to `.caprmedio_runtime/tools/`.
