#!/usr/bin/env python3
import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "walk", "train", "moonwalk", "read"]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        selected = events[index]
        events[:] = events[:index] + events[index + 1:]
        yield selected


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for index in range(1000):
        event = next(event_generator)
        print(f"Event {index}: Player {event[0]} did action {event[1]}")

    events_list = []
    for index in range(10):
        events_list += [next(event_generator)]
    print("Built list of 10 events:", events_list)

    for consumed_event in consume_event(events_list):
        print("\nGot event from list:", consumed_event)
        print("Remains in list:", events_list)


if __name__ == "__main__":
    main()
