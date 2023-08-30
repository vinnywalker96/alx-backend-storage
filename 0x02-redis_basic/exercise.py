#!/usr/bin/env python3
"""Redis"""
from typing import Union, Callable
import redis
import uuid
from functools import wraps



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

    def get(self, key: str, fn: Callable = None) -> None:
        val = self._redis.get(key)
        if fn and val:
            return fn(val)
        return None

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return int(self.get(key, fn=int))
        
