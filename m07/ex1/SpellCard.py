from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("effect type must be a non-empty string")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass
