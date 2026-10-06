import unittest


class SubtestSuiteTests(unittest.TestCase):
    def test_subtests(self):
        for value in ("pass", "fail"):
            with self.subTest(value=value):
                self.assertEqual(value, "pass")
