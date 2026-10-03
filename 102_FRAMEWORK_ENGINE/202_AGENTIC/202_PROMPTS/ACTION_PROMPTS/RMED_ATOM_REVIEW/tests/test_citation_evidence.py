"""Admission tests for readable citation labels in Subject review evidence."""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from context_builder import body_sections, markdown  # noqa: E402
from review_evidence import validate_subject_inventory  # noqa: E402
from test_split_evaluation import context, source, RULE_TEXT  # noqa: E402


ATOM_ID = 'CA-R-200'
SUMMARY = 'Retire tool reference'
LABEL = f'{ATOM_ID}-TOOLS--retire-tool-reference'
SOURCE_PATH = f'authority/04_requirement/{LABEL}.md'


def authority(*, legacy: bool = False) -> str:
    heading = f'# {SUMMARY}' if legacy else f'# Summary\n{SUMMARY}'
    return (
        '---\n'
        f'atom_id: "{ATOM_ID}"\n'
        'version: 1\n'
        'status: "Active"\n'
        'content_role: "Requirement"\n'
        'subjects:\n'
        '  governs: "Atom"\n'
        '---\n'
        f'{heading}\n\n'
        '## Claim\n\n'
        'Atom means the selected governed statement.\n'
    )


def candidate(*, extra_prose: bool = False, repeat_label: bool = False,
              label: str = LABEL) -> str:
    suffix = ' TOOLS remains a substantive execution reference.' if extra_prose else ''
    repeated = f' Repeat {label}.' if repeat_label else ''
    return (
        '---\n'
        'subjects:\n'
        '  governs: "Atom"\n'
        '  depends_on:\n'
        '    - "TOOLS"\n'
        '---\n'
        '# Summary\n'
        'Atom instruction\n\n'
        '## Claim\n'
        f'See {label}.{repeated}{suffix}\n'
    )


def section(raw: str, title: str) -> str:
    return next(address for address in body_sections(raw) if address.endswith(title))


def row(raw: str, *, span_text: str = LABEL, filename: str = LABEL,
        authority_ref: str = f'{ATOM_ID}@1', citation_atom_id: str = ATOM_ID,
        span_section: str | None = None, offset_delta: int = 0,
        label_in_candidate: str = LABEL) -> dict:
    markdown_body = markdown(raw)
    start = markdown_body.index(label_in_candidate) + offset_delta
    claim = section(raw, '## Claim')
    return {
        'status': 'failed',
        'findings': [{'kind': 'violation', 'subject_issue': 'extra', 'entity': 'TOOLS'}],
        'subject_inventory': {
            'complete': True,
            'sections_reviewed': body_sections(raw),
            'mentions': [
                {
                    'location': section(raw, '# Summary'),
                    'excerpt': 'Atom',
                    'entity': 'Atom',
                    'resolution': 'resolved',
                    'resolution_basis': 'meaning',
                    'rationale': 'The candidate directly names the bound governed Entity.',
                    'definitions': [{'authority': f'{ATOM_ID}@1',
                                     'excerpt': 'Atom means the selected governed statement.'}],
                },
                {
                    'location': claim,
                    'excerpt': f'See {label_in_candidate}.',
                    'entity': None,
                    'resolution': 'general',
                    'rationale': 'The reviewer classifies this readable source label as citation-only.',
                    'definitions': [],
                    'citation_evidence': {
                        'authority': authority_ref,
                        'atom_id': citation_atom_id,
                        'filename': filename,
                        'spans': [{
                            'section': span_section or claim,
                            'start': start,
                            'end': start + len(span_text),
                            'text': span_text,
                        }],
                    },
                },
            ],
        },
    }


