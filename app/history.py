import pandas as pd
from app.calculation import Calculation

class History:
    def __init__(self):
        self._history = []

    def add(self, calc: Calculation):
        self._history.append(calc)

    def get_history(self):
        return self._history

    def clear(self):
        self._history.clear()

    def save_to_csv(self, path):
        data = [
            {"operation": c.operation, "a": c.a, "b": c.b, "result": c.result, "timestamp": c.timestamp}
            for c in self._history
        ]
        df = pd.DataFrame(data)
        df.to_csv(path, index=False)

    def load_from_csv(self, path):
        df = pd.read_csv(path)
        for _, row in df.iterrows():
            self.add(Calculation(row["operation"], row["a"], row["b"], row["result"]))
