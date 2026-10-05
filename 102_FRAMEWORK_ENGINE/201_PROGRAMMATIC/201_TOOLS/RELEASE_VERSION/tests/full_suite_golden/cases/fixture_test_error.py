import unittest


class ErrorSuiteTests(unittest.TestCase):
    def test_error(self):
        raise RuntimeError("fixture error")
