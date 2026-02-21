from generated_data import create_dict


def list_example() -> None:
    data = create_dict()
    players = data["players"]
    scores = [name for name in players if players[name]["total_score"] > 2000]
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000):", scores)
    print("Scores doubled:")
    print("Active players:")


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    list_example()


if __name__ == "__main__":
    main()
