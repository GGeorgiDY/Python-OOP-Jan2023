from abc import ABC, abstractclassmethod, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass
    
    @property
    @abstractmethod
    def type(self):
        pass
    

    # валидираме данните, които ще получаваме за manufacturer
    @property
    def manufacturer(self):
        return self.__processor

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '': #изрязваме всичко спейсове от ляво и от дясно
            raise ValueError("Manufacturer name cannot be empty.")
        self.__processor = value

    # валидираме данните, които ще получаваме за model
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return ceil(result) == floor(result)

    # тук преспокойно можем да го направим абстрактен клас, но понеже има много логика която се преповтавя, ние ще
    # използваме наследяване на класа. Така кода ще стане по-чист
    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if not self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def set_parts(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"