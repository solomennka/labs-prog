import pytest
import time
from src.lab1.task2 import retry


# Defining fixtures
@pytest.fixture
def third_success():
    """Fixture that creates a function that
    successfully executes on the third attempt"""
    count = 0

    @retry(attempts=5, delay=0.1, exceptions=(ValueError,))
    def func():
        nonlocal count
        count += 1
        if count < 3:
            raise ValueError()
        return f"Success on 3 attempt"
    return func


@pytest.fixture()
def errors():
    """A fixture that creates a function that
     always throws a ValueError"""
    @retry(attempts=3, delay=0.1, exceptions=(ValueError, ))
    def func():
        raise ValueError
    return func


@pytest.fixture()
def type_error():
    """A fixture that creates a function that
    throws a TypeError (not in the exceptions list)"""
    @retry(attempts=3, delay=0.1, exceptions=(ValueError, ))
    def func():
        raise TypeError
    return func


@pytest.fixture()
def none():
    """Fixture with exceptions=None (success for any result)"""
    @retry(attempts=3, delay=0.1, exceptions=None)
    def func():
        raise TypeError
    return func


def test_third_success(third_success, capsys):
    """Test: the function is successfully
     executed on the third attempt"""
    result = third_success()
    output = capsys.readouterr()
    assert "try: 1" in output.out
    assert "try: 2" in output.out
    assert "try: 3" in output.out
    assert result == "Success on 3 attempt"


def test_errors(errors, capsys):
    """Test: the function fails after all attempts"""
    with pytest.raises(ValueError):
        errors()
    output = capsys.readouterr()
    assert output.out.count("try:") == 3


def test_type_error(type_error, capsys):
    """Test: no repeats when an exception is not in the list"""
    with pytest.raises(TypeError):
        type_error()
    output = capsys.readouterr()
    assert output.out.count("try:") == 1


def test_none(none, capsys):
    """Test: success for any exception (exceptions=None)"""
    with pytest.raises(TypeError):
        none()
    output = capsys.readouterr()
    assert "try: 1" in output.out


def test_custom_arguments(capsys):
    """Test: passing arguments to a decorated function"""
    count = 0

    @retry(attempts=3, delay=0.1, exceptions=(ValueError, ))
    def multi(a, b, c=1):
        nonlocal count
        count += 1
        if count < 2:
            raise ValueError
        return a * b * c
    result = multi(2, 3, c=4)
    assert result == 24
    assert count == 2


def test_time():
    """Test: checking the delay between attempts"""
    count = 0
    start = time.perf_counter()

    @retry(attempts=3, delay=0.2, exceptions=(ValueError, ))
    def func():
        nonlocal count
        count += 1
        if count < 3:
            raise ValueError
        return "OK"
    result = func()
    end = time.perf_counter()
    assert result == "OK"
    assert count == 3
    assert end - start >= 0.4


def test_multiple_retry():
    """Test: several functions with retry"""
    @retry(attempts=2, delay=0.1, exceptions=(ValueError, ))
    def func1():
        return "func1"

    @retry(attempts=5, delay=0.2, exceptions=(TypeError, ))
    def func2():
        return "func2"

    assert func1() == "func1"
    assert func2() == "func2"


def test_zero_attempts():
    """Test: attempts = 0"""
    count = 0

    @retry(attempts=0, delay=0.1)
    def func():
        nonlocal count
        count += 1
        return "Zero"
    func()
    assert count == 0