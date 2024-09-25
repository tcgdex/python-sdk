from typing import Union

from tcgdexsdk.endpoints.Endpoint import Endpoint
from tcgdexsdk.enums import Language
from tcgdexsdk.models.CardResume import CardResume
from tcgdexsdk.models.Card import Card
from tcgdexsdk.models.Serie import Serie
from tcgdexsdk.models.SerieResume import SerieResume
from tcgdexsdk.models.Set import Set
from tcgdexsdk.models.SetResume import SetResume
from tcgdexsdk.models.StringEndpoint import StringEndpoint

class TCGdex:
    """The main TCGdex SDK instance"""

    URI = "https://api.tcgdex.net/v2"
    """The API Endpoint you want to use"""

    def __init__(self, language: Union[str, Language]):
        """
        Create the TCGdex Instance in the specific language
        @param language: the language you want to use, values: [en,fr,es,de,pt,it]
        """
        self.language = language
        self.card = Endpoint(self, Card, CardResume, "cards")
        self.set = Endpoint(self, Set, SetResume, "sets")
        self.serie = Endpoint(self, Serie, SerieResume, "series")

        self.variant = Endpoint(self, StringEndpoint, str, 'variants')
        self.trainerType = Endpoint(self, StringEndpoint, str, 'trainer-types')
        self.suffix = Endpoint(self, StringEndpoint, str, 'suffixes')
        self.stage = Endpoint(self, StringEndpoint, str, 'stages')
        self.regulationMark = Endpoint(self, StringEndpoint, str, 'regulation-marks')
        self.energyType = Endpoint(self, StringEndpoint, str, 'energy-types')
        self.dexId = Endpoint(self, StringEndpoint, int, 'dex-ids')
        self.type = Endpoint(self, StringEndpoint, str, 'types')
        self.retreat = Endpoint(self, StringEndpoint, int, 'retreats')
        self.rarity = Endpoint(self, StringEndpoint, str, 'rarities')
        self.illustrator = Endpoint(self, StringEndpoint, str, 'illustrators')
        self.hp = Endpoint(self, StringEndpoint, int, 'hp')
        self.category = Endpoint(self, StringEndpoint, str, 'categories')
