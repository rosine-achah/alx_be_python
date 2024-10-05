import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

   
# Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,2), 6)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(-1,1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,2 ), 4)
        self.assertEqual(self.calc.multiply(-2, 2 ), -4)
        self.assertEqual(self.calc.multiply(-2, -2 ), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8,4 ), 2)
        self.assertEqual(self.calc.divide(-8, 2 ), -4)
        self.assertEqual(self.calc.divide(-8,-4 ), 2)


        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(8, 0)

if __name__ == "__main__":
    unittest.main() 

