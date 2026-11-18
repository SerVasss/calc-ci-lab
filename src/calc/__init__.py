"""Пакет calc — учебный калькулятор для ЛПР 12."""

from calc.operations import (
    add,
    celsius_to_fahrenheit,
    divide,
    multiply,
    power,
    subtract,
)

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "celsius_to_fahrenheit",
]

__version__ = "0.1.0"
