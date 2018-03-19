import unittest
from CodeAndTest.Src import OnlyNo

class test_OnlyNum(unittest.TestCase):
    def test_filter_nos(self):
        self.assertEqual([1,2,123], OnlyNo.filter_nos([1,2,'aasf','1','123',123]))
        self.assertEqual([1,0,15], OnlyNo.filter_nos([1,'a','b',0,15]))
        self.assertEqual([1,2], OnlyNo.filter_nos([1,2,'a','b']))