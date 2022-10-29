from abc import ABC, abstractmethod
from typing import List


class Pizza:
    """
    representation of a pizza
    """

    def __init__(self):
        self.__state: List[str] = ["Base"]

    def add_ingredient(self, ingredient: str) -> None:
        print(f"New ingredient added to pizza: {ingredient}")
        self.__state.append(ingredient)

    def __str__(self):
        return f"Pizza ingredients: {self.__state}"


class PizzaMaker(ABC):
    """
    an interface for a template
    """

    def make_pizza(self, pizza: Pizza) -> None:
        self.prepare_sauce(pizza)
        self.prepare_topping(pizza)
        self.cook(pizza)

    @abstractmethod
    def prepare_sauce(self, pizza: Pizza) -> None:
        raise NotImplementedError

    @abstractmethod
    def prepare_topping(self, pizza: Pizza) -> None:
        raise NotImplementedError

    @abstractmethod
    def cook(self, pizza: Pizza) -> None:
        raise NotImplementedError


class MargaritaMaker(PizzaMaker):
    """
    a representation of margarita pizza cooking process
    """

    def prepare_sauce(self, pizza: Pizza) -> None:
        pizza.add_ingredient("Tomato sauce")

    def prepare_topping(self, pizza: Pizza) -> None:
        pizza.add_ingredient("Bacon")
        pizza.add_ingredient("Mozzarella")
        pizza.add_ingredient("Mozzarella")

    def cook(self, pizza: Pizza) -> None:
        print("Margarita pizza is going to be ready in 10 minutes")


class SalamiMaker(PizzaMaker):
    """
    a representation of salami pizza cooking process
    """

    def prepare_sauce(self, pizza: Pizza) -> None:
        pizza.add_ingredient("Pesto sauce")

    def prepare_topping(self, pizza: Pizza) -> None:
        pizza.add_ingredient("Salami")
        pizza.add_ingredient("Salami")
        pizza.add_ingredient("Mozzarella")

    def cook(self, pizza: Pizza) -> None:
        print("Salami pizza is going to be ready in 15 minutes")


class Chef:
    """
    a chef representation class
    """

    def __init__(self, template_pizza: PizzaMaker):
        self.__cooking_process = template_pizza

    def set_cook_template(self, template_pizza: PizzaMaker):
        self.__cooking_process = template_pizza

    def make_pizza(self) -> Pizza:
        pizza = Pizza()
        self.__cooking_process.make_pizza(pizza)
        return pizza


if __name__ == "__main__":
    chef = Chef(MargaritaMaker())
    print("*" * 8, "Making a margarita pizza", "*" * 8)
    chef.make_pizza()
    print("*" * 8, "Making a salami pizza", "*" * 8)
    chef.set_cook_template(SalamiMaker())
    chef.make_pizza()
