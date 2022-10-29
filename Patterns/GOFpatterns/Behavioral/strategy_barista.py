from abc import ABC, abstractmethod
from enum import Enum


class ChefMoodTypes(Enum):
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3


class Strategy(ABC):
    """
    strategy interface
    """

    @abstractmethod
    def check_chef_mood(self, mood: ChefMoodTypes) -> bool:
        raise NotImplementedError

    @abstractmethod
    def process_order(self, money: int) -> str:
        raise NotImplementedError


class GoodStrategy(Strategy):
    """
    representation of a good strategy
    """

    def check_chef_mood(self, mood: ChefMoodTypes) -> bool:
        if mood in (ChefMoodTypes.GOOD, ChefMoodTypes.BAD):
            return True
        return False

    def process_order(self, money: int) -> str:
        return "Make best drink ever!"


class BadStrategy(Strategy):
    """
    representation of a bad strategy
    """

    def check_chef_mood(self, mood: ChefMoodTypes) -> bool:
        if mood in (ChefMoodTypes.BAD, ChefMoodTypes.BETTER_STAY_AWAY):
            return True
        return False

    def process_order(self, money: int) -> str:
        return "Praise God for this glass of water"


class NormalStrategy(Strategy):
    """
    representation of a normal strategy
    """

    def check_chef_mood(self, mood: ChefMoodTypes) -> bool:
        return True

    def process_order(self, money: int) -> str:
        if money < 5:
            return "Refuse client's order"
        elif money < 10:
            return "Make an espresso"
        elif money < 20:
            return "Make a cappuccino"
        elif money < 50:
            return "Make wonderful coffee"
        else:
            return "Make best drink ever!"


class Barista:
    """
    a representation for barista
    """

    def __init__(self, strategy: Strategy, chef_mood: ChefMoodTypes):
        self._strategy = strategy
        self._chef_mood = chef_mood
        print(f"Chef's initial mood: {chef_mood.name}")

    def get_chef_mood(self) -> ChefMoodTypes:
        return self._chef_mood

    def set_chef_mood(self, chef_mood: ChefMoodTypes) -> None:
        print(f"Chef's mood changed to {chef_mood.name}")
        self._chef_mood = chef_mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f"Client pays {money} for his order")
        if self._strategy.check_chef_mood(self._chef_mood):
            print(self._strategy.process_order(money))
        else:
            print("Who are you? What do you want from me?")


if __name__ == "__main__":
    barista = Barista(NormalStrategy(), ChefMoodTypes.BETTER_STAY_AWAY)
    barista.take_order(20)
    barista.take_order(50)
    barista.set_strategy(BadStrategy())
    barista.take_order(40)
    barista.take_order(200)
    barista.set_strategy(GoodStrategy())
    barista.take_order(40)
    barista.set_chef_mood(ChefMoodTypes.GOOD)
    barista.take_order(0)
