#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print("\nInitial set of players:", players)

    all_capitalized = [item.capitalize() for item in players]
    print("\nNew list with all names capitalized", all_capitalized)

    prev_capitalized = [item for item in players if item == item.capitalize()]
    print("\nNew list of capitalized names only:", prev_capitalized)

    scores = {item: random.randint(1, 1000) for item in prev_capitalized}
    print("\nScore dict:", scores)

    average = sum(
        scores[item] for item in prev_capitalized) / len(prev_capitalized)
    print("\nScore average is", round(average, 2))

    scores2 = {item: scores[item] for item in scores if scores[item] > average}
    print("High scores:", scores2)


if __name__ == "__main__":
    main()
