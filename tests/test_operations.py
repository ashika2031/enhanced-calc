import pytest
from app.operations import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, PowerOperation, RootOperation, ModulusOperation, IntDivideOperation, PercentOperation, AbsDiffOperation

def test_add_operation():
    op = AddOperation()
    assert op.execute(5, 3) == 8

def test_subtract_operation():
    op = SubtractOperation()
    assert op.execute(10, 4) == 6

def test_multiply_operation():
    op = MultiplyOperation()
    assert op.execute(3, 4) == 12

def test_divide_operation():
    op = DivideOperation()
    assert op.execute(8, 2) == 4

def test_divide_by_zero():
    op = DivideOperation()
    with pytest.raises(ZeroDivisionError):
        op.execute(8, 0)

def test_power_operation():
    op = PowerOperation()
    assert op.execute(2, 3) == 8

def test_root_operation():
    op = RootOperation()
    assert round(op.execute(27, 3), 2) == 3.0

def test_modulus_operation():
    op = ModulusOperation()
    assert op.execute(10, 3) == 1

def test_int_divide_operation():
    op = IntDivideOperation()
    assert op.execute(10, 3) == 3

def test_percent_operation():
    op = PercentOperation()
    assert op.execute(50, 200) == 25

def test_abs_diff_operation():
    op = AbsDiffOperation()
    assert op.execute(10, 7) == 3
    assert op.execute(7, 10) == 3

def test_root_zero_degree():
    from app.operations import RootOperation
    op = RootOperation()
    with pytest.raises(ValueError):
        op.execute(4, 0)

def test_root_operation_zero_degree_error():
    from app.operations import RootOperation
    op = RootOperation()
    with pytest.raises(ValueError):
        op.execute(9, 0)
