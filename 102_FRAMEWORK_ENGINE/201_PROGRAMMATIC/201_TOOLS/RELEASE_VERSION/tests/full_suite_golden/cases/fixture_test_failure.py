import unittest


class FailureSuiteTests(unittest.TestCase):
    def test_failure(self):
        self.fail("fixture failure")
