import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectagle(unittest.TestCase):
    """Base rectangle class test"""
    def test_rect_is_instance_of_base(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_rect_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2)


class TestRectangleWidth(unittest.TestCase):
    """Rectangle width test"""
    def test_rect_get_width(self):
        r1 = Rectangle(1, 7)
        self.assertEqual(r1.width, 1)

    def test_rect_set_width(self):
        r1 = Rectangle(1, 7)
        r1.width = 23
        self.assertEqual(r1.width, 23)

    def test_rect_0_width(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 10)
        width_err = "width must be > 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_negative_width(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-7, 10)
        width_err = "width must be > 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_width_type_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(3.77, 1)
        width_err = "width must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_width_type_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("string", 1)
        width_err = "width must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_width_type_None(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(None, 1)
        width_err = "width must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)


class TestRectangleHeight(unittest.TestCase):
    """Rectangle height test"""
    def test_rect_get_height(self):
        r1 = Rectangle(1, 7)
        self.assertEqual(r1.height, 7)

    def test_rect_set_height(self):
        r1 = Rectangle(1, 7)
        r1.height= 32
        self.assertEqual(r1.height, 32)

    def test_rect_0_height(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        width_err = "height must be > 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_negative_height(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        width_err = "height must be > 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_height_type_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 3.77)
        width_err = "height must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_height_type_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "string")
        width_err = "height must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_height_type_None(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, None)
        width_err = "height must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)


class TestRectangleX(unittest.TestCase):
    """Rectangle x test"""
    def test_rect_get_x_default(self):
        r1 = Rectangle(1, 7)
        self.assertEqual(r1.x, 0)

    def test_rect_get_already_set_x(self):
        r1 = Rectangle(10, 2, 9)
        self.assertEqual(r1.x, 9)

    def test_rect_get_already_set_x_with_y(self):
        r1 = Rectangle(10, 2, 6, 9)
        self.assertEqual(r1.x, 6)

    def test_rect_set_x(self):
        r1 = Rectangle(1, 7)
        r1.x = 8
        self.assertEqual(r1.x, 8)

    def test_rect_negative_x(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -2)
        width_err = "x must be >= 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_x_type_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, "string")
        width_err = "x must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_x_type_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 2.7)
        width_err = "x must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_x_type_None(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, None)
        width_err = "x must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)


class TestRectangleY(unittest.TestCase):
    """Rectangle y test"""
    def test_rect_get_y_default(self):
        r1 = Rectangle(1, 7)
        self.assertEqual(r1.y, 0)

    def test_rect_get_already_set_y_with_x(self):
        r1 = Rectangle(10, 2, 6, 9)
        self.assertEqual(r1.y, 9)

    def test_rect_set_y(self):
        r1 = Rectangle(1, 7)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_rect_negative_y(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, 2, -7)
        width_err = "y must be >= 0"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_y_type_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 1, "string")
        width_err = "y must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_y_type_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 2, 2.7)
        width_err = "y must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)

    def test_rect_y_type_None(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 1, None)
        width_err = "y must be an integer"
        err_msg = e.exception.__str__()
        self.assertEqual(width_err, err_msg)


class TestRectangleArea(unittest.TestCase):
    """Rectangle area test"""
    def test_rect_area_small(self):
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)

    def test_rect_area_medium(self):
        r1 = Rectangle(200, 400)
        self.assertEqual(r1.area(), 80000)

    def test_rect_area_anon(self):
        self.assertEqual(Rectangle(3, 7).area(), 21)

    def test_rect_area_large(self):
        area = Rectangle(123456789, 987654321).area()
        self.assertEqual(area, 121932631112635269)

    def test_react_area_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 7).area(2)

    def test_rect_area_modified_width(self):
        r1 = Rectangle(2, 2)
        r1.width = 33
        self.assertEqual(r1.area(), 66)

    def test_rect_area_modified_height(self):
        r1 = Rectangle(10, 2)
        r1.height = 33
        self.assertEqual(r1.area(), 330)

    def test_rect_area_modified_width_height(self):
        r1 = Rectangle(10, 2)
        r1.width = 11
        r1.height = 22
        self.assertEqual(r1.area(), 242)


