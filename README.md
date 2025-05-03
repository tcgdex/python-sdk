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
		<img src="https://img.shields.io/github/actions/workflow/status/tcgdex/python-sdk/build.yml?style=flat-square" alt="Build Status" />
	</a>
	<a href="https://discord.gg/peACSRMZ7V">
		<img src="https://img.shields.io/discord/857231041261076491?color=%235865F2&label=Discord&style=flat-square" alt="Discord Link">
	</a>
</p>

# TCGdex Python SDK

A fast, type-safe Python SDK for the TCGdex API. Query Pokémon Trading Card Game data easily. 🚀

```python
from tcgdexsdk import TCGdex

# Fetch a card in one line
card = await TCGdex().card.get("swsh3-136")
card = TCGdex().card.getSync("swsh3-136")
print(f"Found: {card.name} ({card.localId}/{card.set.cardCount.total})")
```

## ⚡️ Quick Install

```bash
pip install tcgdex-sdk
```

## 🚀 Features

- **Type-Safe**: Full typing support for better IDE integration
- **Async/Await**: Built for modern Python applications and compatible with synchronous operations
- **Zero Config**: Works out of the box
- **Multi-Language**: Support for English, French, German, Japanese, Chinese, [and more](https://github.com/tcgdex/cards-database/blob/master/interfaces.d.ts#L1-L5)
- **Rich Data**: Access cards, sets, series, rarities, and more
- **Lightweight**: Minimal dependencies (only [dacite](https://github.com/konradhalas/dacite))

## 🎯 Quick Examples

### Find Cards by Various Criteria

```python
sdk = TCGdex("en")

# Get the cards made by the illustrator
cards = await sdk.illustrator.get("5ban Graphics")
cards = sdk.illustrator.getSync("5ban Graphics")

# Get the data about the Sword & Shield serie by ID
series = await sdk.serie.get("swsh")
series = sdk.serie.getSync("swsh")

# Get all cards with 110 HP
hp_cards = await sdk.hp.get("110")
hp_cards = sdk.hp.getSync("110")

# List all available rarities
rarities = await sdk.rarity.list()
rarities = sdk.rarity.listSync()

# List all cards with the name being "Furret"
rarities = await sdk.card.list(Query().equal("name", "Furret"))
rarities = sdk.card.listSync(Query().equal("name", "Furret"))
```

### Working with Sets and Series

```python
# Get set details
darkness_ablaze = await sdk.set.get("Darkness Ablaze")
# darkness_ablaze = sdk.set.getSync("Darkness Ablaze")
print(f"Set: {darkness_ablaze.name} ({darkness_ablaze.cardCount.total} cards)")

# Get series info
swsh = await sdk.serie.get("swsh")
# swsh = sdk.serie.getSync("swsh")
print(f"Series: {swsh.name} ({len(swsh.sets)} sets)")
```

## 🛠 Available Endpoints

### Card Data
```python
sdk.card         # Core card data
sdk.rarity       # Card rarities
sdk.hp           # HP values
sdk.illustrator  # Card illustrators
```

### Game Mechanics
```python
sdk.type         # Pokémon types
sdk.energyType   # Energy types
sdk.retreat      # Retreat costs
sdk.stage        # Evolution stages
```

### Card Details
```python
sdk.variant        # Card variants
sdk.suffix         # Card suffixes
sdk.regulationMark # Regulation marks
sdk.dexId         # Pokédex IDs
```

### Collections
```python
sdk.set           # Card sets
sdk.serie         # Card series
```

## 🌐 Language Support

```python
from tcgdexsdk import TCGdex, Language

# Using string
sdk = TCGdex("en")  # English
sdk = TCGdex("fr")  # French

# Using enum (type-safe)
sdk = TCGdex(Language.EN)
sdk = TCGdex(Language.FR)

# After creating the instance you can change at any time the language
sdk.setLanguage(Language.FR)
# or
sdk.setLanguage("fr")
```

_[full list of languages available here](https://github.com/tcgdex/cards-database/blob/master/interfaces.d.ts#L1-L5)_

__

## 🤝 Contributing

We love contributions! Here's how:

1. 🍴 Fork it
2. 🌿 Create your feature branch (`git checkout -b feature/amazing`)
3. 🔧 Make your changes
4. 🚀 Push to the branch (`git push origin feature/amazing`)
5. 🎉 Open a PR

## 📘 Documentation

- [Full API Documentation](https://www.tcgdex.dev)
- [Python SDK Guide](https://www.tcgdex.dev/sdks/python)

## 💬 Community & Support

- [Discord Server](https://discord.gg/peACSRMZ7V) - Get help and discuss features
- [GitHub Issues](https://github.com/tcgdex/python-sdk/issues) - Bug reports and feature requests

## 📜 License

MIT © [TCGdex](https://github.com/tcgdex)
