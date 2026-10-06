---
cce_version: cce_1
cce_form: separation
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Atom/Content Role: Implementation"
    - "Implementation Binding"
    - "Evidence"
    - "Journal/Record"
    - "Verification"
version: 1
updated_at: "2026-09-17 11:52:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Keep Evaluation realization chains distinct

an Evaluation Atom's realization chains **must** remain distinct between deterministic test implementations **and** qualitative, probabilistic, statistical, rubric-based, **or** model-judged evaluation implementations.

**every** chain **must** keep these contributions distinguishable:

- its executable Implementation;
- its configuration **or** rubric;
- its factual execution result;
- its Evidence;
- its Verification judgment.

a shared runner, prompt, judge, report, **or** gate **must not** merge the chains' meanings, results, **or** coverage. the source authority, executable mechanisms, factual Journal Records, **and** reusable Operations definitions retain their distinct roles under CAPRMEDIO-META-REQU-092 **and** CAPRMEDIO-META-REQU-093.
