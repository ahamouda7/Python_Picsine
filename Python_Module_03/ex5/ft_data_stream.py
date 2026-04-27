import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Bob", "Alice", "Dylan", "Charlie"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]
    while True:
        yield random.choice(players), random.choice(actions)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events_list = []
    for i in range(10):
        event = next(gen)
        events_list.append(event)
    print(f"Built list of 10 events: {events_list}")

    events_list_copy = events_list.copy()
    for event in events_list_copy:
        print(f"Got event from list: {event}")
        events_list.remove(event)
        print(f"Remains in list: {events_list}")
