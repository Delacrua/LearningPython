from abc import ABC, abstractmethod
from enum import Enum


class MenuType(Enum):
    """types of menu"""

    VEGAN = 1
    NOT_VEGAN = 2
    MIXED = 3


class MenuInterface(ABC):
    """
    basic menu interface
    """

    @abstractmethod
    def get_name(self):
        raise NotImplementedError


class VeganMenu(MenuInterface):
    def get_name(self):
        return "Vegan menu"


class NonVeganMenu(MenuInterface):
    def get_name(self):
        return "Non-vegan menu"


class MixedMenu(MenuInterface):
    def get_name(self):
        return "Mixed menu"


class ClientInterface(ABC):
    """
    pizzeria client interface
    """

    @abstractmethod
    def request_menu(self, menu: MenuInterface):
        raise NotImplementedError

    @abstractmethod
    def form_order(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def eating_food(self):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError


class Kitchen:
    """
    representation of pizzeria kitchen
    """

    def prepare_food(self):
        print("Cooking ordered food!")

    def call_waiter(self):
        print("Passing cooked food to the waiter")


class Waiter:
    """
    representation of the waiter
    """

    def take_order(self, client: ClientInterface):
        print(f"Waiter took order from client {client.get_name()}")

    def send_to_kitchen(self, kitchen: Kitchen):
        print("Waiter passed order to the kitchen")

    def serve_client(self, client: ClientInterface):
        print(f"Serving the cooked dishes to client {client.get_name()}!")


class PizzeriaFacade:
    """
    the facade interface for the client
    """

    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {
            MenuType.VEGAN: VeganMenu,
            MenuType.NOT_VEGAN: NonVeganMenu,
            MenuType.MIXED: MixedMenu,
        }

    def get_menu(self, type_menu: MenuType) -> MenuInterface:
        return self.menu[type_menu]()

    def take_order(self, client: ClientInterface):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()


class Client(ClientInterface):
    """
    representation of the client
    """

    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu: MenuInterface):
        print(f"Client {self.name} is reading menu '{menu.get_name()}'")

    def form_order(self) -> dict:
        print(f"Client {self.name} makes an order")
        return {}

    def eating_food(self):
        print(f"Client {self.name} starts eating")

    def get_name(self):
        return self.name


if __name__ == "__main__":
    pizzeria = PizzeriaFacade()
    client1 = Client("Alex")
    client2 = Client("Bob")
    client1.request_menu(pizzeria.get_menu(MenuType.MIXED))
    pizzeria.take_order(client1)
    client2.request_menu(pizzeria.get_menu(MenuType.VEGAN))
    pizzeria.take_order(client2)
    client1.eating_food()
    client2.eating_food()
