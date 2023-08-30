#!/usr/bin/env python3
"""Redis"""
from typing import Union, Callable
import redis
import uuid
from functools import wraps


def call_counts(self, fn: Callable = None) -> Callable:

    @wraps(fn)
    def wrapper(self , *args, **kwargs):
        key = f"method_calls:{fn.__qualname__}"
        self._redis.incr(key)
        return fn(*args, **kwargs)
    return wrapper

class Cache:
    def __init__(self) -> None:
        """Create instance of
        class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[
          str, bytes, int, float]) -> str:
        """store val to redis server"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[bytes, str, int, float, None]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return None
        return fn(value)

    def get_str(self, key: str) -> str:
        return self._redis.get(key).decode("utf-8)


    def get_int(self, key: str) -> int:
        return int(self._redis.get(key, fn=int))

