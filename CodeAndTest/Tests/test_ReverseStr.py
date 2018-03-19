import unittest
from CodeAndTest.Src.ReversedStr import solution

class TestReverseStr(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution(''), '')