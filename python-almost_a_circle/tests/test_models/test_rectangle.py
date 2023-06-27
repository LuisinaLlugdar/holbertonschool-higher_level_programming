#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    unittests for functions in Rectangle Class
    """

    def test_None(self):
        r0 = Rectangle(None, None)
        self.assertEqual(r0.width, None)
        self.assertEqual(r0.height, None)

    def test_ints(self):
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)

        r2 = Rectangle(6, 5)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 5)

        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 5)

    if __name__ == '__main__':
        unittest.main()
