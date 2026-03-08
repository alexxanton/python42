from random import randint, choice
from enum import StrEnum
from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class Creatures(StrEnum):
    DRAGON = "dragon"
    GOBLIN = "goblin"
    GNOME = "gnome"


class Classes(StrEnum):
    WARRIOR = "warrior"
    DRUID = "druid"
    BARD = "bard"


class Spells(StrEnum):
    BOLT = "bolt"
    BLAST = "blast"
    RAY = "ray"


class Elements(StrEnum):
    FIRE = "fire"
    CHAOS = "chaos"
    LIGHTNING = "lightning"


class Artifacts(StrEnum):
    MANA_RING = "mana_ring"
    TRINKET = "trinket"
    MAGIC_JEWEL = "magic_jewel"


class Rarities(StrEnum):
    COMMON = "common"
    RARE = "rare"
    LEGENDARY = "legendary"


class FantasyCardFactory(CardFactory):
    def create_creature(self) -> Card:
        name = f"{choice(list(Creatures))} {choice(list(Classes))}".title()
        cost = randint(0, 10)
        rarity = choice(list(Rarities)).value
        attack = randint(0, 10)
        health = randint(0, 10)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self) -> Card:
        name = f"{choice(list(Elements))} {choice(list(Spells))}".title()
        cost = randint(0, 10)
        rarity = choice(list(Rarities)).value
        effect_type = "a"
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self) -> Card:
        name = choice(list(Artifacts)).value.title()
        cost = randint(0, 10)
        rarity = choice(list(Rarities)).value
        durability = randint(0, 10)
        effect = "a"
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck: list[Card] = []
        gen = [self.create_creature, self.create_spell, self.create_artifact]
        for _ in range(size):
            create = choice(gen)
            deck.append(create())
        return {"deck": deck}

    def get_supported_types(self) -> Dict[str, Any]:
        return {
            "creatures": list(map(str, Creatures)),
            "spells": list(map(str, Spells)),
            "artifacts": list(map(str, Artifacts)),
        }
