import random


achiev_list = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
]


def gen_player_achievements() -> set:
    achiev_number = random.randint(4, 8)
    player_achiev = random.sample(achiev_list, achiev_number)
    return set(player_achiev)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    alice_set = gen_player_achievements()
    print(f"Player Alice: {alice_set}")
    bob_set = gen_player_achievements()
    print(f"Player Bob: {bob_set}")
    charlie_set = gen_player_achievements()
    print(f"Player Charlie: {charlie_set}")
    dylan_set = gen_player_achievements()
    print(f"Player Dylan: {dylan_set}")
    print()

    print("All distinct achievements: "
          f"{alice_set.union(bob_set, charlie_set, dylan_set)}")
    print()

    print("Common achievements: "
          f"{alice_set.intersection(bob_set, charlie_set, dylan_set)}")
    print()

    print("Only Alice has: "
          f"{alice_set.difference(bob_set, charlie_set, dylan_set)}")
    print("Only Bob has: "
          f"{bob_set.difference(alice_set, charlie_set, dylan_set)}")
    print("Only Charlie has: "
          f"{charlie_set.difference(bob_set, alice_set, dylan_set)}")
    print("Only Dylan has: "
          f"{dylan_set.difference(bob_set, charlie_set, alice_set)}")
    print()

    achiev_set = set(achiev_list)
    print(f"Alice is missing: {achiev_set.difference(alice_set)}")
    print(f"Bob is missing: {achiev_set.difference(bob_set)}")
    print(f"Charlie is missing: {achiev_set.difference(charlie_set)}")
    print(f"Dylan is missing: {achiev_set.difference(dylan_set)}")
