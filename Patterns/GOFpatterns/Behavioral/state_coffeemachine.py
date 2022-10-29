from typing import Dict, Optional
from abc import ABC, abstractmethod
from enum import Enum


class CoffeeState(Enum):
    """
    possible coffee machine states
    """

    IDLE = 0
    CHOOSE = 1
    CAPPUCCINO = 2
    LATTE = 3
    ESPRESSO = 4
    RETURN_CHANGE = 5


class State(ABC):
    """
    interface for states
    """

    @abstractmethod
    def insert_money(self, coffee_machine) -> None:
        raise NotImplementedError

    @abstractmethod
    def return_money(self, coffee_machine) -> None:
        raise NotImplementedError

    @abstractmethod
    def make_coffee(self, coffee_machine) -> None:
        raise NotImplementedError


class IdleState(State):
    """
    class representation for idle state of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        print("Going to coffee choosing state")
        coffee_machine.set_state(CoffeeState.CHOOSE)

    def return_money(self, coffee_machine) -> None:
        print("What money, honey?")

    def make_coffee(self, coffee_machine) -> None:
        print("No money - no honey!")


class ChooseState(State):
    """
    class representation for choosing state of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        print("Have you loaded enough for the chosen coffee?")

    def return_money(self, coffee_machine) -> None:
        print("Choose your coffee, no money back!")

    def make_coffee(self, coffee_machine) -> None:
        if coffee_machine.next_state is None:
            print("Choose type of coffee you want to get")
        else:
            coffee_machine.set_state(coffee_machine.next_state)


class ChangeState(State):
    """
    class representation for change returning of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        self.return_money(coffee_machine)

    def return_money(self, coffee_machine) -> None:
        print(f"{coffee_machine.money} returned")
        coffee_machine.money = 0
        coffee_machine.set_state(CoffeeState.IDLE)

    def make_coffee(self, coffee_machine) -> None:
        self.return_money(coffee_machine)


class CappuccinoState(State):
    """
    class representation for making cappuccino of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def return_money(self, coffee_machine) -> None:
        print("I said no money back!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 32
        water = 0.3
        milk = 0.1
        if coffee_machine.money >= cost:
            if coffee_machine.water >= water and coffee_machine.milk >= milk:
                print("Making a cappuccino")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.RETURN_CHANGE)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print(f"not enough money, cappuccino costs {cost}")


class LatteState(State):
    """
    class representation for making latte of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def return_money(self, coffee_machine) -> None:
        print("I said no money back!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 40
        water = 0.3
        milk = 0.2
        if coffee_machine.money >= cost:
            if coffee_machine.water >= water and coffee_machine.milk >= milk:
                print("Making a latte")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.RETURN_CHANGE)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print(f"not enough money, latte costs {cost}")


class EspressoState(State):
    """
    class representation for making espresso of coffee machine
    """

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def return_money(self, coffee_machine) -> None:
        print("I said no money back!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 25
        water = 0.3
        if coffee_machine.money >= cost:
            if coffee_machine.water >= water:
                print("Making an espresso")
                coffee_machine.water -= water
                coffee_machine.money -= cost
            else:
                print("Not enough ingredients")
            if coffee_machine.money > 0:
                coffee_machine.set_stte(CoffeeState.RETURN_CHANGE)
                coffee_machine.returnmoney()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print(f"not enough money, espresso costs {cost}")


class CoffeeMachine:
    """
    a class representation of state-dependant coffee machine
    """

    def __init__(self, water: float, milk: float):
        self.water: float = water
        self.milk: float = milk
        self.money: int = 0
        self.__states: Dict[CoffeeState, State] = {
            CoffeeState.IDLE: IdleState(),
            CoffeeState.CHOOSE: ChooseState(),
            CoffeeState.CAPPUCCINO: CappuccinoState(),
            CoffeeState.LATTE: LatteState(),
            CoffeeState.ESPRESSO: EspressoState(),
            CoffeeState.RETURN_CHANGE: ChangeState(),
        }
        self.__state: State = self.__states[CoffeeState.IDLE]
        self.next_state: Optional[CoffeeState] = None

    def get_state(self, state: CoffeeState):
        return self.__states[state]

    def set_state(self, state: CoffeeState):
        self.__state = self.__states[state]

    def insert_money(self, money: int) -> None:
        self.money += money
        print(f"Inserted totally: {self.money}")
        self.__state.insert_money(self)

    def cappuccino(self) -> None:
        print("Cappuccino chosen")
        self.next_state = CoffeeState.CAPPUCCINO
        self.__state.make_coffee(self)

    def espresso(self) -> None:
        print("Espresso chosen")
        self.next_state = CoffeeState.ESPRESSO
        self.__state.make_coffee(self)

    def latte(self) -> None:
        print("Latte chosen")
        self.next_state = CoffeeState.LATTE
        self.__state.make_coffee(self)

    def make_coffee(self):
        print("Making chosen coffee")
        self.__state.make_coffee(self)

    def return_money(self):
        self.__state.return_money(self)


if __name__ == "__main__":
    print("*" * 5, "Functionality test", "*" * 5)
    coffee_machine = CoffeeMachine(1.0, 1.0)
    coffee_machine.make_coffee()
    coffee_machine.insert_money(10)
    coffee_machine.insert_money(10)
    coffee_machine.cappuccino()
    coffee_machine.make_coffee()
    coffee_machine.insert_money(20)
    print("*" * 5, "Low ingredients test", "*" * 5)
    coffee_machine = CoffeeMachine(0.1, 0.1)
    coffee_machine.insert_money(100)
    coffee_machine.make_coffee()
    coffee_machine.latte()
    coffee_machine.make_coffee()
