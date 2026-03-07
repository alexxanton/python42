from ex0.Card import Card


class ArtifactCard(Card):
    """Applies status effects"""

    card_type = "Artifact"

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability < -1:
            raise ValueError(
                "durability must be a integer bigger or equal to -1"
            )
        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must be a non-empty string")

        self.durability = durability
        self.effect = effect

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
            "effect": self.activate_ability(),
        }

    def activate_ability(self) -> dict:
        ability = f"Active for {self.durability} turn(s): {self.effect}"
        if self.durability == -1:
            ability = f"Permanent: {self.effect}"
        elif self.durability == 0:
            ability = f"Instant: {self.effect}"
        return {"ability": ability}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.card_type,
            "durability": self.durability,
            "effect": self.effect
        }
