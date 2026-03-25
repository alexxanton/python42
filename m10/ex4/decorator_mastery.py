from functools import wraps
from time import time
from typing import Callable


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        print(f"Casting {func.__name__}")
        end = time()
        print(f"Spell completed in {end - start} seconds")
        return func(*args, **kwargs)
    return wrapper


def power_validator(min_power: int) -> callable:
    pass


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main() -> None:
    print()


if __name__ == "__main__":
    main()
