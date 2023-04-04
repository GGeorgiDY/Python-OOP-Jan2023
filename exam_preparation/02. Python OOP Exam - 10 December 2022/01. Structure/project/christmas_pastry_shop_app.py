from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_delicacies = ["Gingerbread", "Stolen"]

        if name in [x.name for x in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in valid_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        # горното може и така
        # if type_delicacy not in self.VALID_DELICACIES:
        #     raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        # create the delicacy
        if type_delicacy == valid_delicacies[0]:
            new_delicacy = Gingerbread(name, price)
            self.delicacies.append(new_delicacy)

        if type_delicacy == valid_delicacies[1]:
            new_delicacy = Stolen(name, price)
            self.delicacies.append(new_delicacy)

        # горните 2 if-a могат да се напишат ето с този ред
        # delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        # self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        # booth = [x for x in self.booths is x.booth_number == booth_number]
        # if booth:
        #     raise Exception(f"Booth number {booth_number} already exists!")
        # може и така

        if booth_number in [x.booth_number for x in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        # create the booth
        # add it to the booths' list
        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        # for booth in self.booths:
        #     if not booth.is_reserved and booth.capacity >= number_of_people:
        #         booth.reserve(number_of_people)
        #         return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        # raise Exception(f"No available booth for {number_of_people} people!")
        # и горното и долното може

        try:
            booth = next(filter(lambda x: x.capacity >= number_of_people and not x.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")
        # и горното и долното може
        # booth = [x for x in self.booths if x.booth_number == booth_number][0]
        # if not booth:
        #     raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        # и горното и долното може
        # delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        # if not delicacy:
        #     raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        # the booth's number will always be valid
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        # booth = [x for x in self.booths if x.booth_number == booth_number][0]

        price_for_all_orders = sum(x.price for x in booth.delicacy_orders)
        bill = booth.price_for_reservation + price_for_all_orders
        self.income += bill

        # booth.delicacy_orders = []
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:" + "\n" f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

