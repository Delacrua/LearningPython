from typing import List


class Memento:
    """
    a memento class that saves current state of pizza ingredients
    """

    def __init__(self, state: List[str]):
        self._state = state

    def get_state(self) -> List[str]:
        return self._state[:]


class Pizza:
    """
    a class representing pizza
    """

    def __init__(self):
        self._state: List[str] = ["Base"]

    def add_ingredient(self, ingredient: str) -> None:
        print(f"Ingredient added to pizza: {ingredient}")
        self._state.append(ingredient)

    def create_memento(self):
        return Memento(self._state[:])

    def set_memento(self, memento: Memento):
        self._state = memento.get_state()

    def __str__(self):
        return f"Current Pizza state: {self._state}"


class Chef:
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        self.pizza_states: List[Memento] = []

    def add_ingredient_to_pizza(self, ingredient: str):
        self.pizza_states.append(self.pizza.create_memento())
        self.pizza.add_ingredient(ingredient)

    def undo_adding_ingredient(self):
        if len(self.pizza_states) == 1:
            self.pizza.set_memento(self.pizza_states[0])
            print("Pizza returned to starting state")
            print(self.pizza)
        else:
            print("Unwinding last change")
            state = self.pizza_states.pop()
            self.pizza.set_memento(state)
            print(self.pizza)


if __name__ == "__main__":
    pizza = Pizza()
    chef = Chef(pizza)
    print(pizza)
    print("*" * 8, "Adding ingredients to pizza", "*" * 8)
    chef.add_ingredient_to_pizza("Sauce")
    chef.add_ingredient_to_pizza("Olives")
    chef.add_ingredient_to_pizza("Salami")
    chef.add_ingredient_to_pizza("Cheese")
    print(pizza)
    print("*" * 8, "Unwinding changes", "*" * 8)
    chef.undo_adding_ingredient()
    chef.undo_adding_ingredient()
    chef.undo_adding_ingredient()
    chef.undo_adding_ingredient()
    print("*" * 8, "Adding new ingredients to pizza", "*" * 8)
    chef.add_ingredient_to_pizza("Sauce")
    chef.add_ingredient_to_pizza("Cheese")
    print(pizza)
