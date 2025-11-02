import pytest
from app.input_validators import validate_inputs, ValidationError

def test_valid_inputs():
    a, b = validate_inputs(5, 3)
    assert a == 5 and b == 3

def test_invalid_inputs():
    with pytest.raises(ValidationError):
        validate_inputs("abc", 3)

def test_value_out_of_range(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "10")
    with pytest.raises(ValidationError):
        validate_inputs(100, 2)
