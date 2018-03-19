import unittest
from CodeAndTest.Src.ReverseSentence import reverse_word

class TestReverse(unittest.TestCase):

    def test_reverse_word(self):
        self.assertEqual(reverse_word("double  spaces"), "elbuod  secaps")
        self.assertEqual(reverse_word("This is an example!"), "sihT si na !elpmaxe")