class TestRectangleDisplay(unittest.TestCase):
    """Rectangle display stdout test"""
    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display2x2(self, stdout):
        r1 = Rectangle(2, 2)
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display2x2_width_modified(self, stdout):
        r1 = Rectangle(2, 2)
        r1.width = 5
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display2x2_height_modified(self, stdout):
        r1 = Rectangle(2, 2)
        r1.height = 5
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display2x2_width__and_height_modified(self, stdout):
        r1 = Rectangle(2, 2)
        r1.width = 7
        r1.height = 5
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display3x4(self, stdout):
        r1 = Rectangle(3, 4)
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display100x50(self, stdout):
        r1 = Rectangle(100, 50)
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1(self, stdout):
        r1 = Rectangle(1, 1)
        r1.display()
        want = "\n".join(["#" * r1.width for _ in range(r1.height)])
        want += "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1x1x0(self, stdout):
        r1 = Rectangle(1, 1, 1)
        r1.display()
        want = "\n".join(
            [(" " * r1.x) + ("#" * r1.width) for _ in range(r1.height)]
        ) + "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1x1x0_x_modified(self, stdout):
        r1 = Rectangle(1, 1, 1)
        r1.x = 7
        r1.display()
        want = "\n".join(
            [(" " * r1.x) + ("#" * r1.width) for _ in range(r1.height)]
        ) + "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1x0x7(self, stdout):
        r1 = Rectangle(1, 1, 0, 7)
        r1.display()
        want = "\n" * r1.y
        want += "\n".join(
            [(" " * r1.x) + ("#" * r1.width) for _ in range(r1.height)]
        ) + "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1x0x7_y_modified(self, stdout):
        r1 = Rectangle(1, 1, 0, 7)
        r1.y = 4
        r1.display()
        want = "\n" * r1.y
        want += "\n".join(
            [(" " * r1.x) + ("#" * r1.width) for _ in range(r1.height)]
        ) + "\n"
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display1x1x0x7_x_and_y_modified(self, stdout):
        r1 = Rectangle(1, 1, 0, 7)
        r1.x = 7
        r1.y = 4
        r1.display()
        want = "\n" * r1.y
        want += "\n".join(
            [(" " * r1.x) + ("#" * r1.width) for _ in range(r1.height)]
        ) + "\n"
        self.assertEqual(stdout.getvalue(), want)

