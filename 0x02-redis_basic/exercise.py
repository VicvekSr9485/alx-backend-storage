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
        self._redis.flushdb
    

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores the input data in Redis using the random key and return the key
        """
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)
