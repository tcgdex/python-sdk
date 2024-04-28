import unittest

from tcgdexsdk import Language
from tcgdexsdk import TCGdex


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = TCGdex(Language.EN)

    def test_card(self):
        self.assertIsNotNone(self.api.fetch_cards())
        self.assertIsNotNone(self.api.fetch_card("swsh3-136"))
        self.assertIsNotNone(self.api.fetch_card("swsh3", "136"))

    def test_set(self):
        self.assertIsNotNone(self.api.fetch_set("swsh3"))
        self.assertIsNotNone(self.api.fetch_sets())

    def test_serie(self):
        self.assertIsNotNone(self.api.fetch_serie("swsh"))
        self.assertIsNotNone(self.api.fetch_series())

    def test_type(self):
        self.assertIsNotNone(self.api.fetch_types())
        self.assertIsNotNone(self.api.fetch_type("Colorless"))

    def test_retreat(self):
        self.assertIsNotNone(self.api.fetch_retreats())
        self.assertIsNotNone(self.api.fetch_retreat("1"))

    def test_rarity(self):
        self.assertIsNotNone(self.api.fetch_rarities())
        self.assertIsNotNone(self.api.fetch_rarity("Uncommon"))

    def test_illustrator(self):
        self.assertIsNotNone(self.api.fetch_illustrators())
        self.assertIsNotNone(self.api.fetch_illustrator("tetsuya koizumi"))

    def test_hp(self):
        self.assertIsNotNone(self.api.fetch_hps())
        self.assertIsNotNone(self.api.fetch_hp("110"))

    def test_category(self):
        self.assertIsNotNone(self.api.fetch_categories())
        self.assertIsNotNone(self.api.fetch_category("Pokemon"))

    def test_dex_id(self):
        self.assertIsNotNone(self.api.fetch_dex_ids())
        self.assertIsNotNone(self.api.fetch_dex_id("162"))

    def test_energy_type(self):
        self.assertIsNotNone(self.api.fetch_energy_types())
        self.assertIsNotNone(self.api.fetch_energy_type("Special"))

    def test_regulation_mark(self):
        self.assertIsNotNone(self.api.fetch_regulation_marks())
        self.assertIsNotNone(self.api.fetch_regulation_mark("D"))

    def test_stage(self):
        self.assertIsNotNone(self.api.fetch_stages())
        self.assertIsNotNone(self.api.fetch_stage("Basic"))

    def test_suffix(self):
        self.assertIsNotNone(self.api.fetch_suffixes())
        self.assertIsNotNone(self.api.fetch_suffix("EX"))

    def test_trainer_type(self):
        self.assertIsNotNone(self.api.fetch_trainer_types())
        self.assertIsNotNone(self.api.fetch_trainer_type("Tool"))

    def test_variant(self):
        self.assertIsNotNone(self.api.fetch_variants())
        self.assertIsNotNone(self.api.fetch_variant("holo"))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
