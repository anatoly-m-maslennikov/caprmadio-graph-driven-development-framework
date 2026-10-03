---
subjects:
  governs:
    occurrent:
      - Python 3.14 Contract Upgrade Validation
  depends_on:
    continuant:
      - Python Runtime
      - Compatibility
      - Validation Evidence
version: 2
updated_at: 2026-08-30 17:21:33 +0400
---
# Validate the Python 3.14 contract upgrade

## Result

The selected Programmatic Python contract and checked-in workflow carrier both target the stable CPython `3.14.*` series. Local validation under CPython 3.14.7 passed for the current Programmatic Python source frontier and all installed read-only Tool interfaces.

This is bounded local execution evidence. It does not claim a successful hosted workflow run or support for another platform.

## Evaluated frontier

- Git revision after the technical contract and workflow changes: `26e3575635e5764d24590165106cf7480d06e67f`.
- `pyproject.toml` SHA-256: `e9f30f59cba7e90ab3ebc66c24468baf760b688e33c2e50df715062c105800b2`.
- `.github/workflows/publish-release.yml` SHA-256: `3401b40b6ccf59acce1b4714aad157ec8236bd3b23c5fcf31f68c0e334045558`.
- Programmatic Python files evaluated: 65.
- Programmatic Python source-frontier SHA-256: `18392c4564c0ef8e0c9a9f44dcb836963cbda4932a95446c005c7a710a296b79`.
- Installed launchers evaluated through their read-only `describe` interface: 15.

## Environment

- Implementation: CPython.
- Version: 3.14.7.
- Executable: `/opt/homebrew/opt/python@3.14/bin/python3.14`.
- Operating system: Darwin.
- Machine: arm64.

## Checks and outcomes

| Check | Outcome |
|---|---|
| Parse `pyproject.toml` and read the canonical selected runtime | Pass: `==3.14.*` |
| Inspect the checked-in workflow interpreter selection | Pass: `python-version: "3.14"` |
| Compile every current Programmatic Python source in memory with CPython 3.14.7 | Pass: 65 of 65 |
| Invoke every installed launcher through its read-only `describe` interface | Pass: 15 of 15 |
| Confirm the standard-library-first default dependency selection remains unchanged | Pass: `required_runtime_dependencies = []` |

The validation compiled source through Python's in-memory `compile` function and did not intentionally create bytecode caches. Four source-tree `__pycache__` directories, including one CPython 3.14 bytecode file, predated this Task and remain a separate existing source-hygiene issue; their timestamps are between 12:42 and 13:35 local time, before the 16:33 migration execution.

## Limitations

- The repository's suspended test suite was not run.
- The hosted release workflow was not executed.
- The workflow still contains historical release implementation beyond the Python selector; this validation does not establish that the complete release job is current.
- No macOS, Linux, Windows, or WSL portability claim is established beyond this one local Darwin arm64 observation.

## Source

- [Python 3.14.7](https://www.python.org/downloads/release/python-3147/), released 2026-08-05.
