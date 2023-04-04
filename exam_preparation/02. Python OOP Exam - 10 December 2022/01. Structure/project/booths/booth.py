from abc import ABC, abstractmethod
from typing import List
from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number #represents the booth's number.
        self.capacity = capacity #represents the booth's capacity.
        self.delicacy_orders: List[Delicacy] = [] #съдържа списък със всички лакомства в тази сергия
        self.price_for_reservation: float = 0.0 #change when booth is reserved
        self.is_reserved: bool = False #change when booth is reserved

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

