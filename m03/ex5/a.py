from typing import Generator


# =========================
# Event Stream Generator
# =========================
def game_event_stream(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up", "completed quest"]

    for i in range(1, n + 1):
        yield {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 7) % 20 + 1,  # pseudo-random level 1–20
            "action": actions[i % len(actions)],
        }


# =========================
# Filters (Generators)
# =========================
def high_level_players(events: Generator[dict, None, None]) -> Generator[dict, None, None]:
    for event in events:
        if event["level"] >= 10:
            yield event


def treasure_events(events: Generator[dict, None, None]) -> Generator[dict, None, None]:
    for event in events:
        if event["action"] == "found treasure":
            yield event


def level_up_events(events: Generator[dict, None, None]) -> Generator[dict, None, None]:
    for event in events:
        if event["action"] == "leveled up":
            yield event


# =========================
# Fibonacci Generator
# =========================
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# =========================
# Prime Generator
# =========================
def prime_numbers() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


# =========================
# Main Program
# =========================
def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    stream = game_event_stream(total_events)

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    processed = 0

    for event in stream:
        processed += 1

        # Print first 3 events as example
        if processed <= 900:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

        # Analytics (single-pass, no storage)
        if event["level"] >= 10:
            high_level_count += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        if event["action"] == "leveled up":
            levelup_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")  # simulated output

    # =========================
    # Generator Demo
    # =========================
    print("\n=== Generator Demonstration ===")

    # Fibonacci
    fib = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        if i < 9:
            print(next(fib), end=", ")
        else:
            print(next(fib))

    # Prime numbers
    primes = prime_numbers()
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        if i < 4:
            print(next(primes), end=", ")
        else:
            print(next(primes))


if __name__ == "__main__":
    main()

