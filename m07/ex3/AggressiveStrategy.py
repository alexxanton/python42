from random import sample
from typing import Any, Dict, List
from ex0.Card import Card
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    """Prioritizes low-cost damage dealing cards and attacking creatures"""
    def execute_turn(
        self, hand: List[Card], battlefield: List[Any]
    ) -> Dict[str, Any]:
        targets = self.prioritize_targets(battlefield)
        cards: List[Card] = [
            card for card in hand if (
                (isinstance(card, CreatureCard) or
                 isinstance(card, SpellCard)) and
                card.cost < 5
            )
        ]
        if not cards:
            if len(cards) >= 5:
                cards = sample(hand, 5)
            else:
                cards = sample(hand, len(cards))
        mana_used = sum([card.cost for card in cards])
        damage = 0
        for card in cards:
            if hasattr(card, "attack"):
                damage += card.attack
            elif hasattr(card, "effect_type"):
                if card.effect_type == "damage":
                    damage += 3

        return {
            "cards_played": len(cards),
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        targets = available_targets
        return [
            str(target).title() for target in targets if (
                "player" in target or
                "creature" in target
            )
        ]
