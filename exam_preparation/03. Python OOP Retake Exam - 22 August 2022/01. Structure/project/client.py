from typing import List
from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_card: List[Meal] = []
        self.bill: float = 0.0 #represents the total amount of money for all meals that the client has added to his shopping cart
        self.my_dict = {}
        self.only_product_names = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value[0] == 0 or len(value) == 10 or all(ele.isdigit() for ele in value)):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

