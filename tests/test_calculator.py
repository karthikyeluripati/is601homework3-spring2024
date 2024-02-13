import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(5, 3) == 8
    assert calculator.history[0].operation == "5 + 3 = 8"

def test_subtract(calculator):
    assert calculator.subtract(8, 2) == 6
    assert calculator.history[0].operation == "8 - 2 = 6"

def test_multiply(calculator):
    assert calculator.multiply(4, 6) == 24
    assert calculator.history[0].operation == "4 * 6 = 24"

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.history[0].operation == "10 / 2 = 5.0"

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
