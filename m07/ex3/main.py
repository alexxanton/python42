from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    """Test the game engine"""
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    engine = GameEngine()
    engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())
    engine.simulate_turn()

if __name__ == "__main__":
    main()
