import unittest
from calc import summ, subtract, multiply, err

class TestCalc(unittest.TestCase):

    # прописать setup и down

    def test_summ_integers(self):
        self.assertEqual(summ(3, 2), 5)
        self.assertEqual(summ(-1, 1), 0)
        self.assertEqual(summ(-8, -2), -10)

    def test_summ_floats(self):
        self.assertEqual(summ(7.5, 3.5), 11)
        self.assertAlmostEqual(summ(3.1, 3.8), 6.9)

    def test_subtract_integers(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(0, 2), -2)
        self.assertEqual(subtract(-1, -3), 2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(7.8, 7.0), 0.8)
        self.assertEqual(subtract(3.5, 1.1), 2.4)

    def test_multiply_integers(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-5, -100), 500)

    def test_multiply_floats(self):
        self.assertEqual(multiply(2.5, 2), 5)
        self.assertEqual(multiply(1.5, 2), 3)

    def test_err_integers(self):
        self.assertEqual(err(0, 5), 0)
        self.assertEqual(err(10, 2), 5)
        self.assertEqual(err(-12, 4), -3)
        self.assertEqual(err(-15, -3), 5)


    def test_err_floats(self):
        self.assertEqual(err(7.4, 2), 3.7)
        self.assertEqual(err(11.5, 2.5), 4.6)
        self.assertEqual(err(-15.5, -2.5), 6.2)


    def test_err_by_zero(self):
        self.assertEqual(err(10, 0), "Ошибка: деление на ноль!")

if __name__ == "__main__":
    unittest.main()

# Использование assertAlmostEqual() не помогло при сравнении действий с плавающей точкой