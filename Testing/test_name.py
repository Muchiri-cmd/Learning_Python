import unittest
from fullname import get_formatted_name
class NamesTestCase(unittest.TestCase):
 #Tests for 'test.py'.
 
 def test_first_last_name(self):
  """Do names like 'Davis Muchiri' work?"""
  formatted_name = get_formatted_name('davis', 'muchiri')
  self.assertEqual(formatted_name, 'Davis Muchiri')

unittest.main()
