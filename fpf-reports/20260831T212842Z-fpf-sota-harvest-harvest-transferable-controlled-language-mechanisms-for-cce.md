:codex-annotation{index="1"} Completed: “Call 2 — harvest transferable mechanisms.”

## Task, scope, and boundaries

- **Task:** Harvest controlled-language mechanisms that could later inform CAPRMEDIO Controlled English (CCE).
- **Receiving use:** Research input for a later CCE gap comparison, option exploration, and design challenge. This report does not select or recommend CCE changes.
- **Target and current state:** The target is CCE. This call does not re-audit CCE authority or assume that CCE is already a formally parseable language.
- **In scope:** Current official ASD-STE100 Issue 9; its official change, training, and AI-support material; formal controlled-English practice; controlled-natural-language classification and evaluation research; and the supplied Chelebi experiment as a secondary cue.
- **Excluded:** ASD-STE100 rule text, vocabulary entries, examples, numbering, or branding; Chelebi’s prompts, skill, hooks, linter, or code; legal conclusions; CCE adoption decisions; implementation; and claims of ASD compliance, certification, affiliation, or endorsement.
- **Evidence policy:** Official ASD/STEMG material is primary for ASD-STE100 facts. Attempto project documentation is primary for ACE. Peer-reviewed or original research publications support cross-tradition claims. The Chelebi material can identify hypotheses but cannot prove transfer to CCE.
- **Authority boundary:** ASD-STE100 remains ASD’s standard. Any CCE mechanism must be independently specified, named, expressed, and tested. The legal notes below are conservative engineering boundaries, not legal advice.
- **Dependencies:** A later decision needs CCE’s intended purpose, authoritative grammar/semantics, artifact profiles, terminology ownership, and evaluation goals.
- **Stop condition:** Stop after the source ledger, mechanism records, bridges, losses, exclusions, and open questions. Do not rank options or recommend changes.
- **Resolved FPF source:** repository revision `563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef`; primary entrypoint G.2, with C.22.2, A.6.C, and G.4 as supporting context.
- **Saved report:** `fpf-reports/20260831T212842Z-fpf-sota-harvest-harvest-transferable-controlled-language-mechanisms-for-cce.md`
- **Open report:** [saved analysis](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20260831T212842Z-fpf-sota-harvest-harvest-transferable-controlled-language-mechanisms-for-cce.md)

## High-confidence results (>=95%)

### 1. Harvest contract and resolved source

The resolved command is `$fpf sota harvest`. The result is a plural synthesis, not a single borrowed recipe: operational technical English, formal controlled English, and CNL design/evaluation research remain separate traditions. The Chelebi experiment remains a fourth, lower-authority experimental cue. **Confidence: 100%. Evidence:** explicit task contract and resolved FPF G.2 workflow.

### 2. Corpus ledger and coverage boundary

