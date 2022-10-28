import copy

from abc import ABC, abstractmethod
from collections import namedtuple
from enum import Enum, auto
from typing import List


PizzaBase = namedtuple("PizzaBase", ["DoughDepth", "DoughType"])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Pizza(Prototype):
    def __init__(
        self,
        name: str,
        dough: PizzaBase = PizzaBase(
            PizzaDoughDepth.THICK, PizzaDoughType.WHEAT
        ),
        sauce: PizzaSauceType = PizzaSauceType.TOMATO,
        topping: list[PizzaTopLevelType] = None,
        cooking_time: int = 15,
    ):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cooking_time = cooking_time  # in minutes

    def __str__(self):
        info: str = (
            f"Pizza name: {self.name} \n"
            f"dough type: {self.dough.DoughDepth.name} & {self.dough.DoughType.name} \n"
            f"sauce type: {self.sauce} \n"
            f"topping: {[topping.name for topping in self.topping]} \n"
            f"cooking time: {self.cooking_time} minutes"
        )
        return info

    def clone(self):
        topping = self.topping.copy() if self.topping is not None else None
        return type(self)(
            self.name,
            self.dough,
            self.sauce,
            self.topping,
            self.cooking_time,
        )


if __name__ == "__main__":
    pizza = Pizza(
        "Margarita",
        topping=[
            PizzaTopLevelType.MOZZARELLA,
            PizzaTopLevelType.MOZZARELLA,
            PizzaTopLevelType.BACON,
        ],
    )
    print(pizza)
    print("# " * 20)
    new_pizza = pizza.clone()
    new_pizza.name = "New_Margarita"
    print(new_pizza)
    print("# " * 20)
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.name = "Salami"
    salami_pizza.dough = PizzaBase(PizzaDoughDepth.THIN, PizzaDoughType.RYE)
    salami_pizza.sauce = PizzaSauceType.BARBEQUE
    salami_pizza.topping = [
        PizzaTopLevelType.MOZZARELLA,
        PizzaTopLevelType.SALAMI,
    ]
    salami_pizza.cooking_time = 10
    print(salami_pizza)
