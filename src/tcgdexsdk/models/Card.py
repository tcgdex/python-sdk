from dataclasses import dataclass
from http.client import HTTPResponse
from typing import List, Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension, Quality
from tcgdexsdk.models.Model import Model
from tcgdexsdk.models.SetResume import SetResume
from tcgdexsdk.models.subs import (
    Booster,
    CardAbility,
    CardAttack,
    CardItem,
    CardVariants,
    CardWeakRes,
    Legal,
)


@dataclass
class Card(Model):
    """Pokémon TCG Card, It contains every information about a specific card"""

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
    dexIDs: Optional[List[int]]
    """the Pokémon Pokédex IDs (multiple if multiple pokémon appears on the card)"""
    hp: Optional[int]
    """HP of the pokemon"""
    types: Optional[List[str]]
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
    abilities: Optional[List[CardAbility]]
    """the Card abilities (some cards have multiple abilities)"""
    attacks: Optional[List[CardAttack]]
    """the Card Attacks"""
    weaknesses: Optional[List[CardWeakRes]]
    """the Pokémon Weaknesses"""
    resistances: Optional[List[CardWeakRes]]
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
    id: str
    """Globally unique card ID based on the set ID and the cards ID within the set"""
    localId: str
    """ID indexing this card within its set, usually just its number"""
    name: str
    """Card name"""
    image: Optional[str]
    """Card image url without the extension and quality"""
    boosters: Optional[List[Booster]]
    """
    The list of boosters the card is in.
    
    if it is `null`, it is available in every boosters.
    
    if an `empty array`, it is available in no boosters (additionnal content or other way of obtaining it)
    """

    def get_image_url(
        self, quality: Union[str, Quality], extension: Union[str, Extension]
    ) -> Optional[str]:
        """
        the Card Image full URL
        @param quality: the quality you want your image to be in
        @param extension: extension you want you image to be
        @return: the full card URL with the extension and quality
        """
        if self.image:
            return f"{self.image}/{quality}.{extension}"

    def get_image(
        self, quality: Union[str, Quality], format: Union[str, Extension]
    ) -> Optional[HTTPResponse]:
        """
        Get image buffer
        @param quality: the quality you want your image to be in
        @param format: extension you want you image to be
        @return: the full card Buffer in the format you want
        """
        if url := self.get_image_url(quality, format):
            return utils.download_image(url)
