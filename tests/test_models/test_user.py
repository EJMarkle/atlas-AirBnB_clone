import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    class for testing the User class.
    """

    def setUp(self):
        """
        Set up a new User instance before each test.
        """
        self.user = User()

    def test_user_email_default(self):
        # Test the default value of the User.email.
        self.assertEqual(self.user.email, "")

    def test_user_password_default(self):
        # Test the default value of the User.password.
        self.assertEqual(self.user.password, "")

    def test_user_first_name_default(self):
        # Test the default value of the User.first_name.
        self.assertEqual(self.user.first_name, "")

    def test_user_last_name_default(self):
        # Test the default value of the User.last_name.
        self.assertEqual(self.user.last_name, "")
