from ex4.TournamentCard import TournamentCard
from typing import Any, Dict, List
from random import sample


class TournamentPlatform:
    """Manages matches between cards"""
    def __init__(self) -> None:
        self.cards: List[TournamentCard] = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card for a tournament"""
        if not isinstance(card, TournamentCard):
            raise ValueError("card must be an instance of TournamentCard")
        if card.card_id in [c.card_id for c in self.cards]:
            raise ValueError("card_id must be unique")
        self.cards.append(card)
        return card.name

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Creates a match and determines what card won"""
        card1 = next((c for c in self.cards if c.card_id == card1_id), None)
        card2 = next((c for c in self.cards if c.card_id == card2_id), None)

        if card1 is None or card2 is None:
            raise ValueError("couldn't get 2 cards to create match")

        winner, loser = sample([card1, card2], 2)
        self.matches += 1
        winner.update_wins()
        loser.update_losses()
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[str]:
        """Sorts by rating and displays the leaderboard in a formatted way"""
        self.cards.sort(reverse=True)
        return [
            f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
            for c in self.cards
        ]

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Generates the tournament report"""
        count = len(self.cards)
        total = sum([c.rating for c in self.cards])

        return {
            "total_cards": count,
            "matches_played": self.matches,
            "avg_rating": total // count if count > 0 else 0.0,
            "platform_status": "active",
        }
