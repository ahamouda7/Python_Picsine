from typing import List, Dict


def artifact_sorter(
    artifacts: List[Dict[str, str | int]]
) -> List[Dict[str, str | int]]:
    artifacts = sorted(artifacts, key=lambda p: int(p["power"]), reverse=True)
    return artifacts


def power_filter(
    mages: List[Dict[str, str | int]],
    min_power: int
) -> List[Dict[str, str | int]]:
    mages = list(filter(lambda p: int(p["power"]) >= min_power, mages))
    return mages


def spell_transformer(spells: List[str]) -> List[str]:
    spells = list(map(lambda s: f"* {s} *", spells))
    return spells


def mage_stats(mages: List[Dict[str, str | int]]) -> Dict[str, int | float]:
    powers = list(map(lambda p: int(p["power"]), mages))

    mini = min(powers)
    maxi = max(powers)
    average = round(sum(powers) / len(powers), 2)

    states = {"max_power": maxi, "min_power": mini, "avg_power": average}
    return states


if __name__ == "__main__":
    artifacts_data: List[Dict[str, str | int]] = [
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]
    print("\nTesting artifact sorter...")
    sorted_data = artifact_sorter(artifacts_data)
    first = sorted_data[0]
    second = sorted_data[1]

    print(
        f"{first['name']} ({first['power']} power) "
        f"comes before {second['name']} ({second['power']} power)"
    )

    spells_data = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    spells = spell_transformer(spells_data)
    for s in spells:
        print(s, end=" ")
    print()
