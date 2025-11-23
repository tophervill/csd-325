import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        # Test input with city and country only
        first_test = city_country("santiago", "chile")
        self.assertEqual(first_test, "Santiago, Chile")

        # Test input with city, country, and population
        second_test = city_country("santiago", "chile", 5000000)
        self.assertEqual(second_test, "Santiago, Chile - Population 5000000")

        # Test input with city, country, population, and language
        third_test = city_country("santiago", "chile", 5000000, "spanish")
        self.assertEqual(third_test, "Santiago, Chile - Population 5000000, Spanish")

if __name__ == '__main__':
    unittest.main()