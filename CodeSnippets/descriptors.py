from typing import Union


class DimensionsDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{owner}__{name}'

    def __set__(self, instance, value):
        if instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    a = DimensionsDescriptor()
    b = DimensionsDescriptor()
    c = DimensionsDescriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self):
        return self.a * self.b * self.c

    def __ge__(self, other: 'Dimensions'):
        return self.get_volume() >= other.get_volume()

    def __gt__(self, other: 'Dimensions'):
        return self.get_volume() > other.get_volume()


class ShopItem:

    def __init__(self, name: str, price: Union[int, float], dim: Dimensions):
        self.name = name
        self.price = price
        self.dimensions = dim


if __name__ == '__main__':
    # Tests
    trainers = ShopItem('trainers', 1024, Dimensions(40, 30, 120))
    umbrella = ShopItem('umbrella', 500.24, Dimensions(10, 20, 50))
    fridge = ShopItem('fridge', 40000, Dimensions(2000, 600, 500))
    chair = ShopItem('chair', 2000.99, Dimensions(500, 200, 200))
    lst_shop = (trainers, umbrella, fridge, chair)
    lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dimensions.get_volume())
