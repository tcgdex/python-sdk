from enum import Enum

# Todo when min is 3.11
# Move to StringEnum and auto


class Language(Enum):
    EN = "en"
    """English"""
    FR = "fr"
    """French"""
    DE = "de"
    """German"""
    ES = "es"
    """Spanish"""
    IT = "it"
    """Italian"""
    PT = "pt"
    """Portuguese"""

    def __str__(self):
        return self.name.lower()


class Extension(Enum):
    """The different extension an image is available in"""

    PNG = "png"
    """.png image, with transparent background"""
    JPG = "jpg"
    """.jpg image, with white background"""
    WEBP = "webp"
    """.webp image, with transparent background"""

    def __str__(self):
        return self.name.lower()


class Quality(Enum):
    """
    Image quality if applicable
    (only cards does have quality selector)
    """

    HIGH = "high"
    """the string representation of the quality"""
    LOW = "low"
    """A Low quality image"""

    def __str__(self):
        return self.name.lower()