class TestRectanglePrint(unittest.TestCase):
    """Rectangle print test"""
    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_difault(self, stdout):
        r = Rectangle(4, 2)
        print(r)
        want = "[Rectangle] ({:d}) 0/0 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_modified_width(self, stdout):
        r = Rectangle(4, 2)
        r.width = 20
        print(r)
        want = "[Rectangle] ({:d}) 0/0 - 20/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_modified_height(self, stdout):
        r = Rectangle(4, 2)
        r.height = 72
        print(r)
        want = "[Rectangle] ({:d}) 0/0 - 4/72\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_modified_width_and_height(self, stdout):
        r = Rectangle(4, 2)
        r.width = 27
        r.height = 72
        print(r)
        want = "[Rectangle] ({:d}) 0/0 - 27/72\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_with_x(self, stdout):
        r = Rectangle(4, 2, 7)
        print(r)
        want = "[Rectangle] ({:d}) 7/0 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_with_modified_x(self, stdout):
        r = Rectangle(4, 2, 7)
        r.x = 9
        print(r)
        want = "[Rectangle] ({:d}) 9/0 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_with_x_and_y(self, stdout):
        r = Rectangle(4, 2, 7, 9)
        print(r)
        want = "[Rectangle] ({:d}) 7/9 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_with_x_and_y_modified_y(self, stdout):
        r = Rectangle(4, 2, 7, 9)
        r.y = 12
        print(r)
        want = "[Rectangle] ({:d}) 7/12 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_print_with_x_and_y_modified_x_and_y(self, stdout):
        r = Rectangle(4, 2, 7, 9)
        r.x = 23
        r.y = 12
        print(r)
        want = "[Rectangle] ({:d}) 23/12 - 4/2\n".format(r.id)
        self.assertEqual(stdout.getvalue(), want)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Rectangle update test"""
    def setUp(self):
        self.r = Rectangle(1, 1, 1, 1, 1)

    def test_rect_update_no_args(self):
        self.r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(self.r))

    def test_rect_update_none_id(self):
        self.r.update(None)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(self.r))

    def test_rect_update_1_args(self):
        self.r.update(7)
        self.assertEqual("[Rectangle] (7) 1/1 - 1/1", str(self.r))

    def test_rect_update_2_args(self):
        self.r.update(7, 6)
        self.assertEqual("[Rectangle] (7) 1/1 - 6/1", str(self.r))

    def test_rect_update_3_args(self):
        self.r.update(7, 6, 5)
        self.assertEqual("[Rectangle] (7) 1/1 - 6/5", str(self.r))

    def test_rect_update_4_args(self):
        self.r.update(7, 6, 5, 4)
        self.assertEqual("[Rectangle] (7) 4/1 - 6/5", str(self.r))

    def test_rect_update_5_args(self):
        self.r.update(7, 6, 5, 4, 3)
        self.assertEqual("[Rectangle] (7) 4/3 - 6/5", str(self.r))

    def test_rect_update_more_than_5(self):
        self.r.update(7, 6, 5, 4, 3, 2, 1)
        self.assertEqual("[Rectangle] (7) 4/3 - 6/5", str(self.r))

    def test_rect_update_twice(self):
        self.r.update(7, 6, 5, 4, 3)
        self.r.update(70, 60, 50, 40, 30)
        self.assertEqual("[Rectangle] (70) 40/30 - 60/50", str(self.r))

    def test_rect_update_invalid_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(None, "")

    def test_rect_update_invalid_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.update(None, 1, "")

    def test_rect_update_invalid_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(None, 1, 1, "")

    def test_rect_update_invalid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(None, 1, 1, 1, "")

    def test_rect_update_invalid_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(None, 0)

    def test_rect_update_invalid_value_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(None, 1, 0)

    def test_rect_update_invalid_value_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(None, 1, 1, -1)

    def test_rect_update_invalid_value_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(None, 1, 1, 1, -1)

class TestRectangleUpdateKwargs(unittest.TestCase):
    """Rectangle update key word args test"""
    def setUp(self):
        self.r = Rectangle(1, 1, 1, 1, 1)

    def test_rect_update_id(self):
        self.r.update(id=7)
        self.assertEqual("[Rectangle] (7) 1/1 - 1/1", str(self.r))

    def test_rect_update_id_width(self):
        self.r.update(width=6, id=7)
        self.assertEqual("[Rectangle] (7) 1/1 - 6/1", str(self.r))

    def test_rect_update_id_widht_height(self):
        self.r.update(id=7, height=5, width=6)
        self.assertEqual("[Rectangle] (7) 1/1 - 6/5", str(self.r))

    def test_rect_update_id_width_height_x(self):
        self.r.update(x=4, height=5, width=6, id=7)
        self.assertEqual("[Rectangle] (7) 4/1 - 6/5", str(self.r))

    def test_rect_update_id_width_height_x_y(self):
        self.r.update(height=5, width=6, id=7, y=3, x=4)
        self.assertEqual("[Rectangle] (7) 4/3 - 6/5", str(self.r))

    def test_rect_update_more_than_5(self):
        self.r.update(7, 6, 5, 4, width=3, id=2, y=1)
        self.assertEqual("[Rectangle] (7) 4/1 - 6/5", str(self.r))

    def test_rect_update_twice(self):
        self.r.update(x=4, y=3, height=5, width=6, id=7)
        self.r.update(x=40, y=30, height=50, width=60, id=70)
        self.assertEqual("[Rectangle] (70) 40/30 - 60/50", str(self.r))

    def test_rect_update_invalid_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(width="")

    def test_rect_update_invalid_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.update(height="")

    def test_rect_update_invalid_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(x="")

    def test_rect_update_invalid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(y="")

    def test_rect_update_invalid_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(width=0)

    def test_rect_update_invalid_value_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(height=0)

    def test_rect_update_invalid_value_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(x=-1)

    def test_rect_update_invalid_value_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(y=-1)


class TestRectangleToDict(unittest.TestCase):
    """Test to_dictionary public method"""
    def setUp(self):
        self.r = Rectangle(1, 1, 0, 0, 1)
        self.dict = {
            "id": 1,
            "width": 1,
            "height": 1,
            "x": 0,
            "y": 0
        }

    def test_rect_dict_minmal(self):
        got = self.r.to_dictionary()
        self.assertDictEqual(got, self.dict)

    def test_rect_dict_modified_id(self):
        self.r.update(id=9)
        self.dict["id"] = 9
        got = self.r.to_dictionary()
        self.assertDictEqual(got, self.dict)

    def test_rect_dict_modified_width_height(self):
        self.r.update(width=7, height=9)
        got = self.r.to_dictionary()
        self.dict["width"] = 7
        self.dict["height"] = 9
        self.assertDictEqual(got, self.dict)

    def test_rect_dict_modified_x_y(self):
        self.r.update(x=7, y=9)
        got = self.r.to_dictionary()
        self.dict["x"] = 7
        self.dict["y"] = 9
        self.assertDictEqual(got, self.dict)

    def test_rect_dict_modified_all(self):
        self.r.update(id=2, width=3, height=4, x=7, y=9)
        got = self.r.to_dictionary()
        self.dict["id"] = 2
        self.dict["width"] = 3
        self.dict["height"] = 4
        self.dict["x"] = 7
        self.dict["y"] = 9
        self.assertDictEqual(got, self.dict)

    def test_rect_dict_type_error(self):
        with self.assertRaises(TypeError):
            self.r.to_dictionary(None)
