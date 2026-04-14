from abc import ABC, abstractmethod
from ex0.normal import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, cr: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, cr: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, cr: Creature) -> None:
        if not self.is_valid(cr):
            raise Exception(
                f"Invalid Creature '{cr.name}' for this aggressive strategy"
                )

    def is_valid(self, cr: Creature) -> bool:
        if not isinstance(cr, TransformCapability | HealCapability):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, cr: Creature) -> None:
        if not self.is_valid(cr):
            raise Exception(
                f"Invalid Creature '{cr.name}' for this aggressive strategy"
                )

    def is_valid(self, cr: Creature) -> bool:
        if isinstance(cr, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, cr: Creature) -> None:
        if not self.is_valid(cr):
            raise Exception(
                f"Invalid Creature '{cr.name}' for this aggressive strategy"
                )

    def is_valid(self, cr: Creature) -> bool:
        if isinstance(cr, HealCapability):
            return True
        return False
