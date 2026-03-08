from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Test the tournament platform"""
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...\n")
    tournament = TournamentPlatform()
    tournament.register_card(TournamentCard(name="Fire Dragon",
                                            card_id="dragon_001",
                                            cost=5,
                                            rarity="Rare",
                                            damage=5,
                                            mana=5,
                                            defense=5,
                                            health=5,
                                            combat="melee"))

    tournament.register_card(TournamentCard(name="Ice Wizard",
                                            card_id="wizard_001",
                                            cost=5,
                                            rarity="Rare",
                                            damage=5,
                                            mana=5,
                                            defense=5,
                                            health=5,
                                            combat="melee"))

    tournament.create_match("dragon_001", "wizard_001")


if __name__ == "__main__":
    main()
