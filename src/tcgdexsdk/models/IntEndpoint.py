from dataclasses import dataclass
from typing import List

from tcgdexsdk.models.CardResume import CardResume
from tcgdexsdk.models.Model import Model


@dataclass
class IntEndpoint(Model):
    """Generic class that handle a lot of Endpoints"""

    name: int
    """the endpoint value"""
    cards: List[CardResume]
    """the cards that contain `name` in them"""
