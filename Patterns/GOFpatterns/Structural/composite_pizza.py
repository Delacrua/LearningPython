from abc import ABC, abstractmethod


class ProductInterface(ABC):
    """
    interface for pizza ingredients
    """

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class Product(ProductInterface):
    """
    a class representation for an ingredient
    """

    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundProduct(ProductInterface):
    """
    a class representation for a combination of ingredients
    """

    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self) -> float:
        total = 0
        for item in self.products:
            total += item.cost()
        return total

    def name(self) -> str:
        return self.__name

    def add_product(self, product: ProductInterface):
        self.products.append(product)

    def remove_product(self, product: ProductInterface):
        if product in self.products:
            self.products.remove(product)

    def clear(self):
        self.products = []


class Pizza(CompoundProduct):
    """
    a representation for pizza
    """

    def cost(self) -> float:
        total = 0
        for item in self.products:
            print(f"Cost of {item.name()} = {item.cost()}")
            total += item.cost()
        print(f"Total pizza {self.name()} ingredients cost {total}")
        return total


if __name__ == "__main__":
    dough = CompoundProduct("dough")
    dough.add_product(Product("Flour", 3))
    dough.add_product(Product("Eggs", 3.3))
    dough.add_product(Product("Salt", 1))
    dough.add_product(Product("Sugar", 0.3))
    dough.add_product(Product("Water", 2))

    sauce = Product("barbeque sauce", 12)

    topping = CompoundProduct("topping")
    topping.add_product(Product("Dor blue", 15))
    topping.add_product(Product("Parmigiano reggiano", 20))
    topping.add_product(Product("Mozzarella", 10))
    topping.add_product(Product("Maasdam", 7))

    pizza = Pizza("Four cheese")
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)

    print(pizza.cost())
