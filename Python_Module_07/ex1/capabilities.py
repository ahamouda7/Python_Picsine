from abc import ABC, abstractmethod
from ..ex0.normal import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        pass


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a large amount"


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, cr_type: str) -> None:
        Creature.__init__(self, name, cr_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, cr_type: str) -> None:
        Creature.__init__(self, name, cr_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling

    def create_evolved(self) -> Bloomelle:
        return Bloomelle


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling

    def create_evolved(self) -> Morphagon:
        return Morphagon
