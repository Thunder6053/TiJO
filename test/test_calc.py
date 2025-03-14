import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("* test_add()")
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_subtract(self):
        print("* test_subtract()")
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        print("* test_multiply()")
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        print("* test_divide()")
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        print("* test_divide_by_zero()")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None


if __name__ == "__main__":
    unittest.main()