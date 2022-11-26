#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class testsAmenity(unittest.TestCase):

    obj = Amenity()

    def setUp(self):
        """set initial"""
        name = ""

    def test_normalAmenity(self):
        """normal tests amenity"""
        my_object = Amenity()
        my_object.name = "My First Model"
        my_object.my_number = 89
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "My First Model")
        self.assertEqual(my_object.my_number, 89)
        self.assertEqual(my_object.__class__.__name__, "Amenity")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_type(self):
        """test type of object"""
        obj = Amenity()
        self.assertEqual(type(self.obj.name), str)

if __name__ == "__main__":
    unittest.main()
