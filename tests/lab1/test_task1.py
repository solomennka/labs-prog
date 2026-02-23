import pytest
import time
from src.lab1.task1 import logger


# Defining fixtures
@pytest.fixture
def dec_add():
    @logger
    def add(a, b):
        return a + b
    return add


@pytest.fixture
def dec_multi():
    @logger
    def multi(a, b, c=3.0):
        return a * b * c
    return multi


# Tests
def test_add_integers(dec_add, capsys):
    """Test addition function with integers"""
    result = dec_add(4, 6)
    output = capsys.readouterr()
    assert "Name function: add" in output.out
    assert "Arguments function: (4, 6), {}" in output.out
    assert "Time:" in output.out
    assert "секунд" in output.out
    assert result == 10


def test_add_fractional(dec_add, capsys):
    """Test addition function with fractional"""
    result = dec_add(-1.24, 14.3)
    output = capsys.readouterr()
    assert "Name function: add" in output.out
    assert "Arguments function: (-1.24, 14.3), {}" in output.out
    assert "Time:" in output.out
    assert "секунд" in output.out
    assert result == 13.06


def test_multi_integers(dec_multi, capsys):
    """Test multiplication function with integers"""
    result = dec_multi(1, 2, c=10)
    output = capsys.readouterr()
    assert "Name function: multi" in output.out
    assert "Arguments function: (1, 2), {'c': 10}" in output.out
    assert "Time:" in output.out
    assert "секунд" in output.out
    assert result == 20


def test_multi_fractional(dec_multi, capsys):
    """Test multiplication function with fractional"""
    result = dec_multi(0.123, 45.3, c=-12.8)
    output = capsys.readouterr()
    assert "Name function: multi" in output.out
    assert "Arguments function: (0.123, 45.3), {'c': -12.8}" in output.out
    assert "Time:" in output.out
    assert "секунд" in output.out
    assert result == -71.32032


def test_time():
    """Test time change"""
    @logger
    def time_func():
        time.sleep(0.1)
        return "ok"

    start = time.perf_counter()
    result = time_func()
    end = time.perf_counter()
    assert result == "ok"
    assert end - start >= 0.1
