import unittest
from cityfunctions import city_country
class CityCaseTest(unittest.TestCase):
	#tests for 'cityfunctions.py'
	
	def test_city_country(self):
		"""Do inputs like santiago and chile provide required output"""
		formatted_name=city_country('santiago','chile')
		self.assertEqual(formatted_name,'Santiago,Chile')
		
	def test_city_country_population(self):
		"""Do inputs like santiago,chile and 5000000 provide req o/p"""
		formatted_name=city_country('santiago','chile',population=5000000)
		self.assertEqual(formatted_name,'Santiago,Chile Population-5000000')
		
		
unittest.main()

