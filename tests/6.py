
import unittest


class PrimeTestCase(unittest.TestCase):

    def test_small_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        for number in range(1, 101):
            with self.subTest(number=number):
                if number in primes:
                    self.assertTrue(is_prime(number))
                else:
                    self.assertFalse(is_prime(number))

    def test_big_numbers(self):
        primes = [947, 953, 967, 971, 977, 983, 991, 997]

        for number in range(942, 1000):
            with self.subTest(number=number):
                if number in primes:
                    self.assertTrue(is_prime(number))
                else:
                    self.assertFalse(is_prime(number))


if __name__ == "__main__":
    unittest.main()