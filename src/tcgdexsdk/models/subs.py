from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class CardAbility:
    """Describes a single ability of a pokemon"""

    type: str
    """The Ability type (language dependant)"""
    name: Optional[str]
    """Name of the ability"""
    effect: Optional[str]
    """Description/Effect of the ability"""


@dataclass
class CardAttack:
    """Describes a single attack of a pokemon, for example 'Confuse Ray'"""

    name: Optional[str]
    """Name of the attack"""
    cost: Optional[List[str]]
    """Cost of the attack in the same order as listed on the card"""
    effect: Optional[str]
    """Effect/Description of the attack, may be null for attacks without text"""
    damage: Optional[Union[int, str]]
    """Damage the attack deals. May just be a number like '30', but can also be a multiplier like 'x20'"""


@dataclass
class CardItem:
    """Card Item"""

    name: Optional[str]
    """the Item name"""
    effect: Optional[str]
    """the item effect"""


@dataclass
class CardVariants:
    """Card variants"""

    normal: bool
    """basic variant no special effects"""
    reverse: bool
    """the card have some shine behind colored content"""
    holo: bool
    """the card picture have some shine to it"""
    firstEdition: bool
    """the card contains a First Edition Stamp (only Base serie)"""
    wPromo: bool
    """the card has a wPromo stamp on it"""


@dataclass
class CardWeakRes:
    """Describes the weakness/resistance of a single pokemon, for example: 2x to Fire"""

    type: str
    """the affecting type"""
    value: Optional[str]
    """the multiplier mostly `x2` but can also be `-30`, `+30` depending on the card"""


@dataclass
class Legal:
    """
    Card Legality
    _note: cards are always usable in the unlimited tournaments_
    """

    standard: bool
    """card is usable in standard tournaments"""
    expanded: bool
    """card is usable in expanded tournaments"""


@dataclass
class SetCardCount:
    """Set card count"""

    total: int
    """total of number of cards"""
    official: int
    """number of cards officialy (on the bottom of each cards)"""
    normal: Optional[int]
    """number of cards having a normal version"""
    reverse: Optional[int]
    """number of cards having an reverse version"""
    holo: Optional[int]
    """number of cards having an holo version"""
    firstEd: Optional[int]
    """Number of possible cards"""


@dataclass
class Booster:
    id: str
    name: str
    logo: Optional[str]
    artwork_front: Optional[str]
    artwork_back: Optional[str]


@dataclass
class SetCardCountResume:
    """Set card count resume"""

    total: int
    """total of number of cards"""
    official: int
    """number of cards officialy (on the bottom of each cards)"""


@dataclass
class SetAbbreviations:
    """Set abbreviations"""

    official: Optional[str]
    """Official abbreviation acronym used on the cards (English version)"""
    fr: Optional[str]
    """French abbreviation acronym used on the cards"""
    es: Optional[str]
    """Spanish abbreviation acronym used on the cards"""
    es_mx: Optional[str]
    """Spanish (Mexico) abbreviation acronym used on the cards"""
    it: Optional[str]
    """Italian abbreviation acronym used on the cards"""
    pt: Optional[str]
    """Portuguese abbreviation acronym used on the cards"""
    pt_br: Optional[str]
    """Portuguese (Brazil) abbreviation acronym used on the cards"""
    pt_pt: Optional[str]
    """Portuguese (Portugal) abbreviation acronym used on the cards"""
    de: Optional[str]
    """German abbreviation acronym used on the cards"""
    nl: Optional[str]
    """Dutch abbreviation acronym used on the cards"""
    pl: Optional[str]
    """Polish abbreviation acronym used on the cards"""
    ru: Optional[str]
    """Russian abbreviation acronym used on the cards"""
    ja: Optional[str]
    """Japanese abbreviation acronym used on the cards"""
    ko: Optional[str]
    """Korean abbreviation acronym used on the cards"""
    zh_tw: Optional[str]
    """Chinese (Taiwan) abbreviation acronym used on the cards"""
    id: Optional[str]
    """Indonesian abbreviation acronym used on the cards"""
    th: Optional[str]
    """Thai abbreviation acronym used on the cards"""
    zh_cn: Optional[str]
    """Chinese (China) abbreviation acronym used on the cards"""
