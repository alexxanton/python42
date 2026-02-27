from nexus_pipeline import *


def nexus_test() -> None:
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    nexus = NexusManager()


def multiformat_test() -> None:
    print("\n=== Multi-Format Data Processing ===\n")
    data = {
        "JSON_001": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "CSV_001": "user,action,timestamp",
        "STRM_001": ""
    }
    messages = {
        "JSON_001": [
            "Processing JSON data through pipeline...",
            "Transform: Enriched with metadata and validation",
            ""
        ],
        "CSV_001": [
            "Processing CSV data through same pipeline...",
            "Transform: Parsed and structured data",
            ""
        ],
        "STRM_001": [
            "Processing Stream data through same pipeline...",
            "Transform: Aggregated and filtered",
            ""
        ]
    }
    nexus = NexusManager()
    nexus.add_pipeline(JSONAdapter("JSON_001"))
    nexus.add_pipeline(CSVAdapter("CSV_001"))
    nexus.add_pipeline(StreamAdapter("STRM_001"))
    nexus.process_data(data)


def pipeline_chaining_demo() -> None:
    print("\n=== Pipeline Chaining Demo ===")


def error_test() -> None:
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    data = {"INVALID_001": 0}
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
