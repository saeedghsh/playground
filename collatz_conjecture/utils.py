"""Some utils"""

import sys
from functools import wraps

import psutil


def memory_guard_decorator(threshold: int):
    """A decorator to detect over-usage of a function to prevent crash.
    threshold is in MB."""

    def memory_usage_mb(process: psutil.Process) -> int:
        """Return memory usage in MB"""
        memory_info = process.memory_info()
        return memory_info.rss // 1024**2

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            process = psutil.Process()
            result = func(*args, **kwargs)
            memory_usage = memory_usage_mb(process)
            if memory_usage > threshold:
                print(f"Memory usage exceeded {threshold} MB. Exiting to prevent crash.")
                sys.exit(1)

            return result

        return wrapper

    return decorator
