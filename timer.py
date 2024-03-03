import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        print(f'Ended at {time.time() - start_time}')
        return r
    return wrapper
