import time
from typing import Callable, Optional, Tuple, Type, Any


def retry(attempts: int, delay: float, exceptions: Optional[Tuple[Type[Exception], ...]] = None) -> Callable:
    """
    Function with parameters for the decorator
    @param attempts: int - number of repetitions of the function
    @param delay: float - the gap between calls
    @param exceptions: Optional[Tuple[Type[Exception] - tuple with functions, None default
    @return: Callable - decorator
    """
    def decorator(func: Callable) -> Callable:
        """
        Decorator that calls a function attempts times.
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
            last_exception = None
            # Сalling the function attempts times
            for attempt in range(attempts):
                try:
                    result = func(*args, **kwargs)
                    print(result)
                    print("try:", attempt + 1)
                    return result

                # Сheck for errors and see if they are in the exceptions
                except Exception as e:
                    print("try:", attempt + 1)
                    print(f"Error: {e}")
                    last_exception = e
                    if exceptions is not None and isinstance(e, exceptions):
                        if attempt != attempts - 1:
                            time.sleep(delay)
                    else:
                        # Ending the loop and displaying errors that are not in the exceptions
                        raise e
            # All attempts have been exhausted
            if last_exception:
                raise last_exception
        return wrapper
    return decorator


@retry(attempts=3, delay=1, exceptions=(ValueError, ZeroDivisionError))
def suma(a, b):
    print(a/b)


try:
    suma(8, 1)
except Exception as e:
    print(f"Error {e}")
