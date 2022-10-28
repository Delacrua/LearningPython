from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, TypeVar

T = TypeVar("T")


class EnumOrder(Enum):
    """
    class to describe possible types of orders
    """

    VEGAN = 1
    NOT_VEGAN = 2
    BUZZ = 3
    IMPOSSIBLE = 4


class ClientRequest:
    """
    class to describe client's request
    """

    def __init__(self, description: List[str], order_type: EnumOrder):
        self._description = description
        self._order_type = order_type

    @property
    def order_list(self):
        return self._description

    @property
    def order_type(self):
        return self._order_type


class Handler(ABC):
    """
    interface for request handlers
    """

    def __init__(self, successor: Optional[T] = None):
        self._successor = successor

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor: Optional[T]):
        self._successor = successor

    def handle(self, request: ClientRequest) -> None:
        res = self._check_request(request.order_type)
        if not res and self._successor:
            self._successor.handle(request)

    @abstractmethod
    def _check_request(self, request_type: EnumOrder) -> bool:
        raise NotImplementedError


class WaiterHandler(Handler):
    """
    a class for processing request by waiter
    """

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = (
            request_type in EnumOrder
            and request_type is not EnumOrder.IMPOSSIBLE
        )
        if check:
            print("The waiter accepted request")
        else:
            print("The waiter did not accept request")
        return not check


class BarmanHandler(Handler):
    """
    a class for processing request by barman
    """

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.BUZZ,)
        if check:
            print(
                'Barmen says: "Piece of cake!" \nThe barmen makes requested buzz'
            )
        else:
            print("The barmen finds no buzz in request and is calling the chef")
        return check


class ChefHandler(Handler):
    """
    a class for processing request by chef
    """

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.VEGAN, EnumOrder.NOT_VEGAN)
        if check:
            print('Chef says: "Consider it done!" \nThe chef started cooking')
        else:
            print("The chef is unable to cook the request")
        return check


if __name__ == "__main__":
    # Setting up links of chain
    chef = ChefHandler()
    barman = BarmanHandler()
    waiter = WaiterHandler()
    # building chain of command
    waiter.successor = barman
    barman.successor = chef

    def handle_request(request: ClientRequest):
        print("*" * 10, "Processing request", "*" * 10)
        print(f"Client requests: {request.order_list}")
        waiter.handle(request)

    req_list = ["Pancakes with caviar", "Fried goose"]
    client_req = ClientRequest(req_list, EnumOrder.NOT_VEGAN)
    handle_request(client_req)

    req_list = ["Bloody Mary", "Pina Colada"]
    client_req = ClientRequest(req_list, EnumOrder.BUZZ)
    handle_request(client_req)

    req_list = ["I need your clothes, your boots and your motorcycle"]
    client_req = ClientRequest(req_list, EnumOrder.IMPOSSIBLE)
    handle_request(client_req)
