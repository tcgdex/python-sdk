from enum import StrEnum
from enum import auto


class Language(StrEnum):
    EN = auto()
    """English"""
    FR = auto()
    """French"""
    DE = auto()
    """German"""
    ES = auto()
    """Spanish"""
    IT = auto()
    """Italian"""
    PT = auto()
    """Portuguese"""


class Extension(StrEnum):
    """The different extension an image is available in"""

    PNG = auto()
    """.png image, with transparent background"""
    JPG = auto()
    """.jpg image, with white background"""
    WEBP = auto()
    """.webp image, with transparent background"""


class Quality(StrEnum):
    """
    Image quality if applicable
    (only cards does have quality selector)
    """

    HIGH = auto()
    """the string representation of the quality"""
    LOW = auto()
    """A Low quality image"""
