"""Resolved Subject evidence needs one exact anchor, with bound supplements."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from review_evidence import _validate_resolved_mention  # noqa: E402


def authority(target, body):
    return (
        '---\n'
        'subjects:\n'
        f'  governs: {json.dumps(target)}\n'
        '---\n'
        '# Definition\n\n'
        + body
    )


def mention(entity, definitions):
    return {
        'entity': entity,
        'resolution_basis': 'meaning',
        'definitions': definitions,
    }


class EntityEvidenceBundleTests(unittest.TestCase):
    def test_explicit_value_registration_composes_a_qualified_entity(self):
        prop = 'Atom/Content Role: Evaluation/Type'
        quote = (f'QA Case **and** Evaluation Control **must** be registered '
                 f'as internal values of `{prop}`.')
        raw = authority(prop, quote).replace(
            'subjects:\n', 'status: Active\ncontent_role: Requirement\nsubjects:\n', 1)
        item = mention(prop + ': Evaluation Control', [{
            'authority': 'REGISTER@1', 'excerpt': quote,
        }])
        item['allowed_value_evidence'] = {
            'property': prop, 'value': 'Evaluation Control',
            'authority': 'REGISTER@1', 'excerpt': quote,
        }
        _validate_resolved_mention(item, {'REGISTER@1': raw}, {'REGISTER@1': prop})

    def test_value_registration_does_not_admit_wrong_qualified_bearer(self):
        prop = 'Atom/Content Role: Evaluation/Type'
        quote = (f'QA Case **and** Evaluation Control **must** be registered '
                 f'as internal values of `{prop}`.')
        raw = authority(prop, quote).replace(
            'subjects:\n', 'status: Active\ncontent_role: Requirement\nsubjects:\n', 1)
        item = mention('Atom/Content Role: Requirement/Type: Evaluation Control', [{
            'authority': 'REGISTER@1', 'excerpt': quote,
        }])
        item['allowed_value_evidence'] = {
            'property': prop, 'value': 'Evaluation Control',
            'authority': 'REGISTER@1', 'excerpt': quote,
        }
        with self.assertRaises(ValueError):
            _validate_resolved_mention(item, {'REGISTER@1': raw}, {'REGISTER@1': prop})

    def test_cce_identity_accepts_active_method_authority_without_r_definition(self):
        quote = 'To write a Claim in CAPRMEDIO Controlled English (CCE), use its identified language version.'
        raw = authority('CCE', quote).replace(
            'subjects:\n', 'status: Active\ncontent_role: Method\ntype: Method\nsubjects:\n', 1)
        item = mention('CCE', [{'authority': 'MOCK-M-001@1', 'excerpt': quote}])
        item.update(resolution_basis='identity', excerpt='write the complete Claim in the current CCE version')
        _validate_resolved_mention(item, {'MOCK-M-001@1': raw}, {'MOCK-M-001@1': 'CCE'})

    def test_cce_method_still_needs_its_exact_governing_target(self):
        quote = 'To write a Claim in CAPRMEDIO Controlled English (CCE), use its identified language version.'
        raw = authority('language', quote).replace(
            'subjects:\n', 'status: Active\ncontent_role: Method\nsubjects:\n', 1)
        item = mention('CCE', [{'authority': 'MOCK-M-001@1', 'excerpt': quote}])
        item.update(resolution_basis='identity', excerpt='write the complete Claim in the current CCE version')
        with self.assertRaisesRegex(ValueError, 'exact full Entity authority anchor'):
            _validate_resolved_mention(item, {'MOCK-M-001@1': raw}, {'MOCK-M-001@1': 'language'})

    def test_draft_method_is_not_silently_promoted_to_identity_authority(self):
        quote = 'To write a Claim in CCE, use its identified language version.'
        raw = authority('CCE', quote).replace(
            'subjects:\n', 'status: Draft\ncontent_role: Method\nsubjects:\n', 1)
        item = mention('CCE', [{'authority': 'MOCK-M-001@1', 'excerpt': quote}])
        item.update(resolution_basis='identity', excerpt='write the complete Claim in the current CCE version')
        with self.assertRaisesRegex(ValueError, 'explicit Active authority'):
            _validate_resolved_mention(item, {'MOCK-M-001@1': raw}, {'MOCK-M-001@1': 'CCE'})

    def test_subject_anchor_accepts_subject_path_supplement(self):
        authorities = {
            'SUBJECT@1': authority('Subject', 'Subject identifies the governed conceptual bearer.'),
            'SUBJECT_PATH@1': authority('SubjectPath', 'SubjectPath records the qualified path composition.'),
        }
        _validate_resolved_mention(mention('Subject', [
            {'authority': 'SUBJECT@1', 'excerpt': 'Subject identifies the governed conceptual bearer.'},
            {'authority': 'SUBJECT_PATH@1', 'excerpt': 'SubjectPath records the qualified path composition.'},
        ]), authorities, {'SUBJECT@1': 'Subject', 'SUBJECT_PATH@1': 'SubjectPath'})

    def test_bundle_without_an_exact_anchor_is_rejected(self):
        for target, entity, body in (
            ('SubjectPath', 'Subject', 'SubjectPath records the qualified path composition.'),
            ('Usage', 'AI Agent', 'Usage records the observed execution context.'),
        ):
            with self.subTest(target=target, entity=entity):
                reference = target.upper() + '@1'
                authorities = {reference: authority(target, body)}
                with self.assertRaisesRegex(ValueError, 'authority anchor'):
                    _validate_resolved_mention(mention(entity, [{
                        'authority': reference,
                        'excerpt': body,
                    }]), authorities, {reference: target})

    def test_artifact_authority_cannot_admit_an_atom_revision(self):
        authorities = {
            'ARTIFACT@1': authority('Artifact', 'An Atom revision is a tracked Artifact revision record.'),
        }
        with self.assertRaisesRegex(ValueError, 'authority anchor'):
            _validate_resolved_mention(mention('Atom', [{
                'authority': 'ARTIFACT@1',
                'excerpt': 'An Atom revision is a tracked Artifact revision record.',
            }]), authorities, {'ARTIFACT@1': 'Artifact'})

    def test_journal_authority_cannot_admit_an_event_identity(self):
        authorities = {
            'JOURNAL@1': authority('Journal', 'Journal: Event identity records the journal event entry.'),
        }
        with self.assertRaisesRegex(ValueError, 'authority anchor'):
            _validate_resolved_mention(mention('Journal: Event identity', [{
                'authority': 'JOURNAL@1',
                'excerpt': 'Journal: Event identity records the journal event entry.',
            }]), authorities, {'JOURNAL@1': 'Journal'})

    def test_qualified_suffix_substring_coincidence_is_not_an_anchor(self):
        authorities = {
            'JOURNAL@1': authority('Journal', 'Journal: Event identity records the journal event entry.'),
        }
        with self.assertRaisesRegex(ValueError, 'authority anchor'):
            _validate_resolved_mention(mention('Journal: Event', [{
                'authority': 'JOURNAL@1',
                'excerpt': 'Journal: Event identity records the journal event entry.',
            }]), authorities, {'JOURNAL@1': 'Journal'})

    def test_exact_qualified_target_accepts_bound_supplement(self):
        authorities = {
            'SUBJECT_ALLOWED@1': authority('Subject: allowed', 'Subject: allowed is the admitted qualified value.'),
            'COMPOSITION@1': authority('Composition', 'Composition explains how the qualified value is assembled.'),
        }
        _validate_resolved_mention(mention('Subject: allowed', [
            {'authority': 'SUBJECT_ALLOWED@1', 'excerpt': 'Subject: allowed is the admitted qualified value.'},
            {'authority': 'COMPOSITION@1', 'excerpt': 'Composition explains how the qualified value is assembled.'},
        ]), authorities, {'SUBJECT_ALLOWED@1': 'Subject: allowed', 'COMPOSITION@1': 'Composition'})


if __name__ == '__main__':
    unittest.main()
