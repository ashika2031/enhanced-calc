class AddOperation:
    def execute(self, a, b):
        return a + b

class SubtractOperation:
    def execute(self, a, b):
        return a - b

class MultiplyOperation:
    def execute(self, a, b):
        return a * b

class DivideOperation:
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

class PowerOperation:
    def execute(self, a, b):
        return a ** b

class RootOperation:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root cannot have degree 0")
        return a ** (1 / b)

class ModulusOperation:
    def execute(self, a, b):
        return a % b

class IntDivideOperation:
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero") #pragma: no cover
        return a // b

class PercentOperation:
    def execute(self, a, b):
        return (a / b) * 100

class AbsDiffOperation:
    def execute(self, a, b):
        return abs(a - b)
