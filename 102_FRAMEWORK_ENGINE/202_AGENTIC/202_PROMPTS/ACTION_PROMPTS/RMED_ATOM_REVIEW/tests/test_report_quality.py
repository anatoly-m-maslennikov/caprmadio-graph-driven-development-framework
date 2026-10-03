"""Actual report defects from the same-20 review, reduced to bounded cases."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_split_evaluation import context, contract, part as contract_part  # noqa: E402
from report_quality import validate_report_quality  # noqa: E402


RAW = '# Summary\nValue\n\n## Scope\nobjects and participants\n\n## Claim\na Claim\n\n## Details\n'


def part(**changes):
    finding = {'kind': 'violation', 'location': 'body:4:## Scope',
               'excerpt': 'objects and participants', 'reason': 'unbolded operator',
               'proposed_fix': 'bold and', 'confidence': 1}
    finding.update(changes)
    return {'checks': [{'findings': [finding]}]}


class ReportQualityTests(unittest.TestCase):
    def test_correct_exact_address(self):
        validate_report_quality(part(), RAW)

    def test_rejects_off_by_one_address_even_when_heading_name_matches(self):
        with self.assertRaisesRegex(ValueError, 'unknown body section'):
            validate_report_quality(part(location='body:5:## Scope'), RAW)

    def test_rejects_quote_from_a_different_real_section(self):
        with self.assertRaisesRegex(ValueError, 'absent'):
            validate_report_quality(part(location='body:7:## Claim'), RAW)

    def test_rejects_identical_duplicate_records(self):
        report = part()
        report['checks'][0]['findings'].append(deepcopy(report['checks'][0]['findings'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate finding'):
            validate_report_quality(report, RAW)

    def test_preserves_distinct_locations_for_repeated_text(self):
        raw = RAW.replace('a Claim', 'objects and participants')
        report = part()
        report['checks'][0]['findings'].append(part(location='body:7:## Claim')['checks'][0]['findings'][0])
        validate_report_quality(report, raw)

    def test_does_not_require_absent_property_to_occur_verbatim(self):
        validate_report_quality(part(kind='omission', excerpt='missing required Property'), RAW)

    def test_omission_still_needs_an_existing_body_address(self):
        with self.assertRaisesRegex(ValueError, 'unknown body section'):
            validate_report_quality(part(kind='omission', location='body:5:## Scope',
                                         excerpt='missing required Property'), RAW)


def validated_contract_part(**changes):
    finding = {
        'kind': 'violation',
        'location': 'body:3:## Scope',
        'excerpt': 'Atoms',
        'reason': 'Scope term lacks the required rendering.',
        'proposed_fix': 'Apply the required inline rendering.',
        'confidence': 0.99,
    }
    finding.update(changes)
    response = contract_part('cce')
    response['checks'][0].update(status='failed', findings=[finding])
    response['result'] = 'failed'
    return response


class ReportQualityContractIntegrationTests(unittest.TestCase):
    def test_validate_part_rejects_unknown_body_address(self):
        response = validated_contract_part(location='body:4:## Scope')
        with self.assertRaisesRegex(ValueError, 'unknown body section'):
            contract.validate_part(response, context=context())

    def test_validate_part_rejects_excerpt_from_another_body_section(self):
        response = validated_contract_part(location='body:5:## Claim')
        with self.assertRaisesRegex(ValueError, 'absent'):
            contract.validate_part(response, context=context())

    def test_validate_part_rejects_identical_duplicate_finding_records(self):
        response = validated_contract_part()
        response['checks'][0]['findings'].append(deepcopy(response['checks'][0]['findings'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate finding'):
            contract.validate_part(response, context=context())


if __name__ == '__main__':
    unittest.main()
