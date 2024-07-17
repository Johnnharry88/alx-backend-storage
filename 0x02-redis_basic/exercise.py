#!/usr/bin/env python3
"""Modules holding Redis attribtues"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the number of times the method of Cace class is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *x, **y):
        """ Wrapper for decorated funtion"""
        self._redis.incr(key)
        return method(self, *x, **y)
    return wrapper


def call_history(method: Callable) -> Callable:
    """stores input and output history"""
    @wraps(method)
    def wrapper(self, *x, **y):
        """Wrapper for decorated fnction"""
        input = str(x)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *x, **y))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """Display call history of a particular function"""
    red = redis.Redis()
    f_name = fn.__qualname__
    v = red.get(f_name)
    try:
        v = int(v.decode("utf-8"))
    except Exception:
        v = 0
    #prints out funcion_name{f_name{} and no of times called {value}
    print("{} was called {} times:".format(f_name, v))
    
    inputs = r.lrange("{}:inputs".format(f_name), 0, -1)

    outputs = r.lrange("{}:outputs".format(f_name), 0, -1)

    for i, o in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        # prints out function name {f_name} with corresponding input and output
        print(f"{f_name}(*{input}) -> {output}")


class Cache:
    """Create a Cache class"""
    
    def __init__(self):
        """Stores instance of the Redis Client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """generate random key"""
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, int, bytes, float]:
        """Changes data back to desired format"""
        vlue = self._redis.get(key)
        if fn:
            vlue = fn(vlue)
        return vlue

    def get_str(self, key: str) -> str:
        """Parmetrize Cace.get with correct convert function"""
        value = self._redis.get(key)
        return value.dcode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametrize Cache.get with some convert function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value - 0
        return value
