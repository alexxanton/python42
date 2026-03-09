from ex4.TournamentCard import TournamentCard
from typing import Any, Dict, List


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: List[TournamentCard] = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card for a tournament"""
        if not isinstance(card, TournamentCard):
            raise ValueError("card must be an instance of TournamentCard")
        self.cards.append(card)
        return card.name

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        card1 = next((c for c in self.cards if c.card_id == card1_id), None)
        card2 = next((c for c in self.cards if c.card_id == card2_id), None)

        if card1 is None or card2 is None:
            raise ValueError("couldn't get 2 cards to create match")

        self.matches += 1
        winner = card1
        loser = card2
        winner.update_wins()
        loser.update_losses()
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted([])
        return [
            f"{c.name} - Rating: {c.raiting} ({c.wins}-{c.losses})"
            for c in sorted_cards
        ]

    def generate_tournament_report(self) -> Dict[str, Any]:
        count = len(self.cards)
        total = sum([c.rating for c in self.cards])

        return {
            "total_cards": count,
            "matches_played": self.matches,
            "avg_rating": total / count if count > 0 else 0.0,
            "platform_status": "active",
        }
