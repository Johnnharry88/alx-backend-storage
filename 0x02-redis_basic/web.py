#!/usr/bin/env python3
"""A File that track and cahes web pages
"""

import requests
import redis
from functools import wraps
from typing import Callable

alx = redis.Redis()


def url_access_count(method: Callable) -> Callable:
    """Keep track of the number of times a url is accessed"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Checks out for wrapped function"""
        x = "cached:" + url
        y = "count:" + url
        alx.incr(y)
        cache_p = alx.get(x)
        if cache_p:
            return cache_p.decode("utf-8")
        response = method(url)
        alx.set(x, response, ex=10)
        alx.expire(x, 10)
        return response
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Get the HTML content of a particular page"""
    res = requests.get(url)
    return res.text
