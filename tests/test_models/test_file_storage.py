""" Tests the FileStorage class """


from models import storage
import unittest
from models.base_model import BaseModel


class FileStorageTest(unittest.TestCase):

    # def setUp(self):
    #     """ sets up the obj """
    #     self.obj = FileStorage.__objects

    def test_file_path(self):
        """ tests that the file contains .json extension """
        self.assertTrue(".json" in storage._FileStorage__file_path)

    def test_file_storage_objects(self):
        """ tests that the __objects is a dict and the key and value
        properly assigned"""
        self.assertEqual(type(storage.all()), dict)

    def test_all(self):
        """ tests that all() returns the obj """
        storage._FileStorage__objects = {}
        dummy = BaseModel()
        storage.new(dummy)
        all_objs = storage.all()
        key = f"BaseModel.{dummy.id}"
        self.assertEqual(all_objs[key], dummy)
