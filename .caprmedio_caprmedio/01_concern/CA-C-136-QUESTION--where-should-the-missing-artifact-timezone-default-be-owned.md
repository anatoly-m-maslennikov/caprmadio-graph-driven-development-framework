---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Framework Instance Settings/Artifact Timestamp Timezone"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Artifact/Revision"
    - "Carrier"
priority: medium
version: 1
updated_at: "2026-09-17 13:42:35 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Where should the missing Artifact timezone default be owned?

how should the existing `local` Artifact timestamp default move **to** its required Default Settings owner **without** losing timezone resolution **or** silently changing a Settings Artifact outside this Atom-only repair frontier?

## Evidence

D-390 currently admits `local`, `UTC`, **or** an IANA name **and** fixes `local` as the default. META-REQU-675 prohibits Atoms from fixing **or** duplicating current Default Settings values; M-279 resolves absent instance parameters through Default Settings. the inspected Default Settings Carrier `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml` has no `artifact_timestamps.timezone` parameter. its observed SHA256 is `15ee714b7481aa54863e7d65198a93e08df48e3b04914dfd9b48fff32fc02feb`.

## Principle check

CA-M-002 requires one authoritative value; CA-M-006 requires the schema, fallback rule, **and** actual source **to** agree; CA-R-1490 protects the existing intended default. deleting the literal from D-390 alone would remove the observed source of that default. selecting another value **or** editing the Settings Artifact is **not** justified by this RMEDO-only repair request.

## Disposition

preserve D-390 until the coordinated value transfer is authorized **and** checked. retain its admitted domain **and** timestamp interpretation; reuse D-408 field conventions **and** M-279 resolution. do **not** invent a fallback, copy a current instance override into defaults, **or** infer that an offset-free timestamp is invalid solely from this open issue.
