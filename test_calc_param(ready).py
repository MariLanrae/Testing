import pytest
from calc import summ, subtract, multiply, err

@pytest.mark.parametrize("x, y, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (-3, -11, -14),
    (2.5, 4.1, 6.6),
    (7, 3.8, 10.8),
])
def test_summ(x, y, expected):
    assert summ(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
    (0, 5, -5),
    (-8, -3, -5),
    (2.5, 1.5, 1.0),
])
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (-5, -4, 20),
    (3.6, 2, 7.2),
])
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (7, 2, 3.5),
    (-9, -3, 3),
    (5, 2.5, 2.0),
])
def test_err(x, y, expected):
    assert err(x, y) == expected

def test_err_by_zero():
    assert err(10, 0) == "Ошибка: деление на ноль!"