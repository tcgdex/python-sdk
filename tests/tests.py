import unittest
from typing import Callable
from unittest.mock import patch

import vcr

from tcgdexsdk import Language, TCGdex
from tcgdexsdk.models.Card import Card
from tcgdexsdk.models.CardResume import CardResume
from tcgdexsdk.models.Serie import Serie
from tcgdexsdk.models.SerieResume import SerieResume
from tcgdexsdk.models.Set import Set
from tcgdexsdk.models.SetResume import SetResume
from tcgdexsdk.models.StringEndpoint import StringEndpoint
from tcgdexsdk.query import Query
from tcgdexsdk.models.subs import Booster

def _use_cassette(test: Callable) -> Callable:
    return vcr.use_cassette(f"tests/.fixtures/{test.__name__}.yaml")(test)


class APITest(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.api = TCGdex(Language.EN)

    @patch("tcgdexsdk.endpoints.Endpoint.fetch")
    @patch("tcgdexsdk.endpoints.Endpoint.fetch_list")
    async def test_uri(self, mock_fetch_list, mock_fetch):
        api = TCGdex(Language.EN)

        api.URI = "http://localhost:3000/v2"

        await api.card.get("swsh1-136")
        mock_fetch.assert_called_once_with(api, "http://localhost:3000/v2/en/cards/swsh1-136", Card)

        await api.card.list()
        mock_fetch_list.assert_called_once_with(api, "http://localhost:3000/v2/en/cards", CardResume)

    @patch("tcgdexsdk.endpoints.Endpoint.fetch")
    @patch("tcgdexsdk.endpoints.Endpoint.fetch_list")
    async def test_endpoint(self, mock_fetch_list, mock_fetch):
        api = TCGdex(Language.EN)

        api.setEndpoint("http://localhost:3000/v2")
        self.assertEqual(api.getEndpoint(), "http://localhost:3000/v2")

        await api.card.get("swsh1-136")
        mock_fetch.assert_called_once_with(api, "http://localhost:3000/v2/en/cards/swsh1-136", Card)

        await api.card.list()
        mock_fetch_list.assert_called_once_with(api, "http://localhost:3000/v2/en/cards", CardResume)

    @patch("tcgdexsdk.endpoints.Endpoint.fetch")
    @patch("tcgdexsdk.endpoints.Endpoint.fetch_list")
    async def test_language(self, mock_fetch_list, mock_fetch):
        api = TCGdex()

        # Default language should be english
        self.assertEqual(api.getLanguage(), Language.EN)

        # Card should be fetched in english
        await api.card.get("swsh1-136")
        mock_fetch.assert_called_once_with(api, f"{api.getEndpoint()}/en/cards/swsh1-136", Card)

        # Card should be fetched in french
        api.setLanguage(Language.FR)

        # Test that the language is set correctly
        self.assertEqual(api.getLanguage(), Language.FR)
        await api.card.get("swsh1-136")
        mock_fetch.assert_called_with(api, f"{api.getEndpoint()}/fr/cards/swsh1-136", Card)

    @_use_cassette
    async def test_fr(self):
        tcg = TCGdex(Language.FR)
        res = await tcg.card.get("swsh3-136")
        self.assertEqual(res.name, "Fouinar")
        tcg2 = TCGdex("fr")
        res = await tcg2.card.get("swsh3-136")
        self.assertEqual(res.name, "Fouinar")

    @_use_cassette
    async def test_query_equal(self):
        tcg = TCGdex(Language.EN)
        res = await tcg.card.list(Query().equal("name", "Furret"))
        for card in res:
            self.assertEqual(card.name, "Furret")

    @_use_cassette
    async def test_query_not_equal(self):
        tcg = TCGdex()
        res = await tcg.card.list(Query().notEqual("name", "Furret"))
        for card in res:
            self.assertNotEqual(card.name, "Furret")

    @_use_cassette
    async def test_card_resume(self):
        res = await self.api.card.list()
        self.assertIsInstance(res[0], CardResume)

    @_use_cassette
    async def test_card(self):
        res = await self.api.card.get("A1-001")
        self.assertIsInstance(res, Card)
        # Also check if the booster is defined & used
        self.assertIsInstance(res.boosters[0], Booster)

    @_use_cassette
    async def test_get_full_card(self):
        set = await self.api.set.get("swsh1")
        card = set.cards[0]
        self.assertIsInstance(card.sdk, TCGdex)
        card_full = await card.get_full_card()
        self.assertIsInstance(card_full, Card)

    @_use_cassette
    async def test_set_resume(self):
        res = await self.api.set.list()
        self.assertIsInstance(res[0], SetResume)

    @_use_cassette
    async def test_set(self):
        res = await self.api.set.get("A1")
        self.assertIsInstance(res, Set)
        self.assertIsInstance(res.boosters[0], Booster)

    @_use_cassette
    async def test_get_full_set(self):
        serie = await self.api.serie.get("swsh")
        set = serie.sets[0]
        self.assertIsInstance(set.sdk, TCGdex)
        set_full = await set.get_full_set()
        self.assertIsInstance(set_full, Set)

    @_use_cassette
    async def test_serie_resume(self):
        res = await self.api.serie.list()
        self.assertIsInstance(res[0], SerieResume)

    @_use_cassette
    async def test_serie(self):
        res = await self.api.serie.get("swsh")
        self.assertIsInstance(res, Serie)

    @_use_cassette
    async def test_get_full_serie(self):
        series = await self.api.serie.list()
        serie = series[0]
        self.assertIsInstance(serie.sdk, TCGdex)
        serie_full = await serie.get_full_serie()
        self.assertIsInstance(serie_full, Serie)

    @_use_cassette
    async def test_variant_list(self):
        res = await self.api.variant.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_variant_item(self):
        res = await self.api.variant.get("reverse")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_trainerType_list(self):
        res = await self.api.trainerType.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_trainerType_item(self):
        res = await self.api.trainerType.get("trainer")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_suffix_list(self):
        res = await self.api.suffix.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_suffix_item(self):
        res = await self.api.suffix.get("ex")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_stage_list(self):
        res = await self.api.stage.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_stage_item(self):
        res = await self.api.stage.get("stage1")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_regulationMark_list(self):
        res = await self.api.regulationMark.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_regulationMark_item(self):
        res = await self.api.regulationMark.get("D")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_energyType_list(self):
        res = await self.api.energyType.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_energyType_item(self):
        res = await self.api.energyType.get("normal")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_dexId_list(self):
        res = await self.api.dexId.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_dexId_item(self):
        res = await self.api.dexId.get("1")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_type_list(self):
        res = await self.api.type.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_type_item(self):
        res = await self.api.type.get("grass")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_retreat_list(self):
        res = await self.api.retreat.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_retreat_item(self):
        res = await self.api.retreat.get("1")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_rarity_list(self):
        res = await self.api.rarity.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_rarity_item(self):
        res = await self.api.rarity.get("common")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_illustrator_list(self):
        res = await self.api.illustrator.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_illustrator_item(self):
        res = await self.api.illustrator.get("0313")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_hp_list(self):
        res = await self.api.hp.list()
        self.assertIsInstance(res[0], int)

    @_use_cassette
    async def test_hp_item(self):
        res = await self.api.hp.get("10")
        self.assertIsInstance(res, StringEndpoint)

    @_use_cassette
    async def test_category_list(self):
        res = await self.api.category.list()
        self.assertIsInstance(res[0], str)

    @_use_cassette
    async def test_category_item(self):
        res = await self.api.category.get("pokemon")
        self.assertIsInstance(res, StringEndpoint)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
