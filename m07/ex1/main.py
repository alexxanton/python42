from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    try:
        deck = Deck()
        effect = "+1 mana per turn"
        deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 1, 1))
        deck.add_card(ArtifactCard("Mana Crystal", 2, "Normal", -1, effect))
        deck.add_card(SpellCard("Lightning Bolt", 3, "Normal", "damage"))
    except ValueError as e:
        print("Error:", e)
        return
    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:")

    game_state = {"mana": 10}
    for _ in range(len(deck.cards)):
        try:
            card = deck.draw_card()
            print(f"\nDrew: {card.name} ({card.card_type})")
            game_state.update(card.play(game_state))
            print("Play result:", game_state)
        except Exception as e:
            print("Error:", e)

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
