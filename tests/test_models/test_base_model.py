"""Test the BaseModel class"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseTest(unittest.TestCase):
    """Tests the BaseModel class"""

    def setUp(self):
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def test_id_is_string(self):
        """tests if the id is converted to string"""
        self.assertIsInstance(self.obj1.id, str)

    def test_id_unique(self):
        """tests if the BaseModel assigns unique id's to different objects"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_save(self):
        """tests the save method updates updated_at"""
        old_time = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(old_time, self.obj1.updated_at)

    def test_to_dict_returns_dict(self):
        """tests if to_dict returns a dictionary"""
        self.assertIsInstance(self.obj1.to_dict(), dict)

    def test_to_dict_contains(self):
        """tests all the attributes in the dictionary representation"""
        d = self.obj1.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], self.obj1.id)
        self.assertEqual(d["created_at"], self.obj1.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.obj1.updated_at.isoformat())

    def test_str_representation(self):
        """tests the string representation of the object"""
        obj = BaseModel()
        expected = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected)

    def test_created_with_kwargs(self):
        """tests the object generated with the kwarg passed"""
        model1 = BaseModel()
        model1.name = "Model One"
        model1.number = 1
        model1_json = model1.to_dict()

        model2 = BaseModel(**model1_json)
        self.assertNotEqual(model1, model2)
        self.assertIsInstance(model1.created_at, datetime)

        for attr in model2.__dict__:
            with self.subTest(attr=attr):
                self.assertIn(attr, model1_json)
