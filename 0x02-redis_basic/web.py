#!/usr/bin/env python3
"""
web cache and tracker
"""

import requests
import redis
from functools import wraps

alx = redis.Redis()


def url_access_count(method):
    """Keep track of the number of times a url is accessed"""
    @wrap(method)
    def wrapper(url):
        key_cache = "cached:" + url
        if key_cache:
            return key_cache.decode("utf-8")

        # Get new content, update cache
        count_k = "count:" + url
        html_cont = method(url)

        alx.incr(count_k)
        alx.set(key_cache, html_cont, ex=10)
        alx.expire(key_cache, 10)
        return html_cont
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Get the HTML content of a particular page"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
