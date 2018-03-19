import unittest
from CodeAndTest.Src.StringEnd import solution

class TestString(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('abcde', 'cde'), True)
        self.assertEqual(solution('abc', 'd'), False)