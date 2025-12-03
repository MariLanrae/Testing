from unittest.mock import patch
from calc2 import calculate

def test_calculate_calls_summ():
    with patch('calc2.summ') as mock_summ:
        mock_summ.return_value = 30
        result = calculate('1', 10, 20)
        mock_summ.assert_called_once_with(10, 20)
        assert result == 30

def test_calculate_calls_subtract():
    with patch('calc2.subtract') as mock_subtract:
        mock_subtract.return_value = -10
        result = calculate('2', 10, 20)
        mock_subtract.assert_called_once_with(10, 20)
        assert result == -10

def test_calculate_calls_multiply():
    with patch('calc2.multiply') as mock_multiply:
        mock_multiply.return_value = 200
        result = calculate('3', 10, 20)
        mock_multiply.assert_called_once_with(10, 20)
        assert result == 200

def test_calculate_calls_err():
    with patch('calc2.err') as mock_err:
        mock_err.return_value = 0.5
        result = calculate('4', 10, 20)
        mock_err.assert_called_once_with(10, 20)
        assert result == 0.5

def test_calculate_calls_err_divide_by_zero():
    with patch('calc2.err') as mock_err:
        mock_err.return_value = "Ошибка: деление на ноль!"
        result = calculate('4', 10, 0)
        mock_err.assert_called_once_with(10, 0)
        assert result == "Ошибка: деление на ноль!"

def test_calculate_invalid_choice():
    with patch('calc2.summ') as mock_summ, \
         patch('calc2.subtract') as mock_subtract, \
         patch('calc2.multiply') as mock_multiply, \
         patch('calc2.err') as mock_err:

        result = calculate('9', 10, 20)
        mock_summ.assert_not_called()
        mock_subtract.assert_not_called()
        mock_multiply.assert_not_called()
        mock_err.assert_not_called()
        assert result is None