"""Расчёт стоимости по коэффициентам варианта 1."""

from decimal import Decimal

BASE_PRICE = Decimal("12000")
COLORS = {
    "белый": Decimal("1"),
    "синий": Decimal("1"),
    "желтый": Decimal("1.1"),
    "красный": Decimal("1"),
    "перламутровый": Decimal("1.2"),
    "серый металлик": Decimal("1.3"),
}
PARTS = {
    "капот": Decimal("1"),
    "передняя дверь": Decimal("1.2"),
    "задняя дверь": Decimal("1.1"),
    "передний бампер": Decimal("1"),
    "задний бампер": Decimal("1"),
    "крыша": Decimal("1.1"),
}


class PaintCalculator:
    """Оценивает окраску одной детали по таблицам задания."""

    def calculate(self, part: str, color: str) -> Decimal:
        part = part.strip().casefold().replace("ё", "е")
        color = color.strip().casefold().replace("ё", "е")
        if part not in PARTS:
            raise ValueError("Неизвестная деталь")
        if color not in COLORS:
            raise ValueError("Неизвестный цвет")
        return (BASE_PRICE * PARTS[part] * COLORS[color]).quantize(Decimal("0.01"))
