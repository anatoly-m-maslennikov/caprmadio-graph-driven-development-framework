---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Directory Carrier"
    - "File Carrier"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Scope Unit"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1579", "CA-R-1534", "CA-R-1536", "CA-R-1537", "CA-R-1538", "CA-D-474", "CA-D-460", "CA-D-461"]}
---
# Validate folder-derived Plan decomposition

the decomposition Evaluation **must** reproduce **only** the Plan Relations admitted by CA-D-474.

- place Plan `A` directly **in** `03_plan`, Plan `B` inside `A`, **and** Plan `C` inside `B/done`: derive `A DECOMPOSES_INTO B` **and** `B DECOMPOSES_INTO C`, plus their exact `IS_DECOMPOSITION_OF` inverses.
- derive `A` reaching `C` **only** **in** the recursive view; do **not** create a direct `A` **to** `C` fact.
- place the matching `A.md` beside `A/`: count one Atom **without** a self-edge. move the whole Bundle below `03_plan/001_backlog`: retain outgoing decomposition **and** **=0** inverse relations for `A`.
- change Labels, numbers, **or** intervening Status directories: retain the same endpoint identities **and** relation meanings.
- reject a cycle, ambiguous Bundle, a non-Plan endpoint, duplicate authored decomposition, a Status folder interpreted as a Plan, **or** structural parentage substituted for planned-work decomposition.
- ensure a related Atom's Claim, Revision, Status, **and** owning Scope Unit remain independent of the Hub's Claim **and** lifecycle.

report exact expected **and** observed endpoints **without** fixing source placement silently.
