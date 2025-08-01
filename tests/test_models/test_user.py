"""Test the BaseModel class"""


import unittest
from models.user import User
from models import storage


class UserTest(unittest.TestCase):
    """ Tests the User class """

    def setUp(self):
        """ creates the object """
        self.obj = User()

    def test_attribute_type(self):
        """ tests that the attributes are strings """
        self.assertTrue(type(self.obj.email), str)
        self.assertTrue(type(self.obj.password), str)
        self.assertTrue(type(self.obj.first_name), str)
        self.assertTrue(type(self.obj.last_name), str)
