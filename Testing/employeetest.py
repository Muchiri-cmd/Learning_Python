import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""tests for employee class"""
	
	def setUp(self):
		"""make an employee to use in tests"""
		self.Davis=Employee('Davis','Muchiri',65000)
		
	def test_give_default_raise(self):
		"""test that default raise works"""
		self.Davis.give_default_raise()
		self.assertEqual(self.Davis.salary,70000)
		
	def test_give_custom_raise(self):
		"""Test that custom raise works correct"""
		self.Davis.give_default_raise(10000)
		self.assertEqual(self.Davis.salary,75000)
		

unittest.main()
		

