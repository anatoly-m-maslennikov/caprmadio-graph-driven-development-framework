"""Adversarial coverage tests for qualified literal extra-Subject evidence."""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from context_builder import body_sections, markdown  # noqa: E402
from review_evidence import validate_subject_inventory  # noqa: E402


AUTHORITY = 'MOCK-R-QUALIFIED@1'
DEFINITION = 'Atom/Claim means the independently replaceable Claim owned by an Atom.'
AUTHORITY_TEXT = (
    '---\natom_id: MOCK-R-QUALIFIED\nversion: 1\nstatus: Active\ncontent_role: Requirement\n'
    'subjects:\n  governs: Atom/Claim\n---\n# Summary\nQualified definition\n'
    '## Scope\nAtoms\n## Claim\n' + DEFINITION + '\n## Details\n'
)
PHRASE = 'Each Atom retains its one independently replaceable Claim.'


def raw(*, extra=''):
    return ('---\nsubjects:\n  governs: Atom/Claim\n  depends_on: [Claim]\n---\n'
            '# Keep each Atom semantically irreducible\n\n' + PHRASE + '\n' + extra)


def report(source, *, entity='Atom/Claim', basis='meaning'):
    body = markdown(source)
    start = body.index(PHRASE)
    claim = body.index('Claim', start)
    mention = {
        'location': 'Keep each Atom semantically irreducible', 'excerpt': PHRASE, 'entity': entity,
        'resolution': 'resolved', 'resolution_basis': basis,
        'rationale': 'Independent authority resolves this exact phrase as the qualified Entity.',
        'definitions': [{'authority': AUTHORITY,
                         'excerpt': DEFINITION}],
        'declared_subject_evidence': {'entity': entity, 'authority': AUTHORITY, 'excerpt': DEFINITION},
        'qualified_literal_evidence': {
            'declared_entity': 'Claim',
            'mention_span': {'section': 'body:1:# Keep each Atom semantically irreducible', 'start': start, 'end': start + len(PHRASE), 'text': PHRASE},
            'literal_spans': [{'section': 'body:1:# Keep each Atom semantically irreducible', 'start': claim, 'end': claim + len('Claim'), 'text': 'Claim'}],
        },
    }
    return {
        'status': 'failed', 'findings': [{'kind': 'violation', 'subject_issue': 'extra', 'entity': 'Claim'}],
        'subject_inventory': {'complete': True, 'sections_reviewed': body_sections(source), 'mentions': [mention]},
    }


