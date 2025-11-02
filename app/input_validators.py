import os
from app.exceptions import ValidationError

def validate_inputs(a, b):
    try:
        a = float(a)
        b = float(b)
    except Exception:
        raise ValidationError("Inputs must be numeric.")

    max_val = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1000000))
    if abs(a) > max_val or abs(b) > max_val:
        raise ValidationError(f"Input exceeds maximum allowed value ({max_val}).")

    return a, b
