import unittest
from CodeAndTest.Src.Wave import wave

class TestWave(unittest.TestCase):

    def test_wave(self):
        self.assertEqual(wave('two words'),['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS'])
        self.assertEqual(wave(' gap '), [" Gap ", " gAp ", " gaP "])
        self.assertEqual(wave('hello'), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
        self.assertEqual(wave('codewars'), ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"])
