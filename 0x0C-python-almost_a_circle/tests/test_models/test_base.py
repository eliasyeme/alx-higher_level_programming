#!/usr/bin/python3
import json
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(7)
        self.b4 = Base()
        self.string = Base("string")
        self.float_2_57 = Base(2.57)

    def tearDown(self):
        pass


    def test_no_args_two_base_class(self):
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_id_argument(self):
        self.assertEqual(self.b3.id, 7)

    def test_id_argument_and_no_id(self):
        self.assertEqual(self.b2.id, self.b4.id - 1)

    def test_set_id(self):
        self.b1.id = 8
        self.assertEqual(self.b1.id, 8)

    def test_string_id(self):
        self.assertEqual(self.string.id, "string")

    def test_float_number(self):
        self.assertEqual(self.float_2_57.id, 2.57)

    def test_access_private_attribute(self):
        with self.assertRaises(AttributeError):
            self.b1.__nb_objects

class TestBaseJsonString(unittest.TestCase):
    """test dictionary to json"""
    def test_to_json_None_dict(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty_dict(self):
        self.assertEqual(Base.to_json_string({}), "[]")

    def test_to_json_type(self):
        self.assertIs(type(Base.to_json_string({})), str)

    def test_to_json_type_with_item(self):
        self.assertIs(type(Base.to_json_string([{"id":1}])), str)

    def test_to_json_rect_dict(self):
        r = Rectangle(1, 1).to_dictionary()
        b = Base().to_json_string([r])
        self.assertEqual(b, json.dumps([r]))

    def test_to_json_squre_dict(self):
        s = Square(1).to_dictionary()
        b = Base().to_json_string([s])
        self.assertEqual(b, json.dumps([s]))

    def test_to_json_dict_list(self):
        s = Square(1).to_dictionary()
        r = Rectangle(1, 1).to_dictionary()
        b = Base().to_json_string([r, s, r, s])
        self.assertEqual(b, json.dumps([r, s, r, s]))

    def test_to_json_invalid_arg(self):
        with self.assertRaises(TypeError):
            Base().to_json_string(None, None)

    def test_to_json_invalid_arg_empty(self):
        with self.assertRaises(TypeError):
            Base().to_json_string()

if __name__ == "__main__":
    unittest.main()
