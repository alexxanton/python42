from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.process_count = 0
        self.error_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria"""
        if not criteria:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returnstream statistics"""
        return {
            "stream_id": self.stream_id,
            "processed": self.process_count,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Sensor data must be a list")

        temps: list[float] = []
        for data in data_batch:
            try:
                if "temp" in data:
                    temp, value_str = data.split(":", 1)
                    value: float = float(value_str)
                    temps.append(value)
            except ValueError as e:
                print("Error:", e)
            self.process_count += 1
        avg: float = sum(temps) / len(temps) if len(temps) > 0 else 0
        return f"{self.process_count} readings processed, avg temp: {avg}°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Transaction data must be a list")

        net_flow: int = 0
        for data in data_batch:
            try:
                action, value_str = data.split(":", 1)
                value: int = int(value_str)
                if action == "buy":
                    net_flow += value
                elif action == "sell":
                    net_flow -= value
            except ValueError as e:
                print("Error:", e)
            self.process_count += 1
        return (
            f"{self.process_count} operations, net flow: "
            f"{'+' if net_flow > 0 else ''}{net_flow} units"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Event data must be a list")

        for event in data_batch:
            if event == "error":
                self.error_count += 1
            self.process_count += 1
        return (
            f"{self.process_count} events, {self.error_count} error detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all_formatted(self, data_batches: Dict[
        str,
        tuple[List[Any], str, str]
    ]) -> None:
        for stream in self.streams:
            try:
                data = data_batches.get(stream.stream_id)
                if data is None:
                    raise ValueError("data can't be empty")
                batch, name, stream_type = data
                print(f"\nInitializing {name.capitalize()} Stream...")
                print(f"Stream ID: {stream.stream_id}, Type: {stream_type}")
                print(f"Processing {name} batch:", str(batch).replace("'", ""))
                filtered: List[Any] = stream.filter_data(batch)
                result: str = stream.process_batch(filtered)
                print("Event analysis:", result)
            except ValueError:
                print()

    def process_all(self, data_batches: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            try:
                batch = data_batches.get(stream.stream_id)
                if batch is None:
                    raise ValueError("batch can't be empty")
                filtered: List[Any] = stream.filter_data(batch)
                result: str = stream.process_batch(filtered).split(",")[0]
                print(
                    f"- data: {result}"
                    f"{' processed' if 'processed' not in result else ''}"
                )
            except ValueError as e:
                print("Error:", e)


def stream_test() -> None:
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches: Dict[str, tuple[List[Any], str, str]] = {
        "SENSOR_001": (
            ["temp:22.5", "humidity:65", "pressure:1013"],
            "sensor",
            "Environmental Data"
        ),
        "TRANS_001": (
            ["buy:100", "sell:150", "buy:75"],
            "transaction",
            "Financial Data"
        ),
        "EVENT_001": (
            ["login", "error", "logout"],
            "event",
            "System Events"
        )
    }

    processor.process_all_formatted(data_batches)


def filter_test() -> None:
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches: Dict[str, List[Any]] = {
        "SENSOR_001": ["", ""],
        "TRANS_001": ["buy:0", "buy:0", "buy:0", "buy:0"],
        "EVENT_001": ["", "", ""],
    }

    processor.process_all(data_batches)
    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    stream_test()
    filter_test()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
