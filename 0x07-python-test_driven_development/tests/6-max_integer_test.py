#!/usr/bin/python3

"""Unittests for max_integer()"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer()"""

    def test_max_in_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_unordered_list(self):
        self.assertEqual(max_integer([2, 3, 1, 4]), 4)

    def test_max_in_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_single_element(self):
        self.assertEqual(max_integer([9]), 9)

    def test_max_in_floats(self):
        nl = [0.42, 99.07, 99.077]
        self.assertAlmostEqual(max_integer(nl), 99.077)

    def test_max_in_ints_and_floats(self):
        self.assertAlmostEqual(max_integer([7, 7.7, 77]), 77)

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

    def test_max_in_string(self):
        string = "deez"
        self.assertEqual(max_integer(string), 'z')

    def test_max_in_list_of_strings(self):
        strings = ["deez", "e10", "dragon", "bofa"]
        self.assertEqual(max_integer(strings), "e10")

if __name__ == '__main__':
    unittest.main()
