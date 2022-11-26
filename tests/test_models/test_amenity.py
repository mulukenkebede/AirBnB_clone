#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class tests_amenity(unittest.TestCase):

    obj = Amenity()

    def set_Up(self):
        """set initial"""
        name = ""

    def test_normalAmenity(self):
        """normal tests amenity"""
        my_object = Amenity()
        my_object.name = "Fantastic"
        my_object.my_number = 14
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Fantastic")
        self.assertEqual(my_object.my_number, 14)
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
