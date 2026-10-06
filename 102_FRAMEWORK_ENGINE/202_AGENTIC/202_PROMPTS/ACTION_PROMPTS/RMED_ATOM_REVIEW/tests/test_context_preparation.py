"""Regressions for context retrieval and evidence, not simulated LLM judgment."""
import copy
from pathlib import Path
import tempfile
import unittest

from test_split_evaluation import context, contract, part, source, RULE_TEXT, SOURCE_TEXT
from context_builder import prepare_context, lookup, prose, rebuild_baseline


TMPDIR = Path(__file__).resolve().parents[6] / '.caprmedio_tmp/epic-resume-prompts'
TMPDIR.mkdir(parents=True, exist_ok=True)


class ContextPreparation(unittest.TestCase):
    def test_manifest_baseline_uses_bound_text_not_previous_convenience_copy(self):
        canonical = source('rule.md', 'MOCK-R-002', RULE_TEXT)
        packet = {'sources': [canonical], 'baseline': [{'raw': 'obsolete'}]}
        manifest = {'sources': [canonical['binding']]}
        rebuild_baseline(packet, manifest)
        self.assertEqual(packet['baseline'], [{'source': canonical['binding'], 'raw': RULE_TEXT}])
        self.assertEqual(packet['source_bindings_manifest'], manifest)
        self.assertIsNot(packet['source_bindings_manifest'], manifest)

    def test_manifest_baseline_rejects_missing_stale_and_duplicate_sources(self):
        canonical = source('rule.md', 'MOCK-R-002', RULE_TEXT)
        for sources, bindings in (
            ([], [canonical['binding']]),
            ([dict(canonical, text='stale')], [canonical['binding']]),
            ([canonical, canonical], [canonical['binding']]),
            ([canonical], [canonical['binding'], canonical['binding']]),
        ):
            with self.subTest(sources=sources, bindings=bindings), self.assertRaises(ValueError):
                rebuild_baseline({'sources': sources}, {'sources': bindings})

    def test_baseline_raw_must_equal_its_canonical_bound_source(self):
        canonical = source('rule.md', 'MOCK-R-002', RULE_TEXT)
        packet = {
            'confidence_threshold': .99,
            'sources': [canonical],
            'baseline': [{'source': canonical['binding'], 'raw': canonical['text']}],
        }
        prepared = prepare_context(packet)
        self.assertEqual(prepared['baseline'], packet['baseline'])
        contract.ReviewContext(packet)

        stale = copy.deepcopy(packet)
        stale['baseline'][0]['raw'] = RULE_TEXT.replace('Atom means', 'Atom formerly meant')
        for prepare in (prepare_context, contract.ReviewContext):
            with self.subTest(prepare=prepare.__name__), self.assertRaisesRegex(
                ValueError, 'baseline source/raw contradicts canonical sources'
            ):
                prepare(stale)

    def test_bound_candidate_is_not_automatically_authority(self):
        admitted = source('rule.md', 'MOCK-R-002', RULE_TEXT)
        candidate = source('candidate.md', 'MOCK-R-003', RULE_TEXT)
        packet = prepare_context({'confidence_threshold': .99,
            'sources': [admitted, candidate], 'authority_bindings': [admitted['binding']]})
        self.assertEqual([admitted['binding']], [row['binding'] for row in packet['entity_index']])
        ctx = contract.ReviewContext(packet)
        with self.assertRaisesRegex(ValueError, 'not admitted as authority'):
            ctx.authorities([candidate['binding']])
        self.assertIn('MOCK-R-002@1', ctx.authorities([admitted['binding']]))

    def test_index_is_retrieval_not_a_definition(self):
        raw = '---\nstatus: active\nsubjects:\n  governs: Atom\n---\n# Atom\n\nAn Atom means a governed Artifact.\n'
        packet = prepare_context({'confidence_threshold': .99, 'sources': [source('a.md', 'A', raw)]})
        records = lookup(packet, 'Atom')
        self.assertEqual(records[0]['entity'], 'Atom')
        self.assertIn('An Atom means', records[0]['body'])
        self.assertNotIn('status:', records[0]['body'])
        self.assertEqual(records[0]['admission'], 'retrieval_candidate_not_definition_proof')

    def test_missing_and_available_resources_are_distinct(self):
        with tempfile.TemporaryDirectory(dir=TMPDIR, ignore_cleanup_errors=True) as folder:
            root = Path(folder)
            (root / 'structure.toml').write_text('[[scope_units]]\nscope_unit_name="PROJECT"\n')
            p = {'confidence_threshold': .99, 'sources': [source('a.md', 'A', RULE_TEXT)]}
            out = prepare_context(p, root=root, resources={
                'project_structure': 'structure.toml', 'operators_registry': 'absent.toml'})
            self.assertEqual(out['preflight']['project_structure']['state'], 'available')
            self.assertEqual(out['preflight']['operators_registry']['state'], 'missing')
            self.assertEqual(out['resources']['project_structure']['data']['scope_units'][0]['scope_unit_name'], 'PROJECT')

    def test_rejects_projection_as_structure(self):
        with tempfile.TemporaryDirectory(dir=TMPDIR, ignore_cleanup_errors=True) as folder:
            root = Path(folder)
            (root / 'old.toml').write_text('[projection]\ngenerator="old"\n')
            out = prepare_context({'confidence_threshold': .99, 'sources': [source('a.md', 'A', RULE_TEXT)]},
                                  root=root, resources={'project_structure': 'old.toml'})
            self.assertEqual(out['preflight']['project_structure']['state'], 'invalid')

    def test_no_silent_legacy_principle_admission(self):
        raw = '---\nlocal_tier: Principle\n---\n# One authority\nNever duplicate authority.\n'
        packet = prepare_context({'confidence_threshold': .99, 'sources': [source('p.md', 'P', raw)]})
        self.assertFalse(packet['applicable_principles'])
        self.assertEqual(packet['preflight']['principles']['state'], 'missing')

    def test_no_secret_or_escape_reads(self):
        with tempfile.TemporaryDirectory(dir=TMPDIR, ignore_cleanup_errors=True) as folder:
            packet = {'confidence_threshold': .99, 'sources': [source('a.md', 'A', RULE_TEXT)]}
            for path in ('../secret.toml', '.env', '.env.local', '/tmp/other.toml'):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    prepare_context(packet, root=Path(folder), resources={'project_structure': path})


