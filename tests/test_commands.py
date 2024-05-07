import pytest
from src.commands import CommandHandler

@pytest.fixture
def handler():
    return CommandHandler()

def test_add(handler):
    assert handler.handle_command("add 1 2 3") == 6
    assert handler.handle_command("add 1 -1") == 0

def test_divide(handler):
    assert handler.handle_command("divide 10 2") == 5
    assert "division by zero" in handler.handle_command("divide 10 0").lower()

def test_unknown_command(handler):
    assert "unknown command" in handler.handle_command("sqrt 16").lower()

def test_error_handling(handler):
    assert "inputs must be numbers" in handler.handle_command("add 10 two").lower()
