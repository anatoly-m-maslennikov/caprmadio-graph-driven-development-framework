"""Explicit text admission is not Atom identity, activation, or global authority."""
from copy import deepcopy
import unittest

from test_split_evaluation import source, SOURCE_TEXT, part
from context_builder import prepare_context
from review_evidence import ReviewContext, validate_quotes
from evaluation_contract import validate_part


class PrincipleCitations(unittest.TestCase):
    def packet(self):
        candidate = source('candidate.md', 'TEST-R-1', SOURCE_TEXT)
        legacy = source('legacy-principle.md', None, '# Preserve information\nKeep valuable evidence.\n')
        legacy['binding']['version'] = None
        return {
            'confidence_threshold': .99, 'sources': [candidate, legacy],
            'authority_bindings': [legacy['binding']],
            'candidate_bindings': [candidate['binding']],
            'principle_admissions': [{
                'binding': legacy['binding'], 'applicable_to': ['candidate.md'],
                'reason': 'Evaluate alignment with this exact text.',
                'provenance': 'Fixture Operator explicitly approved text use only.',
            }],
        }

    def test_explicit_legacy_text_uses_path_and_hash_without_assigning_identity(self):
        packet = prepare_context(self.packet())
        candidate, legacy = packet['sources']
        ctx = ReviewContext(packet)
        refs = ctx.authorities([legacy['binding']], candidate=candidate['binding'])
        expected = f'source:{legacy["binding"]["path"]}#sha256={legacy["binding"]["sha256"]}'
        self.assertEqual(refs, {expected: legacy['text']})
        self.assertEqual(packet['applicable_principles'][0]['reference'], expected)
        self.assertIsNone(legacy['binding']['atom_id'])
        self.assertNotIn('status:', legacy['text'])
        validate_quotes([{'authority': expected, 'excerpt': 'Keep valuable evidence.'}], refs)

    def test_binding_alone_does_not_admit_legacy_authority(self):
        packet = self.packet()
        del packet['principle_admissions']
        ctx = ReviewContext(packet)
        with self.assertRaisesRegex(ValueError, 'carried identity'):
            ctx.authorities([packet['sources'][1]['binding']], candidate=packet['sources'][0]['binding'])

    def test_candidate_is_required_for_admitted_principle(self):
        packet = self.packet()
        ctx = ReviewContext(packet)
        with self.assertRaisesRegex(ValueError, 'candidate'):
            ctx.authorities([packet['sources'][1]['binding']])

    def test_admission_does_not_bypass_authority_allowlist(self):
        packet = self.packet()
        packet['authority_bindings'] = []
        for call in (prepare_context, ReviewContext):
            with self.assertRaisesRegex(ValueError, 'authority allowlist'):
                call(packet)

    def test_legacy_text_needs_an_explicit_authority_allowlist(self):
        packet = self.packet()
        del packet['authority_bindings']
        for call in (prepare_context, ReviewContext):
            with self.assertRaisesRegex(ValueError, 'authority allowlist'):
                call(packet)

    def test_unidentified_principle_needs_exact_selected_candidates(self):
        packet = self.packet()
        del packet['candidate_bindings']
        with self.assertRaisesRegex(ValueError, 'candidate_bindings'):
            prepare_context(packet)

    def test_authority_only_source_cannot_be_a_selected_candidate(self):
        packet = self.packet()
        packet['principle_admissions'][0]['applicable_to'] = ['legacy-principle.md']
        with self.assertRaisesRegex(ValueError, 'applicability'):
            prepare_context(packet)
        packet = self.packet()
        ctx = ReviewContext(packet)
        with self.assertRaisesRegex(ValueError, 'not a selected evaluation candidate'):
            ctx.candidate_text(packet['sources'][1]['binding'])

    def test_admission_cannot_leak_to_another_candidate(self):
        packet = self.packet()
        other = source('other.md', 'TEST-R-2', SOURCE_TEXT)
        packet['sources'].append(other)
        packet['candidate_bindings'].append(other['binding'])
        ctx = ReviewContext(packet)
        with self.assertRaisesRegex(ValueError, 'applicability'):
            ctx.authorities([packet['sources'][1]['binding']], candidate=other['binding'])

    def test_carried_principle_identity_retains_standard_reference(self):
        packet = self.packet()
        binding = packet['sources'][1]['binding']
        binding.update(atom_id='TEST-M-1', version=1)
        ctx = ReviewContext(packet)
        self.assertEqual(list(ctx.authorities([binding], candidate=packet['sources'][0]['binding'])), ['TEST-M-1@1'])

    def test_invalid_admission_is_rejected_not_silently_ignored(self):
        for field, invalid in (
            ('provenance', ''), ('reason', ' '), ('applicable_to', 'candidate.md'),
            ('applicable_to', []), ('applicable_to', ['absent.md']),
            ('applicable_to', ['candidate.md', 'candidate.md']),
        ):
            with self.subTest(field=field, value=invalid):
                packet = self.packet()
                packet['principle_admissions'][0][field] = invalid
                with self.assertRaises(ValueError):
                    prepare_context(packet)
                with self.assertRaises(ValueError):
                    ReviewContext(packet)

    def test_changed_text_binding_or_candidate_is_rejected(self):
        packet = self.packet()
        packet['principle_admissions'][0]['binding'] = dict(packet['sources'][1]['binding'], sha256='0' * 64)
        with self.assertRaises(ValueError):
            prepare_context(packet)
        packet = self.packet()
        candidate = deepcopy(packet['sources'][0]['binding'])
        candidate['sha256'] = '0' * 64
        with self.assertRaises(ValueError):
            ReviewContext(packet).authorities([packet['sources'][1]['binding']], candidate=candidate)

    def test_report_admission_passes_candidate_binding_to_citation_validation(self):
        packet = prepare_context(self.packet())
        ctx = ReviewContext(packet)
        response = part('properties')
        response.update(source=packet['sources'][0]['binding'], context_sha256=ctx.sha256,
                        authority_sources=[packet['sources'][1]['binding']])
        response['checks'][0]['authority'] = [packet['applicable_principles'][0]['reference']]
        validate_part(response, context=ctx)


if __name__ == '__main__':
    unittest.main()
