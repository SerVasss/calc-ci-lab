"""Арифметические операции учебного калькулятора."""


def add(a: float, b: float) -> float:
    """Возвращает сумму a и b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a и b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение a и b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает частное a и b.

    Вызывает ZeroDivisionError с понятным сообщением при делении на ноль.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b


def power(base: float, exponent: int) -> float:
    """Возводит base в целую степень exponent без использования оператора **."""
    if not isinstance(exponent, int):
        raise TypeError("Показатель степени должен быть целым числом")
    result = 1.0
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result


def celsius_to_fahrenheit(c: float) -> float:
    """Переводит температуру из Цельсия в Фаренгейты."""
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("Температура должна быть числом")
    return c * 9 / 5 + 32
