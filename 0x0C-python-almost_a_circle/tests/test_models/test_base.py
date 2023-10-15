#!/usr/bin/python3
import json
import os
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

class TestBaseJsonToFile(unittest.TestCase):
    """test save to file method"""
    def setUp(self) -> None:
        self.r = Rectangle(1, 1)
        self.rn = "Rectangle.json"
        self.s = Square(1)
        self.sn = "Square.json"
        self.b = Base()
        self.bn = "Base.json"

    def tearDown(self):
        fnl = [self.rn, self.sn, self.bn]
        for name in fnl:
            if os.path.exists(name):
                os.remove(name)

    def test_to_file_none_base(self):
        self.b.save_to_file(None)
        with open(self.bn, "r") as file:
            got = json.loads(file.read())
            self.assertListEqual(got, [])

    def test_to_file_none_rect(self):
        self.r.save_to_file(None)
        with open(self.rn, "r") as file:
            got = json.loads(file.read())
            self.assertListEqual(got, [])

    def test_to_file_none_squre(self):
        self.s.save_to_file(None)
        with open(self.sn, "r") as file:
            got = json.loads(file.read())
            self.assertListEqual(got, [])

    def test_to_file_rect_base(self):
        self.b.save_to_file([self.r])
        with open(self.bn, "r") as file:
            got = json.loads(file.read())
            want = [self.r.to_dictionary()]
            self.assertListEqual(got, want)

    def test_to_file_squre_base(self):
        self.b.save_to_file([self.s])
        with open(self.bn, "r") as file:
            got = json.loads(file.read())
            want = [self.s.to_dictionary()]
            self.assertListEqual(got, want)

    def test_to_file_rect_squre(self):
        self.r.save_to_file([self.s])
        with open(self.rn, "r") as file:
            got = json.loads(file.read())
            want = [self.s.to_dictionary()]
            self.assertListEqual(got, want)

    def test_to_file_squre_rect(self):
        self.s.save_to_file([self.r])
        with open(self.sn, "r") as file:
            got = json.loads(file.read())
            want = [self.r.to_dictionary()]
            self.assertListEqual(got, want)

    def test_to_file_rect_multi(self):
        self.r.save_to_file([self.r, self.s])
        with open(self.rn, "r") as file:
            got = json.loads(file.read())
            want = [
                self.r.to_dictionary(), self.s.to_dictionary()
            ]
            self.assertListEqual(got, want)

    def test_to_file_squre_multi(self):
        self.s.save_to_file([self.r, self.s])
        with open(self.sn, "r") as file:
            got = json.loads(file.read())
            want = [
                self.r.to_dictionary(), self.s.to_dictionary()
            ]
            self.assertListEqual(got, want)

    def test_to_file_invalid_args(self):
        with self.assertRaises(TypeError):
            self.r.save_to_file()

    def test_to_file_invalid_args_2(self):
        with self.assertRaises(TypeError):
            self.r.save_to_file(None, None)


class TestFromJsonString(unittest.TestCase):
    """Test from json string to list"""
    def test_json_string_none(self):
        got = Base().from_json_string(None)
        self.assertListEqual(got, [])

    def test_json_string_empty_list(self):
        got = Base().from_json_string("[]")
        self.assertListEqual(got, [])

    def test_json_string_from_rect(self):
        r = Rectangle(1, 1)
        dict_str = r.to_json_string([r.to_dictionary()])
        got = Base().from_json_string(dict_str)
        self.assertListEqual(got, [r.to_dictionary()])

    def test_json_string_from_square(self):
        s = Square(1)
        dict_str = s.to_json_string([s.to_dictionary()])
        got = Base().from_json_string(dict_str)
        self.assertListEqual(got, [s.to_dictionary()])

    def test_json_string_from_rect_and_square(self):
        s = Square(1)
        r = Rectangle(1, 1)
        dict_str = s.to_json_string([s.to_dictionary(), r.to_dictionary()])
        got = Base().from_json_string(dict_str)
        self.assertListEqual(got, [s.to_dictionary(), r.to_dictionary()])

    def test_json_string_invalid_args(self):
        with self.assertRaises(TypeError):
            Base().from_json_string()

    def test_json_string_invalid_args_type(self):
        with self.assertRaises(TypeError):
            Base().from_json_string(2)

    def test_json_string_invalid_args_type(self):
        with self.assertRaises(TypeError):
            Base().from_json_string(None, None)


