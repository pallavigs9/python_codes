import unittest
from CodeAndTest.Src.SumDigit import sum_digits

class TestSumDigit(unittest.TestCase):
    def test_sum_digit(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(-32), 5)
        self.assertEqual(sum_digits(99), 18)