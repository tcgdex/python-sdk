from typing import Generic, List, Optional, Type, TypeVar, Union

from tcgdexsdk.models.Model import Model
from tcgdexsdk.utils import fetch, fetch_list


class Query:
    @property
    def params(self):
        # Implement the logic to get query parameters
        pass

# Generic type variables
Item = TypeVar('Item', bound=Model)
ListModel = TypeVar('ListModel', bound=Union[str, int, Model])

class Endpoint(Generic[Item, ListModel]):
    def __init__(self,
                 tcgdex,
                 item_model: Type[Item],
                 list_model: Type[ListModel],
                 endpoint: str):
        self.tcgdex = tcgdex
        self.item_model = item_model
        self.list_model = list_model
        self.endpoint = endpoint

    async def get(self, id: str) -> Optional[Item]:
        return fetch(self.tcgdex, f"{self.tcgdex.getEndpoint()}/{self.tcgdex.language}/{self.endpoint}/{id.replace(' ', '%20')}", self.item_model)

    async def list(self, query: Optional[Query] = None) -> List[ListModel]:
        return fetch_list(self.tcgdex, f"{self.tcgdex.getEndpoint()}/{self.tcgdex.language}/{self.endpoint}", self.list_model)

    def getSync(self, id: str) -> Optional[Item]:
        return fetch(self.tcgdex, f"{self.tcgdex.getEndpoint()}/{self.tcgdex.language}/{self.endpoint}/{id.replace(' ', '%20')}", self.item_model)

    def listSync(self, query: Optional[Query] = None) -> List[ListModel]:
        return fetch_list(self.tcgdex, f"{self.tcgdex.getEndpoint()}/{self.tcgdex.language}/{self.endpoint}", self.list_model)
