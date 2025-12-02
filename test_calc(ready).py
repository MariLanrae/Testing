import pytest
from calc import summ, subtract, multiply, err

def test_summ():
    assert summ(3, 2) == 5
    assert summ(-1, 1) == 0
    assert summ(-3, -11) == -14
    assert summ(2.5, 4.1) == 6.6
    assert summ(7, 3.8) == 10.8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-8, -3) == -5
    assert subtract(2.5, 1.5) == 1.0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(-5, -4) == 20
    assert multiply(3.6, 2) == 7.2

def test_err():
    assert err(10, 2) == 5
    assert err(7, 2) == 3.5
    assert err(-9, -3) == 3
    assert err(5, 2.5) == 2.0

def test_divide_by_zero():
    assert err(10, 0) == "Ошибка: деление на ноль!"

if __name__ == "__main__":
    pytest.main()