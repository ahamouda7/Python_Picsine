from typing import Any, List, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_processed: List[Any] = []
        self.str_data_processed: List[str] = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        oldest_data = self.str_data_processed.pop(0)
        self.rank += 1
        return (self.rank, oldest_data)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, List):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, List):
            for i in data:
                self.data_processed.append(i)
                i = str(i)
                self.str_data_processed.append(i)
        else:
            self.data_processed.append(data)
            data = str(data)
            self.str_data_processed.append(data)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, List):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, List):
            for i in data:
                self.data_processed.append(i)
                self.str_data_processed.append(i)
        else:
            self.data_processed.append(data)
            self.str_data_processed.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, Dict):
            return True
        elif isinstance(data, List):
            for i in data:
                if not isinstance(i, Dict):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, List):
            for d in data:
                self.data_processed.append(d)
                d = f"{d['log_level']}: {d['log_message']}"
                self.str_data_processed.append(d)
        else:
            self.data_processed.append(data)
            data = f"{data['log_level']}: {data['log_message']}"
            self.str_data_processed.append(data)


class DataStream:
    def __init__(self):
        self.registered_processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc.data_processed)

    def process_stream(self, stream: list[typing.Any]) -> None:
        pass

    def print_processors_stats(self) -> None:
        pass


numeric1 = NumericProcessor()
numeric2 = NumericProcessor()

text1 = TextProcessor()
text2 = TextProcessor()

log1 = LogProcessor()
log2 = LogProcessor()


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")

    print(f"Trying to validate input '42': {numeric1.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric1.validate("Hello")}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric1.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    numeric2.ingest(1)
    numeric2.ingest(2)
    numeric2.ingest(3)
    numeric2.ingest(4)
    numeric2.ingest(5)
    print(f"Processing data: {numeric2.data_processed}")

    print("Extracting 3 values...")
    new_output = numeric2.output()
    print(f"Numeric value {new_output[0]}: {new_output[1]}")
    new_output = numeric2.output()
    print(f"Numeric value {new_output[0]}: {new_output[1]}")
    new_output = numeric2.output()
    print(f"Numeric value {new_output[0]}: {new_output[1]}")

    print()

    print("Testing Text Processor...")

    print(f"Trying to validate input '42': {text1.validate(42)}")

    text2.ingest("Hello")
    text2.ingest("Nexus")
    text2.ingest("World")
    print(f"Processing data: {text2.data_processed}")

    print("Extracting 1 values...")
    new_output = text2.output()
    print(f"Text value {new_output[0]}: {new_output[1]}")

    print()

    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {log1.validate("Hello")}")

    log2.ingest({"log_level": "NOTICE", "log_message": "Connection to server"})
    log2.ingest({"log_level": "ERROR", "log_message": "Unauthorized access!!"})
    print(f"Processing data: {log2.data_processed}")

    print("Extracting 2 entries...")
    new_output = log2.output()
    print(f"Log entry {new_output[0]}: {new_output[1]}")
    new_output = log2.output()
    print(f"Log entry {new_output[0]}: {new_output[1]}")
