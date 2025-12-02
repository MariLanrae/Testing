import pytest
import math
from calc2 import calculate, summ, subtract, multiply, err

def test_divide_by_zero():
    result = err(10, 0)
    assert result == "Ошибка: деление на ноль!"

def test_calculate_divide_by_zero():
    result = calculate('4', 10, 0)
    assert result == "Ошибка: деление на ноль!"

def test_invalid_choice():
    result = calculate('9', 1, 2)
    assert result is None

def test_invalid_choice_with_special_chars():
    result = calculate('a', 1, 2)
    assert result is None

def test_operations_with_zero():
    assert summ(0, 5) == 5
    assert summ(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert err(0, 5) == 0.0

def test_operations_with_negative_numbers():
    assert summ(-3, 2) == -1
    assert subtract(-3, 2) == -5
    assert multiply(-3, 2) == -6
    assert err(-10, 2) == -5.0

def test_operations_with_large_numbers():
    large = 10**10
    assert summ(large, large) == 2 * large
    assert subtract(large, large) == 0
    assert multiply(large, 2) == 2 * large

def test_operations_with_very_small_numbers():
    tiny = 1e-10
    assert summ(tiny, tiny) == pytest.approx(2 * tiny)
    assert subtract(tiny, tiny) == 0
    assert multiply(tiny, 2) == pytest.approx(2 * tiny)
    assert err(tiny, 2) == pytest.approx(tiny / 2)

def test_calculate_with_extreme_values():
    result = calculate('1', 1e10, 1e10)
    assert result == 2e10

    result = calculate('4', 1e-10, 2)
    assert result == pytest.approx(5e-11)

def test_calculate_with_negative_and_zero():
    result = calculate('2', -5, 0)
    assert result == -5

    result = calculate('3', -3, 0)
    assert result == 0

def test_calculate_with_float_precision():
    result = calculate('1', 0.1, 0.2)
    assert result == pytest.approx(0.3)

    result = calculate('4', 1, 3)
    assert result == pytest.approx(0.3333333333333333)

def test_calculate_with_infinity():
    result = calculate('1', float('inf'), 1)
    assert result == float('inf')

def test_calculate_with_nan():
    result = calculate('1', float('nan'), 1)
    assert math.isnan(result)

    result = calculate('2', float('nan'), 1)
    assert math.isnan(result)