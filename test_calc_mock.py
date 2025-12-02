from unittest.mock import patch
import pytest
from calc2 import calculate

def test_calculate_calls_summ():
    """Тестируем, что calculate вызывает summ, используя mock."""
    with patch('calc2.summ') as mock_summ:
        mock_summ.return_value = 5  # Подменяем результат summ
        result = calculate('1', 10, 20)
        mock_summ.assert_called_once_with(10, 20)
        assert result == 5

def test_calculate_calls_subtract():
    """Тестируем, что calculate вызывает subtract, используя mock."""
    with patch('calc2.subtract') as mock_subtract:
        mock_subtract.return_value = -10
        result = calculate('2', 10, 20)
        mock_subtract.assert_called_once_with(10, 20)
        assert result == -10

def test_calculate_calls_multiply():
    """Тестируем, что calculate вызывает multiply, используя mock."""
    with patch('calc2.multiply') as mock_multiply:
        mock_multiply.return_value = 200
        result = calculate('3', 10, 20)
        mock_multiply.assert_called_once_with(10, 20)
        assert result == 200

def test_calculate_calls_err():
    """Тестируем, что calculate вызывает err, используя mock."""
    with patch('calc2.err') as mock_err:
        mock_err.return_value = 0.5
        result = calculate('4', 10, 20)
        mock_err.assert_called_once_with(10, 20)
        assert result == 0.5

def test_calculate_calls_err_divide_by_zero():
    """Тестируем, что calculate вызывает err и возвращает ошибку при делении на ноль."""
    with patch('calc2.err') as mock_err:
        mock_err.return_value = "Ошибка: деление на ноль!"
        result = calculate('4', 10, 0)
        mock_err.assert_called_once_with(10, 0)
        assert result == "Ошибка: деление на ноль!"

def test_calculate_invalid_choice():
    """Тестируем, что calculate возвращает None при неверном выборе."""
    with patch('calc2.summ') as mock_summ, \
         patch('calc2.subtract') as mock_subtract, \
         patch('calc2.multiply') as mock_multiply, \
         patch('calc2.err') as mock_err:

        result = calculate('9', 10, 20)
        # Проверяем, что ни одна из функций не была вызвана
        mock_summ.assert_not_called()
        mock_subtract.assert_not_called()
        mock_multiply.assert_not_called()
        mock_err.assert_not_called()
        assert result is None