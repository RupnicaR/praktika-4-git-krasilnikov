import unittest
from decimal import Decimal
from pricing import PaintCalculator


class PaintCalculatorTests(unittest.TestCase):
    def test_base_price(self):
        self.assertEqual(PaintCalculator().calculate("капот", "белый"), Decimal("12000.00"))

    def test_combined_coefficients(self):
        self.assertEqual(PaintCalculator().calculate("Передняя дверь", "серый металлик"), Decimal("18720.00"))

    def test_uppercase_yo(self):
        self.assertEqual(PaintCalculator().calculate("КРЫША", "ЖЁЛТЫЙ"), Decimal("14520.00"))

    def test_unknown_part_and_color(self):
        with self.assertRaises(ValueError):
            PaintCalculator().calculate("колесо", "белый")
        with self.assertRaises(ValueError):
            PaintCalculator().calculate("капот", "фиолетовый")


if __name__ == "__main__":
    unittest.main()
