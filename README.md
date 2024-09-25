<p align="center">
	<a href="https://www.tcgdex.net">
		<img src="https://www.tcgdex.net/assets/og.png" width="90%" alt="TCGdex Main Image">
	</a>
</p>
<p align="center">
	<a href="http://pypi.org/project/tcgdex-sdk">
		<img src="https://img.shields.io/pypi/v/tcgdex-sdk?style=flat-square" alt="Pypi Version">
	</a>
	<a href="http://pypi.org/project/tcgdex-sdk">
		<img src="https://img.shields.io/pypi/dm/tcgdex-sdk?style=flat-square" alt="Pypi Downloads">
	</a>
		<a href="https://github.com/tcgdex/python-sdk/stargazers">
		<img src="https://img.shields.io/github/stars/tcgdex/python-sdk?style=flat-square" alt="Github stars">
	</a>
	<a href="https://github.com/tcgdex/python-sdk/actions/workflows/build.yml">
		<img src="https://img.shields.io/github/actions/workflow/status/tcgdex/python-sdk/build.yml?style=flat-square" alt="the TCGdex Python SDK is released under the MIT license." />
	</a>
	<a href="https://discord.gg/peACSRMZ7V">
		<img src="https://img.shields.io/discord/857231041261076491?color=%235865F2&label=Discord&style=flat-square" alt="Discord Link">
	</a>
</p>

# TCGdex Python SDK

The TCGdex Python SDK provides a convenient access with the Open Source TCGdex API.

_The full API/SDK documentation is available at [API Documentation - TCGdex](https://www.tcgdex.dev)_

### Getting Started

#### How To install

run the following command:

```bash
pip install tcgdex-sdk
```

#### Getting Started

**Example: Fetch a Card**

```python
from tcgdexsdk import TCGdex

tcgdex = TCGdex("en") # You can also use `Language.EN` TCGdex(Language.EN)
res = await tcgdex.card.get("swsh1-136")
```

**Other Examples**

```python
# fetch a Set using the set's name or ID
await tcgdex.set.get('Darkness Ablaze')

# Fetch a serie using the serie's name or ID
await tcgdex.serie.get('Sword & Shield')

# Fetch cards possible pokemon cards HP
await tcgdex.hp.list()

# Fetch Cards with the specific number of HP
await tcgdex.hp.get('110')

# Fetch cards possible illustrators
await tcgdex.illustrator.list()

# Fetch Cards with the specific illustrator
await tcgdex.illustrator.get('tetsuya koizumi')
```

**Other Endpoints**

Every endpoints below work just like the ones above
- a function `list` to get the list of elements
- a function `get` to get details on the element

- `variant`: fetch by the variants
- `trainerType`: fetch trainer cards types
- `suffix`: fetch differents cards suffixes
- `stage`: fetch differents cards stages
- `regulationMark`: Fetch by the regulation mark (letter at the bottom of the card)
- `energyType`: Fetch different types of energies
- `dexId`: fetch pokemon Global Pokédex IDS
- `type`: fetch the cards using the Pokémon type(s)
- `retreat`: fetch the cards using the retreat count
- `rarity`: fetch the cards rarities
- `illustrator`: fetch all the cards illustrators
- `hp`: fetch the different cards possible HPs
- `category`: the different cards categories


## Contributing

See [CONTRIBUTING.md](https://github.com/tcgdex/python-sdk/blob/master/CONTRIBUTING.md)

TL::DR

- Fork

- Commit your changes

- Pull Request on this Repository

## License

This project is licensed under the MIT License. A copy of the license is available at [LICENSE.md](https://github.com/tcgdex/python-sdk/blob/master/LICENSE.md)