1. **S1 — ASD-STE100 Issue 9, January 2025.** Official current standard; admitted for its high-level architecture, scope, governance, and human-authoring mechanisms. Relevant regions: copyright and highlights; General Introduction; writing-rule section summaries; dictionary introduction. Issue 9 supersedes earlier issues. [Official Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

2. **S2 — STEMG downloads and change process.** Official current-status and maintenance evidence. It identifies Issue 9 as current and describes proposal intake, STEMG assessment, and incorporation of accepted changes in a later issue. [Official downloads and change process](https://www.asd-ste100.org/STE_downloads.html)

3. **S3 — STEMG white paper on ASD-STE100 and AI, June 2026.** Official position on AI support, human accountability, traceability, confidentiality, quality assurance, benchmarks, and standard precedence. [Official AI white paper](https://www.asd-ste100.org/assets/files/WhitePaper-ASD-STE100_and_AI.pdf)

4. **S4 — STEMG training guidance.** Official evidence that correct use needs language competence, domain competence, training, and attention to both vocabulary and writing rules. [Official training guidance](https://www.asd-ste100.org/STE_training.html)

5. **S5 — Attempto Controlled English documentation.** Primary evidence for a formal CNL that separates construction rules from interpretation rules and exposes parser feedback and normalized interpretation to authors. [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_constructionrules.html), [ACE interpretation rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_interpretationrules.html), and [ACE troubleshooting guide](https://attempto.ifi.uzh.ch/site/docs/ace_troubleshooting.html)

6. **S6 — Kuhn’s CNL survey and classification.** Peer-reviewed comparative evidence covering 100 English-based CNLs and distinguishing purpose from the design dimensions of precision, expressiveness, naturalness, and simplicity. [ACL Anthology record and paper](https://aclanthology.org/J14-1005/)

7. **S7 — Kuhn’s CNL evaluation method.** Original research evidence that understandability claims require user experiments and should be isolated from the effects of a particular authoring tool. The reported study is small and is used for method, not as universal proof. [How to Evaluate Controlled Natural Languages](https://ceur-ws.org/Vol-448/paper4.pdf)

8. **S8 — Chelebi’s 2026 experiment and kit description.** Secondary experimental cue only. It compares six engineering-writing tasks, four prompting conditions, and two model families using a heuristic violation score. The author reports directional improvements but also states that the sample is small, the metric is heuristic, one task regressed, model behavior differed, and form quality does not prove substance. [Episode and kit index](https://www.chele.bi/videos/the-cure-for-ai-slop) and [cross-model results with caveats](https://www.chele.bi/videos/the-cure-for-ai-slop/kit/experiment/results-cross-model)

**Coverage boundary:** The admitted corpus covers three independent traditions and one experiment. It does not include a systematic review of every current CNL, multilingual CNL design, legal advice, or an empirical CCE corpus study. **Confidence: 100%.**

### 3. ClaimSheets: transferable mechanism palette

These are abstract mechanisms, not adopted CCE requirements.

#### M1 — Separate lexical control from composition control

- **Problem:** A word list cannot control how claims are composed; grammar alone cannot prevent terminology drift.
- **Mechanism and category:** Maintain two linked control surfaces: a lexical/terminology contract and a sentence/composition contract. Category: language architecture.
- **Evidence and provenance:** ASD-STE100 explicitly consists of writing rules plus a controlled dictionary; Kuhn distinguishes a controlled vocabulary from a CNL because vocabulary alone does not govern complete sentences; ACE separately defines admissible constructions. [ASD-STE100 overview](https://www.asd-ste100.org/about_STE.html), [Kuhn 2014](https://aclanthology.org/J14-1005/), [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_constructionrules.html)
- **Preconditions, limits, cost, failure modes:** The two surfaces need linked versions and conflict rules. Cost is maintaining both. Failure occurs when a permitted term cannot be used in an admitted construction, or a construction changes a term’s governed sense.
- **Safe original reimplementation:** Define original CCE lexicon and construction schemas, original identifiers, and original examples; test cross-consistency between them.
- **Attribution, license, exclusion:** Attribute the high-level inspiration. Do not reproduce ASD rule text, dictionary data, examples, organization, or numbering.
- **Confidence:** 99%.

#### M2 — Combine a controlled core with governed domain terminology

- **Problem:** A closed general vocabulary cannot name all project concepts, but an unrestricted vocabulary reintroduces synonym and meaning drift.
- **Mechanism and category:** Use a stable core plus admitted domain terms. Each term has a concept, grammatical role, governed sense, allowed forms, provenance, scope, and owner. Category: terminology governance.
- **Evidence and provenance:** ASD-STE100 permits subject-field nouns and verbs governed through company glossaries or terminology databases. ACE distinguishes predefined function words from user-defined content words. [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_constructionrules.html)
- **Preconditions, limits, cost, failure modes:** Requires concept identity and an admission owner. Costs include review and migration. Failures include duplicate terms for one concept, one term for incompatible concepts, and local terms escaping their scope.
- **Safe original reimplementation:** Create an independent CCE term record and admission workflow based on CAPRMEDIO concepts and provenance, not on ASD vocabulary entries.
- **Attribution, license, exclusion:** Cite the general controlled-core/domain-extension pattern. Do not import the ASD dictionary or its replacement pairs.
- **Confidence:** 99%.

#### M3 — Type statements by communicative function

- **Problem:** Instructions, descriptions, requirements, questions, and safety statements do different work; one undifferentiated grammar hides that difference.
- **Mechanism and category:** Give each statement an explicit communicative role, then bind that role to admissible operators and constructions. Category: statement typing.
- **Evidence and provenance:** ASD-STE100 separates procedural, descriptive, and safety writing. ACE distinguishes declarative, interrogative, and imperative modes. [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [ACE syntax overview](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/syntax_report.html)
- **Preconditions, limits, cost, failure modes:** Roles need clear boundaries and rules for mixed artifacts. Cost is author classification. Failure occurs when a description is interpreted as an obligation or a note contains an executable instruction.
- **Safe original reimplementation:** Define original CCE roles from CAPRMEDIO’s own work types and operators; give every role its own acceptance tests.
- **Attribution, license, exclusion:** Attribute the cross-tradition idea. Do not copy ASD section structure or ACE grammar productions.
- **Confidence:** 98%.

#### M4 — Make actors, referents, and attachment explicit

- **Problem:** Passive constructions, pronouns, and loosely attached modifiers can hide who acts or what a phrase modifies.
- **Mechanism and category:** Prefer explicit actors and repeated referents where ambiguity is possible; either define deterministic attachment/anaphora rules or reject ambiguous forms. Category: reference and role clarity.
- **Evidence and provenance:** ASD-STE100 constrains passive voice and directs writers to replace ambiguous pronouns. ACE formally specifies attachment and anaphora behavior and warns when accepted syntax does not match intended meaning. [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [ACE interpretation rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_interpretationrules.html)
- **Preconditions, limits, cost, failure modes:** Requires stable entity names or identifiers. The cost is repetition and reduced stylistic naturalness. Mechanical pronoun bans can create false positives without resolving deeper reference errors.
- **Safe original reimplementation:** Use original CCE entity/reference rules and graph identifiers; test minimal pairs in which one surface form changes the resolved actor or object.
- **Attribution, license, exclusion:** Cite the general explicit-reference mechanism; use newly written examples only.
- **Confidence:** 99%.

#### M5 — Separate admissibility from interpretation

- **Problem:** A sentence can be syntactically accepted yet mean something different from what the author intended.
- **Mechanism and category:** Specify two contracts: what strings are admitted, and how every admitted string maps to a normalized meaning. Show the normalized meaning back to the author. Category: formal language semantics.
- **Evidence and provenance:** ACE publishes separate construction and interpretation rules. Its authoring guidance tells users to compare the system’s paraphrase with intended meaning and reformulate when they differ. [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_constructionrules.html), [ACE interpretation rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_interpretationrules.html), [ACE troubleshooting guide](https://attempto.ifi.uzh.ch/site/docs/ace_troubleshooting.html)
- **Preconditions, limits, cost, failure modes:** Requires a formal grammar, a semantic target such as a typed graph or AST, and defined handling of context. It is expensive. Failure occurs when the parser is deterministic but the symbol-to-domain mapping is wrong.
- **Safe original reimplementation:** Independently define a CCE grammar and mapping to CAPRMEDIO graph assertions; add a round-trip or normalized-paraphrase check.
- **Attribution, license, exclusion:** Attribute ACE as the formal-CNL precedent. Do not copy ACE grammar, interpretation rules, examples, or parser code.
- **Confidence:** 99%.

#### M6 — Separate mechanical conformance from domain truth

- **Problem:** A text can satisfy surface rules while remaining false, unsafe, incomplete, or semantically inappropriate.
- **Mechanism and category:** Partition checks into mechanically decidable conformance, semantic consistency, and domain validation. Tools must report the boundary and preserve `UNKNOWN` where they cannot decide. Category: assurance architecture.
- **Evidence and provenance:** STEMG warns that AI output can appear compliant while applying the standard incorrectly or introducing inaccuracies, and retains responsibility with human authors or organizations. ACE documentation also states that parser diagnostics are not perfectly complete or localized. [STEMG AI white paper](https://www.asd-ste100.org/assets/files/WhitePaper-ASD-STE100_and_AI.pdf), [ACE troubleshooting guide](https://attempto.ifi.uzh.ch/site/docs/ace_troubleshooting.html)
- **Preconditions, limits, cost, failure modes:** Needs a published check taxonomy and qualified reviewers. Cost is human review. The main failure is treating a green linter result as proof of correctness.
- **Safe original reimplementation:** Give each CCE diagnostic a declared assurance class and evidence source; prohibit tools from claiming facts outside that class.
- **Attribution, license, exclusion:** Attribute the assurance boundary; do not advertise ASD compliance or endorsement.
- **Confidence:** 99%.

#### M7 — Govern language change as a versioned evidence process

- **Problem:** A controlled language becomes inconsistent when rules and terms change through informal edits.
- **Mechanism and category:** Record a proposed change, affected authority, rationale, source examples, assessment, decision, and target release; publish which version supersedes which. Category: language governance.
- **Evidence and provenance:** STEMG accepts structured change proposals, records assessments, decides changes collectively, and incorporates accepted changes into later issues. Issue 9 supersedes prior issues. [Official change process](https://www.asd-ste100.org/STE_downloads.html), [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)
- **Preconditions, limits, cost, failure modes:** Requires a maintenance owner and release discipline. Cost is governance latency. Failure occurs through unversioned exceptions or tools pinned to different language versions.
- **Safe original reimplementation:** Use an original CAPRMEDIO change record linked to affected CCE authorities, evidence, decision, migration, and conformance-suite version.
- **Attribution, license, exclusion:** Cite the governance pattern; do not copy the ASD change form or its wording.
- **Confidence:** 99%.

#### M8 — Declare applicability profiles and exclusions

- **Problem:** A language overreaches when users assume it governs formatting, units, every artifact type, or every communication goal.
- **Mechanism and category:** State the intended purpose, artifact types, roles, domains, and explicit non-goals. Treat the controlled language as one layer alongside other specifications. Category: scope control.
- **Evidence and provenance:** ASD-STE100 states that it governs expression rather than all formatting or unit conventions and is intended to work with other applicable directives. Kuhn distinguishes CNL goals such as human comprehension, translation, and formal representation, plus written/spoken and domain scope. [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [Kuhn 2014](https://aclanthology.org/J14-1005/)
- **Preconditions, limits, cost, failure modes:** Profiles need precedence and composition rules. Cost is maintaining several contexts. Failure occurs when “CCE-compliant” is asserted without naming the profile and version.
- **Safe original reimplementation:** Define original CCE applicability records by artifact, statement role, domain, and assurance level; make out-of-scope explicit.
- **Attribution, license, exclusion:** Attribute the scope-layering idea; avoid ASD naming and compliance language for CCE.
- **Confidence:** 99%.

#### M9 — Keep AI subordinate to authority and preserve provenance

- **Problem:** Generated text can look authoritative while obscuring sources, responsibility, confidential inputs, and validation gaps.
- **Mechanism and category:** Keep the governed language specification authoritative; record AI assistance, sources, model/tool version, validation, reviewer, and limitations; retain human accountability. Category: AI governance.
- **Evidence and provenance:** STEMG identifies variable reliability, terminology compromise, weak source traceability, confidentiality risk, and non-endorsement of AI tools; it calls for human oversight, internal policy, disclosure, validation, QA, and benchmarks. [STEMG AI white paper](https://www.asd-ste100.org/assets/files/WhitePaper-ASD-STE100_and_AI.pdf)
- **Preconditions, limits, cost, failure modes:** Requires provenance capture and data policy. Costs are storage, review, and privacy controls. Failure occurs when generated plausibility is mistaken for verified authority.
- **Safe original reimplementation:** Define a CAPRMEDIO-native generation receipt and evidence chain; make the validator and responsible human explicit.
- **Attribution, license, exclusion:** Cite STEMG’s position as inspiration. Do not imply that a CCE tool is ASD-approved.
- **Confidence:** 99%.

#### M10 — Evaluate understanding and semantic fidelity, not only violations

- **Problem:** A linter score measures selected surface features and can improve while comprehension, correctness, or task success does not.
- **Mechanism and category:** Evaluate separate outcomes: conformance, referent resolution, semantic fidelity, human comprehension, task success, authoring/edit cost, and false-positive/false-negative rates. Isolate language effects from tool effects where possible. Category: empirical evaluation.
- **Evidence and provenance:** Kuhn argues that understandability claims require user studies and proposes tool-independent tests against an external representation. The Chelebi experiment itself limits its result to a small, heuristic, form-focused study. [Kuhn 2009](https://ceur-ws.org/Vol-448/paper4.pdf), [Chelebi cross-model caveats](https://www.chele.bi/videos/the-cure-for-ai-slop/kit/experiment/results-cross-model)
- **Preconditions, limits, cost, failure modes:** Needs representative users, artifacts, gold meanings, and adequate samples. It is costly. Proxy optimization and benchmark leakage are central risks.
- **Safe original reimplementation:** Build new CCE test worlds from CAPRMEDIO graphs and ask users or systems to classify, reconstruct, or execute meaning; keep surface lint results separate.
- **Attribution, license, exclusion:** Cite the evaluation methods; do not reuse Chelebi’s tasks, prompts, code, or result claims as CCE evidence.
- **Confidence:** 98%.

#### M11 — Publish the language’s design trade-space

- **Problem:** “Controlled English” hides consequential choices about how formal, expressive, natural, and simple the language is.
- **Mechanism and category:** Declare the target position for precision, expressiveness, naturalness, and simplicity, together with the primary purpose. Category: language design rationale.
- **Evidence and provenance:** Kuhn’s survey shows that CNLs occupy different positions between natural and formal language and presents the PENS dimensions; it also separates comprehension, translation, and formal-representation goals. [Kuhn 2014](https://aclanthology.org/J14-1005/)
- **Preconditions, limits, cost, failure modes:** Requires explicit stakeholder priorities and examples of expressible/non-expressible claims. Increasing one quality can reduce another. Failure occurs when “more controlled” is treated as universally better.
- **Safe original reimplementation:** Write an original CCE design profile with its own measurable definitions, loss budget, and out-of-language cases.
- **Attribution, license, exclusion:** Attribute PENS to Kuhn if the named framework is used; otherwise state independently defined dimensions and sources.
- **Confidence:** 99%.

#### M12 — Treat competence and feedback as part of the system

- **Problem:** A specification can be available yet applied incorrectly, especially when authors focus only on vocabulary or lack domain knowledge.
- **Mechanism and category:** Pair the language with role-specific training, domain competence, guided feedback, and reviewer/proofreader practice. Category: operational adoption.
- **Evidence and provenance:** STEMG says correct STE writing needs English and subject competence and warns that dictionary-only use neglects the writing rules. ACE’s troubleshooting material similarly assumes author learning and iterative reformulation. [STEMG training guidance](https://www.asd-ste100.org/STE_training.html), [ACE troubleshooting guide](https://attempto.ifi.uzh.ch/site/docs/ace_troubleshooting.html)
- **Preconditions, limits, cost, failure modes:** Requires maintained learning material and qualified reviewers. Costs include onboarding and reassessment. Failure occurs when tooling is treated as a substitute for competence.
- **Safe original reimplementation:** Create original CCE learning tasks tied to CAPRMEDIO roles and artifacts; evaluate both rule use and domain-preserving rewrites.
- **Attribution, license, exclusion:** Attribute the competence principle; do not reuse ASD course content or claim accreditation.
- **Confidence:** 98%.

#### M13 — Make examples executable as conformance cases

- **Problem:** Prose rules are interpreted inconsistently when they lack discriminating accepted/rejected cases and expected meanings.
- **Mechanism and category:** For each rule, maintain original positive, negative, boundary, and interaction cases with expected diagnostics and, where relevant, normalized semantics. Category: specification verification.
- **Evidence and provenance:** ASD-STE100 systematically explains rules through contrasting cases; ACE marks rejected constructions and exposes interpretations and diagnostics. [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [ACE construction rules](https://attempto.ifi.uzh.ch/site/docs/ace/6.0/ace_constructionrules.html)
- **Preconditions, limits, cost, failure modes:** Requires a test harness and rule-version linkage. Costs rise with interactions. Examples can accidentally become the de facto grammar while leaving untested gaps.
- **Safe original reimplementation:** Write new CCE cases from CAPRMEDIO concepts and compile them into parser, linter, and semantic-projection tests.
- **Attribution, license, exclusion:** Attribute the testable-example mechanism; do not copy source examples or lightly paraphrase them.
- **Confidence:** 98%.

### 4. SoTA set, traditions, and bridges

**Tradition A — Operational controlled technical prose.** ASD-STE100 contributes the strongest evidence for M1–M4, M7–M9, M12, and M13. Its strength is mature human-facing technical-authoring governance. **Loss at the boundary:** it does not by itself establish a fully formal grammar or one machine-derived meaning for every sentence. **Confidence: 99%.**

**Tradition B — Formal controlled English.** ACE contributes the strongest evidence for M4–M6 and M13. Its strength is the explicit split between syntax and interpretation, plus parser feedback. **Loss at the boundary:** its formal semantics, grammar, and naturalness trade-offs cannot be imported into CCE without choosing CCE’s own semantic target and expressive scope. **Confidence: 99%.**

**Tradition C — Comparative CNL design and evaluation.** Kuhn contributes M8, M10, and M11. Its strength is making design goals and empirical claims explicit. **Loss at the boundary:** a classification or test method does not supply a CCE grammar, vocabulary, governance process, or acceptable thresholds. **Confidence: 99%.**

**Tradition D — Prompt/linter experiment.** Chelebi contributes a testable hypothesis: persistent authoring constraints plus feedback at multiple workflow points may influence model prose more reliably than isolated stylistic prohibitions. **Loss at the boundary:** the experiment is small, heuristic, model-dependent, partly mixes ASD-derived language constraints with a separate response-shape layer, and does not establish correctness, comprehension, or CCE transfer. This tradition therefore remains below the high-confidence adoption threshold. **Confidence in this characterization: 99%.**

**Bridge inventory:**

- **Lexicon ↔ grammar:** strong bridge in ASD-STE100 and ACE; loss is cross-consistency work.
- **Grammar ↔ meaning:** explicit in ACE, not supplied merely by a technical style standard; loss is formalization cost and reduced expressiveness.
- **Human clarity ↔ machine validation:** partial bridge only; deterministic checks cover a subset, while technical truth and intended meaning remain separate.
- **Conformance ↔ comprehension:** empirical bridge required; a violation count is not a comprehension measure.
- **Prompt/tooling ↔ authority:** no authority bridge. A prompt, skill, or linter can carry or check rules but cannot become the canonical language specification by repetition.
- **ASD-STE100 ↔ CCE:** inspiration-only bridge. No compatibility, derivative-standard status, compliance, certification, or endorsement follows.

### 5. Disagreements, exclusions, and insufficient basis

- ASD-STE100 and ACE solve overlapping but different problems. Treating ASD-STE100 as if it already supplied ACE-like deterministic semantics would be a category error. **Confidence: 99%.**
- Greater restriction is not automatically better. Precision, expressiveness, naturalness, and simplicity have trade-offs that must be chosen for the receiving use. **Confidence: 99%.**
- Exact ASD vocabulary, limits, rule formulations, examples, organization, and identifiers are source-specific expression and are excluded from this harvest. The official document is copyrighted and the name is a registered EU trademark; the standard also disclaims endorsement of authoring tools. [ASD-STE100 copyright and notices](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) **Confidence: 100%.**
- The Chelebi kit’s own text/code license does not change the ASD standard’s terms, and this task excludes copying the kit in any event. [Kit license notice](https://www.chele.bi/videos/the-cure-for-ai-slop/kit/asd-ste100/LICENSE) **Confidence: 100%.**
- The Chelebi result is useful for hypothesis generation only. It is not evidence that a particular CCE mechanism improves correctness, comprehension, or project outcomes. **Confidence: 100%.**
- No source in this corpus supplies the correct CCE purpose, grammar, terminology owners, compliance profiles, or evaluation weights. Those remain receiving-system decisions. **Confidence: 100%.**

### 6. Receiving use and refresh path

The harvest can be consumed later as a mechanism library. A later CCE comparison should map each mechanism to current authority as `present`, `partial`, `absent`, `conflicting`, or `out of scope`, without treating this report as authority. A later options exploration can then form original candidates and expose their costs. A later design challenge can test whichever candidate survives against project integrity, graph semantics, author usability, and validation evidence.

Refresh the corpus when ASD issues a new standard or AI position, when the official change process materially changes, when stronger independent CNL/LLM evaluation appears, or when CCE’s purpose or authoritative carriers change. Re-run the source ledger before using old conclusions. **Confidence: 99%.**

## Open questions (confidence <95%)

### Q1 — What is CCE’s primary language purpose?

- **Best current answer:** CCE may need both human-readable governance prose and machine-addressable graph assertions, but this harvest does not establish whether deterministic parsing is an objective.
- **Confidence:** 85%.
- **Missing evidence/input:** An approved purpose statement that selects human comprehension, translation, formal representation/execution, or a governed combination.
- **Consequence:** It determines how far M5 and M11 should go and how much naturalness or expressiveness CCE can trade away.
- **Exact next evidence/action:** Recover or approve the canonical CCE purpose and acceptance outcomes before comparing mechanisms.

### Q2 — Should CCE use layered prompt, lint, and gate enforcement?

- **Best current answer:** The architecture is technically plausible as three separate surfaces—generation guidance, author-time diagnostics, and release-time gating—but its CCE value is unproved.
- **Confidence:** 78%.
- **Missing evidence/input:** A CCE error taxonomy, representative corpus, independent gold judgments, false-positive costs, and a comparison against the current workflow.
- **Consequence:** Premature gating could block valid content, optimize proxies, or let a tool silently become authority.
- **Exact next evidence/action:** If later authorized, design an original benchmark and enforcement prototype without copying the Chelebi kit; keep all outputs advisory until validated.

### Q3 — Are fixed sentence or paragraph limits appropriate for CCE?

- **Best current answer:** They are source- and role-specific controls, not universal controlled-language laws. CCE would need profile-specific calibration.
- **Confidence:** 90%.
- **Missing evidence/input:** CCE artifact classes, failure examples, comprehension tests, and preservation checks for conditions and qualifiers.
- **Consequence:** A universal cap could delete necessary semantics or encourage unnatural fragmentation.
- **Exact next evidence/action:** Measure original candidate thresholds on a stratified CCE corpus before making any limit normative.

### Q4 — What public attribution and legal review will a CCE implementation need?

- **Best current answer:** The conservative boundary is to use only abstract mechanisms, write independent rules/code/examples, cite inspirations, avoid ASD material and branding, and make no compliance or endorsement claim.
- **Confidence:** 90%; this is not legal advice.
- **Missing evidence/input:** Intended distribution, marketing claims, jurisdictions, reused materials, and qualified counsel’s review.
- **Consequence:** The answer affects documentation, naming, notices, and what can ship publicly.
- **Exact next evidence/action:** Obtain a focused IP/trademark review before public release if the implementation refers materially to ASD-STE100 or claims compatibility.

### Q5 — Who owns CCE domain-term admission?

- **Best current answer:** CAPRMEDIO’s existing authority and provenance model is the likely home, but this harvest did not verify the current owner, carrier, or decision process.
- **Confidence:** 88%.
- **Missing evidence/input:** Current CCE terminology carriers, ownership relations, admission criteria, and migration rules.
- **Consequence:** M2 cannot be reliable without one accountable admission path.
- **Exact next evidence/action:** Map the live terminology authorities and owners before designing a domain-term registry.

### Q6 — Which evaluation outcomes matter most for CCE?

- **Best current answer:** Conformance, semantic fidelity, human comprehension, task success, editing cost, and diagnostic accuracy should remain separate; their priorities are unknown.
- **Confidence:** 92%.
- **Missing evidence/input:** Stakeholder roles, risk classes, representative tasks, and failure-cost weights.
- **Consequence:** A single aggregate score could conceal a regression in the outcome that matters most.
- **Exact next evidence/action:** Approve a risk-weighted evaluation contract before selecting metrics or thresholds.

## Skills used

- `$fpf sota harvest` — routed the request to a plural, provenance-preserving SoTA synthesis with explicit bridges, losses, receiving use, and refresh conditions.

#### FPF sources consulted (4 read; 4 used)

- **G.2 — SoTA Harvester & Synthesis** — used as the primary harvest workflow.
- **C.22.2 — ProblemCard** — used to keep the concern narrow and separate symptoms from mechanisms.
- **A.6.C — Contract Unpacking for Boundaries** — used to keep language rules, admissibility, obligations, and workflow effects distinct.
- **G.4 — CAL Authoring for a CG-Frame** — used to inspect operator, acceptance, evidence, unknown, and conformance-test mechanisms without turning the harvest into a design recommendation.
