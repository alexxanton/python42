from ex4.TournamentCard import TournamentCard
from typing import Any, Dict


class TournamentPlatform:
    def register_card(self, card: TournamentCard) -> str:
        return ""

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        return {}

    def get_leaderboard(self) -> list:
        return []

    def generate_tournament_report(self) -> Dict[str, Any]:
        return {}
