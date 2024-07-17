#!/usr/bin/env python3
"""A File that track and cahes web pages
"""

import requests
import redis
from functools import wraps
from typing import Callable


def url_access_count(method: Callable) -> Callable:
    """Keep track of the number of times a url is accessed"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Checks out for wrapped function"""
        alx = redis.Redis()        
        alx.incr(f'count:{url}')
        cache_p = alx.get(f'cached:{url}')
        if cache_p:
            return cache_p.decode("utf-8")
        response = method(url)
        alx.set(f'cached{url}', response, 10)
        return response
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Get the HTML content of a particular page"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
