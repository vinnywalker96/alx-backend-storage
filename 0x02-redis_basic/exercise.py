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
        if fn is not None:
            return fn(value)
        try:
            result = get_str(value)
            return result
        except ValueError:
            result = get_int(value)
            return result

    def get_str(self, value: bytes) -> str:
        return str(value)

    def get_int(self, value: bytes) -> int:
        return int(value)
