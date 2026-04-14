from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex0.normal import Creature, CreatureFactory, Flameling, Aquabub
from ex1.capabilities import Sproutling
from ex2.strategies import BattleStrategy


flame = FlameFactory()
aqua = AquaFactory()
heal = HealingCreatureFactory()
trans = TransformCreatureFactory()

normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()


def validate_fighter(creature: Creature, strategy: BattleStrategy) -> int:
    try:
        if isinstance(strategy, NormalStrategy):
            normal.act(creature)
        elif isinstance(strategy, AggressiveStrategy):
            aggressive.act(creature)
        else:
            defensive.act(creature)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
        return 0
    return 1


def get_attributes(creature: CreatureFactory) -> Tuple[str, str]:
    if isinstance(creature, FlameFactory):
        return ("Flameling", "Fire")
    elif isinstance(creature, AquaFactory):
        return ("Aquabub", "Water")
    elif isinstance(creature, HealingCreatureFactory):
        return ("Sproutling", "Grass")
    else:
        return ("Shiftling", "Normal")


def attack_strategy(cr_base: Creature) -> None:
    if isinstance(cr_base, Flameling) or isinstance(cr_base, Aquabub):
        print(cr_base.attack())
    elif isinstance(cr_base, Sproutling):
        print(cr_base.attack())
        print(cr_base.heal())
    else:
        print(cr_base.attack())
        print(cr_base.transform())
        print(cr_base.revert())


def battle(creatures: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(creatures)):
        f1 = creatures[i]
        fighter1 = f1[0]
        fighter1_class = fighter1.create_base()
        name, cr_type = get_attributes(fighter1)
        fighter1_base = fighter1_class(name, cr_type)

        for f2 in creatures[(i + 1):]:
            fighter2 = f2[0]
            fighter2_class = fighter2.create_base()
            name, cr_type = get_attributes(fighter2)
            fighter2_base = fighter2_class(name, cr_type)

            print("* Battle *")
            print(fighter1_base.describe())
            print(" vs.")
            print(fighter2_base.describe())

            print(" now fight!")

            fighters = {fighter1_base: f1[1], fighter2_base: f2[1]}
            for (fighter, strategy) in fighters.items():
                if not validate_fighter(fighter, strategy):
                    return

            attack_strategy(fighter1_base)
            attack_strategy(fighter2_base)
            if i < len(creatures) - 2:
                print()


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    lst = [(flame, normal), (heal, defensive)]
    print("*** Tournament ***")
    print(f"{len(lst)} opponents involved")
    print()

    battle(lst)
    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    lst = [(flame, aggressive), (heal, defensive)]
    print("*** Tournament ***")
    print(f"{len(lst)} opponents involved")
    print()

    battle(lst)
    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    lst = [(aqua, normal), (heal, defensive), (trans, aggressive)]
    print("*** Tournament ***")
    print(f"{len(lst)} opponents involved")
    print()

    battle(lst)
