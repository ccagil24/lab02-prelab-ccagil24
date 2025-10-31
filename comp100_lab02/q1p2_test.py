import unittest
from q1p2 import count_factor_power


class TestCountFactorPower(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_factor_power(15, 3), 1, "Should be 1")

    def test_2(self):
        self.assertEqual(count_factor_power(18, 3), 2, "Should be 2")

    def test_3(self):
        self.assertEqual(count_factor_power(18, 2), 1, "Should be 1")

    def test_4(self):
        self.assertEqual(count_factor_power(100, 2), 2, "Should be 2")

    def test_5(self):
        self.assertEqual(count_factor_power(81, 3), 4, "Should be 4")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCountFactorPower)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
