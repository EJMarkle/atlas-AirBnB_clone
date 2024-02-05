import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """
        Set up a new City instance before each test.
        """
        self.city = City()

    def test_city_state_id_default(self):
        """
        Test the default value of City.state_id.
        """
        self.assertEqual(self.city.state_id, "")

    def test_city_name_default(self):
        """
        Test the default value of City.name.
        """
        self.assertEqual(self.city.name, "")
