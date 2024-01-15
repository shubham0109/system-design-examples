import feedparser
import requests
import ssl
import time

from functools import lru_cache, wraps
from datetime import datetime, timedelta



def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = datetime(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() > func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            return func(*args, **kwargs)

    return wrapper

@timed_lru_cache(10)
def get_article_from_url(url: str):
    print("Fetching article from server..")
    response = requests.get(url)
    return response.text
