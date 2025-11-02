import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.calculator import Calculator
from app.input_validators import validate_inputs
from app.exceptions import ValidationError, OperationError

def main():
    calc = Calculator()
    print("Welcome to the Enhanced Calculator!")
    print("Type 'help' to see available commands. Type 'exit' to quit.\n")

    while True:
        try:
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                print("Goodbye! ")
                break

            elif command == "help":
                print("""
Available Commands:
  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
  undo - Undo the last calculation
  redo - Redo the last undone calculation
  history - View calculation history
  clear - Clear calculation history
  save - Save history to CSV
  load - Load history from CSV
  exit - Quit the application
                """)

            elif command in ["add", "subtract", "multiply", "divide", "power", "root", "modulus", "int_divide", "percent", "abs_diff"]:
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                a, b = validate_inputs(a, b)
                result = calc.calculate(command, a, b)
                print(f"Result: {result}")

            elif command == "undo":
                calc.undo()
                print("Last calculation undone.")

            elif command == "redo":
                calc.redo()
                print("Last undone calculation redone.")

            elif command == "history":
                history = calc.history.get_history()
                if not history:
                    print("No calculations yet.")
                else:
                    print("\nCalculation History:")
                    for c in history:
                        print(f"{c.operation}({c.a}, {c.b}) = {c.result}")

            elif command == "clear":
                calc.history.clear()
                print("History cleared.")

            elif command == "save":
                calc.history.save_to_csv("history/calculation_history.csv")
                print("History saved to history/calculation_history.csv")

            elif command == "load":
                calc.history.load_from_csv("history/calculation_history.csv")
                print("History loaded from history/calculation_history.csv")

            else:
                print("Invalid command. Type 'help' to see available options.")

        except ValidationError as e:
            print(f"Validation Error: {e}")
        except OperationError as e:
            print(f"Operation Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
