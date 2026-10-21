#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "First Steps",
        "Master Explorer",
        "Boss Slayer",
        "Speed Runner",
        "Crafting Genius",
        "World Savior",
        "Strategist",
        "Survivor",
        "Treasure Hunter",
        "Unstoppable",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Hidden Path Finder",
        "Legendary Warrior",
        "Dungeon Conqueror",
        "Treasure Collector",
        "Perfect Timing",
        "Combo Master",
        "Ultimate Champion"]
    number = random.randint(5, 15)
    selected_list = random.sample(achievements, number)
    player_achievement = set(selected_list)
    return player_achievement


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("\nPlayer Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    all_achievements = set.union(alice, bob, charlie, dylan)
    print("\nAll distinct achievements:", all_achievements)

    common_achievements = set.intersection(alice, bob, charlie, dylan)
    print("\nCommon achievements:", common_achievements)

    print("\nOnly Alice has:", set.difference(alice, bob, charlie, dylan))
    print("Only Bob has:", set.difference(bob, alice, charlie, dylan))
    print("Only Charlie has:", set.difference(charlie, alice, bob, dylan))
    print("Only Dylan has:", set.difference(dylan, alice, bob, charlie))

    print("\nAlice is missing: ", set.difference(all_achievements, alice))
    print("\nBob is missing: ", set.difference(all_achievements, bob))
    print("\nCharlie is missing: ", set.difference(all_achievements, charlie))
    print("\nDylan is missing: ", set.difference(all_achievements, dylan))


if __name__ == "__main__":
    main()
