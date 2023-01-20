#!/usr/bin/env python3
""" This module writes strings to redis
"""
from typing import Callable, Optional, Union
import redis
import sys
import uuid
from functools import wraps


class Cache:
    """ class cache """
    def __init__(self) -> None:
        """ class Cache init method """
        self._redis = redis.Redis()
        self._redis.flushdb()
    

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores the input data in Redis using the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get method """
        value = self._redis.get(key)

        if value is not None:
            if fn:
                value = fn(value)
            return value
        else:
            return None

    def get_str(self, val: bytes) -> str:
        """
        automatically parametrize Cache.get
        returns a string
        """
        return str(val, val.decode('utf-8'))

    def get_int(self, val: bytes) -> int:
        """
        automatically parametrize Cache.get
        returns an int
        """
        val = int(val, val.decode('utf-8'))

        return val if val else 0
