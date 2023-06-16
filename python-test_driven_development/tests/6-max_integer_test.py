#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    unittests for the function def max_integer(list=[]):
    """

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_positive_integers_and_floats(self):
        self.assertEqual(max_integer([9, 4, 6, 2, 7]), 9)
        self.assertEqual(max_integer([4.8, 3, 6.3, 10.7, 5.3]), 10.7)

    def test_negative_integers_and_floats(self):
        self.assertEqual(max_integer([-9, -4, -6, -2, -7]), -2)
        self.assertEqual(max_integer([-4.8, -3, -6.3, -10.7, -5.3]), -3)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_integer([9, -4, -6, 2, 7]), 9)
        self.assertEqual(max_integer([-4.8, 3, -6.3, -10.7, 5.3]), 5.3)

    def test_duplicated_integers_and_floats(self):
        self.assertEqual(max_integer([9, -9, 9, 9, -9]), 9)
        self.assertEqual(max_integer([-3.5, 3.5, -3.5, 3.5, -3.5]), 3.5)

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[5, 8.2], [3.7, -4]]), [5, 8.2])

    def test_list_of_strings(self):
        self.assertEqual(max_integer("6423"), '6')
        self.assertEqual(max_integer("apxr"), 'x')
        self.assertEqual(max_integer(['a', 'p', 'f', 'x', 'r', 'j']), 'x')
        self.assertEqual(max_integer(["aei", 'o']), 'o')

    def test_failures(self):
        self.assertRaises(TypeError, max_integer, {1, 3}, {5, 7, 9})
        self.assertRaises(TypeError, max_integer, {1, 3, 5, 7, 9})
        self.assertRaises(TypeError, max_integer, [4, -6.2, "Holberton", {0, 7}])

if __name__ == '__main__':
        unittest.main()
