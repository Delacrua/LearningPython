from abc import ABC, abstractmethod


class PizzaBaseInterface(ABC):
    """
    decorated object interface
    """

    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(PizzaBaseInterface):
    """
    decorated object class
    """

    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost


class DecoratorInterface(PizzaBaseInterface):
    """
    decorator interface
    """

    @abstractmethod
    def name(self) -> str:
        pass


class PizzaMargarita(DecoratorInterface):
    """
    decorate pizza base as Margarita pizza
    """

    def __init__(self, wrapped: PizzaBaseInterface, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Margarita"

    def cost(self) -> float:
        return self.__cost + self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


class PizzaSalami(DecoratorInterface):
    """
    decorate pizza base as Salami pizza
    """

    def __init__(self, wrapped: PizzaBaseInterface, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Salami"

    def cost(self) -> float:
        return self.__cost + self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


if __name__ == "__main__":

    def print_pizza(pizza: DecoratorInterface) -> None:
        print(f"Pizza '{pizza.name()}' costs {pizza.cost()}")

    pizza_base = PizzaBase(3.4)
    print(f"Pizza base costs {pizza_base.cost()}")
    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)
    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)
