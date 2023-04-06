from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.orders = {}
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = ""
        for menu in self.menu:
            result += menu.details() + "\n"
        return result[:-1]

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # check if menu is ready
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        # check if client exist
        cleint_exists = False
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                cleint_exists = True
        if not cleint_exists:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)

        # check is meal name exists in menu list
        meals_name_list = [x.name for x in self.menu]
        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in meals_name_list:
                raise Exception(f"{meal_name} is not on the menu!")

        # check the if the quantity of the meal exists. Check for update!
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda x: x.name == meal_name, self.menu))
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda x: x.name == meal_name, self.menu))
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

            if meal_name in client.order:
                client.order[meal_name] += quantity
            else:
                client.order[meal_name] = quantity

        # print(client.order)
        # {'Hummus and Avocado Sandwich': 5, 'Risotto with Wild Mushrooms': 3, 'Chocolate and Violets': 4, 'Tortilla with Beef and Pork': 2}

        shopping_card_meal_names = [meal.name for meal in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(shopping_card_meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        # You will always be given an existing client phone number.
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.order.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += quantity

        client.order = {}
        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        # You will always be given an existing client phone number.
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        total_paid_money = client.bill
        client.order = {}
        client.shopping_cart = []
        client.bill = 0.0

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


