from dataclasses import dataclass
from http.client import HTTPResponse
from typing import List, Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension
from tcgdexsdk.models.Model import Model
from tcgdexsdk.models.SetResume import SetResume


@dataclass
class Serie(Model):
    """Pokémon TCG Serie"""

    sets: List[SetResume]
    """the list of sets the Serie contains"""

    id: str
    """the Serie unique ID"""
    name: str
    """the Serie name"""
    logo: Optional[str]
    """the Serie Logo (basically also the first set logo)"""

    def get_logo_url(self, extension: Union[str, Extension]) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    def get_logo(self, format: Union[str, Extension]) -> Optional[HTTPResponse]:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if url := self.get_logo_url(format):
            return utils.download_image(url)
