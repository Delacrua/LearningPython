from collections import namedtuple
from enum import Enum, auto

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


class Pizza:
    def __init__(self, builder):
        self.name = builder.name
        self.dough = builder.dough
        self.sauce = builder.sauce
        self.topping = builder.topping
        self.cooking_time = builder.cooking_time  # in minutes

    def __str__(self):
        info: str = (
            f"Pizza name: {self.name} \n"
            f"dough type: {self.dough.DoughDepth.name} & {self.dough.DoughType.name} \n"
            f"sauce type: {self.sauce} \n"
            f"topping: {[topping.name for topping in self.topping]} \n"
            f"cooking time: {self.cooking_time} minutes"
        )
        return info


class Builder:
    def set_name(self, name: str):
        self.name = name

    def set_dough(self, pizza_base: PizzaBase):
        self.dough = pizza_base

    def set_sauce(self, pizza_sauce: PizzaSauceType):
        self.sauce = pizza_sauce

    def set_topping(self, topping: list):
        self.topping = topping

    def set_cooking_time(self, time: int):
        self.cooking_time = time

    def build(self):
        return Pizza(self)


if __name__ == "__main__":
    builder = Builder()
    builder.set_name("Margarita")
    builder.set_dough(PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT))
    builder.set_sauce(PizzaSauceType.TOMATO)
    builder.set_topping(
        [
            topping
            for topping in (
                PizzaTopLevelType.MOZZARELLA,
                PizzaTopLevelType.MOZZARELLA,
                PizzaTopLevelType.BACON,
            )
        ]
    )
    builder.set_cooking_time(15)
    pizza = builder.build()
    print(pizza)
