from __future__ import annotations

from dataclasses import dataclass
from http.client import HTTPResponse
from typing import Optional

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension
from tcgdexsdk.enums import Quality
from tcgdexsdk.internal import Model
from tcgdexsdk.models.subs import CardAbility
from tcgdexsdk.models.subs import CardAttack
from tcgdexsdk.models.subs import CardItem
from tcgdexsdk.models.subs import CardVariants
from tcgdexsdk.models.subs import CardWeakRes
from tcgdexsdk.models.subs import Legal
from tcgdexsdk.models.subs import SetCardCount
from tcgdexsdk.models.subs import SetCardCountResume


@dataclass
class Card(Model):
    """Pokémon TCG Card, It contains every informations about a specific card"""
    id: str
    """Globally unique card ID based on the set ID and the cards ID within the set"""
    localId: str
    """ID indexing this card within its set, usually just its number"""
    name: str
    """Card name"""
    image: Optional[str]
    """Card image url without the extension and quality"""
    illustrator: Optional[str]
    """Card illustrator"""
    rarity: str
    """Card rarity"""
    category: str
    """Card category"""
    variants: CardVariants
    """The card possible variants"""
    set: SetResume
    """Resume of the set the card belongs to"""
    dexIDs: Optional[list[int]]
    """the Pokémon Pokédex IDs (multiple if multiple pokémon appears on the card)"""
    hp: Optional[int]
    """HP of the pokemon"""
    types: Optional[list[str]]
    """Types of the pokemon (multiple because some have multiple in the older sets)"""
    evolvesFrom: Optional[str]
    """Name of the pokemon this one evolves from"""
    description: Optional[str]
    """the Pokémon Pokédex like description"""
    level: Optional[str]
    """the Pokémon Level (can be "X" if the card is of level X)"""
    stage: Optional[str]
    """the Pokémon Stage (changes depending on the API language)"""
    suffix: Optional[str]
    """the Pokémon Suffix (changes depending on the API language)"""
    item: Optional[CardItem]
    """the Item the Pokémon have"""
    abilities: Optional[list[CardAbility]]
    """the Card abilities (some cards have multiple abilities)"""
    attacks: Optional[list[CardAttack]]
    """the Card Attacks"""
    weaknesses: Optional[list[CardWeakRes]]
    """the Pokémon Weaknesses"""
    resistances: Optional[list[CardWeakRes]]
    """the Pokémon Resistances"""
    retreat: Optional[int]
    """the Pokémon retreat Cost"""
    effect: Optional[str]
    """effect the Card Effect (Trainer/Energy only)"""
    trainerType: Optional[str]
    """the trainer sub type (changes depending on the API language)"""
    energyType: Optional[str]
    """the energy sub type (changes depending on the API language)"""
    regulationMark: Optional[str]
    """the Card Regulation mark"""
    legal: Legal
    """the card ability to be played in tournaments"""

    def get_image_url(self, quality: str | Quality, extension: str | Extension) -> str:
        """
        the Card Image full URL
        @param quality: the quality you want your image to be in
        @param extension: extension you want you image to be
        @return: the full card URL with the extension and quality
        """
        return f"{self.image}/{quality}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_image(self, quality: str | Quality, format: str | Extension) -> HTTPResponse:
        """
        Get image buffer
        @param quality: the quality you want your image to be in
        @param format: extension you want you image to be
        @return: the full card Buffer in the format you want
        """
        return utils.download_image(self.get_image_url(quality, format))


@dataclass
class CardResume(Model):
    """Card Resume class, contains basic informations about a specific card

    to get the full card you can use the `get_full_card()` function"""
    id: str
    """Globally unique card ID based on the set ID and the cards ID within the set"""
    localId: str
    """ID indexing this card within its set, usually just its number"""
    name: str
    """Card name"""
    image: Optional[str]
    """Card image url without the extension and quality"""

    def get_image_url(self, quality: str | Quality, extension: str | Extension) -> str:
        """
        the Card Image full URL
        @param quality: the quality you want your image to be in
        @param extension: extension you want you image to be
        @return: the full card URL with the extension and quality
        """
        return f"{self.image}/{quality}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_image(self, quality: str | Quality, format: str | Extension) -> HTTPResponse:
        """
        Get image buffer
        @param quality: the quality you want your image to be in
        @param format: extension you want you image to be
        @return: the full card Buffer in the format you want
        """
        return utils.download_image(self.get_image_url(quality, format))

    def get_full_card(self) -> Optional[Card]:
        """
        Get the full Card
        @return: the full card if available
        """
        return self.tcgdex.fetch_card(self.id)


