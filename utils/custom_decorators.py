import time
import functools


def separate_function(func):
    """Decorator prints proper characters to distinguish function when printing in a terminal window"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(50*'-')
        print(f"Calling {func.__name__}()")
        print(50*'-')
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        
        print(50*'-')
        print(f"Executed in: {end-start}s")
        print(50*'-')
    return wrapper