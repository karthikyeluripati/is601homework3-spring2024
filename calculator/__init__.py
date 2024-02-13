class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        calc = Calculation(f"{a} + {b} = {result}")
        self._save_history(calc)
        return result

    def subtract(self, a, b):
        result = a - b
        calc = Calculation(f"{a} - {b} = {result}")
        self._save_history(calc)
        return result

    def multiply(self, a, b):
        result = a * b
        calc = Calculation(f"{a} * {b} = {result}")
        self._save_history(calc)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        calc = Calculation(f"{a} / {b} = {result}")
        self._save_history(calc)
        return result

    def _save_history(self, calculation):
        self.history.append(calculation)


class Calculation:
    def __init__(self, operation):
        self.operation = operation
