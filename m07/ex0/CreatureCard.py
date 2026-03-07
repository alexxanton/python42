from ex0.Card import Card
from typing import Any, Dict


class CreatureCard(Card):
    """Summons a creature to the battlefield"""

    card_type = "Creature"

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("attack must be a non-negative integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("health must be a non-negative integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return self.play_base(game_state, "Creature summoned to battlefield")

    def attack_target(self, target: Any) -> Dict[str, Any]:
        """Gets a target as a parameter and deals damage"""
        return {
            "attacker": self.name,
            "target": str(target),
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.card_type,
            "attack": self.attack,
            "health": self.health
        }
