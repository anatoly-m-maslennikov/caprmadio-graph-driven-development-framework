---
subjects:
  governs: "artifact-validation"
version: 7
updated_at: "2026-09-15 21:31:49 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1136
    - CA-R-1201
    - CA-R-1202
    - CA-D-269
---
# Reject RMED subject cardinality

## Test case

- give an RMED Atom **=0** GOVERNS targets.
- give another RMED Atom **>=2** distinct GOVERNS targets.
- give a valid RMED Atom **=1** GOVERNS target **and** **>=0** unique DEPENDS_ON targets; include a case with **>=2** DEPENDS_ON targets.

## Expected result

reject the first two fixtures with the stable RMED-subject-cardinality diagnostic **and** a non-zero exit. accept the third fixture with respect **to** Subject cardinality. count **only** GOVERNS targets toward the **=1** governed-target constraint; DEPENDS_ON targets **must not** be counted as additional GOVERNS targets.
