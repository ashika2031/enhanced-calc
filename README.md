# Enhanced Calculator – Command-Line Application

An advanced, modular, and fully-tested **Python calculator** supporting multiple arithmetic operations, undo/redo using the **Memento Pattern**, real-time logging and auto-saving through the **Observer Pattern**, and operation creation via the **Factory Pattern**.
This project integrates **GitHub Actions CI/CD** for automated testing and achieves **100% unit test coverage**.

---

## Badges

![Python application](https://github.com/ashika2031/enhanced-calc/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Features

###  Core Functionalities

* **Arithmetic Operations**

  * Addition, Subtraction, Multiplication, Division
  * Power, Root, Modulus, Integer Division
  * Percentage, Absolute Difference
* **Undo/Redo** history using the **Memento Pattern**
* **Logging & Auto-Save** with the **Observer Pattern**
* **Dynamic History Management** (save/load CSV via `pandas`)
* **Environment-Driven Configuration** using `.env`
* **Color-Coded REPL Interface** powered by `colorama`
* **100% Test Coverage** verified through CI/CD pipeline

---

## Design Patterns Implemented

| Pattern                  | Purpose                                          |
| ------------------------ | ------------------------------------------------ |
| **Factory**              | Dynamically creates operation instances          |
| **Observer**             | Automatically logs and saves calculation history |
| **Memento**              | Enables undo/redo functionality                  |
| **Decorator (Optional)** | Extends help menu dynamically                    |
| **Command (Optional)**   | Provides extensible command encapsulation        |
| **REPL Loop**            | Handles interactive user input/output            |

---

##  Project Structure

```
enhanced_calculator/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── operations.py
│   ├── logger.py
│   └── repl.py
├── tests/
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   ├── test_operations.py
│   └── ...
├── .github/workflows/python-app.yml
├── .coveragerc
├── .env
├── requirements.txt
└── README.md
```

---

## Configuration (`.env` Example)

```env
# Logging
CALCULATOR_LOG_DIR=logs
CALCULATOR_LOG_FILE=calculator.log

# History
CALCULATOR_HISTORY_DIR=history
CALCULATOR_HISTORY_FILE=history.csv
CALCULATOR_MAX_HISTORY_SIZE=50
CALCULATOR_AUTO_SAVE=true

# Limits
CALCULATOR_PRECISION=4
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

---

## Installation & Setup

```bash
# Clone repository
git clone https://github.com/ashika2031/enhanced-calc.git
cd enhanced-calc

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

##  Usage (REPL CLI)

Run the interactive calculator:

```bash
python -m app.repl
```

### Supported Commands

| Command                         | Description                      |
| ------------------------------- | -------------------------------- |
| add, subtract, multiply, divide | Basic arithmetic                 |
| power, root                     | Exponentiation & roots           |
| modulus, int_divide             | Modulo & integer division        |
| percent, abs_diff               | Percentage & absolute difference |
| undo, redo                      | Undo or redo last operation      |
| history, clear                  | View or clear history            |
| save, load                      | Save or load history CSV         |
| help                            | Display available commands       |
| exit                            | Exit the application             |

---

### Example Session

```
calc> add 10 5
Result: 15.0

calc> power 2 3
Result: 8.0

calc> undo
Undone: power(2.0, 3.0) = 8.0

calc> redo
Redone: power(2.0, 3.0) = 8.0

calc> history
add(10.0, 5.0) = 15.0
power(2.0, 3.0) = 8.0
```

---

## Testing & Coverage

Run all tests with full coverage:

```bash
(base) patchigoollaashika@Ashis-MacBook-Air enhanced_calculator % pytest --cov=app --cov-report=term-missing

..........................                                                                                [100%]
================================================ tests coverage =================================================
_______________________________ coverage: platform darwin, python 3.12.4-final-0 ________________________________

Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
app/__init__.py                 0      0   100%
app/calculation.py              8      0   100%
app/calculator.py              29      0   100%
app/calculator_config.py        0      0   100%
app/calculator_memento.py       0      0   100%
app/exceptions.py               4      0   100%
app/history.py                 19      0   100%
app/input_validators.py        12      0   100%
app/logger.py                   0      0   100%
app/operations.py              35      0   100%
app/repl.py                     0      0   100%
---------------------------------------------------------
TOTAL                         107      0   100%
26 passed in 0.80s

```

---

## Continuous Integration (GitHub Actions)

### Workflow File: `.github/workflows/python-app.yml`

```yaml
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests with coverage
        run: |
          pytest --cov=app --cov-config=.coveragerc --cov-fail-under=100
```
---





