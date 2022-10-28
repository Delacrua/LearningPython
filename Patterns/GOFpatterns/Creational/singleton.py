class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self, name: str = "They call me mr.Singleton"):
        self.name = name


if __name__ == "__main__":
    my_singleton1 = MySingleton("Singleton1")
    my_singleton2 = MySingleton("Singleton2")
    print(f"Singleton1 name: {my_singleton1.name}")
    print(f"Singleton2 name: {my_singleton2.name}")
    print(my_singleton1)
    print(my_singleton2)
    print(my_singleton1 is my_singleton2)
