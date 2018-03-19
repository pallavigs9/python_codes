import unittest
from CodeAndTest.Src.SquareDigit import square_digit

class TestSqure(unittest.TestCase):

    def test_square_digit(self):
        self.assertEqual(square_digit(9119), 811181)
        self.assertEqual(square_digit(111), 111)