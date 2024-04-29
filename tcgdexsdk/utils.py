import json
import time
import typing
import urllib.parse
from functools import lru_cache
from http.client import HTTPResponse
from typing import Optional
from typing import TypeVar
from urllib.request import Request

from dacite import from_dict

from tcgdexsdk.internal import Model

_T = TypeVar("_T")
_TM = TypeVar("_TM", bound=Model)

ttl = 60


def _request(url: str) -> Request:
    return Request(url, headers={"User-Agent": f"@HellLord77/python-sdk"})


@lru_cache
def _urlopen(url: str, _: float) -> str:
    return urllib.request.urlopen(_request(url)).read().decode()


def _from_dict(cls: type[_TM], data: dict, tcgdex) -> _TM:
    self = from_dict(cls, data)
    self.tcgdex = tcgdex
    return self


def fetch(tcgdex, url: str, cls: type[_T]) -> Optional[_T]:
    self = json.loads(_urlopen(url, time.monotonic() // (ttl * 60)))
    if is_not_list := typing.get_origin(cls) is None:
        self = (self,)
    else:
        cls = typing.get_args(cls)[0]
    if issubclass(cls, Model):
        self = (_from_dict(cls, item, tcgdex) for item in self)
    return (next if is_not_list else list)(self)


def download_image(url: str) -> HTTPResponse:
    return urllib.request.urlopen(_request(url))