@dataclass
class Serie(Model):
    """Pokémon TCG Serie"""
    sets: list[SetResume]
    """the list of sets the Serie contains"""
    id: str
    """the Serie unique ID"""
    name: str
    """the Serie name"""
    logo: Optional[str]
    """the Serie Logo (basically also the first set logo)"""

    def get_logo_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_logo(self, format: str | Extension) -> HTTPResponse:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if logo := self.get_logo_url(format):
            return utils.download_image(logo)


@dataclass
class SerieResume(Model):
    """Serie Resume"""
    id: str
    """the Serie unique ID"""
    name: str
    """the Serie name"""
    logo: Optional[str]
    """the Serie Logo (basically also the first set logo)"""

    def get_logo_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_logo(self, format: str | Extension) -> HTTPResponse:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if logo := self.get_logo_url(format):
            return utils.download_image(logo)

    def get_full_series(self) -> Optional[Serie]:
        """
        Get the full Serie
        @return: the full serie if available
        """
        return self.tcgdex.fetch_serie(self.id)


@dataclass
class Set(Model):
    """Pokémon TCG Set class"""
    id: str
    """Globally unique set ID"""
    name: str
    """the Set mame"""
    logo: Optional[str]
    """the Set Logo incomplete URL (use get_logo_url/get_logo)"""
    symbol: Optional[str]
    """the Set Symbol imcomplete URL (use get_symbol_url/get_symbol)"""
    serie: SerieResume
    """the serie this set is a part of"""
    tcgOnline: Optional[str]
    """the TCG Online Code"""
    releaseDate: str
    """the Set release date as yyyy-mm-dd"""
    legal: Legal
    """the set legality (won't indicate if a card is banned)"""
    cardCount: SetCardCount
    """the number of card in the set"""
    cards: list[CardResume]
    """the cards contained in this set"""

    def get_logo_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_logo(self, format: str | Extension) -> HTTPResponse:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if logo := self.get_logo_url(format):
            return utils.download_image(logo)

    def get_symbol_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the symbol full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.symbol:
            return f"{self.symbol}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_symbol(self, format: str | Extension) -> HTTPResponse:
        """
        Get the symbol buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if symbol := self.get_symbol_url(format):
            return utils.download_image(symbol)


@dataclass
class SetResume(Model):
    """Set resume"""
    id: str
    """Globally unique set ID"""
    name: str
    """the Set mame"""
    logo: Optional[str]
    """the Set Logo incomplete URL (use get_logo_url/get_logo)"""
    symbol: Optional[str]
    """the Set Symbol imcomplete URL (use get_symbol_url/get_symbol)"""
    cardCount: SetCardCountResume
    """the number of card in the set"""

    def get_logo_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_logo(self, format: str | Extension) -> HTTPResponse:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if logo := self.get_logo_url(format):
            return utils.download_image(logo)

    def get_symbol_url(self, extension: str | Extension) -> Optional[str]:
        """
        Get the symbol full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.symbol:
            return f"{self.symbol}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_symbol(self, format: str | Extension) -> HTTPResponse:
        """
        Get the symbol buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if symbol := self.get_symbol_url(format):
            return utils.download_image(symbol)

    def get_full_set(self) -> Optional[Set]:
        """
        Get the full set
        @return: the full set if available
        """
        return self.tcgdex.fetch_set(self.id)


@dataclass
class StringEndpoint(Model):
    """Generix class that handle a lot of Endpoints"""
    name: str
    """the endpoint value"""
    cards: list[CardResume]
    """the cards that contain `name` in them"""
