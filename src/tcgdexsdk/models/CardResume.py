from dataclasses import dataclass
from http.client import HTTPResponse
from typing import Optional, Union

from tcgdexsdk import utils
from tcgdexsdk.enums import Extension, Quality
from tcgdexsdk.models.Model import Model


@dataclass
class CardResume(Model):
    """Card Resume class, contains basic information about a specific card
    to get the full card you can use the `get_full_card()` function"""

    id: str
    """Globally unique card ID based on the set ID and the cards ID within the set"""
    localId: str
    """ID indexing this card within its set, usually just its number"""
    name: str
    """Card name"""
    image: Optional[str]
    """Card image url without the extension and quality"""

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

    async def get_full_card(self):
        """
        Get the full Card
        @return: the full card if available
        """
        return await self.sdk.card.get(self.id)
