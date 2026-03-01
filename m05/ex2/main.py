from nexus_pipeline import *


def nexus_test() -> None:
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    data = {
        "CSV_001": {
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
    nexus.add_pipeline(StreamAdapter("CSV_001"))
    nexus.process_data(data)


def multiformat_test() -> None:
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
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    data = {"data": "user,action,timestamp"}
    nexus = NexusManager()
    nexus.add_pipeline(CSVAdapter("CSV_A"))
    nexus.add_pipeline(CSVAdapter("CSV_B"))
    nexus.add_pipeline(CSVAdapter("CSV_C"))
    nexus.process_chain(data)


def error_test() -> None:
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
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus_test()
    multiformat_test()
    pipeline_chaining_demo()
    error_test()
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
