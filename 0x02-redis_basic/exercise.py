#!/usr/bin/env python3
"""Redis"""
from typing import Union
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
