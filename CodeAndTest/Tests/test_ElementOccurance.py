import unittest
from CodeAndTest.Src.element_occurance import delete_nth

class TestOccurance(unittest.TestCase):

    def test_occurance(self):
        self.assertEqual(delete_nth([20,37,20,21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertEqual(delete_nth([1,1,1,1],2), [1, 1])