import unittest
from calculator1 import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator(2, 3)
        self.assertEqual(calculator.add(), 5)

    def test_subtract(self):
        calculator = Calculator(10, 5)
        self.assertEqual(calculator.subtract(), 5)

    def test_multiply(self):
        calculator = Calculator(4, 8)
        self.assertEqual(calculator.multiply(), 32)

    def test_divide(self):
        calculator = Calculator(10, 2)
        self.assertEqual(calculator.divide(), 5)
        calculator = Calculator(7, 0)
        self.assertEqual(calculator.divide(), "Деление на ноль невозможно")

if __name__ == '__main__':
    unittest.main()
