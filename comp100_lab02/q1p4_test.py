import unittest
from q1p4 import format_prime_factors


class TestFormatPrimeFactors(unittest.TestCase):
    def test_1(self):
        self.assertEqual(format_prime_factors(360), "2^3 * 3^2 * 5", "Should format 360's factors correctly")

    def test_2(self):
        self.assertEqual(format_prime_factors(100), "2^2 * 5^2", "Should format 100's factors correctly")

    def test_3(self):
        self.assertEqual(format_prime_factors(13), "13", "Should handle prime numbers correctly")

    def test_4(self):
        self.assertEqual(format_prime_factors(29), "29", "29 is prime and should return '29'")

    def test_5(self):
        self.assertEqual(format_prime_factors(210), "2 * 3 * 5 * 7", "210's factorization should include 2, 3, 5, and 7")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFormatPrimeFactors)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
