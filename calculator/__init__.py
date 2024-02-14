from typing import List, Union

class Calculation:
    def __init__(self, operation: str, num1: Union[int, float], num2: Union[int, float], result: Union[int, float]):
        self.operation = operation
        self.num1 = num1
        self.num2 = num2
        self.result = result

class Calculator:
    def __init__(self):
        self.history: List[Calculation] = []

    @staticmethod
    def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 + num2

    @staticmethod
    def subtract(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 - num2

    @staticmethod
    def multiply(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 * num2

    @staticmethod
    def divide(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

    def add_calculation(self, operation: str, num1: Union[int, float], num2: Union[int, float], result: Union[int, float]):
        calculation = Calculation(operation, num1, num2, result)
        self.history.append(calculation)

    def get_last_calculation(self) -> Union[Calculation, None]:
        if not self.history:
            return None
        return self.history[-1]