class QualifiedLiteralEvidenceTests(unittest.TestCase):
    def validate(self, source, record):
        entity = record['subject_inventory']['mentions'][0]['entity']
        validate_subject_inventory(
            record, source, {AUTHORITY: AUTHORITY_TEXT}, {AUTHORITY: entity},
            candidate_binding={'atom_id': 'CANDIDATE', 'version': 1, 'path': 'candidate.md', 'sha256': '0' * 64})

    def test_exact_resolved_meaning_mention_accounts_for_its_qualified_literal(self):
        self.validate(raw(), report(raw()))

    def test_independent_bare_occurrence_remains_an_extra_literal_error(self):
        source = raw(extra='A separate Claim remains independently mentioned.\n')
        with self.assertRaisesRegex(ValueError, 'literal Markdown occurrence'):
            self.validate(source, report(source))

    def test_identity_basis_cannot_supply_qualification(self):
        source = raw()
        with self.assertRaisesRegex(ValueError, 'identity recognition|meaning'):
            self.validate(source, report(source, basis='identity'))

    def test_nonterminal_qualified_target_cannot_qualify_declared_terminal(self):
        source = raw()
        item = report(source, entity='Atom/Claim/Part')
        with self.assertRaisesRegex(ValueError, 'terminal|exact Entity path'):
            self.validate(source, item)

    def test_cross_section_and_out_of_range_mention_spans_fail(self):
        source = raw()
        for mutate in (
            lambda item: item['subject_inventory']['mentions'][0]['qualified_literal_evidence']['mention_span'].update(section='body:preamble'),
            lambda item: item['subject_inventory']['mentions'][0]['qualified_literal_evidence']['mention_span'].update(end=10**6),
        ):
            item = report(source)
            mutate(item)
            with self.subTest(mutate=mutate), self.assertRaisesRegex(ValueError, 'qualified literal'):
                self.validate(source, item)

    def test_duplicate_partial_and_omitted_literal_spans_fail(self):
        source = raw()
        for mutate in (
            lambda q: q['literal_spans'].append(dict(q['literal_spans'][0])),
            lambda q: q['literal_spans'][0].update(end=q['literal_spans'][0]['end'] - 1, text='Clai'),
            lambda q: q.update(literal_spans=[]),
        ):
            item = report(source)
            mutate(item['subject_inventory']['mentions'][0]['qualified_literal_evidence'])
            with self.subTest(mutate=mutate), self.assertRaisesRegex(ValueError, 'qualified literal'):
                self.validate(source, item)

    def test_citation_evidence_cannot_be_recast_as_qualified_literal_evidence(self):
        source = raw()
        item = report(source)
        item['subject_inventory']['mentions'][0]['qualified_literal_evidence']['citation_evidence'] = {}
        with self.assertRaisesRegex(ValueError, 'qualified literal'):
            self.validate(source, item)

    def test_candidate_self_proof_is_rejected_before_qualified_spans(self):
        source = raw()
        item = report(source)
        mention = item['subject_inventory']['mentions'][0]
        candidate = AUTHORITY_TEXT.replace('MOCK-R-QUALIFIED', 'CANDIDATE')
        mention['definitions'] = [{'authority': 'CANDIDATE@1', 'excerpt': DEFINITION}]
        mention['declared_subject_evidence'] = {'entity': 'Atom/Claim', 'authority': 'CANDIDATE@1', 'excerpt': DEFINITION}
        with self.assertRaisesRegex(ValueError, 'candidate'):
            validate_subject_inventory(
                item, source,
                {AUTHORITY: AUTHORITY_TEXT, 'CANDIDATE@1': candidate},
                {AUTHORITY: 'Atom/Claim', 'CANDIDATE@1': 'Atom/Claim'},
                candidate_binding={'atom_id': 'CANDIDATE', 'version': 1, 'path': 'candidate.md', 'sha256': '0' * 64},
            )

    def test_malformed_optional_evidence_fails_even_without_extra_finding(self):
        source = raw()
        item = report(source)
        item['findings'] = []
        item['subject_inventory']['mentions'][0]['qualified_literal_evidence']['literal_spans'] = []
        with self.assertRaisesRegex(ValueError, 'qualified literal'):
            self.validate(source, item)

    def test_null_or_missing_declared_subject_proof_fails_closed(self):
        source = raw()
        item = report(source)
        item['subject_inventory']['mentions'][0]['qualified_literal_evidence'] = None
        with self.assertRaisesRegex(ValueError, 'invalid qualified literal'):
            self.validate(source, item)
        item = report(source)
        del item['subject_inventory']['mentions'][0]['declared_subject_evidence']
        with self.assertRaisesRegex(ValueError, 'declared Subject meaning evidence'):
            self.validate(source, item)

    def test_null_evidence_is_rejected_without_an_extra_finding(self):
        source = raw()
        item = report(source)
        item['findings'] = []
        item['subject_inventory']['mentions'][0]['qualified_literal_evidence'] = None
        with self.assertRaisesRegex(ValueError, 'invalid qualified literal'):
            self.validate(source, item)

    def test_unicode_prefix_uses_codepoint_offsets_not_utf8_byte_offsets(self):
        source = raw().replace(PHRASE, 'λ😀 ' + PHRASE)
        body = markdown(source)
        item = report(source)
        span = item['subject_inventory']['mentions'][0]['qualified_literal_evidence']['mention_span']
        self.assertEqual(span['start'], body.index(PHRASE))
        self.validate(source, item)
        span['start'] += 3  # UTF-8 byte surplus for the two-codepoint prefix.
        with self.assertRaisesRegex(ValueError, 'qualified literal mention span'):
            self.validate(source, item)

    def test_declared_proof_requires_active_complete_claim_and_distinct_atom(self):
        source = raw()
        cases = (
            (AUTHORITY_TEXT.replace('status: Active', 'status: Draft'), 'Active RMEDO'),
            (AUTHORITY_TEXT.replace('## Claim\n', '## Summary\n'), 'asserted Claim context|substantive body'),
            (AUTHORITY_TEXT.replace(DEFINITION, DEFINITION + ' More context.'), 'complete asserted'),
        )
        for authority, error in cases:
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                item = report(source)
                validate_subject_inventory(
                    item, source, {AUTHORITY: authority}, {AUTHORITY: 'Atom/Claim'},
                    candidate_binding={'atom_id': 'CANDIDATE', 'version': 1, 'path': 'candidate.md', 'sha256': '0' * 64})
        alias = AUTHORITY_TEXT.replace('MOCK-R-QUALIFIED', 'CANDIDATE')
        item = report(source)
        mention = item['subject_inventory']['mentions'][0]
        mention['definitions'][0]['authority'] = 'ALIAS@1'
        mention['declared_subject_evidence']['authority'] = 'ALIAS@1'
        with self.assertRaisesRegex(ValueError, 'same-Atom candidate alias'):
            validate_subject_inventory(
                item, source, {'ALIAS@1': alias}, {'ALIAS@1': 'Atom/Claim'},
                candidate_binding={'atom_id': 'CANDIDATE', 'version': 1, 'path': 'candidate.md', 'sha256': '0' * 64})


if __name__ == '__main__':
    unittest.main()
