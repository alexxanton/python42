from random import randint, choice
from enum import StrEnum
from typing import Any, Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class Creatures(StrEnum):
    """Creatures for creature cards"""
    DRAGON = "dragon"
    GOBLIN = "goblin"
    GNOME = "gnome"


class Classes(StrEnum):
    """Classes for creature cards"""
    WARRIOR = "warrior"
    DRUID = "druid"
    BARD = "bard"


class Spells(StrEnum):
    """Spells for spell cards"""
    BOLT = "bolt"
    BLAST = "blast"
    RAY = "ray"


class Elements(StrEnum):
    """Elements for spell cards and dragons"""
    FIRE = "fire"
    CHAOS = "chaos"
    LIGHTNING = "lightning"
    ICE = "ice"


class Artifacts(StrEnum):
    """Artifacts for artifact cards"""
    MANA_RING = "mana_ring"
    TRINKET = "trinket"
    MAGIC_STAFF = "magic_staff"
    CHAOS_CRYSTAL = "chaos_crystal"


class Rarities(StrEnum):
    """Card rarities"""
    COMMON = "common"
    RARE = "rare"
    LEGENDARY = "legendary"


class FantasyCardFactory(CardFactory):
    """Manages fantasy card creation"""
    def create_creature(self) -> Card:
        name = choice(list(Creatures))
        if name == "dragon":
            name = f"{choice(list(Elements))} {name}".title()
        else:
            name = f"{name} {choice(list(Classes))}".title()
        cost = randint(3, 10)
        rarity = choice(list(Rarities))
        attack = randint(3, 10)
        health = randint(4, 10)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self) -> Card:
        effect_types = ["damage", "heal", "buff", "debuff"]
        name = f"{choice(list(Elements))} {choice(list(Spells))}".title()
        cost = randint(3, 10)
        rarity = choice(list(Rarities))
        effect_type = choice(effect_types)
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self) -> Card:
        effects = ["+1 mana", "+1 defense", "+1 attack"]
        name = choice(list(Artifacts)).title()
        cost = randint(3, 10)
        rarity = choice(list(Rarities))
        durability = randint(-1, 10)
        effect = choice(effects)
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
