"""Консольный калькулятор окраски одной детали."""

from labels import SUMMARY_LABEL
from pricing import COLORS, PARTS, PaintCalculator


def main() -> None:
    print("Калькулятор стоимости окраски автомобиля")
    print("Детали: " + ", ".join(PARTS))
    print("Цвета: " + ", ".join(COLORS))
    try:
        part = input("Деталь: ")
        color = input("Цвет: ")
        result = PaintCalculator().calculate(part, color)
        print(f"{SUMMARY_LABEL}: {result:.2f} руб.")
    except ValueError as exc:
        print(f"Ошибка ввода: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
