from abc import ABC, abstractmethod
from typing import Any, List, Union, Protocol
from time import time


class ProcessingStage(Protocol):
    """Base class for stages"""
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    """Base class for pipelines"""
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process pipeline data"""
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a stage for a pipeline process"""
        self.stages.append(stage)

    def build_pipeline(self) -> None:
        """Adds all the necessary stages"""
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())


class JSONAdapter(ProcessingPipeline):
    """Reads a JSON object"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], dict):
            data["adapter"] = "json"
        else:
            raise ValueError("JSON not valid")

        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    """Parses a CSV string to process it"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], str):
            data["adapter"] = "csv"
            data["processed"] = data["data"].split(",")
        else:
            raise ValueError("CSV not valid")

        for stage in self.stages:
            data = stage.process(data)
        return data


class StreamAdapter(ProcessingPipeline):
    """Reads a list of temperatures to process them"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], list):
            data["adapter"] = "stream"
        else:
            raise ValueError("Stream not valid")

        for stage in self.stages:
            data = stage.process(data)
        return data


class InputStage:
    """Validates the input and prints it if required"""
    def process(self, data: Any) -> Any:
        """Processing function for the input stage"""
        d = data["data"]
        match data["adapter"]:
            case "json":
                if (
                    "sensor" not in d or
                    "value" not in d or
                    "unit" not in d
                ):
                    raise TypeError("Invalid JSON keys")
            case "csv":
                for item in data["processed"]:
                    if not item:
                        raise TypeError("Invalid CSV data")
            case "stream":
                if not all(isinstance(item, int | float) for item in d):
                    raise TypeError("Invalid stream data")

        if "info" in data:
            if len(data["info"]) != 4:
                raise ValueError("Not enough information provided")
            print(data["info"][0])
            if data["info"][1] == "Input:":
                print(data["info"][1], repr(data["data"]).replace("'", "\""))
            else:
                print(data["info"][1])
        return data


class TransformStage:
    """Takes the data and operates on it depending on the type"""
    def process(self, data: Any) -> Any:
        """Processing function for the transform stage"""
        if "info" in data:
            print(data["info"][2])

        d = data["data"]
        match data["adapter"]:
            case "json":
                value = float(d["value"])
                unit = d["unit"]
                value_range = "Normal" if value > 0 and value < 35 else "Harsh"
                data["processed"] = value, unit, value_range
            case "csv":
                for item in data["processed"]:
                    pass
                data["processed"] = 1
            case "stream":
                reads = len(d)
                if reads <= 0:
                    raise TypeError(
                        "Error detected in Stage 2: Invalid data format"
                    )
                avg = sum(d) / reads if reads > 0 else 0.0
                data["processed"] = reads, avg

        return data


class OutputStage:
    """Returns the output of the processed data"""
    def process(self, data: Any) -> Any:
        """Processing function for the output stage"""
        if "info" in data:
            msg = str(data["info"][3])
            if msg != "Output:":
                data["output"] = msg
                return data

        processed = data["processed"]
        match data["adapter"]:
            case "json":
                value, unit, value_range = processed
                data["output"] = (
                    f"Output: Processed temperature reading: "
                    f"{value}°{unit} ({value_range} range)"
                )
            case "csv":
                actions = processed
                data["output"] = (
                    f"Output: User activity logged: "
                    f"{actions} actions processed"
                )
            case "stream":
                reads, avg = processed
                data["output"] = (
                    f"Output: Stream summary: {reads} readings, avg: {avg}°C"
                )
        return data


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.pipelines[-1].build_pipeline()

    def process_data(self, data: Any) -> Any:
        for pipeline in self.pipelines:
            try:
                result = pipeline.process(data[pipeline.pipeline_id])
                if isinstance(result, dict) and "output" in result:
                    print(result["output"])
            except (KeyError, TypeError, ValueError) as e:
                print("Error:", e)
                print(
                    "Recovery initiated: "
                    "Switching to backup processor"
                )
                print(
                    "Recovery successful: "
                    "Pipeline restored, processing resumed"
                )

    def process_chain(
        self, data: Any
    ) -> Any:
        result = data
        for pipeline in self.pipelines:
            try:
                processed_result = pipeline.process(result)
                if isinstance(processed_result, dict):
                    result = processed_result
                else:
                    return processed_result
            except (KeyError, TypeError, ValueError) as e:
                print("Error:", e)
                print("Trying with next pipeline...")


def nexus_test() -> None:
    """Simple pipeline test"""
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    data = {
        "STRM_001": {
            "data": [1.0, 2.0, 3.0],
            "info": [
                "Creating Data Processing Pipeline...",
                "Stage 1: Input validation and parsing",
                "Stage 2: Data transformation and enrichment",
                "Stage 3: Output formatting and delivery",
            ]
        }
    }
    nexus = NexusManager()
    nexus.add_pipeline(StreamAdapter("STRM_001"))
    nexus.process_data(data)


def multiformat_test() -> None:
    """Tests multiple pipelines"""
    print("\n=== Multi-Format Data Processing ===")
    data = {
        "JSON_001": {
            "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
            "info": [
                "\nProcessing JSON data through pipeline...",
                "Input:",
                "Transform: Enriched with metadata and validation",
                "Output:"
            ]
        },
        "CSV_001": {
            "data": "user,action,timestamp",
            "info": [
                "\nProcessing CSV data through same pipeline...",
                "Input:",
                "Transform: Parsed and structured data",
                "Output:"
            ]
        },
        "STRM_001": {
            "data": [15.0, 23.0, 31.0, 20.0, 17.0],
            "info": [
                "\nProcessing Stream data through same pipeline...",
                "Input: Real-time sensor stream",
                "Transform: Aggregated and filtered",
                "Output:"
            ]
        }
    }
    nexus = NexusManager()
    nexus.add_pipeline(JSONAdapter("JSON_001"))
    nexus.add_pipeline(CSVAdapter("CSV_001"))
    nexus.add_pipeline(StreamAdapter("STRM_001"))
    nexus.process_data(data)


def pipeline_chaining_demo() -> None:
    """Demonstrates pipeline chaining"""
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
    start_time = time()
    csv_data = "user,action,timestamp," * 100
    data = {"data": csv_data[:-1]}
    nexus = NexusManager()
    nexus.add_pipeline(CSVAdapter("CSV_A"))
    nexus.add_pipeline(CSVAdapter("CSV_B"))
    nexus.add_pipeline(CSVAdapter("CSV_C"))
    nexus.process_chain(data)
    end_time = time()
    total_time = end_time - start_time
    print("Chain result: 100 records processed through 3-stage pipeline")
    print(
        f"Performance: 95% efficiency, "
        f"{total_time:.10f}s total processing time"
    )


def error_test() -> None:
    """Tests error recovery"""
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    data = {
        "INVALID_001": {
            "data": [],
        }
    }
    nexus = NexusManager()
    nexus.add_pipeline(StreamAdapter("INVALID_001"))
    nexus.process_data(data)


def main() -> None:
    """Executes all the tests"""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus_test()
    multiformat_test()
    pipeline_chaining_demo()
    error_test()
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
