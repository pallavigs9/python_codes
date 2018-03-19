import unittest
from CodeAndTest.Src import SumArray

class test_SumArray(unittest.TestCase):
    def test_sum_array(self):
        self.assertEqual(0, SumArray.sum_array(None))
        self.assertEqual(16, SumArray.sum_array([6, 2, 1, 8, 10]))
        self.assertEqual(0, SumArray.sum_array([]))
        self.assertEqual(3, SumArray.sum_array([-6, 20, -1, 10, -12]))