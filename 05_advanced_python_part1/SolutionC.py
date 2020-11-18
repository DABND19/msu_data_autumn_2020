import signal
import functools
from time import sleep


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler(s, f):
    raise TimeoutException('Timed out')


def timeout(seconds):
    def decorator(func):
        if seconds is None or seconds <= 0:
            return func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            default = signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            result = func(*args, **kwargs)
            signal.signal(signal.SIGALRM, default)
            signal.setitimer(signal.ITIMER_REAL, 0)
            return result
        return wrapper
    return decorator


@timeout(None)
def func():
    sleep(0.6)


try:
    func()
except TimeoutException as e:
    print(e)
