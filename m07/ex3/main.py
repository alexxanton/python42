from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    """Test the game engine"""
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    try:
        engine = GameEngine()
        engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())
        print("Actions:", engine.simulate_turn())
        print("\nGame Report:")
        print(engine.get_engine_status())
        print(
            "\nAbstract Factory + Strategy Pattern: "
            "Maximum flexibility achieved!"
        )
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
