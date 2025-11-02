from app.operations import *
from app.exceptions import OperationError
from app.history import History
from app.calculation import Calculation

class Calculator:
    def __init__(self):
        self.history = History()
        self.undo_stack = []
        self.redo_stack = []

    def calculate(self, operation, a, b):
        operation = operation.lower()
        ops = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
            "power": PowerOperation(),
            "root": RootOperation(),
            "modulus": ModulusOperation(),
            "int_divide": IntDivideOperation(),
            "percent": PercentOperation(),
            "abs_diff": AbsDiffOperation(),
        }
        if operation not in ops:
            raise OperationError(f"Unsupported operation: {operation}")

        result = ops[operation].execute(a, b)
        calc = Calculation(operation, a, b, result)
        self.history.add(calc)
        self.undo_stack.append(calc)
        return result

    def undo(self):
        if not self.history.get_history():
            return
        last = self.history.get_history().pop()
        self.redo_stack.append(last)

    def redo(self):
        if not self.redo_stack:
            return
        redo_item = self.redo_stack.pop()
        self.history.add(redo_item)
