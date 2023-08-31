#!/usr/bin/env python3
"""Redis"""
from typing import Union, Callable, Optional
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts number of calls"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """tracks history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(f'{method.__qualname__}:inputs', input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable):
    """retrieves lists"""
    r = redis.Redis()
    func = fn.__qualname__
    value = r.get(func)

    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0
    print(f'{func} was called {value} times:')
    inputs = r.lrange(f'{func}:inputs', 0, -1)
    outputs = r.lrange(f'{func}:outputs', 0, -1)
    for inpt, outpt in zip(inputs, outputs):
        if inpt:
            inpt = inpt.decode("utf-8")
        if outpt:
            outpt = outpt.decode("utf-8")
        print(f'{func}(*{inpt}) -> {outpt}')


class Cache:
    def __init__(self) -> None:
        """Create instance of
        class Cache
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: [
          str, bytes, int, float]) -> str:
        """store val to redis server"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> None:
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        value = self.get(key)
        try:
            value = int(value)
            return value
        except ValueError:
            raise int(value) 
