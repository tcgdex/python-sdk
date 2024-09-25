from dataclasses import dataclass
from http.client import HTTPResponse
from typing import List, Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension, Quality
from tcgdexsdk.models.Card import Card
from tcgdexsdk.models.CardResume import CardResume
from tcgdexsdk.models.Serie import Serie
from tcgdexsdk.models.Model import Model

@dataclass
class IntEndpoint(Model):
    """Generic class that handle a lot of Endpoints"""

    name: int
    """the endpoint value"""
    cards: List[CardResume]
    """the cards that contain `name` in them"""
