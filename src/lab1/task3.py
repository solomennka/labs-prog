import time
from typing import Any, Callable, Type


def logger(func: Callable) -> Callable:
    """
    Decorator that outputs function with its information.
    @param func: Callable - function in decorator
    @return: Callable - same function with additional expressions
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function with additional expressions
        @param args: Any - positional arguments from function
        @param kwargs: Any - keyword arguments from function
        @return: Any - error or result
        """
        class_name = args[0].__class__.__name__ if args else "Unknown"
        print(f"Name class: {class_name}")
        print(f"Method: {func.__name__}")
        print(f"Arguments: {args[1:] if args else args}, {kwargs}")
        # Time counting
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        time_f = end - start
        print(f"Time: {time_f: .4f} секунд")
        print(f"Result: {result}")
        print()
        return result
    return wrapper


def logger_class(show_magic_methods: bool = True):
    """
    Decorator for class with flag show_magic_methods
    @param show_magic_methods: bool - whether to log magical methods (by default True)
    @return: Callable - same class but with modified methods
    """
    def decorator(cls: Type) -> Type:
        """
        Wrapper function for class with additional expressions
        @param cls: Type - original class
        @return: Type - class with modified methods
        """
        # All methods in class
        methods = {
            name: method
            for name, method in vars(cls).items()
            if callable(method)
        }
        for name, method in methods.items():
            # Parameter that method magic or not
            magic = name.startswith("__") and name.endswith("__")
            if show_magic_methods or not magic:
                # Replacing the old method with the logged one
                setattr(cls, name, logger(method))
        return cls
    return decorator


@logger_class(show_magic_methods=False)
class MyClass1:
    def normal_method(self):
        return "обычный"

    def __str__(self):
        return "магический"


obj1 = MyClass1()
obj1.normal_method()
str(obj1)
