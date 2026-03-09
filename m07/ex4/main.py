from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def print_rank_info(card: TournamentCard) -> None:
    """Display card rank  info"""
    info = card.get_rank_info()
    print(f"\n{card.name} (ID: {card.card_id}):")
    print("- Interfaces:", str(info["interfaces"]).replace("'", ""))
    print("- Rating:", info["rating"])
    print("- Record:", info["record"])


def main() -> None:
    """Test the tournament platform"""
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")
    try:
        tournament = TournamentPlatform()
        card1 = TournamentCard("Fire Dragon", "dragon_001", 5, "Rare")
        card2 = TournamentCard("Ice Wizard", "wizard_001", 5, "Rare")

        tournament.register_card(card1)
        tournament.register_card(card2)

        print_rank_info(card1)
        print_rank_info(card2)
        print("\nCreating tournament match...")
        print(tournament.create_match("dragon_001", "wizard_001"))

        print("Tournament Leaderboard:")
        print(tournament.get_leaderboard())

        print("\nPlatform Report:")
        print(tournament.generate_tournament_report())
    except ValueError as e:
        print("Error:", e)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
