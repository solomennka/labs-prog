import pytest
from src.lab1.task4 import call_limiter


@call_limiter(limit=2)
class TestClassLimit2:
    """Test class with call limit of 2"""
    def method1(self, x=0):
        """First test method"""
        return f"method1 called with {x}"

    def method2(self):
        """Second test method"""
        return "method2 called"


@call_limiter(limit=3)
class TestClassLimit3:
    """Test class with call limit of 3"""
    def greet(self, name):
        """Method with parameter"""
        return f"Hello, {name}!"

    def count(self):
        """Method returning a value"""
        return 42


@call_limiter(limit=1)
class TestClassLimit1:
    """Test class with call limit of 1"""
    def single_use(self):
        """Method that can be called only once"""
        return "This method can be called only once"


@call_limiter(limit=0)
class TestClassLimit0:
    """Test class with call limit of 0 (should never work)"""
    def never_call(self):
        """Method that should never be called"""
        return "This should never be printed"


@pytest.fixture
def obj_limit2():
    """Fixture providing instance of TestClassLimit2"""
    return TestClassLimit2()


@pytest.fixture
def obj_limit3():
    """Fixture providing instance of TestClassLimit3"""
    return TestClassLimit3()


@pytest.fixture
def obj_limit1():
    """Fixture providing instance of TestClassLimit1"""
    return TestClassLimit1()


def test_method_called_within_limit(obj_limit2):
    """Test that method works when called within the limit"""
    # First call - should work
    result1 = obj_limit2.method1(5)
    assert result1 == "method1 called with 5"

    # Second call - should still work
    result2 = obj_limit2.method1(10)
    assert result2 == "method1 called with 10"


def test_different_instances_separate_counters():
    """Test that different instances have separate counters"""
    obj1 = TestClassLimit2()
    obj2 = TestClassLimit2()

    # Call obj1 twice (reaches its limit)
    obj1.method1()
    obj1.method1()

    # obj2 should still be able to call twice
    obj2.method1()
    obj2.method1()

    # obj1 third call should fail
    with pytest.raises(RuntimeError):
        obj1.method1()

    # obj2 third call should also fail
    with pytest.raises(RuntimeError):
        obj2.method1()


def test_method_with_parameters(obj_limit3):
    """Test that methods with parameters work correctly"""
    result = obj_limit3.greet("Alice")
    assert result == "Hello, Alice!"


def test_limit_of_one(obj_limit1):
    """Test with limit=1 (method can be called only once)"""
    # First call - should work
    result = obj_limit1.single_use()
    assert result == "This method can be called only once"

    # Second call - should fail
    with pytest.raises(RuntimeError):
        obj_limit1.single_use()


def test_limit_of_zero():
    """Test with limit=0 (method should never be callable)"""
    obj = TestClassLimit0()

    # First call should already fail
    with pytest.raises(RuntimeError):
        obj.never_call()


def test_different_instances_separate_counters():
    """Test that different instances have separate counters"""
    obj1 = TestClassLimit2()
    obj2 = TestClassLimit2()

    # Call obj1 twice (reaches its limit)
    obj1.method1()
    obj1.method1()

    # obj2 should still be able to call twice
    obj2.method1()
    obj2.method1()

    # obj1 third call should fail
    with pytest.raises(RuntimeError):
        obj1.method1()

    # obj2 third call should also fail
    with pytest.raises(RuntimeError):
        obj2.method1()


def test_multiple_instances_different_limits():
    """Test instances with different limit values"""

    @call_limiter(limit=2)
    class ClassA:
        def test(self):
            return "A"

    @call_limiter(limit=3)
    class ClassB:
        def test(self):
            return "B"

    obj_a = ClassA()
    obj_b = ClassB()

    # obj_a can be called 2 times
    obj_a.test()
    obj_a.test()
    with pytest.raises(RuntimeError):
        obj_a.test()

    # obj_b can be called 3 times
    obj_b.test()
    obj_b.test()
    obj_b.test()
    with pytest.raises(RuntimeError):
        obj_b.test()


def test_class_without_methods():
    """Test decorator on class with no methods"""
    @call_limiter(limit=3)
    class EmptyClass:
        """Class with no methods"""
        pass

    obj = EmptyClass()
    assert isinstance(obj, EmptyClass)
