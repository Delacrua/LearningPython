from abc import ABC, abstractmethod


class FahrenheitOven(ABC):
    """
    oven interface with Fahrenheit scale
    """

    @abstractmethod
    def get_temperature(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def set_temperature(self, temperature: float) -> None:
        raise NotImplementedError


class CelsiusOven(ABC):
    """
    oven interface with Celsius scale
    """

    @abstractmethod
    def get_celsius_temperature(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def set_celsius_temperature(self, temperature: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_original_temperature(self) -> float:
        raise NotImplementedError


class OriginalOven(FahrenheitOven):
    """
    represents oven that will be adapted to another interface
    """

    def __init__(self, temperature: float):
        assert temperature >= 32  # 0 in Fahrenheit scale
        self.temperature = temperature

    def get_temperature(self) -> float:
        return self.temperature

    def set_temperature(self, temperature: float) -> None:
        assert temperature >= 32
        self.temperature = temperature


class OvenAdapter(CelsiusOven):
    """
    adapter that allows using an oven with Fahrenheit scale while entering
    temperature in Celsius scale
    """

    FAHRENHEIT_TO_CELSIUS: float = 5.0 / 9.0
    CELSIUS_TO_FAHRENHEIT: float = 9.0 / 5.0
    FAHRENHEIT_ZERO: float = 32.0

    def __init__(self, original_oven: FahrenheitOven):
        self.oven = original_oven
        self.temperature = self._init_temperature()

    def get_original_temperature(self) -> float:
        return self.oven.get_temperature()

    def _init_temperature(self):
        return OvenAdapter.FAHRENHEIT_TO_CELSIUS * (
            self.oven.get_temperature() - OvenAdapter.FAHRENHEIT_ZERO
        )

    def get_celsius_temperature(self) -> float:
        return self.temperature

    def set_celsius_temperature(self, temperature: float) -> None:
        temperature_for_oven = (
            OvenAdapter.CELSIUS_TO_FAHRENHEIT * temperature
            + OvenAdapter.FAHRENHEIT_ZERO
        )
        self.oven.set_temperature(temperature_for_oven)
        self.temperature = temperature


if __name__ == "__main__":

    def print_temperature(oven: CelsiusOven):
        print(f"Original temperature = {oven.get_original_temperature()} F")
        print(f"Celsius temperature = {oven.get_celsius_temperature()} C")

    fahrenheit_oven = OriginalOven(50)
    celsius_oven = OvenAdapter(fahrenheit_oven)
    print_temperature(celsius_oven)
    celsius_oven.set_celsius_temperature(180)
    print("-" * 30)
    print("New temperature")
    print("-" * 30)
    print_temperature(celsius_oven)
