import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        """Sprawdza, czy konstruktor rzuca wyjątek, gdy a = 0"""
        #Arrange
        a,b,c = 0, 2, 4

        #Act & Assert
        with self.assertRaises(ValueError):
            QuadraticEquation(a,b,c)

    def test_two_real_solutions(self):
        """Sprawdza, gdy delta > 0 (dwa pierwiastki)"""
        #Arrange
        a,b,c = 1, -3, 2
        eq = QuadraticEquation(a,b,c)

        #Act
        solutions = eq.solve()

        #Assert
        self.assertIsNotNone(solutions)
        self.assertAlmostEqual(solutions[0], 2.0)
        self.assertAlmostEqual(solutions[1], 1.0)

    def test_one_real_solutions(self):
        """Sprawdza, gdy delta = 0 (jeden pierwiastek)"""

        # Arrange
        a, b, c = 1, -2, 1
        eq = QuadraticEquation(a, b, c)

        # Act
        solutions = eq.solve()

        # Assert
        self.assertIsNotNone(solutions,1)
        self.assertAlmostEqual(solutions[0], 1.0)

    def test_no_real_solutions(self):
        """Sprawdza, gdy delta < 0 (brak rozwiązań)"""
        #Arrange
        a,b,c = 1, 2, 5
        eq = QuadraticEquation(a,b,c)

        #Act
        solutions = eq.solve()
        self.assertIsNotNone(solutions)

if __name__ == '__main__':
    unittest.main()