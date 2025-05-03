from enum import Enum

# Todo when min is 3.11
# Move to StringEnum and auto


class Language(Enum):
    EN = "en"
    """English"""
    FR = "fr"
    """French"""
    ES = "es"
    """Spanish"""
    ES_MX = "es-mx"
    """Latin Spanish"""
    IT = "it"
    """Italian"""
    PT_BR = "pt-br"
    """Brazilian Portuguese"""
    PT_PT = "pt-pt"
    """Portugal Portuguese"""
    DE = "de"
    """German"""
    NL = "nl"
    """"""
    PL = "pl"
    """Polish"""
    RU = "ru"
    """Russian"""
    JA = "ja"
    """Japanese"""
    KO = "ko"
    """Korean"""
    zh_TW = "zh-tw"
    """Chinese"""
    ID = "id"
    """Indonesian"""
    TH = "th"
    """Thai"""
    ZH_CN = "zh-cn"
    """Chinese"""

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
