from abc import ABC, abstractmethod
import time


class Pizza:
    """
    a representation class for pizza
    """

    def __init__(self, name: str, cooking_time: int, temperature: int):
        self.name = name
        self.cooking_time = cooking_time
        self.cooking_temperature = temperature
        self.__is_cooked = False

    def cook(self) -> None:
        self.__is_cooked = True

    def is_cooked(self) -> bool:
        return self.__is_cooked


class OvenInterface(ABC):
    """
    Interface for various ovens
    """

    @abstractmethod
    def warm_up(self, temperature: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def cool_down(self, temperature: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def cook_pizza(self, pizza: Pizza) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_temperature(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_oven_type(self) -> str:
        raise NotImplementedError


class ClassicOven(OvenInterface):
    """
    a representation of a classic oven on wood
    """

    def __init__(self, temperature: int = 0):
        self.temperature = temperature
        self.type = "ClassicOven"

    def warm_up(self, temperature: int) -> None:
        time.sleep((temperature - self.temperature) / 40)
        print(f"Warmed up from {self.temperature} to {temperature}")
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        time.sleep((self.temperature - temperature) / 20)
        print(f"Cooled down from {self.temperature} to {temperature}")
        self.temperature = temperature

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cooking_time / 10)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature


class ElectricalOven(OvenInterface):
    """
    a representation of a modern oven on electricity
    """

    def __init__(self, temperature: int = 0):
        self.temperature = temperature
        self.type = "ElectricalOven"

    def warm_up(self, temperature: int) -> None:
        time.sleep((temperature - self.temperature) / 100)
        print(f"Warmed up from {self.temperature} to {temperature}")
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        time.sleep((self.temperature - temperature) / 50)
        print(f"Cooled down from {self.temperature} to {temperature}")
        self.temperature = temperature

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cooking_time / 10)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature


class Kitchen:
    """
    a representation of kitchen with different ovens
    """

    def __init__(self, oven: OvenInterface):
        self.__oven = oven

    def __prepare_oven(self, temperature: int):
        if self.__oven.get_temperature() > temperature:
            self.__oven.cool_down(temperature)
        elif self.__oven.get_temperature() < temperature:
            self.__oven.warm_up(temperature)
        else:
            print("Ideal temperature")
        print("Oven prepared")

    def cook_pizza(self, pizza: Pizza) -> None:
        self.__prepare_oven(pizza.cooking_temperature)
        print(
            f"Cooking {pizza.name} for {pizza.cooking_time} minutes"
            f" at {pizza.cooking_temperature} C"
        )
        self.__oven.cook_pizza(pizza)
        if pizza.is_cooked():
            print("Pizza is ready")
        else:
            print("Something went wrong")
        print("-" * 30)

    def change_oven(self, oven: OvenInterface) -> None:
        self.__oven = oven
        print("Oven changed")

    def get_temperature(self) -> int:
        return self.__oven.get_temperature()

    def get_oven_type(self) -> str:
        return self.__oven.get_oven_type()


if __name__ == "__main__":
    first_pizza = Pizza("Margarita", 10, 220)
    second_pizza = Pizza("Salami", 9, 180)

    oven = ClassicOven()
    kitchen = Kitchen(oven)
    print(f"Oven type used: {kitchen.get_oven_type()}")
    kitchen.cook_pizza(first_pizza)
    kitchen.cook_pizza(second_pizza)

    new_oven = ElectricalOven(oven.get_temperature())
    kitchen.change_oven(new_oven)
    print(f"Oven type used: {kitchen.get_oven_type()}")
    first_pizza = Pizza("Margarita", 9, 225)
    second_pizza = Pizza("Salami", 8, 185)
    kitchen.cook_pizza(first_pizza)
    kitchen.cook_pizza(second_pizza)
