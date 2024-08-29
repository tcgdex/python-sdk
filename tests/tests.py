import unittest
from typing import Callable

import vcr

from tcgdexsdk import Language
from tcgdexsdk import TCGdex


def _use_cassette(test: Callable) -> Callable:
    return vcr.use_cassette(f"fixtures/{test.__name__.removeprefix('test_')}.yaml")(
        test
    )


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = TCGdex(Language.EN)

    @_use_cassette
    def test_card(self):
        self.assertIsNotNone(self.api.fetch_cards())
        self.assertIsNotNone(self.api.fetch_card("swsh3-136"))
        self.assertIsNotNone(self.api.fetch_card("swsh3", "136"))

    @_use_cassette
    def test_set(self):
        self.assertIsNotNone(self.api.fetch_set("swsh3"))
        self.assertIsNotNone(self.api.fetch_sets())

    @_use_cassette
    def test_serie(self):
        self.assertIsNotNone(self.api.fetch_serie("swsh"))
        self.assertIsNotNone(self.api.fetch_series())

    @_use_cassette
    def test_type(self):
        self.assertIsNotNone(self.api.fetch_types())
        self.assertIsNotNone(self.api.fetch_type("Colorless"))

    @_use_cassette
    def test_retreat(self):
        self.assertIsNotNone(self.api.fetch_retreats())
        self.assertIsNotNone(self.api.fetch_retreat("1"))

    @_use_cassette
    def test_rarity(self):
        self.assertIsNotNone(self.api.fetch_rarities())
        self.assertIsNotNone(self.api.fetch_rarity("Uncommon"))

    @_use_cassette
    def test_illustrator(self):
        self.assertIsNotNone(self.api.fetch_illustrators())
        self.assertIsNotNone(self.api.fetch_illustrator("tetsuya koizumi"))

    @_use_cassette
    def test_hp(self):
        self.assertIsNotNone(self.api.fetch_hps())
        self.assertIsNotNone(self.api.fetch_hp("110"))

    @_use_cassette
    def test_category(self):
        self.assertIsNotNone(self.api.fetch_categories())
        self.assertIsNotNone(self.api.fetch_category("Pokemon"))

    @_use_cassette
    def test_dex_id(self):
        self.assertIsNotNone(self.api.fetch_dex_ids())
        self.assertIsNotNone(self.api.fetch_dex_id("162"))

    @_use_cassette
    def test_energy_type(self):
        self.assertIsNotNone(self.api.fetch_energy_types())
        self.assertIsNotNone(self.api.fetch_energy_type("Special"))

    @_use_cassette
    def test_regulation_mark(self):
        self.assertIsNotNone(self.api.fetch_regulation_marks())
        self.assertIsNotNone(self.api.fetch_regulation_mark("D"))

    @_use_cassette
    def test_stage(self):
        self.assertIsNotNone(self.api.fetch_stages())
        self.assertIsNotNone(self.api.fetch_stage("Basic"))

    @_use_cassette
    def test_suffix(self):
        self.assertIsNotNone(self.api.fetch_suffixes())
        self.assertIsNotNone(self.api.fetch_suffix("EX"))

    @_use_cassette
    def test_trainer_type(self):
        self.assertIsNotNone(self.api.fetch_trainer_types())
        self.assertIsNotNone(self.api.fetch_trainer_type("Tool"))

    @_use_cassette
    def test_variant(self):
        self.assertIsNotNone(self.api.fetch_variants())
        self.assertIsNotNone(self.api.fetch_variant("holo"))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
