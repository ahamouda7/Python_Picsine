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
            raise Exception("Improper log data")

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
            raise Exception("Improper log data")

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
    def __init__(self) -> None:
        self.registered_processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            handled = False
            for proc in self.registered_processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        if len(self.registered_processors) == 0:
            print("No processor found, no data")
            return

        for proc in self.registered_processors:
            if isinstance(proc, NumericProcessor):
                proc_type = "Numeric"
            if isinstance(proc, TextProcessor):
                proc_type = "Text"
            if isinstance(proc, LogProcessor):
                proc_type = "Log"

            print(
                f"{proc_type} Processor: total {len(proc.data_processed)} "
                f"items processed, remaining {len(proc.str_data_processed)}"
                "on processor"
            )


numeric = NumericProcessor()
text = TextProcessor()
log = LogProcessor()

stream = DataStream()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    stream.register_processor(numeric)
    print()

    data_on_stream = [
        "Hello world",
        [3.14, -1, 2.71],

        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },

            {
                "log_level": "INFO",
                "log_message": "User wil isconnected"
            }
        ],

        42,
        ["Hi", "five"]
    ]
    print(f"Send first batch of data on stream: {data_on_stream}")
    stream.process_stream(data_on_stream)
    print()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(data_on_stream)

    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
        )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()
