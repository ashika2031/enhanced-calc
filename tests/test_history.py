import pandas as pd
from app.history import History
from app.calculation import Calculation

def test_add_and_clear_history(tmp_path):
    hist = History()
    hist.add(Calculation('add', 2, 3, 5))
    assert len(hist.get_history()) == 1
    hist.clear()
    assert len(hist.get_history()) == 0

def test_save_and_load_history(tmp_path):
    hist = History()
    hist.add(Calculation('add', 5, 5, 10))
    csv_path = tmp_path / "calc_history.csv"
    hist.save_to_csv(csv_path)
    new_hist = History()
    new_hist.load_from_csv(csv_path)
    assert len(new_hist.get_history()) == 1
    assert new_hist.get_history()[0].result == 10
