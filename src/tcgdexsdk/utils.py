import json
import time
import warnings
from functools import lru_cache, wraps
from http.client import HTTPResponse
from typing import List, Optional, Type, TypeVar
from urllib.request import Request, urlopen

from dacite import from_dict

from tcgdexsdk import __version__
from tcgdexsdk.models.Model import Model

_T = TypeVar("_T")
_TM = TypeVar("_TM", bound=Model)

ttl = 60


def _request(url: str) -> Request:
    return Request(
        url,
        headers={"User-Agent": f"@tcgdex/python-sdk@{__version__}"},
    )


@lru_cache
def _urlopen(url: str, _: float) -> str:
    return urlopen(_request(url)).read().decode()


def _from_dict(cls: Type[_TM], data: dict, tcgdex) -> _TM:
    self = from_dict(cls, data)
    self.sdk = tcgdex

    for _, attr_value in self.__dict__.items():
        if isinstance(attr_value, list):
            for item in attr_value:
                if hasattr(item, "sdk"):
                    item.sdk = tcgdex
        elif hasattr(attr_value, "sdk"):
            attr_value.sdk = tcgdex

    return self


def fetch(tcgdex, url: str, cls: Type[_T]) -> Optional[_T]:
    if not issubclass(cls, Model):
        return None
    data = json.loads(_urlopen(url, time.monotonic() // (ttl * 60)))
    return _from_dict(cls, data, tcgdex)


def fetch_list(tcgdex, url: str, cls: Type[_T]) -> List[_T]:
    data = json.loads(_urlopen(url, time.monotonic() // (ttl * 60)))
    res = []
    if cls is None or not issubclass(cls, Model):
        return data
    for item in data:
        res.append(_from_dict(cls, item, tcgdex))
    return res


def download_image(url: str) -> HTTPResponse:
    return urlopen(_request(url))


def deprecated(reason):
    def decorator(func):
        message = f"{func.__name__} is deprecated: {reason}"

        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator
