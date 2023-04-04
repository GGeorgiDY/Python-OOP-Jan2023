from typing import List
from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = [] # will contain all the meals (objects)
        self.clients_list: List[Client] = [] # will contain all the clients (objects)
        self.receipt_id = 0

    def __find_client_by_phone_number(self, number):
        for client in self.clients_list:
            if client.phone_number == number:
                return client

    def register_client(self, client_phone_number: str):
        #NB! провери дали създаването на клиента трябва да отиде след проверката
        # Creates a client (object)
        new_client = Client(client_phone_number)

        # checks if a client with the same phone number is already registered
        if len(self.clients_list) > 0:
            numbers_match = [x for x in self.clients_list if x.phone_number == client_phone_number][0]
            if numbers_match:
                raise Exception("The client has already been registered!")

        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        meals_list = ["Starter", "MainDish", "Dessert"]

        #add only the  meals that present in meals_list
        for meal in meals:
            if meal.__class__.__name__ in meals_list:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = ""
        for meal in self.menu:
            result += f"{meal.details()}" + "\n"
        return result[:-1]

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # ако менюто не е готово, върни грешка
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        # ако клиента не се е регистрирал, регистрирай го
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self.__find_client_by_phone_number(client_phone_number)

        # ако храната я нямаме, върни грешка
        meals_to_order = []
        current_bill = 0
        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * quantity

                        meal.quantity -= quantity

                        client.my_dict[meal.name] = quantity
                        client.only_product_names.extend([meal.name])
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")


        # добави храната в списъка с храна на клиента
        client.shopping_card.extend(meals_to_order)
        client.bill += current_bill

        return f"Client {client_phone_number} successfully ordered {', '.join(k for k in client.only_product_names)} for {client.bill}lv."

    def cancel_order(self, client_phone_number: str):
        client = [x for x in self.clients_list if x.phone_number == client_phone_number][0]
        if len(client.shopping_card) == 0:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.my_dict.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.name += quantity

        client.my_dict = {}
        client.bill = 0
        client.shopping_card = []
        client.only_product_names = []
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = [x for x in self.clients_list if x.phone_number == client_phone_number][0]
        if len(client.shopping_card) == 0:
            raise Exception("There are no ordered meals!")

        client.shopping_cart = []
        client.only_product_names = []
        paid_bill = client.bill
        client.bill = 0
        self.receipt_id += 1
        client.ordered_meals = {}
        return f"Receipt #{self.receipt_id} with total amount of {paid_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."













