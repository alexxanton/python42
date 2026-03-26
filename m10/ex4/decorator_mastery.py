from functools import wraps
from time import time, sleep
from typing import Callable, Any, TypeVar, cast


TYPE = TypeVar("TYPE", bound=Callable[..., Any])


def spell_timer(func: TYPE) -> TYPE:
    """Decorator for measuring how much time a function runs for"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper function that times the function execution"""
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return cast(TYPE, wrapper)


def power_validator(min_power: int) -> Callable[[TYPE], TYPE]:
    """Decorator factory that validates if power level is enough"""
    def decorator(func: TYPE) -> TYPE:
        """Decorator for the power validation"""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrapper that checks if the args are present before validating"""
            if not args:
                return "You have no power here"
            power = args[-1]
            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return cast(TYPE, wrapper)
    return decorator


def retry_spell(max_attempts: int) -> Callable[[TYPE], TYPE]:
    """Decorator factory that retries a function if it fails"""
    def decorator(func: TYPE) -> TYPE:
        """Decorator for the function retrying"""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrapper that executes the retrying"""
            tries = 1
            while tries <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... ({tries}/{max_attempts})"
                    )
                tries += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return cast(TYPE, wrapper)
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates mage names"""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell by providing the name and power level"""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Test the different decorators"""
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        """Simulates a spell taking up time"""
        sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)

    print("\nTesting retry spell...")

    @retry_spell(3)
    def failed_spell() -> None:
        """Simulates a failed spell"""
        raise ValueError("Your spell is suppressed by a magic field")

    print(failed_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf the Grey"))
    print(MageGuild.validate_mage_name("koolMage777"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 9))


if __name__ == "__main__":
    main()
