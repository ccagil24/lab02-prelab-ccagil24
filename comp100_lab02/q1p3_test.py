import unittest
from q1p3 import format_factor


class TestFormatFactor(unittest.TestCase):
    def test_1(self):
        self.assertEqual(format_factor(2, 3), "2^3", "Should be 2^3")

    def test_2(self):
        self.assertEqual(format_factor(3, 1), "3", "Should be 3 without power")

    def test_3(self):
        self.assertEqual(format_factor(5, 3), "5^3", "Should be 5^3")

    def test_4(self):
        self.assertEqual(format_factor(7, 1), "7", "Should be 7 without power")

    def test_5(self):
        self.assertEqual(format_factor(2, 2), "2^2", "Should be 2^2")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFormatFactor)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
