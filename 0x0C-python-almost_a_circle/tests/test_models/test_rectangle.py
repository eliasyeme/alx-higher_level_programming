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
            Rectangle(0, 10)
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
    @patch('sys.stdout', new_callable=StringIO)
    def test_rect_display2x2(self, stdout):
        r1 = Rectangle(2, 2)
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
