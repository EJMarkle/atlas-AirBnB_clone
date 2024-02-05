import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Amenity instance before each test.
        """
        self.amenity = Amenity()

    def test_amenity_name_default(self):
        """
        Test the default value of Amenity.name.
        """
        self.assertEqual(self.amenity.name, "")
