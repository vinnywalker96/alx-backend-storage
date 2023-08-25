#!/usr/bin/env python3
"""Redis"""
from typing import Union, Callable
import redis
import uuid


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

    def get(self, key, fn=None):
        value = self._redis.get(key)
        if value is None:
            return None
        if str(value) is not str:
            return self.get_str(value)
        else:
            return self.get_str(value)

    def get_str(self, value):
        return str(value)

    def get_int(self, value):
        return int(value)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
