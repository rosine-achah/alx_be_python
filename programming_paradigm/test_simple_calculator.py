import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
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

