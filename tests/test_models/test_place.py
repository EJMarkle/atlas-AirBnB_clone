import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Place instance before each test.
        """
        self.place = Place()

    def test_place_city_id_default(self):
        """
        Test the default value of Place.city_id.
        """
        self.assertEqual(self.place.city_id, "")

    def test_place_user_id_default(self):
        """
        Test the default value of Place.user_id.
        """
        self.assertEqual(self.place.user_id, "")

    def test_place_name_default(self):
        """
        Test the default value of Place.name.
        """
        self.assertEqual(self.place.name, "")

    def test_place_description_default(self):
        """
        Test the default value of Place.description.
        """
        self.assertEqual(self.place.description, "")

    def test_place_number_rooms_default(self):
        """
        Test the default value of Place.number_rooms.
        """
        self.assertEqual(self.place.number_rooms, 0)

    def test_place_number_bathrooms_default(self):
        """
        Test the default value of Place.number_bathrooms.
        """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_place_max_guest_default(self):
        """
        Test the default value of Place.max_guest.
        """
        self.assertEqual(self.place.max_guest, 0)

    def test_place_price_by_night_default(self):
        """
        Test the default value of Place.price_by_night.
        """
        self.assertEqual(self.place.price_by_night, 0)

    def test_place_latitude_default(self):
        """
        Test the default value of Place.latitude.
        """
        self.assertEqual(self.place.latitude, 0.0)

    def test_place_longitude_default(self):
        """
        Test the default value of Place.longitude.
        """
        self.assertEqual(self.place.longitude, 0.0)

    def test_place_amenity_ids_default(self):
        """
        Test the default value of Place.amenity_ids.
        """
        self.assertEqual(self.place.amenity_ids, [])
