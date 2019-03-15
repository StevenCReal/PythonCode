import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """测试是否能正确显示出'London, Britain'的格式？ """ 
    def test_city_country(self):
        formatted_name = city_country('London','britain')
        self.assertEqual(formatted_name, 'London, Britain')
    
    """测试是否能正确显示出'Zhan Jiang, China - Population 5000000'的格式？ """
    def test_city_country_population(self):
        formatted_name = city_country('zhan jiang', 'china', 5000000)
        self.assertEqual(formatted_name, "Zhan Jiang, China - Population 5000000")
    
unittest.main()