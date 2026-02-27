from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol, Generator, Tuple, Optional


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
        for stage in self.stages:
            stage.process(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            stage.process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            stage.process(data)


class InputStage:
    def process(self, data: Any) -> Any:
        print(repr(data).replace("'", "\""))
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            pass
        elif isinstance(data, str):
            pass
        else:
            raise TypeError("Error detected in Stage 2: Invalid data format")
        return data


class OutputStage:
    def process(self, data: Any) -> str:
        return ""


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.pipelines[-1].build_pipeline()

    def process_data(self, data: Dict[str, Union[Dict[str, str] | str]]) -> Any:
        try:
            for pipeline in self.pipelines:
                pipeline.process(data[pipeline.pipeline_id])
        except (KeyError, TypeError) as e:
            print("Error:", e)
