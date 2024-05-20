from typing import Optional
from typing import overload

from tcgdexsdk.enums import Extension
from tcgdexsdk.enums import Language
from tcgdexsdk.enums import Quality
from tcgdexsdk.models import Card
from tcgdexsdk.models import CardResume
from tcgdexsdk.models import Serie
from tcgdexsdk.models import SerieResume
from tcgdexsdk.models import Set
from tcgdexsdk.models import SetResume
from tcgdexsdk.models import StringEndpoint
from tcgdexsdk.utils import _T


class TCGdex:
    """The main TCGdex SDK instance"""

    URI = "https://api.tcgdex.net/v2"
    """The API Endpoint you want to use"""

    def __init__(self, language: str | Language):
        """
        Create the TCGdex Instance in the specific language
        @param language: the language you want to use, values: [en,fr,es,de,pt,it]
        """
        self.language = language

    def fetch_cards(self) -> Optional[list[CardResume]]:
        """
        Fetch every Pokémon cards
        _note: take some time as there is around 13k-15k cards depending on the language_
        @return: the list of Pokémon Cards
        """
        return self.fetch(list[CardResume], "cards")

    @overload
    def fetch_card(self, card: str) -> Optional[Card]:
        """
        Fetch a specific card
        @param card: the card ID
        @return: The card
        """

    # noinspection PyShadowingBuiltins
    @overload
    def fetch_card(self, set: str, card: str) -> Optional[Card]:
        """
        Fetch a specific card by its set and local IDs
        @param set: the set ID/name
        @param card: the card local ID
        @return: the card you want
        """

    # noinspection PyShadowingBuiltins
    def fetch_card(self, set, card=None):
        if card is None:
            paths = "cards", set
        else:
            paths = "sets", set, card
        return self.fetch(Card, *paths)

    def fetch_sets(self) -> Optional[list[SetResume]]:
        """
        Fetch every pokémon TCG Sets
        @return: the list of Pokémon TCG sets
        """
        return self.fetch(list[SetResume], "sets")

    # noinspection PyShadowingBuiltins
    def fetch_set(self, set: str) -> Optional[Set]:
        """
        Fetch a specific set
        @param set: the set you want to fetch (you can use the Set ID or name)
        @return: The set you searched
        """
        return self.fetch(Set, "sets", set)

    def fetch_series(self) -> Optional[list[SerieResume]]:
        """
        Fetch every pokémon TCG Series
        @return: the list of Pokémon TCG Series
        """
        return self.fetch(list[SerieResume], "series")

    def fetch_serie(self, serie: str) -> Optional[Serie]:
        """
        Fetch a specific serie
        @param serie: the serie you want to fetch (you can use the Serie ID or name)
        @return: The serie you searched
        """
        return self.fetch(Serie, "series", serie)

    def fetch_variants(self) -> Optional[list[str]]:
        """
        Fetch evey variants it is possible to have
        @return: the list of evey variants it is possible to have
        """
        return self.fetch(list[str], "variants")

    def fetch_variant(self, variant: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by variant
        @param variant: the variant you want to filter by
        @return: a StringEndpoint containing the cards with the specified variant
        """
        return self.fetch(StringEndpoint, "variants", variant)

    def fetch_trainer_types(self) -> Optional[list[str]]:
        """
        Fetch evey Trainer Types it is possible to have
        @return: the list of evey Trainer Types it is possible to have
        """
        return self.fetch(list[str], "trainer-types")

    # noinspection PyShadowingBuiltins
    def fetch_trainer_type(self, type: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by trainer type
        @param type: the trainer type you want to filter by
        @return: a StringEndpoint containing the cards with the specified trainer type
        """
        return self.fetch(StringEndpoint, "trainer-types", type)

    def fetch_suffixes(self) -> Optional[list[str]]:
        """
        Fetch evey suffixes it is possible to have
        @return: the list of evey suffixes it is possible to have
        """
        return self.fetch(list[str], "suffixes")

    def fetch_suffix(self, suffix: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by suffix
        @param suffix: the suffix you want to filter by
        @return: a StringEndpoint containing the cards with the specified suffix
        """
        return self.fetch(StringEndpoint, "suffixes", suffix)

    def fetch_stages(self) -> Optional[list[str]]:
        """
        Fetch evey stages it is possible to have
        @return: the list of evey stages it is possible to have
        """
        return self.fetch(list[str], "stages")

    def fetch_stage(self, stage: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by stage
        @param stage: the stage you want to filter by
        @return: a StringEndpoint containing the cards with the specified stage
        """
        return self.fetch(StringEndpoint, "stages", stage)

    def fetch_regulation_marks(self) -> Optional[list[str]]:
        """
        Fetch evey regulation marks it is possible to have
        @return: the list of evey regulation marks it is possible to have
        """
        return self.fetch(list[str], "regulation-marks")

    def fetch_regulation_mark(self, regulation_mark: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by regulation mark
        @param regulation_mark: the regulation mark you want to filter by
        @return: a StringEndpoint containing the cards with the specified regulation mark
        """
        return self.fetch(StringEndpoint, "regulation-marks", regulation_mark)

    def fetch_energy_types(self) -> Optional[list[str]]:
        """
        Fetch evey Energy Types it is possible to have
        @return: the list of evey Energy Types it is possible to have
        """
        return self.fetch(list[str], "energy-types")

    def fetch_energy_type(self, energy_type: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by energy type
        @param energy_type: the energy type you want to filter by
        @return: a StringEndpoint containing the cards with the specified energy type
        """
        return self.fetch(StringEndpoint, "energy-types", energy_type)

    def fetch_dex_ids(self) -> Optional[list[str]]:
        """
        Fetch evey Pokédex IDS it is possible to have
        @return: the list of evey Pokédex IDS it is possible to have
        """
        return self.fetch(list[str], "dex-ids")

    def fetch_dex_id(self, dex_id: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by Pokédex ID
        @param dex_id: the Pokédex ID you want to filter by
        @return: a StringEndpoint containing the cards with the specified Pokédex ID
        """
        return self.fetch(StringEndpoint, "dex-ids", dex_id)

    def fetch_types(self) -> Optional[list[str]]:
        """
        Fetch evey types it is possible to have
        @return: the list of evey types it is possible to have
        """
        return self.fetch(list[str], "types")

    # noinspection PyShadowingBuiltins
    def fetch_type(self, type: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by type
        @param type: the type you want to filter by
        @return: a StringEndpoint containing the cards with the specified type
        """
        return self.fetch(StringEndpoint, "types", type)

    def fetch_categories(self) -> Optional[list[str]]:
        """
        Fetch evey categories it is possible to have
        @return: the list of evey categories it is possible to have
        """
        return self.fetch(list[str], "categories")

    def fetch_category(self, category: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by category
        @param category: the category you want to filter by
        @return: a StringEndpoint containing the cards with the specified category
        """
        return self.fetch(StringEndpoint, "categories", category)

    def fetch_retreats(self) -> Optional[list[str]]:
        """
        Fetch evey retreat count it is possible to have
        @return: the list of evey retreat count it is possible to have
        """
        return self.fetch(list[str], "retreats")

    def fetch_retreat(self, retreat: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by retreat
        @param retreat: the retreat you want to filter by
        @return: a StringEndpoint containing the cards with the specified retreat count
        """
        return self.fetch(StringEndpoint, "retreats", retreat)

    def fetch_rarities(self) -> Optional[list[str]]:
        """
        Fetch every Card rarities you can have (in your language)
        @return: the list of Card rarities you can have (in your language)
        """
        return self.fetch(list[str], "rarities")

    def fetch_rarity(self, rarity: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by rarity
        @param rarity: the rarity you want to filter by (language specific)
        @return: a StringEndpoint containing the cards with the specified rarity
        """
        return self.fetch(StringEndpoint, "rarities", rarity)

    def fetch_illustrators(self) -> Optional[list[str]]:
        """
        Fetch every cards illustrators
        @return: the list of illustrators
        """
        return self.fetch(list[str], "illustrators")

    def fetch_illustrator(self, illustrator: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by illustrator
        @param illustrator: the illustrator you want to filter by
        @return: a StringEndpoint containing the cards with the specified illustrator
        """
        return self.fetch(StringEndpoint, "illustrators", illustrator)

    def fetch_hps(self) -> Optional[list[str]]:
        """
        Fetch the list of possible value the HP field can take
        @return: the list of possible value the HP field can take
        """
        return self.fetch(list[str], "hp")

    def fetch_hp(self, hp: str) -> Optional[StringEndpoint]:
        """
        Fetch cards by hp
        @param hp: the hp count you want to filter by
        @return: a StringEndpoint containing the cards with the specified hp count
        """
        return self.fetch(StringEndpoint, "hp", hp)

    def fetch(self, cls: type[_T], *paths: str) -> Optional[_T]:
        return utils.fetch(
            self,
            f"{self.URI}/{self.language}/{'/'.join(paths)}".replace(" ", "%20"),
            cls,
        )
