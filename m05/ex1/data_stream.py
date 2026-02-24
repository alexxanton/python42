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
        return "3 readings processed, avg temp: 22.5°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Transaction data must be a list")
        return "3 operations, net flow: +25 units"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Event data must be a list")
        return "3 events, 1 error detected"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batches: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            print("\nInitializing Stream...")
            print("Stream ID:", stream.stream_id)
            try:
                batch: List[Any] = data_batches.get(stream.stream_id)
                print("Processing batch:", str(batch).replace("'", ""))
                filtered: List[Any] = stream.filter_data(batch)
                result: str = stream.process_batch(filtered)
                print("Event analysis:", result)
            except ValueError:
                print()


def stream_test() -> None:
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:22.5", "humidity:65", "pressure:1013"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75"],
        "EVENT_001": ["login", "error", "logout"]
    }

    processor.process_all(data_batches)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    stream_test()


if __name__ == "__main__":
    main()
