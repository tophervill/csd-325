import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        test_input = city_country("santiago", "chile", 5000000)
        self.assertEqual(test_input, "Santiago, Chile - Population 5000000")

if __name__ == '__main__':
    unittest.main()