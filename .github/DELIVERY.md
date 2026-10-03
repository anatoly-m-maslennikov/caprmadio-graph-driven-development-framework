# Repository delivery policy

This operational document defines how the repository moves changes from `amm/dev` (or the legacy `dev` branch) to `main`. The framework overview and documentation map live in the root [README](../README.md).

## Rules

- [Development branch ruleset](https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/rules/18896762): only `anatoly-m-maslennikov` may create, update, or delete `dev` or `amm/dev`.
- [`main` ruleset](https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/rules/18897046): `main` has no bypass actors; every update requires a pull request, `PR policy`, and the merge-commit method.
- [Policy workflow](workflows/dev-to-main-policy.yml): `PR policy` passes only for a same-repository `dev → main` or `amm/dev → main` pull request authored by the repository owner. A passing non-draft PR is merged automatically.
- Repository tests and validators are temporarily disabled; no successful PR check currently represents test, evaluation, lint, type-check, cross-platform, or framework-validation evidence.
- [WSL proof workflow](workflows/wsl-proof.yml): an explicit manual workflow targets a labeled self-hosted Windows/WSL runner. It is a proof hook, not evidence until a run on the tested commit succeeds.
- [Release publisher](workflows/publish-release.yml): a protected `main` push that changes the coordinated version contract is checked against the committed release declaration, then creates only a missing immutable tag or GitHub Release at the exact merge SHA. Existing collisions stop; the workflow never writes repository content after merge.

Merge commits are deliberate: development branches are long-lived, so preserving their commits as parents of `main` prevents the history divergence caused by repeated squash or rebase merges.

## Delivery sequence

1. The owner commits and pushes a bounded change to `amm/dev` (or legacy `dev`).
2. The owner opens a ready pull request from that branch to `main`.
3. `PR policy` validates the author, repository, head, and base.
4. No automated repository validation runs while the temporary suspension is active.
5. GitHub Actions enables merge-commit auto-merge.
6. GitHub updates `main` only after the required checks pass.
7. When the coordinated version contract changed, the release publisher rechecks the committed transaction at the merge SHA, verifies or creates the immutable tag, and verifies or creates its GitHub Release.

Pull requests to `main` from any branch other than `dev` or `amm/dev`, or from any other repository or author, are expected to fail `PR policy` and cannot merge.

Release preparation is separately explicit: `dset release plan` and `dset release check` are read-only, while `dset release prepare --execute` atomically synchronizes the declared product and Python-package version surfaces. Preparation never publishes, pushes, tags, or creates a GitHub Release.

## Temporary validation suspension

Repository validation was explicitly suspended on 2026-08-10 so the current CAPRMEDIO development line can be delivered while the self-hosting migration backlog is red. The DSET workflow and its required status check are removed for this interval. `PR policy` remains the sole required check, and `Enable auto-merge` remains the delivery action visible on the pull request.

A green pull request during this suspension proves only that the owner-only development-to-main delivery policy passed. It must not be cited as evaluation evidence for repository correctness, test success, validation success, portability, or release readiness.

Restore automated validation by reintroducing a workflow that checks out the exact head, installs the locked environment, and runs `uv run dset verify .` across Linux, macOS, and native Windows, then add its stable context back to the `main` ruleset.
