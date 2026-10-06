---
subjects:
  declared:
    occurrent:
      - projection-generation
  prerequisite:
    continuant:
      - scope-topology
      - cce-language
cce_version: cce_1
cce_form: method
version: 2
updated_at: 2026-08-25 00:02:08
relations: {}
---
# Derive navigation Projections from the CCE Claim

to derive navigation Projections for an Atom, the Generator must perform all of:

1. read the complete Claim, Claim Scope, and active Type-specific Summary rules.
2. derive one concise Summary that preserves the qualified subject and joint governing effect required for navigation.
3. for a Claim Scope selected by a composite Scope Expression, compress the selected set into a qualified subject without reproducing the selection syntax.
4. for a logically composite Claim, state the joint governing effect without reproducing its logical scaffolding, enumerated values, or subordinate details.
5. reject a Summary that contradicts, adds to, or broadens the Claim or Claim Scope.
6. derive the filename Summary slug and H1 from the Summary.
7. derive every requested Translation from the complete Claim and Claim Scope and not from the Summary.
8. never reconstruct or validate the Claim or Claim Scope from the Summary.
