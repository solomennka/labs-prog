import pytest
from src.lab1.task3 import logger_class


@logger_class(show_magic_methods=True)
class TestClassAllMethods:
    """Test class with all methods logged (magic methods included)"""

    def __init__(self, value=0):
        """Initialize with a value"""
        self.value = value

    def normal_method(self, x):
        """Regular instance method"""
        return self.value + x

    def another_method(self, a, b=""):
        """Method with multiple arguments"""
        return a + b + str(self.value)

    def __str__(self):
        """String representation"""
        return f"TestClass({self.value})"

    def __len__(self):
        """Length magic method"""
        return self.value

    def __call__(self, multiplier):
        """Call magic method"""
        return self.value * multiplier


@logger_class(show_magic_methods=False)
class TestClassNoMagic:
    """Test class with magic methods not logged"""

    def __init__(self, value=0):
        """Initialize with a value"""
        self.value = value

    def normal_method(self, x):
        """Regular instance method"""
        return self.value + x

    def __str__(self):
        """String representation"""
        return f"TestClass({self.value})"

    def __len__(self):
        """Length magic method"""
        return self.value


@pytest.fixture
def test_obj_all():
    """Fixture providing an instance of TestClassAllMethods"""
    return TestClassAllMethods(10)


@pytest.fixture
def test_obj_no_magic():
    """Fixture providing an instance of TestClassNoMagic"""
    return TestClassNoMagic(20)


def test_normal_method_logging(test_obj_all, capsys):
    """Test that regular methods are properly logged"""
    result = test_obj_all.normal_method(5)
    output = capsys.readouterr()

    # Check output content
    assert "Name class: TestClassAllMethods" in output.out
    assert "Method: normal_method" in output.out
    assert "Arguments: (5,), {}" in output.out or "Arguments: (5,), {}" in output.out
    assert "Time:" in output.out
    assert "Result: 15" in output.out

    # Check return value
    assert result == 15


def test_magic_method_logging_when_enabled(test_obj_all, capsys):
    """Test that magic methods are logged when show_magic_methods=True"""
    # Call magic methods
    str_result = str(test_obj_all)
    len_result = len(test_obj_all)
    call_result = test_obj_all(3)

    output = capsys.readouterr()

    # Check that all magic methods were logged
    assert "Method: __str__" in output.out
    assert "Method: __len__" in output.out
    assert "Method: __call__" in output.out

    # Check results
    assert str_result == "TestClass(10)"
    assert len_result == 10
    assert call_result == 30


def test_magic_method_not_logged_when_disabled(test_obj_no_magic, capsys):
    """Test that magic methods are not logged when show_magic_methods=False"""
    # Call regular method
    test_obj_no_magic.normal_method(5)

    # Call magic methods
    str_result = str(test_obj_no_magic)
    len_result = len(test_obj_no_magic)

    output = capsys.readouterr()

    # Check that regular method was logged
    assert "Method: normal_method" in output.out

    # Check that magic methods were not logged
    assert "Method: __str__" not in output.out
    assert "Method: __len__" not in output.out

    # Check results
    assert str_result == "TestClass(20)"
    assert len_result == 20


def test_method_with_multiple_arguments(test_obj_all, capsys):
    """Test method that takes multiple arguments"""
    result = test_obj_all.another_method("Hello", b=" World")
    output = capsys.readouterr()

    assert "Arguments: ('Hello',), {'b': ' World'}" in output.out or \
           "Arguments: ('Hello', ' World'), {}" in output.out
    assert result == "Hello World10"


def test_init_method_logging(capsys):
    """Test that __init__ method is logged"""
    obj = TestClassAllMethods(42)
    output = capsys.readouterr()

    assert "Method: __init__" in output.out
    assert "Arguments: (42,), {}" in output.out
    assert obj.value == 42


def test_method_without_arguments(test_obj_all, capsys):
    """Test method with no arguments (except self)"""
    result = test_obj_all.normal_method(0)
    output = capsys.readouterr()

    # Check arguments display
    assert "Arguments: (0,), {}" in output.out
    assert result == 10


def test_empty_class():
    """Test decorator with a class that has no methods"""
    @logger_class()
    class EmptyClass:
        """Class with no methods"""
        pass

    obj = EmptyClass()
    assert isinstance(obj, EmptyClass)
