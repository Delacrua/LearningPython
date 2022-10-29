from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List, Optional


class OrderType(Enum):
    """
    possible order types
    """

    CAPPUCCINO = 1
    LATTE = 2
    ESPRESSO = 3


class Order:
    """
    a class representing order
    """

    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"order №{self.id} ({self.type.name})"


class Observer(ABC):
    """
    observer interface
    """

    @abstractmethod
    def update(self, order_id: int):
        raise NotImplementedError


class Subject(ABC):
    """
    interface for observed subject
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)


class Barista(Subject):
    """
    a representation class for barista
    """

    def __init__(self):
        super().__init__()
        self.__orders: List[Order] = []
        self.__finished_orders: List[Order] = []

    def take_order(self, order: Order) -> None:
        print(f"Barista took {order}")
        self.__orders.append(order)

    def return_order(self, order_id: int) -> None:
        finished_order = None
        for order in self.__finished_orders:
            if order.id == order_id:
                finished_order = order
                break
        self.__finished_orders.remove(finished_order)
        return finished_order

    def process_order(self):
        if self.__orders:
            order = choice(self.__orders)
            self.__orders.remove(order)
            self.__finished_orders.append(order)
            print(f"Barista finished {order}")
            self.notify(order.id)
        else:
            print("Barista has no tasks")


class Client(Observer):
    """
    a representation class for client
    """

    def __init__(self, name: str, barista: Barista):
        self.__barista = barista
        self.__name = name
        self.order: Optional[Order] = None

    def update(self, order_id: int) -> None:
        """
        method observes finished orders and when finds appropriate
        takes it and detaches from barista updates
        :param order_id: observed order id
        :return: None
        """
        if self.order is not None and order_id == self.order.id:
            print(
                f"Client {self.__name} took {self.__barista.return_order(order_id)}"
            )
            self.__barista.detach(self)

    def make_order(self) -> None:
        """
        method for making an order and attaching to barista updates
        :return: None
        """
        order_type = choice(
            [
                OrderType.LATTE,
                OrderType.ESPRESSO,
                OrderType.CAPPUCCINO,
            ]
        )
        self.order = Order(order_type)
        print(f"Client {self.__name} made {self.order}")
        self.__barista.attach(self)
        self.__barista.take_order(self.order)


if __name__ == "__main__":
    clients_names = ["Alex", "Bob", "Charles", "Anthony", "David"]
    barista = Barista()
    clients = [Client(name, barista) for name in clients_names]
    for client in clients:
        print("*" * 30)
        client.make_order()
    print("*" * 5, "Barista is processing the orders", "*" * 5)
    for _ in range(len(clients) + 1):
        print("*" * 30)
        barista.process_order()
