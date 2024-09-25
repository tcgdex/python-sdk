from unittest import IsolatedAsyncioTestCase
from typing import Callable, List

import vcr

from tcgdexsdk import TCGdex, Language
from tcgdexsdk.models.Card import Card
from tcgdexsdk.models.CardResume import CardResume
from tcgdexsdk.models.Serie import Serie
from tcgdexsdk.models.SerieResume import SerieResume
from tcgdexsdk.models.Set import Set
from tcgdexsdk.models.SetResume import SetResume
from tcgdexsdk.models.StringEndpoint import StringEndpoint

def _use_cassette(test: Callable) -> Callable:
    return vcr.use_cassette(f"tests/.fixtures/{test.__name__}.yaml")(
        test
    )

class APITest(IsolatedAsyncioTestCase):
    def setUp(self):
        self.api = TCGdex(Language.EN)

    @_use_cassette
    async def test_card_resume(self):
        res = await self.api.card.list()
        self.assertIsInstance(res[0], CardResume)

    @_use_cassette
    async def test_card(self):
        res = await self.api.card.get("swsh1-136")
        self.assertIsInstance(res, Card)

    @_use_cassette
    async def test_set_resume(self):
        res = await self.api.set.list()
        self.assertIsInstance(res[0], SetResume)

    @_use_cassette
    async def test_set(self):
        res = await self.api.set.get("swsh1")
        self.assertIsInstance(res, Set)

    @_use_cassette
    async def test_serie_resume(self):
        res = await self.api.serie.list()
        self.assertIsInstance(res[0], SerieResume)

    @_use_cassette
    async def test_serie(self):
        res = await self.api.serie.get("swsh")
        self.assertIsInstance(res, Serie)

    @_use_cassette
    async def test_variant_list(self):
        res = await self.api.variant.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_variant_item(self):
        res = await self.api.variant.get('reverse')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_trainerType_list(self):
        res = await self.api.trainerType.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_trainerType_item(self):
        res = await self.api.trainerType.get('trainer')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_suffix_list(self):
        res = await self.api.suffix.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_suffix_item(self):
        res = await self.api.suffix.get('ex')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_stage_list(self):
        res = await self.api.stage.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_stage_item(self):
        res = await self.api.stage.get('stage1')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_regulationMark_list(self):
        res = await self.api.regulationMark.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_regulationMark_item(self):
        res = await self.api.regulationMark.get('D')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_energyType_list(self):
        res = await self.api.energyType.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_energyType_item(self):
        res = await self.api.energyType.get('normal')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_dexId_list(self):
        res = await self.api.dexId.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_dexId_item(self):
        res = await self.api.dexId.get('1')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_type_list(self):
        res = await self.api.type.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_type_item(self):
        res = await self.api.type.get('grass')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_retreat_list(self):
        res = await self.api.retreat.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_retreat_item(self):
        res = await self.api.retreat.get('1')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_rarity_list(self):
        res = await self.api.rarity.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_rarity_item(self):
        res = await self.api.rarity.get('common')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_illustrator_list(self):
        res = await self.api.illustrator.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_illustrator_item(self):
        res = await self.api.illustrator.get('0313')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_hp_list(self):
        res = await self.api.hp.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_hp_item(self):
        res = await self.api.hp.get('10')
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_category_list(self):
        res = await self.api.category.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_category_item(self):
        res = await self.api.category.get('pokemon')
        self.assertIsInstance(res, StringEndpoint)



def main():
    unittest.main()


if __name__ == "__main__":
    main()
