import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(5, 5), 1)

    def test_divide_0(self):
        self.assertEqual(self.calc.divide(5, 0), "Invalid")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_0(self):
        self.assertEqual(self.calc.modulo(2, 2), 0)

if __name__ == '__main__':
    unittest.main()