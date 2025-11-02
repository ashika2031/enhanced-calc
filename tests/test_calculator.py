import pytest
from app.calculator import Calculator
from app.operations import AddOperation, DivideOperation
from app.exceptions import OperationError

def test_addition():
    calc = Calculator()
    result = calc.calculate('add', 5, 3)
    assert result == 8

def test_division():
    calc = Calculator()
    result = calc.calculate('divide', 9, 3)
    assert result == 3

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.calculate('divide', 9, 0)

def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.calculate('unknown', 5, 3)

def test_history_recording():
    calc = Calculator()
    calc.calculate('add', 1, 2)
    history = calc.history.get_history()
    assert len(history) == 1
    assert history[0].result == 3

def test_undo_redo():
    calc = Calculator()
    calc.calculate('add', 2, 2)
    calc.undo()
    assert len(calc.history.get_history()) == 0
    calc.redo()
    assert len(calc.history.get_history()) == 1

def test_auto_save_observer(tmp_path):
    calc = Calculator()
    calc.calculate('add', 4, 6)
    csv_path = tmp_path / "history.csv"
    calc.history.save_to_csv(csv_path)
    assert csv_path.exists()

def test_undo_redo_empty():
    calc = Calculator()
    # Nothing to undo — should not raise
    calc.undo()
    # Nothing to redo — should not raise
    calc.redo()