class TestDictionaryToInstance(unittest.TestCase):
    """Test create instance from dictionary"""
    def setUp(self):
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 4)
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)
        self.r4 = Rectangle(1, 2, 3, 4, 5)

    def test_create_square_arg_1(self):
        s = Square.create(**self.s1.to_dictionary())
        self.assertEqual(str(s), str(self.s1))

    def test_create_square_arg_2(self):
        s = Square.create(**self.s2.to_dictionary())
        self.assertEqual(str(s), str(self.s2))

    def test_create_square_arg_3(self):
        s = Square.create(**self.s3.to_dictionary())
        self.assertEqual(str(s), str(self.s3))

    def test_create_square_arg_4(self):
        s = Square.create(**self.s4.to_dictionary())
        self.assertEqual(str(s), str(self.s4))

    def test_create_square_instance(self):
        s = Square.create(**self.s1.to_dictionary())
        self.assertIsInstance(s, Square)

    def test_create_rect_arg_2(self):
        r = Rectangle.create(**self.r1.to_dictionary())
        self.assertEqual(str(r), str(self.r1))

    def test_create_rect_arg_3(self):
        r = Rectangle.create(**self.r2.to_dictionary())
        self.assertEqual(str(r), str(self.r2))

    def test_create_rect_arg_4(self):
        r = Rectangle.create(**self.r3.to_dictionary())
        self.assertEqual(str(r), str(self.r3))

    def test_create_rect_arg_5(self):
        r = Rectangle.create(**self.r4.to_dictionary())
        self.assertEqual(str(r), str(self.r4))

    def test_create_rect_instance(self):
        r = Rectangle.create(**self.r1.to_dictionary())
        self.assertIsInstance(r, Rectangle)

    def test_create_rect_instance_is_different(self):
        r1 = Rectangle.create(**self.r1.to_dictionary())
        self.assertIsNot(r1,self.r1)

    def test_create_square_instance_is_different(self):
        s1 = Square.create(**self.s1.to_dictionary())
        self.assertIsNot(s1,self.s1)

    def test_create_no_args(self):
        self.assertEqual(Base.create(), None)


class TestLoadFromFile(unittest.TestCase):
    """Test load instance from file"""
    def setUp(self) -> None:
        pass

    def tearDown(self):
        fnl = ["Rectangle.json", "Square.json", "Base.json"]
        for name in fnl:
            if os.path.exists(name):
                os.remove(name)

    def test_load_file_not_exist(self):
        r = Rectangle(1, 1).load_from_file()
        self.assertListEqual(r, [])

    def test_load_from_square(self):
        s = Square(1)
        Square.save_to_file([s])
        l = Square.load_from_file()
        self.assertListEqual([str(s)], [str(x) for x in l])

    def test_load_from_rect(self):
        r = Rectangle(1, 1)
        Rectangle.save_to_file([r])
        l = Rectangle.load_from_file()
        self.assertListEqual([str(r)], [str(x) for x in l])

    def test_load_from_rects(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        l = Rectangle.load_from_file()
        self.assertListEqual([str(r1), str(r2)], [str(x) for x in l])

    def test_load_from_squares(self):
        s1 = Square(1, 1)
        s2 = Square(3, 4)
        Square.save_to_file([s1, s2])
        l = Square.load_from_file()
        self.assertListEqual([str(s1), str(s2)], [str(x) for x in l])

    def test_load_from_invalid_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(None)

if __name__ == "__main__":
    unittest.main()
