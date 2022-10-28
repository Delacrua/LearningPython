from abc import ABC, abstractmethod
from typing import List


class Piece:
    pass


class PizzaPiece(Piece):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"pizza piece №{self.number}"


class Iterator(ABC):
    """
    iterator interface
    """

    @abstractmethod
    def next(self) -> Piece:
        raise NotImplementedError

    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError


class PizzaSliceIterator(Iterator):
    """
    an iterator class for pizza
    """

    def __init__(self, pizza: List[PizzaPiece]):
        self._pizza = pizza
        self._index = 0

    def next(self) -> Piece:
        pizza_item = self._pizza[self._index]
        self._index += 1
        return pizza_item

    def has_next(self) -> bool:
        return True if self._index < len(self._pizza) else False


class PizzaAggregate:
    def __init__(self, slices_amount: int = 10):
        self.slices = [
            PizzaPiece(number + 1) for number in range(slices_amount)
        ]
        print(f"Pizza was cut in {slices_amount} slices")

    def slices_amount(self) -> int:
        return len(self.slices)

    def iterator(self) -> Iterator:
        return PizzaSliceIterator(self.slices)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    iterator = pizza.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(f"This is {item}")
