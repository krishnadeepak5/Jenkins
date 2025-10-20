# test_app.py
import unittest
from app import calculate_area

class TestAreaCalculation(unittest.TestCase):
    """
    Test suite for the calculate_area function.
    """
    def test_positive_integers(self):
        # Test case with standard positive integer inputs
        self.assertEqual(calculate_area(5, 4), 20)

    def test_floating_point_numbers(self):
        # Test case with floating-point inputs
        self.assertAlmostEqual(calculate_area(2.5, 2), 5.0)

    def test_zero_input(self):
        # Test case for input validation (length cannot be zero or negative)
        with self.assertRaises(ValueError):
            calculate_area(0, 5)
            
    def test_negative_input(self):
        # Test case for input validation (width cannot be zero or negative)
        with self.assertRaises(ValueError):
            calculate_area(10, -3)

    def test_large_numbers(self):
        # Test case with large numbers
        self.assertEqual(calculate_area(1000, 1000), 1000000)
