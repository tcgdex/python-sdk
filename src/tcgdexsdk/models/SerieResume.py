from dataclasses import dataclass
from http.client import HTTPResponse
from typing import Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension
from tcgdexsdk.models.Model import Model
from tcgdexsdk.models.Serie import Serie


@dataclass
class SerieResume(Model):
    """Pokémon TCG Serie Resume"""

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

    async def get_full_serie(self) -> Optional[Serie]:
        """
        Get the full Card
        @return: the full card if available
        """
        return await self.sdk.serie.get(self.id)
