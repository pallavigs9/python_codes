import unittest
from CodeAndTest.Src.FindVowels import vowel_indices

class TestFindVowel(unittest.TestCase):

    def test_vowel_indi(self):
        self.assertEqual(vowel_indices('super'), [2,4])
        self.assertEqual(vowel_indices('aeiouy'), [1, 2, 3, 4, 5, 6])