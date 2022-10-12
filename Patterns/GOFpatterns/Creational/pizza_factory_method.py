from enum import Enum
from typing import Union


class PizzaTypes(Enum):
    """
    a Pizza recipy book for factory method
    """
    MARGARITA = 0
    MEXICO = 1
    STELLA = 2


class Pizza:
    """
    basic Pizza class for factory method
    """

    def __init__(self, price: Union[int, float]):
        self._price = price

    def get_price(self) -> Union[int, float]:
        return self._price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaTypes) -> Pizza:
    """
    Factory method for choosing a Pizza factory for the user
    :param pizza_type: given type of Pizza
    :return: Pizza instance
    """
    factory_dict = {
        PizzaTypes.MARGARITA: PizzaMargarita,
        PizzaTypes.MEXICO: PizzaMexico,
        PizzaTypes.STELLA: PizzaStella,
    }
    return factory_dict[pizza_type]()


if __name__ == '__main__':
    for pizza in PizzaTypes:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
