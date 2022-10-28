import concurrent.futures
from itertools import repeat
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonMeta):
    def __init__(self, name: str = "They call me mr.Singleton"):
        self.name = name


class ThreadSafePrinter:
    _lock = Lock()

    @classmethod
    def print_instance_data(cls, instance: MySingleton):
        with cls._lock:
            print(instance.name, instance, id(instance))


def make_instance(name, printer):
    instance = MySingleton(name)
    printer.print_instance_data(instance)


if __name__ == "__main__":
    thread_safe_printer = ThreadSafePrinter()
    names = [f"Singleton" + str(i) for i in range(15)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(make_instance, names, repeat(thread_safe_printer))
