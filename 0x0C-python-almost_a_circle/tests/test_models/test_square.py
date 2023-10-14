import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle


class SquareTest(unittest.TestCase):
    """Base test cases"""
    def test_square_is_instance_of_rect(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_square_id(self):
        s1 = Square(10)
        s2 = Square(1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2)


class TestSquareSize(unittest.TestCase):
    """Rectangle width test"""
    def test_square_get_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_set_size(self):
        s = Square(1)
        s.size = 23
        self.assertEqual(s.size, 23)

    def test_square_0_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-7)

    def test_square_size_type_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.77)

    def test_square_size_type_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string")

    def test_square_size_type_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

class TestSquareX(unittest.TestCase):
    """Square x test"""
    def test_square_get_x_default(self):
        s = Square(1)
        self.assertEqual(s.x, 0)

    def test_square_get_already_set_x(self):
        s = Square(10, 9)
        self.assertEqual(s.x, 9)

    def test_square_get_already_set_x_with_y(self):
        s = Square(10, 2, 6)
        self.assertEqual(s.x, 2)

    def test_square_set_x(self):
        s = Square(1, 7)
        s.x = 8
        self.assertEqual(s.x, 8)

    def test_square_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_x_type_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "string")

    def test_square_x_type_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2.7)

    def test_square_x_type_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)


class TestSquareY(unittest.TestCase):
    """Rectangle y test"""
    def test_square_get_y_default(self):
        s = Square(1)
        self.assertEqual(s.y, 0)

    def test_square_get_already_set_y_with_x(self):
        s = Square(10, 2, 6)
        self.assertEqual(s.y, 6)

    def test_square_set_y(self):
        s = Square(1, 7, 5)
        s.y = 2
        self.assertEqual(s.y, 2)

    def test_square_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -7)

    def test_square_y_type_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "string")

    def test_square_y_type_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 2.7)

    def test_square_y_type_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)


class TestSquareArea(unittest.TestCase):
    """Square area test"""
    def test_square_area_small(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_square_area_medium(self):
        s = Square(400)
        self.assertEqual(s.area(), 160000)

    def test_square_area_anon(self):
        self.assertEqual(Square(3).area(), 9)

    def test_square_area_large(self):
        area = Square(123456789).area()
        self.assertEqual(area, 15241578750190521)

    def test_react_area_arg(self):
        with self.assertRaises(TypeError):
            Square(2).area(2)

    def test_square_area_modified_size(self):
        s = Square(2)
        s.size = 33
        self.assertEqual(s.area(), 1089)


class TestSquareDisplay(unittest.TestCase):
    """Square display stdout test"""
    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display2(self, stdout):
        s = Square(2)
        s.display()
        want = (("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display2x2_size_modified(self, stdout):
        s = Square(2)
        s.size = 5
        s.display()
        want = (("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display100x50(self, stdout):
        s = Square(100)
        s.display()
        want = (("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1(self, stdout):
        s = Square(1)
        s.display()
        want = (("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1x1x0(self, stdout):
        s = Square(1, 1)
        s.display()
        want = "\n" * s.y
        want += ((" " * s.x) + ("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1x1x0_x_modified(self, stdout):
        s = Square(1, 1)
        s.x = 7
        s.display()
        want = "\n" * s.y
        want += ((" " * s.x) + ("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1x0x7(self, stdout):
        s = Square(1, 0, 7)
        s.display()
        want = "\n" * s.y
        want += ((" " * s.x) + ("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1x0x7_y_modified(self, stdout):
        s = Square(1, 1, 0, 7)
        s.y = 4
        s.display()
        want = "\n" * s.y
        want += ((" " * s.x) + ("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_display1x1x0x7_x_and_y_modified(self, stdout):
        s = Square(1, 1, 0)
        s.x = 7
        s.y = 4
        s.display()
        want = "\n" * s.y
        want += ((" " * s.x) + ("#" * s.size) + "\n") * s.size
        self.assertEqual(stdout.getvalue(), want)

class TestSquarePrint(unittest.TestCase):
    """Square print test"""
    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_difault(self, stdout):
        s = Square(4)
        print(s)
        want = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_modified_size(self, stdout):
        s = Square(4)
        s.size = 20
        print(s)
        want = "[Square] ({}) 0/0 - 20\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_with_x(self, stdout):
        s = Square(4, 2)
        print(s)
        want = "[Square] ({}) 2/0 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_with_modified_x(self, stdout):
        s = Square(4, 2)
        s.x = 9
        print(s)
        want = "[Square] ({}) 9/0 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_with_x_and_y(self, stdout):
        s = Square(4, 7, 9)
        print(s)
        want = "[Square] ({}) 7/9 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_with_x_and_y_modified_y(self, stdout):
        s = Square(4, 7, 9)
        s.y = 12
        print(s)
        want = "[Square] ({}) 7/12 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)

    @patch('sys.stdout', new_callable=StringIO)
    def test_square_print_with_x_and_y_modified_x_and_y(self, stdout):
        s = Square(4, 7, 9)
        s.x = 23
        s.y = 12
        print(s)
        want = "[Square] ({}) 23/12 - 4\n".format(s.id)
        self.assertEqual(stdout.getvalue(), want)
