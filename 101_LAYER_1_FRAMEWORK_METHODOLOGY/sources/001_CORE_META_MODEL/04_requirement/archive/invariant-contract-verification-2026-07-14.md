# Invariant contract verification — 2026-07-14

- **LLM session IDs:**
  - `codex:019f591f-04f6-70f2-8de7-828b7cccc69d`

> [!NOTE]
> Historical proof only. This record evaluated the pre-layer DSET 0.2 contract
> at commit `b84c23bdbc642508a142b8f7469de4cd08b94573`. Its `METH-*` candidate
> owners were superseded by schema 1.2 layer-owned `CAPRMEDIO-*` truth, so this file
> no longer supports a current invariant-contract Pass claim. Reopen occurred
> when the ID model, accepted owners, schemas, validation, and version changed.

## Scope

This evidence covers only the DSET 0.2 invariant-contract batch. It verifies stable ownership, requirement, scenario, test, and eval mappings and the integrity of the current repository. It does not claim that the planned governance resolver, materializer, thin wrappers, recursive self-hosting runner, TypeScript profile, or adopter pilots are implemented.

## Contract identity

- Roadmap invariants: `CAPRMEDIO-INVARIANT-TOOL-001..002`, `CAPRMEDIO-INVARIANT-GOV-001..004`, `CAPRMEDIO-INVARIANT-SKILL-001..002`, and `CAPRMEDIO-INVARIANT-META-001`
- Candidate change requirements: `CAPRMEDIO-REQUIREMENT-TOOL-006..007`, `CAPRMEDIO-REQUIREMENT-GOV-007..010`, `CAPRMEDIO-REQUIREMENT-SKILL-002..003`, and `CAPRMEDIO-META-REQU-184--stable-public-identity`
- Candidate deterministic proof: `CAPRMEDIO-TEST-CASE-TOOL-009..011`, `CAPRMEDIO-TEST-CASE-GOV-009..011`, `CAPRMEDIO-TEST-CASE-SKILL-002..003`, and `CAPRMEDIO-TEST-CASE-META-004`
- Candidate qualitative proof: `CAPRMEDIO-EVALUATION-CASE-TOOL-001..002`, `CAPRMEDIO-EVALUATION-CASE-SKILL-002`, and `CAPRMEDIO-EVALUATION-CASE-GOV-009`
- Candidate accepted invariants: `METH-INV-013`–`METH-INV-021`
- Candidate accepted requirements: `METH-REQUIREMENT-026`–`METH-REQUIREMENT-034`
- Candidate accepted deterministic proof: `METH-TEST-CASE-027`–`METH-TEST-CASE-035`
- Candidate accepted qualitative proof: `METH-EVALUATION-CASE-015`–`METH-EVALUATION-CASE-018`

## Deterministic results

| Check | Result | Bounded evidence |
|---|---|---|
| Canonical structural validation | Pass | `python -m dset_toolchain check .` returned `DSET validation passed` throughout the edit sequence |
| Full current toolchain | Pass | `.venv/bin/dset verify .` with `UV_CACHE_DIR` set to a writable cache outside the repository reported 19 Python files formatted, clean Ruff, clean mypy, 18/18 unit tests passing, fresh traceability, and `DSET validation passed` |
| Diff hygiene | Pass | `git diff --check` returned no output |
| Accepted package ID counts | Pass | 34 requirements, 35 deterministic tests, and 18 qualitative evals are present and registered |
| Invariant counts | Pass | The accepted methodology has 21 invariants including the nine new IDs; the roadmap retains exactly nine DSET 0.2 invariants |
| Capability-claim audit | Pass | Every unimplemented 0.2 mechanical seam is labeled `Planned`; the active change is `in-progress`, its PR is `pending`, and its verification status says the mechanics are not implemented |

The first direct `uv run dset verify .` attempt could not use the sandbox-denied user cache. Running the same repository commands through the existing project environment with a writable cache produced the passing result above; `uv` emitted non-blocking project-lock warnings but every configured command completed successfully.

## Disposition

The invariant contract is internally consistent and ready to govern later 0.2 implementation batches. `CAPRMEDIO-TEST-CASE-TOOL-009..011`, `CAPRMEDIO-TEST-CASE-GOV-009..011`, `CAPRMEDIO-TEST-CASE-SKILL-002..003`, `CAPRMEDIO-TEST-CASE-META-004`, `CAPRMEDIO-EVALUATION-CASE-TOOL-001..002`, `CAPRMEDIO-EVALUATION-CASE-SKILL-002`, and `CAPRMEDIO-EVALUATION-CASE-GOV-009` remain planned proof obligations and must not be marked passing until their corresponding mechanics and fixtures exist.
