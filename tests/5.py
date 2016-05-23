
import unittest


class BankTestCase(unittest.TestCase):

    def test_one_year(self):

        self.assertAlmostEqual(bank(10000, 1), 11000)

    def test_normal(self):

        self.assertAlmostEqual(bank(1234, 3), 1642.454)
        self.assertAlmostEqual(bank(2345, 4), 3433.3145)

    def test_no_money(self):

        for years in range(1, 10):
            self.assertEqual(bank(0, years), 0)

    def test_zero_years(self):

        self.assertEqual(bank(200, 0), 200, "Случай вклада на 0 лет тоже нужно рассматривать")


if __name__ == "__main__":
    unittest.main()