import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from query_filter import (  # noqa: E402
    MISSING,
    QueryFilterError,
    collect_selectors,
    evaluate_filter,
    parse_filter,
    parse_filter_with_stats,
    resolve_json_pointer,
    typed_equal,
)


class QueryFilterContractTest(unittest.TestCase):
    def test_parser_consumption_stats_are_parser_derived(self):
        tree, stats = parse_filter_with_stats('"x" = 1', max_tokens=3)
        self.assertEqual(tree, parse_filter('"x" = 1'))
        self.assertEqual(stats, {
            "tokens": 3,
            "grammar_depth": 0,
            "syntactic_depth": 0,
            "literal_depth": 0,
            "in_members": 0,
        })
        with self.assertRaises(QueryFilterError) as exhausted:
            parse_filter_with_stats('"x" = 1', max_tokens=2)
        self.assertEqual(exhausted.exception.statistics["tokens"], 3)

    def test_parser_consumption_counts_depth_in_and_separator_tokens(self):
        _, in_stats = parse_filter_with_stats(
            '"x" IN (1, 2)', max_tokens=7, max_in_members=2
        )
        self.assertEqual(in_stats["tokens"], 7)
        self.assertEqual(in_stats["in_members"], 2)
        _, nested = parse_filter_with_stats('NOT ("x" IN (1, 2))', max_depth=2)
        self.assertEqual(nested["tokens"], 10)
        self.assertEqual(nested["syntactic_depth"], 2)
        self.assertEqual(nested["grammar_depth"], 2)
        self.assertEqual(nested["in_members"], 2)
        _, literal = parse_filter_with_stats('"x" = [[1]]', max_depth=2)
        self.assertEqual(literal["literal_depth"], 2)
        self.assertEqual(literal["grammar_depth"], 2)
        _, long_literal = parse_filter_with_stats('"' + "x" * 300 + '" = {"k": "' + "y" * 300 + '"}')
        self.assertEqual(long_literal["tokens"], 3)

        with self.assertRaises(QueryFilterError) as depth_error:
            parse_filter_with_stats('NOT NOT "x" = true', max_depth=1)
        self.assertEqual(depth_error.exception.statistics["grammar_depth"], 2)
        with self.assertRaises(QueryFilterError) as in_error:
            parse_filter_with_stats('"x" IN (1, 2)', max_in_members=1)
        self.assertEqual(in_error.exception.statistics["in_members"], 2)
        with self.assertRaises(QueryFilterError) as literal_depth_error:
            parse_filter_with_stats('"x" = [[1]]', max_depth=1)
        self.assertEqual(literal_depth_error.exception.statistics["literal_depth"], 2)

    def test_precedence_escaped_quotes_and_null_missing(self):
        tree = parse_filter(
            'NOT "flag" = true OR ("name" = "a\\\"b" AND "nullable" = null)'
        )
        values = {"flag": True, "name": 'a"b', "nullable": None}
        self.assertTrue(evaluate_filter(tree, values.get))
        self.assertFalse(evaluate_filter(parse_filter('"absent" != null'), lambda _: MISSING))
        self.assertTrue(evaluate_filter(parse_filter('"nullable" = null'), values.get))

    def test_json_numbers_share_one_type_but_booleans_do_not(self):
        self.assertTrue(typed_equal(1, 1.0))
        self.assertTrue(typed_equal([1, {"x": 2.0}], [1.0, {"x": 2}]))
        self.assertFalse(typed_equal(True, 1))
        self.assertFalse(typed_equal(False, 0.0))
        tree = parse_filter('"value" IN (1.0, [1, {"x": 2}])')
        self.assertTrue(evaluate_filter(tree, lambda _: [1.0, {"x": 2.0}]))

    def test_all_selectors_are_available_for_prevalidation(self):
        tree = parse_filter('"known" = true OR "unvisited" = 1')
        self.assertEqual(collect_selectors(tree), ("known", "unvisited"))
        self.assertTrue(evaluate_filter(tree, lambda selector: {"known": True}[selector]))

    def test_json_pointer_escaping_and_array_index_rules(self):
        value = {"a/b": {"~key": ["zero", "one"]}}
        self.assertEqual(resolve_json_pointer(value, "/a~1b/~0key/1"), "one")
        self.assertIs(resolve_json_pointer(value, "/a~1b/~0key/01"), MISSING)
        with self.assertRaises(QueryFilterError):
            resolve_json_pointer(value, "/a~2b")
        with self.assertRaises(QueryFilterError):
            resolve_json_pointer(value, "a~1b")

    def test_parser_rejects_invalid_literals_syntax_and_budgets(self):
        invalid = (
            '"x" = {"a": 1, "a": 2}',
            '"x" = NaN',
            '"x" = 1e1000000',
            '"x"IN(1)',
            'NOT"x" = true',
            '"x" = 1 "y" = 2',
            '"x" IN ()',
            '"x" = 1 OR',
        )
        for expression in invalid:
            with self.subTest(expression=expression):
                with self.assertRaises(QueryFilterError):
                    parse_filter(expression)
        with self.assertRaisesRegex(QueryFilterError, "depth"):
            parse_filter('NOT NOT "x" = true', max_depth=1)
        with self.assertRaisesRegex(QueryFilterError, "depth"):
            parse_filter('"x" = [[[0]]]', max_depth=2)
        with self.assertRaisesRegex(QueryFilterError, "token"):
            parse_filter('"x" IN (1, 2)', max_tokens=5)
        with self.assertRaisesRegex(QueryFilterError, "IN member"):
            parse_filter('"x" IN (1, 2)', max_in_members=1)


if __name__ == "__main__":
    unittest.main()
