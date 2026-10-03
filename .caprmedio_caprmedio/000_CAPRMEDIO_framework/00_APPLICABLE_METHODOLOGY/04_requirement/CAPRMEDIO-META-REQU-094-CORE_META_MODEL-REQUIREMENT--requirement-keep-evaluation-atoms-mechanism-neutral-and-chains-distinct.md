---
atom_id: CAPRMEDIO-META-REQU-094
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - evaluation
version: 9
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
  child_of:
    - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-094-CORE_META_MODEL-REQUIREMENT--requirement-keep-evaluation-atoms-mechanism-neutral-and-chains-distinct.md
---
# Requirement — Keep Evaluation Atoms mechanism-neutral and chains distinct

A mechanism-neutral Evaluation Atom defines what claim is checked, the applicable conditions, the acceptance criteria, **and** the disposition rule. It does **not** prescribe whether the check is realized by an automated test, model-judged evaluation, statistical assessment, rubric, manual review, **or** another implementation mechanism.

One Evaluation Atom **may** be realized by multiple distinct evaluation implementations. One implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable to **every** covered claim. Coverage is many-to-many but never implicit.

Deterministic Test implementations **and** qualitative, probabilistic, statistical, rubric-based, **or** model-judged Evaluation implementations retain distinct chains. **every** chain keeps its executable Implementation, configuration **or** rubric, factual Ops result, Evidence, **and** Verification judgment distinguishable. A shared runner, prompt, judge, report, **or** gate does **not** merge their meanings, results, **or** coverage.

Test **and** Evaluation describe implementation mechanisms, **not** Type values under Content Role Evaluation. The Evaluation Atom remains the authority; executable mechanisms are Implementation, **and** their enacted results are Ops.

## Primary claim

Evaluation Atoms remain mechanism-neutral authority, while Test **and** Evaluation implementations **and** their factual Ops results remain distinct, attributable chains.
