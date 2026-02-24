import sys


def main() -> None:
    """Takes the arguments and converts them to integers to analize them"""
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py",
              "<score1> <score2> ...")
        return

    try:
        scores = [int(num) for num in sys.argv[1:]]
    except ValueError as e:
        print("Error:", e)
        return

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
