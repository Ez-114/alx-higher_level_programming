#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-1, 2, 0, 3, -4]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_start(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["hello", "world", "zoo"]), "zoo")


if __name__ == '__main__':
    unittest.main()
