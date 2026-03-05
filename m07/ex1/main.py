from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    try:
        deck = Deck()
        effect = "Permanent: +1 mana per turn"
        deck.add_card(CreatureCard("Fire Dragon", 1, "Legendary", 1, 1))
        deck.add_card(ArtifactCard("Mana Crystal", 1, "Normal", 1, effect))
        deck.add_card(SpellCard("Lightning Bolt", 1, "Normal", "type"))
    except ValueError:
        return
    print(deck.get_deck_stats())
    print("\nDrawing and playing cards:")

    game_state = {}
    for i in range(len(deck.cards)):
        card = deck.draw_card()
        print(f"\nDrew: {card.name} ({card.card_type})")
        print("Play result:", card.play(game_state))

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
