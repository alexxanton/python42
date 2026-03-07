from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any


class EliteCard(Card, Combatable, Magical):
    """Powerful card with multiple abilities"""

    card_type = "Elite Card"

    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 mana: int, defense: int, health: int, combat: str):
        super().__init__(name, cost, rarity)

        if not isinstance(damage, int) or damage < 0:
            raise ValueError("damage must be a non-negative integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("defense must be a non-negative integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("health must be a non-negative integer")
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("mana must be a non-negative integer")
        if not isinstance(combat, str) or not combat:
            raise ValueError("combat must be a non-empty string")

        self.mana = mana
        self.damage = damage
        self.combat = combat
        self.defense = defense
        self.health = health

    def play(self, game_state: dict) -> dict:
        return self.play_base(game_state, "")

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def attack(self, target: Any) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.damage,
            "combat_type": self.combat,
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError(
                "incoming_damage must be a non-negative integer"
            )

        damage_taken = incoming_damage - self.defense
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": incoming_damage - damage_taken,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "damage": self.damage,
            "defense": self.damage,
            "health": self.health,
            "combat_type": self.combat,
        }

    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict:
        if not isinstance(spell_name, str) or not spell_name:
            raise ValueError("spell_name must be a non-empty string")
        if not isinstance(targets, list):
            raise ValueError("targets must be a list")

        mana_usage = 4
        self.mana -= mana_usage

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [str(target) for target in targets],
            "mana_used": mana_usage,
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount must be a non-negative integer")
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
