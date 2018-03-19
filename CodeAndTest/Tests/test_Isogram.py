import unittest
from CodeAndTest.Src.Isogram import is_isogram

class TestGram(unittest.TestCase):

    def test_isogram(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)
        self.assertEqual(is_isogram("moOse"), False)
        self.assertEqual(is_isogram("aba"), False)
        self.assertEqual(is_isogram(""), True)