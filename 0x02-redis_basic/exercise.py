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
    
    def get_str(self, key: str) -> str:
        """Convert byte to str"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Convert byte str to int"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception as err:
            vale = 0
        return val
