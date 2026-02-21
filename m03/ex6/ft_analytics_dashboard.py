def list_example(data: dict) -> None:
    players = data["players"]
    scores = [name for name in players if players[name]["score"] > 2000]
    doubled = [players[name]["score"] * 2 for name in players]
    active = {name for name in players if players[name]["active"]}
    print("\n=== List Comprehension Examples ===")
    print("High scorers (>2000):", scores)
    print("Scores doubled:", doubled)
    print("Active players:", sorted(active))


def dict_examples(data: dict) -> None:
    players = data["players"]
    scores = {name: players[name]["score"] for name in players}
    count = {name: len(players[name]["achievements"]) for name in players}
    categories = {
        category: len(
            [
                p for p in players if
                (category == "high" and players[p]["score"] > 2000) or
                (category == "medium" and players[p]["score"] == 2000) or
                (category == "low" and players[p]["score"] < 2000)
            ]
        )
        for category in ["high", "medium", "low"]
    }
    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", scores)
    print("Score categories:", categories)
    print("Achievement counts:", count)


def set_examples(data: dict) -> None:
    players = data["players"]
    names = {name for name in players}
    achievements = {ach for p in players for ach in players[p]["achievements"]}
    regions = {players[p]["region"] for p in players}
    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", names)
    print("Unique achievements:", achievements)
    print("Active regions:", regions)


def combined_analysis(data: dict) -> None:
    players = data["players"]
    achievements = {ach for p in players for ach in players[p]["achievements"]}
    scores = [players[name]["score"] for name in players]
    score_avg = sum(scores) / len(scores)
    scores_dict = {name: players[name]["score"] for name in players}
    top = max(scores_dict, key=scores_dict.get)
    print("\n=== Combined Analysis ===")
    print("Total players:", len(players))
    print("Total unique achievements:", len(achievements))
    print(f"Average score: {score_avg:.1f}")
    print(
        f"Top performer: {top} ({players[top]['score']} points, "
        f"{len(players[top]['achievements'])} achievements)"
    )


def main() -> None:
    data = {
        "players": {
            "alice": {
                "score": 2300,
                "achievements": [
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "sharpshooter",
                    "veteran",
                ],
                "active": True,
                "region": "north",
            },
            "bob": {
                "score": 1800,
                "achievements": [
                    "first_kill",
                    "level_5",
                    "explorer",
                ],
                "active": True,
                "region": "east",
            },
            "charlie": {
                "score": 2150,
                "achievements": [
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "strategist",
                    "collector",
                    "veteran",
                    "champion",
                ],
                "active": True,
                "region": "central",
            },
            "diana": {
                "score": 2050,
                "achievements": [
                    "level_5",
                    "explorer",
                    "collector",
                ],
                "active": False,
                "region": "north",
            },
        }
    }
    print("=== Game Analytics Dashboard ===")
    list_example(data)
    dict_examples(data)
    set_examples(data)
    combined_analysis(data)


if __name__ == "__main__":
    main()


    #categories = {
    #    category: len([players[p] for p in players if
    #        (category == "high" and players[p]["score"] > 2000) or
    #        (category == "medium" and 1800 <= players[p]["score"] <= 2000) or
    #        (category == "low" and players[p]["score"] < 1800)])
    #    for category in ["high", "medium", "low"]
    #}