class CitationEvidenceTests(unittest.TestCase):
    def validate(self, raw: str, record: dict, *, source: str | None = None,
                 paths: dict | None = None) -> None:
        validate_subject_inventory(
            record, raw, {f'{ATOM_ID}@1': source or authority()}, {f'{ATOM_ID}@1': 'Atom'},
            authority_paths={f'{ATOM_ID}@1': SOURCE_PATH} if paths is None else paths)

    def test_exact_bound_filename_exempts_only_the_citation_label(self):
        raw = candidate()
        for legacy in (False, True):
            with self.subTest(legacy=legacy):
                self.validate(raw, row(raw), source=authority(legacy=legacy))

    def test_noncanonical_labels_cannot_supply_citation_exclusions(self):
        for label in (ATOM_ID, f'{ATOM_ID} — {SUMMARY}', f'{LABEL}.md', SOURCE_PATH,
                      LABEL.lower(), LABEL.replace('-TOOLS', ''), LABEL + '-extra'):
            with self.subTest(label=label):
                raw = candidate(label=label)
                report = row(raw, span_text=label, label_in_candidate=label)
                with self.assertRaisesRegex(ValueError, 'exact bound filename without .md'):
                    self.validate(raw, report)

    def test_forged_filename_or_unbound_source_is_rejected(self):
        raw = candidate()
        altered = row(raw, filename=f'{ATOM_ID}--invented-filename')
        with self.assertRaisesRegex(ValueError, 'filename differs'):
            self.validate(raw, altered)
        unbound = row(raw, authority_ref='CA-R-999@1')
        with self.assertRaisesRegex(ValueError, 'not bound'):
            self.validate(raw, unbound)

    def test_wrong_citation_section_is_rejected_even_when_the_label_exists_elsewhere(self):
        raw = candidate()
        report = row(raw, span_section=section(raw, '# Summary'))
        with self.assertRaisesRegex(ValueError, 'invalid Markdown section'):
            self.validate(raw, report)

    def test_wrong_offset_or_unknown_atom_id_is_rejected(self):
        raw = candidate()
        with self.assertRaisesRegex(ValueError, 'exact bound filename without .md'):
            self.validate(raw, row(raw, offset_delta=1))
        with self.assertRaisesRegex(ValueError, 'exact bound Atom source'):
            self.validate(raw, row(raw, citation_atom_id='CA-R-999'))

    def test_a_separate_substantive_occurrence_still_prevents_extra_target_removal(self):
        raw = candidate(extra_prose=True)
        with self.assertRaisesRegex(ValueError, 'literal Markdown occurrence'):
            self.validate(raw, row(raw))

    def test_repeated_label_needs_every_occurrence_to_be_proven_citation_span(self):
        raw = candidate(repeat_label=True)
        with self.assertRaisesRegex(ValueError, 'literal Markdown occurrence'):
            self.validate(raw, row(raw))

    def test_filename_is_not_reconstructed_from_the_source_summary(self):
        raw = candidate()
        # Source Summary/layout validity is a separate check, not citation proof.
        self.validate(raw, row(raw), source=authority().replace(SUMMARY, 'Different source heading'))

    def test_missing_or_stale_source_path_fails_closed(self):
        raw = candidate()
        for paths in ({}, {f'{ATOM_ID}@1': 'no-markdown.txt'}):
            with self.subTest(paths=paths), self.assertRaisesRegex(ValueError, 'bound Markdown Carrier path'):
                self.validate(raw, row(raw), paths=paths)
        with self.assertRaisesRegex(ValueError, 'filename differs'):
            self.validate(raw, row(raw), paths={f'{ATOM_ID}@1': 'renamed.md'})

    def test_ambiguous_basename_fails_closed(self):
        raw = candidate()
        with self.assertRaisesRegex(ValueError, 'ambiguous across bound sources'):
            validate_subject_inventory(
                row(raw), raw,
                {f'{ATOM_ID}@1': authority(), 'CA-R-999@1': authority().replace(ATOM_ID, 'CA-R-999')},
                {f'{ATOM_ID}@1': 'Atom'},
                authority_paths={f'{ATOM_ID}@1': SOURCE_PATH, 'CA-R-999@1': f'other/{LABEL}.md'})

    def test_context_path_admission_rejects_report_owned_path_changes(self):
        bound = source('rule.md', 'MOCK-R-002', RULE_TEXT)['binding']
        self.assertEqual(context().authority_paths([bound]), {'MOCK-R-002@1': 'rule.md'})
        with self.assertRaisesRegex(ValueError, 'unbound or changed source'):
            context().authority_paths([{**bound, 'path': 'report-chosen-name.md'}])

    def test_citation_evidence_cannot_be_attached_to_a_resolved_entity_mention(self):
        raw = candidate()
        report = row(raw)
        citation = report['subject_inventory']['mentions'][1]
        citation.update(entity='TOOLS', resolution='resolved', resolution_basis='meaning',
                        definitions=[{'authority': f'{ATOM_ID}@1',
                                      'excerpt': 'Atom means the selected governed statement.'}])
        with self.assertRaisesRegex(ValueError, 'only allowed on a general non-Entity'):
            self.validate(raw, report)


if __name__ == '__main__':
    unittest.main()
