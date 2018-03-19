import unittest
from CodeAndTest.Src.ExpandedForm import expanded_form

class test_ExpanForm(unittest.TestCase):
    def test_expanded_form(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')