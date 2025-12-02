import pytest
from calc2 import calculate

@pytest.mark.parametrize("choice, x, y, expected", [
    ('1', 3, 2, 5),
    ('2', 5, 3, 2),
    ('3', 4, 5, 20),
    ('4', 10, 2, 5.0),
    ('4', 7, 2, pytest.approx(3.5)), #учет погрешности
    ('1', 1.1, 2.2, pytest.approx(3.3)),
])
def test_calculate_operations(choice, x, y, expected):
    result = calculate(choice, x, y)
    assert result == expected

def test_calculate_divide_by_zero():
    result = calculate('4', 10, 0)
    assert result == "Ошибка: деление на ноль!"

def test_calculate_invalid_choice():
    result = calculate('9', 1, 2)
    assert result is None

def test_chain_operations():
    result1 = calculate('1', 2, 3)
    result2 = calculate('3', result1, 2)
    result3 = calculate('4', result2, 2)

    assert result1 == 5
    assert result2 == 10
    assert result3 == 5.0