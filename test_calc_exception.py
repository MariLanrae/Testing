import pytest
from calc3 import calculate, summ, subtract, multiply, err

def test_operations_with_zero():
    assert summ(0, 5) == 5
    assert summ(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert err(0, 5) == 0.0

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

def test_calculate_with_float_precision():
    result = calculate('1', 0.1, 0.2)
    assert result == pytest.approx(0.3)

    result = calculate('4', 1, 3)
    assert result == pytest.approx(0.3333333333333333)

def test_calculate_with_infinity():
    result = calculate('1', float('inf'), 1)
    assert result == float('inf')

def test_err_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        err(10, 0)

def test_summ_raises_type_error():
    with pytest.raises(TypeError):
        summ("abc", 2)

def test_calculate_raises_value_error():
    with pytest.raises(ValueError):
        calculate('9', 1, 2)