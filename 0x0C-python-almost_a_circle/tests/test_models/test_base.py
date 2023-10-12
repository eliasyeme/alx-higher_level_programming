#!/usr/bin/python3
import unittest
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

if __name__ == "__main__":
    unittest.main()
