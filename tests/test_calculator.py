from calculator import Calculator
import pytest
def test_calculator():
    calculator = Calculator()
    # Testing get_last_calculation when there are no calculations
    assert calculator.get_last_calculation() is None

def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(1.5, 2.5) == 4.0

def test_subtract():
    assert Calculator.subtract(1, 2) == -1
    assert Calculator.subtract(1.5, 2.5) == -1.0

def test_multiply():
    assert Calculator.multiply(1, 2) == 2
    assert Calculator.multiply(1.5, 2.5) == 3.75

def test_divide():
    assert Calculator.divide(1, 2) == 0.5
    assert Calculator.divide(1.5, 2.5) == 0.6

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_calculation_history():
    calculator = Calculator()
    calculator.add_calculation("add", 1, 2, 3)
    calculator.add_calculation("subtract", 10, 5, 5)
    calculator.add_calculation("multiply", 2, 3, 6)
    calculator.add_calculation("divide", 10, 2, 5)

    last_calculation = calculator.get_last_calculation()
    assert last_calculation.operation == "divide"
    assert last_calculation.num1 == 10
    assert last_calculation.num2 == 2
    assert last_calculation.result == 5