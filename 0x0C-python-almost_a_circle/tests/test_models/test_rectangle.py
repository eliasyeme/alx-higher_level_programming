import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectagle(unittest.TestCase):

    def setUp(self):
        self.r2_10x2 = Rectangle(10, 2)
        self.r2_1x7 = Rectangle(1, 7)
        self.r3_10x2_9 = Rectangle(10, 2, 9)
        self.r3_2x10_6 = Rectangle(2, 10, 6)
        self.r4_10x2_6_9 = Rectangle(10, 2, 6, 9)
        self.r4_2x10_9_6 = Rectangle(2, 10, 9, 6)
        self.r5_10x2_6_9_12 = Rectangle(10, 2, 6, 9, 12)
        self.r5_2x10_9_6_21 = Rectangle(2, 10, 9, 6, 21)

    def tearDown(self):
        pass

    def test_rectangle_is_instance_of_base(self):
        self.assertIsInstance(Rectangle(0, 0), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_rect_id(self):
        id1 = self.r2_10x2.id
        id2 = self.r2_1x7.id - 1
        self.assertEqual(id1, id2)

    def test_rect_get_width(self):
        self.assertEqual(self.r2_1x7.width, 1)

    def test_rect_get_height(self):
        self.assertEqual(self.r2_1x7.height, 7)

    def test_rect_get_x_default(self):
        self.assertEqual(self.r2_1x7.x, 0)

    def test_rect_get_y_default(self):
        self.assertEqual(self.r2_1x7.y, 0)

    def test_rect_get_already_set_x(self):
        self.assertEqual(self.r3_10x2_9.x, 9)

    def test_rect_get_already_set_x_with_y(self):
        self.assertEqual(self.r4_10x2_6_9.x, 6)

    def test_rect_get_already_set_y_with_x(self):
        self.assertEqual(self.r4_10x2_6_9.y, 9)

    def test_rect_set_width(self):
        self.r2_1x7.width = 23
        self.assertEqual(self.r2_1x7.width, 23)

    def test_rect_set_height(self):
        self.r2_1x7.height = 32
        self.assertEqual(self.r2_1x7.height, 32)

    def test_rect_set_x(self):
        self.r2_1x7.x = 2
        self.assertEqual(self.r2_1x7.x, 2)

    def test_rect_set_y(self):
        self.r2_1x7.y = 2
        self.assertEqual(self.r2_1x7.y, 2)
