from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Defines a base class for processing"""
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        return f"{result}"


class NumericProcessor(DataProcessor):
    """Process a list of numbers to get their total sum and average"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total: int = sum(data)
        length: int = len(data)
        avg: float = total / length if length > 0 else 0
        result: str = (
            f"Processed {length} numeric values, sum={total}, "
            f"avg={avg:.1f}"
        )
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list) and
            all(isinstance(item, (int, float)) for item in data)
        )


class TextProcessor(DataProcessor):
    """Process text to find out its length and how many words it has"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        chars: int = len(data)
        words: int = len(data.split())
        result: str = f"Processed text: {chars} characters, {words} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """Process a log message to find its category and format it"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        parts: List[str] = data.split(":", 1)
        category: str = parts[0].strip()
        warning: str = category if not category == "ERROR" else "ALERT"
        msg: str = parts[1].strip()
        result: str = f"[{warning}] {category} level detected: {msg}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data


def process_data(classtype: type[DataProcessor], data: Any, name: str) -> None:
    """Interfaces the process of testing out the processors"""
    print(f"\nInitializing {name} Processor...")
    print("Processing data:", repr(data).replace("'", "\""))
    processor: DataProcessor = classtype()
    try:
        result: str = processor.process(data)
    except ValueError as e:
        print("Error:", e)
        return
    print(f"Validation: {'data' if name != 'Log' else 'entry'} verified")
    print("Output:", result)


def polymorphic_demo() -> None:
    """Demonstrates polymorphic adaptability"""
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data: List[Any] = [
        [1, 2, 3],
        "Hello world!",
        "INFO: System ready"
    ]

    print("\n=== Polymorphic Processing Demo ===")
    for i, processor in enumerate(processors):
        try:
            result: str = processor.process(data[i])
        except ValueError as e:
            print("Error:", e)
            continue
        print(f"Result {i + 1}: {result}")


def main() -> None:
    """Executes the polymorphic tests"""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    process_data(NumericProcessor, [1, 2, 3, 4, 5], "Numeric")
    process_data(TextProcessor, "Hello Nexus World", "Text")
    process_data(LogProcessor, "ERROR: Connection timeout", "Log")
    polymorphic_demo()
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
