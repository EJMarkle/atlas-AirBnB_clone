import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class is for testing the BaseModel class."""
    def setUp(self):
        """Create the test environment."""
        self.my_model = BaseModel()

    def test_save(self):
        # Test the save method.
        og = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(og, self.my_model.updated_at)

    def test_to_dict(self):
        # Test the to_dict method.
        model_dict = self.my_model.to_dict()
        self.assertTrue('__class__' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_id(self):
        # Test the id field.
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at(self):
        # Test the field created_at.
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_str(self):
        rep_str = str(self.my_model)
        self.assertTrue('BaseModel' in rep_str)
        self.assertTrue('id' in rep_str)
        self.assertTrue('created_at' in rep_str)
        self.assertTrue('updated_at' in rep_str)

    def test_save_new_instance(self):
        new_base_model = BaseModel()
        new_base_model.save()
        self.assertIsNotNone(new_base_model.id)
        self.assertIsNotNone(new_base_model.created_at)
        self.assertIsNotNone(new_base_model.updated_at)

    def test_save_existing_instance(self):
        existing_base_model = BaseModel()
        existing_base_model.save()
        original_id = existing_base_model.id
        existing_base_model.some_attribute = "some_value"
        existing_base_model.save()
        self.assertEqual(existing_base_model.id, original_id)
