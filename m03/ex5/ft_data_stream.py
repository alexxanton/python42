from typing import Generator


def fibo() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> Generator[int, None, None]:
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


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    fib = fibo()
    for x in range(10):
        print(next(fib), end="")
        if x < 9:
            print(", ", end="")
        else:
            print()
    
    p = primes()
    for x in range(5):
        print(next(p), end="")
        if x < 4:
            print(", ", end="")
        else:
            print()


if __name__ == "__main__":
    main()
