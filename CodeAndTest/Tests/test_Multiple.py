import unittest
from CodeAndTest.Src.Multiple3Or5 import find

class TestMuliply(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find(5), 8)
        self.assertEqual(find(10), 33)