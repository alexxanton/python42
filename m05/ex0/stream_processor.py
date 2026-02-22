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
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processes numbers"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("")

        total = sum(data)
        length = len(data)
        avg = total / length
        result = f"Processed {length} numeric values, sum={total}, avg={avg}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list) and
            all(isinstance(item, (int, float)) for item in data)
        )


class TextProcessor(DataProcessor):
    """Processes text"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("")

        chars = len(data)
        words = len(data.split(" "))
        result = f"Processed text: {chars} characters, {words} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


def process_data(classtype: DataProcessor, data: Any, name: str) -> None:
    print(f"\nInitializing {name} Processor...")
    print("Processing data:", repr(data).replace("'", "\""))
    validation = f"{name} {'data' if name != 'Log' else 'entry'}"
    processor = classtype()
    try:
        result = processor.process(data)
    except ValueError:
        print(f"Validation: {validation} invalid")
        return
    print(f"Validation: {validation} verified")
    print(result)


def polymorphic_demo() -> None:
    print("\n=== Polymorphic Processing Demo ===")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    process_data(NumericProcessor, [1, 2, 3, 4, 5], "Numeric")
    process_data(TextProcessor, "Hello Nexus World", "Text")
    process_data(LogProcessor, "", "Log")
    polymorphic_demo()


if __name__ == "__main__":
    main()
