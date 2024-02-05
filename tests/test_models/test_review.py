import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Review instance before each test.
        """
        self.review = Review()

    def test_review_place_id_default(self):
        """
        Test the default value of Review.place_id.
        """
        self.assertEqual(self.review.place_id, "")

    def test_review_user_id_default(self):
        """
        Test the default value of Review.user_id.
        """
        self.assertEqual(self.review.user_id, "")

    def test_review_text_default(self):
        """
        Test the default value of Review.text.
        """
        self.assertEqual(self.review.text, "")
