import pytest
from src.utils.history_manager import HistoryManager

def test_history_loading():
    hm = HistoryManager()
    assert hm.history.empty

def test_record_addition():
    hm = HistoryManager()
    hm.add_record("add 1 2", 3)
    assert not hm.history.empty
    assert hm.history.iloc[0]['Result'] == 3
