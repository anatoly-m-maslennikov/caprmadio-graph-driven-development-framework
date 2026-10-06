import unittest


class SkippedSuiteTests(unittest.TestCase):
    @unittest.skip("fixture skip")
    def test_skip(self):
        self.assertTrue(True)
