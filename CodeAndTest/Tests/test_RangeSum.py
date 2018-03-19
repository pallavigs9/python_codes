import unittest
from CodeAndTest.Src import RangeSum

class RangeSum1(unittest.TestCase):
    def test_get_sum(self):
        self.assertEqual(1, RangeSum.get_sum(0,1))
        self.assertEqual(-1, RangeSum.get_sum(0,-1))
        self.assertEqual(2, RangeSum.get_sum(-1, 2))


class_call = RangeSum1
RangeSum1.test_get_sum()

if __name__ == '__main__':      # Another way to call class without class object
    unittest.main(verbosity=2)