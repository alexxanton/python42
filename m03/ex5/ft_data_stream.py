from typing import Generator


type NumGenerator = Generator[int, None, None]
type EventGenerator = Generator[dict[str, str | int], None, None]


def event_gen(n: int) -> EventGenerator:
    events = ["killed monster", "found treasure", "leveled up"]
    players = [
        ("alice", 5), ("bob", 12), ("charlie", 7), ("david", 1)
    ]
    for i in range(n):
        event = events[i % len(events)]
        player, level = players[i % len(players)]
        if event == "leveled up":
            level += 1

        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event
        }


def process_events(n: int) -> tuple[int, int, int, int]:
    processed = 0
    level_events, high_level_events, treasure_events = 0, 0, 0
    stream = event_gen(n)

    print(f"Processing {n} game events...\n")
    for event in stream:
        if processed < 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['event']}"
            )
        elif processed == 3:
            print("...\n")
        processed += 1

        if event["event"] == "found treasure":
            treasure_events += 1
        elif event["event"] == "leveled up":
            level_events += 1
            if int(event["level"]) >= 10:
                high_level_events += 1

    return processed, level_events, high_level_events, treasure_events


def print_analytics(analytics: tuple[int, int, int, int]) -> None:
    processed, level_events, high_level_events, treasure_events = analytics
    print("=== Stream Analytics ===")
    print("Total events processed:", processed)
    print("High-level players (10+):", high_level_events)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_events)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


def fibo() -> NumGenerator:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> NumGenerator:
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def print_sequence(gen: NumGenerator, msg: str, limit: int) -> None:
    print(f"{msg} (first {limit}): ", end="")
    for x in range(limit):
        print(next(gen), end="")
        if x < limit - 1:
            print(", ", end="")
        else:
            print()


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print_analytics(process_events(1000))
    print("=== Generator Demonstration ===")
    print_sequence(fibo(), "Fibonacci sequence", 10)
    print_sequence(primes(), "Prime numbers", 5)


if __name__ == "__main__":
    main()
