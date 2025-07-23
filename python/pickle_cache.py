import functools
import pickle
from pathlib import Path
from typing import Any, Callable

"""
example usage:
@pickle_cache 
def test(a, b):
    return a + b
"""


def pickle_cache(func: Callable[..., Any]):
    """
    Locally cache a long running function using a pickle file
    """

    def decorator(func) -> Callable[..., Any]:
        cache_file = Path(f"{func.__name__}_cache.pkl")

        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            if cache_file.exists():
                try:
                    with cache_file.open("rb") as f:
                        print("PICKLE: file found")
                        cache = pickle.load(f)
                except Exception:
                    cache = {}
            else:
                cache = {}

            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                print("PICKLE: cache hit")
                return cache[key]

            print("PICKLE: cache miss, running function")
            result = func(*args, **kwargs)
            cache[key] = result
            cache_file.parent.mkdir(parents=True, exist_ok=True)
            with cache_file.open("wb") as f:
                pickle.dump(cache, f)
            return result

        return wrapper_func

    return decorator(func)
