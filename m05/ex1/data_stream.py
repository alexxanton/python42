from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union, Tuple, Generator


type Gen = Generator[Dict[str, Union[str, int, float]], None, None]


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.process_count = 0
        self.error_count = 0
        self.name = ""
        self.type = ""

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
        """Return stream statistics"""
        return {
            "stream_id": self.stream_id,
            "processed": self.process_count,
            "errors": self.error_count,
            "type": self.type,
            "name": self.name,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "sensor"
        self.type = "Environmental Data"

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
                self.error_count += 1
                print("Error:", e)
            self.process_count += 1
        avg: float = sum(temps) / len(temps) if len(temps) > 0 else 0.0
        return f"{self.process_count} readings processed, avg temp: {avg}°C"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        def isfloat(num: str) -> bool:
            try:
                float(num)
                return True
            except ValueError:
                return False

        if not criteria or not criteria == "temp":
            return data_batch
        filtered: List[Any] = [
            str(item) for item in data_batch if "temp" in item
        ]
        return [
            item for item in filtered if (
                isfloat(item.split(":")[1]) and
                float(item.split(":")[1]) > 35.0
            )
        ]


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "transaction"
        self.type = "Financial Data"

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
                self.error_count += 1
                print("Error:", e)
            self.process_count += 1
        return (
            f"{self.process_count} operations, net flow: "
            f"{'+' if net_flow > 0 else ''}{net_flow} units"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria or criteria != "large":
            return data_batch
        return [
            item for item in data_batch if (
                item.split(":")[1].isnumeric() and
                int(item.split(":")[1]) > 900
            )
        ]


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "event"
        self.type = "System Events"

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

    def validate(self, batch: Any) -> None:
        if batch is None:
            raise ValueError("data can't be empty")

        if not isinstance(batch, tuple):
            raise TypeError("data_batch must be a tuple")

        if (
            len(batch) != 2 or not isinstance(batch[0], list) or
            not isinstance(batch[1], str) or
            not all(isinstance(item, str) for item in batch[0])
        ):
            raise TypeError("invalid data_batch tuple")

    def process_all(
        self,
        data_batches: Dict[str, Tuple[List[Any], str]],
    ) -> Gen:
        for stream in self.streams:
            try:
                batch = data_batches.get(stream.stream_id)
                self.validate(batch)
                filtered: List[Any] = stream.filter_data(*batch)
                result: str = stream.process_batch(filtered)
                stats: Dict[str, Union[str, int, float]] = stream.get_stats()
                stats["result"] = result
                stats["batch"] = str(batch[0]).replace("'", "")
                yield stats
            except (ValueError, TypeError) as e:
                print(f"\nError in {stream.name} Stream")
                print("Error:", e)


def stream_test() -> None:
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches: Dict[str, Tuple[List[Any], str]] = {
        "SENSOR_001": (["temp:22.5", "humidity:65", "pressure:1013"], ""),
        "TRANS_001": (["buy:100", "sell:150", "buy:75"], ""),
        "EVENT_001": (["login", "error", "logout"], "")
    }

    for d in processor.process_all(data_batches):
        print(f"\nInitializing {d['name'].capitalize()} Stream...")
        print(f"Stream ID: {d['stream_id']}, Type: {d['type']}")
        print(f"Processing {d['name']} batch: {d['batch']}")
        print("Event analysis:", d["result"])


def filter_test() -> None:
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches: Dict[str, Tuple[List[Any], str]] = {
        "SENSOR_001": (["temp:1.0", "temp:36.0", "temp:40.0"], "temp"),
        "TRANS_001": (["buy:100", "sell:50", "buy:1200", "sell:30"], "large"),
        "EVENT_001": (["login", "login", "login", "logout", "error"], "login"),
    }

    high_temp = 0
    large_transaction = 0
    for d in processor.process_all(data_batches):
        print(f"- {d['name'].capitalize()} data: {d['processed']} processed")
        if d["stream_id"] == "SENSOR_001":
            high_temp = d["processed"]
        elif d["stream_id"] == "TRANS_001":
            large_transaction = d["processed"]
    print("\nStream filtering active: High-priority data only")
    print(
        f"Filtered results: {high_temp} critical sensor alerts, "
        f"{large_transaction} large transaction"
    )


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    stream_test()
    filter_test()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
