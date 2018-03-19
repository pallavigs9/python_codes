import unittest
from CodeAndTest.Src import InvertValues

class test_InvertValue(unittest.TestCase):
    def test_invert(self):
        self.assertEqual([-1,2,-3,4,-5], InvertValues.invert([1,-2,3,-4,5]))
        self.assertEqual([], InvertValues.invert([]))