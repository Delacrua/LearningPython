from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from random import choice


class OrderType(Enum):
    """
    possible order types
    """

    FOOD = 1
    BUZZ = 2


class EventType(Enum):
    """
    possible order processinf event types
    """

    GET_ORDER = 1
    FINISH_ORDER = 2


class WorkerType(Enum):
    """
    pizzeria worker types
    """

    WAITER = 1
    CHEF = 2
    BARMAN = 3


class Order:
    """
    a class representing orders
    """

    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"Order №{self.id} ({self.type.name})"


class AnyWorker:
    pass


class Mediator(ABC):
    """
    an interface for mediator
    """

    @abstractmethod
    def notify(self, worker: AnyWorker, order: Order, event: EventType):
        raise NotImplementedError

    @abstractmethod
    def add_worker(self, worker: AnyWorker) -> None:
        raise NotImplementedError


class Worker(ABC, AnyWorker):
    """
    interface class for pizzeria workers
    """

    def __init__(self, name: str, mediator: Mediator):
        self.mediator = mediator
        self.name = name
        self.orders = []
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        raise NotImplementedError

    @abstractmethod
    def finish_order(self, order: Order):
        raise NotImplementedError

    @abstractmethod
    def type(self) -> WorkerType:
        raise NotImplementedError

    def get_orders_id(self) -> List[int]:
        return [order.id for order in self.orders]


class Waiter(Worker):
    """
    a class representing waiter
    """

    def __init__(self, name: str, mediator: Mediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Waiter {self.name} took {order}")
        self.mediator.notify(self, order, EventType.GET_ORDER)

    def finish_order(self, order: Order):
        print(f"Waiter {self.name} served {order} to client")
        self.orders.remove(order)

    def type(self) -> WorkerType:
        return WorkerType.WAITER


class Barman(Worker):
    """
    a class representing barman
    """

    def __init__(self, name: str, mediator: Mediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Barman {self.name} took {order}")

    def finish_order(self, order: Order):
        print(f"Barman {self.name} finished making {order} for the client")
        self.mediator.notify(self, order, EventType.FINISH_ORDER)

    def process_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Barman {self.name} is making {order} for the client")
            self.finish_order(order)
        else:
            print(f"Barman {self.name} is sad: no orders for him")

    def type(self) -> WorkerType:
        return WorkerType.BARMAN


class Chef(Worker):
    """
    a class representing chef
    """

    def __init__(self, name: str, mediator: Mediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Chef {self.name} took {order}")

    def finish_order(self, order: Order):
        print(f"Chef {self.name} finished making {order} for the client")
        self.mediator.notify(self, order, EventType.FINISH_ORDER)

    def process_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Chef {self.name} is making {order} for the client")
            self.finish_order(order)
        else:
            print(f"Chef {self.name} is sad: no orders for him")

    def type(self) -> WorkerType:
        return WorkerType.CHEF


class PizzeriaMediator(Mediator):
    """
    a class representing mediator between pizzeria workers
    """

    def __init__(self):
        self.workers = {
            WorkerType.WAITER: [],
            WorkerType.BARMAN: [],
            WorkerType.CHEF: [],
        }

    def notify(self, worker: Worker, order: Order, event: EventType):
        if event is EventType.GET_ORDER and worker.type() is WorkerType.WAITER:
            if order.type is OrderType.FOOD:
                chef: Chef = choice(self.workers[WorkerType.CHEF])
                chef.take_order(order)
            else:
                barman: Barman = choice(self.workers[WorkerType.BARMAN])
                barman.take_order(order)
        elif event is EventType.FINISH_ORDER and worker.type() in (
            WorkerType.BARMAN,
            WorkerType.CHEF,
        ):
            for waiter in self.workers[WorkerType.WAITER]:
                if order.order_id in waiter.get_orders_id():
                    waiter.finish_order(order)
                    break
            else:
                print(f"{order} was not served to the client!")
        else:
            raise NotImplementedError("Stranger things")

    def add_worker(self, worker: Worker) -> None:
        if worker not in self.workers[worker.type()]:
            self.workers[worker.type()].append(worker)

    def remove_worker(self, worker: Worker):
        if worker in self.workers[worker.type()]:
            self.workers[worker.type()].remove(worker)
        if len(self.workers[worker.type()]) == 0:
            print(f"ATTENTION! no {worker.type().name} left in pizzeria!")


if __name__ == "__main__":
    mediator = PizzeriaMediator()
    waiter1 = Waiter("Alex", mediator)
    waiter2 = Waiter("Bob", mediator)
    waiter3 = Waiter("Charles", mediator)
    barman1 = Barman("Anthony", mediator)
    barman2 = Barman("David", mediator)
    chef = Chef("Gordon", mediator)

    orders = [Order(choice([OrderType.FOOD, OrderType.BUZZ])) for _ in range(5)]

    for order in orders:
        print("*" * 30)
        choice([waiter1, waiter2, waiter3]).take_order(order)

    for _ in range(5):
        chef.process_order()

    for _ in range(5):
        choice([barman1, barman2]).process_order()
