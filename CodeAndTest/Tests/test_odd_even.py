import unittest
from CodeAndTest.Src.ArrayOddEven import Odd_Or_Even

class TestOddEven(unittest.TestCase):
    def test_odd_even(self):
        self.assertEqual(Odd_Or_Even([1023, 1, 2]), 'even')
        self.assertEqual(Odd_Or_Even([0]), 'even')
        self.assertEqual(Odd_Or_Even([0, 1, 2]), 'odd')