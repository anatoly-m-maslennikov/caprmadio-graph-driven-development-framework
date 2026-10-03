"""Prompt packaging checks; not a simulated semantic repair run."""
from pathlib import Path
import json
import re
import unittest


class RepairPromptTests(unittest.TestCase):
    def test_citation_repairs_preserve_identity_and_subject_boundaries(self):
        raw = (Path(__file__).parent / 'propose_repair.prompt.md').read_text()
        for token in ('Format citations using supplied labels only',
                      'no target lookup or rename',
                      'Preserve Subject and relation targets',
                      'Summary or genuine Type changes'):
            self.assertIn(token, raw)

    def test_self_contained_preview_contract(self):
        raw = (Path(__file__).parent / 'propose_repair.prompt.md').read_text()
        self.assertTrue(raw.startswith('# System Prompt\n'))
        self.assertEqual(re.findall(r'^### (\d+)\)', raw, re.M), [str(i) for i in range(1, 10)])
        self.assertLess(len(raw.split()), 850)
        for token in ('inline original text', 'source_mutation', 'separately authorized work',
                      'zero-based finding_index', 'No web', 'independent local evaluation'):
            self.assertIn(token, raw)

    def test_default_workflow_uses_confirmed_findings_without_legacy_preview_gate(self):
        raw = (Path(__file__).parent.parent / 'CA-O-110.prompt.md').read_text()
        for token in ('confirmed report findings', 'caller-granted permission',
                      'Never replay a completed effect', 'fixed_not_rechecked'):
            self.assertIn(token, raw)
        self.assertNotIn('repair_gate.admit_proposal', raw)
        self.assertNotIn('propose_repair.prompt.md', raw)

    def test_output_assessment_is_after_generation_not_a_circular_input(self):
        raw = (Path(__file__).parent / 'propose_repair.prompt.md').read_text()
        for token in ('After candidate generation', 'not prerequisites for generating',
                      'caller-owned', 'provisional'):
            self.assertIn(token, raw)

    def test_canonical_change_authority_is_in_the_delivery_manifest(self):
        manifest = json.loads((Path(__file__).parent.parent / 'source_bindings.json').read_text())
        identifiers = {binding['atom_id'] for binding in manifest['sources']}
        self.assertTrue({'CA-O-067', 'CA-R-1432', 'CA-R-1464', 'CA-R-1766',
                         'CA-R-1700', 'CA-D-276', 'CA-D-283'} <= identifiers)

    def test_recoding_prompt_preserves_identity_and_composes_final_candidate(self):
        raw = (Path(__file__).parent / 'propose_repair.prompt.md').read_text()
        for token in ('recoding require carrier_only', 'CA-R-1766',
                      'Preserve all other non-timestamp frontmatter and body bytes',
                      'Keep the path unchanged', 'never a specialized Type',
                      'complete original-to-final', 'every confirmed finding',
                      'composed revision may combine'):
            self.assertIn(token, raw)
        self.assertNotIn('Keep recoding separate from content or Subject repairs', raw)


if __name__ == '__main__':
    unittest.main()
