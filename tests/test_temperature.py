"""Тесты перевода температуры."""

import pytest

from calc.operations import celsius_to_fahrenheit


@pytest.mark.parametrize(
    "celsius, expected",
    [(0, 32), (100, 212), (-40, -40)],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


def test_celsius_to_fahrenheit_invalid_input():
    with pytest.raises(TypeError, match="Температура должна быть числом"):
        celsius_to_fahrenheit("hello")
