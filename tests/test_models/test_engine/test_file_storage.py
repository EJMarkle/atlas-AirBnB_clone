import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test the FileStorage class."""
    def setUp(self) -> None:
        """Create the test environment."""
        # Define a temporary file path for testing.
        self.test_file_path = "test_file.json"
        # Create a FileStorage instance.
        self.file_storage = FileStorage()
        # Set the __file_path to the temp path.
        self.file_storage._FileStorage__file_path = self.test_file_path

    def tearDown(self) -> None:
        """Delete the temporary file after each test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_file_path(self) -> None:
        # Test __file_path is correctly set.
        self.assertEqual(
            self.file_storage._FileStorage__file_path,
            self.test_file_path
        )

    def test_objects(self) -> None:
        # Test if __objects is empty initally.
        self.assertDictEqual(
            self.file_storage.all(),
            self.file_storage._FileStorage__objects
        )

    def test_all(self) -> None:
        # Test all() returns the __objects dictionary.
        self.assertDictEqual(
            self.file_storage.all(),
            self.file_storage._FileStorage__objects
        )

    def test_new(self) -> None:
        # Test the new() method.
        new_base_model = BaseModel()
        # Call the new method.
        self.file_storage.new(new_base_model)
        # Check the new obj is in __objects.
        key = "{}.{}".format(
            new_base_model.__class__.__name__, new_base_model.id
        )
        self.assertIn(key, self.file_storage._FileStorage__objects)

    def test_save(self) -> None:
        # Test the FileStorage save() method.
        new_base_model = BaseModel()
        # Call new() method and save().
        self.file_storage.new(new_base_model)
        self.file_storage.save()
        # Check if file has been created.
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_reload(self) -> None:
        # Test the FileStorage reload() method.
        new_file_storage = FileStorage()
        new_base_model = BaseModel()
        new_file_storage.new(new_base_model)
        new_file_storage.save()
        first_dict = new_file_storage.all()
        os.remove("file.json")
        new_file_storage.reload()
        second_dict = new_file_storage.all()
        self.assertDictEqual(first_dict, second_dict)
