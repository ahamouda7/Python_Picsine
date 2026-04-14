from ex0 import FlameFactory, AquaFactory
from ex0.normal import CreatureFactory


def verify_creature(factory: CreatureFactory) -> None:
    factory_base_class = factory.create_base()
    factory_evolved_class = factory.create_evolved()

    if isinstance(factory, FlameFactory):
        factory_base = factory_base_class("Flameling", "Fire")
        factory_evolved = factory_evolved_class("Pyrodon", "Fire/Flying")
    else:
        factory_base = factory_base_class("Aquabub", "Water")
        factory_evolved = factory_evolved_class("Torragon", "Water")

    print(factory_base.describe())
    print(factory_base.attack())
    print(factory_evolved.describe())
    print(factory_evolved.attack())
    print()


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    flameling_class = factory1.create_base()
    factory1_base = flameling_class("Flameling", "Fire")

    aquabub_class = factory2.create_base()
    factory2_base = aquabub_class("Aquabub", "Water")

    print(factory1_base.describe())
    print(" vs.")
    print(factory2_base.describe())
    print(" fight!")
    print(factory1_base.attack())
    print(factory2_base.attack())


flame = FlameFactory()
aqua = AquaFactory()


if __name__ == "__main__":
    print("Testing factory")
    verify_creature(flame)

    print("Testing factory")
    verify_creature(aqua)

    print("Testing battle")
    fight(flame, aqua)
