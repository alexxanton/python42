from ex0.Card import Card


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

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            raise KeyError("mana not in game_state")

        if not self.is_playable(game_state.get("mana")):
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": None
            }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "mana": game_state["mana"] - self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        """Gets a target as a parameter and deals damage"""
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.card_type,
            "attack": self.attack,
            "health": self.health
        }
