from abc import ABC, abstractmethod


class PizzaOrderFlyWeight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def __repr__(self):
        return str(self.shared_state)


class PizzaOrderContext:
    def __init__(self, unique_state, flyweight: PizzaOrderFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return (
            f"Unique state: {self.unique_state}\nShared state: {self.flyweight}"
        )


class FlyWeightFactory:
    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> PizzaOrderFlyWeight:

        flyweights = list(
            filter(lambda x: x.shared_state == shared_state, self.flyweights)
        )
        if flyweights:
            return flyweights[0]
        else:
            flyweight = PizzaOrderFlyWeight(shared_state)
            self.flyweights.append(flyweight)
            return flyweight

    @property
    def total(self):
        return len(self.flyweights)


class OrderInterface(ABC):
    @abstractmethod
    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        pass


class PizzaOrderMaker(OrderInterface):
    def __init__(self, factory: FlyWeightFactory):
        self.flyweight_factory = factory
        self.contexts = []

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = PizzaOrderContext(unique_state, flyweight)
        self.contexts.append(context)

        return context


class ProxyOrderMaker(OrderInterface):
    def __init__(self, real_subject: PizzaOrderMaker):
        self.__real_subject = real_subject

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        self.__logging(unique_state, shared_state)
        return self.__real_subject.make_pizza_order(unique_state, shared_state)

    def check_access(self) -> bool:
        print("Checking Proxy")
        return self.__real_subject is not None

    def __logging(self, unique_state, shared_state) -> None:
        print(
            f"----Logging order data----\n"
            f"unique state: {unique_state} \n"
            f"shared state: {shared_state}"
        )


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    pizza_maker = PizzaOrderMaker(flyweight_factory)
    log_proxy = ProxyOrderMaker(pizza_maker)

    shared_states = [
        (30, "Huge pizza"),
        (25, "Medium pizza"),
        (10, "Small pizza"),
    ]
    unique_states = ["Margarita", "Salami", "Four cheese"]

    orders = [
        log_proxy.make_pizza_order(x, y)
        for x in unique_states
        for y in shared_states
    ]
    print("#" * 20)
    print("Amount of made pizzas:", len(orders))
    print("Amount of shared objects:", flyweight_factory.total)
