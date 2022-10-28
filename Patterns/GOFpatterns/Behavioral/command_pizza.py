from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    """
    interface for executing commands
    """

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class Stove:
    """
    representation class for kitchen stove
    """

    def prepare_stove(self):
        print("The stove is heating")

    def cook_pizza(self):
        print("The stove is cooking pizza")


class ChefAssistant:
    """
    representation class for chef's assistant
    """

    def prepare_pizza_dough(self):
        print("Chef's assistant prepares pizza dough")

    def prepare_topping(self):
        print("Chef's assistant cuts topping for pizza")

    def prepare_sauce(self):
        print("Chef's assistant makes sauce for pizza")


class Chef:
    """
    representation class for Chef
    """

    def roll_out_dough(self):
        print("Chef rolls out pizza dough")

    def add_sauce(self):
        print("Chef adds pizza sauce")

    def add_topping(self):
        print("Chef adds pizza topping")

    def serve_pizza(self):
        print("Chef makes a serving of pizza")


class PrepareStoveCommand(Command):
    """
    Command class for heating the stove
    """

    def __init__(self, executor: Stove):
        self._executor = executor

    def execute(self) -> None:
        self._executor.prepare_stove()


class CookPizzaCommand(Command):
    """
    Command class for cooking pizza
    """

    def __init__(self, executor: Stove):
        self._executor = executor

    def execute(self) -> None:
        self._executor.cook_pizza()


class PrepareDoughCommand(Command):
    """
    Command class for preparing pizza dough
    """

    def __init__(self, executor: ChefAssistant):
        self._executor = executor

    def execute(self) -> None:
        self._executor.prepare_pizza_dough()


class PrepareToppingCommand(Command):
    """
    Command class for preparing topping
    """

    def __init__(self, executor: ChefAssistant):
        self._executor = executor

    def execute(self) -> None:
        self._executor.prepare_topping()


class PrepareSauceCommand(Command):
    """
    Command class for preparing sauce
    """

    def __init__(self, executor: ChefAssistant):
        self._executor = executor

    def execute(self) -> None:
        self._executor.prepare_sauce()


class RollOutDoughCommand(Command):
    """
    Command class for rolling out pizza dough
    """

    def __init__(self, executor: Chef):
        self._executor = executor

    def execute(self) -> None:
        self._executor.roll_out_dough()


class AddSauceCommand(Command):
    """
    Command class for adding pizza sauce
    """

    def __init__(self, executor: Chef):
        self._executor = executor

    def execute(self) -> None:
        self._executor.add_sauce()


class AddToppingCommand(Command):
    """
    Command class for adding pizza topping
    """

    def __init__(self, executor: Chef):
        self._executor = executor

    def execute(self) -> None:
        self._executor.add_topping()


class ServePizzaCommand(Command):
    """
    Command class for serving the pizza
    """

    def __init__(self, executor: Chef):
        self._executor = executor

    def execute(self) -> None:
        self._executor.serve_pizza()


class Pizzeria:
    """
    aggregation class for all pizza cooking commands
    """

    def __init__(self):
        self.history: List[Command] = []

    def add_command(self, command: Command) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("No tasks set for cooking")
        else:
            for command in self.history:
                command.execute()
            self.history.clear()


if __name__ == "__main__":
    # setting up the actors
    chef = Chef()
    assistant = ChefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # Setting the commands list
    for command, actor in [
        (PrepareStoveCommand, stove),
        (PrepareDoughCommand, assistant),
        (RollOutDoughCommand, chef),
        (PrepareToppingCommand, assistant),
        (AddToppingCommand, chef),
        (PrepareSauceCommand, assistant),
        (AddSauceCommand, chef),
        (CookPizzaCommand, stove),
        (ServePizzaCommand, chef),
    ]:
        pizzeria.add_command(command(actor))

    pizzeria.cook()
