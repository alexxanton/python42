from ex0.Card import Card


class SpellCard(Card):
    """Casts a spell with varying effects"""

    card_type = "Spell"

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("effect type must be a non-empty string")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return (
            self.play_base(game_state, self.resolve_effect([])["effect"])
        )

    def resolve_effect(self, targets: list) -> dict:
        """Selects the effect based on the effect type"""
        effect = ""
        match self.effect_type:
            case "damage":
                effect = "Deal 3 damage to target"
            case "heal":
                effect = "Heal 3 HP to target"
            case "buff":
                effect = "Boost target stats by 3"
            case "debuff":
                effect = "Lowered target stats by 3"
            case _:
                raise ValueError(f"unknown effect_type '{self.effect_type}'")
        return {"effect": effect}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "effect_type": self.effect_type
        }
