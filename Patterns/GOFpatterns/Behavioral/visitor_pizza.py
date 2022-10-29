from abc import ABC, abstractmethod
from typing import List, Union


class OrderItemVisitor(ABC):
    """
    Visitor interface for orders
    """

    @abstractmethod
    def visit(self, item) -> float:
        raise NotImplementedError


class ItemElement(ABC):
    """
    Interface for ordered products
    """

    @abstractmethod
    def accept(self, visitor) -> OrderItemVisitor:
        raise NotImplementedError


class Pizza(ItemElement):
    """
    representation of ordered pizza
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor) -> OrderItemVisitor:
        return visitor.visit(self)


class Coffee(ItemElement):
    """
    representation of ordered coffee
    """

    def __init__(self, name: str, price: float, volume: float):
        self.name = name
        self.price = price  # price for a litre
        self.volume = volume

    def get_price(self) -> float:
        return self.price

    def get_volume(self) -> float:
        return self.volume

    def accept(self, visitor) -> OrderItemVisitor:
        return visitor.visit(self)


class WithoutDiscountVisitor(OrderItemVisitor):
    """
    visitor for counting order sum without discounts
    """

    def visit(self, item: Union[Pizza, Coffee]) -> float:
        if isinstance(item, Pizza):
            return item.get_price()
        elif isinstance(item, Coffee):
            return item.get_price() * item.get_volume()


class OnlyPizzaDiscountVisitor(OrderItemVisitor):
    """
    visitor for counting order sum with discounts only for pizza
    """

    def visit(self, item: Union[Pizza, Coffee]) -> float:
        pizza_discount: float = 0.15
        if isinstance(item, Pizza):
            return item.get_price() * (1 - pizza_discount)
        elif isinstance(item, Coffee):
            return item.get_price() * item.get_volume()


class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    """
    visitor for counting order sum with discounts only for coffee
    """

    def visit(self, item: Union[Pizza, Coffee]) -> float:
        coffee_discount: float = 0.35
        if isinstance(item, Pizza):
            return item.get_price()
        elif isinstance(item, Coffee):
            return item.get_price() * item.get_volume() * (1 - coffee_discount)


class AllDiscountVisitor(OrderItemVisitor):
    """
    visitor for counting order sum with discounts only for coffee
    """

    def visit(self, item: Union[Pizza, Coffee]) -> float:
        pizza_discount = 0.15
        coffee_discount: float = 0.35
        if isinstance(item, Pizza):
            return item.get_price() * (1 - pizza_discount)
        elif isinstance(item, Coffee):
            return item.get_price() * item.get_volume() * (1 - coffee_discount)


class Waiter:
    def __init__(self, discount_calculator: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount_calculator

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount_calculator: OrderItemVisitor) -> None:
        self.discount_calculator = discount_calculator

    def calculate_final_price(self) -> float:
        total = 0
        if self.order:
            for item in self.order:
                total += item.accept(self.discount_calculator)
        return round(total, 2)


if __name__ == "__main__":
    order: List[ItemElement] = [
        Pizza("Margarita", 12.3),
        Coffee("Latte", 5, 0.25),
        Pizza("Four Cheese", 15.5),
        Pizza("Salami", 14.6),
        Coffee("Cappuccino", 4, 0.4),
    ]
    discount_type = WithoutDiscountVisitor()
    waiter = Waiter(discount_type)
    waiter.set_order(order)
    print(f"Order sum without discounts: {waiter.calculate_final_price()}")
    discount_type = OnlyPizzaDiscountVisitor()
    waiter.set_discount(discount_type)
    print(
        f"Order sum with discounts only on pizza: {waiter.calculate_final_price()}"
    )
    discount_type = OnlyCoffeeDiscountVisitor()
    waiter.set_discount(discount_type)
    print(
        f"Order sum with discounts only on coffee: {waiter.calculate_final_price()}"
    )
    discount_type = AllDiscountVisitor()
    waiter.set_discount(discount_type)
    print(f"Order sum with all of discounts: {waiter.calculate_final_price()}")
