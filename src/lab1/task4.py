from typing import Any, Callable, Type


def call_limiter(limit: int) -> Callable:
    """
    Decorator that sets the limits the number of class method calls.
    @param limit: int - function call limit
    @return: Callable - same class with additional expressions
    """
    def decorator(cls: Type) -> Type:
        """
        Decorator that individually sets the limits the number of class method calls.
        @param cls: Type - original class
        @return: Type - same class with additional expressions
        """
        # Dictionary with class methods and the number of times they are called
        call = {}
        # Iterating through all the methods of the class
        for name, method in cls.__dict__.items():
            if callable(method):
                def make_wrapper(method_name: str, original_method: Any) -> Callable:
                    """
                    Function that creates a wrapper function for a class method
                    @param method_name: str - name jf class method
                    @param original_method: Any - original class method
                    @return: Callable - wrapper function
                    """
                    def wrapper(self: Any, *args: tuple[Any, ...], **kwargs:  dict[str, Any]) -> Any:
                        """
                        Wrapper function for a class method
                        @param self: Any
                        @param args: tuple[Any, ...] - positional arguments from function
                        @param kwargs: dict[str, Any] - keyword arguments from function
                        @return: Any - error or original method
                        """
                        instance_id = id(self)
                        if instance_id not in call:
                            call[instance_id] = {}

                        if method_name not in call[instance_id]:
                            call[instance_id][method_name] = 0
                        # Check limit
                        if call[instance_id][method_name] >= limit:
                            raise RuntimeError("The function call limit has been reached!")
                        call[instance_id][method_name] += 1
                        return original_method(self, *args, **kwargs)
                    return wrapper
                setattr(cls, name, make_wrapper(name, method))
        return cls
    return decorator


@call_limiter(limit=2)
class Printer:
    def hello(self):
        print("Hello!")


p = Printer()
p.hello()
p.hello()
try:
    p.hello()
except Exception as e:
    print(e)
