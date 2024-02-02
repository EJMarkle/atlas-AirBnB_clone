import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class is for testing the BaseModel class."""
    def setUp(self):
        # Test the creation of the class.
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
        self.assertTrue('id'in rep_str)
        self.assertTrue('created_at' in rep_str)
        self.assertTrue('updated_at'in rep_str)

if __name__ == '__main__':
    unittest.main()
