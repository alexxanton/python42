from ex0.Card import Card


class ArtifactCard(Card):
    """Applies status effects"""

    card_type = "Artifact"

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability < 0:
            raise ValueError("durability must be a non-negative integer")
        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must be a non-empty string")

        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.card_type,
        }
