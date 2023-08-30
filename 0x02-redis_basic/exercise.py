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

    def get_str(self, data: bytes) -> str:
        val = data.decode("utf-8")
        return val

    def get_int(self, data: bytes) -> int:
        return int(data)

    def get(self, key: str, fn: Callable = None) -> bytes:
        val = self._redis.get(key)
        if val is None:
            return None
        if fn is None:
            return None
        return fn(val)
        try:
            res = get_int(val)
            return res
        except ValueError:
            res = get_str(val)
            return res
