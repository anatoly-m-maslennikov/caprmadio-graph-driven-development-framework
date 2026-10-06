---
cce_version: cce_1
cce_form: separation
subjects:
  governs: "Artifact"
  depends_on:
    - "Artifact/Authority"
    - "Artifact/Applicability"
    - "Artifact/Currentness"
    - "Artifact/Revision"
    - "Projection"
    - "Provenance"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Evaluation"
    - "Property"
    - "Atom/Claim"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Operations"
version: 2
updated_at: "2026-09-17 11:44:03 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {child_of: [CA-M-001]}
---
# Keep Authority, Applicability, and Currentness distinct

an Artifact's Authority, Applicability, **and** Currentness **must** remain distinct Properties under CA-R-1499, CA-R-1500, **and** CA-R-1501.

- an authoritative Artifact **may** be inapplicable **to** a given context.
- an applicable historical Revision **may** no longer be current.
- a current Projection **may** accurately report state **without** possessing semantic authority.

acceptance, provenance, Implementation, evidence, **and** Evaluation do **not** silently establish **any** of these Properties. precedence **and** conflict resolution select among **otherwise** authoritative **and** applicable Claims; they do **not** merge these Properties. the owning Requirement, Method, Evaluation, Delivery, **and** Operations Atoms govern how these Properties are resolved **and** reported through derived views.
