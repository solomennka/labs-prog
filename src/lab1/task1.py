import time
from typing import Callable, Any


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
        @return: Any - name, arguments, time, result function
        """
        print(f"Name function: {func.__name__}")
        print(f"Arguments function: {args}, {kwargs}")
        # Time counting
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_fun = end_time - start_time
        print(f"Time: {time_fun: .4f} секунд")
        print("Result:", result)
        return result
    return wrapper


@logger
def suma(a, b):
    return a + b


suma(4, 5)
