---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "complementary-software-evidence"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-09-24 17:18:07 +0000"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Combine complementary software behavior evidence

## Claim checked

the Evaluation set covers **every** declared failure mode with an appropriate,
replayable evidence form.

## Test case

review one installed component whose examples cover valid behavior but omit an
invalid state transition **and** the installed Delivery boundary.

## Acceptance criteria

pass **only** **when** stateful **or** explicit failure evidence **and** installed-behavior
evidence are added, with covered **and** uncovered boundaries stated.

## Failure disposition

reject reliance on the incomplete set **without** treating examples as universal
evidence.

## Sources

- [Pytest: good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)

### E2E-first acceptance cases

- reject implementation-first work with no previously prepared end-to-end boundary test; admit **only** the documented minimum prerequisite needed **to** run that test.
- require the real component boundary exercised against valid, invalid, boundary, **and** combined golden-corpus cases. a mocked implementation **or** unit-only pass does **not** satisfy this check.
- introduce an issue exposed by the corpus, reproduce it with a focused unit **or** other appropriate regression test, repair the code, **and** require the focused test **and** relevant end-to-end cases **to** pass. reject changed expected output that merely hides the defect.
- verify implementation completion is independent of creating **or** activating M Atoms. preserve issue evidence for a separate learning Run; existing confidence, retry, **and** permission gates remain applicable.