class SemanticAdmission(unittest.TestCase):
    def test_duplicate_governs_keeps_its_real_mention(self):
        from context_builder import body_sections
        from review_evidence import validate_subject_inventory
        raw = '---\nsubjects:\n  governs: Atom\n  depends_on: [Atom]\n---\n' + SOURCE_TEXT
        row = part('coherence')['checks'][0]
        row['subject_inventory']['sections_reviewed'] = body_sections(raw)
        row['findings'] = [{'kind': 'violation', 'subject_issue': 'duplicate', 'entity': 'Atom'}]
        validate_subject_inventory(row, raw, {'MOCK-R-002@1': RULE_TEXT}, {'MOCK-R-002@1': 'Atom'})
        self.assertEqual('Atom', row['subject_inventory']['mentions'][0]['entity'])

    def test_summary_literal_prevents_false_extra_finding(self):
        from context_builder import body_sections
        from review_evidence import validate_subject_inventory
        raw = '---\nsubjects:\n  governs: Atom\n  depends_on: [Operator]\n---\n' + SOURCE_TEXT.replace('Atom rule', 'Atom rule for Operator')
        row = part('coherence')['checks'][0]
        row['subject_inventory']['sections_reviewed'] = body_sections(raw)
        row['findings'] = [{'kind': 'violation', 'subject_issue': 'extra', 'entity': 'Operator'}]
        with self.assertRaisesRegex(ValueError, 'literal Markdown occurrence'):
            validate_subject_inventory(row, raw, {'MOCK-R-002@1': RULE_TEXT}, {'MOCK-R-002@1': 'Atom'})

    def test_qualified_path_prefix_is_not_standalone_bearer(self):
        from review_evidence import literal_occurs
        self.assertFalse(literal_occurs('Widget', 'Widget/Color: Blue'))
        self.assertTrue(literal_occurs('Widget', 'public Widget displays'))

    def test_extra_subject_does_not_need_an_invented_body_mention(self):
        from review_evidence import _validate_subject_findings
        row = {'subject_inventory': {'complete': True}, 'findings': [{
            'kind': 'violation', 'subject_issue': 'extra', 'entity': 'Operator'}]}
        _validate_subject_findings(row, {'Atom'}, ['Atom', 'Operator'])
        row['subject_inventory']['complete'] = False
        with self.assertRaisesRegex(ValueError, 'complete inventory'):
            _validate_subject_findings(row, {'Atom'}, ['Atom', 'Operator'])

    def test_extra_subject_cannot_be_mentioned_or_undeclared(self):
        from review_evidence import _validate_subject_findings
        row = {'subject_inventory': {'complete': True}, 'findings': [{
            'kind': 'violation', 'subject_issue': 'extra', 'entity': 'Operator'}]}
        for resolved, declared in (({'Operator'}, ['Operator']), ({'Atom'}, ['Atom'])):
            with self.assertRaisesRegex(ValueError, 'Subject'):
                _validate_subject_findings(row, resolved, declared)

    def test_missing_subject_cannot_bypass_omission_resolution(self):
        from review_evidence import _validate_subject_findings
        row = {'subject_inventory': {'complete': True}, 'findings': [{
            'kind': 'violation', 'entity': 'Operator'}]}
        with self.assertRaisesRegex(ValueError, 'omission resolution'):
            _validate_subject_findings(row, {'Atom', 'Operator'}, ['Atom'])
        row['findings'][0].update(subject_issue='governs')
        _validate_subject_findings(row, {'Atom', 'Operator'}, ['Atom'])

    def test_summary_text_cannot_prove_definition(self):
        raw = '# Summary\nAtom means the navigation label only.\n## Claim\nActual definition here.\n'
        self.assertNotIn('navigation label', prose(raw))
        self.assertIn('Actual definition here.', prose(raw))

    def test_definition_evidence_excludes_code_and_quoted_examples(self):
        raw = '# Claim\nActual definition.\n```md\nAtom means invalid example.\n```\n> Atom means quoted claim.\n    Atom means code.\n'
        self.assertIn('Actual definition.', prose(raw))
        self.assertNotIn('Atom means', prose(raw))

    def test_subject_location_must_contain_its_evidence(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['mentions'][0]['location'] = 'Details'
        with self.assertRaisesRegex(ValueError, 'claimed Markdown section'):
            contract.validate_part(response, context=context())

    def test_already_declared_entity_is_not_missing(self):
        from review_evidence import validate_subject_inventory
        raw = '---\nsubjects:\n  governs: Other\n  depends_on: [Atom]\n---\n# Claim\nAtom\n'
        from context_builder import body_sections
        row = part('coherence')['checks'][0]
        row['subject_inventory']['sections_reviewed'] = body_sections(raw)
        row['findings'] = [{'kind': 'omission', 'entity': 'Atom'}]
        with self.assertRaisesRegex(ValueError, 'already declared'):
            validate_subject_inventory(row, raw, {'MOCK-R-002@1': RULE_TEXT}, {'MOCK-R-002@1': 'Atom'})

    def test_rejects_title_only_definition(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['mentions'][0]['definitions'][0]['excerpt'] = '# Definition'
        with self.assertRaisesRegex(ValueError, 'body|definition|quote'):
            contract.validate_part(response, context=context())

    def test_wrong_governs_target_cannot_prove_entity(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['mentions'][0]['entity'] = 'Author'
        with self.assertRaisesRegex(ValueError, 'Entity|target'):
            contract.validate_part(response, context=context())

    def test_subject_finding_needs_resolved_entity(self):
        response = part('coherence')
        row = response['checks'][0]
        row.update(status='failed', findings=[{'kind': 'violation', 'entity': 'Author',
            'location': 'body', 'excerpt': 'Atom', 'reason': 'unproven',
            'proposed_fix': 'add Author', 'confidence': 1.0}])
        response['result'] = 'failed'
        with self.assertRaisesRegex(ValueError, 'resolved|Entity'):
            contract.validate_part(response, context=context())

    def test_missing_context_cannot_be_declared_without_preflight(self):
        response = part('properties')
        response['checks'][0]['status'] = 'blocked'
        response['coverage_gaps'] = [{'check_id': 'properties', 'kind': 'missing_context',
                                     'context_key': 'invented', 'reason': 'not supplied'}]
        response['result'] = 'blocked'
        with self.assertRaisesRegex(ValueError, 'preflight|context'):
            contract.validate_part(response, context=context())

    def test_unreviewed_sections_cannot_claim_complete_inventory(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['sections_reviewed'] = []
        with self.assertRaisesRegex(ValueError, 'section'):
            contract.validate_part(response, context=context())

    def test_complete_and_unresolved_are_incompatible(self):
        response = part('coherence')
        row = response['checks'][0]
        row['subject_inventory']['mentions'][0].update(resolution='unresolved', entity=None, definitions=[])
        row['status'] = 'blocked'
        response.update(result='blocked', coverage_gaps=[{
            'check_id': 'subjects', 'kind': 'unresolved_interpretation', 'reason': 'ambiguity'}])
        with self.assertRaisesRegex(ValueError, 'complete'):
            contract.validate_part(response, context=context())

    def test_metadata_only_definition_is_rejected(self):
        response = part('coherence')
        response['checks'][0]['subject_inventory']['mentions'][0]['definitions'][0]['excerpt'] = 'governs: Atom'
        with self.assertRaisesRegex(ValueError, 'body|definition|quote'):
            contract.validate_part(response, context=context())

    def test_available_resource_cannot_be_called_missing(self):
        bound = context({'project_structure': {'state': 'available', 'reason': 'bound TOML'}})
        response = part('properties')
        response['context_sha256'] = bound.sha256
        response['checks'][0]['status'] = 'blocked'
        response.update(result='blocked', coverage_gaps=[{
            'check_id': 'properties', 'kind': 'missing_context', 'context_key': 'project_structure',
            'reason': 'forgot to read it'}])
        with self.assertRaisesRegex(ValueError, 'available'):
            contract.validate_part(response, context=bound)

    def test_validation_is_non_mutating(self):
        response = part('coherence')
        before = copy.deepcopy(response)
        contract.validate_part(response, context=context())
        self.assertEqual(before, response)
