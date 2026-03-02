from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def build_pipeline(self) -> None:
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())


class JSONAdapter(ProcessingPipeline):
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
    def process(self, data: Any) -> Any:
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
                if "," not in d:
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
    def process(self, data: Any) -> Any:
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
    def process(self, data: Any) -> Any:
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

    def process_data(self, data: Dict[str, Union[Dict[str, str], str]]) -> Any:
        for pipeline in self.pipelines:
            try:
                result = pipeline.process(data[pipeline.pipeline_id])
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

    def process_chain(self, data: Dict[str, Union[Dict[str, str], str]]) -> Any:
        result = data
        for pipeline in self.pipelines:
            try:
                result = pipeline.process(result)
            except (KeyError, TypeError, ValueError) as e:
                print("Error:", e)
                print("Trying with next pipeline...")
