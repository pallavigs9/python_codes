import unittest
from CodeAndTest.Src.sequence_sum import sequence_sum

class test_sequence(unittest.TestCase):
    def test_sum_seq(self):
        self.assertEqual(sequence_sum(1, 5, 3), 5)
        self.assertEqual(sequence_sum(16, 15, 3), 0)
        self.assertEqual(sequence_sum(2, 2, 2), 2)
        self.assertEqual(sequence_sum(0, 15, 3), 45)

