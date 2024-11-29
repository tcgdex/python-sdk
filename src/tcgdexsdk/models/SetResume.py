from dataclasses import dataclass
from http.client import HTTPResponse
from typing import Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension
from tcgdexsdk.models.Model import Model
from tcgdexsdk.models.subs import SetCardCountResume


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
    """the Set Symbol incomplete URL (use get_symbol_url/get_symbol)"""
    cardCount: SetCardCountResume
    """the number of card in the set"""

    def get_logo_url(self, extension: Union[str, Extension]) -> Optional[str]:
        """
        Get the logo full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.logo:
            return f"{self.logo}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_logo(self, format: Union[str, Extension]) -> Optional[HTTPResponse]:
        """
        Get the logo buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if url := self.get_logo_url(format):
            return utils.download_image(url)

    def get_symbol_url(self, extension: Union[str, Extension]) -> Optional[str]:
        """
        Get the symbol full url
        @param extension: the file extension you want to use
        @return: the full URL of the logo
        """
        if self.symbol:
            return f"{self.symbol}.{extension}"

    # noinspection PyShadowingBuiltins
    def get_symbol(
        self, format: Union[str, Extension]
    ) -> Optional[HTTPResponse]:
        """
        Get the symbol buffer
        @param format: the image format
        @return: a buffer containing the image
        """
        if url := self.get_symbol_url(format):
            return utils.download_image(url)

    async def get_full_set(self):
        """
        Get the full set
        @return: the full set if available
        """
        return await self.sdk.set.get(self.id)
