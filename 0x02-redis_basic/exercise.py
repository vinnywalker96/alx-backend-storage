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

    def get(self, key: str, fn: Callable = None):
        val = self._redis.get(key)
        if val is not None:
            val = val.decode("utf-8")
            if fn:
                return fn(val)
            return val
        return None

    def get_str(self, key: str):
        return self.get(key, str)

    def get_int(self, key: int):
        return self.get(key, int)
