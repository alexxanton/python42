from ex3.FantasyCardFactory import FantasyCardFactory
from pprint import pprint


def main() -> None:
    """Test the game engine"""
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    factory.create_themed_deck(50)
    pprint(factory.get_supported_types())


if __name__ == "__main__":
    main()
